# 🕵️ OSINT Roadmap

> A practical, multilingual roadmap for learning Open Source Intelligence through research, verification, analysis, documentation, and hands-on practice.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Beginner Friendly](https://img.shields.io/badge/level-beginner%20to%20advanced-blue)
![Languages](https://img.shields.io/badge/languages-EN%20%7C%20AR%20%7C%20TR-orange)
![Focus](https://img.shields.io/badge/focus-ethical%20OSINT-lightgrey)
[![Link Health](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/link-check.yml/badge.svg)](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/link-check.yml)

A roadmap should tell you more than which tools exist. It should tell you **what question to ask, what evidence is strong enough, what can go wrong, and what to do next**.

This repository is built around that idea.

## 🌐 Choose your language

### 🇬🇧 English

**[Open the English Roadmap →](README.en.md)**

Core material:

- [Research methods](docs/research-methods.md)
- [Tool matrix](docs/tool-matrix.md)
- [Practice labs](docs/practice-labs.md)
- [Report template](docs/report-template.md)
- [English glossary](glossary/README.en.md)

### 🇸🇦 العربية

**[افتح خارطة الطريق العربية →](README.ar.md)**

- [مركز التعلم العربي](docs/ar/README.md)
- [قاموس OSINT بالعربية](glossary/README.ar.md)

### 🇹🇷 Türkçe

**[Türkçe OSINT Yol Haritasını Aç →](README.tr.md)**

- [Türkçe öğrenme merkezi](docs/tr/README.md)
- [Türkçe OSINT sözlüğü](glossary/README.tr.md)

---

## 🗺️ Visual roadmap

**[Open the interactive GitHub-rendered roadmap →](docs/visual-roadmap.md)**

```text
Foundations
    ↓
Discovery
    ↓
Verification
    ↓
Analysis
    ↓
Reporting
    ↓
Specialization
    ↓
Portfolio + Review
```

The roadmap is method-first because tools change much faster than good investigation practice.

## 🎯 Professional specialization tracks

Once the core workflow is comfortable, move into a track instead of collecting random advanced tools.

| Track | What you learn |
| --- | --- |
| [Cyber Threat Intelligence](tracks/cti.md) | PIRs, passive indicator enrichment, infrastructure relationships, ATT&CK mapping, timelines, attribution discipline |
| [Digital Footprint Investigation](tracks/digital-footprint.md) | public trace discovery, archive history, stable identifiers, attribution, privacy minimization |
| [Company Investigation](tracks/company-investigation.md) | legal entity resolution, filings, ownership, corporate timelines, sanctions checks, relationship mapping |
| [Advanced GEOINT Challenges](challenges/advanced-geoint.md) | a 10-level geolocation/chronolocation challenge ladder with a scoring rubric |

## 🧭 Investigation playbooks

Sometimes you do not need another chapter. You need to know what to do with the clue already in front of you.

**[Open the Investigation Playbooks →](playbooks/README.md)**

Playbooks cover:

- I have a domain
- I have a username
- I have an image
- I have a video
- I have a company name
- I have an IP address
- I have a public document
- I have a news claim
- I have a location claim

Every playbook includes verification questions and stop conditions.

## 🧪 Practice that produces evidence of skill

The repository now uses an artifact-based learning model:

```text
Do not mark a skill complete because you read about it.
Mark it complete when you can produce and defend the work.
```

- [Practice labs](docs/practice-labs.md)
- [Advanced GEOINT challenge ladder](challenges/advanced-geoint.md)
- [Skill Matrix & Progress Tracker](docs/skill-matrix.md)
- [Real-world case-study lessons](case-studies/README.md)

The skill matrix ranges from **L0 — Unfamiliar** to **L4 — Mentor** and requires a practical artifact for progression.

## ⚡ Field reference

Need a fast reminder while working?

**[OSINT Quick Reference / Cheat Sheet →](cheatsheets/osint-quick-reference.md)**

It covers search patterns, source verification, image/video checks, username attribution, passive domain research, company research, timelines, confidence language, evidence tables, reporting, and stop rules.

## 📖 OSINT glossary in three languages

- [English](glossary/README.en.md)
- [العربية](glossary/README.ar.md)
- [Türkçe](glossary/README.tr.md)

The glossary covers methodology terms as well as technical concepts such as provenance, corroboration, attribution, chronolocation, passive DNS, Certificate Transparency, entity resolution, source dependency, and stop conditions.

## 🔬 What makes this roadmap different?

The project is deliberately not a directory of thousands of links.

It teaches:

- how to frame an intelligence question;
- how to distinguish discovery from verification;
- how to trace information back to its source;
- how to identify copied-source chains;
- how to challenge the first hypothesis;
- how to calibrate attribution and confidence;
- how to document what a tool **cannot** prove;
- how to stop collecting when additional data adds no analytical value;
- how to use AI for assistance without treating model output as evidence;
- how to produce reports another researcher can reproduce.

```text
Finding information is discovery.
Proving what it means is investigation.
```

## 🤖 AI-assisted OSINT

AI can be useful for:

- generating search-query variants;
- transliteration and language discovery;
- entity extraction from your own collected material;
- organizing notes;
- suggesting alternative hypotheses;
- cleaning structured data.

But:

```text
AI may suggest the next question.
A verifiable source must support the answer.
```

Names, dates, quotations, relationships, URLs, and conclusions still need verification against underlying sources.

## 🛡️ Scope and ethics

This project focuses on lawful public-source research.

It does not teach:

- unauthorized access;
- credential attacks;
- account takeover;
- access-control bypass;
- deceptive social engineering;
- stalking or harassment;
- doxxing;
- intrusive scanning without authorization.

A practical stop rule:

```text
If the next step requires intrusion, deception, private access,
or bypassing a security restriction, stop.
```

## 🔧 Repository quality

Documentation links are checked automatically with GitHub Actions:

- on pull requests that change Markdown;
- after relevant changes land on `main`;
- once a week for link rot;
- manually through `workflow_dispatch`.

See [.github/workflows/link-check.yml](.github/workflows/link-check.yml).

## 🤝 Contributing

Corrections and contributions are welcome, especially:

- better primary sources;
- new safe practice labs;
- regional public-record guides;
- improved translations;
- new investigation playbooks;
- visual-verification methods;
- stale-link fixes;
- clearer explanations of what a tool can and cannot prove.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License © Imed Kablavi

---

If the project is useful, a ⭐ helps more students, researchers, journalists, and security learners discover it.
