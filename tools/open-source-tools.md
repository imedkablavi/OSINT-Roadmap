# Verified Open-Source OSINT Tools

> Reviewed: **2026-08-24** · English · [العربية](open-source-tools.ar.md) · [Türkçe](open-source-tools.tr.md)

This page highlights open-source tools whose current upstream project, license, and practical role were verified before inclusion. Open source does **not** remove authorization, privacy, provider-terms, or data-handling obligations.

| Tool | License | Input | Best for | Important limitation |
| --- | --- | --- | --- | --- |
| [theHarvester](https://github.com/laramies/theHarvester) | GPL-2.0 | Domain, organization | Aggregating public passive sources for hosts, domains and related discovery | Provider coverage, quotas and API-key requirements change; some options add network activity |
| [OWASP Amass](https://github.com/owasp-amass/amass) | Apache-2.0 | Domain, organization, ASN | External asset discovery and attack-surface mapping | Active techniques must only be used on targets you own or are explicitly authorized to assess |
| [Subfinder](https://github.com/projectdiscovery/subfinder) | MIT | Domain | Passive subdomain enumeration across supported sources | Many useful providers require API keys and upstream sources can change or disappear |
| [OpenCTI Community Edition](https://github.com/OpenCTI-Platform/opencti) | Apache-2.0 (CE) | IOC, organization, report | Structuring, linking and visualizing CTI knowledge using STIX2 | It is a platform, not a truth engine; confidence and source provenance still need analyst review |
| [MISP](https://github.com/MISP/MISP) | AGPL-3.0 | IOC, event, organization | Threat-intelligence sharing, structured events and indicator communities | Community data quality varies; sharing rules and sensitive-data handling need governance |

## Selection notes

- **theHarvester** is useful when you want a reproducible aggregator over selected public sources instead of manually querying each provider. Start with the smallest set of sources needed for the question.
- **OWASP Amass** is a mature framework for deeper external asset discovery. Keep passive and active collection clearly separated in authorized workflows.
- **Subfinder** is a focused passive subdomain enumerator and is easier to automate than a full attack-surface platform.
- **OpenCTI Community Edition** is appropriate when the problem is organizing CTI knowledge, relationships, provenance and confidence rather than collecting one more IOC.
- **MISP** is appropriate for structured threat-intelligence exchange and community sharing workflows.

## Safe-use rule

For infrastructure tools, public availability is not authorization. Passive providers still receive query terms, may log requests, and apply their own terms and quotas. Active DNS resolution, probing, scanning, or validation should be limited to owned or explicitly authorized scope.

A tool output is a lead or observation. Preserve the source, timestamp, query, confidence and important limitations before using it in a report.
