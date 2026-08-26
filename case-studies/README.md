# Real-World OSINT Case Study Lessons

This section is not a collection of sensational stories. It extracts reusable methodology from well-known public-source investigations and verification work.

The cases below should be studied from the original publishers and supporting sources. Do not copy conclusions blindly; focus on the workflow and evidence discipline.

## 1 - MH17 open-source investigation

Public investigations into the downing of Malaysia Airlines Flight 17 became a major example of combining social media, imagery, geolocation, vehicle identification, timelines, and public records.

### What to study

- how individual images/videos were geolocated before being placed into a wider narrative;
- how a route can be reconstructed from multiple independently verified observations;
- why timestamps, upload times, and event times must be separated;
- how visual details become useful only when they are reproducible;
- how attribution requires a higher evidence threshold than object or location identification.

### Exercise

Do **not** redo the entire investigation. Pick one published geolocation example and reconstruct only the verification steps from cited public material.

## 2 - Verification of reused or miscaptioned conflict imagery

Newsrooms and verification teams repeatedly encounter authentic images or videos presented with the wrong date, location, or event description.

### What to study

- reverse image search as a provenance tool;
- finding the earliest known public appearance;
- comparing captions across reuploads;
- checking weather, architecture, language, and terrain;
- separating “the media is authentic” from “the caption is accurate.”

### Exercise

Choose a debunked public example from a reputable fact-checking organization. Build a two-column table:

| Claim | What the original evidence actually supports |
| --- | --- |

## 3 - Corporate ownership investigations

Investigative journalism projects frequently combine official company registries, leaked/public datasets, regulatory filings, addresses, directors, and historical company records.

### What to study

- entity resolution before relationship mapping;
- why exact legal names and registration numbers matter;
- current vs historical directors;
- jurisdiction-specific definitions of ownership/control;
- how shared addresses can be meaningful or completely routine;
- the importance of preserving filing dates.

### Exercise

Select a public company that has subsidiaries in multiple countries. Build a relationship map using only official company disclosures and government/regulatory records.

## 4 - Capitol / public-event visual verification workflows

Large public events generate huge volumes of publicly posted images and videos. Verification teams often reconstruct sequences using landmarks, timestamps, camera angles, and cross-source corroboration.

### What to study

- event timeline normalization;
- matching the same scene from multiple public viewpoints;
- source dependency: ten reposts may still represent one original source;
- preserving uncertainty when exact timing cannot be established;
- why public-event verification should not become unrelated personal profiling.

### Exercise

Use a non-sensitive public event such as a parade, launch, sporting celebration, or press event. Build a five-event timeline from independent public sources.

## 5 - Satellite imagery and change detection

Human-rights researchers, journalists, disaster analysts, and investigators use public/commercial satellite imagery to compare locations before and after reported events.

### What to study

- image acquisition date vs publication date;
- cloud cover and sensor limitations;
- resolution limits;
- identifying stable reference features;
- distinguishing visible change from claims about who caused it;
- corroborating imagery with ground-level public sources.

### Exercise

Use a public, non-sensitive example such as construction, wildfire damage, flood extent, or infrastructure development. Document what change is visible and what cannot be inferred from imagery alone.

## 6 - Public web infrastructure investigations

Threat researchers often connect domains, certificates, passive DNS, hosting, URLs, and malware reports to understand campaigns.

### What to study

- timestamped infrastructure relationships;
- shared hosting false positives;
- historical vs current DNS;
- certificate reuse;
- separating campaign linkage from actor attribution;
- comparing multiple vendor reports for source independence.

### Exercise

Use indicators from a public cybersecurity training report or official advisory. Build an evidence table using passive public data only.

## Case-study worksheet

For every case, answer:

```text
Research question:
What was the seed clue?
Which evidence was primary?
Which evidence was only supporting?
Which sources were independent?
What alternative explanation existed?
What was the strongest reproducible step?
Where could the investigation overclaim?
What would lower confidence?
What can I reuse in another investigation?
```

## Case-study rule

The goal is not to memorize famous conclusions.

The goal is to recognize repeatable patterns:

```text
provenance
→ verification
→ independent corroboration
→ structured analysis
→ calibrated conclusion
```
