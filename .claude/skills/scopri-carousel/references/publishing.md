# Publishing pack

Every finished carousel ships with its caption, alt texts and (when needed) pinned comments, as separate `.txt` files. Deliver them without being asked: the user had to ask for them on the first carousel.

## Contents
1. publish.json
2. Caption
3. Pinned comments
4. Alt text
5. Final message

---

## 1. publish.json

Write `carousels/<slug>/publish.json`:

```json
{
  "caption": "…",
  "alt": ["slide 1 alt", "slide 2 alt", "…"],
  "pinned": ["comment 1", "comment 2"]
}
```

Then, from the carousel folder:

```bash
npm run publish
```

This writes `pubblicazione/01-caption.txt`, `02-alt-text-slide-XX.txt` (one per slide) and `03-commento-fissato-N.txt`, each holding only the text to paste. It also checks:
- the caption and each comment are ≤ 2,200 characters;
- there is one alt text per exported slide;
- there are ≤ 3 pinned comments;
- 3–5 hashtags;
- alt texts are ≤ 140 characters.

## 2. Caption

Italian, following `carousel-copy.md` §9, plus the Scopri AI habits:

- **The first ~125 characters are the hook.** It complements slide 1 without repeating it, and ends with 👇.
- **Emoji:** about one per block, at the start of a line (🧠 📌 💬 🔒 ✍️ 📅 ⚠️ 🔖 style). The user asked for them.
- **Body:** the context the slides don't hold, such as why it works, how to use it, practical tips and verified facts with their limits.
- **One honesty line about AI**, e.g. "⚠️ L'AI spiega, ma può sbagliare. Verifica sempre…".
- **The CTA repeated at the end**, the same single ask as the closing slide (usually "🔖 Salva il post: ti servirà…").
- **3–5 specific hashtags** at the very end.
- Natural search keywords the audience would type, in plain Italian.

## 3. Pinned comments

Use them when the carousel's useful content is longer than the caption allows, typically full prompts.

- Split the content across up to 3 comments, each ≤ 2,200 characters. Give each a header line ("I 5 prompt da copiare · parte 1/2"), then the items with their titles.
- No emoji inside prompts, because people paste them straight into an AI.
- The caption must point to them ("Copiali dai commenti fissati qui sotto…"). Mention screenshot text-copy as a fallback: on most phones you can copy text straight from an image.

## 4. Alt text

One per slide, Italian, about 120–140 characters. Formula:

> [role or label]: «headline». [what the visual shows, if it carries meaning]. [pointer, if the full text lives elsewhere]

Examples from the first carousel:
- Cover: «5 prompt prima di firmare». Una lente d'ingrandimento mette a fuoco la clausola «Alla scadenza» di un contratto luce.
- Prompt 1, «Traduci la bolletta»: l'AI spiega ogni voce di spesa e il costo reale per kWh. Testo completo nei commenti fissati.
- Logo Scopri AI. «Salvalo per la prossima offerta. L'AI ti spiega il contratto. La firma, però, resta tua.» Pulsante Salva.

Tell the user where to enter it. Before sharing, open *Impostazioni avanzate* → *Accessibilità* → *Scrivi testo alternativo*, one entry per image. The path may vary slightly between app versions.

## 5. Final message

Write it in Italian and keep it short. Include:

1. **What's ready**, with links: `exports/` (PNG/MP4), `pubblicazione/`, and the contact sheet sent as an image.
2. **What still needs the user**, if anything (a missing fact, an asset to confirm). Lead with this.
3. **Design-system deviations**, if any, in one short list.
4. **Sources**, if research was done, as markdown links.
