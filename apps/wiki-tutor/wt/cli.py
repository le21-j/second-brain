"""Top-level entry point — dispatches to either the web UI (default) or the TUI."""

from __future__ import annotations

import argparse
import sys


def _parse(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="wt", description="wiki-aware Socratic tutor")
    p.add_argument("--tui", action="store_true", help="Run the terminal UI instead of the web UI")
    p.add_argument("--model", default="claude-sonnet-4-6")
    p.add_argument("--port", type=int, default=0, help="Port for the web server (0 = pick a free port)")
    p.add_argument("--no-browser", action="store_true", help="Do not auto-open the browser")
    p.add_argument("--vault", default=None, help="Obsidian vault name override")
    p.add_argument("--obsidian", action="store_true", help="(TUI only) auto-open cited pages in Obsidian")
    return p.parse_args(argv)


def run() -> None:
    args = _parse()
    if args.tui:
        from .main import run as run_tui
        sys.argv = ["wt"]
        if args.obsidian:
            sys.argv.append("--obsidian")
        if args.vault:
            sys.argv += ["--vault", args.vault]
        run_tui()
        return
    from .server import run_web
    run_web(model=args.model, port=args.port, open_browser=not args.no_browser, vault=args.vault)


if __name__ == "__main__":
    run()
