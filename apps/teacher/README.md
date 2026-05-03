# Teacher — Web UI for the Socratic Tutor

A local web app that wraps the same Socratic-tutor system prompt as `/teacher` in Claude Code, but renders responses with **Markdown + LaTeX (KaTeX) + syntax-highlighted code** so dialogue is easier to digest than terminal output.

Everything runs locally; nothing leaves your machine except the Claude API call itself.

## What this fixes

`/teacher` in the Claude Code terminal works, but:
- LaTeX renders as `$\mu$` literal text, not as $\mu$.
- Markdown headings/tables/callouts render as raw `##`/`|`/`> [!note]`.
- Code blocks have no syntax highlight.
- Long Socratic dialogues get cluttered.

This app is the same agent persona, hosted at `http://localhost:8765`, with proper rendering and conversation history.

## Setup (one-time per machine)

1. **Install [uv](https://docs.astral.sh/uv/)** if you haven't:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Get an Anthropic API key** at https://console.anthropic.com → API Keys.

3. **From this directory:**
   ```bash
   cd apps/teacher
   cp .env.example .env
   # Edit .env and paste your ANTHROPIC_API_KEY
   uv sync
   ```

## Run

```bash
cd apps/teacher
uv run server.py
```

Then open http://localhost:8765 in your browser.

## Use

- Type a question (e.g., **"teach me belief propagation"**).
- Submit (Cmd+Enter or click Send).
- Teacher responds with a Socratic question — answer it; iterate.
- Switch model (Sonnet 4.6 fast / Opus 4.7 deep) via the dropdown.
- "New chat" button resets the conversation; chats persist in browser localStorage so you can refresh and resume.
- Click "Save to wiki" on any teacher message to copy a Markdown-formatted attempt into your clipboard, ready to paste into `wiki/practice/` or `wiki/mistakes/`.

## How it works

- **Backend:** FastAPI + the official `anthropic` SDK. Loads the system prompt from `~/.claude/agents/teacher.md` at startup so the persona stays in sync with Claude Code's `/teacher`. Uses **prompt caching** on the system prompt so repeated turns within 5 minutes are cheap.
- **Frontend:** single static HTML page. Markdown via [marked.js](https://marked.js.org/), math via [KaTeX](https://katex.org/), code via [highlight.js](https://highlightjs.org/). Conversations stored in `localStorage`.
- **No database.** Conversation state lives in your browser; transcripts you want to keep go in the wiki.

## Sync across devices

The whole `apps/teacher/` directory is committed to the second-brain repo. On a new device:
```bash
git pull
cd apps/teacher
cp .env.example .env   # add your API key
uv sync
uv run server.py
```

Your `.env` is gitignored — the API key stays local.

## Future enhancements (not built yet)

- [ ] Streaming responses (server-sent events).
- [ ] Auto-write attempts to `wiki/practice/` and misconceptions to `wiki/mistakes/{topic}.md` when a session ends.
- [ ] Sidebar with session history.
- [ ] Wiki-link autocomplete: `[[concept]]` → searches `wiki/concepts/` for matching pages.
