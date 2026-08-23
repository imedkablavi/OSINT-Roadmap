#!/usr/bin/env python3
"""Build a small contributors snapshot for the static credits page.

Uses GitHub's public contributors endpoint when available. If the API is
unreachable or rate-limited, keeps a deterministic maintainer fallback so the
Pages build is never blocked by an external API dependency.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "site" / "contributors.json"
REPO = os.environ.get("GITHUB_REPOSITORY", "imedkablavi/OSINT-Roadmap")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

FALLBACK = [
    {
        "login": "imedkablavi",
        "avatar_url": "https://avatars.githubusercontent.com/u/76208805?v=4",
        "html_url": "https://github.com/imedkablavi",
        "contributions": None,
        "role": "Maintainer",
    }
]


def fetch_contributors() -> list[dict]:
    url = f"https://api.github.com/repos/{REPO}/contributors?per_page=100&anon=0"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "OSINT-Roadmap-Contributors-Builder/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        payload = json.load(response)
    result = []
    for item in payload:
        login = item.get("login")
        if not login or login.endswith("[bot]") or item.get("type") == "Bot":
            continue
        result.append(
            {
                "login": login,
                "avatar_url": item.get("avatar_url", ""),
                "html_url": item.get("html_url", f"https://github.com/{login}"),
                "contributions": int(item.get("contributions", 0)),
                "role": "Maintainer" if login == "imedkablavi" else "Contributor",
            }
        )
    return sorted(result, key=lambda x: (-int(x.get("contributions") or 0), x["login"].lower()))


def main() -> int:
    source = "github-api"
    try:
        contributors = fetch_contributors()
        if not contributors:
            raise RuntimeError("contributors endpoint returned no human accounts")
    except (urllib.error.URLError, TimeoutError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        contributors = FALLBACK
        source = "fallback"
        print(f"Contributor API unavailable; using fallback: {exc}")

    output = {
        "repository": REPO,
        "source": source,
        "contributors": contributors,
    }
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built contributor snapshot with {len(contributors)} people ({source}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
