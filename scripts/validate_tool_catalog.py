#!/usr/bin/env python3
"""Validate structured OSINT catalogues and Tool Finder trust metadata."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

SITE = Path(__file__).resolve().parents[1] / "site"
CATALOGS = (SITE / "tools.json", SITE / "tools-specialist.json")
TRUST = SITE / "tool-trust.json"
REQUIRED = {"name", "url", "category", "input", "cost", "level", "note"}
LEVELS = {"Beginner", "Intermediate", "Advanced"}
SOURCE_TYPES = {
    "Official primary source",
    "Registry / primary source",
    "Public dataset / index",
    "Community / secondary source",
    "Open-source tool",
    "Hosted service / resource",
}


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


def load_trust() -> dict:
    try:
        trust = json.loads(TRUST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{TRUST.name}: {exc}")
    if not isinstance(trust, dict):
        fail(f"{TRUST.name}: root must be an object")
    return trust


def validate_trust(trust: dict, catalogue_names: set[str]) -> None:
    if trust.get("schema_version") != 1:
        fail("tool-trust.json: schema_version must be 1")

    default_type = trust.get("default_source_type")
    if default_type not in SOURCE_TYPES:
        fail(f"tool-trust.json: invalid default_source_type {default_type!r}")

    default_jurisdiction = trust.get("default_jurisdiction")
    if not isinstance(default_jurisdiction, str) or not default_jurisdiction.strip():
        fail("tool-trust.json: default_jurisdiction must be a non-empty string")

    metadata = trust.get("entries")
    if not isinstance(metadata, dict):
        fail("tool-trust.json: entries must be an object keyed by exact tool name")

    unknown = sorted(set(metadata) - catalogue_names)
    if unknown:
        fail(f"tool-trust.json: unknown tool names: {', '.join(unknown)}")

    for name, fields in metadata.items():
        if not isinstance(fields, dict):
            fail(f"{name}: trust metadata must be an object")
        source_type = fields.get("source_type")
        if source_type not in SOURCE_TYPES:
            fail(f"{name}: invalid source_type {source_type!r}")
        jurisdiction = fields.get("jurisdiction")
        if not isinstance(jurisdiction, str) or not jurisdiction.strip() or len(jurisdiction) > 80:
            fail(f"{name}: jurisdiction must be a non-empty string up to 80 characters")

    print(f"Validated trust metadata for {len(metadata)} explicitly classified resources.")


def main() -> None:
    entries = load_catalogues()
    names: set[str] = set()
    catalogue_names: set[str] = set()
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
        catalogue_names.add(name)

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

    validate_trust(load_trust(), catalogue_names)
    print(f"Validated {len(entries)} curated tools across {len(CATALOGS)} catalogues; no duplicate names or URLs found.")


if __name__ == "__main__":
    main()