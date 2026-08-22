# OSINT Tool Radar — August 2026

> A short maintenance note for tools and resources reviewed while expanding the OSINT Roadmap library.

## What changed in the roadmap

This update adds a larger curated tool library covering:

- search and archives;
- usernames and public identity clues;
- image and video verification;
- GEOINT, maps and satellite imagery;
- domains, IPs and internet infrastructure;
- CTI and public IOC enrichment;
- companies, ownership and public records;
- aviation and maritime tracking;
- document/data extraction;
- investigation workspaces;
- blockchain research.

The library is available in English, Arabic and Turkish.

## Satellite imagery: prefer Copernicus Browser for public Sentinel data

The older Sentinel Hub EO Browser now directs users who only need public data to the **Copernicus Browser**. The roadmap therefore treats Copernicus Browser as the current recommended starting point for free public Copernicus/Sentinel exploration.

- Copernicus Browser: https://dataspace.copernicus.eu/browser/
- Documentation: https://documentation.dataspace.copernicus.eu/Applications/Browser.html

Why this matters: copying old OSINT lists without checking the current product path can send beginners to outdated workflows.

## Company research: use identifiers, not names alone

The updated company-research stack now emphasizes:

- **OpenCorporates** for cross-jurisdiction discovery;
- **GLEIF LEI Search** for standardized legal-entity identifiers and reported parent relationships;
- **OpenSanctions** for sanctions/PEP datasets with source provenance;
- **OCCRP Aleph** for investigative documents and structured entities;
- **ICIJ Offshore Leaks** for relationships published from major offshore investigations;
- official registries such as **SEC EDGAR** and **UK Companies House**.

A name match is not entity resolution. Jurisdiction, identifiers, addresses and dates should be used before connecting records.

## GEOINT stack expanded

Recommended learning progression:

```text
Google Maps / OpenStreetMap
        ↓
Google Earth / Mapillary
        ↓
SunCalc / PeakVisor
        ↓
Copernicus Browser / NASA Worldview
        ↓
QGIS
```

The progression moves from visual orientation to multi-layer geospatial analysis instead of sending a beginner directly into a GIS application.

## CTI stack expanded but kept passive-first

The roadmap now includes VirusTotal, urlscan.io, Shodan, Censys, GreyNoise, AlienVault OTX, Pulsedive and abuse.ch resources such as ThreatFox, URLhaus and MalwareBazaar.

The operating rule stays the same:

> Search public or already-observed datasets first. Active probing is a different activity and may require explicit authorization.

## Public identity tools kept behind an attribution warning

WhatsMyName, Sherlock and Maigret are useful for **discovery**, but matching usernames are weak attribution by themselves. The updated documentation repeats this before listing the tools rather than burying the warning at the end.

## Learning resources added

The library now points learners to method-focused resources including:

- Bellingcat Online Investigations Toolkit;
- OSINT Dojo;
- GIJN Resource Center;
- Verification Handbook;
- OSINT Framework;
- IntelTechniques tools;
- Awesome OSINT;
- OSINT Tools Library.

## What to review next month

- ownership or permission changes in browser extensions;
- stale social-platform tooling;
- changes in public satellite interfaces;
- new public-record datasets;
- broken URLs caught by the link-health workflow;
- whether any listed service moved important free features behind a paywall.

---

A tool stays in this project because it remains useful and explainable — not because it was popular on an old OSINT list.
