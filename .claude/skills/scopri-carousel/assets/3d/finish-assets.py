"""Usage: python finish-assets.py <assets/generated> [asset ...]
Finish the supersampled renders: premultiplied Lanczos downscale, crop to the alpha bounds,
save the transparent PNG plus a JSON with the crop offset (used to align the magnifier lens)."""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image

out_dir = Path(sys.argv[1])
raw_dir = out_dir / 'raw'
only = set(sys.argv[2:])          # optional: asset names to finish (default: all raw renders)

for meta_file in sorted(raw_dir.glob('*.meta.json')):
    name = meta_file.name.split('.')[0]
    if only and name not in only:
        continue
    meta = json.loads(meta_file.read_text())
    ss = meta['ss']
    im = np.asarray(Image.open(raw_dir / f'{name}@{ss}x.png').convert('RGBA'), dtype=np.float32) / 255
    a = im[..., 3:4]
    premult = np.concatenate([im[..., :3] * a, a], axis=-1)
    h, w = premult.shape[:2]
    small = np.stack([
        np.asarray(Image.fromarray(premult[..., c]).resize((round(w / ss), round(h / ss)), Image.LANCZOS))
        for c in range(4)], axis=-1).clip(0, 1)
    alpha = small[..., 3:4]
    rgb = np.where(alpha > 1e-4, small[..., :3] / np.maximum(alpha, 1e-4), 0).clip(0, 1)
    rgba = (np.concatenate([rgb, alpha], axis=-1) * 255 + 0.5).astype(np.uint8)
    rgba[rgba[..., 3] < 2] = 0
    ys, xs = np.nonzero(rgba[..., 3] >= 2)
    pad = 2
    x0, y0 = max(xs.min() - pad, 0), max(ys.min() - pad, 0)
    x1, y1 = min(xs.max() + pad + 1, rgba.shape[1]), min(ys.max() + pad + 1, rgba.shape[0])
    crop = rgba[y0:y1, x0:x1]
    Image.fromarray(crop, 'RGBA').save(out_dir / f'{name}.png', optimize=True)
    info = {'width': int(x1 - x0), 'height': int(y1 - y0), 'cropOffset': [int(x0), int(y0)]}
    if 'lensCenter' in meta:
        info['lensCenter'] = [round(meta['lensCenter'][0] - x0, 2), round(meta['lensCenter'][1] - y0, 2)]
        info['rimInner'] = round(meta['rimInner'], 2)
        info['rimOuter'] = meta['rimOuter']
    (out_dir / f'{name}.json').write_text(json.dumps(info, indent=2))
    print(f'{name}.png  {info["width"]}x{info["height"]}  {info}')
