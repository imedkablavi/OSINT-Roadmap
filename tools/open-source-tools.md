# Verified Open-Source OSINT Tools

> Reviewed: **2026-08-24** · English · [العربية](open-source-tools.ar.md) · [Türkçe](open-source-tools.tr.md)

This page lists tools for which the current upstream project and license were checked before applying the **Open Source** label. Public source code without a clear license is not treated as open source here.

## Discovery, archiving and identity

| Tool | License | Practical role | Important limitation |
| --- | --- | --- | --- |
| [Bellingcat Auto Archiver](https://github.com/bellingcat/auto-archiver) | MIT | Automate preservation of public links, media and social posts | Archive provenance and capture time still need recording |
| [Browsertrix](https://github.com/webrecorder/browsertrix) | AGPL-3.0 | High-fidelity browser-based web crawling and preservation | Crawl scope and access restrictions must be respected |
| [ReplayWeb.page](https://github.com/webrecorder/replayweb.page) | AGPL-3.0 | Replay WARC/WACZ archives locally/in-browser | Replay does not independently prove capture time or authenticity |
| [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) | GPL-3.0 | Structure public phone-number research and search pivots | Number metadata does not prove subscriber identity |
| [GHunt](https://github.com/mxrch/GHunt) | AGPL-3.0 | Public Google-account/object OSINT | Some modules need authenticated Google context; minimize account exposure |

## Infrastructure and CTI

| Tool | License | Practical role | Important limitation |
| --- | --- | --- | --- |
| [theHarvester](https://github.com/laramies/theHarvester) | GPL-2.0 | Aggregate public passive infrastructure sources | Provider coverage, quotas and API-key needs change |
| [OWASP Amass](https://github.com/owasp-amass/amass) | Apache-2.0 | External asset discovery and mapping | Active techniques require explicit authorization |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | MIT | Passive subdomain enumeration | Upstream providers can change or require API keys |
| [OpenCTI Community Edition](https://github.com/OpenCTI-Platform/opencti) | Apache-2.0 (CE) | Structure and link CTI knowledge | Source confidence remains an analyst responsibility |
| [MISP](https://github.com/MISP/MISP) | AGPL-3.0 | Structured threat-intelligence sharing | Community data and sharing rules require governance |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | AGPL-3.0 | Orchestrate IOC/file enrichment | External analyzers can receive submitted indicators or samples |
| [YETI](https://github.com/yeti-platform/yeti) | Apache-2.0 | Threat-intelligence entities, observables and enrichment | It organizes evidence; it does not validate every upstream claim |

## Image, media and GEOINT

| Tool | License | Practical role | Important limitation |
| --- | --- | --- | --- |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | Apache-2.0 | Local OCR for images and scanned documents | OCR errors must be checked against the source |
| [MediaInfo](https://github.com/MediaArea/MediaInfo) | BSD-2-Clause | Inspect audio/video technical metadata | Metadata can be missing, edited or rewritten |
| [Sherloq](https://github.com/GuidoBartoli/sherloq) | GPL-3.0 | Digital image-forensics analysis | Anomalies are cues, not proof of manipulation |
| [Overpass Turbo](https://github.com/tyrasd/overpass-turbo) | MIT | Query OpenStreetMap data for GEOINT | OSM completeness/freshness varies geographically |
| [kepler.gl](https://github.com/keplergl/kepler.gl) | MIT | Large-scale geospatial visualization | Visual correlation is not causal evidence |
| [OpenAerialMap](https://github.com/hotosm/openaerialmap) | AGPL-3.0 | Discover openly licensed aerial imagery | Coverage, dates and resolution vary substantially |

## Analysis and investigation workspaces

| Tool | License | Practical role | Important limitation |
| --- | --- | --- | --- |
| [Datasette](https://github.com/simonw/datasette) | Apache-2.0 | Explore/query structured local datasets | Do not accidentally publish sensitive research data |
| [Timesketch](https://github.com/google/timesketch) | Apache-2.0 | Collaborative event/timeline analysis | Parser, clock and timezone errors propagate into timelines |
| [GraphSense](https://github.com/graphsense/graphsense-dashboard) | MIT | Open cryptoasset graph analysis | Clustering and labels are hypotheses requiring corroboration |

## Safe-use rule

Open source does not remove authorization, privacy, provider-terms or data-handling obligations. Infrastructure collection should stay passive unless the target is owned or explicitly authorized. Identity, phone and account research should minimize personal data. Before sending files, URLs or IOCs to third-party analyzers, check retention and redistribution behavior.

A tool output is a **lead or observation**, not an automatic conclusion. Preserve the source, timestamp, query, confidence and limitation before using it in a report.

For clue-based selection across both open-source and official data sources, use the [OSINT Investigator Tool Stack](investigator-stack.md).
