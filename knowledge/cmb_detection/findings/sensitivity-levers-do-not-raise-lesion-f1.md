---
id: sensitivity-levers-do-not-raise-lesion-f1
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), ARBEIT.md 5j bis 5ae und Turnier 2, 2026-09-20 bis 2026-10-02
verweist_auf: [csf-rule-removes-false-alarms-without-loss, two-seeds-per-decision-below-0.08]
---

# Hebel, die das Netz empfindlicher machen, heben das Laesions-F1 nicht

## Aussage
Rund vierzig Eingriffe am Trainingsrezept wurden einzeln gegen dieselbe Basis gemessen
(VALDO, 57 Faelle, gepaart). Jeder Hebel, der die Sensitivitaet fuer kleine Blutungen
hob, bezahlte mit Fehlalarmen, und das F1 fiel oder blieb:
- **blob loss** (Kofler et al. 2023, Dice je zusammenhaengender Laesion statt je
  Ausschnitt): Sensitivitaet kleiner Laesionen 0,52 -> 0,64, F1 -0,044, zweiter
  Startwert -0,063.
- **Zentrumskarten-Kopf + Neugewichtung verpasster Laesionen** (nach CenSynCMB 2026):
  kleine Laesionen 0,52 -> 0,66, F1 -0,054 [-0,110; -0,006]; Neugewichtung allein -0,030.
- **Kuenstliche Blutungen** in zwei Fassungen: -0,130 und kein Gewinn.
- Online-Hard-Negative-Mining +-0,000; 90 / 120 Epochen -0,016 / -0,022; focal Tversky
  -0,355; z-Normierung mit Augmentierung -0,060; kubisches statt lineares Resampling -0,024.
Was blieb, sind die drei Bausteine der Kette: Uebermalung weg, anisotropes Netz,
Liquor-Regel. Der Engpass ist die Unterscheidung Blutung / Gefaessquerschnitt /
Verkalkung mit einer einzigen Magnitudensequenz; Formfilter (Laufstrecke entlang z,
Frangi, Kugeligkeit) scheitern auf dem anisotropen Gitter, weil Blooming eine Blutung
zum kurzen Zylinder macht.

## Traegt
Planung weiterer CMB-Arbeiten auf einer Sequenz: nicht noch ein Verlust, sondern
zusaetzliche Information (Phase/QSM, zweite Sequenz) oder bessere Kandidaten-Pruefung.
Und als Lesehilfe fuer Literatur: ein Sensitivitaetsgewinn ohne Precision ist noch kein
Fortschritt.

## Traegt nicht
Mehrsequenz-Verfahren: CenSynCMB erreicht mit drei Sequenzen auf VALDO per-Proband
0,743, wo dieses Netz auf einer Sequenz bei 0,57 bis 0,63 liegt. Dort koennen dieselben
Hebel wirken.

## Bruchindikator
Ein Trainingshebel auf einer Sequenz, der F1 gepaart mit Intervall ohne Null hebt.

## Ablesung
Eigene Messungen. Quellen der Hebel: Kofler et al., IPMI 2023, LNCS 13939:755-767,
doi:10.1007/978-3-031-34048-2_58; He et al., CenSynCMB, arXiv:2607.05325 (2026, Preprint).
Tier 1a fuer die Messungen.

## Verknuepft
- [csf-rule-removes-false-alarms-without-loss](csf-rule-removes-false-alarms-without-loss.md)
- [two-seeds-per-decision-below-0.08](../rules/two-seeds-per-decision-below-0.08.md)
