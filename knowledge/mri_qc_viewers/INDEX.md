# mri_qc_viewers

Qualitaetskontroll-Seiten fuer Laesionsdetektion und -segmentierung auf MRT: Einzeldatei-HTML,
die Referenz und Modellvorhersagen Schicht fuer Schicht zeigen. Hier stehen die Setzungen,
wie so eine Seite auszusehen hat (vom Nutzer an fertigen Seiten festgelegt), und was noch fehlt.
Keine Patientendaten; die Seiten selbst liegen bei den Projekten.

Stand 2026-10-07. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| regel | [qc-slice-viewer-conventions](rules/qc-slice-viewer-conventions.md) | Zwei Bilder je Schicht, Referenz blau, Tasten, Klick auf Komponente zeigt Werte, Englisch, Dateiname quality_control.html |
| pruefpunkt | [slice-viewer-as-shared-tool](open_checks/slice-viewer-as-shared-tool.md) | Den CMB-Schichtbetrachter als Tool unter tools/mri/ einstellen (Test auf synthetischen Daten fehlt) |

## Herkunft
Projekte valdo-t2s und mb-arena (Alita), `cmb/review/build_slice_viewer.py`, Nutzerrueckmeldungen 29.09. bis 07.10.2026.
