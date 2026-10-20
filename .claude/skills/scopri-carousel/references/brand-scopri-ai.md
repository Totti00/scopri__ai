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
- **Handle:** `@scopri__ai` (two underscores). Since 20 Oct 2026 it is **not printed** on the slides (owner: "via per sempre"); it lives only in the Instagram profile.
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
- **Closing slide:** no corner logo (the big centred logo is already there, and the user flagged the repetition), no counter, no swipe cue.
- **No handle anywhere** (20 Oct 2026): the frame no longer prints `@scopri__ai` bottom-left. The footer keeps only the swipe cue on the right.
- **Swipe invite on the cover only, instead of the filled arrow** (owner, 20 Oct 2026): «SCORRI PER SCOPRIRE →» **centred, above Instagram's carousel dots**. Instagram mobile draws the carousel dots inside the image at ~y 1232/1350 (band ~1215–1250, checked on the owner's phone): the swipe line must sit above them, **caps centre ~y 1175** (`.f-swipe` top 1162 → caps y 1167–1184), with ~40 px between the words and the dots; the band 1205–1350 stays free. Inter Tight 600, 25 px, uppercase, letter-spacing .12em, white with a soft dark glow, then a thin brand-blue arrow (34 × 16 px, accent-300) **centred on the capitals' height** (measured: arrow centre = caps centre). **Optical centring:** the words alone sit on x 540 (the block is shifted 24 px right, half of arrow 34 px + gap 14 px), so they line up with Instagram's dots. Words only, **no dots**. The cover has **no filled arrow bottom-right**; every other content slide keeps its outlined arrow. **Cover line:** a short blue line (160 px, `CAROUSEL.swipeLine`) at the arrow's height (same centre y, 1175.5) that **touches the right edge** (x 920 → 1080, start node on its left end) and carries on into slide 2: the engine makes its y the first seam, and slide 2's `straight` thread eases back to its own exit y with a soft S-bend at x 760–880. The seam check stays on. The other slides keep their thread as before. The engine adds the invite to slide 1 (`.f-swipe`) and to the alternative covers; `CAROUSEL.swipe` changes the words, `false` removes it and brings the filled arrow back. Keep the cover's content (images, captions) above y ≈ 1120.
- **No rubric label on the cover** (20 Oct 2026): no pill ("News lampo", "Prompt"…) on slide 1, ever. The headline starts at y ≈ 216.
- **Eyebrow pills on content slides** are plain mono labels with a short accent dash: no rounded box, no coloured dot (the dot pills clashed with the new captions).
- **No stickers or labels laid over images or cards** (20 Oct 2026). The only text tied to an image is a comparison caption under it, **«Prima: …» / «Dopo: …»** (`.cap`, see §6).
- Everything else in the frame stays as the design system describes: positions, sizes. The cover's filled swipe cue is replaced by the «SCORRI PER SCOPRIRE →» invite (20 Oct 2026).

## 5. Closing slide (CTA)

Redesigned on 20 Oct 2026 (owner: "il pulsante MANDA non si capisce").

- Same mode as the cover (DARK by default), centred, layout T10. No handle, no counter, no corner logo.
- Big centred logo lockup (~112 px, top ≈ 236), then the hierarchy **headline → button → follow line**:
  1. H1 with the **one** main invite and one accent phrase (news: "Mandalo a chi …"; prompts and lists: "Salvalo per …").
  2. A **filled button** a 70-year-old reads as a button: brand-blue pill, 96 px tall, Inter Tight 38 px, icon + words. News/curiosità: paper plane + "Mandalo a un amico"; prompt/lista: bookmark + "Salvalo per dopo"; serie: bell + "Segui Scopri AI".
  3. A smaller **🔔 follow line** under it: the lid of the logo as a small bell (the plain lid, slanted as in the logo, about 44 × 25 px, in the mode's light accent blue, left of the text; **no vibration lines**: the owner removed them on 20 Oct 2026) + "Seguici per non perdere le prossime notizie" (prompt: "i prossimi prompt", curiosità: "le prossime curiosità", lista: "i prossimi consigli"). The engine writes it from `CAROUSEL.tipo`. Not in a *serie*, where following is already the main invite. On Instagram you "segui", never "iscriviti".
- No lead is needed; if one is used, keep it to one line between headline and button.
- The thread rises at x 120 (`threadEndX`) and ends in a node left of the button.

## 6. Imagery defaults

- **Primary family for AI and prompt topics: C (interface fragments).** These are dark UI cards, chat-composer cards, redacted documents and contract cards, built in HTML/CSS. They suit "how to use AI" content and need no image generation.
- **Secondary family: A (Glass & Chrome 3D)**, for 1–2 hero objects per carousel: the cover and/or a peak slide. Render them with the in-house three.js renderer (`assets/3d/`, see `imagery.md`). The user chose this after Replicate failed: "genera tu le immagini, lascio stare replicate". Use Replicate only when a valid token is configured and the subject really needs a generative model, such as Family B photographic cutouts.
- **Material look that worked:** polished chrome lit by a bright gradient studio dome, so it reads as silver, not black. Clear glass with a faint `#8595FF` tint. Accent details in electric-blue glass or blue "sand". Key light from the top-left.
- **Real photos and videos are always in full colour** (owner, 20 Oct 2026): `data-tone="color"` on every `video-box`, no black-and-white or blue duotone on real footage, posters and covers included. This overrides the "no full-color photography" rule of `design-system.md`.
- Prompt slides get **no** imagery. The prompt card is the hero, and anything else costs legibility.
- **Real photos and videos are in colour** (owner, 20 Oct 2026): `.img-box` with the original image, `.video-box` with `data-tone="color"`. The mono tone is no longer the default for news.
- **Captions: only comparison captions, «Prima: …» / «Dopo: …»** (owner, 20 Oct 2026). The word Prima or Dopo, a colon, then 1–3 words saying what changes («Prima: pubblicità», «Dopo: solo le app», «Prima: lentissima», «Dopo: meno della metà»). Nothing else under images (no "Vola.", "Rischio vero.", "Sembra una Apple TV."), no stickers, no labels over images, and no caption on an image that isn't part of a before/after. Each image of the comparison gets its own `<p class="cap" data-under="#img">Prima: …</p>`: Inter Tight 500 30 px with a 32 px accent dash, placed by the engine 28 px under the image, left-aligned; side-by-side captions line up at the same height. Leave room: image bottom ≤ ~1060.
- **Before/after on the cover**: the two screens overlap, "Prima" behind top-left, "Dopo" in front bottom-right (`.img-box.front`, outlined), slightly offset; "Prima" sits under the visible bottom-left edge of the back screen, "Dopo" under the front one.
- **Before/after pairs inside the carousel**: show the whole screenshots, at their original ratio (no crop), side by side.

## 7. Per-carousel dials (defaults)

| Dial | Default for Scopri AI |
|---|---|
| Cover / bookend mode | DARK |
| Primary imagery family | C (interface fragments); A for 1–2 heroes |
| Continuity device | Thread line (accent; white on ACCENT) |
| Human-touch accent | Off |
| Ghost type treatment | Fill |
| Super-shape form | Circle |
