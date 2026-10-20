/* Scopri AI carousel engine. Reads window.CAROUSEL (set in index.html before this script) and builds:
   frame (logo lockup, counter, swipe cue; no handle since 20 Oct 2026), grain, glows, magnifier zooms, the thread line,
   optional motion, QA, dev controls. URL modes: ?export=1 (static PNG capture), ?export=1&video=1 (MP4 frames). */
(() => {
  const C = Object.assign({
    handle: '@scopri__ai',            // kept for reference only: the frame no longer prints it (owner, 20 Oct 2026)
    tipo: 'notizia',                  // 'notizia' | 'curiosita' | 'prompt' | 'lista' | 'serie': picks the 🔔 follow line on the closing slide
    format: 'static',                 // 'static' | 'animated'
    logos: { dark: 'brand/scopri-ai-logo-negativo.png', light: 'brand/scopri-ai-logo-colore.png', accent: 'brand/scopri-ai-logo-bianco.png' },
    seams: [],                        // seams[k] = y where the thread crosses the seam between slide k+1 and k+2
    routes: [],                       // per slide: 'start' | 'straight' | 'rightUp' | 'leftDown' | 'end' | 'none' | { d, nodes }
    threadStart: 600,                 // x of the start node on the cover
    threadEnd: '.apill',              // element on the last slide the thread ends next to
    threadEndX: 120,                  // x of the vertical run on the closing slide (left of the centred follow line)
    slideDuration: 5000,              // ms per slide in animated carousels (override per slide with data-duration)
  }, window.CAROUSEL || {});

  const q = new URLSearchParams(location.search);
  if (q.has('export')) document.body.classList.add('export');
  if (q.has('video')) document.body.classList.add('video');

  const FONT_SPECS = ['200 100px "Inter Tight"', '400 30px "Inter Tight"', '500 30px "Inter Tight"', '600 100px "Inter Tight"', '800 100px "Inter Tight"', '500 20px "JetBrains Mono"'];
  const slides = [...document.querySelectorAll('.slide')];
  const N = slides.length;
  const pad = n => String(n).padStart(2, '0');
  const modeOf = sl => sl.classList.contains('mode-accent') ? 'accent' : sl.classList.contains('mode-light') ? 'light' : 'dark';
  const ARROW = '<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';

  /* Geometry relative to a slide, independent of preview scaling */
  function rel(el, slide) {
    const sr = slide.getBoundingClientRect(), r = el.getBoundingClientRect(), s = sr.width / 1080;
    return { l: (r.left - sr.left) / s, t: (r.top - sr.top) / s, r: (r.right - sr.left) / s, b: (r.bottom - sr.top) / s,
             cx: ((r.left + r.right) / 2 - sr.left) / s, cy: ((r.top + r.bottom) / 2 - sr.top) / s };
  }
  function textRect(el, slide) {
    const rg = document.createRange(); rg.selectNodeContents(el);
    const sr = slide.getBoundingClientRect(), s = sr.width / 1080, r = rg.getBoundingClientRect();
    return { l: (r.left - sr.left) / s, t: (r.top - sr.top) / s, r: (r.right - sr.left) / s, b: (r.bottom - sr.top) / s };
  }
  function lineCount(el) {   // from text-node rects: element rects (e.g. highlight bars) would double-count lines
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), bottoms = [];
    for (let t; (t = w.nextNode());) { if (!t.textContent.trim()) continue; const rg = document.createRange(); rg.selectNodeContents(t); [...rg.getClientRects()].forEach(r => r.width > 1 && bottoms.push(r.bottom)); }
    bottoms.sort((a, b) => a - b);
    return bottoms.reduce((n, b, i) => n + (i === 0 || b - bottoms[i - 1] > 12 ? 1 : 0), 0);
  }

  /* The lid of the Coperchio logo, used as the "bell" of the follow line: the plain small lid, as slanted as in the logo,
     no vibration lines (owner, 20 Oct 2026: the ringing version with curved lines was removed) */
  const BELL = '<svg class="bell" viewBox="0 0 600 340" aria-hidden="true"><path d="M88 140C110 70 200 35 310 40C420 50 545 140 528 262Z"/><path d="M42 160L555 312" style="fill:none;stroke:currentColor;stroke-width:64;stroke-linecap:round"/><path d="M335 22L378 35" style="fill:none;stroke:currentColor;stroke-width:46;stroke-linecap:round"/></svg>';
  const FOLLOW = { notizia: 'Seguici per non perdere le prossime notizie', curiosita: 'Seguici per non perdere le prossime curiosità',
    prompt: 'Seguici per non perdere i prossimi prompt', lista: 'Seguici per non perdere i prossimi consigli', serie: 'Seguici per la prossima puntata' };

  /* Frame (brand overrides): full logo lockup top-left, no logo/counter/cue on the closing slide,
     counter counts content slides only (N − 1). */
  function buildFrame() {
    slides.forEach((sl, i) => {
      const n = i + 1, last = n === N, cover = n === 1, mode = modeOf(sl);
      sl.insertAdjacentHTML('beforeend',
        `<svg class="layer grain" viewBox="0 0 1080 1350"><rect width="1080" height="1350" filter="url(#grain)"/></svg>` +
        (last ? '' : `<img class="f-logo" src="${C.logos[mode]}" alt="Scopri AI">`) +
        (last ? '' : `<div class="f-count"><b>${pad(n)}</b> / ${pad(N - 1)}</div>`) +
        (last ? '' : `<div class="f-cue${cover ? ' filled' : ''}">${ARROW}</div>`));
      sl.querySelectorAll('[data-logo]').forEach(el => { el.innerHTML = `<img src="${C.logos[mode]}" alt="Scopri AI">`; });
      // closing slide, second invite (20 Oct 2026): "🔔 Seguici per non perdere …" with the logo's lid as the bell
      sl.querySelectorAll('.follow').forEach(el => {
        if (!el.textContent.trim()) el.textContent = FOLLOW[C.tipo] || FOLLOW.notizia;
        el.insertAdjacentHTML('afterbegin', BELL);
      });
    });
  }

  /* Captions under images (owner, 20 Oct 2026): only "Prima" / "Dopo" when there is a comparison, never a comment.
     <p class="cap" data-under="#img">Prima</p> sits CAP_GAP px under the
     element(s), left-aligned with it. With several elements (data-under="#a,#b") or class "mid" it is centred under all of
     them, so it reads as one caption for both. Same gap and style on every slide: never place captions by hand. */
  const CAP_GAP = 28;
  function placeCaptions() {
    slides.forEach(sl => sl.querySelectorAll('.cap[data-under]').forEach(cap => {
      const els = [...sl.querySelectorAll(cap.dataset.under)];
      if (!els.length) throw new Error('caption: nothing matches ' + cap.dataset.under);
      const rs = els.map(e => rel(e, sl)), l = Math.min(...rs.map(r => r.l)), r = Math.max(...rs.map(r => r.r)), b = Math.max(...rs.map(r => r.b));
      Object.assign(cap.style, { left: Math.round(l) + 'px', top: Math.round(b + CAP_GAP) + 'px' });
      if (els.length > 1 || cap.classList.contains('mid')) { cap.classList.add('mid'); cap.style.width = Math.round(r - l) + 'px'; }   // one caption for all of them
      // a single caption keeps its text width, so it never spills over a neighbouring (overlapping) image
    }));
  }

  /* Magnifier zoom: <div class="lens" data-source="#card" data-target=".target" data-zoom="1.75" data-asset="#img"><div class="glass"></div></div>
     Centres the lens on the target, puts an enlarged live copy of the source inside, aligns an optional rendered
     magnifier (img with data-lens-x / data-lens-y = lens centre inside the PNG) and any .rings[data-follow]. */
  function buildLenses() {
    document.querySelectorAll('.lens[data-source]').forEach(lens => {
      const sl = lens.closest('.slide'), src = sl.querySelector(lens.dataset.source);
      const tgt = src.querySelector(lens.dataset.target || '.target') || src;
      const R = lens.offsetWidth / 2, inner = R - 14, zoom = +(lens.dataset.zoom || 1.75);
      const t = rel(tgt, sl), d = rel(src, sl), cx = Math.round(t.cx), cy = Math.round(t.cy);
      lens.style.left = (cx - R) + 'px'; lens.style.top = (cy - R) + 'px';
      const z = src.cloneNode(true); z.removeAttribute('id'); z.classList.remove('hero', 'deco');
      z.style.left = (d.l - (cx - inner)) + 'px'; z.style.top = (d.t - (cy - inner)) + 'px';
      z.style.transformOrigin = (cx - d.l) + 'px ' + (cy - d.t) + 'px'; z.style.transform = `scale(${zoom})`;
      lens.querySelector('.glass').appendChild(z);
      if (lens.dataset.asset) { const m = sl.querySelector(lens.dataset.asset); m.style.left = (cx - m.dataset.lensX) + 'px'; m.style.top = (cy - m.dataset.lensY) + 'px'; }
      sl.querySelectorAll('.rings[data-follow]').forEach(r => { r.style.setProperty('--rx', cx + 'px'); r.style.setProperty('--ry', cy + 'px'); });
      sl.dataset.heroX = cx; sl.dataset.heroY = cy;
    });
  }

  /* Glows: <div class="glow" data-for="<selector>"></div> centres on the target; DARK backgrounds lift around the hero */
  function placeGlows() {
    slides.forEach(sl => {
      sl.querySelectorAll('.glow[data-for]').forEach(g => {
        const tgt = sl.querySelector(g.dataset.for); if (!tgt) return;
        const r = rel(tgt, sl); g.style.left = Math.round(r.cx) + 'px'; g.style.top = Math.round(r.cy) + 'px';
        if (!sl.dataset.heroX) { sl.dataset.heroX = r.cx; sl.dataset.heroY = r.cy; }
      });
      if (sl.dataset.heroX) { sl.style.setProperty('--hx', (sl.dataset.heroX / 10.8).toFixed(1) + '%'); sl.style.setProperty('--hy', (sl.dataset.heroY / 13.5).toFixed(1) + '%'); }
    });
  }

  /* Thread line (§11.4): exit y of slide n = entry y of slide n+1, taken from C.seams */
  function route(type, yin, yout, sl) {
    const r = 24;
    if (type && typeof type === 'object') return { d: type.d, nodes: type.nodes || [] };
    switch (type) {
      case 'none': return null;
      case 'start': return { d: `M${C.threadStart} ${yout} H1080`, nodes: [[C.threadStart, yout]] };
      case 'straight': return { d: `M0 ${yin} H1080`, nodes: [] };
      case 'rightUp': case 'rightDown': { const x = 1032, s = yout < yin ? -1 : 1; return { d: `M0 ${yin} H${x - r} Q${x} ${yin} ${x} ${yin + s * r} V${yout - s * r} Q${x} ${yout} ${x + r} ${yout} H1080`, nodes: [] }; }
      case 'leftDown': case 'leftUp': { const x = 48, s = yout < yin ? -1 : 1; return { d: `M0 ${yin} H${x - r} Q${x} ${yin} ${x} ${yin + s * r} V${yout - s * r} Q${x} ${yout} ${x + r} ${yout} H1080`, nodes: [] }; }
      case 'end': {
        const el = sl.querySelector(C.threadEnd); if (!el) return { d: `M0 ${yin} H${C.threadEndX}`, nodes: [] };
        const p = rel(el, sl), ex = Math.round(p.l - 30), ey = Math.round(p.cy), x = C.threadEndX, s = ey < yin ? -1 : 1;
        return { d: `M0 ${yin} H${x - r} Q${x} ${yin} ${x} ${yin + s * r} V${ey - s * r} Q${x} ${ey} ${x + r} ${ey} H${ex}`, nodes: [[ex, ey]] };
      }
    }
    throw new Error('Unknown thread route: ' + type);
  }
  function buildThread() {
    if (!C.routes.length) return;
    slides.forEach((sl, i) => {
      const yin = i > 0 ? C.seams[i - 1] : null, yout = i < N - 1 ? C.seams[i] : null;
      const rt = route(C.routes[i], yin, yout, sl); if (!rt) return;
      const glow = sl.classList.contains('mode-dark');
      sl.insertAdjacentHTML('beforeend',
        `<svg class="layer thread" viewBox="0 0 1080 1350">` +
        (glow ? `<path class="thread-glow" d="${rt.d}" style="fill:none;stroke:var(--line);stroke-width:8;stroke-linecap:round;stroke-linejoin:round;opacity:.5" filter="url(#lineglow)"/>` : '') +
        `<path class="thread-path" d="${rt.d}" style="fill:none;stroke:var(--line);stroke-width:3;stroke-linecap:round;stroke-linejoin:round"/>` +
        rt.nodes.map(([x, y]) => `<circle class="thread-node" cx="${x}" cy="${y}" r="6" style="fill:var(--line)"/>`).join('') + `</svg>`);
    });
  }

  /* Motion for animated carousels: one shared choreography, so every animated carousel moves the same way.
     Order: pill → headline → body → hero/cards/rows (staggered) → thread draw. All text is in place by ~1.3 s.
     Opt out with data-anim="none"; override with data-anim="rise|fade|scale|draw|float" and data-delay="ms". */
  const MOTION = [
    ['.ghost,.supershape,.rings,.dots', 'fade', 0, 1200],
    ['.glow', 'fade', 150, 1200],
    ['.pill', 'rise', 0, 650],
    ['.display,.h1,.h2,.numeral', 'rise', 120, 700],
    ['.lead,.body,.chip', 'rise', 320, 650],
    ['.lens,.asset[data-lens-x]', 'fade', 460, 750],          // a lens and its rendered rim must stay aligned
    ['.card,.pcard,.glassobj,.asset,.cmp>.card,.apill,.logo-full', 'scale', 460, 750],
    ['.row', 'rise', 520, 600, 90],
  ];
  function applyMotion() {
    if (C.format !== 'animated') return;
    const ease = 'cubic-bezier(.2,.7,.2,1)', seen = new Set();
    slides.forEach(sl => {
      MOTION.forEach(([sel, kind, delay, dur, stagger = 0]) => {
        sl.querySelectorAll(sel).forEach((el, k) => {
          if (seen.has(el) || el.closest('.glass') || el.dataset.anim === 'none') return; seen.add(el);
          const kd = el.dataset.anim || kind, dl = +(el.dataset.delay ?? (delay + k * stagger));
          let a = `a-${kd} ${dur}ms ${ease} ${dl}ms both`;
          if (el.matches('.asset:not([data-lens-x]),.glassobj')) a += `, a-float 6s ease-in-out ${dl + dur}ms infinite alternate`;
          if (el.matches('.glow')) a += `, a-breathe 5s ease-in-out ${dl + dur}ms infinite alternate`;
          el.style.animation = a;
        });
      });
      sl.querySelectorAll('.thread-path,.thread-glow').forEach(p => {
        const L = Math.ceil(p.getTotalLength()); p.style.setProperty('--len', L); p.style.strokeDasharray = L;
        p.style.animation = `a-draw 1000ms ${ease} 600ms both`;
      });
      sl.querySelectorAll('.thread-node').forEach(n => { n.style.animation = `a-fade 300ms ease-out 1500ms both`; });
    });
  }

  /* Video capture API (used by export-video.mjs) */
  const slideDuration = sl => +(sl.dataset.duration || C.slideDuration);
  window.__video = {
    count: N,
    duration: i => slideDuration(slides[i]),
    show: i => { document.body.classList.add('solo'); document.querySelectorAll('.slot').forEach((s, k) => s.classList.toggle('on', k === i)); },
    seek: (i, ms) => {
      const sl = slides[i];
      document.getAnimations().forEach(a => { const t = a.effect && a.effect.target; if (t && sl.contains(t)) { a.pause(); a.currentTime = ms; } });
    },
  };

  /* ===== QA ===== */
  /* QA measures the final design: entrance animations are jumped to their end (infinite loops to their start),
     then restored, so a paused first frame (video mode) can't fake an overflow. */
  function settled(fn) {
    const saved = document.getAnimations().map(a => [a, a.currentTime, a.playState]);
    saved.forEach(([a]) => { const t = a.effect.getComputedTiming(); a.pause(); a.currentTime = isFinite(t.endTime) ? t.endTime : (t.delay || 0); });
    try { return fn(); } finally { saved.forEach(([a, ct, ps]) => { a.currentTime = ct; if (ps === 'running') a.play(); }); }
  }
  const runQA = () => settled(runChecks);
  function runChecks() {
    const errors = [], info = [];
    const live = { l: 96, t: 192, r: 984, b: 1134 }, tol = 0.5;
    const inter = (a, b) => a.l < b.r && a.r > b.l && a.t < b.b && a.b > b.t;
    const grow = (r, p) => ({ l: r.l - p, t: r.t - p, r: r.r + p, b: r.b + p });
    const short = el => `"${el.textContent.trim().replace(/\s+/g, ' ').slice(0, 28)}…"`;
    FONT_SPECS.forEach(f => { if (!document.fonts.check(f, 'Aàè€')) errors.push(`Font not loaded: ${f}`); });
    document.querySelectorAll('img').forEach(img => { if (!img.complete || !img.naturalWidth) errors.push(`Image missing: ${img.getAttribute('src')}`); });
    const ends = [];
    slides.forEach((sl, i) => {
      const n = 'S' + pad(i + 1), boxOnly = el => el.matches('.pcard,.card,.cmp,.rows,.logo-full');
      if (sl.offsetWidth !== 1080 || sl.offsetHeight !== 1350) { errors.push(`${n}: canvas ${sl.offsetWidth}×${sl.offsetHeight} (not laid out?)`); return; }
      const zones = [...sl.querySelectorAll('.f-logo,.f-count,.f-handle,.f-cue')].map(el => grow(rel(el, sl), 24));
      const texts = [...sl.querySelectorAll('.qa-text')];
      const measure = el => el.matches('[data-logo]') && el.querySelector('img') ? rel(el.querySelector('img'), sl) : boxOnly(el) ? rel(el, sl) : textRect(el, sl);
      texts.forEach(el => {
        const r = measure(el), lt = el.matches('.numeral') ? 8.5 : tol;   // thin numerals sit 8 px left on purpose (§10 T4)
        if (r.l < live.l - lt || r.r > live.r + tol || r.t < live.t - tol || r.b > live.b + tol)
          errors.push(`${n}: ${short(el)} outside the live area (${r.l.toFixed(0)},${r.t.toFixed(0)})–(${r.r.toFixed(0)},${r.b.toFixed(0)})`);
        if (el.scrollWidth > el.clientWidth + 1 || (el.matches('.pcard,.body,.lead,.card') && el.scrollHeight > el.clientHeight + 1)) errors.push(`${n}: ${short(el)} overflows its box`);
        if (el.dataset.lines && lineCount(el) !== +el.dataset.lines) errors.push(`${n}: ${short(el)} wraps to ${lineCount(el)} lines (expected ${el.dataset.lines})`);
      });
      sl.querySelectorAll('.body,.lead,.pcard p,.pcard li > span:last-child,.cmp .c-body').forEach(el => {
        const fs = parseFloat(getComputedStyle(el).fontSize); if (fs < 28) errors.push(`${n}: body text at ${fs}px (min 28)`);
      });
      const objs = [...sl.querySelectorAll('.card,.lens,.asset,.ghost,.glassobj')].filter(o => !o.closest('.glass'));
      objs.forEach(o => { const r = rel(o, sl); zones.forEach(z => { if (inter(r, z)) errors.push(`${n}: ${o.className.split(' ')[0]} enters a frame clear zone`); }); });
      sl.querySelectorAll('.pcard').forEach(pc => { const r = rel(pc, sl); info.push(`${n}: prompt card y ${r.t.toFixed(0)}→${r.b.toFixed(0)}`); if (r.b > 1100) errors.push(`${n}: prompt card bottom ${r.b.toFixed(0)} > 1100`); });
      const path = sl.querySelector('.thread-path');
      if (path) {
        const L = path.getTotalLength(), avoid = [...texts.map(el => grow(measure(el), 16)),
          ...[...sl.querySelectorAll('.card,.lens,.asset,.glassobj')].filter(o => !o.closest('.glass') && !o.dataset.threadOk).map(el => grow(rel(el, sl), 12)), ...zones];
        let hit = 0;
        for (let d = 0; d <= L; d += 4) { const p = path.getPointAtLength(d), pr = { l: p.x, t: p.y, r: p.x, b: p.y }; if (avoid.some(a => inter(grow(pr, 1.5), a))) hit++; }
        if (hit) errors.push(`${n}: thread touches text, a card or a frame zone (${hit} samples)`);
        ends.push({ i, a: path.getPointAtLength(0), b: path.getPointAtLength(L) });
      }
      if (C.format === 'animated') {
        sl.querySelectorAll('.qa-text').forEach(el => {
          const a = el.getAnimations ? el.getAnimations()[0] : null; if (!a) return;
          const t = a.effect.getComputedTiming(); if (t.delay + t.duration > 1600) errors.push(`${n}: ${short(el)} is readable only after ${(t.delay + t.duration) | 0} ms (keep ≤ 1600)`);
        });
      }
    });
    for (let k = 0; k < ends.length - 1; k++) {
      const A = ends[k], B = ends[k + 1]; if (B.i !== A.i + 1) continue;
      if (Math.abs(A.b.x - 1080) > 0.5 || Math.abs(B.a.x) > 0.5 || Math.abs(A.b.y - B.a.y) > 0.5) errors.push(`Seam ${A.i + 1}/${B.i + 1}: exit (${A.b.x.toFixed(0)},${A.b.y.toFixed(0)}) ≠ entry (${B.a.x.toFixed(0)},${B.a.y.toFixed(0)})`);
    }
    return { errors, info };
  }
  function showQA() {
    const { errors, info } = runQA(), out = document.getElementById('qa-out'); if (!out) return;
    out.className = 'qa ' + (errors.length ? 'bad' : 'ok');
    out.textContent = (errors.length ? `✗ ${errors.length} problemi\n` + errors.join('\n') : '✓ QA superato: nessun problema') + '\n' + info.join('\n');
  }

  /* Dev controls (outside the slides) */
  function devControls() {
    const deck = document.getElementById('deck'), $ = id => document.getElementById(id);
    const press = (on, off) => { $(on)?.setAttribute('aria-pressed', 'true'); $(off)?.setAttribute('aria-pressed', 'false'); };
    if ($('btn-grid')) $('btn-grid').onclick = () => { deck.classList.remove('strip'); press('btn-grid', 'btn-strip'); };
    if ($('btn-strip')) $('btn-strip').onclick = () => { deck.classList.add('strip'); press('btn-strip', 'btn-grid'); };
    if ($('btn-qa')) $('btn-qa').onclick = showQA;
    if ($('btn-play')) { $('btn-play').hidden = C.format !== 'animated'; $('btn-play').onclick = () => document.getAnimations().forEach(a => { a.cancel(); a.play(); }); }
  }

  const imagesLoaded = () => Promise.all([...document.images].map(img => img.complete ? 0 : new Promise(r => { img.onload = img.onerror = r; })));
  Promise.all(FONT_SPECS.map(f => document.fonts.load(f, 'Aàè€'))).then(() => document.fonts.ready)
    .then(() => { buildFrame(); return imagesLoaded(); })      // frame logos are images too
    .then(() => {
      placeCaptions(); buildLenses(); placeGlows(); buildThread(); applyMotion(); devControls();
      if (document.body.classList.contains('video')) document.getAnimations().forEach(a => a.pause());
      window.runQA = runQA; window.__ready = true;
      if (!document.body.classList.contains('export')) showQA();
    });
})();
