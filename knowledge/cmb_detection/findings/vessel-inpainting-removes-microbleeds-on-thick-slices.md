---
id: vessel-inpainting-removes-microbleeds-on-thick-slices
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), ARBEIT.md 4.1, gemessen 2026-09-19/20
verweist_auf: [anisotropic-first-level-beats-isotropic-3d-nets, two-seeds-per-decision-below-0.08]
---

# Die Gefaess-Uebermalung des Originals loescht auf dicken Schichten die Blutungen selbst

## Aussage
MicrobleedNet (Sundaresan et al. 2023) uebermalt vor dem Netz alles, was ein
Frangi-Gefaessfilter je Schicht findet, und rettet nur, was rund und kompakt aussieht.
Auf VALDO (0,8 bis 4 mm Schichten) trifft diese Uebermalung **109 von 236**
annotierten Blutungen, uebermalt 27 vollstaendig und macht 17 unsichtbar; sie malt
12 bis 17 Prozent des Hirns neu. Training ohne die Uebermalung:
F1 0,470 -> 0,588, gepaart **+0,136 [+0,065; +0,226]** -- der groesste Einzelgewinn
der ganzen Kette. Eine reparierte, labelfreie Uebermalung (Skalen in mm, eine Schwelle
je Volumen, nur lange duenne Strukturen) brachte in drei Dosen nichts (0,588 / 0,584 / 0,570).

## Traegt
Jede Wiederverwendung von MicrobleedNet oder aehnlicher "Gefaesse zuerst entfernen"-
Vorverarbeitung auf Daten mit Schichten >= 2 mm. Die Autoren nennen das Risiko selbst;
ihr Verfahren entstand auf duennschichtigem SWI.

## Traegt nicht
Duennschichtiges, isotropes SWI. Dort wurde der Schaden hier nicht gemessen.

## Bruchindikator
Ein Datensatz mit dicken Schichten, auf dem die Uebermalung gepaart gewinnt.

## Ablesung
Eigene Messung, VALDO 2021 Task 2 (Sudre et al. 2024, doi:10.1016/j.media.2023.103029),
57 Faelle, 5-fach-CV, Bootstrap 10 000 Zuege. Referenz: Sundaresan et al., Front.
Neuroinform. 2023, doi:10.3389/fninf.2023.1204186, Code-Stand 958f1cb. Tier 1a (eigene Messung).

## Verknuepft
- [anisotropic-first-level-beats-isotropic-3d-nets](anisotropic-first-level-beats-isotropic-3d-nets.md)
- [two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md)
