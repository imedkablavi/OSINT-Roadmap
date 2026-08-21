# OSINT Quick Reference

A compact field reference for lawful public-source research.

## Before collecting

```text
Question → Scope → Sources → Verification plan → Stop condition
```

Write down:

- what you need to know;
- what you do not need to know;
- time period;
- legal/ethical boundaries;
- what evidence would be strong enough to answer the question.

## Search patterns

```text
"exact phrase"
site:example.com keyword
site:example.com filetype:pdf keyword
intitle:"report" keyword
before:2025-01-01 after:2024-01-01 keyword
"username" -irrelevant -terms
```

Also try:

- spelling variants;
- transliteration variants;
- local-language terms;
- abbreviations;
- old names;
- date ranges;
- multiple search engines.

## Source verification

Check:

- original publisher;
- publication date;
- event date;
- source independence;
- archive history;
- direct evidence vs interpretation;
- contradictions;
- missing context.

## Image/video

```text
original context
→ reverse search
→ earliest appearance
→ visual clue inventory
→ location/time tests
→ independent corroboration
```

Remember:

- missing EXIF is normal;
- shadows are supporting evidence, not magic;
- reuploads can destroy metadata;
- captions can be wrong even when the media is authentic.

## Username attribution

Strong-ish signals when independently supported:

- explicit self-link;
- same unique portfolio/project;
- consistent public contact channel;
- archive-confirmed cross-link.

Weak signals:

- same username;
- same city;
- similar avatar;
- similar interests;
- writing style alone.

## Domain/web

Passive pivots:

- current site;
- archives;
- RDAP/WHOIS;
- DNS;
- Certificate Transparency;
- passive scan datasets;
- web technologies;
- public company/project links.

Shared IP/CDN/ASN ≠ common owner.

## Company research

```text
legal name
+ registration number
+ jurisdiction
+ official filings
+ effective dates
+ current/historical roles
+ ownership where public
+ web history
+ sanctions exact-match checks
```

## Timeline

Normalize to UTC when comparing sources.

Track separately:

- event time;
- publication time;
- first observed time;
- update time;
- archive capture time.

## Confidence language

Use calibrated wording:

```text
Confirmed
Highly likely
Likely
Plausible
Insufficient evidence
Unresolved
Contradicted by available evidence
```

Explain *why*.

## Evidence table

| Claim | Source | Direct/indirect | Independent? | Supports/contradicts | Confidence |
| --- | --- | --- | --- | --- | --- |

## Reporting

Minimum useful report:

1. question;
2. scope;
3. key findings;
4. evidence;
5. analysis;
6. alternative explanations;
7. confidence;
8. limitations;
9. source log.

## Stop rules

Stop if:

- the question is answered;
- new collection adds no analytical value;
- the next step requires deception or private access;
- collection becomes unrelated or unnecessarily sensitive;
- you are only gathering more data because it is available.
