# Video upgrade: narrated explainers with burned-in captions

Each campaign now has a 45–60 s explainer alongside its short reel. It comes in two shapes, with captions burned in and as separate subtitle files, plus a voiceover script.

| File (in `campaigns/<app>/output/video/`) | Spec | Use |
|---|---|---|
| `explainer-9x16.mp4` | 1080×1920, 46–54 s | Instagram Reels, TikTok, YouTube Shorts (all ≤ 60 s) |
| `explainer-1x1.mp4` | 1080×1080 | LinkedIn and Facebook feed (square takes the most feed space) |
| `explainer-cover-9x16.png` | 1080×1920 | Reel / Shorts cover |
| `explainer.srt`, `explainer.vtt` | subtitle files | Upload to LinkedIn, Facebook and YouTube so the platform captions work too (accessibility, muted autoplay) |
| `voiceover-script.md` | table of lines + in/out timecodes + delivery notes | Hand this to whoever records the voiceover |

| Product | Length | Delivery note |
|---|---|---|
| LakshyaPrep | 54 s | Warm, upbeat coach |
| AI MarketPulse | 46 s | Calm, precise; ends on the paper-trading / not-advice line |
| DesiSquare | 49 s | Friendly, peer-to-peer; ends on "Educational community. Not investment advice." |
| EOT-PCS | 49 s | Confident, operational, B2B |
| Swaad | 47 s | Warm, homely; Tamil names pronounced properly |
| KPMRentals | 47 s | Reassuring; slow on the 2 a.m. line |
| Ledger Book | 49 s | Clear, dry, quietly confident |
| BigMo (umbrella) | 46 s | Founder voice, measured |

## How it's built
`tools/longcut.py` holds one script per product. Each script is a list of *(slide, voiceover line)* pairs, and every line restates a fact already in that product's `CAMPAIGN.md` or `phase2.py`.
- Each scene shows one of the campaign's own slides over a blurred copy of itself, so every product keeps its look.
- The line is burned in as a subtitle: white on a dark box, placed above the bottom ~20% of the vertical frame so TikTok and Reels buttons don't cover it.
- Scene length follows the line (about 2.7 words/s plus a breath), so a voiceover read at a natural pace fits without re-editing.

```bash
python3 tools/longcut.py                 # all; or: python3 tools/longcut.py swaad ledgerbook
python3 tools/longcut.py --no-video      # just the .srt/.vtt/script (fast)
```
It needs each campaign's `output/` and its Phase 2 output first.

## Adding voice and music
1. Record each line of `voiceover-script.md` to its slot. A phone in a quiet room is fine for social; aim for −16 LUFS.
2. Lay the VO under `explainer-*.mp4` in any editor (CapCut, Premiere, DaVinci), or in-app on Instagram or TikTok.
3. Add a licensed music bed about 18 dB under the voice.
4. Keep the burned-in captions. Most feed video is watched muted.

**No AI voice clones of real people.** If you use a synthetic voice, use a stock voice and label it where the platform asks.
