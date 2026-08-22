# 🕵️ OSINT Roadmap

## Practical & Ethical Open Source Intelligence

![OSINT Banner](https://images.unsplash.com/photo-1600267165477-6d4cc741b379)

> A professional, methodology-driven roadmap for learning
> **Open Source Intelligence (OSINT)**
> from **Beginner → Intermediate → Professional**.
>
> This roadmap focuses on **analysis, verification, legality, documentation, and ethics** — not random tool collection.

---

## 🌐 Languages

* [English](README.en.md)
* [العربية](README.ar.md)
* [Türkçe](README.tr.md)

---

## 📌 Table of Contents

* [What is OSINT?](#-what-is-osint)
* [OSINT vs Hacking](#-osint-vs-hacking)
* [Who This Roadmap Is For](#-who-this-roadmap-is-for)
* [Learning Roadmap Overview](#-learning-roadmap-overview)
* [Phase 1 – Foundations](#-phase-1--foundations-beginner)
* [Phase 2 – Core OSINT Skills](#-phase-2--core-osint-skills-intermediate)
* [Phase 3 – Advanced OSINT](#-phase-3--advanced-osint-professional)
* [OSINT Workflow](#-osint-workflow)
* [OSINT Source Types](#-osint-source-types)
* [OSINT Tools & Frameworks](#-osint-tools--frameworks)
* [Investigation Checklist](#-investigation-checklist)
* [Case Study Example](#-case-study-example)
* [Reporting & Documentation](#-reporting--documentation)
* [Confidence Levels](#-confidence-levels)
* [Common Mistakes](#-common-mistakes)
* [Learning Resources](#-learning-resources)
* [Recommended Books](#-recommended-books)
* [Certifications & Career Paths](#-certifications--career-paths)
* [Researcher OPSEC](#-researcher-opsec)
* [Ethics & Legal Responsibility](#-ethics--legal-responsibility)
* [Suggested Repository Structure](#-suggested-repository-structure)
* [Repository Development Plan](#-repository-development-plan)
* [Contributing](#-contributing)
* [License](#-license)

---

## 🔍 What is OSINT?

**Open Source Intelligence (OSINT)** is the structured process of collecting, verifying, analyzing, and reporting information from publicly available sources.

OSINT is not just “searching the internet.”
A proper OSINT process starts with a clear question, defines a legal scope, collects public information, verifies it through independent sources, and presents the result in a documented report.

Public sources may include:

* Websites and blogs
* News articles
* Public social media content
* Public records
* Images and videos
* Maps and satellite imagery
* Domain and DNS records
* Company registries
* Academic papers
* Public datasets
* Archived web pages

The value of OSINT is not in collecting the most information.
The value is in proving what can be proven and clearly explaining what remains uncertain.

---

## ⚖️ OSINT vs Hacking

![Legal Boundaries](https://images.unsplash.com/photo-1589829545856-d10d557cf95f)

> **OSINT is observation and analysis, not intrusion.**

| OSINT                                                          | Hacking                                             |
| -------------------------------------------------------------- | --------------------------------------------------- |
| Uses publicly available information                            | Targets private systems or accounts                 |
| Passive collection                                             | Active exploitation                                 |
| No bypassing access controls                                   | Bypassing login, access control, or security layers |
| Focuses on documentation and verification                      | Focuses on unauthorized access or manipulation      |
| Can support research, journalism, security, and investigations | Can create criminal and civil liability             |

OSINT does **not** include:

* Login bypass
* Password guessing
* Credential use without permission
* Exploiting vulnerabilities
* Social engineering
* Impersonation
* Doxxing
* Harassment
* Private account access
* Active scanning without authorization

If access requires deception, intrusion, or bypassing a restriction, it is not ethical OSINT.

---

## 🎯 Who This Roadmap Is For

This roadmap is designed for:

* Beginners starting from zero
* Cybersecurity students
* Digital forensics learners
* Threat intelligence beginners
* SOC analysts
* Journalists and fact-checkers
* Researchers and investigators
* Fraud analysts
* Brand protection analysts
* Anyone interested in ethical public-source research

You do not need advanced technical knowledge to start.
You do need patience, documentation discipline, critical thinking, and respect for legal boundaries.

---

## 🧭 Learning Roadmap Overview

![Roadmap](https://images.unsplash.com/photo-1508780709619-79562169bc64)

```text
Beginner
  ↓
Search basics
  ↓
Source verification
  ↓
Documentation habits
  ↓
SOCMINT / GEOINT / WEBINT
  ↓
Evidence-based analysis
  ↓
Professional reporting
  ↓
Threat intelligence, digital forensics, journalism, or investigation work
```

A good OSINT learner should develop five habits:

1. Ask a clear question.
2. Define the scope before collecting.
3. Verify before concluding.
4. Separate evidence from assumptions.
5. Document everything.

---

## 🟢 Phase 1 – Foundations (Beginner)

![Foundations](https://images.unsplash.com/photo-1526378722484-bd91ca387e72)

### Goal

Build the legal, ethical, and analytical foundation needed before using advanced tools.

### Topics

* What OSINT means
* Information vs intelligence
* Public data vs private data
* Legal and ethical limits
* Search engine basics
* Source evaluation
* Confirmation bias
* Basic OPSEC
* Note-taking and evidence organization
* Basic report writing

### Core Skills

| Skill             | Why It Matters                                           |
| ----------------- | -------------------------------------------------------- |
| Search discipline | Helps you find relevant information without wasting time |
| Source evaluation | Prevents weak or misleading conclusions                  |
| Documentation     | Makes your work reviewable and defensible                |
| Legal awareness   | Keeps the investigation inside safe boundaries           |
| Critical thinking | Reduces false attribution and unsupported claims         |

### Beginner Practice

Start with simple, legal exercises:

* Verify a public news claim.
* Compare two public sources about the same event.
* Find the original source of a public image.
* Build a timeline from public articles.
* Write a short one-page report.

---

## 🟡 Phase 2 – Core OSINT Skills (Intermediate)

![Analysis](https://images.unsplash.com/photo-1551288049-bebda4e38f71)

### 🔎 Advanced Search

Learn how to search with precision.

Topics:

* Boolean logic
* Quotation searches
* Filetype searches
* Site-specific searches
* Date filtering
* Cached and archived pages
* Search engine differences

Examples:

```text
site:example.com filetype:pdf
"exact phrase" "company name"
intitle:"report" "incident"
"username" -pinterest -facebook
```

A good search query should be specific enough to reduce noise, but flexible enough to avoid missing relevant results.

---

### 🧠 SOCMINT

**SOCMINT** means Social Media Intelligence.

It focuses on public activity from social platforms, such as:

* Public posts
* Public profile information
* Public usernames
* Public images and videos
* Public interactions
* Public timestamps
* Visible behavioral patterns

Skills:

* Username correlation
* Timeline reconstruction
* Behavioral pattern analysis
* Public profile comparison
* Cross-platform verification
* Avoiding false attribution

Important note:

```text
A matching username alone is not proof of identity.
It is only an indicator that requires additional evidence.
```

---

### 🖼️ Image & Video Verification

Images and videos can provide strong evidence, but they can also mislead.

Core techniques:

* Reverse image search
* Frame extraction from videos
* Landmark identification
* Shadow and sun position analysis
* Weather comparison
* Metadata review
* Archive checking
* First appearance search
* Visual comparison with maps

Useful questions:

```text
Where was this image first published?
Does the location match the claim?
Do shadows match the claimed time?
Do weather conditions match the date?
Are there signs, buildings, roads, or terrain clues?
```

---

### 🌍 GEOINT

**GEOINT** means Geospatial Intelligence.

In OSINT, it usually includes:

* Map analysis
* Satellite imagery review
* Street-level imagery
* Terrain comparison
* Shadow analysis
* Road and landmark matching
* Weather and environmental context

Common use cases:

* Verifying the location of a photo or video
* Checking whether a claimed event location is plausible
* Comparing public images with maps
* Understanding movement or route claims

---

### 🌐 WEBINT

**WEBINT** focuses on websites and web infrastructure.

Skills:

* WHOIS review
* DNS record analysis
* Subdomain discovery from public sources
* Certificate transparency review
* Web technology identification
* Website archive analysis
* Public metadata review

Important boundary:

```text
Passive research is OSINT.
Active scanning without authorization may not be.
```

---

### 🔗 Relationship Mapping

Relationship mapping helps connect public entities such as:

* Usernames
* Emails
* Domains
* Companies
* Public profiles
* Websites
* Documents
* Images
* Events

Good relationship mapping should show:

* What is confirmed
* What is likely
* What is only a weak indicator
* What remains unknown

Avoid turning weak links into strong claims.

---

## 🔴 Phase 3 – Advanced OSINT (Professional)

### Focus

At the professional level, the goal is not to use more tools.
The goal is to produce reliable, documented, and defensible intelligence.

### Topics

* Priority Intelligence Requirements (PIR)
* Hypothesis testing
* Confidence assessment
* Bias mitigation
* Evidence handling
* Link analysis
* Large dataset triage
* Threat intelligence support
* Business intelligence
* Dark web awareness without illegal access
* Report writing for technical and non-technical readers

### Professional Mindset

A professional OSINT analyst should be able to say:

```text
This is confirmed.
This is likely.
This is possible.
This is unknown.
This cannot be proven with the available evidence.
```

---

## 🔁 OSINT Workflow

![OSINT Workflow](assets/osint-workflow.svg)

```text
1. Define the intelligence question
2. Define the scope and legal boundaries
3. Select public sources
4. Collect information
5. Preserve evidence
6. Verify and triangulate
7. Analyze findings
8. Assess confidence
9. Write the report
10. Review limitations
```

### Example Intelligence Question

```text
Can the public claim about this website, profile, image, or event be verified from independent open sources?
```

### Example Scope

```text
Only public sources.
No login bypass.
No impersonation.
No private accounts.
No active probing.
No harassment.
No publication of sensitive personal data.
```

---

## 🧩 OSINT Source Types

| Source Type        | Description                                                    |
| ------------------ | -------------------------------------------------------------- |
| WEBINT             | Websites, blogs, public pages, archives                        |
| SOCMINT            | Public social media activity                                   |
| GEOINT             | Maps, satellite imagery, geolocation data                      |
| IMINT              | Images, videos, visual evidence                                |
| TECHINT            | Domains, DNS, certificates, infrastructure                     |
| FININT             | Public financial or company records                            |
| Academic OSINT     | Papers, research databases, citations                          |
| Public Records     | Government, legal, corporate, and registry records             |
| News OSINT         | News reports, media archives, press releases                   |
| Dark Web Awareness | Legal awareness of dark web references, without illegal access |

---

## 🧰 OSINT Tools & Frameworks

> Tools support OSINT. They do not replace thinking, verification, or reporting.

### 🗂️ General OSINT Frameworks

* [OSINT Framework](https://osintframework.com/)
* [Bellingcat Resources](https://www.bellingcat.com/category/resources/)
* [Awesome OSINT](https://github.com/jivoi/awesome-osint)
* [Start.me OSINT Collections](https://start.me/)

---

### 🔎 Search & Discovery

* [Google Advanced Search](https://www.google.com/advanced_search)
* [DuckDuckGo](https://duckduckgo.com/)
* [Bing](https://www.bing.com/)
* [Yandex](https://yandex.com/)
* [Brave Search](https://search.brave.com/)

Useful search patterns:

```text
site:domain.com keyword
filetype:pdf keyword
"exact phrase"
intitle:"keyword"
before:2024-01-01 after:2023-01-01
```

---

### 🗄️ Web Archives & Evidence Capture

* [Internet Archive Wayback Machine](https://archive.org/web/)
* [Archive.today](https://archive.today/)
* [Perma.cc](https://perma.cc/)
* [Webrecorder](https://webrecorder.net/)
* [ArchiveBox](https://archivebox.io/)

Use archives to preserve sources before they change or disappear.

---

### 🧠 Social Media & Username Intelligence

* [WhatsMyName](https://whatsmyname.app/)
* [Namechk](https://namechk.com/)
* [Sherlock](https://github.com/sherlock-project/sherlock)
* [Maigret](https://github.com/soxoj/maigret)

Use these tools carefully.
A result is an indicator, not proof.

---

### 🖼️ Image & Video Verification

* [Google Images](https://images.google.com/)
* [Yandex Images](https://yandex.com/images/)
* [TinEye](https://tineye.com/)
* [InVID Verification Plugin](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/)
* [FotoForensics](https://fotoforensics.com/)
* [ExifTool](https://exiftool.org/)
* [Metadata2Go](https://www.metadata2go.com/)

---

### 🌍 Geolocation & Maps

* [Google Earth](https://earth.google.com/)
* [OpenStreetMap](https://www.openstreetmap.org/)
* [SunCalc](https://www.suncalc.org/)
* [GeoHack](https://geohack.toolforge.org/)
* [Wikimapia](https://wikimapia.org/)

Good geolocation work depends on patience and comparison, not guessing.

---

### 🌐 Domains & Infrastructure

* [WHOIS](https://who.is/)
* [SecurityTrails](https://securitytrails.com/)
* [Shodan](https://www.shodan.io/)
* [Censys](https://search.censys.io/)
* [crt.sh](https://crt.sh/)
* [DNSDumpster](https://dnsdumpster.com/)
* [BuiltWith](https://builtwith.com/)
* [Wappalyzer](https://www.wappalyzer.com/)
* [urlscan.io](https://urlscan.io/)
* [VirusTotal](https://www.virustotal.com/)

Use infrastructure tools only within legal and authorized boundaries.

---

### 🧾 Public Records, Companies & Sanctions

* [OpenCorporates](https://opencorporates.com/)
* [OpenSanctions](https://www.opensanctions.org/)
* [OCCRP Aleph](https://aleph.occrp.org/)
* [GLEIF](https://www.gleif.org/)
* [SEC EDGAR](https://www.sec.gov/edgar/search/)

These sources can help with company, ownership, sanctions, and public-record investigations.

---

### 🛠️ Data Processing & Documentation

* [CyberChef](https://gchq.github.io/CyberChef/)
* [Obsidian](https://obsidian.md/)
* [Zotero](https://www.zotero.org/)
* [Maltego](https://www.maltego.com/)
* [Draw.io](https://app.diagrams.net/)
* [Joplin](https://joplinapp.org/)

Documentation tools help keep investigations clear, reproducible, and reviewable.

---

## ✅ Investigation Checklist

Use this checklist before and during any OSINT investigation:

```text
[ ] What question am I trying to answer?
[ ] What is the legal scope?
[ ] Are all sources public?
[ ] Did I avoid private access or deception?
[ ] Did I collect more than one source?
[ ] Did I save links and access dates?
[ ] Did I separate facts from assumptions?
[ ] Did I check for contradictory evidence?
[ ] Did I evaluate source reliability?
[ ] Did I assess confidence level?
[ ] Did I document limitations?
[ ] Did I avoid exposing sensitive personal data?
```

---

## 📍 Case Study Example

**Scenario:** Verifying the location of a viral video.

### Objective

Determine whether the video was recorded in the claimed location.

### Method

1. Extract clear frames from the video.
2. Identify visible landmarks, road signs, buildings, terrain, or shadows.
3. Run reverse image search.
4. Compare the visual clues with satellite imagery.
5. Use maps and street-level imagery when available.
6. Check weather and sunlight conditions.
7. Look for independent sources.
8. Archive evidence.
9. Write a conclusion with confidence level.

### Example Conclusion

```text
Location: Verified with high confidence.
Timeline: Not fully verified.
Reason: The visual location evidence is strong, but shadow angle and weather data do not fully confirm the claimed time.
```

---

## 📝 Reporting & Documentation

A professional OSINT report should be clear, neutral, and evidence-based.

### Basic Report Structure

```text
1. Title
2. Objective
3. Scope
4. Methodology
5. Sources
6. Evidence
7. Findings
8. Analysis
9. Confidence Level
10. Limitations
11. Conclusion
```

### Example Finding Format

```text
Finding:
Two public accounts appear to share similar identifiers.

Evidence:
- Source 1: URL + access date
- Source 2: URL + access date
- Source 3: screenshot or archived copy

Confidence:
Medium

Limitations:
The accounts share public identifiers, but there is no direct proof that they belong to the same person.
```

Opinion is not intelligence.
Evidence, verification, and clear reasoning are the foundation.

---

## 📊 Confidence Levels

| Level     | Meaning                                   |
| --------- | ----------------------------------------- |
| Low       | One weak source or unclear evidence       |
| Medium    | Multiple indicators, but still incomplete |
| High      | Strong evidence from independent sources  |
| Confirmed | Direct evidence with strong verification  |

Use confidence levels to avoid overstating conclusions.

---

## ❌ Common Mistakes

* Starting with tools instead of questions
* Relying on one source
* Treating raw data as a conclusion
* Ignoring contradictory evidence
* Confusing similarity with proof
* Poor OPSEC
* Weak documentation
* Missing access dates
* Overstating confidence
* Ignoring legal boundaries
* Publishing sensitive personal information
* Using OSINT as an excuse for harassment

---

## 📚 Learning Resources

### Free Resources

* [OSINT Framework](https://osintframework.com/)
* [Bellingcat Resources](https://www.bellingcat.com/category/resources/)
* [Verification Handbook](https://verificationhandbook.com/)
* [GIJN Resource Center](https://gijn.org/resource/)
* [OSINTCurious](https://osintcurio.us/)
* [FreeOSINT](https://freeosint.github.io/)
* [Google Search Help](https://support.google.com/websearch/)
* [Google Advanced Search](https://www.google.com/advanced_search)

### Practice Ideas

```text
Week 1: Verify a public claim.
Week 2: Analyze a public website footprint.
Week 3: Geolocate a public image.
Week 4: Write a one-page OSINT report.
```

---

## 📘 Recommended Books

### OSINT & Investigation

* **Open Source Intelligence Techniques**
  Michael Bazzell
  A practical reference for OSINT workflows, tools, privacy, and investigation setup.

* **Open Source Intelligence Methods and Tools**
  Nihad A. Hassan & Rami Hijazi
  A practical guide covering online intelligence, search techniques, social media intelligence, maps, public records, and technical footprinting.

* **We Are Bellingcat**
  Eliot Higgins
  A strong introduction to open-source investigations, verification, and public-interest intelligence work.

### Verification & Digital Evidence

* **Verification Handbook**
  European Journalism Centre
  A practical guide for verifying digital content, especially images, videos, and user-generated content.

* **Digital Witness**
  Sam Dubberley, Alexa Koenig, Daragh Murray
  Useful for understanding digital evidence, documentation, human rights investigations, and verification.

### Intelligence & Analysis

* **Psychology of Intelligence Analysis**
  Richards J. Heuer Jr.
  Useful for understanding bias, assumptions, and analytical thinking.

* **Structured Analytic Techniques for Intelligence Analysis**
  Richards J. Heuer Jr. & Randolph H. Pherson
  Useful for hypothesis testing, confidence assessment, and structured reasoning.

---

## 🎓 Certifications & Career Paths

### Entry-Level / Free or Low-Cost

* [Basel Institute LEARN](https://learn.baselgovernance.org/)
* [Security Blue Team](https://securityblue.team/)

### Professional

* [GIAC GOSI](https://www.giac.org/certifications/open-source-intelligence-gosi/)
* [SANS SEC497 Practical OSINT](https://www.sans.org/cyber-security-courses/practical-open-source-intelligence/)

### Career Paths

OSINT can support several professional paths:

* Cyber Threat Intelligence Analyst
* SOC Analyst
* Digital Forensics Investigator
* Fraud Analyst
* Brand Protection Analyst
* Investigative Journalist
* Security Researcher
* Corporate Risk Analyst
* Lawful Investigation Support
* Human Rights Investigator

Supporting skills:

* Networking basics
* Web technologies
* Cybersecurity fundamentals
* Report writing
* Critical thinking
* Data organization
* Legal awareness
* Privacy awareness

---

## 🛡️ Researcher OPSEC

Before starting research:

* Use a dedicated browser profile.
* Keep personal accounts separate from research.
* Avoid logging in with personal accounts.
* Do not click suspicious links without isolation.
* Keep investigation notes organized.
* Avoid exposing private data.
* Do not contact subjects without a lawful reason.
* Archive public sources when needed.
* Keep evidence files named and dated clearly.

OPSEC is not only about hiding.
It is about reducing unnecessary exposure and keeping the investigation clean.

---

## ⚖️ Ethics & Legal Responsibility

### Allowed

* Public data collection
* Lawful archiving
* Public website review
* Public social media analysis
* Source verification
* Privacy-respecting reporting
* Fact-checking public claims

### Forbidden

* Social engineering
* Doxxing
* Impersonation
* Active probing without permission
* Bypassing security
* Publishing sensitive personal data
* Harassment
* Unauthorized access
* Credential use without consent

> Credibility in OSINT is built on restraint, not reach.

---

## 🧱 Suggested Repository Structure

```text
/
├─ README.md          # Short or general overview
├─ README.en.md       # English version
├─ README.ar.md       # Arabic version
├─ README.tr.md       # Turkish version
├─ assets/            # Images, diagrams, banners, and roadmap visuals
├─ docs/              # Extended guides and learning materials
│  ├─ checklists/     # Investigation and OPSEC checklists
│  ├─ case-studies/   # Practical examples and walkthroughs
│  ├─ report-templates/ # Report templates for different OSINT cases
│  └─ tools/          # Tool notes, safe usage guidance, and references
└─ LICENSE
```

---

## 🚧 Repository Development Plan

Planned improvements:

* Add a custom visual roadmap instead of generic images.
* Add printable OSINT checklists.
* Add report templates.
* Add practical case studies.
* Add a glossary of OSINT terms.
* Add an improved Turkish version.
* Add more free training links.
* Add reliable Arabic learning resources.
* Add a monthly learning plan.
* Add short example reports.
* Add tool usage notes with ethical boundaries.
* Add a source reliability scoring guide.
* Add OPSEC starter checklist.
* Add beginner-friendly practice labs.

---

## 🗓️ Monthly Learning Plan

### Month 1: Foundations

* Learn what OSINT is.
* Study legal and ethical boundaries.
* Practice advanced search.
* Learn source evaluation.
* Write short notes for every finding.

Deliverable:

```text
A one-page report verifying a public claim.
```

### Month 2: Core Skills

* Practice username research.
* Learn web archives.
* Practice reverse image search.
* Learn basic geolocation.
* Start using structured report templates.

Deliverable:

```text
A short case study verifying an image or video location.
```

### Month 3: Technical OSINT

* Learn WHOIS and DNS basics.
* Review certificate transparency.
* Learn website technology identification.
* Practice passive infrastructure research.
* Document findings clearly.

Deliverable:

```text
A passive public footprint report for a website or organization.
```

### Month 4: Professional Reporting

* Learn confidence levels.
* Practice hypothesis testing.
* Review bias and limitations.
* Build final reports.
* Create a portfolio with safe, public examples.

Deliverable:

```text
A full OSINT report with objective, scope, evidence, analysis, confidence level, and limitations.
```

---

## 🤝 Contributing

Contributions are welcome.

You can help by:

* Fixing outdated links
* Adding legal learning resources
* Improving translations
* Adding report templates
* Adding ethical practice cases
* Improving the visual roadmap
* Expanding beginner-friendly explanations
* Adding tool notes and limitations
* Adding Arabic, English, or Turkish learning materials

Suggested workflow:

```text
Fork → Create Branch → Make Changes → Open Pull Request
```

---

## 📄 License

MIT License © Imed Kablavi

---

## 🧠 Final Note

OSINT is not about knowing everything.

It is about asking the right question, using legal public sources, verifying carefully, documenting evidence, and reporting responsibly.

Know what can be proven.
Know what cannot be proven.
Be clear about the difference.
