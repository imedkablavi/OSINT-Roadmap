# OSINT Tool Library

> Reviewed: **2026-08-22** · English · [العربية](tool-library.ar.md) · [Türkçe](tool-library.tr.md)

This is a **curated learning library**, not a dump of every OSINT link on the internet. Tools are included when they solve a clear public-source research problem and can be placed inside a reproducible workflow.

A tool result is a **lead or observation**, not automatic proof. Important findings should be checked against the underlying source and, when possible, corroborated independently.

## How to read the library

| Field | Meaning |
| --- | --- |
| Input | What you normally start with |
| Cost | Free, freemium, paid, or self-hosted |
| Level | Beginner, intermediate, or advanced |
| Best for | The question the tool helps answer |
| Main limitation | What the result does **not** prove or where it can mislead |

## Quick starter kits

### Beginner core

Google Search · Internet Archive · SingleFile · Google Lens · TinEye · Google Earth · OpenStreetMap · ExifTool

### GEOINT

Google Earth · OpenStreetMap · Mapillary · SunCalc · PeakVisor · Copernicus Browser · NASA Worldview · QGIS

### CTI / infrastructure

VirusTotal · urlscan.io · Shodan · Censys · GreyNoise · ThreatFox · RIPEstat · crt.sh

### Company research

OpenCorporates · GLEIF LEI Search · OpenSanctions · OCCRP Aleph · ICIJ Offshore Leaks · SEC EDGAR · Companies House

### Research monitoring

Internet Archive · Archive.today · changedetection.io · GDELT · Hunchly · SingleFile · OpenRefine

---

# 1. Search, discovery & archives

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [Google Search](https://www.google.com/) | keywords, names, domains | Free | Beginner | broad discovery, exact phrases, `site:` and file searches | ranking and personalization can hide results |
| [Bing](https://www.bing.com/) | keywords, images | Free | Beginner | second search index and visual discovery | coverage differs from Google |
| [Brave Search](https://search.brave.com/) | keywords | Free / paid | Beginner | another independent search perspective | smaller coverage in some niches |
| [Kagi](https://kagi.com/) | keywords | Paid | Beginner | low-noise search and research workflows | subscription required |
| [SearXNG](https://searxng.org/) | keywords | Free / self-hosted | Intermediate | metasearch across multiple engines | result quality depends on configured engines |
| [GDELT](https://www.gdeltproject.org/) | topics, entities, locations | Free | Intermediate | large-scale news/event discovery and trend exploration | event extraction needs contextual verification |
| [Google Scholar](https://scholar.google.com/) | academic terms, authors | Free | Beginner | papers, citations and grey-literature leads | not every indexed item is peer reviewed |
| [Internet Archive / Wayback Machine](https://web.archive.org/) | URL | Free | Beginner | historical public web pages | missing capture is not proof a page never existed |
| [Archive.today](https://archive.ph/) | URL | Free | Beginner | point-in-time public page snapshots | availability and completeness vary |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | webpage | Free | Beginner | preserving a page locally as one HTML file | captures what your browser rendered, not server history |
| [ArchiveBox](https://archivebox.io/) | URLs | Free / self-hosted | Intermediate | building a local research archive | requires storage and maintenance |
| [changedetection.io](https://changedetection.io/) | URL | Free / paid / self-hosted | Intermediate | monitoring page changes over time | dynamic pages can create noisy changes |

# 2. Usernames & public identity clues

Use identity tools only for a legitimate research question. A matching username, avatar, or display name does **not** prove two accounts belong to the same person.

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) | username | Free | Beginner | checking a handle across many public services | false positives and recycled usernames |
| [Sherlock](https://github.com/sherlock-project/sherlock) | username | Free | Intermediate | command-line username checks | a hit only shows a matching handle exists |
| [Maigret](https://github.com/soxoj/maigret) | username | Free | Intermediate | broader username enumeration and reports | site checks can break when platforms change |
| [Epieos](https://epieos.com/) | email / phone where lawful | Freemium | Intermediate | discovering public account clues and pivots | results can be sensitive; minimize collection and verify independently |
| [GitHub Search](https://github.com/search) | username, code, organization | Free | Beginner | public profiles, repositories, commits and code references | GitHub identity does not automatically map to a real-world identity |

# 3. Image & video verification

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [Google Lens](https://lens.google/) | image | Free | Beginner | visual matches, objects, text and related pages | similarity is not provenance |
| [TinEye](https://tineye.com/) | image | Free / paid | Beginner | finding matching or modified copies | smaller index than general search engines |
| [Yandex Images](https://yandex.com/images/) | image | Free | Beginner | alternative visual similarity search | results require source verification |
| [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) | video / image / URL | Free | Intermediate | keyframes and verification helpers | assists analysis; does not verify a claim automatically |
| [ExifTool](https://exiftool.org/) | local media/document file | Free | Intermediate | reading metadata from many file types | metadata may be stripped or manipulated |
| [FotoForensics](https://fotoforensics.com/) | image | Free | Intermediate | learning image-forensics signals such as compression patterns | ELA/compression patterns alone do not prove manipulation |
| [FFmpeg](https://ffmpeg.org/) | video/audio file | Free | Intermediate | extracting frames, audio and transcoding for analysis | processing changes files; preserve originals separately |

# 4. GEOINT, maps & satellite imagery

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [Google Maps](https://maps.google.com/) | location / coordinates | Free | Beginner | roads, businesses, landmarks and Street View | imagery and business data can be outdated |
| [Google Earth](https://earth.google.com/) | location / coordinates | Free | Beginner | terrain, 3D context and historical imagery where available | historical coverage varies by place |
| [OpenStreetMap](https://www.openstreetmap.org/) | location / feature | Free | Beginner | open map data, roads and mapped features | community coverage is uneven |
| [Mapillary](https://www.mapillary.com/) | location | Free | Intermediate | crowdsourced street-level imagery | dates and coverage vary widely |
| [SunCalc](https://www.suncalc.org/) | location + time hypothesis | Free | Intermediate | testing sun and shadow direction | useful only with a reasonable location/time hypothesis |
| [PeakVisor](https://peakvisor.com/) | landscape / location | Freemium | Intermediate | mountain and skyline identification | terrain similarity can create false matches |
| [Copernicus Browser](https://dataspace.copernicus.eu/browser/) | area + date | Free account | Intermediate | Sentinel imagery, comparison, analysis and downloads | cloud cover and spatial resolution limit some questions |
| [NASA Worldview](https://worldview.earthdata.nasa.gov/) | area + date | Free | Intermediate | near-real-time Earth observation layers and environmental events | many layers are lower resolution than commercial imagery |
| [QGIS](https://qgis.org/) | geospatial files / layers | Free | Advanced | combining, measuring and analyzing map/satellite data | requires GIS knowledge and careful coordinate handling |

# 5. Domains, IPs & internet infrastructure

These resources are primarily for **passive observation of public records and already-collected datasets**. Active probing or scanning may require explicit authorization.

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [ICANN Lookup](https://lookup.icann.org/) | domain | Free | Beginner | current public registration/RDAP data | privacy redaction is common |
| [crt.sh](https://crt.sh/) | domain / organization | Free | Intermediate | Certificate Transparency history | certificate issuance does not prove current ownership |
| [SecurityTrails](https://securitytrails.com/) | domain / IP | Freemium | Intermediate | DNS history and infrastructure context | depth depends on coverage and plan |
| [DNSDumpster](https://dnsdumpster.com/) | domain | Free | Beginner | visual DNS and host discovery | discovered relationships are leads, not attribution |
| [BuiltWith](https://builtwith.com/) | domain | Freemium | Beginner | website technology signals | detection can be stale or incomplete |
| [Wappalyzer](https://www.wappalyzer.com/) | webpage / domain | Freemium | Beginner | technologies used by a website | client-side detection can be wrong |
| [RIPEstat](https://stat.ripe.net/) | IP / ASN | Free | Intermediate | routing, allocation and ASN context | allocation does not prove who operated a host at a specific moment |
| [BGP.tools](https://bgp.tools/) | ASN / IP prefix | Free | Intermediate | BGP routing and network ownership context | routing relationships change over time |
| [Cloudflare Radar](https://radar.cloudflare.com/) | domain / ASN / trend | Free | Intermediate | internet traffic, routing and technology trends | aggregated observations are not a complete internet view |

# 6. CTI & public indicator enrichment

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [VirusTotal](https://www.virustotal.com/) | hash, URL, domain, IP, file | Freemium | Beginner | multi-source enrichment and historical context | public uploads can expose sensitive material |
| [urlscan.io](https://urlscan.io/) | URL / domain | Freemium | Intermediate | page requests, DOM, screenshots and observed infrastructure | submission visibility matters; do not send sensitive internal URLs publicly |
| [Shodan](https://www.shodan.io/) | IP / domain / query | Freemium | Intermediate | already-observed internet-facing services | data may be stale; do not treat a banner as current fact |
| [Censys Search](https://search.censys.io/) | IP / domain / certificate | Freemium | Intermediate | hosts, services and certificate observations | observations reflect scan timing and coverage |
| [GreyNoise](https://viz.greynoise.io/) | IP | Freemium | Intermediate | understanding internet scanning/noise context | classification is contextual, not proof of intent |
| [AlienVault OTX](https://otx.alienvault.com/) | IOC | Free | Intermediate | community threat pulses and indicator context | community intelligence varies in quality |
| [Pulsedive](https://pulsedive.com/) | domain / IP / URL | Freemium | Beginner | quick threat-intel enrichment | scoring should be checked against source evidence |
| [ThreatFox](https://threatfox.abuse.ch/) | IOC | Free | Intermediate | community malware-related indicators | indicators age quickly |
| [URLhaus](https://urlhaus.abuse.ch/) | URL / host | Free | Intermediate | malware-distribution URLs | absence is not evidence of safety |
| [MalwareBazaar](https://bazaar.abuse.ch/) | hash / malware sample metadata | Free | Intermediate | malware sample intelligence and hashes | handling live samples requires specialist safety controls |
| [AbuseIPDB](https://www.abuseipdb.com/) | IP | Freemium | Beginner | community abuse reports | reports can be wrong or outdated |

# 7. Company, ownership & public records

A database match is not a finding by itself. Resolve the legal entity using jurisdiction, identifiers, dates and addresses before drawing conclusions.

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [OpenCorporates](https://opencorporates.com/) | company / officer | Freemium | Beginner | cross-jurisdiction company discovery | source coverage varies by registry |
| [GLEIF LEI Search](https://search.gleif.org/) | legal name / LEI | Free | Intermediate | standardized legal-entity identifiers and parent relationships when reported | only entities with LEIs are covered |
| [OpenSanctions](https://www.opensanctions.org/) | person / organization | Free for non-commercial / paid | Intermediate | sanctions, PEP and entity datasets with source provenance | a name match alone is not identity confirmation |
| [OCCRP Aleph](https://aleph.occrp.org/) | person / company / document | Free account / public-interest access | Intermediate | investigative documents and structured entity data | dataset availability depends on collections and access |
| [ICIJ Offshore Leaks Database](https://offshoreleaks.icij.org/) | name / company / address | Free | Intermediate | offshore-entity relationships from major investigations | inclusion does not imply illegal conduct; identity must be confirmed |
| [SEC EDGAR](https://www.sec.gov/search-filings) | US issuer / ticker / CIK | Free | Intermediate | official US public-company filings | scope is mainly SEC-regulated entities and filings |
| [UK Companies House](https://find-and-update.company-information.service.gov.uk/) | UK company / officer | Free | Beginner | official UK company filings and officers | filings may contain outdated or self-reported information |

# 8. Aviation, maritime & transport

Tracking platforms have coverage gaps, delayed data and blocked/filtered targets. Use multiple sources and preserve timestamps.

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [Flightradar24](https://www.flightradar24.com/) | flight / aircraft / location | Freemium | Beginner | live and historical flight context | coverage and history depend on receivers and plan |
| [ADS-B Exchange](https://www.adsbexchange.com/) | aircraft / location | Freemium | Intermediate | ADS-B aircraft observations | not every aircraft broadcasts complete data |
| [OpenSky Network](https://opensky-network.org/) | aircraft / time / area | Free / research access | Intermediate | aviation datasets and research queries | historical/API access has limits |
| [MarineTraffic](https://www.marinetraffic.com/) | vessel / IMO / MMSI | Freemium | Beginner | AIS-based vessel positions and port activity | AIS can be absent, delayed or incorrect |
| [VesselFinder](https://www.vesselfinder.com/) | vessel / IMO / MMSI | Freemium | Beginner | alternative AIS vessel tracking | same AIS coverage limitations apply |

# 9. Documents, structured data & cleanup

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [Apache Tika](https://tika.apache.org/) | documents/files | Free | Advanced | extracting text and metadata from many file formats | extracted text can lose layout/context |
| [OCRmyPDF](https://ocrmypdf.readthedocs.io/) | scanned PDF | Free | Intermediate | adding searchable OCR text to PDFs | OCR errors must be checked against the scan |
| [Tabula](https://tabula.technology/) | PDF tables | Free | Beginner | extracting tabular data from PDFs | complex layouts need manual cleanup |
| [OpenRefine](https://openrefine.org/) | CSV / spreadsheet-like data | Free | Intermediate | cleaning, reconciling and normalizing messy data | transformations can hide mistakes if not logged |
| [CyberChef](https://gchq.github.io/CyberChef/) | text / encoded data / files | Free | Intermediate | decoding and transforming technical data | transformations are not interpretation or attribution |
| [jq](https://jqlang.org/) | JSON | Free | Intermediate | querying and transforming structured JSON | command-line learning curve |

# 10. Investigation workspace & relationship analysis

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [Hunchly](https://www.hunch.ly/) | browsing session | Paid | Beginner | preserving visited pages and research context | capture does not validate page claims |
| [Vortimo](https://www.vortimo.com/) | web research | Freemium / paid | Intermediate | organizing public web investigation material | workflow value depends on disciplined tagging/notes |
| [Maltego](https://www.maltego.com/) | entities / indicators | Freemium / paid | Intermediate | relationship graphs and data pivots | transforms can create impressive-looking but weak associations |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | domain / IP / name and other seeds | Free / commercial options | Advanced | automating many OSINT collection modules | automation creates noise and requires validation |
| [Gephi](https://gephi.org/) | graph/network data | Free | Advanced | visualizing large relationship networks | visual proximity does not equal real-world causation |

# 11. Blockchain & cryptocurrency research

| Tool | Input | Cost | Level | Best for | Main limitation |
| --- | --- | --- | --- | --- | --- |
| [Etherscan](https://etherscan.io/) | Ethereum address / tx / contract | Free / paid API | Beginner | Ethereum transactions and contracts | address ownership usually requires external attribution evidence |
| [Tronscan](https://tronscan.org/) | TRON address / tx | Free | Beginner | TRON activity and contracts | on-chain activity does not identify a human by itself |
| [Blockchair](https://blockchair.com/) | address / tx / block | Freemium | Beginner | multi-chain exploration | chain coverage/features differ by network |
| [Breadcrumbs](https://www.breadcrumbs.app/) | crypto address | Freemium | Intermediate | transaction graphing and investigation | clusters/labels require provenance checks |
| [Arkham](https://intel.arkm.com/) | address / entity label | Freemium | Intermediate | entity labels and transaction relationships | a platform label is a lead, not automatic identity proof |

---

# Learning resources worth bookmarking

These resources teach methods, not only tools.

| Resource | Why it is useful |
| --- | --- |
| [Bellingcat Online Investigations Toolkit](https://bellingcat.gitbook.io/toolkit) | curated tools with use cases, cost, difficulty, requirements and limitations |
| [OSINT Dojo](https://www.osintdojo.com/) | progressive challenges and skill ranks for beginners |
| [GIJN Resource Center](https://gijn.org/resource/) | investigative guides, databases, verification, companies, satellite imagery and more; available in many languages |
| [Verification Handbook](https://verificationhandbook.com/) | structured digital-content verification methods |
| [OSINT Framework](https://osintframework.com/) | fast visual discovery of categories and public research resources |
| [IntelTechniques Tools](https://inteltechniques.com/tools/) | practical search utilities and research references |
| [Awesome OSINT](https://github.com/jivoi/awesome-osint) | broad community-maintained directory when you need coverage beyond this curated set |
| [OSINT Tools Library](https://github.com/The-OSINT-Newsletter/OSINT-Tools-Library) | investigation-focused tool directory with maintenance emphasis |

# Tool selection workflow

```text
Start with the research question
        ↓
Identify the input you actually have
        ↓
Choose the smallest tool that answers one question
        ↓
Record source + time + query
        ↓
Verify the result against the underlying source
        ↓
Corroborate important claims independently
        ↓
Document uncertainty and stop conditions
```

# Maintenance policy

A tool should be removed or downgraded when:

- the official project is abandoned and alternatives are stronger;
- the service becomes unreliable or deceptive;
- its permissions or privacy model materially worsen;
- it primarily depends on unlawfully obtained private data;
- its output cannot be explained or verified;
- the official URL changes and cannot be confirmed.

If you notice a change, use the repository's **Resource suggestion** or **Broken link** issue template.
