# OSINT Investigator Tool Stack

> Reviewed: **2026-08-24** · English · [العربية](investigator-stack.ar.md) · [Türkçe](investigator-stack.tr.md)

This is a **selection map**, not a checklist to run every tool. Start with the clue you actually have, use the smallest useful source, preserve provenance, and independently verify important findings.

## Start from your clue

| You have | Good first tools | Add when needed | Main caution |
| --- | --- | --- | --- |
| Username | WhatsMyName, Sherlock, Maigret | GitHub Search, GHunt | Handle reuse alone is weak attribution |
| Email | Have I Been Pwned, Epieos | GHunt | Use lawful/authorized identifiers; breach exposure is not current compromise |
| Phone | PhoneInfoga, Epieos | Search engines, official numbering sources | Number metadata does not prove who controls the number |
| Domain / URL | ICANN Lookup, crt.sh, Internet Archive, urlscan.io | Common Crawl, SecurityTrails, DNSViz, Subfinder, Amass | Prefer passive evidence; active techniques require authorization |
| IP / ASN | RIPEstat, BGP.tools, GreyNoise | Censys, Shodan, IntelOwl | Observation time and scan age matter |
| Image | Google Lens, TinEye, Yandex Images | ExifTool, Sherloq, Tesseract OCR | Forensic anomalies are cues, not manipulation proof |
| Video / audio | InVID & WeVerify, FFmpeg, MediaInfo | ExifTool, frame-level image checks | Containers and tags can be rewritten |
| Location | OpenStreetMap, Google Maps/Earth, SunCalc | Overpass Turbo, OpenAerialMap, Mapillary, kepler.gl, QGIS | Map and imagery coverage varies by region/date |
| Company | Official registry, OpenCorporates, GLEIF | SEC EDGAR, Companies House, OpenSanctions, ICIJ, USAspending, TED | Resolve the legal entity before connecting records |
| US nonprofit | ProPublica Nonprofit Explorer | IRS source filings, USAspending | Compare filing periods and processing dates |
| US court case/person/company | CourtListener / RECAP | Docket alerts and primary court sources | Legal records need jurisdiction and procedural context |
| IOC / hash | VirusTotal, CIRCL hashlookup, abuse.ch | IntelOwl, YETI, MISP, OpenCTI | Submitting indicators/files may disclose them to providers |
| Flight / aircraft | Flightradar24, ADS-B Exchange, OpenSky | Maps and weather context | Coverage and receiver availability vary |
| Vessel | MarineTraffic, VesselFinder | Global Fishing Watch | AIS gaps/spoofing can invalidate naive conclusions |
| Rail infrastructure | OpenRailwayMap, OpenStreetMap | Overpass Turbo | Community map completeness varies |
| Crypto address / transaction | Blockchair, Etherscan/Tronscan | GraphSense, Breadcrumbs | Clustering or labels are hypotheses, not identity proof |
| PDF / scanned document | ExifTool, Apache Tika, OCRmyPDF | Tesseract, Tabula, CyberChef | Preserve the original before transformations |
| Large structured dataset | OpenRefine, jq | Datasette, QGIS, kepler.gl | Record every transform so results are reproducible |
| Timeline / event set | Timesketch | Gephi or other relationship views | Timezone, clock and parser errors propagate |
| Researcher / paper / DOI | OpenAlex, Crossref | ORCID Search | Author-name matching and self-managed profiles can be wrong |
| Historical webpage | Internet Archive, Archive.today | Common Crawl, Browsertrix, ReplayWeb.page | Capture date and archive provenance matter |
| Evidence preservation | SingleFile, Bellingcat Auto Archiver | Browsertrix, ArchiveBox, ReplayWeb.page | Archive creation is not independent verification |

## A practical minimum stack

For most investigations you do **not** need 100 tools. A defensible baseline is:

1. **Discovery:** two independent search/index sources.
2. **Primary source:** registry, filing, original post, map dataset or official record.
3. **Preservation:** save the source, URL, timestamp and a reproducible copy where lawful.
4. **Enrichment:** add a specialist tool only when it answers a defined question.
5. **Verification:** corroborate with an independent source or method.
6. **Analysis:** maintain notes, confidence and alternatives; use graph/timeline tools only when complexity justifies them.
7. **Reporting:** distinguish observed facts, tool output, inference and unknowns.

## Privacy and authorization

- Public availability does not make every query or action appropriate.
- For phone, email and account research, minimize personal-data collection and use authorized identifiers.
- For infrastructure, passive observations are preferred; active scanning/probing is outside ordinary OSINT unless you own the target or have explicit permission.
- Before submitting files, URLs or indicators to CTI/cloud services, check whether the provider stores or redistributes them.
- Do not treat breach presence, username reuse, crypto clustering, metadata, image-forensics signals or automated enrichment as identity proof.

## Open-source preference

When two tools are similarly useful, this roadmap prefers tools with a maintained upstream, a clear license, inspectable behavior and self-hosting/local-processing options. See [Verified Open-Source OSINT Tools](open-source-tools.md).
