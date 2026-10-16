# cmb_detection

Automatische Erkennung zerebraler Mikroblutungen (CMB) auf T2*-GRE und SWI. Alle
Zahlen stammen aus dem oeffentlichen Datensatz VALDO 2021 Task 2 (72 Faelle, drei
Kohorten mit 0,8 bis 4 mm Schichtdicke; Sudre et al. 2024, doi:10.1016/j.media.2023.103029),
gemessen als Laesions-F1 in 5-fach-Kreuzvalidierung auf 57 Faellen, gepaart ueber
Faelle mit 95-%-Bootstrap-Intervall. Ausgangspunkt war MicrobleedNet
(Sundaresan et al. 2023, doi:10.3389/fninf.2023.1204186). Keine Zahlen eigener
Kohorten; die oeffentliche Seite mit allen Schritten und Quellen:
https://mendeltem.github.io/valdo-cmb-qc/architecture.html

Stand 2026-10-12. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| befund | [fine-tune-from-public-valdo-weights](findings/fine-tune-from-public-valdo-weights.md) | Public VALDO weights: unadapted over-detect on another T2* cohort (F1 rises with threshold to 0.9); fine-tuned with lr 1e-4 for 6 epochs +0.11 F1 over short scratch, on par with 60 epochs (one fold, vorschlag) |
| regel | [count-lesions-on-the-fine-grid-deliver-a-label-map](rules/count-lesions-on-the-fine-grid-deliver-a-label-map.md) | On 5 mm slices two microbleeds merge in the binary mask (37 -> 36); count on the model grid, deliver a label map (2026-10-16) |
| befund | [vessel-inpainting-removes-microbleeds-on-thick-slices](findings/vessel-inpainting-removes-microbleeds-on-thick-slices.md) | Gefaess-Uebermalung des Originals loescht 109 von 236 Blutungen; ohne sie +0,136 F1 |
| befund | [anisotropic-first-level-beats-isotropic-3d-nets](findings/anisotropic-first-level-beats-isotropic-3d-nets.md) | Erste Ebene nur in der Schicht falten: +0,159 gegen Attention-U-Net, zwei Turniere |
| befund | [csf-rule-removes-false-alarms-without-loss](findings/csf-rule-removes-false-alarms-without-loss.md) |  98 von 176 Fehlalarmen liegen im Liquor; SynthSeg-Regel 0,585 -> 0,646 ohne Verlust auf VALDO; Nachtrag 08.10.: auf SWI 62/426 und T2* 15/545 Blutungen geloescht |
| befund | [one-shared-candidate-classifier-for-all-cohorts](findings/one-shared-candidate-classifier-for-all-cohorts.md) | Ein Klassifikator auf dem Kandidaten-Pool aller Kohorten, eine Schwelle 0,30: = Liquor-Regel auf VALDO/T2*, SWI +0,061; braucht keine Gewebekarte |
| befund | [sensitivity-levers-do-not-raise-lesion-f1](findings/sensitivity-levers-do-not-raise-lesion-f1.md) | blob loss, Zentrumskarten, Neugewichtung, Synthese: Sensitivitaet rauf, F1 runter |
| befund | [valdo-cohort-3-mask-is-a-head-mask](findings/valdo-cohort-3-mask-is-a-head-mask.md) | Gelieferte Masken nicht eng: Kohorte 3 zu 40 % Nicht-Hirn; Abhilfe SynthSeg-Maske |
| befund | [valdo-t1-carries-nan-in-33-of-72-cases](findings/valdo-t1-carries-nan-in-33-of-72-cases.md) | 33/72 T1 mit NaN (Randschale); SynthSeg liefert lautlos leer bei rc 0; nan_to_num ist geprueft sicher |
| befund | [training-loss-does-not-rank-networks-or-schedules](findings/training-loss-does-not-rank-networks-or-schedules.md) | Verlustkurven von 16 Turnierlaeufen: gleicher Verlust bei F1 0,176 gegen 0,404; 90/120 Epochen senken den Verlust, nicht den Out-of-fold-Wert; Fruehstopp feuert auf Rauschen |
| befund | [full-data-last-state-models-run-hotter](findings/full-data-last-state-models-run-hotter.md) | Vollmodell ohne inneren Checkpoint: Wahrscheinlichkeiten verschoben, feste Schwelle 0,3 auf fremdem Scanner 0,415 statt 0,622; kreuzgewaehlt gleichauf; zweite Stufe faengt es ab (0,604) |
| befund | [training-geometry-must-cover-target-geometry](findings/training-geometry-must-cover-target-geometry.md) | Leave-one-cohort-out T2*: 4-mm-Kohorte ersetzbar (gleich), 0,8-mm-Kohorte nicht (0,295 gegen 0,641), 5 mm ohne sich selbst 0,336; Fallzahl anderer Geometrie ersetzt die Zielgeometrie nicht |
| befund | [csf-rule-on-swi-deletes-deep-lesions-synthseg-mislabels](findings/csf-rule-on-swi-deletes-deep-lesions-synthseg-mislabels.md) | Geloeschte Treffer liegen tief (Median ~10 mm vom Rand), Label 24 von SynthSeg auf SWI falsch; erodierte Liquor-Maske beste Variante; kein T1 -> kein FreeSurfer |
| regel | [report-healthy-controls-separately](rules/report-healthy-controls-separately.md) | Faelle ohne Referenzlaesion getrennt: FP je Fall und Fall-Spezifitaet statt F1; Fallmittel nur ueber Laesionsfaelle; eigene Gruppe in der Fallliste |
| regel | [patches-not-whole-images-for-small-lesions](rules/patches-not-whole-images-for-small-lesions.md) | Ausschnitte trainieren, Schiebefenster vorhersagen: 1,6 GiB VRAM statt Dutzende GB, 800 Beispiele je Epoche statt 57, Dosisreihe 24/38/48 mm ohne Gewinn ueber dem Rezept |
| regel | [two-seeds-per-decision-below-0.08](rules/two-seeds-per-decision-below-0.08.md) | Startwert-Rauschen eines U-Net-Trainings ~0,08 F1; kleinere Effekte brauchen zweiten Startwert |

## Herkunft
Projekt valdo-t2s (Alita), Arbeitsprotokoll ARBEIT.md, 2026-09-10 bis 2026-10-07;
Reproduzierbarkeitspaket privat auf GitHub (cmb-valdo-chain), QC-Seite oeffentlich (valdo-cmb-qc).
