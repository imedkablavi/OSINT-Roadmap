# OSINT Roadmap

> A practical learning path for open-source intelligence: search better, verify what you find, document the evidence, and report without overstating the result.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Beginner Friendly](https://img.shields.io/badge/level-beginner%20to%20advanced-blue)
![Focus](https://img.shields.io/badge/focus-ethical%20OSINT-lightgrey)

OSINT is easy to start and surprisingly easy to do badly. Finding a result is not the same as proving a claim, and using more tools does not automatically produce a better investigation.

This repository is built around that difference.

It gives you a path from basic search and source evaluation to visual verification, infrastructure research, timelines, attribution, reporting, and more advanced workflows. The focus stays on lawful public-source research and reproducible reasoning.

## Languages

- [English — full roadmap](README.en.md)
- [العربية — خارطة الطريق](README.ar.md)
- Türkçe — planned

## Start here

If you are new to OSINT, use this order:

```text
1. Learn how to frame a research question
2. Search and collect leads
3. Verify important claims independently
4. Record provenance and timestamps
5. Analyze competing explanations
6. Write a conclusion with confidence and limitations
```

Then use the practice labs instead of trying to memorize a giant list of tools.

## What's inside

| Section | What you get |
| --- | --- |
| [Full English roadmap](README.en.md) | Beginner-to-advanced learning path |
| [خارطة الطريق بالعربية](README.ar.md) | النسخة العربية الموسعة |
| [Research methods](docs/research-methods.md) | Repeatable methods that reduce common investigation errors |
| [Tool matrix](docs/tool-matrix.md) | Tools grouped by use case, cost, difficulty, and limitations |
| [Practice labs](docs/practice-labs.md) | Eight hands-on exercises with a self-scoring rubric |
| [Report template](docs/report-template.md) | A reproducible structure for findings, sources, confidence, and limitations |
| [Contributing](CONTRIBUTING.md) | How to add resources, methods, labs, and translations |

## The roadmap

### 1 — Foundations

Learn what OSINT is, what counts as a public source, how to define scope, and where legal and ethical boundaries sit.

Core habits:

- define a specific question;
- separate facts from assumptions;
- keep useful notes from the beginning;
- treat privacy and OPSEC as part of the workflow.

### 2 — Search and discovery

Build search discipline before relying on automation.

Topics include:

- advanced search operators;
- archives and historical pages;
- public records;
- username and profile discovery;
- domains, DNS, and web footprinting;
- multilingual and transliteration searches;
- news and claim research.

### 3 — Verification

This is where a lead becomes evidence.

Practice:

- source provenance;
- cross-checking independent sources;
- timeline reconstruction;
- image and video verification;
- metadata interpretation;
- geolocation basics;
- attribution without overclaiming.

A useful rule:

```text
Discovery asks what might be relevant.
Verification asks what can actually be supported.
```

### 4 — Analysis

Raw facts are not yet an assessment.

Learn to:

- compare competing hypotheses;
- distinguish correlation from attribution;
- identify source dependencies;
- reason about missing information without treating absence as proof;
- assign confidence based on evidence quality and unresolved gaps.

### 5 — Reporting

A useful OSINT report should allow another researcher to understand how the conclusion was reached.

At minimum, include:

- question and scope;
- key findings;
- evidence;
- method;
- confidence rationale;
- alternative explanations;
- limitations;
- source log.

Use the [report template](docs/report-template.md) when you need a starting structure.

### 6 — Advanced tracks

Once the core workflow is solid, specialize.

Possible tracks:

- cyber threat intelligence;
- public web infrastructure research;
- visual investigations and geolocation;
- corporate and business intelligence;
- public-event verification;
- digital footprint analysis;
- incident-support research;
- public social-network analysis;
- investigative journalism workflows.

The specialization changes. The evidence rules do not.

## New research methods

The repository now includes methods that are useful across almost any investigation, including:

- evidence ladders;
- sideways searching to escape source repetition;
- source provenance tracking;
- discovery vs. verification separation;
- alternative-hypothesis tables;
- timezone-normalized timelines;
- stable-identifier pivots;
- multilingual search variants;
- explicit stop conditions;
- challenging your strongest finding before publishing it.

Read the full guide: [Research Methods That Make OSINT Better](docs/research-methods.md).

## AI-assisted OSINT

AI can help generate search variants, translate terms, extract entities from documents, summarize your own notes, suggest alternative hypotheses, or clean structured data.

It should not be treated as evidence.

```text
AI may suggest the next question.
A verifiable source must support the answer.
```

Names, dates, quotations, URLs, relationships, and conclusions should always be checked against the underlying source.

## Tool philosophy

This project is deliberately not trying to become a directory of thousands of links.

For every tool, ask:

```text
What question am I trying to answer?
What evidence would answer it?
Why is this tool the right source?
How will I verify its output?
```

The [tool matrix](docs/tool-matrix.md) includes recommended use cases and limitations so a beginner can understand what a result means, not only where to click.

## Practice instead of passive reading

The [practice labs](docs/practice-labs.md) cover:

1. tracing a claim to its earliest public source;
2. rebuilding a changed webpage with archives;
3. verifying a public image;
4. mapping a public web footprint;
5. testing a username attribution hypothesis safely;
6. building and challenging a timeline;
7. geolocation using purpose-built or public material;
8. turning an investigation into a one-page intelligence note.

Each lab focuses on a skill and includes limits on what the final conclusion should claim.

## Ethics and scope

OSINT does not mean “anything found online is fair game.”

This roadmap is for lawful research using genuinely public sources. It does not teach unauthorized access, credential attacks, bypassing access controls, impersonation, deceptive social engineering, stalking, harassment, or doxxing.

A practical stop rule is simple:

```text
If the next step requires intrusion, deception, private access,
or collection unrelated to the research question, stop.
```

## Contributing

Contributions are welcome, especially:

- better primary sources;
- updated or corrected resources;
- new safe practice labs;
- improved translations;
- regional public-record guides;
- visual verification methods;
- reporting examples;
- fixes for stale links or unclear explanations.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a larger pull request.

## Planned additions

- Turkish full translation
- visual roadmap diagram
- source-verification checklist
- geolocation field guide
- public-record research by region
- threat-intelligence learning track
- investigation note template
- link-health checks for curated resources
- glossary of common OSINT terms

## License

MIT License © Imed Kablavi

---

If this roadmap helps your learning, a star makes the project easier for other researchers and students to discover.
