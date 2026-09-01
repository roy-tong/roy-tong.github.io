#!/usr/bin/env python3
"""Read-only release checks for the public knowledge library (stdlib only).

Run after Jekyll build: python3 scripts/verify_knowledge.py
No source fetching, private-workspace access, or file writes.
"""
import csv
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
ERRORS = []
CHECKS = 0

def check(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        ERRORS.append(message)

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.counts = [], [], Counter()
        self.canonical = None
        self.text = path.read_text(encoding="utf-8")
        self.feed(self.text)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        self.counts[tag] += 1
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag in ("a", "link") and attributes.get("href"):
            self.links.append(attributes["href"])
        if tag in ("script", "img") and attributes.get("src"):
            self.links.append(attributes["src"])
        if tag == "link" and attributes.get("rel") == "canonical":
            self.canonical = attributes.get("href")

def target_for(url):
    path = unquote(urlsplit(url).path)
    target = SITE / path.lstrip("/")
    return target / "index.html" if not target.suffix else target

if not (SITE / "knowledge/index.json").is_file():
    sys.exit("Build the Jekyll site first.")

index = read_json(SITE / "knowledge/index.json")
records = index["records"]
topics = {item["id"] for item in index["topics"]}
sources = read_json(ROOT / "_data/research_sources.json")
source_ids = {item["id"] for item in sources}
notes = {item["id"].removeprefix("knowledge-"): item for item in records if item["kind"] == "knowledge"}
articles = {item["url"]: item for item in records if item["kind"] == "article"}

check(len(topics) == 6, "Expected the six approved themes.")
check(len(notes) >= 20, "Knowledge release is missing required notes.")
check(len(sources) == len(source_ids), "Source IDs must be unique.")
check(len(records) == len({r["id"] for r in records}), "Index IDs must be unique.")
check(len(records) == len({r["url"] for r in records}), "Index URLs must be unique.")
expected_articles = list((ROOT / "_posts").glob("*.md")) + list((ROOT / "en/_posts").glob("*.md"))
check(len(articles) == len(expected_articles), "Article index does not cover the current post collection.")
# These publications were deliberately moved out of the article stream before v2.
standalone_publications = {"/notes/embodied-intelligence-beginners-guide/", "/notes/agent-usage-measurement-standard/"}
for publication_url in standalone_publications:
    check(target_for(publication_url).is_file(), "Moved publication lost its original URL: " + publication_url)
check(sum(r["lang"] == "en" for r in articles.values()) >= 10, "Existing English editions are missing.")
for row in records:
    check(row["topic"] in topics, "Unknown topic: " + row["id"])
    check(row["kind"] in ("knowledge", "article", "project"), "Unknown type: " + row["id"])
    minimum_text_length = 20 if row["kind"] == "project" else 300
    check(len(row.get("text", "")) > minimum_text_length, "Empty or implausibly short indexed text: " + row["id"])
    check(bool(row.get("summary")), "Missing summary: " + row["id"])
    for slug in row.get("related") or []:
        check(slug in notes, "Missing related note: " + row["id"] + " -> " + slug)
    for sid in row.get("source_ids") or []:
        check(sid in source_ids, "Missing source ID: " + sid)
    for url in row.get("related_articles") or []:
        check(url in articles or url in standalone_publications and target_for(url).is_file(),
              "Missing related publication: " + row["id"] + " -> " + url)
    if row.get("translation_of"):
        original = row["translation_of"]
        check(original in articles or original in standalone_publications and target_for(original).is_file(),
              "Missing original of translation: " + row["id"])
    if row["kind"] != "project":
        check(target_for(row["url"]).is_file(), "Missing rendered page: " + row["url"])

sitemap = ET.parse(SITE / "sitemap.xml")
sitemap_urls = [n.text for n in sitemap.findall(".//{*}loc")]
check(len(sitemap_urls) == len(set(sitemap_urls)), "Duplicate sitemap URLs.")
pages = list((SITE / "knowledge").rglob("*.html"))
pages += [SITE / "notes" / slug / "index.html" for slug in
          ("ai-video-second-edit", "local-ai-box-task-economics", "home-robots-recovery-burden")]
parsed = {}
for path in pages:
    parsed[path] = Page(path)
    p = parsed[path]
    page_url = "https://roy-tong.github.io/" + path.relative_to(SITE).as_posix().removesuffix("index.html")
    check(p.counts["h1"] == 1, "Expected one h1: " + str(path.relative_to(SITE)))
    check(len(p.ids) == len(set(p.ids)), "Duplicate IDs: " + str(path.relative_to(SITE)))
    check(p.canonical == page_url, "Incorrect canonical URL: " + str(path.relative_to(SITE)))
    check(page_url in sitemap_urls, "Page absent from sitemap: " + page_url)

# Inspect links from new knowledge pages and the three new essays.
# Other GitHub Pages projects have separate deployments, not files in this repo.
separate_projects = ("/AgentMeasure/",)
checked_links = 0
for path, page in list(parsed.items()):
    page_url = "https://roy-tong.github.io/" + path.relative_to(SITE).as_posix()
    for href in page.links:
        url = urlsplit(urljoin(page_url, href))
        if url.scheme not in ("http", "https") or url.hostname != "roy-tong.github.io":
            continue
        if any(url.path.startswith(prefix) for prefix in separate_projects):
            continue
        target = target_for(url.geturl())
        check(target.is_file(), "Broken internal link: " + str(path.relative_to(SITE)) + " -> " + href)
        checked_links += 1
        if target.is_file() and target.suffix == ".html" and url.fragment:
            destination = parsed.setdefault(target, Page(target))
            if url.path == "/knowledge/library/" and url.fragment.startswith("collection="):
                collection_id = url.fragment.split("=", 1)[1]
                known = {c["id"] for c in read_json(ROOT / "_data/research_collections.json")}
                check(collection_id in known, "Unknown collection filter: " + href)
            else:
                check(unquote(url.fragment) in destination.ids, "Broken anchor: " + href)

# Existing posts are retained and receive a current related-knowledge entry.
for url, row in articles.items():
    path = target_for(url)
    if path.exists():
        body = path.read_text(encoding="utf-8")
        marker = "Related research materials" if row["lang"] == "en" else "相关研究资料"
        check(marker in body, "Article missing knowledge backlink: " + url)

data = read_json(ROOT / "_data/research_corpora_20260831.json")
rendered = read_json(SITE / "knowledge/data/research-corpora-2026-08-31.json")
check(data == rendered, "Published aggregate JSON differs from its reviewed source.")
with (SITE / "knowledge/data/corpus-summary-2026-08-31.csv").open(encoding="utf-8", newline="") as stream:
    csv_summary = {row["study_id"]: row for row in csv.DictReader(stream)}
for study in data["studies"]:
    count = study["record_count"]
    check(sum(study["platform_counts"].values()) == count, "Platform counts do not sum: " + study["id"])
    check(sum(study["machine_evidence_label_counts"].values()) == count, "Label counts do not sum: " + study["id"])
    check(abs(study["largest_source_records"] / count * 100 - study["largest_source_share_pct"]) < 0.0001,
          "Incorrect share: " + study["id"])
    check(re.fullmatch(r"[0-9a-f]{64}", study["input_sha256"]) is not None, "Invalid snapshot digest.")
    check(study["semantic_label_validation"] == "not-performed-in-this-recount", "Review scope changed.")
    check(int(csv_summary[study["id"]]["record_count"]) == count, "CSV summary mismatch.")
    check(int(csv_summary[study["id"]]["missing_stored_text_hashes"]) == study["missing_stored_text_hashes"],
          "CSV missing-hash count mismatch.")
for filename, field, key in [
    ("platform-counts-2026-08-31.csv", "platform_counts", "platform"),
    ("machine-labels-2026-08-31.csv", "machine_evidence_label_counts", "machine_candidate_label"),
]:
    with (SITE / "knowledge/data" / filename).open(encoding="utf-8", newline="") as stream:
        actual = {(r["study_id"], r[key]): int(r["record_count"]) for r in csv.DictReader(stream)}
    expected = {(s["id"], k): v for s in data["studies"] for k, v in s[field].items()}
    check(actual == expected, "CSV content mismatch: " + filename)

# No-script access: materials in the full catalogue; articles in their own archive.
catalog = Page(SITE / "knowledge/library/index.html")
for row in notes.values():
    check(row["url"] in catalog.links, "Missing static/no-script directory link: " + row["url"])
article_archive = Page(SITE / "archive/index.html")
for row in articles.values():
    archive = Page(SITE / "en/archive/index.html") if row["lang"] == "en" else article_archive
    check(row["url"] in archive.links, "Article missing from its static archive: " + row["url"])
check("<noscript>" in catalog.text, "No-script guidance missing.")
check(re.search(r'data-library-form[^>]*hidden', catalog.text),
      "Search must not appear interactive before initialization.")
check('credentials: \'omit\'' in (ROOT / "assets/js/knowledge-search.js").read_text(), "Search must not send credentials.")

# Scan only the newly distributed rendered surfaces; print paths, never matches.
sensitive = [
    re.compile(r"/Users/|file:///|feishu-staging|roy-memory", re.I),
    re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    re.compile(r"(?i)(?:app[_ -]?secret|api[_ -]?key|password)\s*[:=]\s*[\"']?[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?:ghp_|github_pat_)[A-Za-z0-9_]{25,}"),
]
scan = pages + [SITE / "knowledge/index.json", SITE / "knowledge/data/research-corpora-2026-08-31.json"]
for path in scan:
    body = path.read_text(encoding="utf-8")
    for pattern in sensitive:
        check(not pattern.search(body), "Possible private data in " + str(path.relative_to(SITE)))
for forbidden in ("PRODUCT.md", "README.md", "docs", "scripts", ".impeccable", "_knowledge", "_materials", "_data"):
    check(not (SITE / forbidden).exists(), "Build exposes an excluded source path: " + forbidden)
feed = (SITE / "feed.xml").read_text(encoding="utf-8")
for slug in ("ai-video-second-edit", "local-ai-box-task-economics", "home-robots-recovery-burden"):
    check("/notes/" + slug + "/" in feed, "New essay missing from RSS: " + slug)

print(json.dumps({"checks": CHECKS, "rendered_pages_checked": len(pages), "internal_links_checked": checked_links,
                  "index_records": len(records), "knowledge_notes": len(notes), "article_pages": len(articles),
                  "errors": ERRORS}, ensure_ascii=False, indent=2))
sys.exit(1 if ERRORS else 0)
