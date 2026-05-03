"""Local web UI for Jayden's Socratic teacher agent.

Loads the same system prompt as Claude Code's /teacher (from ~/.claude/agents/teacher.md)
and serves it over HTTP with prompt caching so repeated turns stay cheap.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Literal

from anthropic import Anthropic
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

ROOT = Path(__file__).parent
load_dotenv(ROOT / ".env")

TEACHER_AGENT_PATH = Path.home() / ".claude" / "agents" / "teacher.md"
DEFAULT_FALLBACK_PROMPT = (
    "You are a Socratic AI tutor. Refuse to give direct answers; ask one leading question at a time, "
    "calibrated to the student's level. Use Markdown and LaTeX freely."
)

ALLOWED_MODELS = {
    "claude-sonnet-4-6",
    "claude-opus-4-7",
    "claude-haiku-4-5-20251001",
}


def load_teacher_prompt() -> str:
    if not TEACHER_AGENT_PATH.exists():
        return DEFAULT_FALLBACK_PROMPT
    text = TEACHER_AGENT_PATH.read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].strip()
    return text


TEACHER_PROMPT = load_teacher_prompt()
client = Anthropic()

app = FastAPI(title="Teacher", description="Socratic tutor web UI")


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]
    model: str = "claude-sonnet-4-6"
    max_tokens: int = 4096


@app.post("/api/chat")
async def chat(req: ChatRequest):
    if req.model not in ALLOWED_MODELS:
        raise HTTPException(status_code=400, detail=f"Model {req.model!r} not allowed.")
    if not req.messages:
        raise HTTPException(status_code=400, detail="At least one message required.")

    try:
        msg = client.messages.create(
            model=req.model,
            max_tokens=req.max_tokens,
            system=[
                {
                    "type": "text",
                    "text": TEACHER_PROMPT,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": m.role, "content": m.content} for m in req.messages],
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Anthropic API error: {e}") from e

    text = "".join(b.text for b in msg.content if b.type == "text")
    usage = msg.usage
    return {
        "role": "assistant",
        "content": text,
        "model": msg.model,
        "stop_reason": msg.stop_reason,
        "usage": {
            "input_tokens": usage.input_tokens,
            "output_tokens": usage.output_tokens,
            "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", 0) or 0,
            "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", 0) or 0,
        },
    }


@app.get("/api/health")
async def health():
    return {
        "ok": True,
        "teacher_prompt_loaded": bool(TEACHER_PROMPT),
        "teacher_prompt_chars": len(TEACHER_PROMPT),
        "teacher_prompt_source": str(TEACHER_AGENT_PATH) if TEACHER_AGENT_PATH.exists() else "fallback",
        "models": sorted(ALLOWED_MODELS),
    }


# Static frontend last so the API routes win.
app.mount("/", StaticFiles(directory=str(ROOT / "static"), html=True), name="static")


def main():
    import uvicorn

    if not os.getenv("ANTHROPIC_API_KEY"):
        raise SystemExit(
            "ANTHROPIC_API_KEY not set. Copy .env.example to .env and add your key."
        )
    uvicorn.run(
        "server:app",
        host="127.0.0.1",
        port=int(os.getenv("PORT", "8765")),
        reload=bool(os.getenv("RELOAD")),
    )


if __name__ == "__main__":
    main()
