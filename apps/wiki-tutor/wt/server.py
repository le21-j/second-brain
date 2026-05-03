"""FastAPI web server — the default UI mode for `wt`.

Serves a single-page app with MathJax + Marked.js + Tailwind for pixel-accurate
rendering of the wiki (matching Obsidian's appearance). WebSocket streams chat
turns from the Claude Agent SDK.
"""

from __future__ import annotations

import asyncio
import datetime as dt
import re
import socket
import sys
import webbrowser
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel

from .constants import (
    DEFAULT_VAULT_NAME,
    MAX_PRACTICE_SETS_PER_TOPIC,
    TOPIC_RE,
)
from .llm import AuthError, LLMSession, list_available_agents
from .wiki import (
    MAX_INLINE_PAGE_BYTES,
    WikiRootError,
    get_wiki_root,
    read_page,
    search_index,
    strip_frontmatter,
)


WEB_DIR = Path(__file__).parent / "web"


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _today() -> str:
    return dt.date.today().isoformat()


def _next_set_number(practice_dir: Path, topic: str) -> int:
    pattern = re.compile(rf"^{re.escape(topic)}-set-(\d+)\.md$")
    nums: list[int] = []
    if practice_dir.exists():
        for p in practice_dir.iterdir():
            m = pattern.match(p.name)
            if m:
                nums.append(int(m.group(1)))
    return (max(nums) + 1) if nums else 1


class SaveRequest(BaseModel):
    topic: str
    transcript: str


class MistakeRequest(BaseModel):
    topic: str
    transcript: str


class NoteRequest(BaseModel):
    slug: str
    title: str
    content: str


class LatexConvertRequest(BaseModel):
    text: str
    mode: str = "inline"  # "inline" or "display"


class SessionPayload(BaseModel):
    date: str
    chat: list = []
    pins: list = []
    research: list = []
    notes: list = []


DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


LATEX_CONVERTER_PROMPT = """You convert natural-language descriptions of math, plain-ASCII math, or messy mixed prose into clean LaTeX.

Rules:
- Output ONLY the converted LaTeX. No commentary, no preamble, no explanation, no quotation marks.
- Inline math is wrapped in $...$. Display math is wrapped in $$...$$.
- Use proper LaTeX commands: \\frac, \\partial, \\sqrt, \\sum, \\int, \\prod, \\lim, \\nabla, etc.
- Greek letters: \\alpha, \\beta, \\gamma, \\omega, \\mu, \\pi, \\lambda, \\sigma, \\theta, \\eta, \\Phi, \\Psi.
- Operators: \\cdot, \\leq, \\geq, \\neq, \\approx, \\propto, \\pm, \\in, \\to, \\mapsto, \\otimes.
- Vectors: \\vec{x}; matrices: \\mathbf{H}; sets: \\mathbb{R}; cal: \\mathcal{L}.
- If the user requests display mode, prefer $$...$$ even for short equations.
- If the input is already valid LaTeX, return it unchanged.
- If the input has no math content (pure prose), return the input unchanged.

Examples:
- Input: "gradient of L with respect to W"  →  $\\nabla_W L$
- Input: "partial L over partial W"  →  $\\frac{\\partial L}{\\partial W}$
- Input: "1 over N times sum from i=1 to N of x_i squared"  →  $\\frac{1}{N}\\sum_{i=1}^{N} x_i^2$
- Input: "alpha squared plus 2 alpha beta plus beta squared"  →  $\\alpha^2 + 2\\alpha\\beta + \\beta^2$
- Input: "hat y equals W times x plus b"  →  $\\hat{y} = W x + b$
- Input: "BLER less than or equal to 10^-2"  →  $\\text{BLER} \\leq 10^{-2}$
"""


SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,80}$")


def create_app(model: str) -> FastAPI:
    app = FastAPI(title="wiki-tutor")

    @app.get("/", response_class=HTMLResponse)
    async def index() -> HTMLResponse:
        html = (WEB_DIR / "index.html").read_text(encoding="utf-8")
        return HTMLResponse(html)

    @app.get("/api/config")
    async def config() -> dict:
        wiki_root = get_wiki_root()
        return {
            "models": [
                {"id": "claude-sonnet-4-6", "label": "Sonnet 4.6"},
                {"id": "claude-opus-4-7", "label": "Opus 4.7 (1M ctx)"},
                {"id": "claude-haiku-4-5-20251001", "label": "Haiku 4.5"},
            ],
            "agents": list_available_agents(wiki_root),
            "default_model": model,
            "default_agent": "teacher",
        }

    @app.get("/api/search")
    async def search(q: str = "") -> dict:
        if not q.strip():
            return {"results": []}
        results = await asyncio.to_thread(search_index, q)
        return {"results": [{"stem": s, "desc": d, "score": sc} for s, d, sc in results]}

    @app.get("/api/page/{stem}")
    async def page(stem: str) -> JSONResponse:
        body = await asyncio.to_thread(read_page, stem, None, MAX_INLINE_PAGE_BYTES)
        if body is None:
            return JSONResponse({"error": "not found or too large"}, status_code=404)
        return JSONResponse({"stem": stem, "content": strip_frontmatter(body)})

    @app.post("/api/save/practice")
    async def save_practice(req: SaveRequest) -> JSONResponse:
        if not TOPIC_RE.match(req.topic):
            return JSONResponse({"error": "invalid topic"}, status_code=400)
        wiki_root = get_wiki_root()
        practice_dir = wiki_root / "wiki" / "practice"
        practice_dir.mkdir(parents=True, exist_ok=True)
        n = _next_set_number(practice_dir, req.topic)
        while n < MAX_PRACTICE_SETS_PER_TOPIC:
            path = practice_dir / f"{req.topic}-set-{n:02d}.md"
            try:
                with path.open("x", encoding="utf-8") as f:
                    f.write(_practice_body(req.topic, n, req.transcript))
                _append_log(
                    wiki_root,
                    f"## [{_today()}] practice | {req.topic}-set-{n:02d} (written by wt-web)",
                )
                return JSONResponse({"path": str(path), "n": n})
            except FileExistsError:
                n += 1
        return JSONResponse({"error": "too many sets"}, status_code=409)

    @app.post("/api/save/mistake")
    async def save_mistake(req: MistakeRequest) -> JSONResponse:
        if not TOPIC_RE.match(req.topic):
            return JSONResponse({"error": "invalid topic"}, status_code=400)
        wiki_root = get_wiki_root()
        mistakes_dir = wiki_root / "wiki" / "mistakes"
        mistakes_dir.mkdir(parents=True, exist_ok=True)
        path = mistakes_dir / f"{req.topic}.md"
        if path.exists():
            existing = path.read_text(encoding="utf-8")
            entry = f"\n- `{_today()}` — *Logged from wt-web session.*\n\n{req.transcript}\n"
            marker = "## Jayden's personal log"
            updated = existing.replace(marker, f"{marker}{entry}", 1) if marker in existing else f"{existing}\n\n{marker}\n{entry}"
            path.write_text(updated, encoding="utf-8")
        else:
            path.write_text(_mistake_body(req.topic, req.transcript), encoding="utf-8")
        _append_log(
            wiki_root,
            f"## [{_today()}] practice | mistake log update: {req.topic} (written by wt-web)",
        )
        return JSONResponse({"path": str(path)})

    @app.get("/api/notes")
    async def list_notes() -> dict:
        wiki_root = get_wiki_root()
        notes_dir = wiki_root / "wiki" / "notes"
        if not notes_dir.exists():
            return {"notes": []}
        notes: list[dict] = []
        for p in sorted(notes_dir.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True):
            title = p.stem
            try:
                text = p.read_text(encoding="utf-8")
                fm = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
                if fm:
                    fm_title = re.search(r"^title:\s*(.+)$", fm.group(1), re.MULTILINE)
                    if fm_title:
                        title = fm_title.group(1).strip().strip('"').strip("'")
                    text = text[fm.end():]
                heading = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
                if heading and title == p.stem:
                    title = heading.group(1).strip()
            except OSError:
                pass
            notes.append({
                "slug": p.stem,
                "title": title,
                "updated": p.stat().st_mtime,
            })
        return {"notes": notes}

    @app.post("/api/notes")
    async def save_note(req: NoteRequest) -> JSONResponse:
        if not SLUG_RE.match(req.slug):
            return JSONResponse({"error": "invalid slug"}, status_code=400)
        wiki_root = get_wiki_root()
        notes_dir = wiki_root / "wiki" / "notes"
        notes_dir.mkdir(parents=True, exist_ok=True)
        path = notes_dir / f"{req.slug}.md"
        is_new = not path.exists()
        if is_new:
            today = _today()
            body = (
                f"---\n"
                f"title: {req.title}\n"
                f"type: note\n"
                f"tags: [note, wt-web]\n"
                f"created: {today}\n"
                f"updated: {today}\n"
                f"---\n\n"
                f"# {req.title}\n\n"
                f"{req.content}\n"
            )
        else:
            existing = path.read_text(encoding="utf-8")
            updated_body = re.sub(r"^updated: .*$", f"updated: {_today()}", existing, count=1, flags=re.MULTILINE)
            # split frontmatter and body, replace body
            if updated_body.startswith("---\n"):
                end = updated_body.find("\n---\n", 4)
                frontmatter = updated_body[: end + 5] if end > 0 else ""
                body = f"{frontmatter}\n# {req.title}\n\n{req.content}\n"
            else:
                body = f"# {req.title}\n\n{req.content}\n"
        path.write_text(body, encoding="utf-8")
        return JSONResponse({"slug": req.slug, "path": str(path), "new": is_new})

    @app.post("/api/convert-latex")
    async def convert_latex(req: LatexConvertRequest) -> JSONResponse:
        from claude_agent_sdk import (
            AssistantMessage,
            ClaudeAgentOptions,
            TextBlock,
            query,
        )

        text = req.text.strip()
        if not text:
            return JSONResponse({"latex": ""})
        prompt_suffix = "\n\n(Use display mode $$...$$.)" if req.mode == "display" else ""
        options = ClaudeAgentOptions(
            system_prompt=LATEX_CONVERTER_PROMPT,
            model="claude-haiku-4-5-20251001",
            allowed_tools=[],
            setting_sources=[],
            max_turns=1,
        )
        out: list[str] = []
        try:
            async for message in query(
                prompt=f"Convert to LaTeX:\n\n{text}{prompt_suffix}",
                options=options,
            ):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            out.append(block.text)
        except Exception as e:  # noqa: BLE001
            return JSONResponse({"error": str(e)}, status_code=500)
        latex = "".join(out).strip()
        # safeguard: strip stray code fences if model wrapped output
        if latex.startswith("```") and latex.endswith("```"):
            latex = re.sub(r"^```[a-z]*\n?", "", latex)
            latex = re.sub(r"\n?```$", "", latex)
        return JSONResponse({"latex": latex})

    @app.get("/api/sessions")
    async def list_sessions() -> dict:
        wiki_root = get_wiki_root()
        sessions_dir = wiki_root / ".wt" / "sessions"
        if not sessions_dir.exists():
            return {"sessions": []}
        items: list[dict] = []
        for p in sorted(sessions_dir.glob("*.json"), reverse=True):
            if not DATE_RE.match(p.stem):
                continue
            try:
                import json as _json
                data = _json.loads(p.read_text(encoding="utf-8"))
                items.append({
                    "date": p.stem,
                    "chat_turns": len(data.get("chat", [])),
                    "pin_count": len(data.get("pins", [])),
                    "research_count": len(data.get("research", [])),
                    "modified": p.stat().st_mtime,
                })
            except Exception:  # noqa: BLE001
                continue
        return {"sessions": items}

    @app.get("/api/sessions/{date}")
    async def get_session(date: str) -> JSONResponse:
        if not DATE_RE.match(date):
            return JSONResponse({"error": "invalid date"}, status_code=400)
        wiki_root = get_wiki_root()
        path = wiki_root / ".wt" / "sessions" / f"{date}.json"
        if not path.exists():
            return JSONResponse({"date": date, "chat": [], "pins": [], "research": [], "notes": []})
        try:
            import json as _json
            data = _json.loads(path.read_text(encoding="utf-8"))
            return JSONResponse(data)
        except Exception as e:  # noqa: BLE001
            return JSONResponse({"error": str(e)}, status_code=500)

    @app.post("/api/sessions/{date}")
    async def save_session(date: str, payload: SessionPayload) -> JSONResponse:
        if not DATE_RE.match(date):
            return JSONResponse({"error": "invalid date"}, status_code=400)
        wiki_root = get_wiki_root()
        sessions_dir = wiki_root / ".wt" / "sessions"
        sessions_dir.mkdir(parents=True, exist_ok=True)
        path = sessions_dir / f"{date}.json"
        import json as _json
        body = payload.model_dump()
        body["lastModified"] = dt.datetime.now().timestamp()
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(_json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp.replace(path)
        return JSONResponse({"date": date, "saved": True})

    @app.delete("/api/notes/{slug}")
    async def delete_note(slug: str) -> JSONResponse:
        if not SLUG_RE.match(slug):
            return JSONResponse({"error": "invalid slug"}, status_code=400)
        wiki_root = get_wiki_root()
        path = wiki_root / "wiki" / "notes" / f"{slug}.md"
        if not path.exists():
            return JSONResponse({"error": "not found"}, status_code=404)
        path.unlink()
        return JSONResponse({"deleted": slug})

    @app.websocket("/ws/chat")
    async def ws_chat(ws: WebSocket) -> None:
        await ws.accept()
        session: LLMSession | None = None
        try:
            session = LLMSession(model=model, agent_name="teacher")
            await session.connect()
            await ws.send_json(
                {"type": "ready", "model": session.model, "agent": session.agent_name}
            )
            while True:
                data = await ws.receive_json()
                kind = data.get("type", "message")
                if kind == "reset":
                    await session.reset()
                    await ws.send_json({"type": "reset_done"})
                    continue
                if kind == "reconfigure":
                    await session.reconfigure(
                        model=data.get("model"),
                        agent_name=data.get("agent"),
                    )
                    await ws.send_json(
                        {
                            "type": "reconfigured",
                            "model": session.model,
                            "agent": session.agent_name,
                        }
                    )
                    continue
                user_msg = (data.get("message") or "").strip()
                if not user_msg:
                    continue
                try:
                    async for chunk in session.chat(user_msg):
                        await ws.send_json({"type": "chunk", "text": chunk})
                    await ws.send_json({"type": "done"})
                except Exception as e:  # noqa: BLE001
                    await ws.send_json({"type": "error", "message": str(e)})
        except WebSocketDisconnect:
            pass
        except AuthError as e:
            await ws.send_json({"type": "error", "message": str(e)})
            await ws.close()
        finally:
            if session is not None:
                await session.disconnect()

    return app


def _practice_body(topic: str, n: int, transcript: str) -> str:
    title = topic.replace("-", " ").title()
    today = _today()
    return (
        f"---\n"
        f'title: "{title} — Practice Set {n:02d}"\n'
        f"type: practice\n"
        f"course: []\n"
        f"tags: [practice, {topic}]\n"
        f"concept: []\n"
        f"difficulty: mixed\n"
        f"created: {today}\n"
        f"updated: {today}\n"
        f"---\n\n"
        f"# {title} — Practice Set {n:02d}\n\n"
        f"> Saved by wt-web on {today} from a live tutoring session.\n\n"
        f"## Conversation transcript\n\n"
        f"{transcript}\n\n"
        f"## Jayden's attempts\n\n"
        f"- `{today}` — initial session.\n"
    )


def _mistake_body(topic: str, transcript: str) -> str:
    title = topic.replace("-", " ").title()
    today = _today()
    return (
        f"---\n"
        f"title: {title} — Mistakes\n"
        f"type: mistake\n"
        f"course: []\n"
        f"tags: [mistakes, {topic}]\n"
        f"concept: []\n"
        f"created: {today}\n"
        f"updated: {today}\n"
        f"---\n\n"
        f"# {title} — Common Mistakes\n\n"
        f"## Known gotchas (general)\n\n"
        f"- *(populate from session)*\n\n"
        f"## Jayden's personal log\n\n"
        f"- `{today}` — *Logged from wt-web session.*\n\n"
        f"{transcript}\n"
    )


def _append_log(wiki_root: Path, line: str) -> None:
    log_path = wiki_root / "log.md"
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
    sep = "" if existing.endswith("\n\n") else ("\n" if existing.endswith("\n") else "\n\n")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"{sep}{line}\n")


def run_web(
    model: str = "claude-sonnet-4-6",
    port: int = 0,
    open_browser: bool = True,
    vault: str | None = None,
) -> None:
    import uvicorn

    try:
        wiki_root = get_wiki_root()
    except WikiRootError as e:
        print(f"[wt] {e}", file=sys.stderr)
        sys.exit(1)
    chosen_port = port or _free_port()
    url = f"http://127.0.0.1:{chosen_port}"
    print(f"wt-web serving on {url}")
    print(f"wiki: {wiki_root}")
    print(f"model: {model}")
    if open_browser:
        webbrowser.open(url)
    app = create_app(model=model)
    if vault:
        app.state.vault = vault
    else:
        app.state.vault = DEFAULT_VAULT_NAME
    uvicorn.run(app, host="127.0.0.1", port=chosen_port, log_level="warning")
