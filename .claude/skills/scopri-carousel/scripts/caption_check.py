"""Controllo della caption di Scopri AI, prima di consegnarla (16/10/2026).
Adattato da caption.py della skill "ig-caption", con le regole di CLAUDE.md e brand/crescita.md.

Uso:   python caption_check.py <caption.txt | -> [--tipo notizia|curiosita|prompt|lista|serie]
                               [--formato carosello|reel] [--parole "gemini,google"] [--json]
Esce con 0 solo se la caption è PRONTA (nessun errore e nessun avviso).
publish-pack.py lo importa: check(...) → dict, render(dict) → testo, ricevuta(dict) → una riga.

Tipi:  notizia e curiosita → servono "Fonti: …" e l'invito 📩 Mandalo a …
       prompt e lista      → niente fonti, invito 📌 Salvalo …
       serie               → invito 🔔 Seguici
Riga 🔔 Seguici (20/10/2026): in tutti gli altri tipi, oltre all'unico invito, serve anche una riga che inizia con 🔔
       ("🔔 Seguici per non perdere le prossime notizie."), prima di "Fonti: …" e degli hashtag. Non conta come secondo invito.
Formati: carosello (la caption aggiunge alle slide) · reel (corta: 2–4 righe, chi la legge non ha visto slide)."""
import argparse
import json
import re
import sys
import unicodedata

LIMIT = 2200        # massimo di Instagram
VISIBLE = 125       # quanto si legge prima di "altro"
HASHTAG_MAX = 5     # Instagram ignora quelli oltre il quinto
REEL_SOFT = 450     # la caption di un Reel resta corta
EMOJI_PER_100 = 4   # oltre, sembra una pagina di spam

HASHTAG_RE = re.compile(r'(?<![\w&])#(\w+)', re.UNICODE)
MENTION_RE = re.compile(r'(?<![\w.])@[\w.]+')
LINK_RE = re.compile(r'https?://\S+|www\.\S+|\b[\w-]+\.(?:com|it|ai|io|org|net|ly|me|app)(?:/\S*)?\b', re.I)
EMOJI_RE = re.compile('[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U00002B00-\U00002BFF]')
FONTI_RE = re.compile(r'^[ \t]*Fonti?[ \t]*:', re.I | re.M)
# gancio concreto: un numero, un nome proprio a metà frase, un prodotto
CONCRETE_RE = re.compile(r'\d|(?<=[a-zàèéìòù,:] )[A-Z][\w-]+|\b(?:ChatGPT|Gemini|Claude|Copilot|Siri|Alexa|Meta|Google|Apple|OpenAI|Microsoft|Amazon|Samsung|Tesla|NASA)\b')

# un solo invito per post (CLAUDE.md, carousel-copy.md §8)
INVITI = {
    'manda': re.compile(r'\b(?:mandal[oa]|invial[oa]|condividil[oa]|giral[oa])\b(?:\s+\w+){0,2}\s+(?:a|al|alla|allo|ai|agli|alle)\b', re.I),
    'salva': re.compile(r'\bsalval[oa]\b|\bsalva\s+(?:il\s+)?(?:post|carosello|lista|prompt)\b', re.I),
    'segui': re.compile(r'\bseguici\b|\bsegui\s+(?:la\s+pagina|@scopri__ai|scopri\s+ai)\b', re.I),
}
# riga "🔔 Seguici per non perdere …" (20/10/2026): richiesta in aggiunta all'invito principale, tranne nelle serie
FOLLOW_RE = re.compile(r'^[ \t]*🔔[^\n]*?\b(?:seguici|segui\s+scopri\s+ai)\b[^\n]*$', re.I | re.M)
FOLLOW_TESTO = {'notizia': 'le prossime notizie', 'curiosita': 'le prossime curiosità', 'prompt': 'i prossimi prompt',
                'lista': 'i prossimi consigli'}
INVITO_GIUSTO = {'notizia': 'manda', 'curiosita': 'manda', 'prompt': 'salva', 'lista': 'salva', 'serie': 'segui'}
NOME_INVITO = {'manda': '📩 Mandalo a …', 'salva': '📌 Salvalo …', 'segui': '🔔 Seguici'}

# esche che Instagram punisce (brand/crescita.md): mai
# "commenta PAROLA e ti mando …" è ammesso dal 21/10/2026 (decisione del proprietario)
ESCHE = [
    (re.compile(r'\btagga(?:te)?\s+(?:\d+|un[oa]?|due|tre|i\s+tuoi|il\s+tuo|la\s+tua)\b', re.I), 'tagga un amico'),
    (re.compile(r'\b(?:metti|lascia(?:mi)?|mettete)\s+(?:un\s+)?(?:like|mi\s+piace|cuore)\b', re.I), 'metti like'),
    (re.compile(r'\blink\s+in\s+bio\b', re.I), 'link in bio'),
    (re.compile(r'\bscrivimi\s+in\s+(?:dm|direct|privato)\b', re.I), 'scrivimi in DM'),
]
TAG_INUTILI = {'instagood', 'viral', 'virale', 'fyp', 'foryou', 'perte', 'neiperte', 'explore', 'explorepage',
               'followme', 'follow', 'like4like', 'l4l', 'f4f', 'instadaily', 'love', 'reels', 'reel', 'trending'}


def visible_window(text, cut=VISIBLE):
    """Quello che si legge nel feed prima di "altro": fino al primo a capo, al massimo `cut` caratteri."""
    first = text.strip().split('\n', 1)[0]
    if len(first) <= cut:
        return first, len(text.strip()) > len(first)
    clip = first[:cut]
    if ' ' in clip[cut // 2:]:
        clip = clip[:clip.rfind(' ')]
    return clip.rstrip(' ,;:'), True


def check(text, tipo='notizia', formato='carosello', parole=()):
    text = text.replace('\r\n', '\n').strip()
    lines = [l for l in text.split('\n')]
    first = next((l for l in lines if l.strip()), '')
    window, cut = visible_window(text)
    tags = HASHTAG_RE.findall(text)
    res = []

    def add(nome, esito, msg):
        res.append({'controllo': nome, 'esito': esito, 'messaggio': msg})

    # 1. lunghezza
    n = len(text)
    if n > LIMIT:
        add('LUNGHEZZA', 'errore', f'{n} caratteri: Instagram ne accetta {LIMIT}.')
    elif formato == 'reel' and n > REEL_SOFT:
        add('LUNGHEZZA', 'avviso', f'{n} caratteri: per un Reel bastano 2–4 righe (≤ {REEL_SOFT}).')
    else:
        add('LUNGHEZZA', 'ok', f'{n}/{LIMIT} caratteri.')

    # 2. prima riga
    if not first:
        add('PRIMA RIGA', 'errore', 'Caption vuota.')
    elif first.lstrip()[0] in '#@':
        add('PRIMA RIGA', 'errore', 'La prima riga inizia con un hashtag o una menzione: deve essere il gancio.')
    elif FONTI_RE.match(first) or any(r.search(first) for r in INVITI.values()):
        add('PRIMA RIGA', 'errore', "La prima riga è l'invito o le fonti: deve essere il gancio.")
    elif len(first) > VISIBLE:
        add('PRIMA RIGA', 'ok', f'{len(first)} caratteri: Instagram la taglia dopo {VISIBLE}, guarda nel riquadro se il taglio regge.')
    else:
        add('PRIMA RIGA', 'ok', f'{len(first)} caratteri, si legge tutta.')

    # 3. gancio concreto
    if CONCRETE_RE.search(window):
        add('GANCIO CONCRETO', 'ok', 'Nella parte visibile c\'è un nome, un numero o un prodotto.')
    else:
        add('GANCIO CONCRETO', 'avviso', 'La parte visibile non ha nomi, numeri o prodotti: rischia di essere generica.')

    # 4. parole che la gente cerca
    cerca = [p.strip() for p in parole if p.strip()]
    if cerca:
        trovate = [p for p in cerca if p.lower() in window.lower()]
    else:   # senza --parole: basta "intelligenza artificiale", "AI" o un prodotto noto
        cerca = ['intelligenza artificiale']
        trovate = ['intelligenza artificiale'] if 'intelligenza artificiale' in window.lower() else \
            [m.group(0) for m in [re.search(r'\bAI\b|\b(?:ChatGPT|Gemini|Claude|Copilot|Grok|Llama|Sora|Midjourney|Perplexity)\b', window)] if m]
    if trovate:
        add('PAROLE CERCATE', 'ok', 'Nella parte visibile: ' + ', '.join(trovate) + '.')
    elif any(p.lower() in text.lower() for p in cerca):
        add('PAROLE CERCATE', 'avviso', f'"{cerca[0]}" c\'è, ma non nei primi {VISIBLE} caratteri.')
    else:
        add('PAROLE CERCATE', 'avviso', 'Mancano le parole che la gente cerca (' + ', '.join(cerca) + ').')

    # 5. hashtag
    low = [t.lower() for t in tags]
    if len(tags) > HASHTAG_MAX:
        add('HASHTAG', 'errore', f'{len(tags)} hashtag: Instagram legge solo i primi {HASHTAG_MAX}.')
    elif not tags:
        add('HASHTAG', 'avviso', f'Nessun hashtag: ne servono 3–{HASHTAG_MAX}, con #intelligenzaartificiale.')
    else:
        problemi = []
        if len(set(low)) < len(low):
            problemi.append('doppioni')
        inutili = sorted(set(low) & TAG_INUTILI)
        if inutili:
            problemi.append('generici: #' + ' #'.join(inutili))
        if 'intelligenzaartificiale' not in low:
            problemi.append('manca #intelligenzaartificiale')
        add('HASHTAG', 'avviso' if problemi else 'ok', f'{len(tags)} hashtag' + (': ' + '; '.join(problemi) + '.' if problemi else '.'))

    # 6. hashtag in fondo
    if tags:
        last_body = max((i for i, l in enumerate(lines) if l.strip() and not re.fullmatch(r'(\s*#\w+)+\s*', l)), default=-1)
        sparsi = [i for i, l in enumerate(lines) if HASHTAG_RE.search(l) and i < last_body]
        if sparsi:
            add('HASHTAG IN FONDO', 'avviso', 'Ci sono hashtag in mezzo al testo: vanno tutti nell\'ultima riga.')
        else:
            add('HASHTAG IN FONDO', 'ok', 'Tutti nell\'ultima riga.')

    # 7. fonti (regola 2)
    fonti = list(FONTI_RE.finditer(text))
    if tipo in ('notizia', 'curiosita'):
        if not fonti:
            add('FONTI', 'errore', 'Manca la riga "Fonti: …" (regola 2: notizie e curiosità hanno sempre la fonte).')
        else:
            primo_tag = HASHTAG_RE.search(text)
            if primo_tag and primo_tag.start() < fonti[-1].start():
                add('FONTI', 'errore', '"Fonti: …" deve venire prima degli hashtag.')
            elif any(l.strip() and not re.fullmatch(r'(\s*#\w+)+\s*', l)
                     for l in lines[text[:fonti[-1].start()].count('\n') + 1:]):
                add('FONTI', 'avviso', 'Dopo "Fonti: …" c\'è altro testo: le fonti vanno in fondo, seguite solo dagli hashtag.')
            else:
                add('FONTI', 'ok', 'In fondo, prima degli hashtag.')
    elif fonti:
        add('FONTI', 'avviso', 'I post di prompt non hanno fonte (regola 2): togli "Fonti: …".')

    # 8. un solo invito (la riga 🔔 Seguici non conta, tranne nelle serie dove è l'invito)
    follow = FOLLOW_RE.findall(text)
    testo_inviti = text if tipo == 'serie' else FOLLOW_RE.sub('', text)
    trovati = {k: len(r.findall(testo_inviti)) for k, r in INVITI.items()}
    tipi = [k for k, v in trovati.items() if v]
    giusto = INVITO_GIUSTO.get(tipo)
    if len(tipi) > 1:
        add('UN SOLO INVITO', 'errore', 'Più inviti diversi (' + ', '.join(NOME_INVITO[k] for k in tipi) + '): ne va uno solo.')
    elif not tipi:
        add('UN SOLO INVITO', 'avviso', f'Nessun invito: per questo tipo di post serve {NOME_INVITO[giusto]}.')
    elif tipi[0] != giusto:
        add('UN SOLO INVITO', 'avviso', f'Invito {NOME_INVITO[tipi[0]]}, ma per un post "{tipo}" serve {NOME_INVITO[giusto]}.')
    elif trovati[tipi[0]] > 1:
        add('UN SOLO INVITO', 'avviso', f'{NOME_INVITO[tipi[0]]} compare {trovati[tipi[0]]} volte: basta una.')
    else:
        add('UN SOLO INVITO', 'ok', NOME_INVITO[tipi[0]] + '.')

    # 8b. riga 🔔 Seguici, in aggiunta all'invito (20/10/2026)
    if tipo != 'serie':
        atteso = f'🔔 Seguici per non perdere {FOLLOW_TESTO.get(tipo, "i prossimi post")}.'
        if not follow:
            add('SEGUICI', 'avviso', f'Manca la riga "{atteso}" (prima di Fonti e hashtag).')
        elif len(follow) > 1:
            add('SEGUICI', 'avviso', f'La riga 🔔 Seguici compare {len(follow)} volte: basta una.')
        elif fonti and text.find(follow[0]) > fonti[-1].start():
            add('SEGUICI', 'avviso', 'La riga 🔔 Seguici va prima di "Fonti: …".')
        else:
            add('SEGUICI', 'ok', follow[0].strip()[:70])

    # 9. esche
    esche = sorted({nome for r, nome in ESCHE if r.search(text)})
    if esche:
        add('NIENTE ESCHE', 'errore', 'Esca che Instagram punisce: ' + ', '.join(f'"{e}"' for e in esche) + '.')
    else:
        add('NIENTE ESCHE', 'ok', 'Niente "commenta PAROLA", "tagga", "link in bio".')

    # 10. domanda vera
    domande = [l for l in lines if '?' in l and not FONTI_RE.match(l)]
    if not domande:
        add('DOMANDA', 'avviso', 'Nessuna domanda: aggiungine una vera, sul contenuto, per i commenti.')
    elif len(domande) > 2:
        add('DOMANDA', 'avviso', f'{len(domande)} righe con domande: ne basta una, chiara.')
    else:
        add('DOMANDA', 'ok', domande[-1].strip()[:70])

    # 11. link
    corpo = text[:fonti[-1].start()] if fonti else text
    links = LINK_RE.findall(MENTION_RE.sub('', corpo))
    if links:
        add('LINK', 'avviso', 'Link nella caption (' + ', '.join(links[:3]) + '): su Instagram non si clicca. Nomina il sito a parole.')
    else:
        add('LINK', 'ok', 'Nessun link.')

    # 12. emoji
    ne = len(EMOJI_RE.findall(text))
    dens = ne / max(n, 1) * 100
    if dens > EMOJI_PER_100:
        add('EMOJI', 'avviso', f'{ne} emoji ({dens:.1f} ogni 100 caratteri): troppe, una per blocco basta.')
    else:
        add('EMOJI', 'ok', f'{ne} emoji.')

    # 13. menzioni e nome della pagina
    if MENTION_RE.search(window):
        add('MENZIONI', 'avviso', 'Una menzione nella parte visibile: gli autori si nominano solo in "Fonti".')
    if re.search(r'Scopri\.AI|ScopriAI|Scopri Ai\b|Scopri\.ai', text):
        add('NOME', 'errore', 'Il nome è "Scopri AI" (con lo spazio, senza punto).')

    errori = sum(r['esito'] == 'errore' for r in res)
    avvisi = sum(r['esito'] == 'avviso' for r in res)
    verdetto = 'DA SISTEMARE' if errori else 'DA RICONTROLLARE' if avvisi else 'PRONTA'
    return {'verdetto': verdetto, 'tipo': tipo, 'formato': formato, 'caratteri': n, 'hashtag': len(tags),
            'invito': NOME_INVITO[tipi[0]] if len(tipi) == 1 else None, 'domanda': bool(domande),
            'fonti': bool(fonti), 'seguici': bool(follow) if tipo != 'serie' else None, 'visibile': window, 'tagliata': cut, 'controlli': res}


def box(window, cut):
    testo = window + (' … altro' if cut else '')
    righe, riga = [], ''
    for w in testo.split(' '):
        if len(riga) + len(w) + 1 > 44 and riga:
            righe.append(riga)
            riga = w
        else:
            riga = (riga + ' ' + w).strip()
    righe.append(riga)
    larg = max(46, max(_w(r) for r in righe) + 2)
    return '\n'.join(['┌' + '─' * larg + '┐'] + ['│ ' + r + ' ' * (larg - 2 - _w(r)) + ' │' for r in righe] + ['└' + '─' * larg + '┘'])


def _w(s):   # larghezza a schermo: le emoji occupano due colonne
    return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 0 if unicodedata.category(c) == 'Mn' or c == '\ufe0f' else 1 for c in s)


def ricevuta(r):
    icona = {'PRONTA': '✅', 'DA RICONTROLLARE': '⚠️', 'DA SISTEMARE': '❌'}[r['verdetto']]
    return (f"{icona} CAPTION {r['verdetto']} · {r['formato']} · {r['tipo']} — {r['caratteri']}/{LIMIT} caratteri · "
            f"{r['hashtag']} hashtag · invito: {r['invito'] or 'nessuno'} · domanda: {'sì' if r['domanda'] else 'no'}"
            + (f" · fonti: {'sì' if r['fonti'] else 'no'}" if r['tipo'] in ('notizia', 'curiosita') else '')
            + (f" · seguici: {'sì' if r.get('seguici') else 'no'}" if r.get('seguici') is not None else ''))


def render(r):
    segno = {'ok': '✔', 'avviso': '⚠', 'errore': '✖'}
    out = [f"Come si vede nel feed ({VISIBLE} caratteri):", box(r['visibile'], r['tagliata']), '']
    out += [f"{segno[c['esito']]} {c['controllo']:<17} {c['messaggio']}" for c in r['controlli']]
    out += ['', ricevuta(r)]
    return '\n'.join(out)


def tipo_da_cartella(nome):
    nome = nome.lower()
    for chiave, tipo in (('-curiosita-', 'curiosita'), ('-prompt-', 'prompt'), ('-lista-', 'lista'), ('-serie-', 'serie')):
        if chiave in nome:
            return tipo
    return 'notizia'


if __name__ == '__main__':
    try:
        sys.stdout.reconfigure(encoding='utf-8')   # Windows: le emoji non rompono la console
    except AttributeError:
        pass
    ap = argparse.ArgumentParser(description='Controllo della caption di Scopri AI')
    ap.add_argument('input', help='file .txt con la caption, oppure - per leggerla da stdin')
    ap.add_argument('--tipo', choices=sorted(set(INVITO_GIUSTO)), default=None, help='default: dal nome della cartella, altrimenti notizia')
    ap.add_argument('--formato', choices=['carosello', 'reel'], default=None, help='default: reel se il file si chiama *reel*')
    ap.add_argument('--parole', default='', help='parole che la gente cerca, separate da virgole (es. "gemini,google")')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args()
    text = sys.stdin.read() if a.input == '-' else open(a.input, encoding='utf-8').read()
    import os
    tipo = a.tipo or tipo_da_cartella(os.path.basename(os.path.dirname(os.path.abspath(a.input))) if a.input != '-' else '')
    formato = a.formato or ('reel' if 'reel' in os.path.basename(a.input).lower() else 'carosello')
    r = check(text, tipo, formato, a.parole.split(',') if a.parole else ())
    print(json.dumps(r, ensure_ascii=False, indent=2) if a.json else render(r))
    sys.exit(0 if r['verdetto'] == 'PRONTA' else 1)
