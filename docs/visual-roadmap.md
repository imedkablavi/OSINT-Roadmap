# Visual OSINT Roadmap

This diagram is intentionally method-first. Tools change; the investigation cycle should remain understandable.

```mermaid
flowchart TD
    A[Start: Define the research question] --> B[Scope, ethics & stop condition]
    B --> C[Foundations]
    C --> C1[Search discipline]
    C --> C2[Source evaluation]
    C --> C3[Documentation & OPSEC]

    C1 --> D[Discovery]
    C2 --> D
    C3 --> D

    D --> D1[Search & archives]
    D --> D2[Public records]
    D --> D3[Social / username leads]
    D --> D4[Domains & public web data]
    D --> D5[Images / video / maps]

    D1 --> E[Verification]
    D2 --> E
    D3 --> E
    D4 --> E
    D5 --> E

    E --> E1[Provenance]
    E --> E2[Independent corroboration]
    E --> E3[Timeline normalization]
    E --> E4[Alternative hypotheses]
    E --> E5[Confidence assessment]

    E1 --> F[Analysis]
    E2 --> F
    E3 --> F
    E4 --> F
    E5 --> F

    F --> G[Reporting]
    G --> G1[Evidence table]
    G --> G2[Confidence + limitations]
    G --> G3[Source log]
    G --> G4[Reproducible conclusion]

    G --> H{Choose specialization}

    H --> I[CTI]
    H --> J[Digital Footprint]
    H --> K[Company Investigation]
    H --> L[GEOINT / Visual Investigation]
    H --> M[Journalism / Fact Checking]
    H --> N[Public Web Infrastructure]

    I --> O[Advanced portfolio]
    J --> O
    K --> O
    L --> O
    M --> O
    N --> O

    O --> P[Review other investigations]
    P --> Q[Teach / mentor / improve methodology]
```

## Learning sequence

```text
FOUNDATIONS
    ↓
DISCOVERY
    ↓
VERIFICATION
    ↓
ANALYSIS
    ↓
REPORTING
    ↓
SPECIALIZATION
    ↓
PORTFOLIO + REVIEW
```

## What “complete” means

A stage is not complete because you know the tool names.

It is complete when you can produce an artifact:

| Stage | Evidence of learning |
| --- | --- |
| Foundations | scoped research question + stop condition |
| Discovery | documented search/source collection plan |
| Verification | provenance table + independent corroboration |
| Analysis | competing-hypothesis table + confidence rationale |
| Reporting | reproducible intelligence note |
| CTI | PIR-driven threat assessment |
| Digital Footprint | privacy-minimized attribution assessment |
| Company | entity-resolution + corporate timeline |
| GEOINT | geolocation report with rejected candidates |

Use the [Skill Matrix](skill-matrix.md) to track progress.
