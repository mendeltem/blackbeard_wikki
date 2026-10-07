---
id: unseen-scanners-are-not-the-weak-spot
typ: befund
status: getragen
thema: knowledge/wmh_segmentation
stand: 2026-10-07
herkunft: Projekt wmhseg (Alita), WMH-Linie 2026-09-12 bis 2026-09-18
verweist_auf: [measure-tails-paired-not-by-percentile]
---

# Ungesehene Scanner sind nicht die Schwachstelle; schwierige Faelle auf bekannten Geraeten sind es

## Aussage
Der Challenge-Testsatz traegt drei Standortnamen, aber **fuenf Geraete**: "Amsterdam" zerfaellt
nach FLAIR-Voxelvolumen (`nib.load(f).header.get_zooms()`) in drei Scanner (3,52 / 1,75 /
4,72 mm3), von denen zwei weder im Challenge-Training noch in den eigenen Trainingsdaten
vorkommen. Dice des ausgelieferten Modells je Geraet (n = 30 / 10 / 10 / 30 / 30):

| Scanner | Mittel | schlechtester Fall | Faelle < 0,5 |
|---|---|---|---|
| Amsterdam 3,52 mm3 (GE 3T, bekannt) | 0,723 | 0,452 | 1 |
| Amsterdam 1,75 mm3 (**ungesehen**) | 0,718 | 0,513 | 0 |
| Amsterdam 4,72 mm3 (**ungesehen**) | 0,710 | 0,532 | 0 |
| Singapore 3,00 mm3 (bekannt) | 0,759 | 0,321 | 1 |
| Utrecht 2,76 mm3 (bekannt) | 0,707 | 0,235 | 3 |

Die 20 Faelle der beiden ungesehenen Geraete haben keinen einzigen Ausfall; alle fuenf
Ausfaelle unter 0,5 liegen auf bekannten Scannern. Das dreht die Suchrichtung: nicht
Scanner-Robustheit, sondern die Fehlerart der Ausfaelle untersuchen. Und: immer nach den
fuenf Geraeten stratifizieren, nicht nach dem Standortfeld -- "Amsterdam" ist selbst ein
Mittel ueber Voxelvolumina mit Faktor 2,7.

## Traegt
Robustheitsfragen bei FLAIR-WMH-Netzen auf 3T-Daten vergleichbarer Protokolle.

## Traegt nicht
Stark abweichende Protokolle (1,5 T, andere Sequenzen) -- nicht gemessen. n = 10 je ungesehenem Geraet ist klein.

## Bruchindikator
Ein neuer Scanner mit Ausfallrate ueber der der bekannten Geraete.

## Ablesung
Eigene Messung, 110 oeffentliche Challenge-Testfaelle, 2026-09-13. Tier 1a.

## Verknuepft
- [measure-tails-paired-not-by-percentile](../rules/measure-tails-paired-not-by-percentile.md)
- [slices-not-cases-weigh-in-2d-training](slices-not-cases-weigh-in-2d-training.md)
