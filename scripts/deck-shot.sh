#!/bin/zsh
# deck-shot.sh <out.jpg> <url> [height] [scroll-y]
#
# Captures a page for a conference-deck slide. Wraps scripts/deck-shot.mjs,
# which drives Chrome over the DevTools protocol so the LAYOUT VIEWPORT stays
# one normal screen (1400x900) while the screenshot extends below it.
#
# Why not just --window-size=1400,1900: these sites give their heroes
# `min-height: 100vh`, so a tall window makes the hero as tall as the capture
# and the rest of the page never appears. The viewport has to stay 900 tall for
# 100vh to mean one screen.
#
# Default 1400x1900 is the capitals poster's proportion (0.74), which is the
# shape that reads well in an .s-column. Do NOT capture the whole scroll
# height: these pages run 3-6 screens, so the full page lands at 0.25-0.49 and
# comes out 160-310px wide beside its text.
set -e
out="$1"; url="$2"; h="${3:-1900}"; y="${4:-0}"
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --remote-debugging-port=9222 \
  --user-data-dir="$tmp/profile" about:blank >/dev/null 2>&1 &
pid=$!
trap 'kill $pid 2>/dev/null; rm -rf "$tmp"' EXIT
for i in {1..20}; do curl -s -m 1 -o /dev/null http://127.0.0.1:9222/json/version && break; sleep 0.5; done
node "$here/deck-shot.mjs" "$tmp/page.png" "$url" "$h" "$y"
sips --resampleWidth 1200 "$tmp/page.png" --out "$tmp/small.png" >/dev/null
sips -s format jpeg -s formatOptions 88 "$tmp/small.png" --out "$out" >/dev/null
echo "wrote $out"
