---
id: hcp-aging-labels-are-mostly-unet-silver
typ: befund
status: vorschlag
thema: knowledge/pvs_detection
stand: 2026-10-07
herkunft: Literaturrunde 3 (Sonnet-Agent, Preprint-Volltext ueber Europe PMC), PVS-Cluster Alita, 2026-10-07; Details pvs-arena/literatur/hcp_labels.md, valdo_task1_protokoll.md
verweist_auf: [small-pvs-only-in-hcp-t2-reference, reference-first-then-metric-then-model]
---

# HCP-Aging-PVS: 160 von 200 Masken sind U-Net-Vorhersagen, die 40 Handfaelle sind nicht gekennzeichnet; VALDO-Rater stimmen nur zu F1 0,20 ueberein

## Aussage
Im HCP-Aging-PVS-Datensatz (OpenNeuro ds005595) sind 40 Faelle (4-5 je Lebensdekade) von zwei Neuroanatomen
korrigiert; die uebrigen 160 Masken stammen von einem U-Net, das auf diesen 40 (plus 40 semi-supervised) nach
Frangi-Vorfilter trainiert wurde. Welche 40 das sind, steht weder in participants.tsv noch in den JSONs oder im
Repo. Markiert ist nur weisse Substanz, Basalganglien ausdruecklich nicht; Masken bis 1 Voxel (0,8 mm) duenn.
Der Inter-Rater-Dice 0,97 stammt aus 10 Faellen mit gemeinsamer Vorlage. Folge: ein F1 auf HCP misst
Uebereinstimmung mit deren Frangi+U-Net, und Frangi-Verfahren sehen dort systematisch gut aus.
Zum Vergleich VALDO Task 1 (1 mm, T1+T2+FLAIR, SABRE-Ganzhirn): Inter-Rater Dice 0,53 und Instanz-F1 etwa 0,20;
der Sieger (0,39 F1) lag ueber der Rater-Uebereinstimmung. Die Etikett-Decke fuer PVS bei 1 mm ist also niedrig.

## Traegt
Wahl und Deutung der Messlatten einer PVS-Arena: HCP = Trainings-/Entwicklungsdaten fuer kleine PVS, nicht
Experten-Wahrheit; EPVS-2024 und VALDO = ehrliche, aber rater-begrenzte Messlatten. Jedes eigene Rating braucht
zwei Rater und eine gemessene Uebereinstimmung, bevor Modelle daran gemessen werden.

## Traegt nicht
Ob die Autoren die 40er-Liste herausgeben (Kontakt im Preprint); ob der Vorlagen-Bias den 0,97 wirklich aufblaeht,
ist Vermutung.

## Bruchindikator
Eine veroeffentlichte 40er-Liste; oder Inter-Rater-Werte ohne gemeinsame Vorlage nahe 0,97.

## Ablesung
Chai et al., medRxiv 10.1101/2025.03.19.25324269 (Volltext Europe PMC); VALDO-Paper arXiv 2208.07167 (Tabelle,
Fliesstext widerspruechlich: 59,49/45,5 ist der Lakunen-Wert). DOIs nicht alle nachgeprueft.

## Verknuepft
- [small-pvs-only-in-hcp-t2-reference](small-pvs-only-in-hcp-t2-reference.md)
- [reference-first-then-metric-then-model](../../lesion_detection_method/rules/reference-first-then-metric-then-model.md)
