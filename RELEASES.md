# Monthly Releases

OSINT Roadmap publishes calendar-versioned snapshots using `YYYY.MM` tags, for example `2026.09`.

## Why monthly snapshots exist

The roadmap is continuously maintained, but OSINT tools, pricing, interfaces, ownership and public data sources can change quickly. A monthly GitHub Release provides a stable point-in-time reference for learners, educators and researchers who need to cite or revisit a known project state.

## Schedule

The `Monthly Release` GitHub Actions workflow runs on the first day of each month and publishes the current `YYYY.MM` version from `main` if that version does not already exist. It can also be run manually with an explicit version.

Each release:

- points to the exact `main` snapshot for that month;
- uses GitHub-generated change notes;
- links naturally to the repository history and monthly Tool Radar when present;
- does **not** imply that every third-party tool will remain unchanged after the release date.

## Freshness vs. releases

A release is historical. For current operational choices, check the latest Tool Finder review dates, Tool Freshness workflow and Tool Radar before relying on a third-party resource.
