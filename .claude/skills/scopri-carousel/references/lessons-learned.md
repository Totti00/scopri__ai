# Lessons learned from the first carousel

This file records what happened between the original brief and the approved carousel ("5 prompt prima di firmare", Oct 2026). It covers the user's feedback, the decisions it produced, the mistakes that had to be corrected, and the technical traps. Read it before writing copy and again before building.

## Contents
1. Copy-stage feedback
2. Design-stage feedback
3. Publishing-stage feedback
4. Recurring mistakes and their fixes
5. Technical traps
6. Working-style notes

---

## 1. Copy-stage feedback

| What happened | Rule it produced |
|---|---|
| The first draft had 5 one-line prompts (~25 words each). The user said: "vorrei prompt più lunghi, di 100 parole circa. Prompt efficaci che funzionerebbero, non una semplice domanda o azione da far fare ad un LLM." | When the carousel teaches prompts, each prompt is a **complete, working ~100-word prompt**. Use the structure: **role** ("Agisci come…") → **context** (what is attached; personal data already hidden) → **3–4 numbered tasks** → **output rules** (format such as a table, plus an anti-hallucination rule: "se un dato non è leggibile, dimmelo: non inventarlo", "citala parola per parola", "se manca un dato, chiedimelo"). Mark the parts to replace with `[parentesi quadre]`. Keep all prompts in one carousel parallel in shape. |
| I proposed a "Perché funzionano" (prompt-anatomy) slide in place of the recap. The user removed it: "la slide 9 non la voglio, il resto va benissimo". | Don't add meta or explanatory slides the content doesn't need. A recap or summary slide is optional: propose one only when it adds real save value, and don't insist. |
| The user approved with "il resto va benissimo". | A clear positive statement counts as approval of everything not mentioned. Apply the requested change and continue. Don't ask for approval again for the same draft. |
| The user twice clicked a reply button whose text ended in ":" ("I'd like these changes to the copy:"), and it sent nothing after the colon. | Don't offer reply buttons that need the user to type more. When asking for revisions, ask an open question in the message. Buttons must be complete messages ("Approva il copy", "Riscrivi l'hook"). |
| The cover hook "5 prompt prima di firmare" (4 words) was approved. The alternatives were offered alongside it. | Offer 2–3 alternative hooks next to the pick. The cover display holds **≤ 6 words** (design-system §11.5), about 13 characters per line at 128 px. That is stricter than the copy guide's 12 words. |

## 2. Design-stage feedback

| What happened | Rule it produced |
|---|---|
| I put the speech-bubble symbol alone in the frame. The user said: "hai messo la foto profilo nelle slide, non il logo. io voglio il logo (scopri AI)". | The frame shows the **full logo lockup** (see `brand-scopri-ai.md` §4). |
| The final slide showed the logo twice, top-left and centred. The user said: "c'è la ripetizione di scopri AI". | On the closing slide, drop the corner logo. |
| The counter read 09 / 09 on the closing slide. The user said it "non dovrebbe contare anche l'ultima" and the closing slide shouldn't have a counter. | The counter counts content slides only, and the closing slide has none. The engine does this automatically. |
| The user shared their colours (white, blue, yellow) and logo. | Apply the brand blue as the accent ramp. Don't introduce yellow (single accent hue). Explain why in one line, and offer it as an exception. |
| Replicate failed (invalid token). The user said: "genera tu le immagini, lascio stare replicate". | In-house 3D renders (three.js, difference-matted transparent PNGs) are the default way to get Family A glass & chrome objects. See `imagery.md`. |
| I placed handle and logo as placeholders after asking twice for them. | For Scopri AI both are known now (`@scopri__ai`, Coperchio kit). Never ship placeholders. If a brand detail is unknown, ask once, together with the copy, so it doesn't block later. |

### 20 Oct 2026 — "Prima e dopo: la TV ripulita dall'AI" (news, owner's draft review)

| What happened | Rule it produced |
|---|---|
| Real before/after photos and the video were toned mono-blue. The owner: everything in colour, video included. | Real photos and videos stay in **colour** (`data-tone="color"`, plain `.img-box`). |
| The cover carried the "NEWS LAMPO" pill. | **No rubric label on the cover**, ever. Content slides keep their eyebrow, now a plain mono label with an accent dash (no box, no dot). |
| `@scopri__ai` printed bottom-left on every slide. | **No handle** in the frame (engine). |
| The closing pill "MANDA" (small, outlined, uppercase mono) wasn't understood. | Filled blue button with icon and words ("Mandalo a un amico"), then a smaller **🔔 Seguici per non perdere le prossime notizie** line with the logo's lid as the bell. Hierarchy: headline → button → follow line. Text per type from `CAROUSEL.tipo`. |
| Round pills with a coloured dot over images and cards ("Prima", "Dopo", "Sparita", "Vola", "Fai-da-te"…) looked cheap. | **Captions under the image** (`.cap[data-under]`), same gap and style on every slide; centred under both images when it applies to both. Stickers are no longer used on Scopri AI slides. |
| Caption: only the main invite. | Every caption also has a `🔔 Seguici per non perdere …` line before Fonti/hashtags (not in *serie*). `caption_check.py` warns when it is missing and doesn't count it as a second invite. |
| Second review: the comment captions under images ("Sembra una Apple TV.", "Vola.", "Rischio vero.", "Prima: l'annuncio. Ora è sparito.") went too. | Then the owner wanted the comparison captions back with their text. Final rule: **only comparison captions, «Prima: …» / «Dopo: …»** with 1–3 words on what changes ("Prima: pubblicità" / "Dopo: solo le app"), under the images of a before/after. No other caption or comment on the slides, and none on an image outside a comparison. Anything that must be said (e.g. "non è un prodotto ufficiale") goes in the body or inside a card. |
| The cover with two side-by-side cropped screens was less striking than the earlier overlap. | Cover before/after = **overlapping collage**: before behind top-left, after in front bottom-right (`.img-box.front`), captions under the visible bottom-left edge of each. |
| Mihir Gupta's before/after were cropped to fill the boxes. | Before/after screenshots inside the carousel are shown **whole**, at their original ratio (box sized to the image), side by side. |
| `python` in `/usr/local/bin` (cloud) has a broken Pillow; `npm run previews` / `npm run media` failed. | Run them with `PATH=/usr/bin:$PATH`. |
| The cover headline at top 200 measured 191 (font ascent) and failed the live-area QA. | Without a pill, start the cover headline at **y 216**. |

## 3. Publishing-stage feedback

| What happened | Rule it produced |
|---|---|
| The user asked "caption? e testo alternativo?" after the build. | Always deliver caption **and** alt text with the finished carousel, without being asked. |
| The user asked "niente emoji nella caption?" | Captions use emoji, about one per block or line start (👇 🧠 📌 💬 🔒 ✍️ 📅 ⚠️ 🔖 style). Prompts in pinned comments stay emoji-free, because people paste them into an AI. |
| The user asked for the texts as separate `.txt` files. | Write a `pubblicazione/` folder: `01-caption.txt`, `02-alt-text-slide-XX.txt` (one per slide), `03-commento-fissato-N.txt`. Each file holds only the text to paste. `scripts/publish-pack.py` does this and checks the limits. |
| Five 100-word prompts (about 2,870 characters) don't fit in a caption (2,200 limit). | Put the full prompts in pinned comments, each ≤ 2,200 characters (Instagram pins up to 3). The caption points to them ("Copiali dai commenti fissati qui sotto…") and mentions screenshot text-copy as a fallback. |

## 4. Recurring mistakes and their fixes

1. **Single words alone on the last line** ("accanto.", "traduce.", "chi sei."). Fix: `text-wrap: pretty` on body, lead and card text, and `text-wrap: balance` on centred leads. The engine sets both. Still check the renders.
2. **A sticker pill overlapping the card's first line.** Fix: leave about 48 px of top padding in any card that carries a sticker.
3. **Ghost numerals cropped so far off the edge that "01" read as "0".** Fix: `right: -72px` at 460 px. Keep both digits legible, with only 15–30% off-canvas.
4. **The cover lens hid the card title**, so it read "Offerta l…zzo fisso" and looked like a glitch in the thumbnail. Fix: move the magnified target line lower. Always check the cover at 360 px wide.
5. **Text overlapping a hero object.** Check the display's longest line against the object box. On slide 2 the hourglass had to start below the headline's last line, and was scaled to 82%.
6. **Chrome rendered nearly black.** A dark studio means a dark mirror. Fix: a light gradient dome plus big softboxes. See `imagery.md`.
7. **Placeholder brand details shipped**, and handle and logo were asked for three times. For Scopri AI they are now fixed in the brand file.
8. **Claims.** The 14-day cooling-off right applies only to contracts signed at a distance or away from the seller's premises. State that, and when the 14 days start. Privacy advice ("oscura IBAN, codice fiscale, POD") was presented as practical advice, not attributed to the Garante, because no source was found. **Qualify legal claims, don't attribute advice to authorities you didn't verify, keep carousels evergreen** (skip dated news unless asked), and list sources in chat.

## 5. Technical traps

- **Fonts in headless export.** Wait for `document.fonts.load()` on every weight used, then `document.fonts.ready`, then assert `document.fonts.check(font, 'Aàè€')`. Pass a text sample: without one, faces split by unicode-range report false. Plain `chrome --screenshot` doesn't wait and silently falls back to Arial.
- **QA false positives:**
  - Headings with line-height < 1.1 have `scrollHeight > clientHeight` because of descenders. Only check vertical overflow on body, lead and cards.
  - Count lines from text-node rects, not element rects: a highlight bar's padding made one line look like two.
  - Exclude cloned or magnified copies (`.glass` children) from object checks.
- **SVG filter on a horizontal line:** with the default `objectBoundingBox` units, a zero-height bounding box makes the blur disappear. Use `filterUnits="userSpaceOnUse"` with an explicit region. The engine's `#lineglow` does this.
- **Presentation attributes don't take `var()`.** Use `style="stroke:var(--line)"`, not `stroke="var(--line)"`.
- **`fetch()` doesn't work on `file://`.** Store any alignment data the page needs (for example the lens centre of a render) in `data-` attributes, not in a JSON the page fetches.
- **WebGL in headless Chrome:** launch with `--use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`. WebGL2 then works, and transmission is supported.
- **Transparent glass:** render once over black and once over white with `NoToneMapping`. Decode sRGB to linear, then α = 1 − mean(white − black) and colour = black / α. Downscale on premultiplied alpha (Lanczos), then crop to the alpha bounds.
- **Replicate tokens:** a valid token starts with `r8_` and is 40 characters long. The project's token was 32 characters with no `r8_` prefix, and `/v1/account` returned 401. Never guess, fix or print a token. Tell the user to create a new one at replicate.com/account/api-tokens. A file called `replicate.mcp.json` is *not* loaded by Claude Code: project MCP config must be `.mcp.json`, and it loads only at session start. The scripts don't need MCP anyway.
- **Emoji break shell heredocs.** A Bash heredoc that contained ✍️ and ⚠️ (emoji with a variation selector) failed to parse. Write `publish.json`, captions and any text with emoji through the Write tool, then run the scripts on the file.
- **Video mode measured nothing.** Hiding all slides before the engine measured them broke the glows and the QA. The engine now measures with every slide visible, and shows one slide at a time only when capture starts. Each video render uses its own temp folder, because a stopped run deleted a shared one mid-render.
- **Never use `export $(grep … .env | xargs)`.** When the file is missing, `export` with no arguments dumped the whole environment, including session tokens, into the log. Read the token with `process.env.REPLICATE_API_TOKEN` only, and load a `.env` with `node --env-file=.env` if needed.
- **Extruding an SVG logo in three.js** (Claude spark, 17 Oct 2026): flip SVG's downward y with `geo.rotateX(Math.PI)`, never `geo.scale(1, -1, 1)`. A negative scale turns the faces inside out and the object renders grey or black whatever its material. An opaque coloured material also needs a little `emissive` of its own colour, or the studio renders it dull brown. `render-3d.html` now loads `SVGLoader` for this (objects `spark`, `curve`).
- **Long official video in a slide** (Claude e la NSA, 17 Oct 2026): the owner asked for Anthropic's 5-minute animation in slide 3, "massimo 60 secondi", and the completo also ≤ 60 s instead of the whole file. Fix: two montages of the relevant scenes (47 s for the slide, 59.5 s for the completo), English subtitles cropped away, and `data-full` in `export-media.mjs` for the completo source. Before this the poster in `slide-XX.png` stayed in colour while the MP4 was mono: the poster now gets the same tone. See `build-guide.md` §11.
- **Instagram limits** (verified from Meta's API docs and guides):
  - caption and each comment: 2,200 characters;
  - alt text: 1,000 via the API, but keep it about 100–140 characters (guides recommend ≤ 125–256);
  - up to 3 pinned comments.

## 6. Working-style notes

- The user follows progress in Italian, and replies are short. Keep chat updates short and concrete, and lead with what's not done yet or what needs their action.
- Show visuals (a contact sheet, the cover, changed slides) instead of describing them.
- When the user corrects something small (logo, counter, a slide), change only that, re-export, show the changed slide, and confirm in one or two lines.
