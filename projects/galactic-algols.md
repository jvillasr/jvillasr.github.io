---
layout: project
title: "Galactic Algols Project"
subtitle: "Using high-resolution, multi-epoch spectroscopy to pin down mass-transfer efficiency in massive Algol binaries."
slug: algols
tags: [algols, binaries, mass-transfer, spectroscopy]
hero_image: /assets/projects/algol3_banner.jpg         # replace with a 3:2 or 16:9 banner
hero_caption: "Artist’s impression of an Algol-type binary: gas overflows from the donor star (left) and feeds a disc around the accretor (right)."
hero_credit: 'Image: Jaime Villaseñor (generated with GPT-5 and Google AI Studio, 2025). Licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>.'
hero_alt: "Mass transfer in an Algol binary: stream from donor to disc around accretor."
links:
  - label: "FEROS @ ESO/MPG 2.2 m"
    url: "https://www.eso.org/sci/facilities/lasilla/instruments/feros.html"
#   - label: "ADS (Algol papers)"
#     url: "https://ui.adsabs.harvard.edu/search/q=all%3A%28Algol%20binary%29%20AND%20author%3A%28Villase%C3%B1or%29&sort=date%20desc"
---

## Overview

Most massive stars (M ≳ 8 M☉) live in binaries and many **exchange mass**—a process that reshapes their spins, orbits, and final fates. The **efficiency** of that mass transfer remains one of the biggest unknowns in binary-evolution models. This project searches for **mass-transferring Algol systems** (semi-detached binaries) at high spectral resolution and over multiple epochs to measure precise **orbits**, **component spectra**, and **atmospheric parameters**, to confronts detailed evolution models.

<div class="notification is-light">
<strong>At a glance</strong><br>
• Telescope/instrument: ESO/MPG 2.2 m + FEROS (R≈48 000, 360–920 nm)<br>
• Time awarded: 76 h in P113 and 92 h in P114<br>
• Sample: 98 southern Algol/semidetached candidates, V ≲ 11, periods ≲ 12 d, earlier than B3<br>
• Observing strategy: 8 epochs per target; individual S/N = 90 at 4000 Å to reach combined S/N ≈ 250 for spectral disentangling.<br>
• Status: Student-led (F. Wallauer) first analysis (RV variability and initial orbital solutions) underway<br>
</div>

## Science goals

1) **Constrain mass-transfer efficiency.** Compare measured mass ratios (q), periods (P), and component properties against grids of detailed binary-evolution models to discriminate between conservative and non-conservative mass transfer pathways.

2) **Recover component spectra.** Use spectral **disentangling** to isolate both stars, then fit for **T<sub>eff</sub>**, **log g**, **v sin i**, and key **abundances** (He, N) to identify interaction products (stripped/bloated donors).

3) **Build a benchmark sample.** Massive Algols with well-measured parameters are surprisingly rare; this programme aims to deliver a homogeneous set suitable for constraining binary interactions and evolution.

## Methods

- **RVs & orbits.** Line-profile fitting to obtain RVs for SB1 and SB2 systems; full orbital solutions.
- **Spectral disentangling.** Separate composite spectra into primary/secondary contributions; recover **K<sub>1</sub>, K<sub>2</sub>** and flux ratios directly from the data.
- **Atmosphere analysis.** Joint fitting of both components with non-LTE models to obtain **T<sub>eff</sub>**, **log g**, **v sin i**, **He/N** abundances and masses.  

## Team & roles

- **PI / lead:** Jaime Villaseñor (programme design, RV/orbital pipeline; disentangling; atmosphere analysis).
- **Student:** Farah Wallauer (MPIA Summer Intern) leading the first pass on RVs and orbital solutions (2025).
- **Collaborators:** Koushik Sen (University of Arizona), Norbert Langer (Universität Bonn)

## Key results (so far)
- **Survey set-up:** target sample and observing strategy defined (98 candidates; multi-epoch FEROS spectroscopy).
- **First-pass results:** RV variability screening and initial orbital solutions underway (student-led).

## Publications
<div class="pubs">
  {% include publications.html data="papers_all" tag="algols" year_headings="true" authors="short" first_n="8" %}
</div>
