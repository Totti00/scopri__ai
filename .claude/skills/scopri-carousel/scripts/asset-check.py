"""Composite transparent assets on the three Electric Mono background modes (DARK, ACCENT, LIGHT)
so edges, transparency and light direction can be judged before placing them on a slide.
Usage: python asset-check.py <asset.png> [more.png ...]   → writes <asset>-check.png next to each file"""
import sys
from pathlib import Path

from PIL import Image

BGS = [(10, 10, 13), (35, 64, 255), (242, 242, 245)]   # ink-950 · accent-500 · paper-100

for arg in sys.argv[1:]:
    p = Path(arg)
    im = Image.open(p).convert('RGBA')
    pad = 24
    w, h = im.width + 2 * pad, im.height + 2 * pad
    sheet = Image.new('RGB', (w * 3, h))
    for i, c in enumerate(BGS):
        tile = Image.new('RGBA', (w, h), c + (255,))
        tile.alpha_composite(im, (pad, pad))
        sheet.paste(tile.convert('RGB'), (w * i, 0))
    out = p.with_name(p.stem + '-check.png')
    sheet.save(out)
    semi = sum(im.getchannel('A').histogram()[1:255]) / (im.width * im.height)
    print(f'{out}  ({im.width}x{im.height}, {semi:.0%} semi-transparent pixels)')
