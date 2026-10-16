# Animated carousels

Read this only when the user chose **animated**. The slides are the same as a static carousel. The engine adds one shared motion language, and `export-video.mjs` renders each slide to its own MP4.

## Contents
1. Principles
2. The default choreography
3. Overrides
4. Export to MP4
5. Review

---

## 1. Principles

From the original brief and the design system:
- Motion supports the design: subtle and polished, no bouncing, spinning or movement on every element.
- **All important text becomes readable quickly.** Every text element must be fully in place by about 1.3 s. QA fails anything later than 1.6 s.
- The final frame is the static design. Each slide holds still long enough to read: about 3.5 s after the entrance.
- Every slide stays exactly 1080 × 1350, and each slide is its own MP4.
- All animated carousels move the same way. That consistency is part of the brand, so use the shared choreography instead of inventing new motion per carousel.

## 2. The default choreography

The engine applies it automatically when `CAROUSEL.format = 'animated'`. The ease is `cubic-bezier(.2,.7,.2,1)` throughout.

| Element | Motion | Delay | Duration |
|---|---|---|---|
| ghost type, super-shape, patterns | fade | 0 | 1200 ms |
| glow | fade, then a slow "breathe" (opacity .82 ↔ 1, 5 s) | 150 ms | 1200 ms |
| pill | rise (28 px + fade) | 0 | 650 ms |
| display / H1 / H2 / numeral | rise | 120 ms | 700 ms |
| lead / body / chip | rise | 320 ms | 650 ms |
| cards, prompt card, glass object, asset, CTA pill, logo | scale .96 → 1 + fade | 460 ms | 750 ms |
| lens + its rendered rim | fade (they must stay aligned) | 460 ms | 750 ms |
| list rows | rise, staggered 90 ms | 520 ms | 600 ms |
| thread line | draws in | 600 ms | 1000 ms |
| thread nodes | fade | 1500 ms | 300 ms |
| assets and glass objects (after entering) | float 8 px, 6 s, alternate | after entrance | loop |

The frame (logo, counter, handle, swipe cue) and the grain stay static.

The default slide length is **5 s**. Set `data-duration="6000"` on a `.slide` for denser slides, such as prompt cards, which need about 7 s. Keep every slide between 4 and 8 s.

## 3. Overrides

- `data-anim="none"` on an element keeps it static.
- `data-anim="fade|rise|scale|float"` changes its motion; `data-delay="ms"` changes its delay.
- Don't add other animation styles. If a carousel really needs a new motion, add it to the engine, so it becomes part of the shared language, and say so.

## 4. Export to MP4

From the carousel folder:

```bash
npm run export
npm run export:video
```

- `npm run export` writes static PNGs of the final state (used for the contact sheet and as fallbacks).
- `npm run export:video` writes `exports/slide-XX.mp4` plus a poster PNG of the last frame.
- Rendering is deterministic. Every animation is paused and seeked frame by frame (30 fps, change it with `FPS`), screenshotted, and encoded with ffmpeg: H.264, yuv420p, CRF 18, faststart.
- It takes about 15–25 s per slide.
- ffmpeg comes from the PATH or from `ffmpeg-static`, which the scaffold installs at the project root for animated carousels. You can also set `FFMPEG_PATH`.
- On Instagram, each MP4 is one carousel item (4:5, 1080 × 1350). Video and image items can be mixed.

## 5. Review

- Run `npm run previews` on the static export and review it as for a static carousel.
- In the browser preview, use **Riproduci animazioni** to replay the motion.
- For a frame-accurate check, run `FPS=10 npm run export:video` for a quick low-fps pass, then the full render.
- Check that:
  - nothing pops or flickers;
  - text is never covered by a moving object;
  - the lens and its rim stay aligned;
  - the thread draws in the reading direction.
