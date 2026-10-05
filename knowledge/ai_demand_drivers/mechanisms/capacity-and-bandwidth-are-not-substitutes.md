---
id: capacity-and-bandwidth-are-not-substitutes
typ: mechanismus
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-06
herkunft: Projekt SK Hynix, Recherche-Report HBM Demand and Profitable AI Workloads (03.08.2026), eingetragen 2026-10-06
verweist_auf: [bandwidth-bottleneck, mtia-ranking-asic-avoids-hbm, roofline-decides-memory-class, hbm-bypass-architectures, ddr5-hbm-per-wafer-opportunity-cost]
---

# Kapazitäts- und Bandbreitenspeicher wachsen gleichzeitig, sie ersetzen sich nicht

## Aussage
Geprüfter Schluss: "Die rentablen KI-Lasten (Ranking, Empfehlung) sind kapazitätsdominiert, also wandert Kapital von HBM zu kapazitätsdominiertem Speicher, netto negativ für HBM."

Ergebnis: die technische Prämisse hält, die Folgerung nicht.
- Kapazität und Bandbreite sind physikalisch keine Substitute. Ironwood liefert 192 GB und 7,4 TB/s zugleich; HBM wird als Träger von beidem gekauft.
- Die Hersteller melden beide Klassen als wachsend: SK Hynix für 2025 mehr als verdoppelten HBM-Umsatz und gleichzeitig mehr als verdoppelte Auslieferung von DDR5-Modulen ab 128 GB gegenüber dem Vorquartal; Micron einen HBM-Markt von rund 35 Mrd. USD (2025) auf rund 100 Mrd. USD (2028) und zugleich SOCAMM2 mit 192 GB.
- Drei Kräfte ziehen Last zu HBM zurück: die Menge der Inferenz auf HBM-GPUs (Nvidia: über 40 % des Rechenzentrumsumsatzes der letzten vier Quartale), Transformer in der Empfehlung, längerer KV-Cache durch Reasoning.

## Trägt
Verschiebt sich Inferenz auf SOCAMM, LPDDR oder RDIMM, sinkt nicht zwingend die HBM-Nachfrage; alle diese Klassen verbrauchen DRAM-Wafer.

## Trägt nicht
Dass HBM je Token konstant bleibt. Niedrigere Präzision (FP8, FP4) und KV-Kompression senken die Bytes je Token; ob das Volumen das ausgleicht, ist die Jevons-Frage. Herstellerprognosen (100 Mrd. USD) sind Tier 1a in der Herkunft, nicht in der Verlässlichkeit.

## Bruchindikator
SK Hynix oder Micron weisen in einem vollen Geschäftsjahr ein HBM-Umsatzwachstum unter dem Wachstum ihres kapazitätsdominierten Server-DRAM aus.

## Ablesung
Micron Call Q1 FY2026 (17.12.2025) und SK Hynix Ergebnis FY2025 (28.01.2026), Tier 1a; Nvidia-CFO-Aussage, Tier 1a. Aus dem Projekt-Report übernommen, nicht nachgeprüft.

## Verknüpft
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [mtia-ranking-asic-avoids-hbm](../findings/mtia-ranking-asic-avoids-hbm.md)
- [roofline-decides-memory-class](roofline-decides-memory-class.md)
- [hbm-bypass-architectures](../risks/hbm-bypass-architectures.md)
- [ddr5-hbm-per-wafer-opportunity-cost](../../memory_supply/mechanisms/ddr5-hbm-per-wafer-opportunity-cost.md)
