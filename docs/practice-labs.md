# OSINT Practice Labs

These labs are designed to build investigation habits without targeting private individuals or requiring restricted access.

Use fictional, historical, institutional, or clearly public-interest subjects. Document uncertainty and stop when a task would require deception, bypassing access controls, or collecting sensitive personal data.

## Lab 1 - Trace the first public source

**Level:** Beginner  
**Time:** 20–30 minutes

Pick a public claim from a company blog, government announcement, news story, or public dataset.

Your task:

1. Save the version of the claim you started with.
2. Search for earlier appearances of the same claim.
3. Find the closest available primary source.
4. Compare dates and wording.
5. Write three lines explaining which source should be cited and why.

**Skill:** source provenance.

**Do not assume:** the highest-ranking search result is the original source.

---

## Lab 2 - Rebuild a changed webpage

**Level:** Beginner

Choose a public webpage that has existed for several years, such as a project page, company page, documentation site, or public organization profile.

Your task:

1. Open the current page.
2. Find at least two archived versions.
3. Record what changed: names, dates, products, claims, or contact information.
4. Separate meaningful changes from design changes.
5. Create a short timeline.

**Skill:** web archives and temporal reasoning.

---

## Lab 3 - Verify a public image

**Level:** Beginner / Intermediate

Use an image from a news article, official public account, Wikimedia Commons, or another source where the context is safe to investigate.

Your task:

1. Find earlier appearances with reverse-image search.
2. Identify visible landmarks, signs, terrain, road markings, or weather clues.
3. Compare those clues against maps or street-level imagery.
4. Check whether the claimed date is consistent with the earliest appearance.
5. State what you can verify and what remains uncertain.

**Skill:** visual verification.

A useful conclusion sounds like:

> The location is strongly supported by A and B, but the capture date cannot be independently confirmed.

---

## Lab 4 - Map a public web footprint

**Level:** Intermediate

Choose a public organization, open-source project, conference, or company domain.

Your task:

1. Identify the official domain.
2. Review public DNS records.
3. Search Certificate Transparency logs.
4. Inspect archived versions of the website.
5. Identify technologies visible from public sources.
6. Build a small diagram showing confirmed infrastructure and unconfirmed leads separately.

**Skill:** infrastructure research and evidence labeling.

**Important:** discovering a hostname does not prove who operates the underlying server.

---

## Lab 5 - Test a username attribution hypothesis

**Level:** Intermediate

Do this only with a fictional identity, your own accounts, a consenting participant, or a public organization/brand.

Create a hypothesis that two public profiles may be connected.

Compare signals such as:

- exact username reuse;
- linked websites;
- self-declared cross-links;
- identical public profile descriptions;
- matching public project references;
- timing and posting patterns, used cautiously.

Then score the evidence:

| Signal | Strength | Why |
| --- | --- | --- |
| Same username only | Weak | Handles can be reused by unrelated people |
| One account links directly to the other | Strong | Explicit public connection |
| Same avatar only | Weak–Medium | Images can be copied |
| Same unique project linked from both | Medium–Strong | More specific, but still needs context |

**Skill:** attribution without overclaiming.

---

## Lab 6 - Build and challenge a timeline

**Level:** Intermediate

Choose a well-documented public event.

Collect 8–12 timestamped sources and build a timeline. Then try to disprove your own interpretation.

Ask:

- Are timestamps in different time zones?
- Was an article updated after publication?
- Is a screenshot missing context?
- Is a social post quoting an older event?
- Do two sources depend on the same original report?

**Skill:** chronology and source independence.

---

## Lab 7 - Geolocation from non-sensitive public material

**Level:** Intermediate / Advanced

Use a tourism image, historical photo, public challenge image, or a geolocation puzzle intentionally published for investigation.

Work from broad to narrow:

```text
Country / region
→ city or area
→ road / landmark cluster
→ exact viewpoint, if evidence allows
```

Record every clue and one alternative explanation for it. Do not geolocate private residences or people who have not intentionally made their location public.

**Skill:** structured geolocation.

---

## Lab 8 - Write a one-page intelligence note

**Level:** Any

Take one completed lab and turn it into a concise report containing:

- Question
- Scope
- Key finding
- Evidence
- Confidence
- Alternative explanation
- Limitations
- Sources with access dates

Then remove every sentence that is not supported by evidence or necessary context.

**Skill:** professional reporting.

---

# Scoring yourself

Use this simple rubric after each lab:

| Area | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Scope | Undefined | Partly defined | Clear and respected |
| Sources | One weak source | Multiple but dependent | Multiple independent sources |
| Verification | None | Partial | Key claims cross-checked |
| Notes | Missing | Incomplete | Reproducible |
| Confidence | Overstated | Vague | Explicit and justified |
| Limitations | Missing | Generic | Specific to the investigation |

A perfect score is less important than being able to explain why you gave yourself each score.
