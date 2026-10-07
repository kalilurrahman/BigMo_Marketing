#!/usr/bin/env bash
# Re-capture Ledger Book screens from a local demo build (no DATABASE_URL = seeded demo ledger).
#   cd ../LedgerBookPilot && npm install --no-package-lock && npm run dev -- --port 5199 &  PORT=8787 node server/server.mjs &
#   bash campaigns/ledgerbook/capture.sh
# Writes full-size PNGs to .cache/raw; build.py's crop step (or assets/screens/*.jpg) uses them.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
OUT="$HERE/.cache/raw"; mkdir -p "$OUT"
CH="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
APP="${APP:-http://127.0.0.1:5199}"
shot() { # name route width height
  "$CH" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size="$3,$4" --virtual-time-budget=15000 --user-data-dir="$(mktemp -d)" \
    --screenshot="$OUT/$1.png" "$APP/#/$2" >/dev/null 2>&1
}
shot d-today today 1440 1300
shot d-copilot copilot 1440 1300
for r in review reports close journal invoices; do shot "t-$r" "$r" 1440 3200; done
for r in today review copilot invoices; do shot "m-$r" "$r" 390 844; done
echo "captured → $OUT"
