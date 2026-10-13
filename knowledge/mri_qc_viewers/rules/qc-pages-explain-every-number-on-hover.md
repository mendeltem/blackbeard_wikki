---
id: qc-pages-explain-every-number-on-hover
typ: regel
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-12
herkunft: Nutzer 12.10.2026 zum DEMDAS-GM-Betrachter: "kannst du die Software alle sagen, wie das alles berechnet worden ist, in der Wiki, wenn man darueber hovert?"
verweist_auf: [demdas-gm-qc-page-how-every-number-is-computed, qc-pages-english-sessions-in-one-window, qc-slice-viewer-conventions]
---

# Jede Zahl auf einer QC-Seite erklaert sich beim Hovern: Software, Rechenweg, Label-Menge

## Aussage
1. **Jede Zeilenbeschriftung** mit einer Zahl traegt ein `title=` (Hover) mit Software und Version, Eingabe,
   Rechenweg und, bei Aggregaten, der genauen Label-Menge. Sichtbar durch gepunktete Unterstreichung
   (`.hilf{border-bottom:1px dotted;cursor:help}`).
2. **Ein Knopf "? Methods"** (Taste M, Esc schliesst) oeffnet ein Overlay mit allen Texten in fester
   Reihenfolge, dem Bauzeitpunkt, dem Generator und einem Link auf die Langfassung im Wiki (Hinweis
   "internal wiki, needs access", denn das Repo ist privat). Die Seite muss ohne den Link vollstaendig sein.
3. **Fehlende Werte nennen den Grund und den Stand**, nicht nur "not computed yet": z. B.
   "FreeSurfer recon-all has not finished for this session (31 of 63 sessions finished when this page was built,
   about 1 h per session; the rest are queued and the page is rebuilt automatically)". Die Zahlen setzt der
   Generator beim Bau ein, nie von Hand.
4. **Die Texte leben im Generator** (`methoden()`-Woerterbuch in gm_qc_axial.py, neben dem Code, der die
   Zahlen rechnet), werden als JSON in die Seite eingesetzt und beim Rendern HTML-escaped. Englisch wie die Seite.
5. Was die Anzeige veraendert, ohne die Zahlen zu veraendern (Ausrichtung der Folgesitzungen auf M0), steht
   als eigene Zeile im Sitzungs-Panel ("Aligned to M0, overlap 0.99") mit Hover-Erklaerung.

## Traegt
Jede QC-Seite mit Zahlen (Volumina, Dicken, F1, Zaehler), die an Dritte geht; jeden Generator unter
mri_qc_viewers. Pruefung: headless rendern, im DOM `class=hilf` und die `<dt>`-Liste des Overlays nachsehen.

## Traegt nicht
Reine Bildbetrachter ohne Zahlen; Eingabetabellen (Excel) -- dort steht die Methode im Blatt Lies_mich.

## Bruchindikator
Eine Zahl auf einer Stick-Seite, deren Beschriftung keinen Hover-Text hat, oder ein Generator, dessen
Rechenweg sich geaendert hat, waehrend der Hover-Text den alten beschreibt.

## Ablesung
Umgesetzt 12.10.2026 09:10-09:15 auf Alita (gm_qc_axial.py, Stick aktualisiert, headless geprueft:
19 Overlay-Eintraege, Hover an allen Zeilen des linken Panels).

## Verknuepft
- [demdas-gm-qc-page-how-every-number-is-computed](../findings/demdas-gm-qc-page-how-every-number-is-computed.md)
- [qc-pages-english-sessions-in-one-window](qc-pages-english-sessions-in-one-window.md)
- [qc-slice-viewer-conventions](qc-slice-viewer-conventions.md)

**Nachtrag 2026-10-12 (Nutzerregel, 16:45): Software-Block ist Pflicht.** Jede QC-Seite nennt alle Programme mit Version, die ihre Zahlen und Bilder erzeugt haben (z.B. FreeSurfer 8.2.0 build-stamp, SynthSeg-Flags, FSL-Version, Infarkt- und WMH-Netze mit Gewichtsdatei, dcm2niix aus dem JSON, Python-Pakete, Bauzeitpunkt, Rechner), eingesammelt zur Bauzeit im Generator, als Abschnitt "Software" im Methods-Overlay und als Fusszeile "Built <date> with ...". Fehlt eine Angabe, steht "not recorded <date>", nie nichts.

## Software block mandatory (English, for external readers)

Every quality-control page of every viewer must carry a mandatory "Software" block, in English, listing every program and version that produced the numbers and images on that page: the MRI package with its build stamp and the exact segmentation flags, the atlas/registration tools, all deep-learning models with their weights file and training set, the DICOM converter version as recorded in the BIDS sidecars, the Python interpreter and package versions, the operating system and host, and the build date and time. Versions are collected automatically at build time from the tools themselves (build stamps, version files, git commits, sidecar JSON); anything a tool cannot report is printed as "not recorded <date>", never omitted. The block appears as a "Software" section in the page (Methods overlay or dedicated section) and as a one-line footer "Built <date> with FreeSurfer x.y, SynthSeg (flags), FSL x.y, ...". It contains no patient data. DEMDAS implements this in `qc_software.py` (demdas-gm), shared by gm_qc_axial.py, verlauf_statistik.py, fehler_statistik.py and abc_qc_bauen.py, plus an English "Software" sheet in DEMDAS_GM_Beispiel.xlsx.
