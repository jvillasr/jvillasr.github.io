#!/usr/bin/env bash
# Convenience wrapper to pull latest ADS data, commit, and push in one go.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

LIB_NAME="${ADS_LIBRARY:-JIV}"
ALL_PATH="_data/papers_all.yml"
SDSS_PATH="_data/papers_sdssv.yml"
COMMIT_MSG="${1:-"Refresh ADS publications $(date +%Y-%m-%d)"}"

echo "Syncing ADS library '${LIB_NAME}'..."
./scripts/update_ads_pubs.py "${LIB_NAME}" "${ALL_PATH}" --sdss "${SDSS_PATH}"

echo "Staging ${ALL_PATH} and ${SDSS_PATH}..."
git add "${ALL_PATH}" "${SDSS_PATH}"

if git diff --cached --quiet; then
  echo "No changes detected; nothing to commit."
  exit 0
fi

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"
echo "Committing to ${CURRENT_BRANCH}..."
git commit -m "${COMMIT_MSG}"

echo "Pushing ${CURRENT_BRANCH}..."
git push

echo "Done."
