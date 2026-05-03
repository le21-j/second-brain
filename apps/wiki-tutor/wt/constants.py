from __future__ import annotations

import re
from pathlib import Path

DEFAULT_WIKI_ROOT = Path.home() / "Documents" / "second-brain"
DEFAULT_VAULT_NAME = "second-brain"
TOP_K_PAGES = 5
INDEX_SEARCH_LIMIT = 10
MAX_AUTO_OPEN_PER_RESPONSE = 3
MAX_PRACTICE_SETS_PER_TOPIC = 100
CONFIG_DIR = Path.home() / ".config" / "wiki-tutor"
CONFIG_FILE = CONFIG_DIR / "config.toml"
TEACHER_PERSONA_PATH = Path.home() / ".claude" / "agents" / "teacher.md"
SUPPORTED_TERM_PROGRAMS = {"iTerm.app", "WezTerm", "Hyper", "vscode", "ghostty"}

TOPIC_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
TAB_ID_SAFE_RE = re.compile(r"[^a-zA-Z0-9_-]")
TAB_ID_CHAT = "tab-chat"

CALLOUT_STYLES = {
    "note": "blue",
    "tip": "green",
    "warning": "yellow",
    "example": "cyan",
    "info": "blue",
    "question": "magenta",
}
