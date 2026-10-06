# OSINT Roadmap

## Practical and Ethical Open Source Intelligence

[![GitHub Repo stars](https://img.shields.io/github/stars/imedkablavi/OSINT-Roadmap?style=plastic)](https://github.com/imedkablavi/OSINT-Roadmap/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/imedkablavi/OSINT-Roadmap?style=plastic)](https://github.com/imedkablavi/OSINT-Roadmap/network/members)
[![GitHub contributors](https://img.shields.io/github/contributors/imedkablavi/OSINT-Roadmap?style=plastic)](https://github.com/imedkablavi/OSINT-Roadmap/graphs/contributors)
[![Latest release](https://img.shields.io/github/v/release/imedkablavi/OSINT-Roadmap?style=plastic&label=latest)](https://github.com/imedkablavi/OSINT-Roadmap/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=plastic)](LICENSE)
[![Link Health](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/link-check.yml/badge.svg)](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/link-check.yml)
[![Tool Freshness](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/tool-freshness.yml/badge.svg)](https://github.com/imedkablavi/OSINT-Roadmap/actions/workflows/tool-freshness.yml)

> A roadmap for learning OSINT by doing careful research, checking sources, and writing conclusions that can survive scrutiny.

---

## The Roadmap

![OSINT Roadmap — Research to Intelligence](assets/osint-roadmap.svg)

The roadmap follows the investigation process rather than a list of favorite tools.

~~~text
Question
  ↓
Scope
  ↓
Discovery
  ↓
Verification
  ↓
Correlation
  ↓
Assessment
  ↓
Reporting
  ↓
Specialization
~~~

The order matters. Learn how to think about evidence first. Expand the toolset as your questions become more specific.

### A useful standard

A completed investigation should make four things clear:

| Question | What a good answer looks like |
| --- | --- |
| What were you trying to find out? | A focused research question |
| Where did the information come from? | Traceable public sources |
| How did you test it? | Independent corroboration and context checks |
| What can you conclude? | A confidence-calibrated assessment |

> [!IMPORTANT]
> A tool can give you a lead. It cannot remove the need to verify the source behind the lead.

---

## What is OSINT?

Open Source Intelligence is the structured collection, verification, analysis, and reporting of information available from public sources.

The structure matters. Searching without a question creates noise. Collecting without verification creates false confidence.

Public sources can include websites, archives, public records, public social media content, maps, imagery, company records, academic publications, public datasets, and domain or certificate information.

OSINT is not a form of unauthorized access. This project stays within lawful public-source research.

---

## Where to Start

Choose one clue and work through it from the first search to the final report.

| Starting clue | First step |
| --- | --- |
| Domain | [Domain playbook](playbooks/README.md#i-have-a-domain) |
| Username | [Username playbook](playbooks/README.md#i-have-a-username) |
| Email or phone | [Identity and attribution workflow](playbooks/README.md#i-have-a-username) |
| Image | [Image playbook](playbooks/README.md#i-have-an-image) |
| Video | [Video playbook](playbooks/README.md#i-have-a-video) |
| Company | [Company playbook](playbooks/README.md#i-have-a-company-name) |
| IP address | [IP playbook](playbooks/README.md#i-have-an-ip-address) |
| Public document | [Document playbook](playbooks/README.md#i-have-a-public-document) |
| News claim | [News-claim playbook](playbooks/README.md#i-have-a-news-claim) |
| Location claim | [Location playbook](playbooks/README.md#i-have-a-location-claim) |

Do not try to memorize the whole OSINT ecosystem before you can complete a small investigation well.

---

## Foundations

Start with the habits that prevent weak conclusions:

- research-question design;
- scope and stopping conditions;
- provenance and source dependency;
- independent corroboration;
- timeline handling;
- entity resolution;
- confidence and uncertainty;
- evidence tables and source logs;
- researcher OPSEC.

[Research methods](docs/research-methods.md)  
[Skill Matrix](docs/skill-matrix.md)  
[Quick Reference](cheatsheets/osint-quick-reference.md)

---

## Discovery

### Search and Archives

Learn deliberate search rather than random searching:

- exact phrases and Boolean operators;
- site, file type, title, and date filters;
- archive reconstruction;
- multilingual search and transliteration;
- tracing claims towards their earliest public source.

### Identity and Digital Footprints

Work with public clues such as usernames, aliases, public email addresses, public phone numbers, stable identifiers, self-declared links, and archived profile history.

A username match alone is weak attribution evidence.

### Organizations and Public Records

Practice:

- legal-entity resolution;
- public registries and filings;
- ownership and relationship research;
- procurement and regulatory records;
- corporate timelines.

Resolve the entity before making claims about it.

---

## Verification

### Image and Video

Study reverse image search, earliest public appearance, provenance and repost chains, frame extraction, visual clues, temporal consistency, and cautious metadata interpretation.

[Browser Extensions and Web Tools](tools/browser-extensions.md)

### News and Claims

A useful workflow is:

1. find the earliest source you can identify;
2. locate primary documents or first-hand statements;
3. compare genuinely independent reporting;
4. check corrections and later updates;
5. use archives when they add useful context.

### GEOINT

Start broad and narrow the candidate set with evidence.

~~~text
Country or region
      ↓
City or area
      ↓
Road, landmark, or terrain
      ↓
Specific location, only when justified
~~~

[Advanced GEOINT Challenges](challenges/advanced-geoint.md)

---

## Analysis

After important observations are verified, connect them carefully.

Learn:

- entity resolution;
- relationship mapping;
- timeline analysis;
- geographic correlation;
- competing hypotheses;
- confidence calibration;
- missing-data analysis.

The goal is not the largest graph. It is the strongest explanation the evidence can support.

---

## Reporting

A professional note should make the research reproducible.

~~~text
Question
Scope
Method
Sources
Findings
Analysis
Confidence
Limitations
Conclusion
~~~

[OSINT Report Template](docs/report-template.md)

---

## Specialization

Choose a track when the core workflow is comfortable.

| Track | Focus |
| --- | --- |
| [Cyber Threat Intelligence](tracks/cti.md) | PIRs, public indicators, infrastructure relationships, ATT&CK, timelines, attribution |
| [Digital Footprint Investigation](tracks/digital-footprint.md) | public traces, attribution, archives, privacy-aware research |
| [Company Investigation](tracks/company-investigation.md) | entity resolution, filings, ownership, corporate timelines |
| [Advanced GEOINT](challenges/advanced-geoint.md) | geolocation, chronolocation, imagery, candidate rejection |
| Journalism and Fact Checking | source tracing, media provenance, claim verification |
| Public Web Infrastructure | domains, DNS, certificates, passive infrastructure research |

---

## Tool Library

The repository keeps a curated collection of tools and public-source resources rather than trying to list everything.

Each entry is intended to make four things clear:

~~~text
What input does it need?
What is it useful for?
What are its limits?
How should the result be verified?
~~~

[Tool Library](tools/tool-library.md)  
[Investigator Tool Stack](tools/investigator-stack.md)  
[Verified Open-Source Tools](tools/open-source-tools.md)

---

## Practice

The project uses an artifact-based learning model.

~~~text
Learn
  ↓
Practice
  ↓
Produce
  ↓
Defend
  ↓
Review
~~~

A useful artifact can be a timeline, source assessment, claim-verification report, geolocation exercise, attribution assessment, or short intelligence note.

[Practice Labs](docs/practice-labs.md)  
[Skill Matrix](docs/skill-matrix.md)  
[Case Studies](case-studies/README.md)

---

## AI-Assisted OSINT

AI can help with search-query variants, language support, organization, entity extraction, and alternative hypotheses.

It should not be treated as a substitute for sources.

~~~text
AI suggests
    ↓
You inspect
    ↓
You verify
    ↓
You document
~~~

---

## Scope, Ethics and Safe Use

This project is limited to lawful public-source research.

It does not cover unauthorized access, credential attacks, account takeover, access-control bypass, deceptive social engineering, stalking, harassment, doxxing, or intrusive scanning without authorization.

Practical rule:

~~~text
If the next step requires intrusion,
deception, private access,
or bypassing a security control,
stop.
~~~

---

## Maintenance

OSINT resources change. Ownership, pricing, permissions, coverage, interfaces, and terms can all change.

A working URL does not prove that a resource description is still current.

[OSINT Tool Radar](updates/2026-08-tool-radar.md)  
[Updates Archive](updates/README.md)

The repository separates link health from content freshness and runs automated checks for both.

---

## Contributing

Good contributions are specific and verifiable.

Examples include correcting a source, replacing an outdated resource, improving a translation, adding a safe practice lab, documenting a better verification method, or explaining a tool limitation more accurately.

[Contributing Guide](CONTRIBUTING.md)

---

## License

MIT License © Imed Kablavi
