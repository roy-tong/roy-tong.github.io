#!/usr/bin/env python3
"""Generate per-tag pages under tags/ for every tag used by 2+ posts.

Run before publishing (see README): python3 scripts/generate_tags.py
Pure static output, so GitHub Pages needs no plugins. Pages carry
`generated: true` and are rewritten wholesale; hand-edits will be lost.

Chinese tags need a hand-picked ASCII slug in TAG_SLUGS (keeps URLs
readable and stable). A tag reaching 2+ posts without a slug fails the
script so the mapping stays deliberate. Single-post tags never need a
slug: they get no page (thin content), only anchors on /tags/.
"""

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_POSTS = 2

TAG_SLUGS = {
    "agent": "agent",
    "agents": "agents",
    "ai": "ai",
    "ai agent": "ai-agent",
    "agentmeasure": "agentmeasure",
    "ai native": "ai-native",
    "benchmark": "benchmark",
    "capability economy": "capability-economy",
    "caas": "caas",
    "context engineering": "context-engineering",
    "deepseek harness": "deepseek-harness",
    "measurement": "measurement",
    "产品研究": "product-research",
    "产品方法": "product-method",
    "产品判断": "product-judgment",
    "产品策略": "product-strategy",
    "产品设计": "product-design",
    "具身智能": "embodied-intelligence",
    "智能硬件": "smart-hardware",
    "机器人": "robots",
    "家庭机器人": "home-robots",
    "用户研究": "user-research",
    "研究方法": "research-methods",
    "研究盘点": "research-review",
    "计量": "metering",
    "大疆": "dji",
    "组织管理": "organization",
    "创业生态": "startup-ecosystem",
    "工程实践": "engineering",
    "商业化": "commercialization",
    "硬件": "hardware",
}

FRONT_MATTER = """---
layout: tag
title: "标签：{tag}"
permalink: /tags/{slug}/
tag: {tag}
{alt_line}count: {count}
lang: zh-CN
sitemap: true
generated: true
---

"""


def parse_tags(text: str) -> list:
    fm = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        return []
    body = fm.group(1)
    inline = re.search(r"^tags:\s*\[(.*)\]\s*$", body, re.M)
    tags = []
    if inline:
        tags = [t.strip().strip("\"'") for t in inline.group(1).split(",") if t.strip()]
    else:
        block = re.search(r"^tags:\s*\n((?:\s+-\s+.*\n?)+)", body, re.M)
        if block:
            tags = [ln.split("-", 1)[1].strip().strip("\"'") for ln in block.group(1).strip().splitlines()]
    return [t for t in tags if t]


def canonical(tag: str) -> str:
    """ASCII tags are case-folded so en/_posts ('agent') and _posts
    ('Agent') share one page; Chinese tags are kept as-is."""
    return tag.lower() if tag.isascii() else tag


def main() -> int:
    posts = list((ROOT / "_posts").glob("*.md")) + list((ROOT / "en" / "_posts").glob("*.md"))
    counter = Counter()
    display = Counter()  # most frequent original spelling per canonical key
    for p in posts:
        for t in parse_tags(p.read_text()):
            key = canonical(t)
            counter[key] += 1
            display[(key, t)] += 1

    wanted = {k: c for k, c in counter.items() if c >= MIN_POSTS}
    missing = [k for k in wanted if k not in TAG_SLUGS]
    if missing:
        print("ERROR: tags with 2+ posts but no slug mapping — add them to TAG_SLUGS:")
        for k in sorted(missing):
            print(f'    "{k}": "",  ({wanted[k]} posts)')
        return 1

    out_dir = ROOT / "tags"
    out_dir.mkdir(exist_ok=True)
    keep = set()
    for key, count in sorted(wanted.items(), key=lambda kv: (-kv[1], kv[0])):
        names = sorted({n for (k, n) in display if k == key})
        shown = max(names, key=lambda n: display[(key, n)])
        alt = next((n for n in names if n != shown), None)
        alt_line = f"tag_alt: {alt}\n" if alt else ""
        slug = TAG_SLUGS[key]
        path = out_dir / f"{slug}.md"
        path.write_text(FRONT_MATTER.format(tag=shown, slug=slug, alt_line=alt_line, count=count))
        keep.add(path.name)
        print(f"{count:>3}  {shown}  ->  /tags/{slug}/")

    stale = [p for p in out_dir.glob("*.md") if p.name not in keep]
    for p in stale:
        p.unlink()
        print(f"removed stale page: {p.name}")

    singles = sum(1 for t, c in counter.items() if c < MIN_POSTS)
    print(f"\n{len(wanted)} tag pages written, {singles} single-post tags stay as anchors on /tags/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
