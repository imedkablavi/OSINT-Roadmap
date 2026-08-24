#!/usr/bin/env python3
"""Check review age for every curated tool independently of link availability."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL_FILES = (ROOT / "site" / "tools.json", ROOT / "site" / "tools-specialist.json")
REVIEW = ROOT / "site" / "tool-review.json"


def parse_date(value: str) -> dt.date:
    return dt.date.fromisoformat(value)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--today", help="ISO date override for deterministic tests")
    parser.add_argument("--warn-only", action="store_true")
    args = parser.parse_args()

    today = parse_date(args.today) if args.today else dt.datetime.now(dt.timezone.utc).date()
    tools = []
    for path in TOOL_FILES:
        tools.extend(json.loads(path.read_text(encoding="utf-8")))
    review = json.loads(REVIEW.read_text(encoding="utf-8"))

    baseline = parse_date(review["catalog_reviewed"])
    threshold = int(review.get("stale_after_days", 120))
    overrides = review.get("overrides", {})

    names = {tool["name"] for tool in tools}
    unknown = sorted(set(overrides) - names)
    if unknown:
        print("Unknown review overrides:")
        for name in unknown:
            print(f"  - {name}")
        return 1

    stale: list[tuple[int, str, dt.date]] = []
    future: list[tuple[str, dt.date]] = []
    ages: list[int] = []

    for tool in tools:
        reviewed = parse_date(overrides.get(tool["name"], review["catalog_reviewed"]))
        if reviewed > today:
            future.append((tool["name"], reviewed))
            continue
        age = (today - reviewed).days
        ages.append(age)
        if age > threshold:
            stale.append((age, tool["name"], reviewed))

    print(f"Freshness audit: {len(tools)} tools across {len(TOOL_FILES)} catalogues; stale threshold {threshold} days")
    print(f"Oldest review age: {max(ages, default=0)} days")
    print(f"Per-tool overrides: {len(overrides)}")

    if future:
        print("Review dates in the future:")
        for name, reviewed in future:
            print(f"  - {name}: {reviewed}")
        return 1

    if stale:
        print(f"STALE REVIEW CANDIDATES ({len(stale)}):")
        for age, name, reviewed in sorted(stale, reverse=True):
            print(f"  - {name}: reviewed {reviewed} ({age} days ago)")
        print("Update only the tools you actually re-check in site/tool-review.json overrides.")
        return 0 if args.warn_only else 2

    print("PASS: every curated tool is within the review-age budget.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
