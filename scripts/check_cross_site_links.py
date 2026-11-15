#!/usr/bin/env python3
"""Non-blocking cross-site link check.

The blog, Askovo, Growovo and Verovo live in four repositories but are read as
one surface. This script checks the public URLs that cross those boundaries and
reports status, final URL and a required body marker. It never fails the build
unless --strict is passed: a third-party timeout must not block a deploy.
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request

CHECKS = [
    ("blog home", "https://roy-tong.github.io/", "Roy.Tong"),
    ("projects", "https://roy-tong.github.io/projects/", "Askovo"),
    ("root sitemap", "https://roy-tong.github.io/sitemap.xml", "<urlset"),
    ("Askovo home", "https://roy-tong.github.io/Askovo/", "看一个具体需求判断"),
    ("Askovo guide", "https://roy-tong.github.io/Askovo/guides/need-validation.html", "说了不算，做了才算"),
    ("Growovo home", "https://roy-tong.github.io/Growovo/", "一次被闸门拦下的执行"),
    ("Growovo autopsy", "https://roy-tong.github.io/Growovo/guides/launch-autopsy.html", "未完成可靠测量"),
    ("Verovo home", "https://roy-tong.github.io/Verovo/", "26,563.25"),
    ("Verovo invoice", "https://roy-tong.github.io/Verovo/blog/ai-invoice-reconciliation.html", "UNPROVABLE"),
    ("Askovo sitemap", "https://roy-tong.github.io/Askovo/sitemap.xml", "<urlset"),
    ("Growovo sitemap", "https://roy-tong.github.io/Growovo/sitemap.xml", "<urlset"),
    ("Verovo sitemap", "https://roy-tong.github.io/Verovo/sitemap.xml", "ai-invoice-reconciliation"),
]

UA = "ovo-cross-site-check/1.0 (+https://roy-tong.github.io/)"


def fetch(url: str) -> tuple[int, str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read(200_000).decode("utf-8", "replace")
            return resp.status, resp.geturl(), body
    except urllib.error.HTTPError as exc:
        return exc.code, url, ""
    except (urllib.error.URLError, TimeoutError) as exc:
        return 0, url, f"ERROR {exc}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    failures = 0
    for label, url, marker in CHECKS:
        status, final, body = fetch(url)
        ok = status == 200 and marker in body
        if not ok:
            failures += 1
        print(f"{'OK  ' if ok else 'FAIL'} {label:18} {status} {url}"
              + ("" if final == url else f" -> {final}"))
        if status == 200 and marker not in body:
            print(f"     marker missing: {marker!r}")

    print(f"\ncross_site: {len(CHECKS) - failures}/{len(CHECKS)} checks passed")
    return 1 if (args.strict and failures) else 0


if __name__ == "__main__":
    sys.exit(main())
