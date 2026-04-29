#!/usr/bin/env python3
"""
Bulk-download lecture slides from Canvas for EEE 341 and EEE 335.

EEE 341: each lecture is an Assignment with a Canvas file link in the description.
EEE 335: each lecture is a Page with Dropbox slide/problems/solutions links.

Saves into:
  raw/slides/eee-341/<lecture-slug>.pdf
  raw/slides/eee-335/<lecture-slug>-slides.pdf
  raw/slides/eee-335/<lecture-slug>-problems.pdf
  raw/slides/eee-335/<lecture-slug>-solutions.pdf

Idempotent — skips files already on disk.
"""

import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / ".canvas-config"
RAW = ROOT / "raw" / "slides"

def cfg():
    out = {}
    for ln in CONFIG.read_text().splitlines():
        ln = ln.strip()
        if "=" in ln and not ln.startswith("#"):
            k, v = ln.split("=", 1)
            out[k.strip()] = v.strip()
    return out

CFG = cfg()
DOMAIN = CFG["CANVAS_DOMAIN"]
TOKEN = CFG["CANVAS_TOKEN"]

def api(path, params=""):
    url = f"{DOMAIN}/api/v1{path}{('?' + params) if params else ''}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def list_pages(course_id):
    """List all pages in a course (paginated)."""
    out = []
    page = 1
    while True:
        try:
            data = api(f"/courses/{course_id}/pages", f"per_page=100&page={page}")
        except urllib.error.HTTPError:
            return out
        if not data:
            break
        out.extend(data)
        if len(data) < 100:
            break
        page += 1
    return out

def safe_name(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:80]

def download(url, dest, label="file"):
    if dest.exists() and dest.stat().st_size > 0:
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if len(data) < 1000:
            print(f"    ⚠ {label}: response too small ({len(data)} bytes), skipping")
            return False
        dest.write_bytes(data)
        print(f"    ✓ {label}: {dest.name} ({len(data)//1024} KB)")
        return True
    except Exception as e:
        print(f"    ✗ {label}: {e}")
        return False

def download_canvas_file(course_id, file_id, dest):
    """Get the actual download URL for a Canvas file via the API, then fetch it."""
    if dest.exists() and dest.stat().st_size > 0:
        return False
    try:
        meta = api(f"/courses/{course_id}/files/{file_id}")
    except urllib.error.HTTPError as e:
        print(f"    ✗ canvas file {file_id}: {e}")
        return False
    durl = meta.get("url")
    fname = meta.get("display_name") or dest.name
    if not durl:
        print(f"    ✗ canvas file {file_id}: no URL in metadata")
        return False
    return download(durl, dest, label=fname)

# ============================================================================
# EEE 341 — assignments containing Canvas file links to slides
# ============================================================================
def process_eee341():
    course_id = 250894
    out_dir = RAW / "eee-341"
    print(f"\n=== EEE 341 (course {course_id}) ===")

    cache = Path(os.environ.get("TEMP", "/tmp")) / f"canvas_modules_{course_id}.json"
    if not cache.exists():
        # fall back to Windows temp
        cache = Path(r"C:\Users\JAYDEN~1\AppData\Local\Temp") / f"canvas_modules_{course_id}.json"
    mods = json.loads(cache.read_text(encoding="utf-8"))

    # collect lecture assignment IDs
    lectures = []
    for m in mods:
        for it in m.get("items") or []:
            if it.get("type") == "Assignment" and "Lecture" in it.get("title", ""):
                lectures.append({
                    "title": it["title"],
                    "url": it.get("url", ""),
                })
    print(f"Found {len(lectures)} lecture assignments")

    downloaded = 0
    for lec in lectures:
        # extract assignment ID
        m = re.search(r"assignments/(\d+)", lec["url"])
        if not m:
            continue
        aid = m.group(1)
        # fetch assignment description
        try:
            a = api(f"/courses/{course_id}/assignments/{aid}")
        except Exception as e:
            print(f"  ✗ {lec['title'][:50]}: {e}")
            continue
        desc = a.get("description", "") or ""
        # find Canvas file IDs in the description
        file_ids = re.findall(r"/files/(\d+)", desc)
        if not file_ids:
            continue
        slug = safe_name(lec["title"])
        print(f"  {lec['title'][:60]}")
        for i, fid in enumerate(set(file_ids)):
            suffix = "" if i == 0 else f"-{i}"
            dest = out_dir / f"{slug}{suffix}.pdf"
            if download_canvas_file(course_id, fid, dest):
                downloaded += 1
                time.sleep(0.3)  # be polite
    print(f"EEE 341: {downloaded} new files downloaded")
    return downloaded

# ============================================================================
# EEE 335 — pages with Dropbox links
# ============================================================================
def process_eee335():
    course_id = 245462
    out_dir = RAW / "eee-335"
    print(f"\n=== EEE 335 (course {course_id}) ===")

    cache = Path(os.environ.get("TEMP", "/tmp")) / f"canvas_modules_{course_id}.json"
    if not cache.exists():
        cache = Path(r"C:\Users\JAYDEN~1\AppData\Local\Temp") / f"canvas_modules_{course_id}.json"
    mods = json.loads(cache.read_text(encoding="utf-8"))

    # collect lecture page slugs
    lectures = []
    for m in mods:
        for it in m.get("items") or []:
            if it.get("type") == "Page" and ("Lecture" in it.get("title", "") or "Lab" in it.get("title", "")):
                lectures.append({
                    "title": it["title"],
                    "page_url": it.get("page_url", ""),
                })
    print(f"Found {len(lectures)} page items (lectures + labs)")

    downloaded = 0
    for lec in lectures:
        slug_url = lec["page_url"]
        if not slug_url:
            continue
        try:
            p = api(f"/courses/{course_id}/pages/{slug_url}")
        except Exception as e:
            print(f"  ✗ {lec['title'][:50]}: {e}")
            continue
        body = p.get("body", "") or ""
        # find dropbox links
        dropbox_links = re.findall(r'href=["\']([^"\']*dropbox\.com[^"\']+)["\']', body)
        if not dropbox_links:
            continue
        slug = safe_name(lec["title"])
        print(f"  {lec['title'][:60]} ({len(dropbox_links)} files)")
        for link in dropbox_links:
            # categorize by URL hint
            link_unescaped = link.replace("&amp;", "&")
            # ensure dl=1 for direct download
            if "dl=0" in link_unescaped:
                dl_url = link_unescaped.replace("dl=0", "dl=1")
            elif "dl=1" in link_unescaped:
                dl_url = link_unescaped
            else:
                dl_url = link_unescaped + ("&dl=1" if "?" in link_unescaped else "?dl=1")
            # name from URL
            url_lower = link_unescaped.lower()
            if "solution" in url_lower:
                kind = "solutions"
            elif "problem" in url_lower:
                kind = "problems"
            elif "lab" in url_lower:
                kind = "lab"
            else:
                kind = "slides"
            dest = out_dir / f"{slug}-{kind}.pdf"
            if download(dl_url, dest, label=kind):
                downloaded += 1
                time.sleep(0.3)
    print(f"EEE 335: {downloaded} new files downloaded")
    return downloaded

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else "both"
    n = 0
    if only in ("both", "341"):
        n += process_eee341()
    if only in ("both", "335"):
        n += process_eee335()
    print(f"\nTotal new files: {n}")
