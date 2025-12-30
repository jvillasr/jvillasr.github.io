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
    - About title should be larger, in line with Research and Resume sections.
    - Profile picture should span the column width.
    - Header text: "Building survey-to-inference pipelines to constrain massive-binary evolution and uncover compact companions at scale." sounds a bit off. It's a good description but it could use some rephrasing. Give me 3 different options to choose from.
    - 
- Add extra buttons to display publications: [DONE][2025-12-24]
    - latest 10 (default)
    - More cited
    - First/second author
- Add "All (ADS)" button next to "first/second author" [DONE][2025-12-24]
- Add research metrics: [DONE][2025-12-24]
    - Total papers
    - total citations
    - h-index
    - g-index
    Add and upward green arrow with the number giving by how much each number increased from 2024 to 2025.
- Add plots of: [DONE][2025-12-24]
    1. papers per year
    2. Citations per year
    3. Reads per year
    4. Indices per year: h-index, g-index, i10-index, read10-index.
    Use data from ADS.
- Add a dedicated publications page (data-driven; keep URLs stable)(optional) [][]
- [BUG] "Research" is the only button in the nav bar that doesn't stay highlighted
- SEO/social previews sanity check (remove duplicate `<title>`, confirm OpenGraph image, add per-page descriptions) [][]
- Analytics: migrate off Universal Analytics (UA) or switch to a privacy-friendly option [][]
- Add automated link checking (GitHub Action) [][]
- Add somewhere past students. [][]
- Update "key results" section of the SDSS-V project with some punchy lines/results from the Zari+2025 paper.
- Update README file, remove everything related to WhatATheme

## Later
- Add “Talks / Posters” page [][]
- Add bilingual support (EN/ES) [][]
- Create a Readthedocs page for MINATO (will be done as part of the minato repo: `/Users/villasenor/science/github/jvillasr/MINATO/minato`)
- Add “Teaching / Outreach” page (optional) [][]
- Add HTML validation / accessibility smoke checks (lightweight) [][]
- Discuss visits metrics; I'd like to have stats of how many people visit the webpage, what do they click on, etc.

## Ideas parking lot
- Dark mode toggle (only if it stays simple and consistent) [][]
- Better publication search (client-side, small, no heavy deps) [][]
- “Featured highlights” strip for top 3 papers/projects [][]
