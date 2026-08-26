# Digital Footprint Investigation Track

This track teaches how to assess a public digital footprint without turning weak correlations into identity claims.

## Core principle

A digital footprint is a collection of public traces. It is not automatically a verified identity map.

## Learning goals

You should be able to:

- define a lawful research question;
- separate discovery from attribution;
- pivot across usernames, public profiles, domains, documents, and public archives;
- compare stable and unstable identifiers;
- build timelines of public activity;
- record conflicting evidence;
- stop when the evidence no longer justifies the collection.

## Stage 1 - Define the seed

Common public seeds:

- username;
- public display name;
- public website;
- domain;
- public profile URL;
- public document author field;
- company or project name.

Avoid beginning with sensitive personal information unless it is necessary, lawful, and directly relevant to the research question.

## Stage 2 - Discovery table

Create a table before deciding whether two results are related.

| Result | Platform/source | Matching signal | Conflicting signal | First/last observed | Status |
| --- | --- | --- | --- | --- | --- |
| profile A | platform | same username | different biography | dates | lead |
| profile B | platform | same avatar | username differs | dates | lead |

## Stage 3 - Stable identifiers

Signals vary in strength.

Potentially stronger public indicators:

- exact linked domain;
- self-declared cross-profile link;
- same unique public portfolio;
- repeated unique phrase combined with other evidence;
- consistent public contact channel published by the subject.

Weak indicators:

- same common name;
- same generic avatar;
- same city;
- same interests;
- similar writing style alone;
- username similarity alone.

## Stage 4 - Archive history

Use archived versions to answer:

- Did the profile or site previously link to another public account?
- When did a username, biography, or project name change?
- Is a current claim contradicted by an earlier public version?

Record the archive timestamp separately from the original content date.

## Stage 5 - Timeline

Normalize important events:

```text
DATE/TIME | source | observation | confidence | notes
```

Look for both supporting and conflicting sequences. A timeline is especially useful when two profiles appear similar but were active in impossible or inconsistent ways.

## Stage 6 - Attribution scorecard

Do not use a single numeric score as proof. Use a structured rationale instead.

| Signal | Supports | Conflicts | Strength |
| --- | --- | --- | --- |
| self-link | yes | | strong |
| same username | yes | | weak |
| overlapping active dates | yes | | medium |
| different public identity statement | | yes | strong conflict |

Conclusion examples:

```text
Likely related, but ownership is not independently confirmed.
Public self-link confirms the two profiles were presented as related at the observed time.
Insufficient evidence to attribute both profiles to the same person.
```

## Stage 7 - Privacy minimization

Collect only what is relevant to the question. Do not turn a research exercise into a personal dossier.

Stop when:

- the research question is answered;
- additional collection would add sensitive personal detail without analytical value;
- the next step requires private access, deception, or bypassing a restriction.

## Practice labs

1. Compare two purpose-built training profiles and test whether they represent the same fictional entity.
2. Reconstruct a public project's naming history using archives.
3. Build a provenance table for a username across public sources.
4. Write an attribution assessment that includes the strongest conflicting evidence.

## Completion evidence

Produce:

- one discovery table;
- one archive-backed timeline;
- one attribution assessment;
- one privacy-minimized final report.
