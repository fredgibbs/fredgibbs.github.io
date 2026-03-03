#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

JEKYLL_HOST="127.0.0.1"
JEKYLL_PORT="4000"
SITE_URL="http://${JEKYLL_HOST}:${JEKYLL_PORT}"
BUILD_DIR="${ROOT_DIR}/.tmp_a11y_site"

rm -rf "$BUILD_DIR"

bundle exec jekyll serve \
  --host "$JEKYLL_HOST" \
  --port "$JEKYLL_PORT" \
  --destination "$BUILD_DIR" \
  --quiet &
JEKYLL_PID=$!

cleanup() {
  kill "$JEKYLL_PID" >/dev/null 2>&1 || true
  rm -rf "$BUILD_DIR"
}
trap cleanup EXIT INT TERM

for _ in {1..60}; do
  if curl -sSf "$SITE_URL" >/dev/null 2>&1; then
    break
  fi
  sleep 1
done

if ! curl -sSf "$SITE_URL" >/dev/null 2>&1; then
  echo "Jekyll did not start at $SITE_URL in time."
  exit 1
fi

echo "Running pa11y-ci..."
npx --yes pa11y-ci@4.1.0 --config .pa11yci.json

echo "Running Lighthouse CI..."
npx --yes @lhci/cli@0.14.0 autorun --config=./lighthouserc.json

echo "Accessibility checks complete."
