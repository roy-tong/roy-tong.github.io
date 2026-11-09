#!/usr/bin/env python3
"""Release checks for llms.txt, the agent-facing index (stdlib only).

Run after Jekyll build: python3 scripts/verify_llms.py

Invariants:
  1. Every URL mentioned in llms.txt resolves to a built page in _site
     (or is an intentional external link, which must at least be absolute).
  2. Recent posts are represented: anything published in the last
     RECENT_DAYS must appear in llms.txt, so the agent index cannot go
     stale silently while the essay archive moves on.
"""

import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
RECENT_DAYS = 45
ERRORS = []

def check(condition, message):
    if not condition:
        ERRORS.append(message)

def target_for(url: str) -> Path:
    path = url.split("roy-tong.github.io", 1)[-1].split("?")[0].split("#")[0]
    if not path.startswith("/"):
        return SITE / path  # relative like knowledge/...
    target = SITE / path.lstrip("/")
    return target / "index.html" if not target.suffix else target

# 1. Every llms.txt URL exists in the build.
# Site URLs are those served BY the Pages site itself; GitHub repo links
# (github.com/roy-tong/roy-tong.github.io/...) are external.
llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
urls = re.findall(r"https?://[^\s\)\]]+", llms)
internal = [u for u in urls if re.match(r"https?://roy-tong\.github\.io/", u)]
for url in internal:
    check(target_for(url).is_file(), "llms.txt URL not built: " + url)
external = [u for u in urls if u not in internal]
check(len(external) > 0, "llms.txt lost all external links — parsing may be broken")

# 2. Recent posts are mentioned.
cutoff = date.today() - timedelta(days=RECENT_DAYS)
for posts_dir in (ROOT / "_posts", ROOT / "en" / "_posts"):
    for post in posts_dir.glob("*.md"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", post.name)
        if not m:
            continue
        published = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        if published < cutoff:
            continue
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-|\.md$", "", post.name)
        slug = re.sub(r"-en$", "", slug)
        check(slug in llms, f"post from {published} missing from llms.txt: {slug}")

if ERRORS:
    print(json.dumps({"errors": ERRORS}, ensure_ascii=False, indent=2))
    sys.exit(1)
print(f"llms.txt OK: {len(internal)} site URLs resolve, recent posts covered ({RECENT_DAYS}d window)")
