"""Wiki search + context injection. Load-bearing module.

Reads the user's Obsidian-flavored second-brain wiki and produces a context
block to prepend to each turn of the LLM conversation.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml

from .constants import DEFAULT_WIKI_ROOT, INDEX_SEARCH_LIMIT, TOP_K_PAGES


class WikiRootError(RuntimeError):
    pass


INDEX_LINE_RE = re.compile(r"^\s*-\s*\[\[([^\]|]+)(?:\|[^\]]+)?\]\]\s*[—\-:]?\s*(.*)$")
WORD_RE = re.compile(r"[A-Za-z0-9]+")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


@dataclass(frozen=True, slots=True)
class IndexEntry:
    stem: str
    description: str
    line_no: int


def get_wiki_root() -> Path:
    raw = os.environ.get("WT_WIKI_ROOT", str(DEFAULT_WIKI_ROOT))
    root = Path(raw).expanduser().resolve()
    if not root.exists():
        raise WikiRootError(
            f"Wiki root {root} does not exist. Set WT_WIKI_ROOT or create the directory."
        )
    if not (root / "index.md").exists():
        raise WikiRootError(
            f"index.md not found at {root}/index.md. Is this the right wiki root?"
        )
    return root


def _tokenize(text: str) -> set[str]:
    return {m.group(0).lower() for m in WORD_RE.finditer(text)}


@lru_cache(maxsize=4)
def _parse_index_cached(path_str: str, mtime_ns: int) -> tuple[IndexEntry, ...]:
    raw = Path(path_str).read_text(encoding="utf-8")
    entries: list[IndexEntry] = []
    for i, line in enumerate(raw.splitlines()):
        m = INDEX_LINE_RE.match(line)
        if not m:
            continue
        entries.append(
            IndexEntry(stem=m.group(1).strip(), description=m.group(2).strip(), line_no=i)
        )
    return tuple(entries)


def _parse_index(root: Path) -> tuple[IndexEntry, ...]:
    idx = root / "index.md"
    return _parse_index_cached(str(idx), idx.stat().st_mtime_ns)


@lru_cache(maxsize=512)
def _frontmatter_corpus_cached(path_str: str, mtime_ns: int) -> str:
    try:
        text = Path(path_str).read_text(encoding="utf-8")
    except OSError:
        return ""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return ""
    try:
        data = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return ""
    parts: list[str] = []
    for key in ("title", "tags", "course"):
        val = data.get(key)
        if val is None:
            continue
        if isinstance(val, list):
            parts.extend(str(v) for v in val)
        else:
            parts.append(str(val))
    return " ".join(parts)


def _frontmatter_corpus(path: Path) -> str:
    try:
        mtime = path.stat().st_mtime_ns
    except OSError:
        return ""
    return _frontmatter_corpus_cached(str(path), mtime)


def resolve_stem(stem: str, root: Path | None = None) -> Path | None:
    root = root or get_wiki_root()
    matches = sorted((root / "wiki").rglob(f"{stem}.md"))
    if not matches:
        return None
    return matches[0]


MAX_INLINE_PAGE_BYTES = 1_000_000


def read_page(stem: str, root: Path | None = None, max_bytes: int | None = None) -> str | None:
    path = resolve_stem(stem, root=root)
    if path is None:
        return None
    text = path.read_text(encoding="utf-8")
    if max_bytes is not None and len(text.encode("utf-8")) > max_bytes:
        return None
    return text


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def _score_query(query_tokens: set[str], haystack: set[str]) -> int:
    """Hybrid scoring so partial typing surfaces relevant pages.

    For each query token: exact whole-token match scores 3, prefix match (a
    haystack token starts with the query token) scores 2, substring match
    anywhere in any haystack token scores 1. Substring/prefix matching is
    skipped for query tokens shorter than 2 chars so a stray letter doesn't
    match every page.
    """
    score = 0
    for q in query_tokens:
        if q in haystack:
            score += 3
            continue
        if len(q) < 2:
            continue
        if any(h.startswith(q) for h in haystack):
            score += 2
            continue
        if any(q in h for h in haystack):
            score += 1
    return score


def search_index(query: str, root: Path | None = None) -> list[tuple[str, str, int]]:
    root = root or get_wiki_root()
    entries = _parse_index(root)
    tokens = _tokenize(query)
    if not tokens:
        return []
    scored: list[tuple[int, int, IndexEntry]] = []
    for entry in entries:
        corpus = f"{entry.stem} {entry.description}"
        path = resolve_stem(entry.stem, root=root)
        if path is not None:
            corpus = f"{corpus} {_frontmatter_corpus(path)}"
        haystack = _tokenize(corpus)
        score = _score_query(tokens, haystack)
        if score == 0:
            continue
        scored.append((score, -entry.line_no, entry))
    scored.sort(reverse=True)
    seen: set[str] = set()
    deduped: list[tuple[str, str, int]] = []
    for s, _, e in scored:
        if e.stem in seen:
            continue
        seen.add(e.stem)
        deduped.append((e.stem, e.description, s))
        if len(deduped) >= INDEX_SEARCH_LIMIT:
            break
    return deduped


def build_context(query: str, root: Path | None = None) -> str:
    """Return a *lean* candidate-page list — names + one-line descriptions only.

    Page bodies are NOT pre-injected; the agent has the `Read` tool and can
    fetch what it needs. Cuts ~6K tokens/turn vs. inlining bodies, which is
    the dominant TTFT cost on Sonnet.
    """
    root = root or get_wiki_root()
    matches = search_index(query, root=root)
    if not matches:
        return "No matching wiki pages found in the index for this query.\n"
    top = matches[:TOP_K_PAGES]
    lines: list[str] = [
        "Relevant wiki pages (from [[index.md]]) — use the Read tool to open the ones you need:",
    ]
    for stem, desc, _score in top:
        snippet = desc.strip()
        if len(snippet) > 120:
            snippet = snippet[:117].rstrip() + "…"
        if snippet:
            lines.append(f"- [[{stem}]] — {snippet}")
        else:
            lines.append(f"- [[{stem}]]")
    return "\n".join(lines)
