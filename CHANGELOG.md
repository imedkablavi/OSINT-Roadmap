# Changelog

All notable project changes are documented here.

This project follows [Semantic Versioning](https://semver.org/) for public releases and uses Git tags in the form `vMAJOR.MINOR.PATCH`.

## [Unreleased]

### Added
- Production release audit and stronger Pages smoke-test coverage.
- SEO parity checks for English, Arabic, and Turkish routes.

### Changed
- Arabic and Turkish landing pages now expose consistent canonical, hreflang, RSS discovery, social metadata, and structured data.
- Localized landing pages now match the maintained 80+ tool catalogue claim.

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
