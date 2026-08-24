# OSINT Tools Hub

This directory contains the roadmap's maintained tool references.

## Main library

- [English Tool Library](tool-library.md)
- [مكتبة الأدوات بالعربية](tool-library.ar.md)
- [Türkçe Araç Kütüphanesi](tool-library.tr.md)

The main library is organized by **research question and input**, not by popularity. Each category explains cost, skill level, best use and the main limitation of the output.

## Investigator stack — start from the clue you have

The expanded investigator stack maps common starting clues to a small, defensible set of tools instead of encouraging users to run everything:

- [English — OSINT Investigator Tool Stack](investigator-stack.md)
- [العربية — حزمة أدوات الباحث في OSINT](investigator-stack.ar.md)
- [Türkçe — OSINT Araştırmacı Araç Seti](investigator-stack.tr.md)

It covers usernames, email, phone, domains, IP/ASN, images, video/audio, GEOINT, companies, sanctions, lobbying/FARA, procurement, beneficial ownership, court records, CTI, transport, crypto, documents, datasets, timelines, academic research and evidence preservation.

## Source trust taxonomy

Tool Finder separates **what a resource is** from what its output proves. `site/tool-trust.json` adds reviewed metadata without changing the underlying tool catalogue.

Source types are deliberately small and controlled:

- **Official primary source** — an official government or intergovernmental system publishing the underlying record or dataset.
- **Registry / primary source** — an authoritative registry or standards-based source such as legal-entity, domain or publication metadata.
- **Public dataset / index** — a maintained public index or aggregation that should still be traced to its upstream sources for important claims.
- **Community / secondary source** — community-maintained or secondary material useful for discovery and corroboration, not a replacement for the underlying evidence.
- **Open-source tool** — derived from the catalogue only when an upstream repository and explicit license are present.
- **Hosted service / resource** — the conservative default when a stronger source classification is not explicitly supported.

`Jurisdiction` records legal or institutional scope where it matters, such as `US`, `UK`, `EU`, `UN / Global` or `EPO / Global`. Unclassified resources default to `Global / varies` rather than guessing a legal scope.

A source-type badge is **not a confidence score**. Official records can contain amendments, reporting delays, name collisions or jurisdiction-specific meanings. Always inspect date, identifiers, provenance and the record's procedural context.

## Verified open-source tools

A focused list of open-source tools with verified upstream repositories, licenses, use cases and limitations is maintained in all three project languages:

- [English — Verified Open-Source OSINT Tools](open-source-tools.md)
- [العربية — أدوات OSINT مفتوحة المصدر الموثقة](open-source-tools.ar.md)
- [Türkçe — Doğrulanmış Açık Kaynak OSINT Araçları](open-source-tools.tr.md)

Open source does not remove authorization, privacy or provider-terms requirements. Public source code without a clear license is **not** labelled open source in the structured catalogue.

## Interactive Tool Finder

Use:

**https://imedkablavi.github.io/OSINT-Roadmap/tool-finder.html**

The finder combines the core and specialist catalogues and filters by:

- Domain / URL / IP / ASN
- Username / Email / Phone / Name
- Image / Video / Audio
- Location / Coordinates
- Organization / public records
- Document / File / Dataset
- Aircraft / Flight / Vessel / rail context
- Crypto Address / Transaction / Block
- DOI / ORCID / academic research
- Source type / jurisdiction
- Category / cost / skill level / open-source license

## Browser extensions

- [English browser extensions guide](browser-extensions.md)
- [الدليل العربي لإضافات المتصفح](browser-extensions.ar.md)
- [Türkçe tarayıcı eklentileri rehberi](browser-extensions.tr.md)

The browser guide focuses on extension permissions, privacy and research-profile separation.

## Tool updates

- [OSINT Tool Radar — August 2026](../updates/2026-08-tool-radar.md)
- [All project updates](../updates/README.md)

## Selection rule

```text
Research question
      ↓
Input you actually have
      ↓
Smallest useful tool
      ↓
Underlying source
      ↓
Independent verification
      ↓
Document confidence + limits
```

A tool stays in this project because it remains useful, explainable and maintainable — not because it appears in an old OSINT list.