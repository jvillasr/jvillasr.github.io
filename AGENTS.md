# AGENTS.md

This repo is my personal website (academic/research profile). Agents and collaborators: follow this file as the single source of truth for how to work here.

## Goal
Maintain a fast, clean, professional website that highlights:
- Research projects
- Publications
- CV / Resume
- Talks / Outreach / Teaching (optional)
- Contact

Primary priorities: clarity, readability, stability, low maintenance, and a polished design.

## Non-goals
- No heavy frameworks (no React rebuild, no complex client-side app)
- No database / server backend
- No “clever” over-engineering
- Avoid fragile build steps and dependency explosions

## Tech assumptions (adjust if repo differs)
- Static site (Jekyll / GitHub Pages compatible)
- Content in Markdown
- Data-driven sections via `_data/*.yml`
- Reusable components via `_includes/` and layouts via `_layouts/`
- Styling via Sass/CSS

If you discover the repo differs, report it to me before making any changes.

---

## Working style rules (important)
1. **Small, reviewable changes**  
   Keep PRs focused. Don’t mix unrelated refactors with content updates.

2. **Do not introduce tables for layout**  
   Use proper semantic HTML and CSS (flex/grid) instead.

3. **Prefer consistency over novelty**  
   Reuse existing components, spacing, typography, and patterns.

4. **Don’t invent macro-like systems unless asked**  
   No new “magic” conventions that are hard to remember. If a reusable abstraction is needed, keep it obvious and documented.

5. **Accessibility is not optional**
   - Meaningful headings (H1 once per page, then H2/H3)
   - Alt text for images (or empty alt for purely decorative)
   - Sufficient contrast and readable font sizes

6. **Stability matters**
   - Don’t break existing URLs
   - Don’t rename pages/paths without redirects or strong reason
   - Avoid changes that require manual steps every update

7. **Update CHANGELOG**
    - After making changes always update the CHANGELOG
    - Add "DONE" labels to added features/solved problems in ROADMAP.
    - Always follow the GitHub workflow after making changes: Add, commit, push.
    - For deep changes/large works, crate a new branch to test changes and make sure we don't break things.
---

## Definition of Done (for any change)
- Site builds locally without errors
- No obvious layout regressions on mobile + desktop widths
- No broken internal links introduced
- Content is consistent in tone and formatting
- Images are optimized (reasonable size; no multi-MB uncompressed assets)

---

## Suggested local workflow (if Jekyll)
Run locally:
- `bundle install`
- `bundle exec jekyll serve` (or `bundle exec jekyll build`)

If the repo uses a different toolchain, follow the existing README.

---

## Content conventions
### Publications
- Publications should be data-driven if possible (YAML/JSON in `_data/`)
- Keep citation links stable and prefer authoritative sources (publisher / DOI / ADS)
- Avoid duplicating the same publication info across multiple files

### Projects / Research pages
- Each project should have: short summary, key results, role, links (paper/code), and a clean hero image (optional)
- Prefer concise text and scannable structure

### CV / Resume
- Single source of truth (avoid maintaining the same content in 3 places)
- If PDF is generated, keep the pipeline simple and documented

---

## Branch + commit hygiene
- Use feature branches (e.g., `feat/resume`, `fix/nav-spacing`)
- Commit messages: short and descriptive
  - `feat: add resume section`
  - `fix: correct publication year ordering`
  - `style: tighten spacing on research cards`

---

## When unsure
If you hit ambiguity:
- Inspect existing patterns and copy them
- Prefer the smallest change that solves the problem
- Leave a short note in the PR describing the decision and tradeoff
- Report to me
