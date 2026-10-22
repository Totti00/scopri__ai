"""Writes the publishing texts as separate .txt files and checks Instagram's limits.
Input:  <carousel-dir>/publish.json  {"caption": "...", "alt": ["slide 1", ...], "pinned": ["comment 1", ...],
                                     "tipo": "notizia|curiosita|prompt|lista|serie", "parole": ["gemini", "google"]}
        (tipo: optional, default from the folder name; parole: what people search, checked in the first 125 characters)
Output: <carousel-dir>/pubblicazione/01-caption.txt, 02-testi-alternativi.txt (all slides in one file, numbered), 03-commento-fissato-N.txt
The caption (and caption-reel.txt, when present) goes through caption_check.py, the Scopri AI caption rules:
an error there stops the pack. Ends with the "CAPTION PRONTA" receipt(s) for the final message.
Usage:  python publish-pack.py <carousel-dir>"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import caption_check as cc  # noqa: E402

try:
    sys.stdout.reconfigure(encoding='utf-8')   # Windows console and emoji
except AttributeError:
    pass

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
tipo = data.get('tipo') or cc.tipo_da_cartella(base.resolve().name)
parole = data.get('parole', [])
stile = data.get('stile', 'carosello')   # 'tweet' = format/6-stile-tweet.md
checks = [('caption del carosello', cc.check(caption, tipo, 'carosello', parole, stile))]
reel = base / 'caption-reel.txt'
if reel.exists():
    checks.append(('caption-reel.txt', cc.check(reel.read_text(encoding='utf-8'), tipo, 'reel', parole, stile)))
for name, r in checks:
    print(f'— {name} —\n{cc.render(r)}\n')
    errors += [f"{name}: {c['controllo']}: {c['messaggio']}" for c in r['controlli'] if c['esito'] == 'errore']
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
# one file with every alt text, labelled by slide number (owner, 20 Oct 2026)
if alts:
    files['02-testi-alternativi.txt'] = '\n\n'.join(f'Slide {i}\n{a}' for i, a in enumerate(alts, 1))
files.update({f'03-commento-fissato-{i}.txt': p for i, p in enumerate(pinned, 1)})
for name, text in files.items():
    (out / name).write_text(text + '\n', encoding='utf-8', newline='\n')
    print(f'{name:30s} {len(text):5d} caratteri')
for w in warns:
    print('warning:', w)
print()
for name, r in checks:
    print(cc.ricevuta(r))
