---
id: no-standard-cycle-without-absorption-check
typ: regel
status: getragen
thema: knowledge/memory_supply
stand: 2026-10-03
herkunft: Vorgabe Mendel, 2026-10-03
verweist_auf: [gpu-memory-absorbs-fab-additions, rubin-hbm4-wafer-demand-2028-2030, demand-is-not-earnings]
---

# Kein Standardzyklus ohne Absorptionsprüfung

## Aussage
Wer für DRAM oder HBM mit dem Standardzyklus argumentiert ("Knappheit führt zu Capex, Capex zu Überangebot, Überangebot zu Preisverfall"), muss vorher zeigen, dass der Zubau nicht von mehr Speicher je Beschleuniger aufgefressen wird. Pflichtrechnung:

    Nachfrage-Wachstum = Wachstum (GB je Package) × Wachstum (Packages)
    Angebots-Wachstum  = Wachstum (GB je Wafer) × Wachstum (Waferkapazität)
    Überangebot nur, wenn Angebots-Wachstum > Nachfrage-Wachstum, je Jahr belegt

Erst wenn diese Rechnung ein Überangebot ergibt, darf der Zyklus als Argument stehen. Sonst ist er eine Analogie, kein Befund. Ausgangspunkt der Rechnung: [gpu-memory-absorbs-fab-additions](../mechanisms/gpu-memory-absorbs-fab-additions.md) und [rubin-hbm4-wafer-demand-2028-2030](../open_checks/rubin-hbm4-wafer-demand-2028-2030.md).

## Trägt
Neue Chats und Agenten beginnen nicht bei null mit dem Lehrbuchzyklus, sondern beim Stand dieser Rechnung. Historische Zyklen bleiben als Hypothese erlaubt, müssen aber gegen die Absorption getestet werden.

## Trägt nicht
Dass ein Zyklus ausgeschlossen ist. Die Regel verlangt die Prüfung, nicht ein bestimmtes Ergebnis. Fällt die Stückzahl (Finanzierungsgrenze) oder baut CXMT konventionelles DRAM schneller aus als erwartet, kann die Rechnung ein Überangebot ergeben, dann gilt es.

## Bruchindikator
keiner, Verfahrensregel

## Ablesung
Vorgabe Mendel. Die Zahlen in den verknüpften Einträgen sind Annahmen und Branchendienste.

## Verknüpft
- [gpu-memory-absorbs-fab-additions](../mechanisms/gpu-memory-absorbs-fab-additions.md)
- [rubin-hbm4-wafer-demand-2028-2030](../open_checks/rubin-hbm4-wafer-demand-2028-2030.md)
- [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)
