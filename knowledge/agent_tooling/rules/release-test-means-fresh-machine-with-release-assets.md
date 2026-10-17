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
Beleg am selben Abend: der erste Lauf von 0 fand zwei Fehler, die 89 gruene Tests uebersahen -- (1) `evaluate -o ../my_runs/pred` (relativ, wie in der README) schrieb abgeleitete Dateien mit relativem Pfad in eine Fallliste, die Pfade relativ zu IHREM Ordner aufloest: Pfad verdoppelt, Abbruch; alle Tests nutzten absolute tmp-Pfade. (2) Der Validierungsanteil (-tr_prop 0.8) hielt beim Beispiel genau einen Fall OHNE Laesion zurueck (10 x 0.2 ergab per Gleitkomma 1), F1 dort immer 0, Schwellenwahl sinnlos. Daraus: Tests rufen die Befehle so auf wie die README (relative Pfade, Arbeitsordner = Repo), und ein neuer Test muss am alten Code scheitern.
Die eigene Entwicklungsumgebung ist kein Beleg: dort ist das Paket editierbar installiert, Hilfspakete
(z. B. openpyxl fuer die Dateitabelle) sind von frueher da, Umgebungsvariablen gesetzt.

## Confirmed 2026-10-17 (second independent fresh run, different agent profile)

The whole README of `cmb_3d_unet_experiments` ran from zero again on the workstation: fresh clone from GitHub,
brand-new conda env, no reuse of the dev environment. All six command blocks verbatim, working directory = the
clone, `ALL README BLOCKS OK`. Total 14,098 s (3 h 55 min) on one RTX A5000, max VRAM 1.71 GiB:

| block | command | measured |
|---|---|---|
| install | `./install.sh --name <new>` | 93 s |
| 4 | `cmbx preprocess` (2 raw scans, FSL-free `-f True`) | 15 s |
| 5 | `cmbx train` (10 cases, 60 epochs) | 1524 s |
| 6 | `cmbx train --frst False` | 1778 s |
| 7 | `cmbx fine_tune -m pre` | 1786 s |
| 8 | `cmbx evaluate` (2 cases without labels) | 3 s |
| 9 | `cmbx cross_validate -fold 5` | 8899 s |

What a new user should know:

- **The check is affordable but not short: budget ~4 h from clone to green.** One single block (cross-validation,
  five trainings of 60 epochs) is 63 % of it; `train`, `train --frst False` and `fine_tune` are ~30 min each.
- **The README understates its own cost.** It promises "about 1 h on one GPU" for cross-validation on the examples;
  measured 2 h 28 on an RTX A5000. Treat README timings as lower bounds and state the GPU.
- **No external download is needed after the install:** `fine_tune -m pre` loads the pretrained VALDO weights from
  the repository itself (`models/valdo_t2/final/model.pt`) and logs the channel match
  (`['image','frst'] <- ['image','frst']`). Good for a fresh machine without internet beyond pip/GitHub.
- **The synthetic examples are a plumbing test, not a benchmark.** Cross-validation returned F1 0.963 on 10 cases
  (13 reference lesions, one false positive, per-case F1 mean 0.980). A green run proves the commands work on a new
  machine -- it says nothing about detection quality, and such a number must never be quoted as a result.
- **Silent-failure surface shrinks as more of the chain is public:** `preprocess`, `train`, `fine_tune`, `evaluate`,
  `cross_validate` all ran without FSL, HD-BET, FreeSurfer or SimpleITK present.

## Verknuepft
- [pip-freeze-is-not-an-install-file](pip-freeze-is-not-an-install-file.md)
