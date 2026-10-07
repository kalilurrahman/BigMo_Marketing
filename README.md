# BigMo Marketing

Social campaign kits for BigMo products — ready-to-post Instagram and LinkedIn images, carousels, document PDFs and videos, plus captions and a posting plan for each.

| # | Product | Folder | Status |
|---|---|---|---|
| 1 | LakshyaPrep (`academy-kpm-spark`) | [`campaigns/lakshyaprep`](campaigns/lakshyaprep/CAMPAIGN.md) | ✅ ready |
| 2 | AI MarketPulse (`marketpulse-relay`) | [`campaigns/marketpulse`](campaigns/marketpulse/CAMPAIGN.md) | ✅ ready |
| 3 | DesiSquare (`desisquarev5-product`) | [`campaigns/desisquare`](campaigns/desisquare/CAMPAIGN.md) | ✅ ready |
| 4 | EOT-PCS (`eotpcs-…`) | [`campaigns/eotpcs`](campaigns/eotpcs/CAMPAIGN.md) | ✅ ready |
| 5 | Swaad — niche e-commerce (`niche-ecommerce-flow`) | [`campaigns/swaad`](campaigns/swaad/CAMPAIGN.md) | ✅ ready |
| 6 | KPMRentals (`kpm-rentals`) | [`campaigns/kpm-rentals`](campaigns/kpm-rentals/CAMPAIGN.md) | ✅ ready |
| 7 | Ledger Book (`LedgerBookPilot`) | [`campaigns/ledgerbook`](campaigns/ledgerbook/CAMPAIGN.md) | ✅ ready |
| ★ | **BigMo umbrella** — all seven, one rule | [`campaigns/bigmo`](campaigns/bigmo/CAMPAIGN.md) | ✅ ready |

## Other platforms
See [`PLATFORMS.md`](PLATFORMS.md) — X, Facebook, YouTube (incl. Shorts) and TikTok: file mapping, rendered banners/headers/thumbnails (`tools/platforms.py`) and per-product copy.

## How it works
`tools/socialkit.py` is a small Pillow + ffmpeg layout kit (browser/phone frames, brand type, eased push-in video with cross-fades). Each campaign's `build.py` holds that product's brand tokens, copy and screenshot picks, and writes to `campaigns/<app>/output/`.

```bash
pip install pillow   # ffmpeg must be on PATH
python3 campaigns/lakshyaprep/build.py --src ../academy-kpm-spark
```
Fonts (SIL OFL, `tools/fonts/`): Source Serif 4, Noto Serif Tamil, DM Serif Display, Fira Sans, Archivo. Inter is used from the system.
