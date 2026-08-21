# Investigation Playbooks

Use these playbooks when you have a starting clue and need to decide what to do next. They are decision guides, not automation recipes.

## I have a domain

```text
Define question
→ confirm exact domain and time period
→ inspect current site
→ review archives
→ inspect RDAP/WHOIS where available
→ inspect DNS / certificate transparency / passive records
→ identify self-declared company or project links
→ build timeline
→ corroborate important relationships
→ report limitations
```

Ask:

- Is this the correct domain or a lookalike?
- Who publicly claims it?
- What changed over time?
- Which infrastructure relationships are common/shared and therefore weak?
- Does a historical DNS or certificate relationship answer the research question?

Stop before active exploitation, intrusive scanning, authentication bypass, or private access.

## I have a username

```text
Define attribution question
→ search exact username
→ search variants/transliterations
→ collect public candidate profiles
→ compare self-links and stable identifiers
→ inspect archives if relevant
→ build supporting/conflicting evidence table
→ assess attribution confidence
```

Never treat a username match alone as identity proof.

## I have an image

```text
Preserve original context
→ note claimed time/location
→ reverse image search
→ find earliest public appearance
→ inventory visual clues
→ test geolocation candidates
→ test time/weather/shadow clues if useful
→ search for independent context
→ state confidence and unresolved gaps
```

Do not infer sensitive personal details that are unrelated to the research question.

## I have a video

```text
Preserve source URL/context
→ extract representative frames
→ reverse-search key frames
→ inspect audio/text/signage
→ identify scene changes
→ geolocate individual scenes
→ compare claimed timeline
→ locate original/earliest upload where possible
→ document edits or uncertainty
```

## I have a company name

```text
Resolve legal entity
→ identify jurisdiction + registration number
→ check official registry/filings
→ record current vs historical officers/addresses
→ review ownership/subsidiaries where public
→ check official web presence + archives
→ review sanctions/watchlists carefully
→ build relationship table
→ report exact source dates
```

A name match is not enough. Resolve the entity first.

## I have an IP address

```text
Define why the IP matters
→ identify ASN/provider
→ review passive public service/history data
→ inspect historical domain resolutions
→ compare timestamps
→ identify shared hosting/CDN context
→ corroborate any claimed relationship
```

An IP shared by many customers is weak attribution evidence.

## I have a public document

```text
Save source + timestamp
→ identify publisher
→ inspect document metadata cautiously
→ extract names/dates/entities
→ verify key statements against external sources
→ search unique phrases for prior versions
→ compare document revisions if available
→ build source log
```

Metadata is a lead, not guaranteed truth.

## I have a news claim

```text
Capture exact claim
→ locate earliest source
→ distinguish reporting from original evidence
→ search official/primary records
→ compare independent reporting
→ normalize dates/times
→ identify copied-source chains
→ write confirmed / disputed / unknown
```

## I have a location claim

```text
Record exact claimed location
→ list observable clues
→ generate multiple candidates
→ eliminate contradictions
→ compare maps/street/satellite imagery
→ use terrain/weather/shadow as corroboration
→ search independent event context
→ state precision honestly
```

City-level evidence does not justify building-level precision.

## Universal stop questions

Before another pivot, ask:

1. Does this step answer the original question?
2. Is the source genuinely public and lawful to use?
3. Will this add evidence or only more data?
4. Am I collecting sensitive detail that is unnecessary?
5. Would another independent source be more valuable?
6. Is the next action intrusive, deceptive, or outside scope?

If the answer to #6 is yes, stop.
