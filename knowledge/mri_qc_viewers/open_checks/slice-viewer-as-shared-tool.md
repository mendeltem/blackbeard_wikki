---
id: slice-viewer-as-shared-tool
typ: pruefpunkt
status: offen
thema: knowledge/mri_qc_viewers
stand: 2026-10-08
herkunft: Claude-Code-Sitzung Alita, 2026-10-07
verweist_auf: [qc-slice-viewer-conventions]
---

# Den Schichtbetrachter als Tool unter tools/mri/ einstellen

## Aussage
`cmb/review/build_slice_viewer.py` (Projekt valdo-t2s, englischer Code, keine Daten) erzeugt die
QC-Seite aus Manifest, Wahrscheinlichkeitskarten und optionaler Gewebekarte. Fuer die Wiki fehlt
ein Tool-Ordner nach `templates/tool/` mit README, INSTALL, einem Test auf synthetischen Volumen
und den Setzungen aus [qc-slice-viewer-conventions](../rules/qc-slice-viewer-conventions.md).

- [x] Umbau Tasten (Proband links/rechts, Schicht hoch/runter), flache Leisten, F1 je Fall (07.10.).
- [ ] Klick-Werte je Komponente (Geometrie und Zuordnung in data.json, Hervorhebung) im Generator.
- [x] Test (08.10.): zwei synthetische Volumen mit je drei Kugeln, Referenz und eine "Vorhersage" mit einem
      Fehlalarm; pruefen, dass data.json TP/FP/FN richtig zaehlt und die Seite baut.
- [x] Ordner `tools/mri/mri_segmentation/qc_slice_viewer/` angelegt (08.10.), README, INSTALL, CHANGELOG, PAPERS; manifestgesteuert, Vergleichsmaske und Liquor-Ebenen inklusive; Gegenprobe an drei VALDO-Faellen identisch mit dem CMB-Generator.
- [x] Live-Modus (07.10.): `live_server.py` serviert den Ordner auf 127.0.0.1, beobachtet die mtime des
      Generators, baut per `--refresh-html` aus `build_args.json` neu; die Seite pollt Last-Modified per HEAD
      (1,5 s) und laedt sich selbst, Fall und Schicht bleiben (Hash, sessionStorage). Gehoert mit ins Tool.
- [x] Generator-Option `--cohort NAME` (Anzeigename der Kohorte ohne Aenderung der Manifeste) und
      Live-Server fuer einen Elternordner mit mehreren Betrachtern (07.10.).

## Traegt
Wiederverwendung fuer WMH- und PVS-QC ohne Neubau.

## Traegt nicht
--

## Bruchindikator
--

## Ablesung
blind

## Verknuepft
- [qc-slice-viewer-conventions](../rules/qc-slice-viewer-conventions.md)
