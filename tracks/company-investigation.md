# Company Investigation Track

A public-source workflow for understanding companies, ownership, filings, sanctions exposure, web presence, and public relationships without treating registry data as infallible.

## Learning goals

You should be able to:

- identify the correct legal entity;
- distinguish trade names from registered names;
- compare official filings across time;
- investigate directors, beneficial ownership where lawfully public, subsidiaries, parent entities, and addresses;
- map public domains and corporate web history;
- review sanctions and watchlist references carefully;
- document source jurisdiction and update dates;
- separate verified corporate relationships from inferred associations.

## Stage 1 — Entity resolution

Start by proving you have the right entity.

Collect:

- legal name;
- registration number;
- jurisdiction;
- registered address;
- incorporation date;
- status;
- known trading names;
- official website.

Do not rely on a company name alone. Names can be duplicated across jurisdictions.

## Stage 2 — Source hierarchy

Prefer:

1. official national/company registry;
2. regulatory filings;
3. stock-exchange or securities filings;
4. official company disclosures;
5. reputable aggregators that link back to original records;
6. news and third-party profiles.

Aggregators are useful for discovery, but important facts should be checked against the underlying record when available.

## Stage 3 — Ownership and control

Record each relationship separately.

| Entity/person | Relationship | Source | Effective date | Confidence | Notes |
| --- | --- | --- | --- | --- | --- |
| Parent A | owns 75% of Company B | filing | date | High | direct disclosure |
| Person C | director | registry | date | High | role may have ended later |

Check whether the record is current. A historical director is not necessarily a current director.

## Stage 4 — Corporate timeline

Track:

- incorporation;
- name changes;
- director appointments/resignations;
- address changes;
- mergers/acquisitions;
- major filings;
- public website changes;
- sanctions/listing events;
- dissolution or insolvency events.

## Stage 5 — Sanctions and watchlists

When checking sanctions:

- verify exact entity identifiers;
- check aliases;
- compare jurisdiction and address;
- distinguish an entity from similarly named organizations;
- record the issuing authority and date;
- do not treat an aggregator match as final confirmation.

## Stage 6 — Web presence

Useful public questions:

- Which domains are officially linked by the company?
- How has the website changed over time?
- Which contact details are self-published?
- Are subsidiary or brand websites linked from official pages?
- Do archived pages reveal historical names or business lines?

## Stage 7 — Relationship mapping

Map only relationships you can label precisely.

Use labels such as:

```text
registered director
shareholder according to filing dated X
subsidiary according to annual report
same registered address
website linked from official company page
reported commercial partner
```

Avoid vague graph edges such as “connected to” unless you explain what the connection actually is.

## Stage 8 — Risk-aware reporting

A company investigation can affect real organizations and people. Use neutral language and cite the underlying source.

Good:

```text
Registry X lists Person A as a director as of DATE.
```

Bad:

```text
Person A secretly controls the company.
```

unless reliable public evidence actually supports that conclusion.

## Practice labs

1. Resolve two same-name companies in different jurisdictions.
2. Build a five-year corporate timeline from official filings.
3. Compare an aggregator profile against the original registry.
4. Map a fictional company's parent/subsidiary structure from supplied training records.
5. Audit a sanctions match for false positives.

## Completion evidence

Produce:

- one entity-resolution worksheet;
- one ownership table;
- one corporate timeline;
- one source-backed relationship map;
- one concise company profile with limitations.
