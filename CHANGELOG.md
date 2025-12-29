# CHANGELOG.md

All notable changes to this website will be documented here.

Format inspired by "Keep a Changelog".
This project does not need strict SemVer; entries are grouped by release date.

## Unreleased
### Added
- `notes/blog-ideas.md` (repo-only; excluded from site build)
- New blog post: `The Universe’s Power Couples: Why Massive Binary Stars Run the Show`
- Resume publications dashboard with filters, metrics, and ADS plots
- ADS metrics dataset for resume publications (`_data/ads_metrics.yml`)

### Changed
- Homepage hero tagline and CTA (`site.description`, hero button points to Research)
- Navbar links use relative `/#section` anchors; improved mobile menu close behavior
- Publications dataset refreshed from ADS (`_data/papers_all.yml`)
- Publications UI: show title first; improved title hover/focus styling
- Publications badges: stronger hover/focus affordance (ADS/arXiv/DOI/Cited)
- Publications data: strip ADS HTML from titles; include page ranges when present
- Publications resume panel: add Latest/Most cited/First-author filters and sparkline plots
- ADS sync script now exports metrics/plots (`scripts/update_ads_pubs.py --metrics`)
- Homepage hero background now uses a local, smaller image (`heroimage: /assets/images/30dor.jpeg`)
- Images resized and lazy-loaded in About/footer for faster loads
- Project pages: added “Key results (so far)” where missing
- Roadmap reprioritised to reflect current site state
- Sample theme posts are kept locally but removed from the published blog
- Blog post layout: constrain header width for readability
- Blog post layout: single-column hero + left-aligned metadata

### Fixed
- Jekyll Sass build failure caused by non-ASCII characters in SCSS
- Stray closing `</a>` in hero section markup
- Contact/footer icon sizing and alignment (switch key icons to inline SVG so they render without Font Awesome)
- Missing About illustrations (`research`/`how`) replaced with lightweight SVGs
- Blog listing and search links now use relative URLs (local preview stays on localhost)
- Cache-bust `assets/css/style.css` per build revision to avoid stale CSS on GitHub Pages
- Footer Contact link now points to the homepage `#contact` section

---

## 2025-12-24
### Added
- Repository workflow files: AGENTS.md, CHANGELOG.md, ROADMAP.md

### Changed
- (initial baseline)

### Fixed
- (initial baseline)
