#!/usr/bin/env python3
"""Build a dependency-free search index for the OSINT Roadmap static site."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
OUTPUT = SITE / "search-index.json"
EXCLUDED_DIRS = {".git", ".github", "node_modules", "lighthouse-reports"}
MAX_TEXT = 8000

TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_RE = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.I | re.S)
SPACE_RE = re.compile(r"\s+")
MD_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
MD_MARKUP_RE = re.compile(r"[`*_>#|~]+")


def compact(value: str) -> str:
    return SPACE_RE.sub(" ", value).strip()


def strip_markdown(text: str) -> str:
    text = MD_LINK_RE.sub(lambda m: m.group(1), text)
    text = MD_MARKUP_RE.sub(" ", text)
    return compact(text)


def strip_html(text: str) -> str:
    text = SCRIPT_RE.sub(" ", text)
    text = TAG_RE.sub(" ", text)
    return compact(html.unescape(text))


def markdown_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return compact(line[2:])
    return fallback


def html_title(text: str, fallback: str) -> str:
    match = re.search(r"<title>(.*?)</title>", text, re.I | re.S)
    return compact(html.unescape(match.group(1))) if match else fallback


def language_for(path: Path) -> str:
    parts = set(path.parts)
    if "ar" in parts or path.name.endswith(".ar.md") or path.name == "README.ar.md":
        return "ar"
    if "tr" in parts or path.name.endswith(".tr.md") or path.name == "README.tr.md":
        return "tr"
    return "en"


def include_markdown(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    return not any(part in EXCLUDED_DIRS for part in rel.parts)


def build() -> list[dict[str, str]]:
    records: list[dict[str, str]] = []

    for path in sorted(ROOT.rglob("*.md")):
        if not include_markdown(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_markdown(raw)[:MAX_TEXT]
        if len(text) < 40:
            continue
        records.append(
            {
                "title": markdown_title(raw, path.stem.replace("-", " ").title()),
                "path": rel,
                "url": f"https://github.com/imedkablavi/OSINT-Roadmap/blob/main/{rel}",
                "kind": "Documentation",
                "lang": language_for(path),
                "text": text,
            }
        )

    for path in sorted(SITE.rglob("*.html")):
        if path.name == "search.html":
            continue
        rel = path.relative_to(SITE).as_posix()
        raw = path.read_text(encoding="utf-8", errors="replace")
        text = strip_html(raw)[:MAX_TEXT]
        if len(text) < 40:
            continue
        records.append(
            {
                "title": html_title(raw, path.stem.replace("-", " ").title()),
                "path": f"site/{rel}",
                "url": rel,
                "kind": "Website",
                "lang": language_for(path),
                "text": text,
            }
        )

    return records


def main() -> int:
    records = build()
    OUTPUT.write_text(json.dumps(records, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Built search index with {len(records)} documents: {OUTPUT.relative_to(ROOT)}")
    if len(records) < 30:
        raise SystemExit("search index unexpectedly small")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
