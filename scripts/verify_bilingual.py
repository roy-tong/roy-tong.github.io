#!/usr/bin/env python3
"""Report bilingual article coverage; use --strict to fail on any gap."""

import argparse
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def parse_post(path, english):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not match:
        raise ValueError(f"{path}: missing front matter")
    front_matter = match.group(1)

    def field(name):
        found = re.search(rf"^{name}:\s*[\"']?([^\"'\n]+?)[\"']?\s*$", front_matter, re.M)
        return found.group(1).strip() if found else None

    permalink = field("permalink")
    if not permalink and not english:
        permalink = f"/notes/{path.stem[11:]}/"
    slug_match = re.search(r"/(?:en/)?notes/([^/]+)/", permalink or "")
    content_id = field("content_id") or (slug_match.group(1) if slug_match else path.stem[11:])
    expected_prefix = "/en/notes/" if english else "/notes/"
    if not permalink or not permalink.startswith(expected_prefix):
        raise ValueError(f"{path}: permalink must start with {expected_prefix}")
    language = field("lang") or "zh-CN"
    if english and language not in {"en", "en-US"}:
        raise ValueError(f"{path}: English post has lang={language}")
    if not english and language in {"en", "en-US"}:
        raise ValueError(f"{path}: Chinese post has lang={language}")
    return content_id, permalink


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="fail when either language is missing")
    args = parser.parse_args()
    posts = defaultdict(lambda: {"zh": [], "en": []})
    errors = []

    for english, folder, key in [(False, "_posts", "zh"), (True, "en/_posts", "en")]:
        for path in sorted((ROOT / folder).glob("*.md")):
            try:
                content_id, permalink = parse_post(path, english)
                posts[content_id][key].append(permalink)
            except ValueError as error:
                errors.append(str(error))

    for english, folder, key in [(False, "notes", "zh"), (True, "en/notes", "en")]:
        for path in sorted((ROOT / folder).glob("*/index.html")):
            content_id = path.parent.name
            if english and content_id.endswith("-zh") and posts[content_id[:-3]]["zh"]:
                content_id = content_id[:-3]
            permalink = f"/{'en/' if english else ''}notes/{path.parent.name}/"
            if not posts[content_id][key]:
                posts[content_id][key].append(permalink)

    for content_id, editions in posts.items():
        if not editions["zh"] and (ROOT / "_site" / "notes" / content_id / "index.html").exists():
            editions["zh"].append(f"/notes/{content_id}/")

    for content_id, editions in posts.items():
        for language, urls in editions.items():
            if len(urls) > 1:
                errors.append(f"{content_id}: duplicate {language} editions: {', '.join(urls)}")

    missing_en = sorted(content_id for content_id, editions in posts.items() if editions["zh"] and not editions["en"])
    missing_zh = sorted(content_id for content_id, editions in posts.items() if editions["en"] and not editions["zh"])
    paired = sum(1 for editions in posts.values() if editions["zh"] and editions["en"])
    zh_count = sum(len(editions["zh"]) for editions in posts.values())
    en_count = sum(len(editions["en"]) for editions in posts.values())

    print(f"Articles: {zh_count} Chinese, {en_count} English, {paired} paired")
    print(f"Missing English ({len(missing_en)}): {', '.join(missing_en) or 'none'}")
    print(f"Missing Chinese ({len(missing_zh)}): {', '.join(missing_zh) or 'none'}")
    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")

    if errors or (args.strict and (missing_en or missing_zh)):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
