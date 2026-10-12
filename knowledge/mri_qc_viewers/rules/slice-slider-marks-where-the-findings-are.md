---
id: slice-slider-marks-where-the-findings-are
typ: regel
status: getragen
thema: knowledge/mri_qc_viewers
stand: 2026-10-12
herkunft: Nutzer 12.10.2026 am SWI-Betrachter: "die FP zu suchen ist schwer, ich will Hinweis auf dem horizontalen Bar gezeigt bekommen, wo das ist"
verweist_auf: [qc-slice-viewer-conventions, report-healthy-controls-separately]
---

# Der Schichtregler zeigt, in welchen Schichten Funde liegen; N/P springen zum naechsten Fund

## Aussage
Unter dem Schichtregler liegt eine Leiste mit farbigen Strichen je Schicht: gruen = erkannte Laesion, gelb = Fehlalarm,
rot = verpasste Referenz (drei Reihen, damit alle drei gleichzeitig sichtbar sind); im Modellvergleich (ohne Urteil) gruen =
irgendeine Vorhersage, rot = Referenz. Klick auf einen Strich springt zur Schicht. Tasten **N / P** springen zur naechsten /
vorigen Schicht mit irgendeinem Fund. Die Daten dafuer stecken schon in den Kachel-Flags je Schicht (`tiles[i].<run>.fp/
detected/missed`, `tiles[i].ref`), es ist nur Anzeige. Der Regler braucht genug Breite (flex 3, mindestens 200 px), sonst
verschwinden die Striche in 70 px.

Umgesetzt in `cmb/review/build_slice_viewer.py` (ticks(), jumpFinding(), Hilfetext), 12.10.2026; alle Stick-Seiten per
`--refresh-html` neu. Beim Uebernehmen in das Wiki-Tool qc_slice_viewer nachziehen.

## Traegt
Jeden Schichtbetrachter mit mehr als ~30 Schichten und seltenen Funden (CMB, PVS, kleine WMH).

## Traegt nicht
Betrachter ohne Referenz (dort nur gruen = Vorhersage) und Seiten, die keine Flags je Schicht mitfuehren.

## Bruchindikator
Ein Betrachter, in dem man Fehlalarme durch Blaettern suchen muss.

## Ablesung
Nutzer-Screenshot 12.10.2026 09:56; gerendert und geprueft 12.10. 10:50.

## Verknuepft
- [qc-slice-viewer-conventions](qc-slice-viewer-conventions.md)
- [qc-pages-explain-every-number-on-hover](qc-pages-explain-every-number-on-hover.md)
