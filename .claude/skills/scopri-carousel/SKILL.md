---
name: scopri-carousel
description: Creates Scopri AI Instagram carousels end to end. It writes the copy, iterates on it until approved, then builds 1080×1350 slides in the Electric Mono design system with the Scopri AI brand (Coperchio logo, brand blue, @scopri__ai). It exports PNGs or per-slide MP4s and delivers caption, alt text and pinned comments as separate .txt files. Use this skill whenever the user asks for a carousel, a carosello, a swipe post, Instagram slides, or to turn a topic, transcript, article, notes or file into slides, even from a one-line request like "fai un carosello su 7 modi per usare Codex" or "turn this file into a static carousel". Also use it to revise, restyle or re-export an existing carousel in carousels/.
---

# Scopri AI carousel

This skill makes carousels the way the first one was made ("5 prompt prima di firmare", Oct 2026), including every correction the user gave along the way. It keeps a fixed order: **format → sources/research → copy → approval loop → build → QA → publishing pack**. The two gates (format first, copy approval before building) exist because the user wants to steer the content before any design time is spent.

**Precedence when files disagree:**
1. `references/brand-scopri-ai.md` (brand decisions)
2. `references/lessons-learned.md` (feedback and fixes)
3. `references/design-system.md` (visual system)
4. `references/carousel-copy.md` (writing guide)
5. `references/original-brief.md` (baseline brief)

The skill's `references/design-system.md` is a copy of the project's file with a contents line added. Before building, compare the two sections (`diff` ignoring that header). If the project file has changed, it wins: the user updated it.

Write slides, caption and alt text in **Italian** even when the request is written in English, because Scopri AI's audience is Italian. Use another language only if the user names one. Say "Copy in italiano" at the top of the copy message, so an English-speaking user can redirect early. Talk to the user in the language they write in.

## Step 0: Read the request

Pull out:
- the topic or angle;
- extra instructions (audience, tone, slide count, CTA);
- any source material (files, pasted text, links);
- the format, if stated.

Treat static as stated when the user says static, statico, PNG, immagini or foto. Treat animated as stated when they say animated, animato, video, MP4 or motion.

## Step 1: Format gate

If the format isn't stated, ask this before anything else, and stop until the user answers:

> Vuoi un carosello **statico** o **animato**?

(Use "Should this be a **static** or **animated** carousel?" if the user writes in English.)

- Nothing needs to be read before this question, and nothing else goes in the message. If your interface offers reply buttons, use two complete ones: "Statico" and "Animato".
- Don't research, outline or write copy before the answer: the user asked for this order explicitly.
- If the format is already stated, don't ask again.

## Step 2: Sources and research

- **Source material supplied:** read all of it. It is the primary source. Don't research what it already covers. Research only gaps the user asked to fill, or facts that need checking because they may be outdated.
- **Topic only:** research whenever the copy needs facts, current features, laws, prices or numbers. Use official sources first (product docs, authorities). AI tools change fast, so check features against their docs as of today's date.
- **Never invent facts, numbers, quotes or testimonials.** If a number isn't available, use a concrete situation instead.
- Qualify legal and financial claims precisely: who it applies to, and from when. Don't attribute advice to an authority you didn't verify. Keep carousels evergreen: avoid dated news unless asked.
- **Defaults that change** (a product's default mode, a shortcut, a price): describe what to do, not version history. Avoid version numbers and "novità" framing, and note the date-sensitive points in *Note sui contenuti* so the user can judge.
- Keep a list of the sources you used. It goes at the end of the copy message.

## Step 3: Draft the copy

Read `references/carousel-copy.md`, `references/brand-scopri-ai.md` §1, `references/lessons-learned.md` §1 and `references/publishing.md` §2 (caption habits) first. Then:

1. Define the carousel in one sentence: who it's for, what they get, the one action.
2. Pick a framework (copy guide §6). Outline the value slides, with the strongest point early.
3. Write 5–10 hooks and run them through the hook test (copy guide §3.2). Pick one and keep 2–3 alternatives. The **cover headline holds ≤ 6 words**, about 13 characters per line, 3 lines (design-system §11.5). The copy guide's "≤ 12 words" is the cover's total budget, headline plus sottotitolo (≤ 8 words).
4. Write slide 2 as a standalone second hook.
5. Keep density within copy guide §2: one idea per slide; split, don't cram.
6. Let the content decide the slide count, usually 7–10. Include the closing slide, which is not counted in the progress counter.
   - **A number in the request is a promise.** "7 tips" means exactly 7 value slides, one per tip, plus cover, optional re-hook and closing slide: about 9–10 slides. If 7 don't fit the material, say so instead of silently changing the number.
7. Don't add meta slides ("perché funziona", "come usare questo carosello") unless the content needs them. The user removed one.
   - A **recap/checklist slide** is different: it's the most save-worthy slide for long listicles and step-by-steps. Don't add it by default. Offer it in *Note sui contenuti* ("vuoi una checklist finale da salvare?"), and include it straight away only for checklist or cheat-sheet carousels.
   - **Technical topics** (Claude Code, Codex, terminals, git): the audience is non-programmers. Explain every technical term in plain Italian the first time ("il «contesto», cioè…"), prefer what to do over how it works, and leave advanced features out unless asked.
8. End with **one** CTA, usually Salva, tied to the value ("Salvalo per la prossima offerta"). The closing slide then adds the smaller 🔔 follow line, and the caption the `🔔 Seguici per non perdere …` line (not in *serie*; `brand-scopri-ai.md` §5).
9. Include one honest line that the AI can be wrong and the reader should check (caption or CTA lead).
10. **Prompt carousels:** each prompt is a complete, working ~100-word prompt: role → context (what's attached, personal data hidden) → 3–4 numbered tasks → output rules with an anti-hallucination clause. Mark the parts to replace with `[parentesi quadre]`. Plan pinned comments, because full prompts don't fit in a caption. See `lessons-learned.md` §1.
11. Draft the caption: hook in the first 125 characters, emoji at the start of blocks, context, CTA repeated, 3–5 hashtags. In Scopri AI `npm run publish` checks it with `scripts/caption_check.py` (see `references/publishing.md`).

**Present it in this shape, then stop and wait:**

```markdown
_Copy in italiano · formato: statico · 8 slide + chiusura (il contatore va da 01/08 a 08/08)_

**In una frase:** who it's for, what they get, the one action · **Struttura:** framework (copy guide §6)

### 01 — Copertina
- **Pill:** …
- **Titolo:** … (accento: «…»)
- **Sottotitolo:** …

### 02 — …
- **Pill:** … · **Titolo:** … (*corsivo* = parte in accento o in grigio) · **Testo:** …
- Add the fields the layout needs: **Rimedio**, **Esempio (card)**, **Prompt**, **Visual**
…
### NN — Chiusura
- **Titolo:** … · **Testo:** … · **Pulsante:** SALVA

### Caption
> …

**Hook alternativi:** … · … · …
**Note sui contenuti:** claims I qualified or left out (one line each)
Fonti: [titolo](url) …
```

End the message by asking for approval or changes, in an open sentence; complete buttons ("Approva il copy") are fine if your interface offers them. **Never offer reply buttons whose text ends with ":" or needs typing to complete.** Twice the user clicked one and sent an empty request. Buttons must be complete messages ("Approva il copy", "Riscrivi l'hook").

## Step 4: Revision loop

- Apply exactly what the user asked:
  - rewrite single slides;
  - regenerate everything;
  - change the hook or angle;
  - add or remove slides;
  - merge their own edits.
- Show the revised copy. Changed slides go in full; unchanged slides can be listed in one line. Mention any knock-on effects, such as slide counts or caption length.
- A clear positive statement ("va bene", "approvato", "il resto va benissimo") approves everything not mentioned. Apply the requested tweaks and move on. Don't ask for approval again.
- Skip the approval stage only if the user explicitly says so.

## Step 5: Build (only after approval)

Read `references/build-guide.md`. Then:

1. **Scaffold** from the project root:

   ```bash
   node .claude/skills/scopri-carousel/scripts/new-carousel.mjs <slug> --title "…" --format static|animated
   ```

   It creates `carousels/<slug>/` (engine, layout library, Coperchio logos, export scripts) and installs the shared deps once at the root. Save the approved copy to `copy.md`.

2. **Plan the slides** in a table: mode, template, hero, thread in → out. Follow the mode sequences, the template rhythm and the accent budget (`build-guide.md` §3). The cover and the closing slide are DARK.

3. **Imagery.** Decide per slide whether an image helps (`references/imagery.md`). The default is code-built interface cards, plus 1–2 glass & chrome heroes rendered in-house:

   ```bash
   node .claude/skills/scopri-carousel/assets/3d/render-assets.mjs <object>
   ```

   Use Replicate only if `REPLICATE_API_TOKEN` is set and valid (`scripts/replicate.mjs check`), and only when the subject really needs a generative model. Read the token from the environment only; never print or hardcode it.

   If Replicate isn't configured, continue without AI-generated images. Code-built visuals and in-house 3D renders are part of the design toolkit, and the user asked for them on the first carousel. If the user explicitly asks for AI-generated imagery and there's no valid token, explain how to set one up (`imagery.md` §4) instead of failing silently.

   Check every asset on all three backgrounds with `scripts/asset-check.py` before placing it.

4. **Write the slides** in `index.html` from the layout library. No pill on the cover, no handle (the engine no longer prints it), no stickers or labels over images or cards, no comment captions: the only captions are comparison ones under the images of a before/after, «Prima: …» / «Dopo: …» with 1–3 words on what changes, `<p class="cap" data-under="#id">Prima: pubblicità</p>` (20 Oct 2026). Set `tipo` in `CAROUSEL` (the scaffold does it from the slug). Replace all sample copy, mark text with `qa-text`, and pin headline line counts with `data-lines`. Set `CAROUSEL.seams/routes` for the thread. Keep slide-specific CSS in the page's `<style>`, not in `engine/`.

5. **Export and check**, from `carousels/<slug>/`:

   ```bash
   npm run export
   npm run previews
   ```

   Fix every QA error. Then **look at the images yourself**: the contact sheet, the strip, `cover-360.png`, and individual slides wherever something might be off. Use the review list in `build-guide.md` §8. Re-export until clean.

6. **Animated carousels:** read `references/animation.md`. The engine applies the shared choreography. Then run `npm run export:video` (one MP4 per slide, plus poster PNGs).

7. **Publishing pack** (`references/publishing.md`): write `publish.json` with the caption, one alt text per slide and any pinned comments, then run `npm run publish`. Deliver it without being asked.

8. **Final message** (Italian, short):
   - links to `exports/` and `pubblicazione/`;
   - the contact sheet sent as an image;
   - anything still needing the user, first;
   - design-system deviations in one short list;
   - sources.

## Revisions after the build

Modify the existing carousel instead of rebuilding it. Preserve what works. Change only what was asked, re-export, re-run the previews, and show the changed slides. Keep `copy.md` and `publish.json` in sync.

If the feedback is a rule for every future carousel (a brand, frame or copy habit), also update `references/brand-scopri-ai.md` or `references/lessons-learned.md`, and the engine if it's visual. Tell the user it now applies going forward.

## Reference map

| File | Read when |
|---|---|
| `references/brand-scopri-ai.md` | always: before copy and before build |
| `references/lessons-learned.md` | before copy and before build (feedback, fixed mistakes, technical traps) |
| `references/carousel-copy.md` | writing or revising copy |
| `references/design-system.md` | designing slides (§2–§11), final QA (§14) |
| `references/build-guide.md` | building, exporting, reviewing |
| `references/imagery.md` | any slide that may get an image |
| `references/animation.md` | animated carousels only |
| `references/publishing.md` | caption, alt text, pinned comments, final message |
| `references/original-brief.md` | the baseline brief this skill grew from |
| `examples/bollette-contratti/` | worked example: approved copy, caption, alt text, pinned comments, contact sheet |

## Bundled tools

| Path | What it does |
|---|---|
| `scripts/new-carousel.mjs` | scaffold `carousels/<slug>/`, copy the logo kit, install shared deps |
| `assets/template/` | `index.html` layout library + `engine/` (CSS/JS: frame, thread, glows, lens, motion, QA) + `export.mjs` + `export-video.mjs` |
| `scripts/previews.py` | contact sheet, strip (seam check), cover at 360 px |
| `scripts/publish-pack.py` | `publish.json` → `pubblicazione/*.txt` with Instagram limit checks and the caption check |
| `scripts/caption_check.py` | Scopri AI caption rules (Italian), carousel or Reel; prints the "CAPTION PRONTA" receipt |
| `assets/3d/` | three.js glass & chrome renderer (magnifier, hourglass, add more) → transparent PNGs |
| `scripts/asset-check.py` | composite assets on DARK / ACCENT / LIGHT for review |
| `scripts/replicate.mjs` | optional Replicate generation + background removal (token from env only) |
| `assets/brand/` | fallback copy of the Coperchio logo kit |

Requirements: Node 18+, Python 3 with Pillow and numpy, Google Chrome (or set `CHROME_PATH`), and an internet connection for Google Fonts and three.js.

## In the Scopri AI repository (Totti00/scopri__ai)

The team's `costruttore-post` agent drives this skill from the scheduled routines (`.claude/agents/costruttore-post.md`, `routine/README.md`). There, the project's `CLAUDE.md` rules come first: no format gate (static by default; slides with a real video become MP4 via `npm run media`, `build-guide.md` §11), news rubrics follow CLAUDE.md (2 sources, real photos and videos, sources only in the caption) instead of "keep it evergreen", and the two owner stops are the menu and the copy + static draft. The alternative covers are still made with the draft (owner confirmed, 20 Oct 2026); the engine adds «SCORRI PER SCOPRIRE» to the cover (`brand-scopri-ai.md` §4). In the cloud the scripts find Chromium at `/opt/pw-browsers/chromium` and add `--no-sandbox` when running as root.
