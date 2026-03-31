#!/usr/bin/env bash
# Refresh ADS publications/metrics, record the refresh, build, and publish.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LIB_NAME="${ADS_LIBRARY:-JIV}"
ALL_PATH="_data/papers_all.yml"
METRICS_PATH="_data/ads_metrics.yml"
CHANGELOG_PATH="CHANGELOG.md"
DELTA_YEAR="${ADS_DELTA_YEAR:-2026}"
TODAY="$(date +%F)"
COMMIT_MSG="${1:-"chore: refresh ADS metrics for ${DELTA_YEAR}"}"
CHANGELOG_LINE="- Publications dataset and metrics refreshed from ADS on ${TODAY} (\`${ALL_PATH}\`, \`${METRICS_PATH}\`)"

if [[ -z "${ADS_DEV_KEY:-}" ]]; then
  echo "ADS_DEV_KEY is not set; aborting."
  exit 1
fi

echo "Refreshing ADS library '${LIB_NAME}' with delta year ${DELTA_YEAR}..."
./scripts/update_ads_pubs.py "${LIB_NAME}" "${ALL_PATH}" --metrics "${METRICS_PATH}" --delta-year "${DELTA_YEAR}"

echo "Verifying metrics snapshot..."
python3 - "$METRICS_PATH" "$TODAY" "$DELTA_YEAR" <<'PY'
import sys
import yaml

path, expected_date, expected_year = sys.argv[1:4]
with open(path, "r", encoding="utf-8") as handle:
    payload = yaml.safe_load(handle) or {}

actual_date = str(payload.get("as_of", ""))
actual_year = str(payload.get("delta_year", ""))

if actual_date != expected_date:
    raise SystemExit(f"Expected as_of={expected_date}, found {actual_date}")
if actual_year != expected_year:
    raise SystemExit(f"Expected delta_year={expected_year}, found {actual_year}")
PY

if git diff --quiet -- "${ALL_PATH}" "${METRICS_PATH}"; then
  echo "No publication or metrics changes detected; nothing to commit."
  exit 0
fi

echo "Recording refresh in ${CHANGELOG_PATH}..."
python3 - "$CHANGELOG_PATH" "$CHANGELOG_LINE" <<'PY'
import sys

path, line = sys.argv[1:3]
with open(path, "r", encoding="utf-8") as handle:
    text = handle.read()

if line in text:
    raise SystemExit(0)

marker = "### Changed\n"
idx = text.find(marker)
if idx == -1:
    raise SystemExit("Could not find '### Changed' in CHANGELOG.md")

insert_at = idx + len(marker)
text = text[:insert_at] + line + "\n" + text[insert_at:]

with open(path, "w", encoding="utf-8") as handle:
    handle.write(text)
PY

echo "Building the site..."
bundle exec jekyll build

echo "Staging publication refresh..."
git add "${ALL_PATH}" "${METRICS_PATH}" "${CHANGELOG_PATH}"

if git diff --cached --quiet; then
  echo "Nothing staged after refresh; nothing to commit."
  exit 0
fi

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
echo "Committing to ${CURRENT_BRANCH}..."
git commit -m "${COMMIT_MSG}"

echo "Pushing ${CURRENT_BRANCH}..."
git push

echo "Done."
