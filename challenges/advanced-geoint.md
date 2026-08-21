# Advanced GEOINT Challenge Ladder

These challenges are designed for legal practice using training material, public landmarks, or self-created images. Do not use them to track private individuals or sensitive locations.

## How to use this ladder

For each challenge, submit:

1. final location assessment;
2. clue inventory;
3. rejected hypotheses;
4. map/image comparisons;
5. confidence level;
6. what would change your conclusion.

## Level 1 — Country narrowing

Goal: identify the most likely country from non-unique clues.

Look at:

- road markings;
- driving side;
- utility poles;
- language/script;
- vehicle plates without collecting personal data;
- vegetation;
- public transport style.

Do not conclude from one clue.

## Level 2 — City discrimination

You are given three plausible cities in the same country.

Task:

- identify discriminating features;
- compare terrain, architecture, road layout, transit, signage, and skyline;
- explain why the other two candidates are weaker.

## Level 3 — Landmark-free geolocation

No famous landmark is visible.

Use combinations of:

- street geometry;
- building setbacks;
- mountain profiles;
- drainage;
- curb design;
- utility infrastructure;
- shop categories;
- municipal objects.

## Level 4 — Shadow and sun consistency

Given a claimed location and approximate date/time:

- estimate shadow direction;
- compare expected solar azimuth;
- account for camera orientation uncertainty;
- state whether the claim is consistent, inconsistent, or inconclusive.

Shadow analysis rarely proves an exact location by itself.

## Level 5 — Weather corroboration

Compare the visible conditions with historical public weather records.

Check:

- precipitation;
- cloud cover;
- temperature-dependent conditions;
- snow cover;
- wind-sensitive indicators.

Weather is usually corroborative, not uniquely identifying.

## Level 6 — Terrain profile matching

Use ridge lines, coastlines, valleys, or horizon geometry.

Workflow:

```text
extract prominent shapes
→ generate candidate areas
→ compare orientation
→ reject impossible terrain
→ verify with independent clues
```

## Level 7 — Chronolocation

Determine whether imagery plausibly belongs to a claimed period.

Possible clues:

- construction progress;
- storefront changes;
- road works;
- vegetation season;
- public transit liveries;
- temporary event infrastructure;
- archived street imagery;
- historical satellite imagery.

## Level 8 — Multi-image correlation

Given several images that may or may not be from the same area:

- identify repeated structural clues;
- determine whether camera positions can coexist geometrically;
- build a rough spatial model;
- document contradictions.

## Level 9 — Route reconstruction

Using only purpose-built training imagery or public event material, reconstruct an approximate route.

Require at least three independent anchor points.

Never apply this exercise to track a private person's routine or current location.

## Level 10 — Adversarial challenge

You receive an image with one deliberately misleading clue.

Your task is to:

- identify which clue is weakest;
- explain why it could mislead;
- reach a conclusion using independent evidence.

## Scoring rubric

| Area | Points |
| --- | ---: |
| clue diversity | 20 |
| independent verification | 20 |
| rejected alternatives | 20 |
| reproducibility | 15 |
| confidence calibration | 15 |
| ethics/scope discipline | 10 |

90–100: strong professional-style reasoning  
75–89: solid but some assumptions remain  
60–74: useful direction, insufficient verification  
<60: repeat the challenge with better evidence discipline
