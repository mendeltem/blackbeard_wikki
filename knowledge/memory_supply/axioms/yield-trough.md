---
id: yield-trough
typ: axiom
status: getragen
thema: knowledge/memory_supply
stand: 2026-10-06
herkunft: Projekt SK Hynix, Systemprompt Fassung 10 (07.08.2026), eingetragen 2026-10-06
verweist_auf: [cadence-and-yield-trough, bandwidth-bottleneck, stacked-yield-is-decomposed, hybrid-bonding-forced-by-stack-height]
---

# Yield-Tal

## Aussage
Yield sinkt je Generation. HBM4E und Nachfolger (16-Hi, dünnere Dies, Hybrid Bonding, Logik-Basisdie aus der Foundry) starten mit niedrigerem Yield als die Vorgängergeneration. Innerhalb einer Generation gilt eine Lernkurve.

Zusammen mit dem Axiom bandwidth-bottleneck (im Projektprompt "Schnellster Beschleuniger") ergibt das die zentrale Verknappungsmechanik: die Nachfrage konzentriert sich auf genau die Generation mit dem schlechtesten Yield. Diese Kopplung wird gerechnet, nicht behauptet.

## Trägt
Weniger Bits je Wafer zu Beginn jeder Generation, im Basisszenario als gesetzt.

## Trägt nicht
Eine Yieldzahl. Yieldangaben aus Branchendiensten (etwa 12-Hi 50 bis 70 %, 16-Hi 30 bis 50 %) sind Warnsignal, unzulässige Quelle.

## Bruchindikator
Einer der drei Anbieter meldet 16-Hi-Volumenyield auf dem Niveau der Vorgängergeneration. Die Wirkungsrichtung hängt davon ab, wer es meldet, und ist bei Auslösung anzugeben.

Gegenzeichen, im Projekt notiert (Quelle nicht dokumentiert, also Warnsignal): Micron fährt den Yield von HBM4 12-Hi doppelt so schnell hoch wie bei der Vorgängergeneration. Betrifft 12-Hi; die Setzung hängt an 16-Hi. Ebenfalls berichtet: Kunden fragen 16-Hi begrenzt nach, 12-Hi HBM4E bleibt Mainstream. Dann verschiebt sich das Tal, statt einzutreten.

## Ablesung
Aussage des Anbieters selbst (Call, Präsentation) oder Konferenzpapier, Tier 1a oder 1b. Unregelmäßig getaktet. Wörtlich aus dem Projektprompt verdichtet; Setzung von Mendel.

## Verknüpft
- [cadence-and-yield-trough](../../ai_demand_drivers/mechanisms/cadence-and-yield-trough.md)
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
- [stacked-yield-is-decomposed](../rules/stacked-yield-is-decomposed.md)
- [hybrid-bonding-forced-by-stack-height](../../memory_technology_roadmap/mechanisms/hybrid-bonding-forced-by-stack-height.md)
