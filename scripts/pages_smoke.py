#!/usr/bin/env python3
"""Smoke-test the static OSINT Roadmap site over HTTP."""

from __future__ import annotations

import argparse
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
    "contributors.html": "Contributors",
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
    "contributors.json",
    "robots.txt",
    "sitemap.xml",
    "feed.xml",
)

EXPECTED_PRODUCTION_ROOT = "https://imedkablavi.github.io/OSINT-Roadmap/"


def url_for(base: str, path: str) -> str:
    return urllib.parse.urljoin(base.rstrip("/") + "/", path)


def fetch(url: str, retries: int, delay: float) -> tuple[bytes, str]:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "OSINT-Roadmap-Pages-Smoke/1.0"})
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


def run(base_url: str, retries: int, delay: float) -> None:
    print(f"Smoke-testing {base_url}")
    for path, marker in EXPECTED_PAGES.items():
        body, content_type = fetch(url_for(base_url, path), retries, delay)
        text = body.decode("utf-8", errors="replace")
        require("text/html" in content_type, f"{path or '/'} is not HTML: {content_type}")
        require(marker.lower() in text.lower(), f"{path or '/'} is missing marker: {marker}")
        require("<html" in text.lower(), f"{path or '/'} does not look like HTML")
        print(f"PASS page: /{path}")

    resources: dict[str, bytes] = {}
    for path in STATIC_RESOURCES:
        body, _ = fetch(url_for(base_url, path), retries, delay)
        require(len(body) > 0, f"{path} is empty")
        resources[path] = body
        print(f"PASS resource: /{path}")

    tools = json.loads(resources["tools.json"].decode("utf-8"))
    require(isinstance(tools, list) and len(tools) >= 80, f"expected at least 80 tools, found {len(tools)}")
    names = [tool.get("name") for tool in tools]
    require(all(names) and len(names) == len(set(names)), "tool names must be present and unique")
    print(f"PASS catalogue: {len(tools)} tools")

    review = json.loads(resources["tool-review.json"].decode("utf-8"))
    require(review.get("catalog_reviewed"), "tool-review.json is missing catalog_reviewed")
    require(int(review.get("stale_after_days", 0)) >= 30, "stale_after_days is unexpectedly low")
    require(isinstance(review.get("overrides", {}), dict), "tool-review overrides must be an object")
    print(f"PASS freshness metadata: baseline {review['catalog_reviewed']}")

    search_index = json.loads(resources["search-index.json"].decode("utf-8"))
    require(isinstance(search_index, list) and len(search_index) >= 30, "search index unexpectedly small")
    require(any(item.get("lang") == "ar" for item in search_index), "search index is missing Arabic content")
    require(any(item.get("lang") == "tr" for item in search_index), "search index is missing Turkish content")
    require(any("playbook" in item.get("path", "").lower() for item in search_index), "search index is missing playbooks")
    print(f"PASS search index: {len(search_index)} documents")

    credits = json.loads(resources["contributors.json"].decode("utf-8"))
    contributors = credits.get("contributors", [])
    require(isinstance(contributors, list) and contributors, "contributors.json must contain at least one person")
    require(all(person.get("login") and person.get("html_url") for person in contributors), "contributors must have login and profile URL")
    require(not any(str(person.get("login", "")).endswith("[bot]") for person in contributors), "bots must not appear in contributor credits")
    print(f"PASS contributor credits: {len(contributors)} human account(s), source={credits.get('source')}")

    sitemap_text = resources["sitemap.xml"].decode("utf-8")
    ElementTree.fromstring(sitemap_text)
    for path in (
        "tool-finder.html", "search.html", "contributors.html", "osint-for-beginners.html",
        "username-osint.html", "reverse-image-osint.html", "domain-osint.html", "company-osint.html",
        "osint-tools.html", "geoint-guide.html", "ar/", "tr/",
    ):
        expected = EXPECTED_PRODUCTION_ROOT + path
        require(expected in sitemap_text, f"sitemap.xml is missing {expected}")
    print("PASS sitemap: valid XML and critical routes present")

    feed_text = resources["feed.xml"].decode("utf-8")
    ElementTree.fromstring(feed_text)
    require("OSINT Roadmap" in feed_text, "feed.xml is missing project identity")
    print("PASS feed: valid XML")

    robots_text = resources["robots.txt"].decode("utf-8")
    require("User-agent:" in robots_text, "robots.txt is missing User-agent")
    require(EXPECTED_PRODUCTION_ROOT + "sitemap.xml" in robots_text, "robots.txt does not advertise the production sitemap")
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
