# Electric Mono — Instagram Carousel Design System

> Copy of the project's `design-system.md` (16 Oct 2026). Scopri AI overrides, such as the brand-blue accent, the full-logo frame and the counter rules, are in `brand-scopri-ai.md` and win. If the project root has a newer `design-system.md`, read that one.
>
> **Contents:** 0. How to use this document · 1. Style DNA (the feel in nine lines) · 2. Canvas, grid and safe zones · 3. The frame (persistent on every slide) · 4. Color system · 5. Typography · 6. Spacing, radius, borders, shadows, effects · 7. Imagery · 8. Graphic elements and motifs · 9. Composition principles · 10. Layout templates · 11. Carousel architecture (consistency between slides) · 12. Consistency contract · 13. Do / Don't · 14. QA checklist · 15. Design tokens · 16. Worked blueprint (abstract example, 7 slides, all defaults)


> **Monochrome canvas, one electric signal.**
> A premium, tech-editorial carousel style. Cool neutrals and deep near-black carry the composition. A single saturated electric-blue accent marks what matters. Each slide has one isolated hero (an oversized headline, a giant numeral, or a single sculptural object), with generous empty space, soft light and fine grain. Slides alternate between dark, light and accent backgrounds. They read as one continuous strip because a fixed frame, a shared text axis and elements that cross the slide seams tie them together.

---

## 0. How to use this document

This file is the only source of truth. Someone following it can build new carousels in this style without seeing any reference material.

**Rule priority (when rules conflict, the higher one wins):**
1. **Legibility and contrast** (section 4.4, section 5.5)
2. **Consistency contract** (section 12): constants are never broken
3. **Carousel-level locks** (section 12.2): once chosen, they apply to every slide
4. **Layout templates** (section 10)
5. **Stylistic suggestions** (everything marked *optional*)

**Zero-input default.** If you are given no other direction, use the default for every dial: Dark cover, Glass & Chrome imagery, Thread-line continuity, Human-touch off, electric-blue accent. That always produces the same canonical look.

**Units.** All measurements are in px on a **1080 × 1350** canvas unless stated otherwise. "em" values are relative to the font size of the element.

---

## 1. Style DNA (the feel in nine lines)

1. **Restraint plus one signal.** Nearly everything is neutral (near-black, white, cool grays). One electric accent hue marks key words, numbers, lines and glows. It is never decorative noise.
2. **One hero per slide.** Each slide has exactly one dominant element: an oversized headline, a giant ultra-thin numeral, or one isolated object. Everything else is clearly secondary.
3. **Extreme scale contrast.** Huge type and objects sit next to small, quiet body text and tiny meta text. The gap between levels is dramatic, not gradual.
4. **Air.** At least 35% of every slide is empty. Emptiness is a design element.
5. **Sculptural, desaturated imagery.** Imagery is glass and chrome 3D objects, grayscale cutouts or dark interface cards. All of it is monochrome or tinted with the accent. There are no full-color photos. *(Scopri AI override, 20 Oct 2026: real photos and videos are always shown in full colour — see `brand-scopri-ai.md`.)*
6. **Atmosphere, never flat.** Every background has a subtle tonal gradient, ambient light, an accent glow behind the hero, and fine film grain.
7. **Alternating rhythm.** Dark, light and accent slides alternate, so the carousel pulses as you swipe.
8. **A fixed frame.** Logo, progress counter, handle and swipe cue sit in exactly the same place on every slide.
9. **Continuity across seams.** A line, shape or object flows from one slide into the next, so the carousel reads as one long panorama.

---

## 2. Canvas, grid and safe zones

### 2.1 Canvas
| Property | Value |
|---|---|
| Size | **1080 × 1350 px** (4:5 portrait), the same for every slide |
| Export | PNG (or JPG at quality 92+), sRGB |
| Slide count | 5–10 recommended (minimum 3, maximum 20) |

### 2.2 Margins and grid
| Property | Value |
|---|---|
| Outer margin | **96 px** on all four sides |
| Live width | 888 px (x = 96 → 984) |
| Columns | **12 columns × 52 px**, **24 px gutters** |
| Column span width | `76n − 24` px → 4 cols = 280, 6 = 432, 7 = 508, 8 = 584, 10 = 736, 12 = 888 |
| Baseline unit | 8 px (every vertical position snaps to multiples of 8) |

Column x-starts: col1 = 96, col2 = 172, col3 = 248, col4 = 324, col5 = 400, col6 = 476, col7 = 552, col8 = 628, col9 = 704, col10 = 780, col11 = 856, col12 = 932.

### 2.3 Vertical zones
| Zone | y-range | Content |
|---|---|---|
| Header row | 96 → 136 | Frame: logo (left), progress counter (right) |
| Content zone | **192 → 1134** | Everything else |
| Footer row | 1198 → 1254 | Frame: handle (left), swipe cue (right) |

**Fixed anchors (shared by every text-top layout):**
- Eyebrow pill top edge: **y = 192**
- Headline box top edge: **y = 288**
- Text axis: **x = 96**. Pills, headlines and body text always start here, so text never jumps sideways between slides.

### 2.4 Profile-grid safe zone
The Instagram profile grid shows a narrower, roughly 3:4 crop of 4:5 posts, cutting into the left and right edges. The 96 px side margins clear that crop with room to spare. **Keep everything critical on the cover inside the margins.** Only bleeding objects and atmosphere may reach the edges.

---

## 3. The frame (persistent on every slide)

The frame is the strongest consistency anchor. Its position, size and style **never change**. Only its color adapts to the background mode (section 4.3).

```
┌──────────────────────────────────────────────┐
│ [LOGO MARK]                        02 / 07   │  ← header row, y 96–136
│                                              │
│ ( • EYEBROW PILL )                           │  ← y 192 (content, not frame)
│                                              │
│ Headline starts here at y 288                │
│ ...                                          │
│                                              │
│                                              │
│ @handle                                (→)   │  ← footer row, y 1198–1254
└──────────────────────────────────────────────┘
```

| Element | Position | Spec |
|---|---|---|
| **Logo mark** | Top-left, x = 96, y = 96 | Symbol only (no wordmark), **height 40 px**, width ≤ 120 px. Single color: text-primary of the mode. |
| **Progress counter** | Top-right, right edge x = 984, vertically centered on y = 116 | JetBrains Mono 500, 20 px, tracking +0.08em. Format `02 / 07`, zero-padded. The current number is text-primary, ` / 07` is text-meta. |
| **Handle** | Bottom-left, x = 96, baseline y = 1240 | JetBrains Mono 500, 20 px, tracking +0.04em, color text-meta. Write the handle as-is (e.g. `@yourbrand`). |
| **Swipe cue** | Bottom-right, circle 56 × 56 px, right edge x = 984, center y = 1226 | 2 px ring in text-primary at 30% opacity, with a 24 px right-arrow (2 px stroke, round caps) in text-primary. On the **cover** it is filled: solid `accent-500` with a white arrow on a DARK cover, or solid `white` with an `accent-700` arrow on an ACCENT cover. **Omitted on the last slide.** |

**Frame rules**
- Never move, resize, restyle or remove a frame element. The only exception is that the swipe cue disappears on the final slide.
- Keep at least 24 px of clear space around every frame element. Objects, lines and ghost type may bleed off the canvas edges, but they must stay out of these clear-space zones. Atmosphere (gradient, glow, rings, grain) is the only thing allowed behind frame elements.
- The frame sits on the top layer, above everything else.
- Do not add other persistent elements (no borders around the slide, no page frame, no corner ornaments).

---

## 4. Color system

### 4.1 Core palette
| Token | Hex | Role |
|---|---|---|
| `ink-950` | `#0A0A0D` | Dark background base; primary text on light |
| `ink-900` | `#121218` | Card and surface fill (all modes) |
| `ink-850` | `#17171F` | Card gradient top, raised surface |
| `ink-700` | `#2A2A33` | Dividers inside cards |
| `gray-600` | `#5E5E6A` | Body and meta text on light |
| `gray-500` | `#6E6E7A` | "Recede" words in large headlines on dark |
| `gray-450` | `#7E7E8A` | "Recede" words in large headlines on light |
| `gray-400` | `#8B8B97` | Meta text on dark |
| `gray-300` | `#A1A1AC` | Body text on dark |
| `paper-50` | `#F7F7FA` | Light background highlight |
| `paper-100` | `#F2F2F5` | Light background base |
| `paper-200` | `#E4E5EB` | Light background shadow side |
| `white` | `#FFFFFF` | Primary text on accent; highlight bars on accent |
| `snow` | `#F5F5F7` | Primary text on dark (softer than pure white) |
| **`accent-500`** | **`#4353FF`** | **Electric blue: the signal.** Accent background, accent words on light, lines, fills |
| `accent-300` | `#8F98FF` | Accent words and numbers **on dark** (lighter for luminance) |
| `accent-700` | `#2530C9` | Deep accent: gradient ends, accent text on white bars |
| `accent-100` | `#E3E6FF` | Soft tint for subtle fills on light (never text) |
| `signal-500` | `#3DDC84` | **Functional only.** Success checks, "live" dots, positive deltas inside UI cards. Never in headlines or decoration. Maximum one instance per slide. |

### 4.2 Accent gradient (restricted use)
```
accent-gradient: linear-gradient(120deg, #7A6BFF 0%, #4353FF 50%, #3B9BFF 100%)
```
Use it **only** for: hero numerals, glows, the thread line (optional), and the tint inside 3D glass objects. Never use it on headlines, body text, backgrounds or buttons.

### 4.3 Background modes
Every slide uses exactly one of three modes. **No flat fills: every mode has a gradient, light and grain.**

| | **DARK** (`D`) | **LIGHT** (`L`) | **ACCENT** (`A`) |
|---|---|---|---|
| Base | `#0A0A0D` | `#F2F2F5` | `#4353FF` |
| Gradient | Radial lift `#1A1C2E` → transparent (ellipse 80% × 60%, centered on the hero) plus edge vignette `rgba(0,0,0,.45)` | `linear-gradient(160deg, #F7F7FA 0%, #ECEDF1 55%, #E4E5EB 100%)` plus a white radial highlight at the top-left, 90% → 0 | `linear-gradient(150deg, #5D6BFF 0%, #4353FF 45%, #2B36D6 100%)` plus a white radial highlight at the top-left, 14% → 0 |
| Hero glow | Yes, accent (section 6.5) | No colored glow. Soft contact shadow under objects; optional `accent-100` haze at 40% | Yes, white/periwinkle (section 6.5) |
| Grain | 7%, overlay | 5%, multiply | 8%, overlay |
| Text-primary | `snow #F5F5F7` | `ink-950 #0A0A0D` | `white #FFFFFF` |
| Body text | `gray-300 #A1A1AC` | `gray-600 #5E5E6A` | `white` (hierarchy by size only) |
| Meta (frame) | `gray-400 #8B8B97` | `gray-600 #5E5E6A` | `white` at 100% |
| Accent words | `accent-300 #8F98FF` | `accent-500 #4353FF` | `ink-950` (display sizes only) **or** a white highlight bar with `accent-700` text |
| Recede words | `gray-500 #6E6E7A` | `gray-450 #7E7E8A` | not used |
| Hairlines | `rgba(255,255,255,.12)` | `rgba(10,10,13,.12)` | `rgba(255,255,255,.24)` |

### 4.4 Verified contrast pairs (WCAG ratios)
| Text / background | Ratio | Allowed for |
|---|---|---|
| `snow` on `ink-950` | ~19:1 | everything |
| `gray-300` on `ink-950` | ~7.7:1 | body |
| `gray-400` on `ink-950` | ~5.9:1 | meta, body |
| `accent-300` on `ink-950` | ~7.6:1 | everything |
| `gray-500` on `ink-950` | ~3.9:1 | **large text only (≥ 56 px)** |
| `ink-950` on `paper-100` | ~18:1 | everything |
| `gray-600` on `paper-100` | ~5.7:1 | body, meta |
| `accent-500` on `paper-100` | ~4.8:1 | headlines and large text; avoid for body under 28 px |
| `gray-450` on `paper-100` | ~3.6:1 | **large text only (≥ 56 px)** |
| `white` on `accent-500` | ~5.4:1 | everything (keep body text on the deeper half of the gradient) |
| `ink-950` on `accent-500` | ~3.7:1 | **display sizes only (≥ 88 px)** |
| `accent-700` on `white` | ~9:1 | highlight bars |

### 4.5 Color usage rules
- **One hue.** The accent family (500/300/700/100 and the gradient) is the only chromatic color. The single exception is `signal-500`, inside UI elements only.
- **Accent budget per slide:** about 5–10% of the slide area on D and L slides for words, lines, chips and small fills. Glow, 3D tint and the super-shape don't count toward it. On A slides the accent is the field and white does the signaling.
- **Emphasis count:** at most **2 accent emphasis instances per slide** (for example, one accent phrase plus one accent line or chart).
- **Never** combine accent words and a highlight bar in the same headline.
- **Accent-on-accent inversion (blanket rule for ACCENT slides).** Anything in this document specified as `accent-500`, `accent-300` or the accent gradient becomes **`white`** on an ACCENT slide. This covers lines, the thread line, chart lines, highlighted dots, progress arcs, index numbers, icons, card borders, nodes and seam lines. Large solid accent fills (the super-shape, big shapes) become **`ink-950`**. Hero numerals become solid `white`, with their suffix in `ink-950`. The accent gradient is **never** used on ACCENT slides. Accent underglows on cards become the ACCENT card shadow (section 6.4). Pill and highlight-bar variants already have their own ACCENT specs.

### 4.6 Swapping the accent hue (brand adaptation)
The system works with any single saturated hue (magenta, cyan, orange and so on). To swap it, replace the whole accent ramp and keep every role:
- `accent-500`: a saturated mid-tone with **≥ 4.5:1 against white** (white text sits on it).
- `accent-300`: a lighter version with **≥ 4.5:1 on `ink-950`**.
- `accent-700`: a deep version with **≥ 7:1 against white**.
- `accent-100`: a pale tint for fills.
- Accent gradient: a ±25° hue shift around `accent-500`.
- Keep the neutrals unchanged, but you may shift their temperature slightly toward the new hue (±3% saturation).

Only one accent hue per brand. Never mix ramps.

---

## 5. Typography

### 5.1 Families (all free on Google Fonts)
| Role | Family | Fallback stack |
|---|---|---|
| **Primary** (everything) | **Inter Tight** (weights 200, 400, 500, 600, 800) | `"Inter", "Helvetica Neue", Arial, sans-serif` |
| **Meta** | **JetBrains Mono** (500) | `"IBM Plex Mono", ui-monospace, monospace` |
| **Human-touch serif** (optional, see section 8.10) | **Instrument Serif** *Italic* (400) | `"Playfair Display" italic, Georgia, serif` |

Premium drop-in replacements for Inter Tight, if licensed: Neue Montreal, Aeonik, Satoshi or General Sans. Use one family only.

Each slide uses at most **two families** (primary plus meta). The serif appears only if the Human-touch dial selects it.

### 5.2 Type scale
| Role | Size (px) | Weight | Line-height | Tracking | Case | Default color |
|---|---|---|---|---|---|---|
| **Numeral XXL** (hero numbers) | 320–420 | **200** | 0.85 | −0.06em | n/a | accent-gradient fill **or** text-primary with the suffix (`+ % x B M K`) in accent |
| **Display** (cover headline) | 120–136 | **600** | 0.95 | −0.045em | Sentence case | text-primary |
| **H1** (slide headline) | 88–104 | **600** | 1.00 | −0.035em | Sentence case | text-primary |
| **H2** (secondary headline / numeral label) | 56–64 | **600** | 1.05 | −0.025em | Sentence case | text-primary |
| **H3** (list rows, card titles) | 40–44 | **500** | 1.15 | −0.015em | Sentence case | text-primary |
| **Lead** (sub-line under display) | 34–36 | **400** | 1.30 | −0.01em | Sentence case | body color |
| **Body** | 28–30 | **400** | 1.40 | −0.005em | Sentence case | body color |
| **UI text** (inside cards) | 20–26 | **500** | 1.30 | 0 | Sentence case | `snow` / `gray-300` |
| **Meta** (pill, progress, handle, index numbers) | 20 | **500** (Mono) | 1.00 | +0.08em | UPPERCASE (handle as written) | meta color |
| **Ghost type** (background words/numerals) | 400–1000 | **800** for words / **200** for numerals | 0.80 | −0.05em | UPPERCASE for words | see section 5.6 |

### 5.3 Typographic rules
- **Weight system is fixed.** Headlines are 600, hero numerals 200, body 400, meta Mono 500. Do not change weights within a headline for emphasis; emphasis is done with color (section 5.4). The contrast between ultra-thin giant numerals and solid headlines is a signature of this style.
- **Sentence case** for all headlines and body text. UPPERCASE only for meta, pills and ghost words.
- **Left-aligned, ragged-right**, starting on the x = 96 axis. The **only** centered slide is the final CTA slide (template T10).
- **Tight display setting.** Negative tracking scales with size (see the table). Never use positive tracking on headlines.
- **Headline length:** Display ≤ 3 lines (about 13 characters per line at 128 px). H1 ≤ 4 lines (about 18 characters per line at 96 px). Break lines by meaning, never leaving a single short word alone on a line.
- **Body length:** ≤ 3 short paragraphs, ≤ 40 words per slide, max width **508 px** (7 columns). A body block of one or two lines may stretch to 584 px.
- **Maximum 3 text sizes per slide**, not counting meta and UI text.
- Use hanging punctuation for opening quotes and similar marks in display sizes (shift them left so the letters align to x = 96).
- No text shadows, outlines on headlines, or gradient fills on words (gradients are for numerals only).
- No justified text, no hyphenation, no all-caps sentences.

### 5.4 Headline emphasis (two-tone headlines)
Every headline is two-tone. Choose one method per headline:

| Method | How | When |
|---|---|---|
| **Accent phrase** (default) | 1–4 contiguous words in the accent color for the mode. ≤ 40% of the headline. | Most slides |
| **Recede split** | The key phrase stays text-primary; the less important part drops to the recede gray. | Statements, manifesto slides, adding variety |
| **Highlight bar** | A solid bar behind 1–4 words (section 8.3). | Max **1 per slide**, about 1 in 3 slides at most |

A headline uses **at most two colors**. Use exactly one emphasized phrase per headline.

### 5.5 Minimum sizes (phone legibility)
A 1080 px slide shows at about 390 pt on a phone, so 1 pt is roughly 2.8 px.
- Body text: **≥ 28 px**. Never smaller.
- Meta and UI text: **≥ 20 px**, and only for non-essential or decorative information.
- Essential information is **never** placed in UI text or meta text alone.
- Cover headline: **≥ 120 px** so it stays legible in the profile-grid thumbnail.

### 5.6 Ghost typography
Oversized background type: a word, or more often a numeral, that sits behind the content as texture and depth.
- Size 400–1000 px. **Always cropped** by at least one canvas edge (15–40% of it off-canvas).
- Treatment (choose one per carousel and keep it): **Fill** at low opacity (dark mode white 6%, light mode ink 5%, accent mode white 12%) **or** **Outline** with a 2 px stroke (text-primary at 18%).
- Words: Inter Tight 800, UPPERCASE. Numerals: Inter Tight 200.
- It always sits behind the hero object and headline, and never competes with readable text (≤ 12% opacity, or outline).
- Maximum one ghost element per slide, on about 30–50% of slides.

---

## 6. Spacing, radius, borders, shadows, effects

### 6.1 Spacing scale (px)
`8 · 16 · 24 · 32 · 40 · 48 · 64 · 96 · 128 · 160`

| Relationship | Gap |
|---|---|
| Header row → content zone | 56 (fixed: content starts at y 192) |
| Pill → headline | 48 (pill 192–240, headline top 288) |
| Headline → lead/body | 40 |
| Body paragraph → paragraph | 24 |
| Text block → hero object (when stacked) | ≥ 64 |
| Content zone → footer row | ≥ 64 |
| Card inner padding | 32 |
| List row height | 96 (H3 centered, hairline between rows) |

### 6.2 Corner radius scale
| Token | px | Use |
|---|---|---|
| `r-xs` | 6 | Highlight bars, tiny chips |
| `r-sm` | 16 | Inputs, small UI elements inside cards |
| `r-md` | **28** | **UI cards** (standard) |
| `r-lg` | **56** | Large panels, image masks, framed photos |
| `r-pill` | 999 | Pills, buttons, toggles |

There are no sharp 90° corners on containers. The only sharp edges are the canvas edges and cropped bleeding objects.

### 6.3 Borders and lines
- Hairline weight: **2 px** (1 px disappears after Instagram compression).
- Card border: 2 px inner, `rgba(255,255,255,.08)`, plus a 1 px top highlight `rgba(255,255,255,.12)`.
- Dividers: 2 px, hairline color of the mode.
- Decorative and connector lines: 2–3 px, round caps, accent or hairline color.
- No borders around images, slides or headlines.

### 6.4 Shadows (objects and cards only; never text)
| Context | Recipe |
|---|---|
| Card or object on **LIGHT** | `0 48px 96px -24px rgba(10,10,20,.40), 0 12px 32px -8px rgba(10,10,20,.18)` |
| Cutout object on **LIGHT** | Contact shadow: an ellipse 70% of the object width × 40 px, `rgba(10,10,13,.28)`, blur 40 px, placed under the object |
| Card on **DARK** | No drop shadow (it would be invisible). Use the 2 px border, the top highlight and an accent underglow: `0 40px 120px -20px rgba(67,83,255,.35)` |
| Card on **ACCENT** | `0 40px 100px -24px rgba(16,20,90,.55)` |

### 6.5 Glow (the hero's light source)
On DARK and ACCENT slides, the hero object or hero numeral sits in light:
- **Outer glow:** radial, diameter **800–1000 px**, centered behind the hero. DARK: `accent-500` at 40% → 0 at 60% of the radius. ACCENT: `#FFFFFF` at 18% → 0.
- **Core glow:** radial, diameter **280–360 px**. DARK: `accent-300` at 45% → 0. ACCENT: `#FFFFFF` at 30% → 0.
- One glow per slide. It always comes from the hero, never from empty space.
- Optional **concentric rings** around the glow (section 8.7).

### 6.6 Grain (always on)
A full-canvas monochrome noise overlay on every slide (see section 4.3 for opacity per mode). It gives a tactile, printed quality and unifies the 3D, photo and UI elements.

```html
<filter id="grain">
  <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" stitchTiles="stitch"/>
  <feColorMatrix type="saturate" values="0"/>
</filter>
<rect width="1080" height="1350" filter="url(#grain)" opacity="0.07" style="mix-blend-mode:overlay"/>
```

---

## 7. Imagery

### 7.1 Universal image rules
- **No full-color photography** *(not for Scopri AI: real photos and videos stay in full colour, owner decision 20 Oct 2026)*. All imagery is **grayscale**, **accent-duotone**, or **neutral plus accent** (3D renders). The accent is the only chroma allowed.
- **Isolated subjects.** Objects are cut out or rendered on nothing, and float in space. No busy scenes.
- **One hero image per slide**, at most two small supporting elements.
- **Symbolic, slightly surreal subjects** work best: abstract forms (spheres, rings, ribbons, cubes, arrows, waves), hands (human or robotic), classical busts, vintage or modern hardware, everyday objects reimagined in glass or chrome. Avoid literal stock clichés (handshakes, people pointing at screens).
- Lighting comes **from the top-left** in every image, so it matches the background highlights.
- Scale: the hero object occupies **35–60% of the canvas height** and often bleeds off one edge.

### 7.2 Imagery families (choose ONE primary family per carousel; see section 12.2)

#### Family A — Glass & Chrome 3D *(default)*
- Single sculptural object made of **frosted or clear glass with an accent-blue internal tint**, sometimes with **polished chrome** parts.
- Studio product-render look: soft rim light from the top-left, subtle caustics, gentle reflections, very smooth surfaces.
- Rendered on transparent, pure black, pure `#4353FF` or `#F2F2F5`, matching the slide mode.
- On DARK: a strong accent glow behind it. On LIGHT: contact shadow plus a pale accent haze. On ACCENT: white glow, and the object reads in lighter blues and whites.

**Prompt template:**
```
A single [OBJECT] made of frosted translucent glass with an electric blue (#4353FF) internal
tint and polished chrome details, floating in empty space, high-end 3D product render, soft
rim light from top-left, subtle caustics, smooth surfaces, minimalist, centered with generous
negative space, isolated on a solid [pure black | #4353FF blue | light gray #F2F2F5]
background, no text, no logos
Negative: multicolor, rainbow, warm tones, text, watermark, clutter, busy background, cartoon,
low-poly, plastic toy look
```

#### Family B — Monochrome cutouts
- **High-contrast black-and-white photographic cutouts** (busts, hands, animals, objects, hardware) with clean edges (1 px feather, no halo, no outline stroke).
- **Accent pop:** exactly **one element** in the image is recolored to solid `accent-500` (one object in a group, one part of a figure, one prop). On ACCENT slides the pop is `ink-950` instead.
- Optional **halftone** on the cutout (section 8.8) for a printed, collage feel. Lock it on or off for the whole carousel.
- Cutouts may overlap panels or cards and break out of their containers. A head or hand rising out of a rounded panel is a typical move.

**Prompt template:**
```
High-contrast black and white studio photograph of [SUBJECT], isolated on a plain white
background, crisp clean edges, dramatic soft side light from top-left, fine film grain,
editorial, minimal, no text
```
Post-process: remove the background, desaturate 100%, contrast +20, apply a slight S-curve, then recolor one element to `#4353FF`.

#### Family C — Interface fragments
- **Abstracted, dark UI cards** (section 8.2) floating on any background mode: notifications, input fields, toggles, buttons, small charts, status chips, flow nodes.
- Content is generic and minimal (placeholder labels, short numbers, neutral circles instead of real logos or flags).
- Arranged as a **stack or cluster**: 1 primary card plus 1–2 secondary cards, offset by 48–96 px and overlapping, with depth from shadow or glow.
- Can also include a **device frame** (laptop or phone outline in `ink-900` with a 2 px hairline), always shown with a dark UI.
- Built fully in code, so this is the **fallback** when image generation is not available.

### 7.3 Atmospheric full-bleed images (optional, at most 2 per carousel)
Full-bleed images (architecture, sky, abstract landscapes, close-up textures) are allowed when **duotoned**:
- On ACCENT: shadows `#2530C9` → highlights `#FFFFFF`.
- On DARK: shadows `#0A0A0D` → highlights `#8F98FF`.
- Text sits on the calmest area, with a 30–50% gradient scrim (mode base color → transparent) behind the text block.
- Grain stays on top.

### 7.4 Masks and framing
- A non-cutout photo is masked into a **rounded panel (`r-lg` 56)** or a **circle**, never a sharp rectangle.
- Objects may **bleed** off the canvas edge (encouraged: 10–30% off-canvas), but never off the top edge on slides where the pill and headline sit at the top.

### 7.5 No-image fallback
If imagery can't be produced, every slide can still be built from:
1. **Type-only:** Display or H1 plus ghost type plus super-shape (section 8.9).
2. **Numeral hero:** Numeral XXL plus line chart or dot field (section 8.6).
3. **Interface fragments** (Family C) built in HTML/CSS/SVG.
4. **Abstract glass in CSS:** overlapping rounded rectangles or circles with `backdrop-filter: blur(24px)`, fill `rgba(255,255,255,.08–.16)`, 2 px white border at 20%, and the accent glow behind them.

---

## 8. Graphic elements and motifs

### 8.1 Eyebrow pill (category label)
Sits at **x 96, y 192**, above the headline on text-top layouts.
| Property | Value |
|---|---|
| Height | 48 px, padding 0 22 px, `r-pill` |
| Text | JetBrains Mono 500, 20 px, UPPERCASE, +0.08em, 1–3 words |
| Leading dot | 10 px circle, 12 px gap before text |
| DARK | fill `rgba(255,255,255,.06)`, 2 px border `rgba(255,255,255,.14)`, text `snow`, dot `accent-300` |
| LIGHT | fill `ink-950`, text `snow`, dot `accent-300` |
| ACCENT | fill `white`, text `accent-700`, dot `accent-500` |

**Sticker variant** (Family C only): the same pill attached to a card corner, rotated **−6° to +6°**, overlapping the card edge by half its height. Maximum one per slide.

### 8.2 UI card
| Property | Value |
|---|---|
| Fill | `linear-gradient(180deg, #17171F 0%, #101015 100%)`, **dark in every mode** |
| Radius | 28 px; inner elements 16 px or pill |
| Border | 2 px `rgba(255,255,255,.08)` + 1 px top highlight `rgba(255,255,255,.12)` |
| Padding | 32 px |
| Shadow | per mode (section 6.4) |
| Contents | UI text 20–26 px; primary button = white pill with `ink-950` text; secondary = outline pill; status = `signal-500` dot or check; data accent = `accent-300` |
| Width | Primary card 560–720 px; secondary cards 320–480 px |

Cards are flat-on (not rotated, no 3D perspective). Only sticker pills rotate.

### 8.3 Highlight bar
- A solid rectangle behind 1–4 words of a headline, **`r-xs` 6 px**, padding **0.08em vertical / 0.2em horizontal**. Each wrapped line gets its own bar (`box-decoration-break: clone`).
- DARK and LIGHT: bar `accent-500`, text `white`. ACCENT: bar `white`, text `accent-700`.
- Max one per slide; never in the same headline as an accent phrase.

### 8.4 Hairline rows (lists)
- 2 px dividers in the mode's hairline color, full live width (x 96 → 984).
- Row height 96 px. Index number in Mono 20 px accent at x 96; text in H3 at x 172 (col 2); optional right-aligned meta at x 984.

### 8.5 Connector lines and nodes
- 2–3 px strokes, round caps, in the accent or hairline color. Paths are smooth Bézier curves or orthogonal elbows with **24 px corner radius**.
- Nodes: 12 px solid accent dots, or 40 px circles with a 2 px ring and an icon.
- Used for flows, convergence (several inputs merging into one) and the thread line (section 11.4).

### 8.6 Data graphics
- **Line chart:** a single 3 px accent line (on DARK, add an 8 px blur duplicate at 50% for glow), no axes, no grid, no labels except **one end-point chip** (a small pill with the value). The line usually bleeds off the right edge.
- **Dot field / map:** 8–14 px dots on an even grid in hairline color, with 3–8 highlighted dots in accent.
- **Progress ring:** a 6 px stroke ring, track in hairline color, value arc in accent with round caps.
- Avoid bar charts, pie charts and multi-series charts. One data idea per slide.

### 8.7 Line patterns (atmosphere; max one per slide)
- **Concentric rings:** 2 px strokes, spacing 56 px, centered on the hero, opacity 6–10%, fading radially to 0 at about 600 px. Recipe: `repeating-radial-gradient(circle at X Y, transparent 0 54px, rgba(255,255,255,.08) 54px 56px)` masked by a radial fade.
- **Perspective wire grid:** 2 px lines every 72 px at 8% opacity, receding toward a vanishing point behind the hero (a floor under an object).
- **Dot grid:** 4 px dots every 32 px at 10%.

### 8.8 Halftone (Family B only, optional lock)
- A 45° dot screen of about 10–12 px cells over the cutout, dots in `ink-950` (multiply) on light or `white` (screen) on dark, opacity 25–40%.
- Recipe: `background-image: radial-gradient(circle, #000 32%, transparent 34%); background-size: 11px 11px; transform: rotate(45deg)`, clipped to the cutout's alpha.

### 8.9 Super-shape
A single brand-derived geometric shape (default: **perfect circle**; alternatives: quarter-round block, rounded blob, 4-point star; lock one per brand), shown **huge and cropped**:
- Size 1.2–2× the canvas width. Only **15–35% visible** on any slide.
- Color: `accent-500` on DARK and LIGHT, `ink-950` on ACCENT. Grain applies on top.
- Sits behind text but in front of the background. Text over it must keep its contrast. If text overlaps the shape, the overlapping part switches color (e.g. white text on the accent shape).
- Its position changes per slide; its form never does.

### 8.10 Human-touch accents (optional dial; default OFF)
A single hand-made counterpoint to the clean grotesk. Choose **one** for the whole carousel:
- **Italic serif word:** one word in a headline set in Instrument Serif Italic at 1.08× the headline size, in the emphasis color. Max one per slide, on ≤ 50% of slides.
- **Marker stroke:** a hand-drawn accent stroke (6–8 px, round caps, slight wobble, single pass): an underline swoosh under a word, a loose ellipse around a word, or a short curved arrow pointing at the hero. Max one per slide.

### 8.11 Icons
- Line icons only (Lucide/Feather style), 2 px stroke, round caps and joins, sized 32–48 px, in text-primary or accent.
- Never filled, multicolor, emoji or 3D icons.

### 8.12 Logo usage
- **Mark only** in the frame (40 px). The **full logo** may appear once on the CTA slide at 96–140 px.
- Single color only (text-primary of the mode). No effects on the logo.

---

## 9. Composition principles

1. **One focal point.** Decide the hero first: headline, numeral or object. The second-largest element should be **≤ ⅓** of the hero's visual weight.
2. **Diagonal balance.** Place the text mass and the hero mass in **opposite quadrants**: default text top-left with hero bottom-right; variation hero top with text bottom-left.
3. **Negative space ≥ 35%** of the content zone (background, glow and grain don't count as filled).
4. **Scale jumps ≥ 1.6×** between adjacent hierarchy levels; the headline is ≥ 3× body size.
5. **Edge tension.** Every slide has at least one element that touches or bleeds an edge (hero object, ghost type, super-shape, line or chart).
6. **Shared axes across slides.** The text axis is x = 96; pills sit at y = 192 and headlines start at y = 288 on every text-top layout. When swiping, the text stays fixed and only the scenery changes.
7. **Layer order (back → front):** background gradient → line pattern → super-shape → ghost type → glow → hero object/cards → text → frame. Text is always above images.
8. **Text over imagery** only on calm areas, with contrast meeting section 4.4. Never put text over detailed parts of an object.
9. **Nothing centered** except the CTA slide and symmetric hero objects (an object can be centered horizontally while the text stays left-aligned).
10. **Quiet body.** Body text is short, small and secondary. It should never compete with the hero.

---

## 10. Layout templates

All coordinates are on the 1080 × 1350 canvas. "Live" means x 96–984. The frame (section 3) is present on every template.

### T1 — Statement Cover
- **Mode:** Cover lock (D or A).
- Pill at (96, 192).
- **Display headline** at y 288, width up to 888 (12 columns), ≤ 3 lines, one accent phrase.
- **Hero object** in the bottom-right quadrant: bounding box about x 500 → 1180 (bleeds off the right edge), y 600 → 1150 (stays out of the footer row). Glow centered on the object.
- Optional ghost word behind the object.
- **Lead** (34 px, ≤ 2 lines) bottom-left at y about 1020, width ≤ 356 (5 columns), so it stays clear of the hero box.
- Swipe cue in its filled cover variant.

### T2 — Headline + Object (the workhorse)
- Pill at (96, 192). **H1** at y 288, width ≤ 736 (10 columns), ≤ 4 lines.
- Body 40 px below the headline, width ≤ 508 (7 columns).
- Hero object or card in the lower-right: box x 520 → 1080+ (may bleed), y 640 → 1134.

### T3 — Object + Headline (mirror)
- Hero visual or card cluster in the **upper half**: centered horizontally or offset right, y 192 → 700, may bleed the right edge. No pill on this template (the visual takes the top).
- **H1** anchored bottom-left: last baseline at about y 1080, width ≤ 584 (8 columns).
- Body either below the H1 (if 1–2 lines) **or** as a small column at x 704 → 984 (cols 9–12), top-aligned with the H1's last line.

### T4 — Big Number
- Pill at (96, 192).
- **Numeral XXL** with its top at y 272, left at x 88 (an −8 px optical offset for thin numerals), fully visible.
- **H2 label** 32 px below the numeral, width ≤ 584.
- Body ≤ 2 lines, width ≤ 432.
- Supporting graphic in the lower third: a line chart from x 96 that bleeds off the right edge, with one end-point chip, **or** a dot field, **or** a small object at the bottom-right.
- Glow behind the numeral on D and A slides.

### T5 — Numbered Point
- **Ghost numeral** (800–1000 px, 200 weight), right-aligned so that 25–35% bleeds off the right edge, vertically centered.
- Pill at (96, 192) with an index (e.g. `POINT 02`).
- **H2** at y 288, width ≤ 660 (9 columns).
- Body 40 px below, width ≤ 584, ≤ 40 words.
- Optional small object or card at the bottom-left or bottom-right (≤ 30% of the height).
- In a series of numbered points, repeat T5 but **alternate the background mode** and **mirror the object side**.

### T6 — Contrast / Comparison
- Pill plus **H1** (≤ 2 lines) at the top.
- Two cards side by side at y 560 → 1100: left x 96 → 528, right x 552 → 984 (6 columns each, 24 px gutter); or stacked full width with the second overlapping the first by 48 px.
- **Card A (before / other):** muted (text in recede gray, no accent).
- **Card B (after / ours):** accent, with a 2 px `accent-500` border, an accent underglow and a `signal-500` check if relevant.
- An optional connector arrow between the cards.

### T7 — List / Rows
- Pill plus **H1** (≤ 2 lines) at the top.
- 3–5 hairline rows (section 8.4) starting at y about 600, each 96 px tall, spanning x 96 → 984.
- An optional small object bleeding in from the right edge behind the rows (≤ 20% opacity if it's behind text, otherwise fully clear of the rows).

### T8 — Flow / Interface Focus
- A card cluster or a flow diagram (nodes plus connector lines) is the hero, centered in y 360 → 940, spanning up to the full live width. Cards may overlap; one sticker pill is allowed.
- **H1** either at the top (pill at 192, H1 at 288, ≤ 2 lines) **or** at the bottom (last baseline about 1080); never both.
- The hero glow sits behind the main card.

### T9 — Manifesto (type-only)
- No pill (or a pill only if the series needs it).
- **Display** at 120–160 px, starting at y 288, 3–5 lines, width up to 888. Use **recede split** emphasis (key words text-primary, the rest recede gray). On ACCENT, recede isn't available, so use an `ink-950` accent phrase instead.
- **Super-shape** cropped into the bottom-right or right edge, 15–30% visible.
- Optional ghost word. Nothing else.

### T10 — CTA / Closing (the only centered layout)
- **Mode:** same as the cover (bookend).
- Full logo or a large logo mark, centered, 96–140 px tall, at about y 380.
- **H1** centered, ≤ 2 lines, width ≤ 736, at about y 560.
- Lead or body centered, ≤ 2 lines, width ≤ 584.
- **Action row** at about y 960: 2–3 small outline pills (icon plus Mono label, e.g. save / share / follow), centered, with 16 px gaps.
- The thread line or super-shape **resolves** here: the line ends in a node at the logo, or the shape becomes a complete, uncropped circle behind the logo.
- No swipe cue.

---

## 11. Carousel architecture (consistency between slides)

### 11.1 Mode sequencing rules
1. **Cover** = DARK (default) or ACCENT (see section 12.2).
2. **Final slide** = the same mode as the cover (bookend).
3. **Adjacent slides differ in mode.** Allow at most one same-mode pair per carousel, and **never 3 in a row**.
4. **ACCENT slides:** at least 1 and at most ⅓ of the carousel. They are never adjacent to each other and are reserved for peaks: the cover, the key stat or insight, and/or the CTA.
5. **DARK and LIGHT** split the rest roughly evenly.

**Reference sequences**
| Slides | Sequence (cover → end) |
|---|---|
| 5 | `D · L · A · L · D` |
| 6 | `D · L · D · A · L · D` |
| 7 | `D · L · D · L · A · L · D` |
| 8 | `D · L · A · L · D · L · A · D` |
| 10 | `D · L · D · A · L · D · L · A · L · D` |
| ACCENT cover (any length) | Start and end on `A`, alternate `L`/`D` between, add 0–1 interior `A` (e.g. 7: `A · L · D · L · D · L · A`) |

### 11.2 Layout rhythm rules
- **Never use the same template on two consecutive slides**, except a T5 series (which must then alternate mode and mirror the object side).
- **Zig-zag the hero.** If slide *n* has its hero bottom-right, slide *n+1* puts its hero top, left or as type-only. The eye should travel diagonally through the carousel.
- **Vary the hero type.** Within any 3 consecutive slides, include at least two different hero types (object, numeral, type-only, cards).
- **Scale pulse.** Follow a very large hero (Display, Numeral, ghost) with a calmer slide (T2 or T7), and vice versa.

**Default story arc**
| Position | Purpose | Recommended template |
|---|---|---|
| 1 | Hook / cover | T1 |
| 2 | Context / problem | T2 or T9 |
| 3…n−2 | Points, proof, data, process | T4, T5, T6, T7, T8 (vary) |
| n−1 | Peak / key insight (often ACCENT) | T4 or T9 |
| n | CTA | T10 |

### 11.3 Seam continuity (the panorama)
Instagram shows carousel slides edge to edge, so design them as one strip:
- **Work on a strip** of `N × 1080` × 1350 px, then slice it at x = 1080, 2160, 3240 and so on.
- **No text ever crosses a seam.** Keep text at least 96 px from every seam (the margins already guarantee this).
- **Each half stands alone.** An element crossing a seam must look intentional on both slides, with **≥ 30% of the element on each side**. Never leave a sliver.
- **Seam elements use the accent color** (or glass/chrome objects with an accent tint), so they hold up across a change of background mode (for example a D → L seam). **On ACCENT slides, accent-colored lines and shapes switch to `white`** (the super-shape switches to `ink-950`). The color switch happens exactly at the seam, where the background also changes.
- Never cross the seam between the last content slide and the CTA with an object. Only the thread line or super-shape may arrive there and **resolve** on the CTA.

### 11.4 Continuity devices (one primary device per carousel; see section 12.2)
**Thread line** *(default)*
- A single 3 px accent line (optionally with an 8 px glow duplicate on D slides; white on A slides) that runs through every slide.
- It exits the right edge of slide *n* at a height Y and enters slide *n+1* at x = 0 at **exactly the same Y**.
- Inside a slide it may curve, step with 24 px rounded elbows, pass through 12 px nodes, become a chart line (T4) or a flow connector (T8). It never touches, crosses or underlines text.
- It ends on the CTA slide in a node at the logo or the action row.
- Its route stays in the "quiet" zones: it never crosses the headline box or the hero's face.

**Super-shape migration**
- The super-shape (section 8.9) appears on about 50–70% of slides, crossing at least 2 seams, so it "rolls" through the carousel. It completes into a full shape on the CTA.

**Seam objects**
- 2–3 hero objects in the carousel are placed centered on a seam (split 40/60 to 60/40), typically on seams 1–2 and in the middle of the carousel.

Regardless of the primary device, a **secondary seam object** is allowed at most once.

### 11.5 Cover and CTA rules
- **Cover:** the highest contrast and largest type in the carousel. Display ≥ 120 px, ≤ 6 words, one accent phrase. One hero object or numeral. It must still read at about 1/3 scale (profile grid): test by viewing it at 360 px wide.
- **CTA:** same mode as the cover, centered, calm, with the continuity device resolving. No new visual ideas on the last slide.

---

## 12. Consistency contract

### 12.1 CONSTANT: never changes on any slide of any carousel
| Category | Constant |
|---|---|
| Canvas | 1080 × 1350, 96 px margins, 12-column grid, 8 px baseline |
| Frame | Logo mark top-left, progress top-right, handle bottom-left, swipe cue bottom-right, with exact positions and styles (section 3) |
| Anchors | Text axis x = 96; pill at y 192; headline top at y 288 (text-top layouts) |
| Type | Inter Tight plus JetBrains Mono; the weight system (600 / 200 / 400 / Mono 500); the scale ranges; sentence case; left alignment (except T10); negative tracking on display |
| Emphasis | Color-based two-tone headlines; ≤ 2 colors per headline; ≤ 2 accent instances per slide |
| Color | Neutral palette; a single accent ramp; the three background modes and their exact recipes; contrast pairs |
| Surfaces | Dark UI cards in every mode; radii 6/16/28/56/pill; 2 px hairlines; shadow and glow recipes |
| Texture | Grain on every slide; no flat fills |
| Imagery treatment | Monochrome or accent-tinted only; isolated subjects; top-left light |
| Composition | One hero, ≥ 35% empty space, diagonal balance, edge tension, the layer order |

### 12.2 LOCKED PER CAROUSEL: choose once, then apply identically to all slides
| Dial | Options | Default |
|---|---|---|
| **1. Cover / bookend mode** | DARK · ACCENT | **DARK** |
| **2. Primary imagery family** | A Glass & Chrome 3D · B Monochrome cutouts · C Interface fragments | **A** |
| **3. Continuity device** | Thread line · Super-shape migration · Seam objects | **Thread line** |
| **4. Human-touch accent** | Off · Italic serif word · Marker stroke | **Off** |

Also locked per carousel (implied):
- **Ghost type treatment:** fill *or* outline (section 5.6).
- **Halftone** on or off (Family B only).
- **Super-shape form** (locked per brand).
- **Secondary imagery family:** optional, at most 1, used on ≤ 30% of image slides, and only if it follows the same treatment (monochrome plus accent). Family C pairs well with A or B. **A and B together are allowed** only if the B cutouts are on LIGHT slides and the A renders on DARK or ACCENT slides.

### 12.3 VARIABLE PER SLIDE: free within the rules
| Variable | Constraint |
|---|---|
| Background mode | Follows the sequencing rules (section 11.1) |
| Layout template | Follows the rhythm rules (section 11.2) |
| Hero type and subject | Object, numeral, type-only or cards; the subject follows the locked family |
| Hero position | The diagonal zig-zag across slides |
| Headline size | Within the role's range (e.g. H1 88–104) |
| Emphasized words and method | Accent phrase, recede split or highlight bar (≤ 1 bar per slide) |
| Ghost type | Present or absent (30–50% of slides), word or numeral |
| Atmosphere pattern | Rings, wire grid, dot grid or none (max 1 per slide) |
| Glow position | Always behind the hero, wherever the hero is |
| Pill text | Changes per slide; style is fixed |
| Data graphic | Line, dot field or ring (only on data slides) |

---

## 13. Do / Don't

**Do**
- Let one element dominate each slide, and make it big.
- Use the accent sparingly so it means something.
- Alternate the background modes, and bookend the cover and CTA.
- Keep text on the x = 96 axis and at the fixed y anchors.
- Let objects, lines and ghost type bleed off the edges.
- Put every hero in light (glow on dark and accent slides, contact shadow on light slides).
- Design the carousel as one strip and check every seam.
- Keep body text short, small and gray.
- Apply grain to everything, last.

**Don't**
- Use any second hue, rainbow gradients or full-color photos.
- Center headlines or body text (except on the CTA).
- Use bold or italic weight changes for emphasis inside a headline.
- Put more than one hero, or more than 3 text sizes, on a slide.
- Use drop shadows, outlines or gradients on text (gradients are for numerals only).
- Use sharp-cornered containers, thick borders, slide borders or decorative frames.
- Use clip-art, emoji, filled multicolor icons or stock-photo scenes.
- Put text over busy image detail or across a seam.
- Use body text smaller than 28 px or pack in more than about 40 words of body copy.
- Use `signal-500` outside UI elements.
- Move, resize or restyle frame elements between slides.

---

## 14. QA checklist

**Per slide**
- [ ] The frame is present and pixel-identical in position (swipe cue absent only on the last slide).
- [ ] Exactly one hero, clearly dominant.
- [ ] Text starts at x = 96; pill at y 192 and headline at y 288 (if it's a text-top layout).
- [ ] Headline is two-tone, with ≤ 2 colors and one emphasized phrase.
- [ ] ≤ 3 text sizes (excluding meta and UI); body ≥ 28 px; meta ≥ 20 px.
- [ ] All text and background pairs meet section 4.4.
- [ ] ≥ 35% empty space; at least one element touches or bleeds an edge.
- [ ] Imagery is monochrome or accent-tinted; light comes from the top-left; the hero has a glow or contact shadow.
- [ ] Background is a gradient (not flat); grain is applied.
- [ ] ≤ 2 accent instances; ≤ 1 highlight bar; ≤ 1 atmosphere pattern; ≤ 1 ghost element.

**Per carousel**
- [ ] The cover reads at 360 px wide; Display ≥ 120 px; ≤ 6 words.
- [ ] Mode sequence: no two adjacent slides share a mode (one exception max), never 3 in a row, ACCENT slides never adjacent, CTA mode = cover mode.
- [ ] No template repeated back-to-back (except a T5 series with alternating modes and mirrored sides).
- [ ] The hero position zig-zags; hero types vary.
- [ ] All four per-carousel dials are chosen and applied consistently.
- [ ] The continuity device crosses the seams correctly (exact Y match, ≥ 30% per side, no text on seams) and resolves on the CTA.
- [ ] Progress counter numbering is correct (`01 / N` … `N / N`).
- [ ] The whole strip, viewed side by side, reads as one continuous piece.

---

## 15. Design tokens

```css
:root {
  /* Canvas */
  --canvas-w: 1080px;  --canvas-h: 1350px;
  --margin: 96px;      --gutter: 24px;  --col: 52px;
  --y-pill: 192px;     --y-headline: 288px;
  --content-top: 192px; --content-bottom: 1134px;

  /* Neutrals */
  --ink-950: #0A0A0D;  --ink-900: #121218;  --ink-850: #17171F;  --ink-700: #2A2A33;
  --gray-600: #5E5E6A; --gray-500: #6E6E7A; --gray-450: #7E7E8A;
  --gray-400: #8B8B97; --gray-300: #A1A1AC;
  --paper-50: #F7F7FA; --paper-100: #F2F2F5; --paper-200: #E4E5EB;
  --snow: #F5F5F7;     --white: #FFFFFF;

  /* Accent (swap the whole ramp together) */
  --accent-100: #E3E6FF; --accent-300: #8F98FF;
  --accent-500: #4353FF; --accent-700: #2530C9;
  --accent-gradient: linear-gradient(120deg, #7A6BFF 0%, #4353FF 50%, #3B9BFF 100%);
  --signal-500: #3DDC84; /* UI only */

  /* Backgrounds */
  --bg-dark:
    radial-gradient(80% 60% at var(--hero-x, 70%) var(--hero-y, 70%), #1A1C2E 0%, transparent 70%),
    radial-gradient(120% 100% at 50% 50%, transparent 60%, rgba(0,0,0,.45) 100%),
    #0A0A0D;
  --bg-light:
    radial-gradient(70% 50% at 10% 0%, rgba(255,255,255,.9) 0%, transparent 70%),
    linear-gradient(160deg, #F7F7FA 0%, #ECEDF1 55%, #E4E5EB 100%);
  --bg-accent:
    radial-gradient(70% 50% at 10% 0%, rgba(255,255,255,.14) 0%, transparent 70%),
    linear-gradient(150deg, #5D6BFF 0%, #4353FF 45%, #2B36D6 100%);

  /* Type */
  --font-primary: "Inter Tight", "Inter", "Helvetica Neue", Arial, sans-serif;
  --font-meta: "JetBrains Mono", "IBM Plex Mono", ui-monospace, monospace;
  --font-serif: "Instrument Serif", "Playfair Display", Georgia, serif;

  --fs-numeral: 380px; --fw-numeral: 200; --lh-numeral: .85; --ls-numeral: -.06em;
  --fs-display: 128px; --fw-display: 600; --lh-display: .95; --ls-display: -.045em;
  --fs-h1: 96px;       --fw-h1: 600;      --lh-h1: 1.0;      --ls-h1: -.035em;
  --fs-h2: 60px;       --fw-h2: 600;      --lh-h2: 1.05;     --ls-h2: -.025em;
  --fs-h3: 42px;       --fw-h3: 500;      --lh-h3: 1.15;     --ls-h3: -.015em;
  --fs-lead: 35px;     --fw-lead: 400;    --lh-lead: 1.3;    --ls-lead: -.01em;
  --fs-body: 29px;     --fw-body: 400;    --lh-body: 1.4;    --ls-body: -.005em;
  --fs-ui: 24px;       --fw-ui: 500;
  --fs-meta: 20px;     --fw-meta: 500;    --ls-meta: .08em;

  /* Radius */
  --r-xs: 6px; --r-sm: 16px; --r-md: 28px; --r-lg: 56px; --r-pill: 999px;

  /* Lines */
  --hairline: 2px;
  --hair-dark: rgba(255,255,255,.12);
  --hair-light: rgba(10,10,13,.12);
  --hair-accent: rgba(255,255,255,.24);

  /* Shadows */
  --shadow-light: 0 48px 96px -24px rgba(10,10,20,.40), 0 12px 32px -8px rgba(10,10,20,.18);
  --shadow-dark-glow: 0 40px 120px -20px rgba(67,83,255,.35);
  --shadow-accent: 0 40px 100px -24px rgba(16,20,90,.55);

  /* Card */
  --card-fill: linear-gradient(180deg, #17171F 0%, #101015 100%);
  --card-border: 2px solid rgba(255,255,255,.08);
  --card-pad: 32px;

  /* Grain opacity per mode */
  --grain-dark: .07; --grain-light: .05; --grain-accent: .08;
}
```

```json
{
  "system": "Electric Mono",
  "canvas": { "w": 1080, "h": 1350, "margin": 96, "columns": 12, "col": 52, "gutter": 24, "baseline": 8 },
  "anchors": { "textX": 96, "pillY": 192, "headlineY": 288, "contentBottom": 1134 },
  "frame": {
    "logo": { "x": 96, "y": 96, "h": 40 },
    "progress": { "rightX": 984, "centerY": 116, "font": "meta", "format": "NN / NN" },
    "handle": { "x": 96, "baselineY": 1240, "font": "meta" },
    "swipeCue": { "rightX": 984, "centerY": 1226, "size": 56, "hideOnLast": true }
  },
  "dialsDefault": { "coverMode": "dark", "imagery": "glass-chrome", "continuity": "thread-line", "humanTouch": "off" },
  "modeSequence": { "5": "DLALD", "6": "DLDALD", "7": "DLDLALD", "8": "DLALDLAD", "10": "DLDALDLALD" }
}
```

---

## 16. Worked blueprint (abstract example, 7 slides, all defaults)

*Dials: Cover = DARK · Imagery = Glass & Chrome · Continuity = Thread line · Human-touch = Off · Ghost = fill.*

| # | Mode | Template | Hero | Composition notes | Thread line |
|---|---|---|---|---|---|
| 1 | D | T1 Cover | Glass object, bottom-right (box x 500 → 1180, y 600 → 1110), bleeding right | Display (3 lines, y 288 → ~655), accent phrase on line 2; ghost word behind the object; strong accent glow | Starts in a node at the object's contact point (~x 760, y 1140) and exits right at **y 1140** |
| 2 | L | T3 Mirror | Glass object at the top, centered (y 192 → 700), contact shadow | H1 (2 lines) bottom-left, last baseline ~1060, recede split; body as a 2-line right column at x 704 → 984 (ends ~1070) | Enters at y 1140, runs straight beneath the text block, exits at **y 1140** |
| 3 | D | T4 Big Number | Numeral XXL in accent gradient, top-left (y 272 → ~595) | H2 label (~627 → 690); 2-line body (~730 → 815), x ≤ 528; glow behind the numeral | Enters at y 1140 and becomes the line chart, rising to an end-point value chip at ~(840, 960) (right of the body, below it), exits at **y 940** |
| 4 | L | T5 Numbered Point | Ghost numeral bleeding off the right edge; small glass object bottom-right (x 640 → 1000, y 820 → 1134) | Pill index; H2 (288 → ~480) with a highlight bar; body (520 → ~760), width 584 | Enters at y 940, steps down at x 240 with a 24 px elbow to **y 1150** and runs under the object as its "floor" (contact shadow sits on the line), exits at **y 1150** |
| 5 | A | T9 Manifesto | Type-only, Display 140 px (288 → ~950) | `ink-950` accent phrase (no recede on ACCENT); super-shape in `ink-950` cropped at the bottom-right; concentric rings | Switches to white at the seam, enters at y 1150 below the text, runs straight, exits at **y 1150** |
| 6 | L | T8 Flow | Interface cards plus flow nodes, centered (y 560 → 940) | Pill plus H1 at the **top** (288 → ~480, 2 lines); one sticker pill on the main card | Enters at y 1150, rises at x 160 to y 750, runs through the flow nodes as their connector (x 160 → 920), drops at x 940 to **y 1100** and exits right |
| 7 | D | T10 CTA | Logo, centered (~y 380) | Centered H1 (~560 → 760), action row (~960 → 1008); no swipe cue | Enters at y 1100 and curves up into a node at the left end of the action row (~x 300, y 984). This is where the thread resolves. |

Check:
- **Modes** D L D L A L D: adjacent slides always differ, a single ACCENT peak, bookended by DARK.
- **Templates** T1 → T3 → T4 → T5 → T9 → T8 → T10: no repeats.
- **Hero zig-zag:** bottom-right object → top object → top-left numeral → right ghost and bottom-right object → type-only → centered cluster → centered logo. No two consecutive slides share a hero position.
- **Imagery:** Family A (glass) is primary on slides 1, 2 and 4. Family C (cards) appears once, on slide 6: 1 of 4 image slides (25%, within the ≤ 30% cap).
- **Thread:** the exit Y matches the next slide's entry Y at every seam (1140, 1140, 940, 1150, 1150, 1100). The thread never crosses a text box or a frame clear-space zone (it stays above y 1174 near the swipe cue), turns white only on the ACCENT slide, and resolves on the CTA.

---

*End of system. If something isn't covered here, choose the option that is quieter, more monochrome and more consistent with the slides already made.*
