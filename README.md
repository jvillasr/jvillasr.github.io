# Jaime I. Villaseñor Website

This repository contains the source for my personal academic website:
[jvillasr.github.io](https://jvillasr.github.io).

The site is a lightweight Jekyll project for presenting:

- research projects
- publications and metrics
- CV and career history
- selected writing
- contact details

## Tech stack

- Jekyll
- Liquid templates
- Sass
- GitHub Pages-compatible static output

## Local development

Install dependencies:

```bash
bundle install
```

Build the site:

```bash
bundle exec jekyll build
```

Serve locally:

```bash
bundle exec jekyll serve
```

The local preview is usually available at [http://127.0.0.1:4000](http://127.0.0.1:4000).

## Repository structure

- `_includes/`: reusable page sections and components
- `_layouts/`: page and post layouts
- `_sass/`: Sass partials
- `_data/`: structured content, including publications and ADS metrics
- `projects/`: project pages
- `assets/`: images, styles, and other static files
- `scripts/`: helper scripts for data refresh tasks

## Publications workflow

Publications and metrics are maintained from ADS data.

Refresh publications and metrics:

```bash
./scripts/update_ads_pubs.py --metrics
```

This updates:

- `_data/papers_all.yml`
- `_data/ads_metrics.yml`

The script expects an `ADS_DEV_KEY` environment variable to be set locally.

## Content notes

- Keep publication links stable and prefer DOI, publisher, or ADS links.
- Prefer editing shared data files rather than duplicating publication content across pages.
- Keep site changes small and reviewable.

## License

This repository is distributed under the terms in [LICENSE](LICENSE).
