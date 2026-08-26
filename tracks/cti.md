# Cyber Threat Intelligence (CTI) Track

A practical specialization path for learners who already understand the core OSINT workflow and want to apply it to cyber threat intelligence.

## What this track teaches

CTI is not a feed of indicators. The useful part is connecting technical observations to an intelligence question and explaining what the evidence supports.

By the end of this track you should be able to:

- frame Priority Intelligence Requirements (PIRs);
- distinguish strategic, operational, tactical, and technical intelligence;
- enrich public indicators without treating reputation scores as truth;
- pivot safely between domains, IP addresses, certificates, URLs, files, malware families, campaigns, and public reporting;
- build evidence-backed timelines;
- map observations to MITRE ATT&CK when the behavior is actually supported;
- separate infrastructure overlap from actor attribution;
- communicate confidence and collection gaps.

## Stage 1 - Intelligence requirements

Before collecting anything, write the question.

Examples:

```text
Which publicly documented infrastructure is associated with this campaign?
What behaviors are consistently reported across independent sources?
Is the observed domain reuse enough to support a relationship claim?
What changed between the first and most recent public reporting?
```

Bad requirement:

```text
Find everything about this threat actor.
```

Good requirement:

```text
Identify publicly documented infrastructure and behaviors attributed to the campaign between DATE_A and DATE_B, and assess which relationships are independently corroborated.
```

## Stage 2 - Source hierarchy

Prefer sources in roughly this order when available:

1. original vendor or incident-response report;
2. official advisory or CERT publication;
3. primary technical artifact or sandbox report that can be independently inspected;
4. reputable secondary analysis with citations;
5. aggregators and reputation portals;
6. social posts and unsourced claims.

The order is not absolute. A primary-looking source can still be wrong, and a secondary source may contain unique, well-supported analysis.

## Stage 3 - Passive indicator enrichment

Common public pivots:

| Seed | Useful public pivots | What it does not prove |
| --- | --- | --- |
| Domain | DNS history, certificate logs, passive scan records, WHOIS/RDAP, URL observations | actor ownership |
| IP address | ASN, hosting, passive services, historical resolutions | maliciousness or attribution |
| Certificate | SANs, issuance history, related hostnames | common operator |
| URL | redirects, archive history, passive scan/sandbox observations | campaign membership by itself |
| Hash | public malware reports, sandbox behavior, family labels | actor identity |
| Email | public reporting and registries where lawful | account ownership |

## Stage 4 - Infrastructure relationship analysis

Use an evidence table instead of drawing a graph first.

| Entity A | Entity B | Relationship | Evidence | Independent corroboration | Confidence |
| --- | --- | --- | --- | --- | --- |
| domain-a | IP-1 | historical resolution | Source A | Source B | High |
| domain-a | domain-b | same certificate | CT log | none | Medium |
| domain-b | campaign-x | mentioned in report | Vendor report | CERT advisory | High |

A shared hosting provider, registrar, certificate authority, ASN, or CDN is usually weak evidence. Shared infrastructure is common.

## Stage 5 - Behavior analysis

When public reporting describes activity, capture behavior separately from labels.

Example:

```text
Observed behavior: scheduled task creation for persistence
Source: report URL + page/section
Mapped ATT&CK technique: only after confirming the behavior matches the technique definition
Confidence: High
```

Do not map ATT&CK techniques from a campaign name alone.

## Stage 6 - Timeline reconstruction

Normalize timestamps to UTC and distinguish:

- event time;
- first observed time;
- report publication time;
- last updated time;
- archive capture time.

A report published later does not mean the activity started later.

## Stage 7 - Attribution discipline

Attribution is the easiest place to overclaim.

Use levels such as:

```text
Infrastructure relationship confirmed
Operational overlap likely
Campaign relationship plausible
Actor attribution unsupported with available evidence
```

Never convert “reported by one vendor as X” into “X definitely did it” unless your report explicitly attributes the claim to that source.

## Stage 8 - Reporting

A compact CTI assessment should contain:

1. intelligence question;
2. key judgments;
3. confidence statement;
4. scope and collection period;
5. relevant infrastructure or behaviors;
6. evidence table;
7. timeline;
8. alternative explanations;
9. gaps and limitations;
10. source list.

## Safe practice labs

### Lab 1 - Public advisory comparison

Pick two public advisories describing the same campaign. Compare terminology, indicators, behaviors, dates, and attribution language.

### Lab 2 - Passive domain pivot

Use a domain from a public training report. Build a relationship table using only passive public data.

### Lab 3 - ATT&CK mapping audit

Take a public report and map only behaviors explicitly described in the source. Record which mappings are certain and which are interpretive.

### Lab 4 - Attribution challenge

Write the strongest alternative explanation for an apparent infrastructure relationship.

## Completion evidence

You have completed the track when you can produce:

- one PIR-driven collection plan;
- one passive infrastructure map with evidence table;
- one UTC-normalized incident timeline;
- one ATT&CK mapping with source references;
- one two-page CTI assessment with explicit confidence and gaps.

## Recommended companion material

- [Research Methods](../docs/research-methods.md)
- [Tool Matrix](../docs/tool-matrix.md)
- [Report Template](../docs/report-template.md)
- [Investigation Playbooks](../playbooks/README.md)
