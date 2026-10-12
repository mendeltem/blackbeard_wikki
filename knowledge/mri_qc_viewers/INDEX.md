# mri_qc_viewers

Qualitaetskontroll-Seiten fuer Laesionsdetektion und -segmentierung auf MRT: Einzeldatei-HTML,
die Referenz und Modellvorhersagen Schicht fuer Schicht zeigen. Hier stehen die Setzungen,
wie so eine Seite auszusehen hat (vom Nutzer an fertigen Seiten festgelegt), und was noch fehlt.
Keine Patientendaten; die Seiten selbst liegen bei den Projekten.

Stand 2026-10-12. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| regel | [qc-slice-viewer-conventions](rules/qc-slice-viewer-conventions.md) | Zwei Bilder je Schicht, Referenz blau, Pfeile links/rechts = Proband, flache Leisten, F1 je Fall, Klick auf Komponente zeigt Werte, Englisch, Dateiname quality_control.html; Pruefpunkt headless rendern |
| regel | [qc-build-order-for-a-new-lesion-type](rules/qc-build-order-for-a-new-lesion-type.md) | Zehn Setzungen in Reihenfolge: Generator statt neue Seite, Vergleich heisst Vergleich, Urteils- oder Modellfarben, Regel-Ebenen vor der Kette, Warum je Fund, Rating getrennt und verblindet, nur 127.0.0.1, Pruefung vor Abgabe, Vorlesung eigenes Artefakt, drei Zeilen danach |
| regel | [qc-pages-english-sessions-in-one-window](rules/qc-pages-english-sessions-in-one-window.md) | Jede QC-Seite Englisch (auch Index, Plots, Manifest-Titel, Rating-Hinweis; im Generator, nicht nur in der Datei); Laengsschnitt: Sitzungsknoepfe M0..M60 im selben Fenster, Schicht bleibt, Tabelle ueber Sitzungen |
| regel | [qc-pages-explain-every-number-on-hover](rules/qc-pages-explain-every-number-on-hover.md) | Jede Zahl erklaert sich beim Hovern (Software, Rechenweg, Label-Menge); Knopf "? Methods" mit Overlay und Wiki-Link; fehlende Werte nennen Grund und Stand; Texte im Generator |
| befund | [demdas-gm-qc-page-how-every-number-is-computed](findings/demdas-gm-qc-page-how-every-number-is-computed.md) | Langfassung (Englisch) fuer den DEMDAS-GM-Betrachter: SynthSeg 8.2.0, DeepISLES, Label-Mengen der Aggregate, WMH-3D-U-Net, recon-all-Dicke, Ausrichtung auf M0 |
| regel | [slice-slider-marks-where-the-findings-are](rules/slice-slider-marks-where-the-findings-are.md) | Farbige Striche unter dem Schichtregler (gruen/gelb/rot je Schicht), Klick springt, N/P naechster/voriger Fund |
| regel | [the-local-mirror-is-the-source-of-the-qc-stick](rules/the-local-mirror-is-the-source-of-the-qc-stick.md) | ~/QUALITY_CONTROLL ist die Quelle, der Stick eine Kopie; vor dem Abziehen sync, cmp, lsof |
| pruefpunkt | [slice-viewer-as-shared-tool](open_checks/slice-viewer-as-shared-tool.md) | Den CMB-Schichtbetrachter als Tool unter tools/mri/ einstellen (Test auf synthetischen Daten fehlt) |

## Herkunft
Projekte valdo-t2s und mb-arena (Alita), `cmb/review/build_slice_viewer.py`, Nutzerrueckmeldungen 29.09. bis 07.10.2026.
