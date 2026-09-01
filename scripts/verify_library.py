#!/usr/bin/env python3
"""Verify the material library's public release contracts (read-only, stdlib)."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
ERRORS = []
CHECKS = 0


def check(value, message):
    global CHECKS
    CHECKS += 1
    if not value:
        ERRORS.append(message)


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def local_target(url):
    parsed = urlsplit(url)
    check(not parsed.netloc and parsed.path.startswith('/'), 'Unexpected non-local material URL: ' + url)
    file = SITE / unquote(parsed.path).lstrip('/')
    return file if file.suffix else file / 'index.html'


class Markup(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids, self.material_ids, self.material_urls, self.links, self.images = [], [], [], [], []
        self.h1 = 0
        self.canonical = None
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if 'data-material' in a:
            self.material_ids.append(a['data-id'])
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'img' and a.get('src'):
            self.images.append(a['src'])
        if tag == 'h1':
            self.h1 += 1
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href')


if not (SITE / 'knowledge/materials.json').is_file():
    sys.exit('Build the site before checking the material library.')

index = read(SITE / 'knowledge/materials.json')
records = index['records']
collections = read(ROOT / '_data/research_collections.json')
types = read(ROOT / '_data/research_material_types.json')
type_ids = {t['id'] for t in types}
ids = {r['id'] for r in records}
by_slug = {r['slug']: r for r in records}
catalog = Markup(SITE / 'knowledge/library/index.html')
sitemap_urls = {n.text for n in ET.parse(SITE / 'sitemap.xml').findall('.//{*}loc')}
legacy = read(SITE / 'knowledge/index.json')
article_urls = {r['url'] for r in legacy['records'] if r['kind'] == 'article'}

check(index['schema_version'] == '3.0', 'Unexpected public material schema.')
check(index['types'] == types and index['collections'] == collections, 'Index metadata differs from canonical definitions.')
check(len(ids) == len(records), 'Duplicate material ID.')
check(len(by_slug) == len(records), 'Duplicate material slug.')
check(len({r['url'] for r in records}) == len(records), 'Duplicate material canonical URL.')
source_count = len(list((ROOT / '_knowledge').glob('*.md'))) + len(list((ROOT / '_materials').glob('*.md')))
check(len(records) == source_count, 'Source files and material index differ in coverage.')
check(set(catalog.material_ids) == ids and len(catalog.material_ids) == len(records), 'No-script directory must contain every material exactly once.')
check(not article_urls.intersection({r['url'] for r in records}), 'Article pages must not be counted as material records.')
check({r['kind'] for r in records} <= type_ids, 'Unknown material type.')
check(legacy.get('materials_index') == '/knowledge/materials.json', 'Legacy index does not point to material index.')

for record in records:
    ident = record['id']
    check(bool(record['title'] and record['summary'] and record['version'] and record['access']), 'Missing useful material metadata: ' + ident)
    check(all(record.get(field) for field in ('use_for', 'public_scope', 'boundary', 'review_status')),
          'Missing use or evidence boundary: ' + ident)
    check(bool(re.fullmatch(r'\d{4}-\d{2}-\d{2}', record['updated'])), 'Missing date: ' + ident)
    check(len(record.get('text', '')) > 200, 'No useful searchable content: ' + ident)
    expected_collections = {c['id'] for c in collections if record['slug'] in c['notes'] + c['materials']}
    check(set(record['collections']) == expected_collections and bool(expected_collections), 'Broken topic membership: ' + ident)
    target = local_target(record['url'])
    check(target.is_file(), 'Missing material page: ' + ident)
    check(record['url'] in catalog.links, 'Missing no-script material link: ' + ident)
    if target.is_file():
        page = Markup(target)
        check(page.h1 == 1 and len(page.ids) == len(set(page.ids)), 'Invalid headings or duplicate IDs: ' + ident)
        check(page.canonical == 'https://roy-tong.github.io' + record['url'], 'Wrong canonical: ' + ident)
        check(page.canonical in sitemap_urls, 'Material absent from sitemap: ' + ident)
        for cid in record['collections']:
            check('/knowledge/collections/' + cid + '/' in page.links, 'Missing return link to collection: ' + ident)
    for download in record.get('downloads') or []:
        target = local_target(download['url'])
        check(target.is_file() and target.stat().st_size > 0, 'Missing or empty download: ' + ident)
    if record.get('source_page'):
        canonical = 'https://roy-tong.github.io' + record['source_page']
        check(local_target(record['source_page']).is_file(), 'Lost original report address: ' + ident)
        check(canonical in sitemap_urls, 'Original report missing from sitemap: ' + ident)

for collection in collections:
    page = Markup(local_target('/knowledge/collections/' + collection['id'] + '/'))
    expected = {by_slug[slug]['id'] for slug in collection['notes'] + collection['materials'] if slug in by_slug}
    check(len(expected) == len(collection['notes'] + collection['materials']), 'Missing or duplicate collection member: ' + collection['id'])
    check(set(page.material_ids) == expected, 'Collection page shows the wrong material set: ' + collection['id'])
    for url in collection['articles']:
        check(url in article_urls and url in page.links, 'Broken related article: ' + url)
        if local_target(url).is_file():
            article = Markup(local_target(url))
            check('/knowledge/collections/' + collection['id'] + '/' in article.links,
                  'Article lacks its reciprocal collection link: ' + url)

corpora = read(ROOT / '_data/research_corpora_20260831.json')
files = {'local-ai-2024': 'local-ai-summary.json', 'ai-glasses-2023': 'ai-glasses-summary.json', 'home-robots-2023': 'home-robots-summary.json'}
for study in corpora['studies']:
    exported = read(SITE / 'knowledge/data' / files[study['id']])
    check(exported['study'] == study, 'Per-study download changed reviewed data: ' + study['id'])
    check('aggregate-only' in exported['release_scope'] and len(exported['limitations']) >= 3, 'Missing public-data boundary.')
    matches = [r for r in records if r.get('study_id') == study['id']]
    check(len(matches) == 1 and matches[0]['kind'] == 'data', 'Each study needs one material record.')
    check(matches[0]['access'] == '仅汇总数据', 'Aggregate must not be advertised as raw data.')

book = by_slug['embodied-field-guide']
check(book['access'] == '公开试读', 'Do not advertise the paid/partial book as full text.')
check('前 12 页' in book['summary'], 'Trial scope missing from catalogue.')

# Scan every new public index or material page without inspecting private inputs.
private_patterns = [re.compile(p, re.I) for p in [
    r'/Users/|file:///|feishu-staging|source-inventory\.json|publication-candidates\.json',
    r'feishu_node_token|feishu_document_token|feishu_url|local_path|policy_hint',
    r'BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY',
    r'(?:ghp_|github_pat_)[A-Za-z0-9_]{25,}',
    r'(?:app[_ -]?secret|api[_ -]?key|password)\s*[:=]\s*["\']?[A-Za-z0-9_-]{20,}',
]]
for path in (SITE / 'knowledge').rglob('*'):
    if path.is_file() and path.suffix in {'.html', '.json', '.csv'}:
        text = path.read_text(encoding='utf-8')
        for pattern in private_patterns:
            check(not pattern.search(text), 'Possible private data in public output: ' + str(path.relative_to(SITE)))
check(not (SITE / '_materials').exists(), 'Source collection directory exposed.')
check(not (SITE / 'PRODUCT.md').exists(), 'Private product configuration exposed.')

print(json.dumps({'checks': CHECKS, 'materials': len(records), 'types': dict(Counter(r['kind'] for r in records)),
                  'collections': len(collections), 'errors': ERRORS}, ensure_ascii=False, indent=2))
sys.exit(1 if ERRORS else 0)
