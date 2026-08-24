#!/usr/bin/env python3
"""Validate all structured OSINT catalogues used by the Pages Tool Finder."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

SITE = Path(__file__).resolve().parents[1] / "site"
CATALOGS = (SITE / "tools.json", SITE / "tools-specialist.json")
REQUIRED = {"name", "url", "category", "input", "cost", "level", "note"}
LEVELS = {"Beginner", "Intermediate", "Advanced"}


def fail(message: str) -> None:
    raise SystemExit(f"tool-catalog validation failed: {message}")


def valid_https_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def load_catalogues() -> list[tuple[str, dict]]:
    combined: list[tuple[str, dict]] = []
    for path in CATALOGS:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{path.name}: {exc}")
        if not isinstance(data, list) or not data:
            fail(f"{path.name}: catalogue must be a non-empty JSON array")
        for item in data:
            combined.append((path.name, item))
    return combined


def main() -> None:
    entries = load_catalogues()
    names: set[str] = set()
    urls: set[str] = set()

    for index, (catalogue_name, item) in enumerate(entries, start=1):
        where = f"{catalogue_name} entry {index}"
        if not isinstance(item, dict):
            fail(f"{where} is not an object")

        missing = REQUIRED - item.keys()
        if missing:
            fail(f"{where} is missing: {', '.join(sorted(missing))}")

        name = str(item["name"]).strip()
        url = str(item["url"]).strip()
        level = str(item["level"]).strip()
        inputs = item["input"]

        if not name:
            fail(f"{where} has an empty name")
        if name.casefold() in names:
            fail(f"duplicate tool name across catalogues: {name}")
        names.add(name.casefold())

        if not valid_https_url(url):
            fail(f"{name}: URL must be an absolute HTTPS URL")
        if url.casefold() in urls:
            fail(f"duplicate tool URL across catalogues: {url}")
        urls.add(url.casefold())

        if level not in LEVELS:
            fail(f"{name}: invalid level {level!r}")
        if not isinstance(inputs, list) or not inputs or not all(isinstance(v, str) and v.strip() for v in inputs):
            fail(f"{name}: input must be a non-empty list of strings")

        for field in ("category", "cost", "note"):
            if not isinstance(item[field], str) or not item[field].strip():
                fail(f"{name}: {field} must be a non-empty string")

        if "open_source" in item and not isinstance(item["open_source"], bool):
            fail(f"{name}: open_source must be a boolean when present")

        if item.get("open_source") is True:
            license_name = item.get("license")
            source_url = item.get("source_url")
            if not isinstance(license_name, str) or not license_name.strip():
                fail(f"{name}: open-source entries must declare a license")
            if not isinstance(source_url, str) or not valid_https_url(source_url.strip()):
                fail(f"{name}: open-source entries must declare an absolute HTTPS source_url")

    print(f"Validated {len(entries)} curated tools across {len(CATALOGS)} catalogues; no duplicate names or URLs found.")


if __name__ == "__main__":
    main()
