# BigMo Marketing

Social campaign kits for BigMo products — ready-to-post Instagram and LinkedIn images, carousels, document PDFs and videos, plus captions and a posting plan for each.

| # | Product | Folder | Status |
|---|---|---|---|
| 1 | LakshyaPrep (`academy-kpm-spark`) | [`campaigns/lakshyaprep`](campaigns/lakshyaprep/CAMPAIGN.md) | ✅ ready |
| 2 | MarketPulse (`marketpulse-relay`) | `campaigns/marketpulse` | next |
| 3 | DesiSquare (`desisquarev5-product`) | `campaigns/desisquare` | planned |
| 4 | EOTPCS (`eotpcs-…`) | `campaigns/eotpcs` | planned |
| 5 | Niche e-commerce (`niche-ecommerce-flow`) | `campaigns/ecommerce` | planned |
| 6 | KPM Rentals (`kpm-rentals`) | `campaigns/kpm-rentals` | planned |
| 7 | LedgerBook (`LedgerBookPilot`) | `campaigns/ledgerbook` | planned |

## How it works
`tools/socialkit.py` is a small Pillow + ffmpeg layout kit (browser/phone frames, brand type, eased push-in video with cross-fades). Each campaign's `build.py` holds that product's brand tokens, copy and screenshot picks, and writes to `campaigns/<app>/output/`.

```bash
pip install pillow   # ffmpeg must be on PATH
python3 campaigns/lakshyaprep/build.py --src ../academy-kpm-spark
```
Fonts: Source Serif 4 (SIL OFL, `tools/fonts/`).
