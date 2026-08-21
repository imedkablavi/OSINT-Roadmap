# OSINT Browser Extensions & Web Tools

![OSINT Browser Extensions & Web Tools](../assets/osint-browser-tools.svg)

A browser extension can save time, but it can also see sensitive browsing data. Treat extensions as software, not bookmarks: install only what you need, check permissions, prefer maintained projects, and separate research browsing from personal accounts when practical.

> **Rule:** an extension result is a lead. Verify important findings against the underlying source.

## Recommended starter set

If you are new, do not install everything. Start with a small set:

| Need | Recommended starting point | Why |
| --- | --- | --- |
| Save a page | [SingleFile](https://github.com/gildas-lormeau/SingleFile) | Creates a self-contained local HTML copy |
| Historical page | [Wayback Machine](https://web.archive.org/) | Checks archived versions of public pages |
| Monitor changes | [Distill](https://distill.io/) | Watches selected page content for changes |
| Reverse image search | [TinEye](https://tineye.com/) + [Google Lens](https://lens.google/) | Useful complementary image-search approaches |
| Video verification | [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/) | Frames, keyframes and verification helpers |
| IOC enrichment | [VirusTotal](https://www.virustotal.com/) + [urlscan.io](https://urlscan.io/) | Public enrichment and web-observation context |
| Passive infrastructure | [Shodan](https://www.shodan.io/) + [Censys](https://search.censys.io/) | Search already-observed internet data |
| Full-page screenshot | [GoFullPage](https://gofullpage.com/) or [FireShot](https://getfireshot.com/) | Evidence capture with context |
| Structured page data | [Web Scraper](https://webscraper.io/) | Extracts repeated page structures |
| Blockchain lookup | [Etherscan](https://etherscan.io/) / [Blockchair](https://blockchair.com/) | Public transaction and address data |

## 1. Web capture & archiving

### [Hunchly](https://www.hunch.ly/)
Investigation-oriented capture and browsing documentation.

**Useful for:** recording visited public pages, research sessions, URLs and context.

**Do not assume:** a captured page proves the claim on that page is true.

### [Vortimo](https://www.vortimo.com/)
Browser-oriented OSINT workflow and collection tooling.

**Useful for:** organizing information encountered during public web research.

### [Wayback Machine](https://web.archive.org/)
Historical snapshots of public web pages.

**Useful for:** page history, removed statements, previous website structure and timeline work.

**Limitation:** absence from the archive does not prove a page never existed.

### [SingleFile](https://github.com/gildas-lormeau/SingleFile)
Saves a web page into a single HTML file.

**Useful for:** local preservation of the page as viewed during research.

### [Distill Web Monitor](https://distill.io/)
Monitors pages or selected page regions for changes.

**Useful for:** public pages that update over time, such as notices, listings or statements.

## 2. Image & video analysis

### [Google Lens](https://lens.google/)
Visual search and object/text discovery.

### [TinEye](https://tineye.com/)
Reverse-image search focused on finding matching or modified copies.

### [InVID & WeVerify](https://www.invid-project.eu/tools-and-services/invid-verification-plugin/)
Verification plugin with video keyframe and media-analysis helpers.

### [FotoForensics](https://fotoforensics.com/)
Image-forensics learning and analysis service.

**Important:** compression artefacts and ELA patterns are not, by themselves, proof of manipulation.

### [ExifTool](https://exiftool.org/)
Powerful metadata reader for local files.

**Important:** missing metadata is common after social-media upload and is not evidence of fabrication.

## 3. Threat intelligence & IOC lookup

### [Pulsedive](https://pulsedive.com/)
Public threat-intelligence enrichment for indicators.

### [Mitaka](https://github.com/ninoseki/mitaka)
Browser extension that pivots selected indicators into multiple investigation services.

### [VirusTotal](https://www.virustotal.com/)
File, URL, domain and IP enrichment from multiple engines and datasets.

**Privacy note:** do not upload confidential files or sensitive internal URLs to public analysis services.

### [urlscan.io](https://urlscan.io/)
Public website scan observations and page artefacts.

**Privacy note:** understand visibility settings before submitting a URL.

### [Shodan](https://www.shodan.io/)
Searches internet-facing systems previously observed by Shodan.

### [Censys Search](https://search.censys.io/)
Searches internet hosts and certificates from Censys observations.

> Passive search is different from actively probing a system. This roadmap focuses on public/passive research unless you have explicit authorization.

## 4. Data extraction & scraping

### [Instant Data Scraper](https://webrobots.io/instantdata/)
Browser-assisted extraction of repeated page data.

### [Web Scraper](https://webscraper.io/)
Visual scraping workflows for structured public pages.

### [Link Gopher](https://addons.mozilla.org/en-US/firefox/addon/link-gopher/)
Extracts links from a page for review or export.

**Use carefully:** scraping can be restricted by site terms, rate limits, copyright or privacy law. Prefer small, purpose-driven collection.

## 5. Screenshots & media capture

### [GoFullPage](https://gofullpage.com/)
Full-page capture in Chromium-based browsers.

### [FireShot](https://getfireshot.com/)
Page screenshot and export tooling.

### [Screenity](https://github.com/alyssaxuu/screenity)
Open-source screen recorder.

For evidence capture, record the URL, access time, relevant timezone and what the screenshot is intended to show.

## 6. Download helpers

### [DownThemAll!](https://www.downthemall.org/)
Bulk download manager for browser-accessible files.

### [Video DownloadHelper](https://www.downloadhelper.net/)
Browser extension for downloading supported media.

**Boundary:** downloading publicly accessible material can still be limited by copyright, platform terms or local law. Use downloads for legitimate research and preservation.

## 7. Blockchain & crypto investigation

### [Etherscan](https://etherscan.io/)
Ethereum blockchain explorer.

### [Tronscan](https://tronscan.org/)
TRON blockchain explorer.

### [Blockchair](https://blockchair.com/)
Explorer covering multiple blockchains.

### [Breadcrumbs](https://www.breadcrumbs.app/)
Blockchain investigation and visualization platform.

### [Arkham](https://intel.arkm.com/)
Blockchain intelligence and entity-labeling platform.

**Attribution rule:** an address label is not automatically proof that a specific human controls the address. Record the source of the label and confidence.

## Extension safety checklist

Before installing an extension:

- [ ] Is the publisher/project clearly identifiable?
- [ ] Is it actively maintained?
- [ ] Are the requested permissions proportionate to the feature?
- [ ] Can you use a web version instead of granting broad browser access?
- [ ] Does it send visited URLs or page content to a third party?
- [ ] Is the privacy policy understandable?
- [ ] Can you isolate it in a dedicated research browser/profile?

## Suggested research-browser setup

```text
Personal browser/profile
    └─ personal accounts, normal browsing

Research browser/profile
    ├─ minimal extensions
    ├─ no unnecessary personal logins
    ├─ separate downloads folder
    ├─ evidence-capture tools
    └─ clear note-taking workflow
```

## Related roadmap material

- [Tool Matrix](../docs/tool-matrix.md)
- [Investigation Playbooks](../playbooks/README.md)
- [OSINT Quick Reference](../cheatsheets/osint-quick-reference.md)
- [Research Methods](../docs/research-methods.md)
- [Report Template](../docs/report-template.md)

---

This list is curated, not exhaustive. Tools change, disappear and change ownership. Re-check a tool before installing it and report stale links through the repository issue tracker.