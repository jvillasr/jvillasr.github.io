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
- ADS sync script now defaults to the standard YAML paths and library name (no need to pass file names)
- ADS sync script now supports a manual delta year for metrics (stored in `_data/ads_metrics.yml`)
- Resume publications layout: metrics title + filters below publications heading + plots in 2x2 grid
- Resume publications list: stronger title/author hierarchy and lighter author/journal styling
- Resume publication metrics now append the year to each delta value
- Resume publication plots now use an explicit SVG height so lines render consistently
- Resume publication plots now include padding so baseline lines stay visible
- Resume publication plot point lists now use comma separators to survive HTML compression
- Resume publication plots now include axes, yearly ticks, and markers
- Resume publication index chart now scales read10 by 10 for balance
- Resume publication plots now rotate year labels and show hover tooltips per marker
- Resume publication plots now tighten the left axis spacing, boost marker hover size, and recolor index lines
- Resume publication plot tooltips now render as inline labels on hover
- Resume publication plot tooltips now use styled pill labels and index legend colors match line colors
- Index plot hover labels now use the "label: value" format
- Resume publication plots now place y-axis ticks/labels inside to reduce left gutter
- Resume publication plots now pull the y-axis closer to the left edge
- Resume publication plot cards now reduce left padding to minimize extra whitespace
- Resume publication plots now align viewbox and aspect ratio to remove extra horizontal padding
- Resume publication plots now place y-axis labels outside and bring x-labels closer
- Resume publication plots now allocate more left margin for y-axis labels and tighten x-label spacing
- Resume publication plots now anchor y-axis labels to the left of the axis
- Resume publication plots now reserve extra space for larger y-axis labels
- Resume publication plots now abbreviate large y-axis labels with k-suffixes
- Resume publication plot ticks now round to multiples of 10 (midpoints align on 5s)
- Resume publication section subtitles now use a larger font size
- Resume publications ADS button now matches the black filter styling
- Resume publications ADS button now keeps the full pill border
- Resume publications section now uses a top-level "Publications" heading with a list subtitle and ADS button
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
- Resume publication metrics totals updated and plots rendered correctly

---

## 2025-12-24
### Added
- Repository workflow files: AGENTS.md, CHANGELOG.md, ROADMAP.md

### Changed
- (initial baseline)

### Fixed
- (initial baseline)
