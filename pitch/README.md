# YojanaConnect — Technical Pitch Deck

Materials for impressing enterprise / Tamil Nadu reviewers with a live product story.

## Live product

https://yojnaconnect.prakharkr.online/schemes

## Files

| File | Use |
|------|-----|
| `YojnaConnect-TechPitch.html` | **Primary dynamic deck** — open in Chrome, fullscreen (F11), arrow keys |
| `YojnaConnect-TechPitch.pptx` | PowerPoint / Google Slides export for offline meetings |
| `assets/*.png` | Live product screenshots embedded in both decks |
| `generate_pptx.py` | Regenerates the `.pptx` if you update copy/screenshots |

## Present like a pro (HTML deck)

1. Open `YojnaConnect-TechPitch.html` in Chrome (keep the `assets/` folder beside it).
2. Press **F** for fullscreen (Reveal.js) or OS fullscreen.
3. Use **→** / space for next slide; fragments animate step-by-step.
4. Keep the live site open on a second window/monitor for demo after slide 4–5.
5. Do **not** claim JWT/ML as live — the deck frames them as roadmap.

## Suggested 8-minute flow

1. Title + live URL (30s)
2. Problem → solution (90s)
3. Live metrics + screenshots (90s) → switch to live site demo (2 min)
4. Architecture + API + data model (2 min)
5. Security + scale + TN pilot ask (90s)

## Regenerate PPTX

```bash
python3 pitch/generate_pptx.py
```
