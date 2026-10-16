# Scopri AI brand layer

This file adapts `design-system.md` (Electric Mono) to the Scopri AI brand. **Where they differ, this file wins.** Every rule here came from a decision or a correction made while building the first carousel. The reasons are kept next to each rule, so you can judge edge cases.

## Contents
1. Identity and voice
2. Colour
3. Logo ("Coperchio")
4. Frame overrides
5. Closing slide (CTA)
6. Imagery defaults
7. Per-carousel dials (defaults)

---

## 1. Identity and voice

- **Brand:** Scopri AI. An Italian Instagram account that teaches non-technical people how to use AI in everyday life: bills, contracts, work, study.
- **Handle:** `@scopri__ai` (two underscores). It is printed bottom-left on every slide.
- **Language:** slides, caption, alt text and pinned comments are written in **Italian** unless the user asks otherwise. Talk to the user in the language they write in, which has been Italian.
- **Voice:** "tu", direct, practical and friendly. Explain technical terms the first time (kWh, POD/PDR, scheda sintetica…). No corporate tone, no hype.
- **Honesty line:** carousels about using AI include one honest reminder that the AI can be wrong and the user must check, e.g. "L'AI spiega, ma può sbagliare: verifica sempre…". Put it in the caption, the CTA lead or both.

## 2. Colour

The accent ramp is swapped to the brand blue, as `design-system.md` §4.6 allows. The neutrals and the three background modes stay as they are.

| Token | Value | Check |
|---|---|---|
| `accent-100` | `#E0E4FF` | fills only |
| `accent-300` | `#8595FF` | 7.3:1 on ink-950 |
| `accent-500` | `#2340FF` (brand blue) | 6.5:1 with white |
| `accent-700` | `#0F26BD` | 10.3:1 with white |
| rgb helpers | `35,64,255` · `133,149,255` | for rgba() glows and shadows |
| accent gradient | `linear-gradient(120deg,#6F52FF 0%,#2340FF 50%,#1F8EFF 100%)` | numerals, glows, 3D tint only |
| ACCENT background | `radial-gradient(70% 50% at 10% 0%,rgba(255,255,255,.14) 0%,transparent 70%), linear-gradient(150deg,#4760FF 0%,#2340FF 45%,#1A32D1 100%)` | white body text 4.8:1 even on the light corner |

- `ink-950` on `accent-500` is only 3.1:1. Use it only at display sizes (≥ 88 px). It worked at 120 px for "per anni." on slide 2.
- **Yellow `#FFD84D`** is part of the brand (it appears in the logo kit's tint variant), but carousels don't use it. The design system allows one accent hue, and adding yellow would break the system. Only use it if the user explicitly asks, and then only as a small, deliberate exception.
- The brand near-black `#121212` is close enough to `ink-950` that no change is needed.

## 3. Logo ("Coperchio")

Since 16 Oct 2026 the logo is **"Coperchio"**: the wordmark "Scopri AI", with "AI" in blue and a pot lid lifting off it ("scoprire" = to take the lid off). It replaced an older speech-bubble logo, now archived in `assets/brand/logo/archivio/`. Don't use the old one. The first carousel (bollette-contratti) was built before the rebrand and still shows the bubble.

The logo comes as a **PNG kit**; the user declined SVG. The source of truth is the project folder `assets/brand/logo/kit/`. Copies live in this skill's `assets/brand/` for when the project folder is missing.

| File | Use on | Look |
|---|---|---|
| `scopri-ai-logo-negativo.png` | DARK slides | white "Scopri", light-blue AI and lid |
| `scopri-ai-logo-colore.png` | LIGHT slides | black "Scopri", blue AI and lid |
| `scopri-ai-logo-bianco.png` | ACCENT slides, photos | all white |
| `scopri-ai-logo-nero.png` | yellow / one-tint | all black (not used in carousels) |
| `scopri-ai-simbolo-*.png` | tight spaces | "AI" + lid only |

The lockups are 1538 × 600 (ratio 2.56). At the 40 px frame height a lockup is about 103 px wide, inside the design system's 120 px limit. The scaffold script copies the three lockups into each carousel's `brand/` folder. The engine then picks the right one per background mode automatically.

The logo keeps its brand colours (blue "AI" on light and dark). This overrides the design system's single-colour logo rule (§8.12): the user wants the real logo, not a recoloured version.

## 4. Frame overrides

These differ from `design-system.md` §3. Each one is the user's correction from the first carousel.

- **Top-left: the full logo lockup**, not the symbol alone, 40 px tall, in the mode's kit variant. The user said "hai messo la foto profilo nelle slide, non il logo. io voglio il logo (scopri AI)".
- **The progress counter counts content slides only.** With N slides the counter runs `01 / N−1` … `N−1 / N−1`. The closing slide has no counter. The user said the counter should not count the last slide, and the closing slide shouldn't show it.
- **Closing slide:** no corner logo (the big centred logo is already there, and the user flagged the repetition), no counter, no swipe cue. The handle stays.
- Everything else in the frame stays as the design system describes: positions, sizes, the swipe cue filled on the cover, the handle bottom-left.

## 5. Closing slide (CTA)

- Same mode as the cover (DARK by default), centred, layout T10.
- Big centred logo lockup, about **112 px** tall, in the mode's variant.
- H1 with one accent phrase, then a lead of at most 2 lines, then **one** action pill. Usually **SALVA** with a bookmark icon. T10 suggests 2–3 pills, but the copy guide asks for one CTA, and one pill matched the approved copy.
- The thread line ends in a node just left of the action pill.

## 6. Imagery defaults

- **Primary family for AI and prompt topics: C (interface fragments).** These are dark UI cards, chat-composer cards, redacted documents and contract cards, built in HTML/CSS. They suit "how to use AI" content and need no image generation.
- **Secondary family: A (Glass & Chrome 3D)**, for 1–2 hero objects per carousel: the cover and/or a peak slide. Render them with the in-house three.js renderer (`assets/3d/`, see `imagery.md`). The user chose this after Replicate failed: "genera tu le immagini, lascio stare replicate". Use Replicate only when a valid token is configured and the subject really needs a generative model, such as Family B photographic cutouts.
- **Material look that worked:** polished chrome lit by a bright gradient studio dome, so it reads as silver, not black. Clear glass with a faint `#8595FF` tint. Accent details in electric-blue glass or blue "sand". Key light from the top-left.
- Prompt slides get **no** imagery. The prompt card is the hero, and anything else costs legibility.

## 7. Per-carousel dials (defaults)

| Dial | Default for Scopri AI |
|---|---|
| Cover / bookend mode | DARK |
| Primary imagery family | C (interface fragments); A for 1–2 heroes |
| Continuity device | Thread line (accent; white on ACCENT) |
| Human-touch accent | Off |
| Ghost type treatment | Fill |
| Super-shape form | Circle |
