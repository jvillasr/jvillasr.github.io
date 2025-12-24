# ROADMAP.md

## Status convention
Each item ends with `[][]`.

- First bracket: fill with `STARTED` (optional) or `DONE` when completed
- Second bracket: fill with completion date (`YYYY-MM-DD`)

Example:
- Add link-check workflow [DONE][2025-12-15]

---

## Now (highest priority)
- Fix icon display in section 'Contact' and in the footer (only Bluesky icon showing) [DONE][2025-12-24]
- Publications: Start with the Title, then authors (Currently the other way around). Add hovering effect in title. [DONE][2025-12-24]
- Homepage hero copy: upgrade `site.description` + CTA (make it specific and scannable) [DONE][2025-12-24]
- Navigation polish: anchors from subpages + mobile menu behavior [DONE][2025-12-24]
- Publications: verify data quality + tags + stable links (DOI/ADS/arXiv) [DONE][2025-12-24]
- Performance quick wins: compress large images + lazy-load below-the-fold media [DONE][2025-12-24]
- Projects: ensure each project page has role, key results, and links (paper/code) [DONE][2025-12-24]
- Blog: start document to put ideas about future blog entries [DONE][2025-12-24]

## Next
- Re-style the "About" section. Follow instructions in `about-revamp.md`. This will need a new branch to work on these changes. [STARTED][2025-12-24]
- Add extra buttons to display publications:
    - latest 10 (default)
    - More cited
    - First/second author
- Add a dedicated publications page (data-driven; keep URLs stable)(optional) [][]
- SEO/social previews sanity check (remove duplicate `<title>`, confirm OpenGraph image, add per-page descriptions) [][]
- Analytics: migrate off Universal Analytics (UA) or switch to a privacy-friendly option [][]
- Add automated link checking (GitHub Action) [][]
- Add somewhere past students.
- Update "key results" section of the SDSS-V project with some punchy lines/results from the Zari+2025 paper.
- Update README file, remove everything related to WhatATheme

## Later
- Add bilingual support (EN/ES) [][]
- Create a Readthedocs page for MINATO (part of the minato repo: `/Users/villasenor/science/github/jvillasr/MINATO/minato`)
- Add “Talks / Posters” page (data-driven; optional) [][]
- Add “Teaching / Outreach” page (optional) [][]
- Add HTML validation / accessibility smoke checks (lightweight) [][]

## Ideas parking lot
- Dark mode toggle (only if it stays simple and consistent) [][]
- Better publication search (client-side, small, no heavy deps) [][]
- “Featured highlights” strip for top 3 papers/projects [][]
