# cmb_detection

Automatische Erkennung zerebraler Mikroblutungen (CMB) auf T2*-GRE und SWI. Alle
Zahlen stammen aus dem oeffentlichen Datensatz VALDO 2021 Task 2 (72 Faelle, drei
Kohorten mit 0,8 bis 4 mm Schichtdicke; Sudre et al. 2024, doi:10.1016/j.media.2023.103029),
gemessen als Laesions-F1 in 5-fach-Kreuzvalidierung auf 57 Faellen, gepaart ueber
Faelle mit 95-%-Bootstrap-Intervall. Ausgangspunkt war MicrobleedNet
(Sundaresan et al. 2023, doi:10.3389/fninf.2023.1204186). Keine Zahlen eigener
Kohorten; die oeffentliche Seite mit allen Schritten und Quellen:
https://mendeltem.github.io/valdo-cmb-qc/architecture.html

Stand 2026-10-07. Ein Eintrag je Datei.

| Typ | Eintrag | Inhalt |
|---|---|---|
| befund | [vessel-inpainting-removes-microbleeds-on-thick-slices](findings/vessel-inpainting-removes-microbleeds-on-thick-slices.md) | Gefaess-Uebermalung des Originals loescht 109 von 236 Blutungen; ohne sie +0,136 F1 |
| befund | [anisotropic-first-level-beats-isotropic-3d-nets](findings/anisotropic-first-level-beats-isotropic-3d-nets.md) | Erste Ebene nur in der Schicht falten: +0,159 gegen Attention-U-Net, zwei Turniere |
| befund | [csf-rule-removes-false-alarms-without-loss](findings/csf-rule-removes-false-alarms-without-loss.md) | 98 von 176 Fehlalarmen liegen im Liquor; SynthSeg-Regel 0,585 -> 0,646, keine Blutung verloren |
| befund | [one-shared-candidate-classifier-for-all-cohorts](findings/one-shared-candidate-classifier-for-all-cohorts.md) | Ein Klassifikator auf dem Kandidaten-Pool aller Kohorten, eine Schwelle 0,30: = Liquor-Regel auf VALDO/T2*, SWI +0,061; braucht keine Gewebekarte |
| befund | [sensitivity-levers-do-not-raise-lesion-f1](findings/sensitivity-levers-do-not-raise-lesion-f1.md) | blob loss, Zentrumskarten, Neugewichtung, Synthese: Sensitivitaet rauf, F1 runter |
| befund | [valdo-cohort-3-mask-is-a-head-mask](findings/valdo-cohort-3-mask-is-a-head-mask.md) | Gelieferte Masken nicht eng: Kohorte 3 zu 40 % Nicht-Hirn; Abhilfe SynthSeg-Maske |
| befund | [valdo-t1-carries-nan-in-33-of-72-cases](findings/valdo-t1-carries-nan-in-33-of-72-cases.md) | 33/72 T1 mit NaN (Randschale); SynthSeg liefert lautlos leer bei rc 0; nan_to_num ist geprueft sicher |
| befund | [training-loss-does-not-rank-networks-or-schedules](findings/training-loss-does-not-rank-networks-or-schedules.md) | Verlustkurven von 16 Turnierlaeufen: gleicher Verlust bei F1 0,176 gegen 0,404; 90/120 Epochen senken den Verlust, nicht den Out-of-fold-Wert; Fruehstopp feuert auf Rauschen |
| regel | [two-seeds-per-decision-below-0.08](rules/two-seeds-per-decision-below-0.08.md) | Startwert-Rauschen eines U-Net-Trainings ~0,08 F1; kleinere Effekte brauchen zweiten Startwert |

## Herkunft
Projekt valdo-t2s (Alita), Arbeitsprotokoll ARBEIT.md, 2026-09-10 bis 2026-10-07;
Reproduzierbarkeitspaket privat auf GitHub (cmb-valdo-chain), QC-Seite oeffentlich (valdo-cmb-qc).
