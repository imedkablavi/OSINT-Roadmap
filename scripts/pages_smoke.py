#!/usr/bin/env python3
"""Smoke-test the static OSINT Roadmap site over HTTP.

The same checks run against a local server in pull requests and against the
real GitHub Pages URL after deployment is enabled.
"""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from xml.etree import ElementTree

EXPECTED_PAGES = {
    "": "OSINT Roadmap",
    "learn-osint.html": "OSINT",
    "osint-tools.html": "OSINT",
    "tool-finder.html": "OSINT Tool Finder",
    "search.html": "Search the OSINT Roadmap",
    "osint-for-beginners.html": "OSINT for Beginners",
    "username-osint.html": "Username OSINT",
    "reverse-image-osint.html": "Reverse Image OSINT",
    "domain-osint.html": "Domain OSINT",
    "company-osint.html": "Company OSINT",
    "geoint-guide.html": "GEOINT",
    "cti-osint.html": "OSINT",
    "digital-footprint.html": "Digital",
    "company-investigation.html": "Company",
    "ar/": "OSINT",
    "tr/": "OSINT",
}

STATIC_RESOURCES = (
    "style.css",
    "tools.json",
    "tool-review.json",
    "search-index.json",
    "robots.txt",
    "sitemap.xml",
    "feed.xml",
)

EXPECTED_PRODUCTION_ROOT = "https://imedkablavi.github.io/OSINT-Roadmap/"
LANGUAGE_ROUTES = {
    "": ("en", EXPECTED_PRODUCTION_ROOT),
    "ar/": ("ar", EXPECTED_PRODUCTION_ROOT + "ar/"),
    "tr/": ("tr", EXPECTED_PRODUCTION_ROOT + "tr/"),
}


class LinkExtractor(HTMLParser):
    """Collect real href attributes from parsed HTML tags only.

    This deliberately ignores tag-looking strings inside script/template text,
    preventing JavaScript snippets such as href=\"${t.url}\" from being treated
    as deployed routes.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name.lower() == "href" and value:
                self.hrefs.append(value)


def url_for(base: str, path: str) -> str:
    return urllib.parse.urljoin(base.rstrip("/") + "/", path)


def fetch(url: str, retries: int, delay: float) -> tuple[bytes, str]:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "OSINT-Roadmap-Pages-Smoke/1.0"},
            )
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status != 200:
                    raise RuntimeError(f"HTTP {response.status}")
                return response.read(), response.headers.get("Content-Type", "")
        except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(delay)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def require_metadata(path: str, text: str, lang: str, canonical: str) -> None:
    lower = text.lower()
    require(f'<html lang="{lang}"' in lower, f"/{path} has wrong or missing lang attribute")
    if lang == "ar":
        require('dir="rtl"' in lower, "/ar/ is missing RTL direction")
    require(f'rel="canonical" href="{canonical}"' in text, f"/{path} has wrong canonical")
    for hreflang, href in (
        ("en", EXPECTED_PRODUCTION_ROOT),
        ("ar", EXPECTED_PRODUCTION_ROOT + "ar/"),
        ("tr", EXPECTED_PRODUCTION_ROOT + "tr/"),
        ("x-default", EXPECTED_PRODUCTION_ROOT),
    ):
        require(
            f'hreflang="{hreflang}" href="{href}"' in text,
            f"/{path} missing hreflang={hreflang}",
        )
    require('type="application/rss+xml"' in lower, f"/{path} is missing RSS discovery")
    require('type="application/ld+json"' in lower, f"/{path} is missing structured data")
    require('property="og:title"' in lower, f"/{path} is missing Open Graph metadata")
    require('name="twitter:card"' in lower, f"/{path} is missing Twitter card metadata")


def require_internal_routes(base_url: str, text: str, page_path: str, retries: int, delay: float) -> None:
    parser = LinkExtractor()
    parser.feed(text)
    checked: set[str] = set()
    for href in parser.hrefs:
        parsed = urllib.parse.urlparse(href)
        if parsed.scheme or parsed.netloc or href.startswith(("#", "mailto:", "tel:", "javascript:")):
            continue
        target = urllib.parse.urljoin(url_for(base_url, page_path), href)
        parsed_target = urllib.parse.urlparse(target)
        if parsed_target.path.lower().endswith((".css", ".js", ".json", ".xml", ".ico", ".svg", ".png", ".jpg", ".jpeg", ".webp")):
            continue
        clean_target = urllib.parse.urlunparse(parsed_target._replace(fragment=""))
        if clean_target in checked:
            continue
        checked.add(clean_target)
        fetch(clean_target, retries, delay)


def run(base_url: str, retries: int, delay: float) -> None:
    print(f"Smoke-testing {base_url}")

    page_texts: dict[str, str] = {}
    for path, marker in EXPECTED_PAGES.items():
        body, content_type = fetch(url_for(base_url, path), retries, delay)
        text = body.decode("utf-8", errors="replace")
        page_texts[path] = text
        require("text/html" in content_type, f"{path or '/'} is not HTML: {content_type}")
        require(marker.lower() in text.lower(), f"{path or '/'} is missing marker: {marker}")
        require("<html" in text.lower(), f"{path or '/'} does not look like HTML")
        require_internal_routes(base_url, text, path, retries, delay)
        print(f"PASS page + internal routes: /{path}")

    for path, (lang, canonical) in LANGUAGE_ROUTES.items():
        require_metadata(path, page_texts[path], lang, canonical)
        print(f"PASS metadata: /{path}")

    resources: dict[str, bytes] = {}
    for path in STATIC_RESOURCES:
        body, _ = fetch(url_for(base_url, path), retries, delay)
        require(len(body) > 0, f"{path} is empty")
        resources[path] = body
        print(f"PASS resource: /{path}")

    tools = json.loads(resources["tools.json"].decode("utf-8"))
    require(isinstance(tools, list), "tools.json must contain a JSON array")
    require(len(tools) >= 80, f"expected at least 80 tools, found {len(tools)}")
    names = [tool.get("name") for tool in tools]
    require(all(names), "every tool must have a name")
    require(len(names) == len(set(names)), "tools.json contains duplicate tool names")
    print(f"PASS catalogue: {len(tools)} tools")

    review = json.loads(resources["tool-review.json"].decode("utf-8"))
    require(review.get("catalog_reviewed"), "tool-review.json is missing catalog_reviewed")
    require(int(review.get("stale_after_days", 0)) >= 30, "stale_after_days is unexpectedly low")
    require(isinstance(review.get("overrides", {}), dict), "tool-review overrides must be an object")
    print(f"PASS freshness metadata: baseline {review['catalog_reviewed']}")

    search_index = json.loads(resources["search-index.json"].decode("utf-8"))
    require(isinstance(search_index, list), "search-index.json must contain a JSON array")
    require(len(search_index) >= 30, f"search index unexpectedly small: {len(search_index)}")
    require(any(item.get("lang") == "ar" for item in search_index), "search index is missing Arabic content")
    require(any(item.get("lang") == "tr" for item in search_index), "search index is missing Turkish content")
    require(any("playbook" in item.get("path", "").lower() for item in search_index), "search index is missing playbooks")
    print(f"PASS search index: {len(search_index)} documents")

    sitemap_text = resources["sitemap.xml"].decode("utf-8")
    ElementTree.fromstring(sitemap_text)
    for path in EXPECTED_PAGES:
        expected = EXPECTED_PRODUCTION_ROOT + path
        require(expected in sitemap_text, f"sitemap.xml is missing {expected}")
    print("PASS sitemap: valid XML and all smoke-tested routes present")

    feed_text = resources["feed.xml"].decode("utf-8")
    ElementTree.fromstring(feed_text)
    require("OSINT Roadmap" in feed_text, "feed.xml is missing project identity")
    require(EXPECTED_PRODUCTION_ROOT in feed_text, "feed.xml is missing production project URL")
    print("PASS feed: valid XML")

    robots_text = resources["robots.txt"].decode("utf-8")
    require("User-agent:" in robots_text, "robots.txt is missing User-agent")
    require(
        EXPECTED_PRODUCTION_ROOT + "sitemap.xml" in robots_text,
        "robots.txt does not advertise the production sitemap",
    )
    print("PASS robots.txt: sitemap advertised")

    print("Pages smoke test passed.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--retry-delay", type=float, default=2.0)
    args = parser.parse_args()

    try:
        run(args.base_url, max(args.retries, 1), max(args.retry_delay, 0))
    except (AssertionError, RuntimeError, ValueError, json.JSONDecodeError, ElementTree.ParseError) as exc:
        print(f"SMOKE TEST FAILED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
