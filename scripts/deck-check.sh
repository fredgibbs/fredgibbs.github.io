#!/bin/zsh
# deck-check.sh <course>/<deck> [...]  — the typography and image pass.
#
#   LC_ALL=en_US.UTF-8 bundle exec jekyll build
#   scripts/deck-check.sh making-history/inventing-nations
#
# Serves the already-built _site, opens each deck in headless Chrome at
# 960x700 and runs scripts/deck-check.mjs over every slide. Build first: this
# checks what Jekyll produced, not index.md. Exits 1 if any deck has a FAIL.
# The rules are in courses/SLIDE-STYLE.md, "Before publishing".
set -e
here="$(cd "$(dirname "$0")" && pwd)"
site="$here/../_site"
[[ -d "$site" ]] || { echo "no _site: build first" >&2; exit 2; }
tmp="$(mktemp -d)"
PORT=8799; CDP=9229
(cd "$site" && python3 -m http.server $PORT >/dev/null 2>&1) & srv=$!
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --remote-debugging-port=$CDP \
  --user-data-dir="$tmp/profile" about:blank >/dev/null 2>&1 &
pid=$!
trap 'kill $pid $srv 2>/dev/null; rm -rf "$tmp"' EXIT
for i in {1..20}; do curl -s -m 1 -o /dev/null http://127.0.0.1:$CDP/json/version && break; sleep 0.5; done
rc=0
for d in "$@"; do
  course="${d%%/*}"; deck="${d#*/}"
  echo "== $course/slides/$deck"
  CDP_PORT=$CDP node "$here/deck-check.mjs" "http://127.0.0.1:$PORT/courses/$course/slides/$deck/" || rc=1
done
exit $rc
