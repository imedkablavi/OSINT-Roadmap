# OSINT Tool Matrix

A tool list is only useful when you know **when** to use each tool and what its output can actually prove.

This matrix is intentionally small. It favors reliable, widely used services and manual verification over collecting hundreds of links.

> Before using any service, check its current terms, local law, and whether the target information is genuinely public.

## Search and discovery

| Tool / source | Best used for | Cost | Difficulty | Main limitation |
| --- | --- | --- | --- | --- |
| Google | General discovery, exact phrases, site-specific searching | Free | Beginner | Results are ranked and personalized; absence is not proof |
| Bing | Alternative indexing and image search | Free | Beginner | Different coverage from Google; verify important findings elsewhere |
| Brave Search | Independent search results and comparison | Free / Paid | Beginner | Smaller index for some niche topics |
| DuckDuckGo | Quick general research with less personalization | Free | Beginner | Often depends on third-party indexes |
| Internet Archive | Historical versions of public webpages | Free | Beginner | Captures can be incomplete or missing assets |
| Archive.today | Public webpage snapshots | Free | Beginner | Coverage and availability vary |

## Domains and web infrastructure

| Tool / source | Best used for | Cost | Difficulty | Main limitation |
| --- | --- | --- | --- | --- |
| ICANN Lookup | Registration data that is still public | Free | Beginner | Privacy redaction is common |
| SecurityTrails | DNS and infrastructure history | Freemium | Intermediate | Historical depth depends on plan and coverage |
| DNSDumpster | Visual DNS discovery | Free | Beginner | Treat discovered relationships as leads, not attribution |
| crt.sh | Certificate Transparency searches | Free | Intermediate | Certificates show issuance, not necessarily active ownership |
| urlscan.io | Public scans of websites and resources | Freemium | Intermediate | Public submissions may expose what you search; review privacy settings |
| BuiltWith / Wappalyzer | Website technology identification | Freemium | Beginner | Detection can be stale or incorrect |

## Images and video

| Tool / source | Best used for | Cost | Difficulty | Main limitation |
| --- | --- | --- | --- | --- |
| Google Lens | Reverse image search and visual matches | Free | Beginner | Similarity is not proof of original source |
| Bing Visual Search | Alternative image matches | Free | Beginner | Coverage differs from Google |
| Yandex Images | Visual similarity and regional coverage | Free | Beginner | Results require careful source verification |
| InVID-WeVerify | Keyframes and verification workflow | Free | Intermediate | Helps analysis; it does not automatically verify a claim |
| ExifTool | Reading locally available metadata | Free | Intermediate | Social platforms often strip metadata |

## Maps and geolocation

| Tool / source | Best used for | Cost | Difficulty | Main limitation |
| --- | --- | --- | --- | --- |
| Google Maps | Roads, businesses, landmarks, Street View where available | Free | Beginner | Imagery dates vary |
| Google Earth | Historical imagery and terrain comparison | Free | Intermediate | Coverage is uneven by location and date |
| OpenStreetMap | Community-maintained map data | Free | Beginner | Completeness varies by region |
| Mapillary | Street-level imagery contributed by users | Free | Intermediate | Capture date and coverage vary |
| SunCalc | Sun position and shadow hypothesis checking | Free | Intermediate | Needs a reasonably accurate location/time hypothesis |

## Social platforms and usernames

Start manually. Search the username in quotes, inspect the platform's own public search, compare profile history, and record what actually links two accounts.

Automated username tools can save time, but a matching handle alone is weak evidence. Common names, recycled usernames, impersonation, and inactive accounts produce false positives.

Useful public tools include:

- WhatsMyName - checks a username across many services.
- Sherlock - command-line username checks across supported sites.
- Maigret - broader username enumeration with reporting features.

Treat every hit as a **lead** until another independent signal supports the connection.

## News, claims, and archives

For claim verification, do not search only for the claim wording. Search for:

1. the earliest version you can find;
2. primary documents or first-hand statements;
3. independent reporting;
4. corrections or later updates;
5. archived versions if the page changed.

Useful sources include Google News, GDELT, official public records, newsroom archives, the Internet Archive, and reputable fact-checking organizations.

## A simple selection rule

Before opening another tool, ask:

```text
What question am I trying to answer?
What evidence would actually answer it?
Which source is closest to that evidence?
How will I verify the result independently?
```

If you cannot answer those four questions, adding more tools usually creates noise instead of confidence.
