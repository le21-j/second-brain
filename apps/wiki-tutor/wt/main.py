"""Textual app shell — `wt` command entry point.

Workspace layout:
- Left: dockable Wiki sidebar (search + result list).
- Center: tabbed workspace (Chat + opened wiki pages).
- Right: dockable Pinboard (notes + pinned questions).
- Bottom: input bar (always routes to the chat session).
"""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import os
import re
import subprocess
import sys
from pathlib import Path

from rich.markup import escape as escape_markup
from rich.text import Text
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.css.query import NoMatches
from textual.widgets import (
    Footer,
    Header,
    Input,
    Label,
    ListItem,
    ListView,
    Markdown,
    Static,
    TabbedContent,
    TabPane,
)

from .constants import (
    DEFAULT_VAULT_NAME,
    MAX_AUTO_OPEN_PER_RESPONSE,
    MAX_PRACTICE_SETS_PER_TOPIC,
    TAB_ID_CHAT,
    TAB_ID_SAFE_RE,
    TOPIC_RE,
)
from .llm import AuthError, LLMSession
from .render import WIKILINK_RE, obsidian_url, render
from .wiki import (
    MAX_INLINE_PAGE_BYTES,
    WikiRootError,
    get_wiki_root,
    read_page,
    resolve_stem,
    search_index,
    strip_frontmatter,
)


RENDER_THROTTLE_CHARS = 96


def _validate_topic(topic: str) -> str | None:
    if TOPIC_RE.match(topic):
        return None
    return (
        f"Invalid topic '{topic}'. Use lowercase letters, digits, and hyphens "
        "only (1-64 chars, starting with a letter or digit)."
    )


def _spawn_detached(args: list[str]) -> None:
    subprocess.Popen(  # noqa: S603 — args are constants + quoted URLs
        args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )


HELP_TEXT = """\
**Slash commands**

| Command | Description |
|---|---|
| `/wiki <query>` | Search and populate the left sidebar |
| `/open <stem>` | Open page inline as a new tab |
| `/obsidian <stem>` | Open page in the external Obsidian app |
| `/pin <text>` | Pin text to the right Pinboard |
| `/unpin <n>` | Remove pin number n |
| `/save <topic>` | Save conversation as `wiki/practice/<topic>-set-NN.md` |
| `/mistake <topic>` | Append misconception to `wiki/mistakes/<topic>.md` |
| `/reset` | Clear conversation history |
| `/help` | Show this list |

**Keyboard**

| Key | Action |
|---|---|
| `Ctrl+B` | Toggle wiki sidebar |
| `Ctrl+P` | Toggle pinboard |
| `Ctrl+T` | New chat-focus (next tab) |
| `Ctrl+W` | Close current wiki tab |
| `Ctrl+L` | Reset conversation |
| `Ctrl+C` | Quit |
"""


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
        f"> Saved by `wt` on {today} from a live tutoring session.\n\n"
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
        f"- `{today}` — *Logged from `wt` session.*\n\n"
        f"{transcript}\n"
    )


def _exclusive_practice_path(
    practice_dir: Path, topic: str, transcript: str
) -> tuple[Path, int]:
    n = _next_set_number(practice_dir, topic)
    while n < MAX_PRACTICE_SETS_PER_TOPIC:
        path = practice_dir / f"{topic}-set-{n:02d}.md"
        try:
            with path.open("x", encoding="utf-8") as f:
                f.write(_practice_body(topic, n, transcript))
            return path, n
        except FileExistsError:
            n += 1
    raise RuntimeError(f"Too many practice sets for topic '{topic}' (>={MAX_PRACTICE_SETS_PER_TOPIC}).")


def _write_mistake(mistakes_dir: Path, topic: str, transcript: str) -> Path:
    path = mistakes_dir / f"{topic}.md"
    if not path.exists():
        path.write_text(_mistake_body(topic, transcript), encoding="utf-8")
        return path
    existing = path.read_text(encoding="utf-8")
    entry = f"\n- `{_today()}` — *Logged from `wt` session.*\n\n{transcript}\n"
    marker = "## Jayden's personal log"
    if marker in existing:
        updated = existing.replace(marker, f"{marker}{entry}", 1)
    else:
        updated = f"{existing}\n\n{marker}\n{entry}"
    path.write_text(updated, encoding="utf-8")
    return path


class ChatTurn(Markdown):
    def __init__(self, role: str, body: str = "") -> None:
        super().__init__(body)
        self.role = role
        self._buffer = body
        self._last_rendered = len(body)

    def append_chunk(self, chunk: str) -> None:
        self._buffer += chunk
        if len(self._buffer) - self._last_rendered >= RENDER_THROTTLE_CHARS:
            self.flush()

    def flush(self) -> None:
        self.update(self._buffer)
        self._last_rendered = len(self._buffer)

    @property
    def body(self) -> str:
        return self._buffer


class ChatPane(VerticalScroll):
    def __init__(self) -> None:
        super().__init__(id="chat-pane")

    def add_turn(self, role: str, body: str) -> ChatTurn:
        turn = ChatTurn(role=role, body=body)
        turn.add_class(role)
        self.mount(turn)
        self.scroll_end(animate=False)
        return turn

    def add_system_message(self, text: str) -> None:
        widget = Static(Text(text, style="dim italic"))
        widget.add_class("system")
        self.mount(widget)
        self.scroll_end(animate=False)

    def clear(self) -> None:
        for child in list(self.children):
            child.remove()

    def transcript(self) -> str:
        parts: list[str] = []
        for child in self.children:
            if isinstance(child, ChatTurn):
                parts.append(f"### {child.role.title()}\n\n{child.body}\n")
        return "\n".join(parts)


class WikiSidebar(Vertical):
    def __init__(self) -> None:
        super().__init__(id="wiki-sidebar")

    def compose(self) -> ComposeResult:
        yield Label("📚 Wiki", classes="sidebar-title")
        yield Input(placeholder="search index…", id="wiki-search")
        yield Label("Results", classes="sidebar-section")
        yield ListView(id="wiki-results")

    def populate(self, results: list[tuple[str, str, int]]) -> None:
        view = self.query_one("#wiki-results", ListView)
        view.clear()
        for stem, desc, score in results:
            shown = desc[:60] + "…" if len(desc) > 60 else desc
            label = Label(f"[bold]{stem}[/]\n[dim]{shown or '(no description)'}[/]")
            item = ListItem(label)
            item.data = stem  # type: ignore[attr-defined]
            view.append(item)


class Pinboard(Vertical):
    def __init__(self) -> None:
        super().__init__(id="pinboard")
        self._pins: list[str] = []

    def compose(self) -> ComposeResult:
        yield Label("📌 Pinboard", classes="sidebar-title")
        yield Input(placeholder="pin a thought…", id="pin-input")
        yield Label("Pinned", classes="sidebar-section")
        yield ListView(id="pin-list")

    def add_pin(self, text: str) -> int:
        self._pins.append(text)
        view = self.query_one("#pin-list", ListView)
        n = len(self._pins)
        item = ListItem(Label(f"[bold]{n}.[/] {escape_markup(text)}"))
        item.data = n  # type: ignore[attr-defined]
        view.append(item)
        return n

    def remove_pin(self, n: int) -> bool:
        if n < 1 or n > len(self._pins):
            return False
        self._pins.pop(n - 1)
        view = self.query_one("#pin-list", ListView)
        view.clear()
        for i, text in enumerate(self._pins, start=1):
            item = ListItem(Label(f"[bold]{i}.[/] {escape_markup(text)}"))
            item.data = i  # type: ignore[attr-defined]
            view.append(item)
        return True

    def get_pin(self, n: int) -> str | None:
        if n < 1 or n > len(self._pins):
            return None
        return self._pins[n - 1]


class WikiTutorApp(App):
    CSS = """
    Screen { layout: vertical; }

    Header { dock: top; }
    Footer { dock: bottom; }
    Input#prompt { dock: bottom; }

    #workspace-row { height: 1fr; layout: horizontal; }

    #wiki-sidebar {
        width: 32;
        border-right: solid $accent;
        padding: 1 1;
        background: $boost;
    }
    #pinboard {
        width: 32;
        border-left: solid $accent;
        padding: 1 1;
        background: $boost;
    }
    #wiki-sidebar.hidden, #pinboard.hidden { display: none; }

    .sidebar-title { color: $accent; text-style: bold; padding: 0 0 1 0; }
    .sidebar-section { color: $text-muted; padding: 1 0 0 0; }

    #workspace { width: 1fr; }

    #chat-pane { height: 1fr; padding: 0 1; }

    ChatTurn.user { background: $boost; padding: 0 1; margin: 0 0 1 0; }
    ChatTurn.assistant { padding: 0 1; margin: 0 0 1 0; }
    .system { color: $text-muted; padding: 0 1; }

    TabPane { padding: 0 1; }
    """
    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", priority=True),
        Binding("ctrl+l", "reset_session", "Reset chat"),
        Binding("ctrl+b", "toggle_wiki_sidebar", "Wiki ◀"),
        Binding("ctrl+p", "toggle_pinboard", "Pinboard ▶"),
        Binding("ctrl+t", "next_tab", "Next tab"),
        Binding("ctrl+w", "close_current_tab", "Close tab"),
    ]

    def __init__(self, model: str, obsidian_open: bool, vault: str) -> None:
        super().__init__()
        self.model = model
        self.obsidian_open = obsidian_open
        self.vault = vault
        self.session: LLMSession | None = None
        self._session_ready = False
        self._busy = False
        self._stream_task: asyncio.Task[None] | None = None
        self._stem_cache: dict[str, Path | None] = {}

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with Horizontal(id="workspace-row"):
            yield WikiSidebar()
            with Vertical(id="workspace"):
                with TabbedContent(id="tabs"):
                    with TabPane("Chat ✦", id=TAB_ID_CHAT):
                        yield ChatPane()
            yield Pinboard()
        yield Input(placeholder="Ask the tutor or type / for commands", id="prompt")
        yield Footer()

    async def on_mount(self) -> None:
        self.title = "wiki-tutor"
        try:
            wiki_root = get_wiki_root()
        except WikiRootError as e:
            self._sys(f"[wiki error] {e}")
            self.exit(return_code=1)
            return
        try:
            self.session = LLMSession(model=self.model)
            await self.session.connect()
        except AuthError as e:
            self._sys(f"[auth error] {e}")
            self.exit(return_code=1)
            return
        self.sub_title = str(wiki_root)
        self._sys(
            f"wiki-tutor loaded. Wiki: {wiki_root}. "
            "Use the left sidebar to search, the right pinboard to capture thoughts. "
            "Type /help for commands."
        )
        self.query_one("#prompt", Input).focus()
        await asyncio.to_thread(self._prewarm_stem_cache, wiki_root)
        self._session_ready = True

    def _prewarm_stem_cache(self, wiki_root: Path) -> None:
        for path in (wiki_root / "wiki").rglob("*.md"):
            self._stem_cache.setdefault(path.stem, path)

    def _resolve_stem_cached(self, stem: str) -> Path | None:
        if stem not in self._stem_cache:
            self._stem_cache[stem] = resolve_stem(stem)
        return self._stem_cache[stem]

    async def on_unmount(self) -> None:
        if self.session is not None:
            await self.session.disconnect()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        widget_id = event.input.id
        text = event.value.strip()
        event.input.value = ""
        if widget_id == "prompt":
            await self._handle_prompt(text)
        elif widget_id == "wiki-search":
            await self._handle_wiki_search(text)
        elif widget_id == "pin-input":
            await self._handle_pin_input(text)

    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        list_id = event.list_view.id
        item = event.item
        data = getattr(item, "data", None)
        if list_id == "wiki-results" and isinstance(data, str):
            await self._open_inline(data)
        elif list_id == "pin-list" and isinstance(data, int):
            text = self.query_one(Pinboard).get_pin(data)
            if text is None:
                return
            prompt = self.query_one("#prompt", Input)
            prompt.value = text
            prompt.focus()

    async def _handle_prompt(self, text: str) -> None:
        if not text:
            return
        if text.startswith("/"):
            await self._handle_command(text)
            return
        await self._handle_chat(text)

    async def _handle_wiki_search(self, query: str) -> None:
        if not query:
            return
        results = await asyncio.to_thread(search_index, query)
        sidebar = self.query_one(WikiSidebar)
        sidebar.populate(results)
        if not results:
            self._sys(f"No matches for '{query}'.")

    async def _handle_pin_input(self, text: str) -> None:
        if not text:
            return
        n = self.query_one(Pinboard).add_pin(text)
        self._sys(f"📌 pinned #{n}: {text[:60]}")

    async def _handle_command(self, text: str) -> None:
        head, _, tail = text.partition(" ")
        tail = tail.strip()
        handler = {
            "/help": self._cmd_help,
            "/wiki": self._cmd_wiki,
            "/open": self._cmd_open,
            "/obsidian": self._cmd_obsidian,
            "/pin": self._cmd_pin,
            "/unpin": self._cmd_unpin,
            "/save": self._cmd_save,
            "/mistake": self._cmd_mistake,
            "/reset": self._cmd_reset,
        }.get(head)
        if handler is None:
            self._sys(f"Unknown command {head}. Type /help for the list.")
            return
        await handler(tail)

    async def _cmd_help(self, _tail: str) -> None:
        chat = self.query_one(ChatPane)
        chat.add_turn("assistant", HELP_TEXT)

    async def _cmd_wiki(self, query: str) -> None:
        if not query:
            self._sys("Usage: /wiki <query>")
            return
        await self._handle_wiki_search(query)
        self.query_one(WikiSidebar).remove_class("hidden")

    async def _cmd_open(self, stem: str) -> None:
        if not stem:
            self._sys("Usage: /open <page-stem>")
            return
        await self._open_inline(stem)

    async def _cmd_obsidian(self, stem: str) -> None:
        if not stem:
            self._sys("Usage: /obsidian <page-stem>")
            return
        path = self._resolve_stem_cached(stem)
        if path is None:
            self._sys(f"No page found for [[{stem}]].")
            return
        _spawn_detached(["open", obsidian_url(stem, vault=self.vault)])
        self._sys(f"Opened [[{stem}]] in Obsidian.")

    async def _cmd_pin(self, text: str) -> None:
        if not text:
            self._sys("Usage: /pin <text>")
            return
        await self._handle_pin_input(text)

    async def _cmd_unpin(self, raw: str) -> None:
        try:
            n = int(raw.strip())
        except ValueError:
            self._sys("Usage: /unpin <number>")
            return
        ok = self.query_one(Pinboard).remove_pin(n)
        self._sys(f"Unpinned #{n}." if ok else f"No pin #{n}.")

    async def _cmd_reset(self, _tail: str) -> None:
        if not self._session_ready or self.session is None:
            self._sys("Session not ready yet.")
            return
        if self._stream_task is not None and not self._stream_task.done():
            self._stream_task.cancel()
        await self.session.reset()
        self.query_one(ChatPane).clear()
        self._sys("Conversation cleared.")

    async def _cmd_save(self, topic: str) -> None:
        if not topic:
            self._sys("Usage: /save <topic>")
            return
        if self._busy:
            self._sys("Wait for the current response to finish before /save.")
            return
        err = _validate_topic(topic)
        if err:
            self._sys(err)
            return
        await self._save_practice(topic)

    async def _cmd_mistake(self, topic: str) -> None:
        if not topic:
            self._sys("Usage: /mistake <topic>")
            return
        if self._busy:
            self._sys("Wait for the current response to finish before /mistake.")
            return
        err = _validate_topic(topic)
        if err:
            self._sys(err)
            return
        await self._save_mistake(topic)

    async def _open_inline(self, stem: str) -> None:
        body = await asyncio.to_thread(read_page, stem, None, MAX_INLINE_PAGE_BYTES)
        if body is None:
            self._sys(
                f"Cannot inline [[{stem}]] (not found or larger than "
                f"{MAX_INLINE_PAGE_BYTES // 1000}KB). Try /obsidian {stem}."
            )
            return
        tabs = self.query_one("#tabs", TabbedContent)
        tab_id = f"tab-wiki-{TAB_ID_SAFE_RE.sub('_', stem)}"
        if any(p.id == tab_id for p in tabs.query(TabPane)):
            tabs.active = tab_id
            return
        rendered = render(strip_frontmatter(body), self._resolve_stem_cached, vault=self.vault)
        viewer = VerticalScroll(Markdown(rendered))
        await tabs.add_pane(TabPane(stem, viewer, id=tab_id))
        tabs.active = tab_id

    async def _handle_chat(self, user_message: str) -> None:
        if not self._session_ready or self.session is None:
            self._sys("Session not ready yet — try again in a moment.")
            return
        if self._busy:
            self._sys("Still answering — wait for the current response to finish.")
            return
        # Atomic check-and-set under cooperative scheduling: no await between check
        # above and assignment here, so the second handler invocation will see _busy.
        self._busy = True
        self._stream_task = asyncio.create_task(self._stream_response(user_message))
        try:
            await self._stream_task
        finally:
            self._stream_task = None
            self._busy = False

    async def _stream_response(self, user_message: str) -> None:
        if self.session is None:
            self._sys("[error] No active session.")
            return
        chat = self.query_one(ChatPane)
        tabs = self.query_one("#tabs", TabbedContent)
        tabs.active = TAB_ID_CHAT
        chat.add_turn("user", user_message)
        assistant_turn = chat.add_turn("assistant", "")
        try:
            async for chunk in self.session.chat(user_message):
                rendered = render(chunk, self._resolve_stem_cached, vault=self.vault)
                assistant_turn.append_chunk(rendered)
            assistant_turn.flush()
        except asyncio.CancelledError:
            assistant_turn.append_chunk("\n\n*[cancelled]*")
            assistant_turn.flush()
            raise
        except Exception as e:  # noqa: BLE001 — UI must not die on stream errors
            assistant_turn.append_chunk(f"\n\n*[stream error: {e}]*")
            assistant_turn.flush()
            self._sys(f"[error during stream] {e}")
            return
        if self.obsidian_open:
            self._auto_open_obsidian(assistant_turn.body)

    def _auto_open_obsidian(self, body: str) -> None:
        seen: set[str] = set()
        opened = 0
        for match in WIKILINK_RE.finditer(body):
            if opened >= MAX_AUTO_OPEN_PER_RESPONSE:
                break
            stem = match.group(1).strip()
            if stem in seen:
                continue
            seen.add(stem)
            if self._resolve_stem_cached(stem) is None:
                continue
            _spawn_detached(["open", obsidian_url(stem, vault=self.vault)])
            opened += 1

    def _sys(self, text: str) -> None:
        try:
            self.query_one(ChatPane).add_system_message(text)
        except NoMatches:
            print(f"[wt] {text}", file=sys.stderr)

    async def _save_practice(self, topic: str) -> None:
        wiki_root = get_wiki_root()
        practice_dir = wiki_root / "wiki" / "practice"
        practice_dir.mkdir(parents=True, exist_ok=True)
        transcript = self.query_one(ChatPane).transcript()
        path, n = _exclusive_practice_path(practice_dir, topic, transcript)
        self._append_log(f"## [{_today()}] practice | {topic}-set-{n:02d} (written by wt)")
        self._sys(f"Saved [[practice/{topic}-set-{n:02d}]] at {path}")

    async def _save_mistake(self, topic: str) -> None:
        wiki_root = get_wiki_root()
        mistakes_dir = wiki_root / "wiki" / "mistakes"
        mistakes_dir.mkdir(parents=True, exist_ok=True)
        transcript = self.query_one(ChatPane).transcript()
        path = _write_mistake(mistakes_dir, topic, transcript)
        self._append_log(f"## [{_today()}] practice | mistake log update: {topic} (written by wt)")
        self._sys(f"Saved [[mistakes/{topic}]] at {path}")

    def _append_log(self, line: str) -> None:
        wiki_root = get_wiki_root()
        log_path = wiki_root / "log.md"
        existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""
        sep = "" if existing.endswith("\n\n") else ("\n" if existing.endswith("\n") else "\n\n")
        with log_path.open("a", encoding="utf-8") as f:
            f.write(f"{sep}{line}\n")
            f.flush()

    async def action_reset_session(self) -> None:
        if not self._session_ready:
            return
        await self._cmd_reset("")

    def action_toggle_wiki_sidebar(self) -> None:
        try:
            self.query_one(WikiSidebar).toggle_class("hidden")
        except NoMatches:
            return

    def action_toggle_pinboard(self) -> None:
        try:
            self.query_one(Pinboard).toggle_class("hidden")
        except NoMatches:
            return

    def action_next_tab(self) -> None:
        try:
            tabs = self.query_one("#tabs", TabbedContent)
        except NoMatches:
            return
        panes = list(tabs.query(TabPane))
        if not panes:
            return
        ids = [p.id for p in panes if p.id]
        if not ids:
            return
        try:
            i = ids.index(tabs.active)
        except ValueError:
            i = -1
        tabs.active = ids[(i + 1) % len(ids)]

    async def action_close_current_tab(self) -> None:
        try:
            tabs = self.query_one("#tabs", TabbedContent)
        except NoMatches:
            return
        active = tabs.active
        if active == TAB_ID_CHAT or not active:
            return
        await tabs.remove_pane(active)
        tabs.active = TAB_ID_CHAT


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="wt", description="wiki-aware Socratic tutor TUI")
    p.add_argument("--model", default="claude-sonnet-4-6")
    p.add_argument("--obsidian", action="store_true", help="Auto-open cited wiki pages in Obsidian")
    p.add_argument("--vault", default=os.environ.get("WT_VAULT_NAME", DEFAULT_VAULT_NAME))
    return p.parse_args(argv)


def run() -> None:
    args = _parse_args()
    app = WikiTutorApp(model=args.model, obsidian_open=args.obsidian, vault=args.vault)
    try:
        app.run()
    except (AuthError, WikiRootError) as e:
        print(f"[wt] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    run()
