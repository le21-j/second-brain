#!/usr/bin/env python3
"""
Weekly Dashboard for Jayden's LLM Wiki.

Pulls live Canvas data (using cached token from .canvas-config), reads the latest
workload-plan summary, scans recent wiki pages, and prints a terminal dashboard
showing what's due, what wiki pages support each item, and what's been added
to the second brain this week.

Usage:
  python scripts/dashboard.py
  python scripts/dashboard.py --refresh   # re-fetch Canvas data
  python scripts/dashboard.py --week      # show this week only (default 14d)
"""

import json, os, sys, re, html, urllib.request, urllib.error, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
CACHE = Path(os.environ.get("TEMP", "/tmp")) / "canvas_cache"
CONFIG = ROOT / ".canvas-config"

COURSES = {
    250894: ("EEE 341", "Electromagnetics"),
    246317: ("EEE 304", "Signals & Systems II"),
    246051: ("EEE 350", "Random Signal Analysis"),
    245853: ("EEE 202", "Lab (TA)"),
    245462: ("EEE 335", "Analog & Digital Circuits"),
    241591: ("EEE 404", "Real-Time DSP"),
}

# courses Jayden is taking (excludes EEE 202 which he TAs)
TAKING = {250894, 246317, 246051, 245462, 241591}

# colors (ANSI)
class C:
    R = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAG = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

def load_config():
    if not CONFIG.exists():
        print(f"{C.RED}No Canvas config found at {CONFIG}.{C.R}")
        print("Create it with two lines:")
        print("  CANVAS_DOMAIN=https://canvas.asu.edu")
        print("  CANVAS_TOKEN=<your token>")
        sys.exit(1)
    cfg = {}
    for ln in CONFIG.read_text().splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#") or "=" not in ln:
            continue
        k, v = ln.split("=", 1)
        cfg[k.strip()] = v.strip()
    return cfg

def fetch(url, token, cache_path, force=False):
    if cache_path.exists() and not force:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read().decode("utf-8")
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(data, encoding="utf-8")
        return json.loads(data)
    except urllib.error.URLError as e:
        print(f"{C.RED}Canvas fetch failed: {e}{C.R}")
        if cache_path.exists():
            return json.loads(cache_path.read_text(encoding="utf-8"))
        return []

def strip_html(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def get_assignments(cfg, force=False):
    """Pull all assignments for active courses, return list of dicts."""
    items = []
    for cid in TAKING:
        url = f"{cfg['CANVAS_DOMAIN']}/api/v1/courses/{cid}/assignments?per_page=100&include[]=submission&order_by=due_at"
        cache = CACHE / f"assignments_{cid}.json"
        data = fetch(url, cfg["CANVAS_TOKEN"], cache, force=force)
        for a in data:
            due = a.get("due_at")
            if not due:
                continue
            try:
                due_dt = dt.datetime.fromisoformat(due.replace("Z", "+00:00"))
            except Exception:
                continue
            sub = a.get("submission") or {}
            items.append({
                "course_id": cid,
                "course": COURSES[cid][0],
                "name": a.get("name", ""),
                "due": due_dt,
                "points": a.get("points_possible") or 0,
                "url": a.get("html_url", ""),
                "submitted": sub.get("workflow_state") in ("submitted", "graded", "complete"),
                "missing": sub.get("missing", False),
                "score": sub.get("score"),
            })
    items.sort(key=lambda x: x["due"])
    return items

def find_recent_wiki(days=14):
    """Find wiki .md files modified in the last N days."""
    cutoff = dt.datetime.now() - dt.timedelta(days=days)
    recent = []
    for p in WIKI.rglob("*.md"):
        mtime = dt.datetime.fromtimestamp(p.stat().st_mtime)
        if mtime >= cutoff:
            rel = p.relative_to(WIKI)
            recent.append((mtime, rel, p))
    recent.sort(key=lambda x: x[0], reverse=True)
    return recent

def find_wiki_links_for(text):
    """Heuristic: find concept/walkthrough pages whose name appears in text."""
    text_lower = text.lower()
    hits = []
    for sub in ("walkthroughs", "concepts", "examples"):
        for p in (WIKI / sub).glob("*.md"):
            stem = p.stem
            # match if course code or page stem appears
            if stem in text_lower or stem.replace("-", " ") in text_lower:
                hits.append(stem)
    return hits[:3]  # cap

def render(items, recent_wiki, horizon_days):
    now = dt.datetime.now(dt.timezone.utc)
    horizon = now + dt.timedelta(days=horizon_days)

    print()
    print(f"{C.BOLD}{C.CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{C.R}")
    title = f"WEEKLY DASHBOARD — {now.astimezone().strftime('%a %Y-%m-%d %I:%M %p')}"
    print(f"{C.BOLD}{C.CYAN}║{C.R}  {C.BOLD}{title}{C.R}{' ' * (76 - len(title))}{C.BOLD}{C.CYAN}║{C.R}")
    sub = f"Looking ahead {horizon_days} days · 5 active courses · wiki at {ROOT.name}/wiki"
    print(f"{C.BOLD}{C.CYAN}║{C.R}  {C.DIM}{sub}{C.R}{' ' * (76 - len(sub))}{C.BOLD}{C.CYAN}║{C.R}")
    print(f"{C.BOLD}{C.CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{C.R}")

    # Filter window
    window = [i for i in items if i["due"] >= now - dt.timedelta(days=1) and i["due"] <= horizon]
    not_done = [i for i in window if not i["submitted"]]

    # Section: assignments due
    print()
    print(f"{C.BOLD}{C.YELLOW}📋 ASSIGNMENTS DUE ({len(not_done)} open / {len(window)} total in window){C.R}")
    print(f"{C.DIM}{'─' * 80}{C.R}")
    total_pts_open = 0
    for i in window:
        days = (i["due"] - now).total_seconds() / 86400
        if i["submitted"]:
            badge = f"{C.GREEN}✓ DONE  {C.R}"
        elif i["missing"]:
            badge = f"{C.RED}✗ MISS  {C.R}"
        elif days < 1:
            badge = f"{C.RED}{C.BOLD}⏰ TODAY{C.R}"
            total_pts_open += i["points"]
        elif days < 3:
            badge = f"{C.YELLOW}⚠️  SOON {C.R}"
            total_pts_open += i["points"]
        else:
            badge = f"{C.BLUE}   open {C.R}"
            total_pts_open += i["points"]

        due_str = i["due"].astimezone().strftime("%a %m/%d %I:%M%p")
        days_str = f"{days:+.1f}d"
        course = i["course"]
        name = i["name"][:48]
        pts = f"{i['points']:>5.0f}p"
        print(f"  {badge}  {C.CYAN}{course:<8}{C.R} {C.DIM}{due_str:<18} {days_str:>6}{C.R}  {name:<50} {C.MAG}{pts}{C.R}")

    print(f"{C.DIM}{'─' * 80}{C.R}")
    print(f"  {C.BOLD}Open points in window:{C.R} {C.MAG}{total_pts_open:.0f}{C.R}")

    # Section: today/tomorrow priority
    soon = [i for i in not_done if (i["due"] - now).total_seconds() / 86400 < 2]
    if soon:
        print()
        print(f"{C.BOLD}{C.RED}🚨 NEXT 48 HOURS — DO THESE FIRST{C.R}")
        print(f"{C.DIM}{'─' * 80}{C.R}")
        for i in soon:
            hrs = (i["due"] - now).total_seconds() / 3600
            print(f"  {C.RED}{C.BOLD}▸{C.R} {i['course']} — {i['name']}  ({C.YELLOW}{hrs:+.1f}h{C.R})")
            print(f"      {C.DIM}{i['url']}{C.R}")
            # find related wiki pages
            wiki_hits = find_wiki_links_for(i["name"] + " " + i["course"])
            if wiki_hits:
                print(f"      {C.GREEN}wiki:{C.R} {', '.join(f'[[{h}]]' for h in wiki_hits)}")

    # Section: wiki activity this week
    print()
    print(f"{C.BOLD}{C.GREEN}📚 WIKI PAGES TOUCHED THIS WEEK ({len(recent_wiki)} files){C.R}")
    print(f"{C.DIM}{'─' * 80}{C.R}")
    for mtime, rel, _ in recent_wiki[:20]:
        days_ago = (dt.datetime.now() - mtime).days
        bucket = str(rel.parent)
        name = rel.stem
        ago = "today" if days_ago == 0 else f"{days_ago}d ago"
        print(f"  {C.DIM}[{bucket:<13}]{C.R} {C.CYAN}{name:<55}{C.R} {C.DIM}{ago}{C.R}")
    if len(recent_wiki) > 20:
        print(f"  {C.DIM}… and {len(recent_wiki) - 20} more{C.R}")

    # Section: per-course pts breakdown
    print()
    print(f"{C.BOLD}{C.BLUE}🎯 PER-COURSE BREAKDOWN (open items in window){C.R}")
    print(f"{C.DIM}{'─' * 80}{C.R}")
    by_course = {}
    for i in not_done:
        by_course.setdefault(i["course"], []).append(i)
    for course in sorted(by_course.keys()):
        ci = by_course[course]
        pts = sum(i["points"] for i in ci)
        # find course wiki page
        course_slug = course.lower().replace(" ", "-")
        course_page = WIKI / "courses" / f"{course_slug}.md"
        wiki_status = f"{C.GREEN}[[{course_slug}]]{C.R}" if course_page.exists() else f"{C.RED}(no wiki page){C.R}"
        print(f"  {C.CYAN}{course:<8}{C.R} {len(ci):>2} items, {pts:>5.0f} pts   {wiki_status}")

    print()
    print(f"{C.DIM}Run with --refresh to re-fetch from Canvas. Latest workload plan:{C.R}")
    workloads = sorted(WIKI.glob("summaries/daily-*-workload.md"), reverse=True)
    if workloads:
        print(f"  {C.BLUE}wiki/summaries/{workloads[0].name}{C.R}")
    print()

def main():
    force = "--refresh" in sys.argv
    horizon = 7 if "--week" in sys.argv else 14

    cfg = load_config()
    items = get_assignments(cfg, force=force)
    recent = find_recent_wiki(days=horizon)
    render(items, recent, horizon)

if __name__ == "__main__":
    main()
