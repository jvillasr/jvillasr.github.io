# "About" Section Revamp Guidelines (Funding-First, Non-Redundant)

Goal: Redesign the **About** section so it serves the *funding-committee path* through the site.
It must **not repeat** content already covered in:
- **HOME hero** (broad research framing),
- **RESEARCH** (projects and details),
- **RESUME** (positions, education, timeline).

The About section should answer:
1) **Why fund Jaime?** (credibility + strategy + execution)
2) **What’s the unique edge?** (method + scale + reproducibility)
3) **What will be delivered next?** (direction, not a CV)

---

## 0) Hard constraints

- Do **not** re-state “Astronomer exploring massive binary stars…” (already on HOME).
- Do **not** re-state affiliation/title like “Researcher at MPIA” as the main payload (already on RESUME).
- Do **not** re-list projects (SDSS-V, BBC, BLOeM, Algols, MINATO) as a “card catalog” (already on RESEARCH).
- No broken images. If any image is missing, replace with **SVG icon** immediately.
- Keep the section to **one screen height** on desktop (approx.), with clear scannability.
- Use consistent visual language (either *all icons* or *all mini-illustrations*, but not mixed).

---

## 1) Layout concept: “Clean academic hero + 3 pillars”

### Desktop layout
Two columns:
- **Left column**: identity + hook + action
- **Right column**: three stacked pillar cards

### Mobile layout
- Portrait + hook first
- Pillars stacked
- Credibility strip becomes a compact list (2×2 grid or vertical)

---

## 2) Left column content (Identity + committee-ready hook)

### 2.1 Portrait
- Use existing portrait, but simplify styling:
  - remove heavy multi-ring decoration
  - max: one subtle ring OR none

### 2.2 Headline (positioning line)
One sentence, grant-style. Must be:
- specific (massive binaries + surveys + inference)
- impact-oriented (compact objects / GW progenitors / evolution constraints)
- NOT a repetition of the HOME line

**Example pattern (do not copy verbatim):**
“Building survey-to-inference pipelines to constrain massive-binary evolution and uncover compact companions at scale.”

### 2.3 Micro-abstract (60–90 words)
A short paragraph that follows:
- **Problem → Approach → Payoff**

Rules:
- Avoid listing institutions or degrees
- Avoid listing project names
- Focus on what you *deliver* as a researcher

**Structure:**
- Problem: what’s missing in the field (demographics / interaction products / compact companions)
- Approach: surveys + RV inference + targeted follow-up + open pipelines
- Payoff: population constraints relevant to compact-object formation and GW sources

### 2.4 Credibility chips (3–5)
Small tags under the micro-abstract. Examples:
- `Survey-scale spectroscopy`
- `Probabilistic inference`
- `Binary evolution`
- `Open-source pipelines`
- `Compact companions`

Avoid:
- “MPIA”, “Heidelberg”, “Chile” as chips (too biographical; use pillars for narrative if needed)

### 2.5 CTA buttons (2 primary actions + 1 subtle link)
- Primary button: `Download CV`
- Secondary button: `Research` (scroll/link)
- Text link: `Contact`

Rules:
- CTAs should be visible without scrolling
- Use consistent style with site buttons
- No extra CTAs in this area

---

## 3) Right column: the 3 pillar cards (Background / Currently / Research focus)

General rules for all cards:
- Titles in **sentence case**, not ALL CAPS
- Each card contains:
  - small icon (same style across all 3)
  - 2–4 bullets max
  - optional “micro-proof line” in muted text (1 line)
- Avoid repeating content that belongs in RESUME or RESEARCH

### 3.1 Pillar 1 — Background (NOT a mini CV)
Purpose: communicate *how Jaime thinks and what perspective he brings*.
Do:
- one line on international training context (Chile/Europe) as *context*, not the point
- emphasize methodological identity and working style
- focus on “bridging surveys and physics” rather than geography

Content guidelines:
- Bullet 1: training perspective (quantitative spectroscopy + binaries)
- Bullet 2: strength: linking observation → inference → population interpretation
- Bullet 3: value: reproducibility / tool-building / collaboration

Optional accent:
- a tiny “Chile → Europe” mini-line graphic as a footer accent
- only if the other two cards also have subtle, matching footer accents

Avoid:
- listing degrees, years, or full institution history (RESUME has that)
- “Born in Chile” as the main line (fine as a small aside only)

### 3.2 Pillar 2 — Currently (Execution, not affiliation)
Purpose: show what’s being *executed now* that funding accelerates.

Content guidelines (choose 3–4 bullets total):
- “Now building”: survey-to-inference pipeline, RV/orbit inference at scale
- “Now leading”: coordination/ownership responsibilities (function, not title soup)
- “Now shipping”: open-source tooling, reusable pipeline components, reproducible outputs
- “Now enabling”: targeted follow-up strategy (as a method, not a list of instruments)

Micro-proof line example types:
- “From survey selection → RV modeling → population constraints.”
- “Tooling designed for collaboration and reproducibility.”

Avoid:
- “Postdoc at MPIA” as the headline bullet (belongs elsewhere)
- listing project names as the main bullets

### 3.3 Pillar 3 — Research focus (Committees want questions)
Purpose: state a coherent program via 3 concrete research questions.

Write as questions (preferred) or strongly framed themes.
Must be more specific than HOME, but not a list of projects.

Recommended 3 focus questions:
1) environment/metallicity dependence of close-binary demographics
2) identifying observable interaction products (mass transfer, mergers)
3) efficient discovery/validation of compact companions in large surveys

Include a tiny “pipeline diagram” visual (new element not elsewhere on the site):
- `Survey → RVs → Orbits → Populations → Compact objects / GW`
Rules:
- simple SVG preferred
- keep it subtle and consistent with site style

Avoid:
- repeating the HOME phrasing (“massive binary stars & gravitational waves”)
- listing SDSS-V/BBC/etc. in the focus card

---

## 4) Add a “Credibility strip” under the pillars (funding signal)

A thin horizontal strip directly below the pillar cards.
It must be **scannable** and contain 4 items max.

Each item should be a short label + short descriptor.
Examples of categories (choose 4):
- **Scale**: “Survey-scale spectroscopy”
- **Inference**: “Probabilistic RV/orbit modeling”
- **Delivery**: “Open-source tools & reproducible pipelines”
- **Leadership**: “Coordination & lead-author execution”
- **Impact**: “Compact companions & evolution constraints”

Rules:
- do not include exact metrics unless they are verified and maintained
- keep to 1 line per item on desktop
- on mobile, collapse into 2×2 grid or vertical list

---

## 5) Keep the storytelling, but move it into an accordion

If there is longer narrative text (e.g., “why massive binaries matter”),
move it into a collapsible section titled:

- “Why massive binaries?”
or
- “Why this problem matters”

Rules:
- Default collapsed
- 1–2 paragraphs max inside
- No duplication with HOME hero text; rewrite to complement it

---

## 6) Visual design requirements (to fix the current “dashboard” feel)

- Remove thick black borders; use:
  - light neutral border OR none
  - soft shadow
- Reduce corner radius slightly (less “UI kit”)
- Ensure consistent spacing:
  - reduce empty whitespace above cards
  - align card heights visually
- Unify imagery:
  - choose icons OR mini-illustrations, not both
  - no mismatched styles (no mixed clipart + line drawing + photo)
- Typography:
  - titles: sentence case
  - body: slightly larger font + increased line-height
  - keep bullets short (max 1 line each on desktop when possible)

---

## 7) Acceptance checklist (Definition of Done)

- [ ] About fits within ~1 desktop viewport height (no “unfinished empty” look)
- [ ] No repeated content from HOME/RESEARCH/RESUME (especially the “research focus” phrasing)
- [ ] 3 pillar cards read as: *perspective → execution → program*
- [ ] Credibility strip present and scannable
- [ ] All images present; no broken placeholders; SVG icons used where possible
- [ ] One consistent illustration/icon language across the section
- [ ] Clear CTA path: CV → Research → Contact

---

## 8) Implementation notes (for agent)

- Prefer implementing About as a dedicated include:
  - `_includes/about.html` + `_sass/_about.scss` (or equivalent)
- Keep content in a data file if site uses structured data:
  - e.g. `_data/about.yml` for bullets and labels
- Ensure responsive behavior:
  - 2-column → stacked at mobile breakpoint
  - pillar cards remain readable and not cramped
- Test in:
  - desktop wide
  - desktop narrow
  - mobile
- Validate that internal anchors (Research, Resume, Contact) scroll correctly
