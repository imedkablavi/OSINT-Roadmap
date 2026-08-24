# Changelog

All notable project changes are documented here.

This project follows [Semantic Versioning](https://semver.org/) for public releases and uses Git tags in the form `vMAJOR.MINOR.PATCH`.

## [Unreleased]

### Added
- Production release audit and stronger Pages smoke-test coverage.
- SEO parity checks for English, Arabic, and Turkish routes.
- A specialist OSINT catalogue that expands Tool Finder coverage across web preservation, identity, media forensics, GEOINT, CTI, public records, transport, datasets, timelines, blockchain, academic research and public SOCMINT discovery.
- Clue-first investigator tool stacks in English, Arabic and Turkish.
- Verified primary-source coverage for UK and UN sanctions, EU and US lobbying disclosures, DOJ FARA filings, NOAA historical weather, global OCDS procurement discovery and beneficial-ownership register discovery.

### Changed
- Arabic and Turkish landing pages expose consistent canonical, hreflang, RSS discovery, social metadata, and structured data.
- Tool Finder, catalogue validation, Pages smoke tests and freshness automation operate across the core and specialist catalogues.
- Public landing-page copy uses a conservative `110+` catalogue claim while the current structured catalogue contains 132 reviewed tools and primary-source resources.
- Newly added resources carry explicit review dates and limitations so matches, filings, sanctions records, metadata and automated enrichment are not presented as automatic proof.

## Release policy

- **MAJOR**: breaking structural changes to public routes, data formats, or contribution contracts.
- **MINOR**: new learning tracks, substantial new site features, or major catalogue expansions that remain backward-compatible.
- **PATCH**: corrections, link/tool maintenance, translation fixes, SEO/accessibility improvements, and non-breaking content updates.

Each release should:

1. Start from a green `main` branch.
2. Update the `Unreleased` section into a dated version section.
3. Create an annotated tag such as `v1.0.0`.
4. Publish GitHub Release notes summarizing user-visible changes and maintenance changes separately.
5. Keep the prior GitHub Pages URL stable unless a migration plan and redirects exist.