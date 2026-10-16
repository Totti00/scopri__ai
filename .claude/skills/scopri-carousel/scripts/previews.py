"""Review images for a carousel's exports/: a 3-column contact sheet, the edge-to-edge strip (seam check)
and the cover at 360 px wide (profile-grid thumbnail test, design-system.md §11.5).
Usage: python previews.py <carousel-dir>"""
import sys
from pathlib import Path

from PIL import Image

exp = Path(sys.argv[1] if len(sys.argv) > 1 else '.') / 'exports'
slides = sorted(p for p in exp.glob('slide-*.png'))
if not slides:
    sys.exit(f'No slide PNGs in {exp}: run npm run export first')
ims = [Image.open(p).convert('RGB') for p in slides]
bad = [p.name for p, im in zip(slides, ims) if im.size != (1080, 1350)]
if bad:
    sys.exit(f'Not 1080x1350: {", ".join(bad)}')

cols, tw, th = 3, 540, 675
rows = -(-len(ims) // cols)
sheet = Image.new('RGB', (cols * tw, rows * th), 'white')
for i, im in enumerate(ims):
    sheet.paste(im.resize((tw, th), Image.LANCZOS), ((i % cols) * tw, (i // cols) * th))
sheet.save(exp / 'contact-sheet.jpg', quality=90)

strip = Image.new('RGB', (1080 * len(ims), 1350))
for i, im in enumerate(ims):
    strip.paste(im, (1080 * i, 0))
strip.resize((270 * len(ims), 338), Image.LANCZOS).save(exp / 'strip-preview.jpg', quality=90)

ims[0].resize((360, 450), Image.LANCZOS).save(exp / 'cover-360.png')
print(f'{len(ims)} slides OK · contact-sheet.jpg · strip-preview.jpg · cover-360.png in {exp}')
