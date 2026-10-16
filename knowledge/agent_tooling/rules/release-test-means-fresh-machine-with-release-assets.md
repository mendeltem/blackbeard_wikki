---
id: release-test-means-fresh-machine-with-release-assets
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-16
herkunft: Repo microbleed_detection_3D_UNET, Neuer-Server-Tests und GitHub-Actions-Job fresh-machine, 2026-10-07
verweist_auf: [pip-freeze-is-not-an-install-file]
---

# "Installierbar" heisst: frische Maschine, nur die README-Befehle, Gewichte vom Release -- und jede CLI-Option einmal

## Aussage
Ein Paket mit vortrainierten Gewichten gilt erst als installierbar, wenn drei Dinge
unabhaengig voneinander durchlaufen:

1. **Frische Umgebung, nur README:** `pip install torch` (CPU-Index), `pip install git+https://...`,
   `--list-models`, `--selftest` (synthetisches Phantom, keine Downloads), dann ein echter Lauf,
   bei dem die Gewichte vom oeffentlichen Release geladen und per SHA-256 geprueft werden.
   Erst dieser Lauf fand den Fehler, den alle lokalen Tests uebersahen: der FSL-Wrapper
   `fast` blockiert OHNE `FSLDIR` stumm (0 % CPU, kein Fehler) -- lokal war die Variable
   immer gesetzt. Abhilfe: das Paket setzt `FSLDIR`/`FSLOUTPUTTYPE` aus dem gefundenen
   Installationspfad selbst und gibt jedem Fremdaufruf eine Zeitgrenze.
2. **Anderer Rechner:** ein CI-Job auf einem frischen Runner, der dasselbe tut (Installation von
   GitHub, Download vom Release, Segmentierung eines Phantoms) -- das ist der einzige "andere
   Rechner", den ein Agent ohne zweite Maschine hat.
3. **Jede Option einmal:** eine Testmatrix ueber jeden CLI-Schalter mit echten Gewichten auf dem
   Phantom (Sekunden je Fall) plus ein Fall mit echtem Bild, Maske, Gewebekarte und externem
   Werkzeug; Schalter, die nur mit Zusatzsoftware gehen (HD-BET, SimpleITK, FSL, CUDA), werden
   uebersprungen statt gefaelscht.

## Traegt
Jedes Werkzeug, das "einfach installieren und sofort ausfuehren" verspricht; besonders
Pipelines mit externen Programmen (FSL, FreeSurfer, HD-BET), deren Umgebungsvariablen auf der
Entwicklungsmaschine immer gesetzt sind.

## Traegt nicht
Bibliotheken ohne externe Programme und ohne Gewichtsdateien -- dort reicht der CI-Lauf.

## Bruchindikator
Ein Nutzer auf einer anderen Maschine, der mit den README-Befehlen scheitert, obwohl alle drei
Pruefungen gruen waren.

## Ablesung
Eigener Lauf 2026-10-07: erster Neuer-Server-Test haengt 10 min in `fast`; nach der Abhilfe
Lauf 2 mit Download 1150 s (FSL 620 s, Fenster 475 s auf CPU), CI-Job fresh-machine gruen,
Optionsmatrix 14/14. Tier 1a.

## Ergaenzung 2026-10-16 (Nutzerregel: "immer testen, wenn wir was bauen: ist es von 0 installierbar")
Gilt fuer JEDEN Bau, nicht nur fuer Releases: vor dem Push frischer Klon, NEUE Umgebung mit neuem Namen (ein
Installer, der eine vorhandene Umgebung gleichen Namens wiederverwendet, testet sonst nichts -- `install.sh` von
cmb_3d_unet_experiments tut genau das, also `--name <neu>`), dann der Selbsttest und jeder README-Block woertlich.
Die eigene Entwicklungsumgebung ist kein Beleg: dort ist das Paket editierbar installiert, Hilfspakete
(z. B. openpyxl fuer die Dateitabelle) sind von frueher da, Umgebungsvariablen gesetzt.

## Verknuepft
- [pip-freeze-is-not-an-install-file](pip-freeze-is-not-an-install-file.md)
