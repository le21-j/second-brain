# wiki-tutor (`wt`)

A wiki-aware Socratic tutor TUI for Jayden's `second-brain` Obsidian vault. Drops you into a chat with the `teacher` persona that auto-injects relevant wiki pages as context, renders LaTeX as Unicode, makes `[[wiki-links]]` clickable (OSC 8), and writes practice attempts back to the wiki.

## Install

```bash
# 1) Generate a 1-year OAuth token from your Claude Pro/Max subscription (one time)
claude setup-token

# 2) Add the printed token to your shell rc
echo 'export CLAUDE_CODE_OAUTH_TOKEN=sk-ant-oat01-...' >> ~/.zshrc
source ~/.zshrc

# 3) Install wt as a global uv tool
uv tool install ~/Code/wiki-tutor

# 4) Run it from anywhere
wt
```

## Usage

```bash
wt                    # default: claude-sonnet-4-6, no auto-open
wt --model claude-opus-4-7
wt --obsidian         # auto-open cited [[pages]] in Obsidian
wt --vault second-brain
```

## Layout

```
┌──────────────────────────────────────────────────────────────────┐
│  Header: wiki-tutor  •  ~/Documents/second-brain                 │
├──────────────┬──────────────────────────────────┬────────────────┤
│  📚 Wiki     │  ╭─[Chat ✦]─[backprop]──[ofdm]─╮ │  📌 Pinboard   │
│  ──────────  │  │                              │ │  ──────────    │
│  search:     │  │   Active tab content         │ │  pin a thought │
│  [_______]   │  │   (chat or wiki page)        │ │  [_______]     │
│              │  │                              │ │                │
│  Results:    │  │                              │ │  Pinned:       │
│  • backprop  │  │                              │ │  1. ...        │
│  • autograd  │  │                              │ │  2. ...        │
│  • pytorch   │  ╰──────────────────────────────╯ │                │
├──────────────┴──────────────────────────────────┴────────────────┤
│  > Ask the tutor or type / for commands                          │
├──────────────────────────────────────────────────────────────────┤
│  ^B WikiBar  ^P Pinboard  ^T Tab  ^W Close  ^L Reset  ^C Quit    │
└──────────────────────────────────────────────────────────────────┘
```

**Three panes, all toggleable.** The center workspace is a tab strip:
- **Chat ✦** is always tab 0 — the live conversation. Cannot be closed.
- Each `/open <stem>` (or click on a wiki search result) adds a new tab showing that wiki page rendered with LaTeX → Unicode and clickable `[[links]]`.
- Click an item in the wiki sidebar's result list to open it inline.
- Click an item in the pinboard to copy that pin back into the prompt for re-asking.

## Slash commands

| Command | Description |
|---|---|
| `/wiki <query>` | Search `index.md`; populate the left sidebar |
| `/open <stem>` | Open page **inline as a new tab** |
| `/obsidian <stem>` | Open page in the external Obsidian app |
| `/pin <text>` | Pin text to the right pinboard |
| `/unpin <n>` | Remove pin number n |
| `/save <topic>` | Save conversation as `wiki/practice/<topic>-set-NN.md` |
| `/mistake <topic>` | Append misconception to `wiki/mistakes/<topic>.md` |
| `/reset` | Clear conversation history |
| `/help` | Show command list |

## Keybindings

| Key | Action |
|---|---|
| `Ctrl+B` | Toggle wiki sidebar |
| `Ctrl+P` | Toggle pinboard |
| `Ctrl+T` | Cycle through open tabs |
| `Ctrl+W` | Close current wiki tab (chat tab cannot be closed) |
| `Ctrl+L` | Reset conversation |
| `Ctrl+C` | Quit |

## Environment variables

| Var | Default | Purpose |
|---|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | — (required) | Auth from `claude setup-token` |
| `WT_WIKI_ROOT` | `~/Documents/second-brain` | Wiki root directory |
| `WT_VAULT_NAME` | `second-brain` | Obsidian vault name for `obsidian://` URLs |
| `WT_FORCE_OSC8` | unset | Force OSC 8 hyperlinks even on unrecognized terminals |

## How wiki context injection works

On every user turn, `wt`:

1. Reads `index.md`.
2. Tokenizes the user query.
3. Scores each `- [[stem]] — description` line by keyword overlap (also matches frontmatter `title`, `tags`, `course`).
4. Picks the top 5 pages and reads each in full.
5. Prepends them to the user message inside a `[WIKI CONTEXT]` block before sending to Claude.

System prompt is `~/.claude/agents/teacher.md` + `<wiki>/CLAUDE.md`, loaded once at session start.

## Modules

```
wt/
├── constants.py    # paths, defaults, callout style map
├── wiki.py         # search_index, build_context, resolve_stem, read_page
├── llm.py          # ClaudeSDKClient wrapper + system prompt loader
├── render.py       # latex_to_unicode + OSC 8 wiki-link wrapping
└── main.py         # Textual app, slash commands, write-back
```

## Terminal compatibility

OSC 8 hyperlinks render as clickable `[[stem]]` text in: iTerm2, WezTerm, Hyper, Ghostty, VS Code integrated terminal. Other terminals fall back to plain `[[stem]]` (still readable). Set `WT_FORCE_OSC8=1` to force.

LaTeX rendering uses Unicode approximations only — no TeX install required. Greek letters, common operators, sub/superscripts (digits + simple letters), `\frac`, `\sqrt` all handled. For math-heavy answers, use `--obsidian` to auto-open the cited wiki page in Obsidian where MathJax renders properly.
