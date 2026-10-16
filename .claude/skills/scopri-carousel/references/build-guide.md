# Build guide

How to turn approved copy into the finished carousel with the bundled engine. Read it when the copy is approved.

## Contents
1. Folder layout
2. Scaffold
3. Plan the slides before writing HTML
4. Components (class → design-system role)
5. The thread line
6. Prompt-card slides
7. Cover recipes
8. Export, QA and visual review
9. Revisions
10. Allowed deviations

---

## 1. Folder layout

```
<project>/
├── design-system.md, carousel-copy.md.pdf      ← the user's originals (skill copies in references/)
├── package.json, node_modules/                  ← shared deps (puppeteer-core, ffmpeg-static), installed once
├── assets/brand/logo/kit/                       ← Coperchio logo PNGs (source of truth)
├── assets/generated/                            ← rendered / generated images, reusable across carousels
└── carousels/<slug>/
    ├── index.html        ← slides + CAROUSEL config (the only file you normally edit)
    ├── engine/           ← carousel.css + carousel.js (copied from the skill; don't fork per carousel)
    ├── brand/            ← the three logo variants used by the frame
    ├── copy.md           ← approved copy (keep it in sync with the slides)
    ├── publish.json      ← caption, alt texts, pinned comments → npm run publish
    ├── exports/          ← slide-XX.png (+ .mp4), contact-sheet.jpg, strip-preview.jpg, cover-360.png
    └── pubblicazione/    ← the .txt files the user pastes into Instagram
```

## 2. Scaffold

From the project root:

```bash
node .claude/skills/scopri-carousel/scripts/new-carousel.mjs <slug> --title "Titolo" --format static
```

Use a short kebab-case Italian slug, e.g. `codex-7-modi`. The script copies the template, the engine and the logo kit. It installs `puppeteer-core` once at the project root, plus `ffmpeg-static` for animated carousels when ffmpeg isn't installed. It refuses to overwrite an existing carousel: revise that one in place instead.

The template's `index.html` is a **layout library** of 10 slides: T1, T2, T4, T9, T5 numbered point, T5 prompt card, T7, T6, T3, T10. Its sample copy only describes each layout. Keep the layouts you need, duplicate any you need more of, delete the rest, and replace all sample copy.

## 3. Plan the slides before writing HTML

Write this table into your notes first. It prevents most rework.

| # | Role | Mode | Template | Hero (type, position) | Thread in → out |
|---|---|---|---|---|---|

- **Modes** (design-system §11.1). The cover and the closing slide are DARK. Adjacent slides differ, with at most one same-mode pair and never 3 in a row. ACCENT slides are 1 to ⅓ of the total, never adjacent, and reserved for peaks. Reference sequences:
  - 5: `D L A L D`
  - 6: `D L D A L D`
  - 7: `D L D L A L D`
  - 8: `D L A L D L A D`
  - 9: `D A L D L D L A D` (the first carousel)
  - 10: `D L D A L D L A L D`
- **Templates** (§11.2). Never repeat a template back to back, except a T5 series, which must alternate modes. Zig-zag the hero position. Within any 3 slides, use at least two hero types. Follow a big hero with a calmer slide.
- **The closing slide is not counted.** With N slides the counter shows `/ N−1`. The engine handles this, but say so when you present the plan.
- **Accent budget:** at most 2 accent instances per slide. A typical pair is the accent phrase plus the thread line. When a slide already has accent elements, such as placeholders in a prompt card or redaction bars, use **recede split** for the headline instead. On ACCENT slides, the emphasis is an `ink-950` phrase (display sizes only) or a white highlight bar.

## 4. Components (class → design-system role)

| Class | Role / spec | Notes |
|---|---|---|
| `section.slide.mode-dark / mode-light / mode-accent` | 1080 × 1350 canvas, background mode | Always inside `<div class="slot">` |
| `.layer.bg` | background gradient | first child of every slide |
| `.layer.rings` / `.layer.dots` | atmosphere pattern (max 1) | rings: set `--rx/--ry`, or `data-follow` with a lens |
| `.supershape` | §8.9 circle; accent on D/L, ink on A | 1.2–2× canvas, 15–35% visible |
| `.ghost.num` / `.ghost.word` | ghost type, fill treatment | ≤ 1 per slide, about 30–50% of slides |
| `.glow[data-for="sel"]` | hero light (§6.5) | engine centres it; also lifts the DARK background |
| `.pill.qa-text` | eyebrow at (96,192) | 1–3 words, uppercased by CSS |
| `.stack` | text column at x 96, top 288 | children `.h1/.h2/.display`, then `.body/.lead` with a 40 px gap |
| `.display` 128 · `.h1` 96 · `.h2` 64 · `.h3` 42 | type scale §5.2 | set font-size inline within the ranges |
| `.lead` 35 · `.body` 29 | body text, ≥ 28 px | max width 508 (584 for 1–2 lines) |
| `.em` / `.rc` / `.bar` | accent phrase / recede / highlight bar | one emphasis per headline |
| `.card` (+ `.abs`) | dark UI card, every mode | padding 32, radius 28; `.ui` / `.ui-meta` = UI text (non-essential only) |
| `.sticker` | rotated pill on a card corner | max 1 per slide; give the card ≥ 48 px top padding |
| `.pcard` + `.ph` | prompt composer card + `[placeholder]` | see §6 |
| `.rows > .row > .idx/.t/.m` | T7 hairline rows, 96 px | starts around y 600 |
| `.numeral` (+ `.suf`) + `.chip` | T4 Numeral XXL + end-point chip | the chart line is the thread (custom route) |
| `.cmp > .card.muted / .card.win` | T6 comparison | `.win` gets the accent border and a `signal-500` check |
| `.glassobj > i(.sq)` | CSS frosted-glass object | fallback hero when no rendered asset fits |
| `.asset` | rendered or generated PNG | absolute; see `imagery.md` |
| `.lens[data-source][data-target]` | magnifier zoom of live HTML | §7 |
| `.logo-full[data-logo]`, `.cstack`, `.actions > .apill` | T10 closing slide | the engine fills the logo per mode |

- Mark every text element that must stay in the live area (x 96–984, y 192–1134) with `qa-text`.
- Add `data-lines="N"` to headlines whose line breaks matter: QA fails if they wrap differently.
- Use `<br>` for meaningful headline breaks. Never leave one short word alone on a line.
- Put slide-specific CSS in the `<style>` block of `index.html`. Don't edit `engine/` for one carousel. If something belongs in every carousel, change the skill's engine and say so.

## 5. The thread line

The thread line is configured in `window.CAROUSEL` in `index.html`:

- `seams[k]` is the y where the line crosses between slide k+1 and k+2.
- `routes[i]` is one of:
  - `'start'`: the cover; a node at `threadStart`, exits right;
  - `'straight'`;
  - `'rightUp'` / `'rightDown'`: a vertical run in the right margin at x 1032;
  - `'leftDown'` / `'leftUp'`: a vertical run in the left margin at x 48;
  - `'end'`: the closing slide; ends in a node 30 px left of `threadEnd`, by default `.apill`;
  - `'none'`;
  - `{ d, nodes }`: a custom SVG path. It must start at `x 0, y = seams[i−1]` and end at `x 1080, y = seams[i]`.

Patterns that worked:
- **y 1150 under the content.** It clears the footer zone, which starts at y 1174. The content must end by about y 1100, because QA keeps a 12–16 px buffer.
- **Prompt series:** `rightUp` 1150 → 360 on one slide, then `leftDown` 360 → 1150 on the next. The line wraps each card like a bracket and crosses the seam at y 360.
- **T4:** the line *is* the chart, rising to a node with the value chip.
- **Closing slide:** the line rises at x 200 and ends at the action pill.

QA checks that every seam's exit equals the next entry. It also samples the path and fails if it touches text, a card, an asset or a frame zone.

## 6. Prompt-card slides

The **T5 prompt series**: a pill (`Prompt 0N`), an H2 (1–2 lines, recede split), and a `.pcard`. Inside the card goes the intro `<p>`, then `<ol>` with `<span class="n">1.</span><span>…</span>` items, then `<p class="out">` for the output rules. Add a sticker `Allega: …` that names what to attach.

- 28 px text; the card bottom must be ≤ 1100 (QA reports each card's y range). A ~100-word prompt fits with a 2-line H2.
- Placeholders go in `<span class="ph">[…]</span>`. They are the slide's accent instance, so the H2 uses recede, or a highlight bar on ACCENT.
- Alternate `.pcard.alt` to flip the sticker's rotation. Alternate modes D/L/D/L/A. Use ghost numerals `0N`.
- These slides exceed the design system's 40-word and 35%-empty limits. That's accepted, because the user asked for full prompts.

## 7. Cover recipes

- **Contract or document + magnifier (first carousel):**
  - A `.card` document with a `.target` word inside its fine print.
  - A `.lens` with `data-source="#doc"`, `data-target=".target"` and `data-asset="#magnifier"`.
  - The rendered magnifier `<img class="asset" id="magnifier" data-lens-x="154.42" data-lens-y="154.42">`, using the values from `assets/generated/magnifier.json`.
  - Put the target low enough that the lens doesn't hide the card's title.
- **Glass object** (`.glassobj` or a rendered `.asset`) bottom-right, in the box x 500–1180 × y 600–1150, with the glow behind it.
- The display is ≤ 6 words, 3 lines, with one accent phrase. The lead goes bottom-left at y about 1020, width 356, 2 lines.
- After export, open `exports/cover-360.png`: the headline must still read at that size.

## 8. Export, QA and visual review

From the carousel folder:

```bash
npm run export
```

This runs the in-page QA, then writes `exports/slide-XX.png`.

QA checks:
- fonts loaded;
- images loaded;
- every canvas is 1080 × 1350;
- text inside the live area;
- no overflow;
- expected line counts;
- body text ≥ 28 px;
- objects outside the frame clear zones;
- prompt cards end by y 1100;
- the thread avoids text and lines up at the seams;
- (animated) text readable by 1.6 s.

**Fix every QA error. Never weaken a check to pass it.** The only exception is a check that is genuinely wrong for a new layout: fix the check in the skill's engine and say so.

Then:

```bash
npm run previews
```

This writes `contact-sheet.jpg`, `strip-preview.jpg` and `cover-360.png`. **Read the images yourself**: the contact sheet, the strip, the cover thumbnail, and each slide at full size wherever something might be off. Look for:

- widows and orphans, and one word alone on a line;
- stickers or chips colliding with text;
- a hero object touching text, or text over busy image detail;
- the lens or an object hiding something the reader needs;
- ghost numerals readable but quiet;
- the logo variant matching the mode; no corner logo, counter or cue on the closing slide; the counter reading `/ N−1`;
- the cover reading at 360 px;
- accent count ≤ 2 per slide; one emphasis per headline;
- the strip reading as one panorama, with no slivers at the seams;
- generated or rendered assets looking like one set, with clean edges and no halos.

Then send the user the contact sheet (and the cover). Lead with anything not yet done.

## 9. Revisions

- Change only what the user asked. Edit `index.html` in place, re-run `npm run export` and `npm run previews`, and show the changed slides.
- Keep `copy.md` and `publish.json` in sync with any copy change.
- If a change affects every future carousel (a brand or frame rule), update `brand-scopri-ai.md` and/or the engine as well, and tell the user it now applies to future carousels.

## 10. Allowed deviations

These need no further approval, but list them in your summary when they occur:

- Prompt slides over 40 words or under 35% empty, when the user asked for long prompts.
- A T5 series repeating the same template, with modes alternated.
- Ghost numerals on every slide of a numbered series, even if that's slightly over 50%.
- The swipe cue sitting on top of a super-shape (as in the design system's own worked example).
- The frame logo as the full lockup, and the CTA with one action pill (brand rules).

## 11. Real videos inside slides (Scopri AI news, added 16 Oct 2026)

News carousels show the real thing: official clips (from X via `https://api.fxtwitter.com/<account>/status/<id>`) or the author's original post. Put the file in `carousels/<slug>/media/` and place a box on the slide:

```html
<div class="video-box" data-video="media/robot.mp4" data-start="97" data-dur="4"
     style="left:96px;top:600px;width:888px;height:520px"></div>
```

| Attribute | Default | Meaning |
|---|---|---|
| `data-start` / `data-dur` | 0 / 8 | the piece to keep, in seconds |
| `data-fit` | `cover` | `contain` shows the whole frame with dark bands |
| `data-pos` | `.5` | horizontal crop, 0 = left, 1 = right |
| `data-tone` | `mono` | black and white with the brand-blue tint (Electric Mono's "monochrome imagery"); `color` keeps the colours |
| `border-radius` (style) | 56 px | `r-lg` panel radius; `0` for a full-bleed box |

Then, after `npm run export`: `npm run media` (trimmed clips) or `npm run media -- --full` (also `slide-XX-completo.mp4` with the whole source video, which the owner trims in Instagram). It writes a poster frame into the box, so `slide-XX.png` and the previews show the clip, and stacks: full slide → video → everything in front of it (the frame, and any text, pill, sticker or card that overlaps the box: these are kept in front automatically; add class `over-video` to force it). Output: 1080 × 1350, 30 fps, H.264, no audio.

Credit whoever made the clip in `fonti.md` and in "Fonti: …" at the end of the caption, never on the slide.
