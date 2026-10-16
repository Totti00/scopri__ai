# Note — Tesla Roadster che salta, si capovolge e "vola" (bozza, 16/10/2026)

## Scelta del proprietario
- Notizia 2 del menu del 16/10, titolo **c** "10 getti d'aria da razzo: guarda cosa fa la nuova Tesla", tipo **Scoperte**, **solo post** (niente Reel).
- Regole nuove del 16/10 applicate (`format/carousel-copy.md`): il meglio subito (capriola in slide 2, testa in giù in slide 3), contatore "N/8" su tutte tranne la copertina, slide 2 che sta in piedi da sola (nomina la Tesla Roadster e i 10 getti), slide "In breve" prima della chiusura, un solo invito nella chiusura: **"📩 Mandalo a chi sogna le auto volanti"** (stesso testo in caption).

## Colori
- **Post: giallo.** L'ultimo post (Google Play) partiva dal bianco; il giallo non è mai stato usato come partenza (meno recente del blu, usato il 14/10). I video sono notturni e scuri: un fondo chiaro li fa risaltare.
- **Chiusura: blu.** L'ultima chiusura era carta/bianco; tra blu e giallo, il blu (mai usato) stacca dall'"In breve" giallo che la precede, quindi non ha lo stesso colore dell'ultima slide di contenuto.
- Ritmo delle tinte (copertina → In breve): A, F, E = giallo, blu, carta, blu, giallo, carta, giallo · B, C, D = giallo, carta, blu, giallo, carta, blu, giallo. Chiusura blu in tutte le righe.

## Verifica del dato "10 getti d'aria"
- **Confermato** da più fonti: The Next Web ("10 thrusters linked to 600 litres of compressed air", parole di Lars Moravy di Tesla riportate da TechCrunch), autoevolution ("ten cold-gas thruster nozzles, integrated into the body panels"), InsideEVs (10 ugelli e 250 kg di gas compresso, secondo Tesla; letto solo dall'estratto di ricerca, la pagina dava errore 502). Il numero risale anche a Musk (2018: "~10 small rocket thrusters").
- Attenzione: è il numero **dichiarato da Tesla**. Electrek non dà un totale e nei video si vedono 4 getti dietro. I getti sono ad **aria compressa** (gas freddo, soprattutto azoto), non motori a razzo veri: "da razzo" regge perché la tecnica viene da SpaceX (Engadget, Electrek), ma in caption va spiegato.
- Titolo **non cambiato**.

## Dubbi rimasti
1. **"Nessuno a bordo"**: Electrek scrive "for the demos, nobody was in the car"; Engadget racconta che all'apertura delle portiere al posto di guida c'era un robot Optimus, "solo per scena", e che le acrobazie erano programmate. Nessuna persona a bordo è corretto; se il proprietario preferisce, il fumetto può diventare "Nessuna persona a bordo." o si può citare il robot.
2. **CNN e "messa in scena"**: la pagina CNN da qui risponde 451 (non leggibile). Nelle slide non ho scritto "messa in scena": ho scritto "Era una prova su una pista di SpaceX, in Texas" e, nell'"In breve", "Poca AI: acrobazie programmate" (Engadget). Un sito trovato in ricerca parla di capriola "tethered and remotely staged" (con cavi e comandata a distanza), ma è una fonte sola: non usato.
3. **"Giro della morte"** (menu): nei video non è un giro completo. L'auto sale su una rampa a C e **si ferma a testa in giù** (le ventole la tengono attaccata), poi si stacca, si gira in aria e scende con i getti (Engadget, Electrek). Ho scritto così.
4. **250.000 dollari**: è la prenotazione della versione "Thrust" (con i getti dietro): 5.000 subito + 45.000 entro 10 giorni + 245.000 per il pacchetto (Engadget; The Next Web dice "250.000 per la Thrust"). Prezzo finale non annunciato.
5. **"Non per strada."**: Tesla scrive che la versione "Rocket" (quella che "vola") non è omologata per le strade pubbliche (Electrek); la "Thrust" è "race ready", da pista. Il fumetto vale per le versioni con i getti, non per la Roadster base.
6. **Poca AI**: detto con onestà nell'"In breve". Le acrobazie sono programmate; nessuna fonte parla di AI alla guida.
7. Numero di slide: 8 (sopra le 3–5 della scheda news lampo, ma nella fascia 7–10 della guida nuova). Se serve accorciare, la slide 5 (derapata) è la più sacrificabile.
8. Nei fotogrammi di `roadster2` c'è la scritta "TESLA LIVE" in basso a destra (è il live ufficiale). Nel finale si può tagliare.
9. Anteprime di `carosello.py` (bozza/A, bozza/B): A e B partono ancora dal blu (manca il parametro del colore di partenza) e lo stile B non disegna il riquadro "numero" (slide 6 vuota in alto). Le anteprime giuste in giallo sono in `bozza/A/giallo/` e `bozza/B/giallo/`, rese dai `.dc.html`.

## Video (per il finale)
- `media/roadster1.mp4` (15 s, 1920×1080, Tesla, post di @elonmusk): 0–3 s capriola sopra il camion (copertina), 6–11 s salto sopra le auto parcheggiate e discesa con i getti (slide 4).
- `media/roadster2.mp4` (48 s, 1398×782, Tesla Live, post di @elonmusk): 8–11 s derapata con i getti (slide 5), 12–15 s rampa a C a testa in giù (slide 3), 26–31 s capriola sopra il Tesla Semi (slide 2 e seconda idea di copertina), 39–45 s auto sollevata dai getti (sfondo di E6).
- Fotogrammi usati nella bozza: `media/*.png` (copiati in `bozza/img/`).
- La bozza si rigenera con `python3 bozza/genera-bozza.py` (testi in testa al file).
