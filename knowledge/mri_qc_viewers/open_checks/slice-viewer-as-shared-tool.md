---
id: slice-viewer-as-shared-tool
typ: pruefpunkt
status: offen
thema: knowledge/mri_qc_viewers
stand: 2026-10-07
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
- [ ] Test: zwei synthetische Volumen mit je drei Kugeln, Referenz und eine "Vorhersage" mit einem
      Fehlalarm; pruefen, dass data.json TP/FP/FN richtig zaehlt und die Seite baut.
- [ ] Ordner `tools/mri/mri_segmentation/qc_slice_viewer/` anlegen, CHANGELOG, PAPERS (keine).

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
