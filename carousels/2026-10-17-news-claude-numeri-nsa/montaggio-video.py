# Usage: python3 -I montage.py SRC OUT "start-end:crop;start-end:crop;!start-end:crop"
# crop A = room scenes (inside the painted panel), B = number scenes; both ~2.114:1, English subtitles cut off.
# Segments are joined with a 0.5 s fade; a leading "!" joins with a hard cut (use it on blank frames).
import sys, subprocess
src, out, spec = sys.argv[1], sys.argv[2], sys.argv[3]
CROPS = {'A': '1570:743:175:85', 'B': '1766:835:77:70', 'D': '1840:870:40:70'}
W, H, X = 1776, 840, 0.5
segs = []
for part in spec.split(';'):
    cut = part.startswith('!')
    rng, c = part.lstrip('!').split(':')
    a, b = map(float, rng.split('-'))
    segs.append((a, b, CROPS[c], cut))
f = ''
for i, (a, b, c, _) in enumerate(segs):
    f += f'[{i}:v]setpts=PTS-STARTPTS,crop={c},scale={W}:{H}:flags=lanczos,setsar=1,fps=30,format=yuv420p[s{i}];'
last, t = '[s0]', segs[0][1] - segs[0][0]
for i in range(1, len(segs)):
    d = segs[i][1] - segs[i][0]
    if segs[i][3]:
        f += f'{last}[s{i}]concat=n=2:v=1:a=0[x{i}];'
        t += d
    else:
        off = t - X
        f += f'{last}[s{i}]xfade=transition=fade:duration={X}:offset={off:.3f}[x{i}];'
        t = off + d
    last = f'[x{i}]'
f = f.rstrip(';')
inputs = [x for (a, b, c, _) in segs for x in ('-ss', str(a), '-t', f'{b - a:.3f}', '-i', src)]
subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', f, '-map', last, '-an',
                '-c:v', 'libx264', '-crf', '16', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], check=True)
print(out, f'{t:.2f} s')
