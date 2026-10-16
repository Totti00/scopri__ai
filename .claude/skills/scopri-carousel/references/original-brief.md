# Original carousel brief (baseline)

This is the prompt that started the first Scopri AI carousel ("5 prompt per capire bolletta e contratti prima di firmare", October 2026), kept word for word. The skill carries it forward. Where later decisions changed or sharpened a rule, `brand-scopri-ai.md` and `lessons-learned.md` say so, and they win.

The first carousel's values were:
- BRAND NAME: Scopri AI
- TOPIC: 5 prompt per capire bolletta e contratti prima di firmare
- CAROUSEL TYPE: STATIC
- Language: Italian ("In italian!")

---

BRAND NAME: [brand]

TOPIC: [topic]

CAROUSEL TYPE: [STATIC | ANIMATED | blank]

I want you to create an Instagram carousel for the brand and topic above.

Use `design-system.md` as the source of truth for all visual decisions.

Use `carousel-copy.md` as the default guide for the writing, hook, structure, slide density, flow, CTA and caption where relevant.

FIRST ACTION - STATIC OR ANIMATED

If CAROUSEL TYPE is blank, ask me whether I want a static or animated carousel before doing anything else.

Do not research, write the copy or start designing until I answer.

If CAROUSEL TYPE is already specified, do not ask again.

CONTENT WORKFLOW

1. Understand the topic and the main point the carousel should communicate.
2. If I attached or provided source material, use that as the primary source.
3. If I did not provide enough source material, research the topic before writing the carousel.
4. Create the proposed carousel copy before designing anything.
5. Show me the copy slide by slide.
6. Keep each slide focused on one main idea where possible.
7. Use the number of slides the content actually needs. Do not force a fixed slide count.
8. Keep the copy concise enough to work visually.
9. Do not generate the finished carousel until I approve the copy or tell you to continue.

CAROUSEL FORMAT

Every slide must use an exact 1080 x 1350 px canvas with a 4:5 aspect ratio.

Build the carousel as self-contained HTML/CSS/JavaScript designed specifically for accurate export at 1080 x 1350.

Never treat the browser viewport as the slide size.

Every slide must have its own fixed 1080 x 1350 export container.

Keep all important content inside safe margins.

Nothing should clip, overflow or overlap unintentionally.

Any development controls, slide selectors, export controls or navigation must sit outside the exportable slide area.

Use real HTML text whenever possible rather than generating text inside an image.

DESIGN

Follow `design-system.md` closely for typography, colors, spacing, hierarchy, imagery, graphic elements and composition.

Do not invent a completely different visual style.

The full carousel must feel like one visual system from beginning to end.

Maintain consistency in typography, color treatment, image style, visual weight, spacing, lighting, illustration style, effects and graphic treatment.

Slides do not need to use the exact same layout.

Vary layouts where useful, but keep the visual language consistent.

Prioritize readability.

Do not squeeze too much copy onto a slide.

Split content across more slides when needed.

Avoid generic AI-looking gradients, cards, icons, effects or decorative elements unless they fit the design system.

IMAGE GENERATION

If Replicate is configured in this project, you may use it to generate visual assets when those assets genuinely improve the carousel.

Do not generate images simply because the API is available.

Before generating the first asset, study `design-system.md` and decide on one image direction for this carousel.

Keep generated imagery consistent across every slide.

Maintain the same visual characteristics where relevant:

- art or photography style
- palette
- lighting
- contrast
- texture
- level of realism
- perspective
- rendering style
- subject treatment
- edge treatment
- overall mood

Do not mix noticeably different image styles inside the same carousel.

Do not use an asset if it looks visually disconnected from the rest of the design.

Regenerate or edit it instead.

When generating multiple related assets, reuse the same core visual description so they feel like they belong to the same set.

If the same person, character, object or product appears more than once, preserve its appearance as closely as the available model allows.

Generated assets should support the composition rather than fight with the text.

When useful, generate images with suitable empty space or positioning for the intended slide layout.

Avoid generating important written copy inside images.

Keep important text as real HTML text.

For standalone visual elements such as people, products, objects or illustrations, remove the background before placing them on the slide unless the background is intentionally part of the design.

Use a transparent PNG for those cutout assets.

If the generation model does not provide a clean transparent background, use a Replicate background-removal model before placing the asset on the slide.

Save generated assets inside `assets/generated/` with clear filenames.

STATIC OR ANIMATED

For a STATIC carousel:

Create the finished carousel in HTML and make every slide individually exportable as a 1080 x 1350 PNG.

The HTML version and exported PNG should look the same.

For an ANIMATED carousel:

Use HTML/CSS/JavaScript with tasteful motion that supports the design.

Keep animation subtle and polished.

Avoid excessive bouncing, spinning or movement on every element.

All important text should become readable quickly.

Each slide must remain exactly 1080 x 1350 and be suitable for rendering as an individual MP4.

REVIEW

Before presenting the finished carousel, check:

- every slide is exactly 1080 x 1350
- typography follows `design-system.md`
- no elements are clipped or overflowing
- all text is readable
- spacing is consistent
- visual style remains consistent from the first slide to the last
- generated images match the brand and the rest of the carousel
- generated image styles do not clash with one another
- cutout assets have clean transparent backgrounds where required
- no generated image looks obviously pasted in or disconnected from the design
- no development or navigation UI appears inside the exported slides

After the carousel type is confirmed, research if necessary and then show me the proposed carousel copy only.

Wait for me to approve it or ask for revisions.

Only after I approve the copy should the carousel creation and design process begin.
