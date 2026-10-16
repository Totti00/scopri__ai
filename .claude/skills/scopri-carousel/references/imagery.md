# Imagery

When to use images, how to make them consistent, and the three ways to produce them. Read it when planning hero slides.

## Contents
1. Decide first
2. One direction per carousel
3. Option A: the in-house 3D renderer (default for glass & chrome)
4. Option B: Replicate (only with a valid token)
5. Option C: code-built visuals (UI cards, CSS glass)
6. Placing an asset
7. Asset QA

---

## 1. Decide first

Use an image only where it makes the slide better: usually the **cover hero** and at most **one peak slide**, such as a statement on an ACCENT slide. Value slides full of copy (prompt cards, lists) get no imagery, because it would cost legibility. "Replicate is available" is never a reason to generate something.

Before producing anything, write down:
- which slides get an image and why;
- the family: C (interface fragments) is primary for Scopri AI; A (glass & chrome) for 1–2 heroes; B (monochrome cutouts) only if the topic needs people or real objects;
- one shared description: material, palette, lighting, camera, mood. Every asset in the carousel reuses it.

## 2. One direction per carousel

The direction that worked (first carousel: magnifier on the cover, hourglass on slide 2):

> A single [OBJECT] in clear glass with a faint electric-blue (#8595FF) tint and polished chrome details, electric-blue (#2340FF) glass or sand accents. High-end studio product render, key softbox from the top-left, vertical strip light on the right rim, light-grey gradient environment so the chrome reads silver. Isolated, transparent background, generous empty space. No text, no logos.

- Same studio, same materials and same light direction on every asset.
- If an object appears twice, reuse the same render, or the same builder with the same parameters.
- Check every asset on all three backgrounds (§7) before placing it.

## 3. Option A: the in-house 3D renderer (default for glass & chrome)

`assets/3d/render-3d.html` builds objects in three.js with physical materials: `chrome`, `glass`, `blueGlass`, `sand`, all lit by one studio environment. `render-assets.mjs` renders each object twice, over black and over white. Difference matting turns the two frames into a PNG whose glass is really transparent. Then a Lanczos downscale on premultiplied alpha and a crop to the object's bounds.

```bash
node .claude/skills/scopri-carousel/assets/3d/render-assets.mjs magnifier hourglass
```

The output goes to `assets/generated/<name>.png`, plus `<name>.json` (size, crop offset, and for the magnifier the lens centre).

**Library:**

| Object | Look | Notes |
|---|---|---|
| `magnifier` | chrome rim, glass lens, electric-blue grip at 30° | orthographic, face-on, 300 px rim at 1×. Use the JSON's `lensCenter` as `data-lens-x/y` to sit it over a `.lens` HTML zoom. |
| `hourglass` | glass bulbs, rounded chrome caps and posts, blue sand | perspective; worked at 82% scale on the ACCENT slide |

**Adding an object:**
1. Copy a builder in `OBJECTS`: keep the materials and the studio, change the geometry.
2. Size the canvas to the object, with about 10% margin.
3. Run the renderer, then the asset check (§7).

Good subjects for this audience: magnifier, padlock, key, pen nib, envelope, document stack, lightbulb, gauge, toggle, speech bubble, calendar, coin, shield, hourglass.

**Rules learned the hard way:**
- Chrome mirrors its surroundings. A dark studio makes black chrome, so keep the bright gradient dome and the big softboxes.
- Use `NoToneMapping`, or the matte stops being linear.
- Rounded edges (lathe profiles, torus rims) catch highlights. Flat faces read as grey plastic.
- WebGL in headless Chrome needs `--use-angle=swiftshader --enable-unsafe-swiftshader` (already set). Each render takes 4–7 s.

## 4. Option B: Replicate (only with a valid token)

Use it when a subject can't reasonably be built in 3D code, for example Family B photographic cutouts (hands, busts, hardware), and only if `REPLICATE_API_TOKEN` is set and valid.

```bash
node .claude/skills/scopri-carousel/scripts/replicate.mjs check
node .claude/skills/scopri-carousel/scripts/replicate.mjs schema black-forest-labs/flux-1.1-pro
node .claude/skills/scopri-carousel/scripts/replicate.mjs generate --name cover-key --prompt "<direction + subject>" --input '{"aspect_ratio":"4:5","output_format":"png"}' --remove-bg
```

- **`check`:** run it first. A valid token starts with `r8_` and is about 40 characters. A 401 means the token is invalid. Tell the user to create a new one at replicate.com/account/api-tokens. Don't try to fix, guess or print it.
- **`schema`:** model names and inputs change over time. List a model's input fields before using it. Pass the model's own parameter names via `--input`.
- **Prompts:** use the design-system templates (§7.2 Family A or B) with the shared direction from §2. Keep every prompt in a carousel identical except for the subject. Say "no text, no logos".
- **Background:** `--remove-bg` runs a background-removal model (default `851-labs/background-remover`; change it with `--bg-model` and `--bg-key`). Glass and translucent subjects cut badly. Prefer Option A for those.
- **Reject and regenerate** anything that breaks the direction: wrong light, a second hue, clutter, a cartoon look, halos.
- The script reads the token from the environment only, and writes the raw output, the cutout and a provenance JSON to `assets/generated/`. Never hardcode or echo the token. Never `export $(cat .env)`; use `node --env-file=.env …`.

## 5. Option C: code-built visuals (UI cards, CSS glass)

These are the primary family for AI topics: chat-composer cards, redacted documents with accent bars and a "Dati oscurati" sticker, contract cards with fine print, flow nodes. They are crisp, editable and on-brand. `.glassobj` (frosted CSS shapes) is the quick fallback when a 3D render isn't worth it.

## 6. Placing an asset

- The hero takes 35–60% of the canvas height and often bleeds off one edge (10–30%), never off the top on text-top slides.
- Keep it in the quadrant opposite the text (diagonal balance), clear of every text line by at least 40 px, and outside the frame clear zones.
- DARK and ACCENT slides: put a `.glow[data-for="#asset"]` behind the asset. LIGHT slides: use a contact shadow and no colored glow.
- The thread may run under the object as its "floor", with a gap of 20 px or more (QA buffer).
- Scale in CSS (width and height) rather than re-rendering. Scaling down to about 80% stays sharp.
- Assets live in `assets/generated/`. Reference them from a carousel as `../../assets/generated/<name>.png`.

## 7. Asset QA

```bash
python .claude/skills/scopri-carousel/scripts/asset-check.py assets/generated/<name>.png
```

This composites the asset on the DARK, ACCENT and LIGHT backgrounds into `<name>-check.png`. Read that image and check:

- clean edges, no halos;
- glass shows the background through it;
- chrome reads silver;
- same light direction and palette as the other assets;
- nothing looks pasted on.

Then check it in place on the exported slide.
