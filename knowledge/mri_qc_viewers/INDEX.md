# mri_qc_viewers

Qualitaetskontroll-Seiten fuer Laesionsdetektion und -segmentierung auf MRT: Einzeldatei-HTML,
die Referenz und Modellvorhersagen Schicht fuer Schicht zeigen. Hier stehen die Setzungen,
wie so eine Seite auszusehen hat (vom Nutzer an fertigen Seiten festgelegt), und was noch fehlt.
Keine Patientendaten; die Seiten selbst liegen bei den Projekten.

Stand 2026-10-08. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| regel | [qc-slice-viewer-conventions](rules/qc-slice-viewer-conventions.md) | Zwei Bilder je Schicht, Referenz blau, Pfeile links/rechts = Proband, flache Leisten, F1 je Fall, Klick auf Komponente zeigt Werte, Englisch, Dateiname quality_control.html; Pruefpunkt headless rendern |
| regel | [qc-build-order-for-a-new-lesion-type](rules/qc-build-order-for-a-new-lesion-type.md) | Zehn Setzungen in Reihenfolge: Generator statt neue Seite, Vergleich heisst Vergleich, Urteils- oder Modellfarben, Regel-Ebenen vor der Kette, Warum je Fund, Rating getrennt und verblindet, nur 127.0.0.1, Pruefung vor Abgabe, Vorlesung eigenes Artefakt, drei Zeilen danach |
| pruefpunkt | [slice-viewer-as-shared-tool](open_checks/slice-viewer-as-shared-tool.md) | Den CMB-Schichtbetrachter als Tool unter tools/mri/ einstellen (Test auf synthetischen Daten fehlt) |

## Herkunft
Projekte valdo-t2s und mb-arena (Alita), `cmb/review/build_slice_viewer.py`, Nutzerrueckmeldungen 29.09. bis 07.10.2026.
