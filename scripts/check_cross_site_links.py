#!/usr/bin/env python3
"""Cross-site link check: reachability *and* the link relationship.

A 200 on the target is only half the check. The other half is that the source
page the reader actually visits contains an href that resolves to that target.
Third-party timeouts must never block a deploy, so this script exits 0 unless
--strict is passed; the scheduled workflow surfaces failures as a red run.
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import urljoin

UA = "ovo-cross-site-check/2.0 (+https://roy-tong.github.io/)"

# label, target URL, body marker, source URL (None = no source-page assertion)
CHECKS = [
    ("blog home", "https://roy-tong.github.io/", "Roy.Tong", None),
    ("projects", "https://roy-tong.github.io/projects/", "Askovo", "https://roy-tong.github.io/"),
    ("root sitemap", "https://roy-tong.github.io/sitemap.xml", "<urlset", "https://roy-tong.github.io/robots.txt"),
    ("Askovo home", "https://roy-tong.github.io/Askovo/", "看一个具体需求判断", "https://roy-tong.github.io/projects/"),
    ("Askovo guide", "https://roy-tong.github.io/Askovo/guides/need-validation.html", "说了不算，做了才算", "https://roy-tong.github.io/Askovo/"),
    ("Growovo home", "https://roy-tong.github.io/Growovo/", "一次被闸门拦下的执行", "https://roy-tong.github.io/projects/"),
    ("Growovo autopsy", "https://roy-tong.github.io/Growovo/guides/launch-autopsy.html", "未完成可靠测量", "https://roy-tong.github.io/Growovo/"),
    ("Verovo home", "https://roy-tong.github.io/Verovo/", "26,563.25", "https://roy-tong.github.io/projects/"),
    ("Verovo invoice", "https://roy-tong.github.io/Verovo/blog/ai-invoice-reconciliation.html", "UNPROVABLE", "https://roy-tong.github.io/Verovo/"),
    ("Askovo sitemap", "https://roy-tong.github.io/Askovo/sitemap.xml", "<urlset", "https://roy-tong.github.io/robots.txt"),
    ("Growovo sitemap", "https://roy-tong.github.io/Growovo/sitemap.xml", "<urlset", "https://roy-tong.github.io/robots.txt"),
    ("Verovo sitemap", "https://roy-tong.github.io/Verovo/sitemap.xml", "ai-invoice-reconciliation", "https://roy-tong.github.io/robots.txt"),
]


def fetch(url: str) -> tuple[int, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return resp.status, resp.geturl(), resp.read(400_000).decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, url, ""
    except (urllib.error.URLError, TimeoutError) as exc:
        return 0, url, f"ERROR {exc}"


def links_in(page_url: str, body: str) -> set[str]:
    out = set()
    for raw in re.findall(r'href=["\']([^"\']+)["\']', body, re.I):
        if raw.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        out.add(urljoin(page_url, raw).split("#", 1)[0])
    for raw in re.findall(r"(?im)^\s*Sitemap:\s*(\S+)", body):
        out.add(raw.split("#", 1)[0])
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    failures = 0
    for label, target, marker, source in CHECKS:
        status, final, body = fetch(target)
        ok = status == 200 and marker in body
        detail = "" if ok else f" (status={status}, marker_present={marker in body})"
        if source:
            s_status, s_final, s_body = fetch(source)
            linked = target in links_in(s_final, s_body) if s_status == 200 else False
            ok = ok and linked
            detail += f" source={source} linked={linked}"
        print(f"{'OK  ' if ok else 'FAIL'} {label:18} {status} {target}{detail}")
        failures += 0 if ok else 1

    print(f"\ncross_site: {len(CHECKS) - failures}/{len(CHECKS)} checks passed")
    return 1 if (args.strict and failures) else 0


if __name__ == "__main__":
    sys.exit(main())
