"""Writes the publishing texts as separate .txt files and checks Instagram's limits.
Input:  <carousel-dir>/publish.json  {"caption": "...", "alt": ["slide 1", ...], "pinned": ["comment 1", ...]}
Output: <carousel-dir>/pubblicazione/01-caption.txt, 02-alt-text-slide-XX.txt, 03-commento-fissato-N.txt
Usage:  python publish-pack.py <carousel-dir>"""
import json
import re
import sys
from pathlib import Path

LIMIT = 2200            # caption and each comment
ALT_SOFT = 140          # what worked; guides say ≤125–256, the API allows 1,000

base = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
data = json.loads((base / 'publish.json').read_text(encoding='utf-8'))
caption, alts, pinned = data['caption'].strip(), [a.strip() for a in data['alt']], [p.strip() for p in data.get('pinned', [])]
errors, warns = [], []

n_slides = len(list((base / 'exports').glob('slide-*.png')))
if n_slides and len(alts) != n_slides:
    errors.append(f'{len(alts)} alt texts for {n_slides} slides')
if len(caption) > LIMIT:
    errors.append(f'caption is {len(caption)} characters (limit {LIMIT})')
tags = re.findall(r'(?<!\w)#\w+', caption)
if not 3 <= len(tags) <= 5:
    warns.append(f'{len(tags)} hashtags (guide: 3–5)')
for i, p in enumerate(pinned, 1):
    if len(p) > LIMIT:
        errors.append(f'pinned comment {i} is {len(p)} characters (limit {LIMIT})')
if len(pinned) > 3:
    errors.append(f'{len(pinned)} pinned comments (Instagram pins at most 3)')
for i, a in enumerate(alts, 1):
    if len(a) > ALT_SOFT:
        warns.append(f'alt text {i} is {len(a)} characters (aim ≤ {ALT_SOFT})')

if errors:
    sys.exit('Not written:\n  ' + '\n  '.join(errors))
out = base / 'pubblicazione'
out.mkdir(exist_ok=True)
for old in out.glob('*.txt'):
    old.unlink()
files = {'01-caption.txt': caption}
files.update({f'02-alt-text-slide-{i:02d}.txt': a for i, a in enumerate(alts, 1)})
files.update({f'03-commento-fissato-{i}.txt': p for i, p in enumerate(pinned, 1)})
for name, text in files.items():
    (out / name).write_text(text + '\n', encoding='utf-8', newline='\n')
    print(f'{name:30s} {len(text):5d} caratteri')
print(f'\nFirst 125 characters of the caption (shown before "altro"):\n  {caption[:125]}')
for w in warns:
    print('warning:', w)
