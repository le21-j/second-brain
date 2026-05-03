"""Claude Agent SDK wrapper.

Wraps `ClaudeSDKClient` for a long-running, multi-turn Socratic chat session.
Auth is taken from the `CLAUDE_CODE_OAUTH_TOKEN` env var that
`claude setup-token` produces.
"""

from __future__ import annotations

import asyncio
import os
from collections.abc import AsyncIterator
from pathlib import Path

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    StreamEvent,
    TextBlock,
)

from .wiki import build_context, get_wiki_root


class AuthError(RuntimeError):
    pass


def _check_auth() -> None:
    if os.environ.get("CLAUDE_CODE_OAUTH_TOKEN"):
        return
    if os.environ.get("ANTHROPIC_API_KEY"):
        return
    raise AuthError(
        "No auth found. Run `claude setup-token` and add the printed token "
        "to your shell rc as CLAUDE_CODE_OAUTH_TOKEN."
    )


def _read_or_warn(path: Path, label: str) -> str:
    if not path.exists():
        return f"[{label} not found at {path}]"
    return path.read_text(encoding="utf-8")


def find_agent_path(agent_name: str, wiki_root: Path) -> Path:
    """Project scope wins over user scope (per project CLAUDE.md)."""
    project = wiki_root / ".claude" / "agents" / f"{agent_name}.md"
    if project.exists():
        return project
    return Path.home() / ".claude" / "agents" / f"{agent_name}.md"


def list_available_agents(wiki_root: Path) -> list[str]:
    seen: set[str] = set()
    for d in (
        wiki_root / ".claude" / "agents",
        Path.home() / ".claude" / "agents",
    ):
        if not d.exists():
            continue
        for p in d.glob("*.md"):
            seen.add(p.stem)
    return sorted(seen)


def load_system_prompt(wiki_root: Path, agent_name: str = "teacher") -> str:
    persona_path = find_agent_path(agent_name, wiki_root)
    persona = _read_or_warn(persona_path, f"{agent_name}.md")
    schema = _read_or_warn(wiki_root / "CLAUDE.md", "CLAUDE.md")
    return f"{persona}\n\n---\n\n{schema}"


class LLMSession:
    def __init__(
        self,
        model: str = "claude-sonnet-4-6",
        agent_name: str = "teacher",
    ) -> None:
        _check_auth()
        self.wiki_root = get_wiki_root()
        self.model = model
        self.agent_name = agent_name
        self.system_prompt = load_system_prompt(self.wiki_root, self.agent_name)
        self._client: ClaudeSDKClient | None = None

    def _refresh_system_prompt(self) -> None:
        self.system_prompt = load_system_prompt(self.wiki_root, self.agent_name)

    async def reconfigure(
        self,
        model: str | None = None,
        agent_name: str | None = None,
    ) -> None:
        changed = False
        if model and model != self.model:
            self.model = model
            changed = True
        if agent_name and agent_name != self.agent_name:
            self.agent_name = agent_name
            self._refresh_system_prompt()
            changed = True
        if changed:
            await self.reset()

    async def __aenter__(self) -> "LLMSession":
        await self.connect()
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.disconnect()

    async def connect(self) -> None:
        options = ClaudeAgentOptions(
            system_prompt=self.system_prompt,
            model=self.model,
            allowed_tools=[],
            setting_sources=[],
            include_partial_messages=True,
            max_turns=1,
        )
        self._client = ClaudeSDKClient(options=options)
        await self._client.connect()

    async def disconnect(self) -> None:
        if self._client is None:
            return
        await self._client.disconnect()
        self._client = None

    async def reset(self) -> None:
        await self.disconnect()
        await self.connect()

    async def chat(self, user_message: str) -> AsyncIterator[str]:
        if self._client is None:
            raise RuntimeError("LLMSession not connected. Use `async with` or call connect().")
        context = await asyncio.to_thread(build_context, user_message, self.wiki_root)
        framed = (
            f"[WIKI CONTEXT — sourced from [[index.md]]]\n"
            f"{context}\n"
            f"[END WIKI CONTEXT]\n\n"
            f"{user_message}"
        )
        await self._client.query(framed)
        stream = self._client.receive_response()
        streamed_any = False
        try:
            while True:
                try:
                    async with asyncio.timeout(60):
                        message = await anext(stream)
                except StopAsyncIteration:
                    break
                except TimeoutError as e:
                    raise TimeoutError("LLM stream idle for 60s — aborting.") from e
                if isinstance(message, AssistantMessage) and streamed_any:
                    # Final summary message; tokens already arrived via StreamEvents.
                    continue
                for chunk in self._extract_text(message):
                    streamed_any = True
                    yield chunk
        finally:
            aclose = getattr(stream, "aclose", None)
            if callable(aclose):
                await aclose()

    @staticmethod
    def _extract_text(message: object) -> list[str]:
        match message:
            case AssistantMessage(content=blocks):
                return [b.text for b in blocks if isinstance(b, TextBlock)]
            case StreamEvent():
                return LLMSession._extract_stream_text(message)
            case ResultMessage():
                return []
            case _:
                return []

    @staticmethod
    def _extract_stream_text(event: StreamEvent) -> list[str]:
        sentinel = object()
        data: object = getattr(event, "event", sentinel)
        if data is sentinel:
            data = getattr(event, "data", {})
        if not isinstance(data, dict):
            return []
        delta = data.get("delta")
        if not isinstance(delta, dict):
            return []
        text = delta.get("text")
        return [text] if isinstance(text, str) else []
