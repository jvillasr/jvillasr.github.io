---
layout: project
title: "MINATO — Massive bINaries Analysis TOols"
subtitle: "Open-source Python tools for precise RVs, orbital periods, and spectral analysis of massive binaries."
slug: minato
tags: [minato, software, binaries]
hero_image: /assets/projects/minato_hero.jpg
hero_caption: "Example line-profile fits (left) and RV curve + orbital model (right) produced with minato.ravel."
hero_credit: 'Credit: Adapted from Villaseñor et al. (2025), <a href="https://www.aanda.org/articles/aa/full_html/2025/06/aa53166-24/aa53166-24.html"><em>A&amp;A</em> 698, A41</a>'
hero_alt: "Example RV curve and spectral-line fit from MINATO.ravel"
links:
  - label: "GitHub"
    url: "https://github.com/jvillasr/MINATO"
  - label: "Latest release"
    url: "https://github.com/jvillasr/MINATO/releases"
  - label: "Tutorials"
    url: "https://github.com/jvillasr/MINATO/tree/develop/minato/tutorials"
  - label: "Issues"
    url: "https://github.com/jvillasr/MINATO/issues"
  # - label: "Docs"
  #   url: "https://jvillasr.github.io/MINATO"   # add after we generate docs
---

## Overview
MINATO is a set of Python tools to analyse massive binary stars: robust **radial velocities** via **spectral line fitting** for SB1/SB2 systems, **orbital period search**, and **binary spectral analysis** using atmosphere models. It’s the toolkit behind several of my first-author results and is being prepared for broader community use.  

<div class="notification is-light">
<strong>At a glance</strong><br>
• Modules: <code>ravel</code> (RVs, time series), <code>span</code> (spectral analysis)<br>
• Used in: BBC I, BBC II, BLOeM, and ongoing projects.<br>
• License: MIT • Public releases (v0.2.0) • Python 3.10+<br>
</div>

## Why it matters
Accurate RVs and stellar atmosphere analysis are the bottleneck for tight orbits, interaction products, and compact-companion candidates. MINATO standardises those steps so results are reproducible across surveys and follow-up programs.

## Features
- **RVs & time series (`ravel`)**: line-profile fitting for SB1/SB2; Lomb–Scargle, FAP; sinusoidal fits to phased RVs.  
- **Spectral analysis (`span`)**: simultaneous binary fits for Teff, log g, v sin i, He/H, light ratio; synthetic model grids.
- **Roadmap**: SED fitting, spectral classification, and binary population simulations.

## How to install
<details>
  <summary><strong>Clone & run locally</strong></summary>
  <pre><code class="language-bash">git clone https://github.com/jvillasr/MINATO
cd MINATO
mamba env create -f minato_env.yml  # or: conda env create -f minato_env.yml
conda activate minato</code></pre>
</details>

## How to cite
<div class="notification is-light" markdown="1">
If you use MINATO in your research, please cite:

- **For `span`:**  
  [Villaseñor et al. (2023), MNRAS, 525, 5121](https://ui.adsabs.harvard.edu/abs/2023MNRAS.525.5121V/abstract)

- **For `ravel`:**  
  [Villaseñor et al. (2025), A&amp;A, 698, A41](https://ui.adsabs.harvard.edu/abs/2025A%26A...698A..41V/abstract)
</div>