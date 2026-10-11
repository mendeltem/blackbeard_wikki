---
id: qc-pages-english-sessions-in-one-window
typ: regel
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-11
herkunft: Nutzerentscheidung 11.10.2026 zum QC-Stick (QUALITY_CONTROLL/): "alles auf Englisch, jede Qualitaetskontrolle"; Wunsch zum DEMDAS-GM-Betrachter "M0, M6 ... in einem Fenster wechseln"
verweist_auf: [qc-slice-viewer-conventions, qc-build-order-for-a-new-lesion-type]
---

# Jede QC-Seite auf Englisch; Laengsschnitt-Sitzungen im selben Fenster umschalten

## Aussage
1. **Alle QC-Seiten sind Englisch**, nicht nur die Schichtbetrachter: auch der Stick-Index,
   Volumetrie-Verlaufsseiten mit ihren Plots (Achsen, Legenden, Titel), NiiVue-Seiten, Rating-Hinweise
   (README.txt neben LIESMICH.txt) und die Titel der Manifeste (`dataset`, `info`), die in den
   Seitentitel wandern. Deutsche Reste kamen 11.10. aus genau diesen Nebenwegen: Manifest-Titel
   ("Trenner", "Gewebesegmentierung"), Plot-Beschriftungen im Statistik-Skript, Index-Prosa.
   Die Uebersetzung gehoert in den **Generator** (gm_qc_axial.py, verlauf_statistik.py, qc_vorlage.html,
   qc_hcp_manifest.py, abc_qc_bauen.py), nicht nur in die gebaute Datei, sonst kommt das Deutsche beim
   naechsten Bau zurueck. Eingabespalten (Excel) bleiben als Schluessel unangetastet; uebersetzt wird nur
   die Anzeige (Display-Map im Skript).
2. **Laengsschnitt (ein Proband, mehrere Sitzungen) wird im selben Fenster umgeschaltet**:
   Knopfreihe `Session: M0 M6 M36 M60` ueber dem Bild, Pfeil hoch/runter laeuft nur durch die Sitzungen
   DESSELBEN Probanden, Bild hoch/runter (und Pfeilknoepfe neben dem Titel) wechseln den Probanden,
   die Fallliste gruppiert nach Proband. **Die Schicht bleibt beim Sitzungswechsel stehen** (geklemmt auf n-1),
   beim Probandenwechsel springt sie auf die Startschicht. Daneben eine Tabelle "Across sessions" mit den
   Kernvolumina (Brain, GM, WM, CSF, WMH) ueber alle Sitzungen, aktive Spalte hervorgehoben.
   Sortierung nach Monat (M0, M6, M10, M36, M60), nicht alphabetisch (M0, M10, M36, M6).
3. **Pruefung**: Suche nach deutschen Woertern ueber alle Seiten (Textknoten und String-Literale,
   DATA-Arrays und Base64 vorher entfernt), danach jede geaenderte Seite headless rendern
   (`chrome-headless-shell --screenshot --dump-dom`, liegt unter `~/.cache/ms-playwright/`) und im DOM
   nachsehen, dass die Knopfreihe gebaut wurde.

## Traegt
Jede QC-Seite, die auf den Stick oder an Dritte geht; jeden Betrachter mit mehr als einer Sitzung je Proband.

## Traegt nicht
Eingabedaten (Excel-Spalten, JSON-Schluessel wie `standort`, `schichten`), Dateinamen (`verlauf.html`,
`DEMDAS_GM_Beispiel.xlsx`), deutsche Notizen (.md) auf dem Stick, die der Index als solche kennzeichnet.

## Bruchindikator
Eine neu gebaute Seite auf dem Stick zeigt wieder deutsche Oberflaechentexte, oder ein Laengsschnitt-Betrachter
listet Sitzungen flach als eigene Faelle.

## Ablesung
Nutzer 11.10.2026 (zwei Nachrichten im selben Lauf); umgesetzt und gerendert 11.10. 18:28-18:40 auf Alita.
Offen: `DEMDAS_GM_Beispiel.xlsx` hat noch deutsche Blatt- und Spaltennamen (zwei Leser haengen daran).

## Verknuepft
[qc-slice-viewer-conventions](qc-slice-viewer-conventions.md), [qc-build-order-for-a-new-lesion-type](qc-build-order-for-a-new-lesion-type.md)
