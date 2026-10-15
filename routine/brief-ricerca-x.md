# Brief: ricerca su X con Claude in Chrome (sessione sul computer del proprietario)

Da usare quando serve cercare su X video e demo per una notizia (deciso il 15/10/2026). La routine nel cloud non può pilotare Chrome: questa ricerca si fa in una sessione locale di Claude Code con l'estensione **Claude in Chrome**, con X già aperto e acceso con il tuo account.

## Come si usa
1. Apri Chrome, entra su x.com con il tuo account.
2. Apri Claude Code in locale nella cartella del repository (`git pull origin main` prima).
3. Incolla il testo qui sotto, cambiando solo la parte tra `<<…>>`.

## Testo da incollare
```
Usa Claude in Chrome e cerca su X (x.com, già aperto e acceso) video e demo per questa notizia:
<<NOTIZIA: es. "Google Play permette di lanciare app fatte con Google AI Studio (vibe coding), dal 13/10/2026">>
Cerca solo post con VIDEO pubblicati dopo il <<DATA, es. 13/10/2026>>.

1. Ricerche (tab "Più recenti" e "Media"): parole chiave e hashtag della notizia, es. #vibecoding, #AIStudio, #GooglePlay, #Gemini, "vibe coded", "Play Store", "AI Studio". Prova anche in italiano.
2. Account da guardare uno per uno: <<ES.: @GoogleAIStudio @GooglePlay @Android @AndroidDev @OfficialLoganK @patloeber @ammaar>>.
3. Risposte e citazioni ai post che parlano della notizia (qui di solito gli utenti mettono le loro demo): <<ES.: i post di The Verge, Chrome Unboxed, Teja Karlapudi>>.
4. Per ogni video trovato: link del post (https://x.com/<account>/status/<id>), autore, data e ora, cosa mostra in una riga, durata, quante visualizzazioni e like, se è del vero autore o una ripubblicazione. Scarta le ripubblicazioni di pagine raccolta e dei concorrenti (@ai__facile, ecc.): da lì prendi solo lo spunto e risali all'originale.
5. Per i migliori controlla il link MP4 con `https://api.fxtwitter.com/<account>/status/<id>` (campo media.videos[].url).

Regole del progetto (CLAUDE.md): foto e video veri, dal post originale dell'autore; l'autore si nomina solo in "Fonti" della caption, mai sulle slide; mai grafiche o video dei concorrenti; niente frasi inventate.

Risultato: scrivi una tabella in notizie/<<AAAA-MM-GG>>.md, sezione "5. Video trovati su X" (link, autore, data, cosa mostra, durata, visualizzazioni, MP4 se trovato, giudizio: usabile / da chiedere all'autore / no). Poi `git add`, commit con autore Claude <noreply@anthropic.com> e `git push origin main`. Non pubblicare nulla su Instagram e non scrivere su X.
```

## Dopo
Torna nella sessione della routine e scrivi "fatto, guarda la sezione 5": il regista legge i video trovati, scarica gli MP4 usabili in `media/` e li mette nelle slide e nel Reel.
