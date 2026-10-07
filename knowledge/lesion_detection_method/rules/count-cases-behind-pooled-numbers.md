---
id: count-cases-behind-pooled-numbers
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekt valdo-t2s (CMB), ARBEIT.md 5i, 2026-09-20; wmhseg 2026-09-14; uebertragen 2026-10-07
verweist_auf: [measure-tails-paired-not-by-percentile, noise-floor-before-effects]
---

# Hinter jeder gepoolten Zahl die Faelle zaehlen

## Aussage
Laesionslasten sind schief verteilt: wenige Faelle tragen die meisten Instanzen. Auf einer
eigenen T2*-Kohorte stellten drei Faelle 28 % aller Blutungen und rund die Haelfte der
Uebersehenen; ohne sie lag das F1 bei 0,696 statt 0,613. Eine "Kleinhirn-Luecke" des
Modells war in Wahrheit ein Fall-Effekt dieser drei. Beim WMH-Testsatz haengt das
Vorzeichen des 5. Perzentils bei n = 30 an der Interpolation.

Vorschriften:
- Jede gepoolte Zahl (F1 ueber alle Laesionen, Gesamtvolumen, Gesamtzahl) nur zusammen
  mit der Verteilung je Fall berichten: Median, Anteil der Top-3-Faelle an den Instanzen.
- Vergleiche gepaart je Fall mit Bootstrap ueber Faelle, nicht ueber Laesionen.
- Bevor man ein Muster deutet (Region, Scanner, Kohorte), die Faelle dahinter zaehlen.
  Erst Faelle, dann Deutung.
- Stichproben nie als "die ersten N" einer sortierten Liste ziehen; das ist ein Block,
  kein Querschnitt (dreimal daneben gelegen).

## Traegt
Alle Zaehlmasse und Volumina von Laesionen je Fall; besonders PVS- und CMB-Lasten,
die ueber Faelle um Groessenordnungen variieren.

## Traegt nicht
Masse, die je Fall normiert sind und deren Verteilung ueber Faelle schon geprueft wurde.

## Bruchindikator
Eine Kohorte, in der die Top-3-Faelle unter 10 % der Instanzen tragen -- dann ist die
Pooling-Verzerrung klein und die Regel kann auf das Berichten beschraenkt werden.

## Ablesung
Eigene Messungen (eigene Kohorten nur als Summen) und WMH Segmentation Challenge 2017.
Tier 1a.

## Verknuepft
- [measure-tails-paired-not-by-percentile](../../wmh_segmentation/rules/measure-tails-paired-not-by-percentile.md)
- [noise-floor-before-effects](noise-floor-before-effects.md)
