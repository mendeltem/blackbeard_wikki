---
id: roofline-decides-memory-class
typ: mechanismus
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-06
herkunft: Projekt SK Hynix, Recherche-Reports vom 26.07. und 03.08.2026, eingetragen 2026-10-06
verweist_auf: [bandwidth-bottleneck, mtia-ranking-asic-avoids-hbm, capacity-and-bandwidth-are-not-substitutes, hbm-bypass-architectures, hbf-announced-not-demonstrated]
---

# Die arithmetische Intensität der Last entscheidet die Speicherklasse

## Aussage
Roofline-Modell: liegt die arithmetische Intensität eines Kernels (FLOP je Byte Speicherverkehr) unter dem Ridge-Point der Hardware (Spitzenrechenleistung / Spitzenbandbreite), begrenzt die Bandbreite, sonst die Rechenleistung.

| Last | Intensität | bindet | Speicherklasse |
|---|---|---|---|
| LLM-Decode, kleiner Batch | um 1 FLOP/Byte | Bandbreite (Gewichte, KV-Cache) | HBM |
| LLM-Prefill | etwa Sequenzlänge | Rechenleistung | HBM nur für Kapazität |
| LLM-Training | hoch (große GEMM) | Rechenleistung, Kapazität | HBM |
| Empfehlung, klassisch (DLRM) | niedrig, hohe Lokalität | Kapazität, Latenz | LPDDR, DDR, SRAM |
| Robotik, Bild, Batch 1 | niedrig | Speicher, aber nicht rein Bandbreite | moderat |

Ridge-Points laut Report: B200 rund 250, H100 rund 660 FLOP/Byte. Folgen: Batching hebt die Intensität und erhöht zugleich die Kapazitätsnachfrage (ein KV-Cache je Batch-Element). Niedrigere Präzision senkt die Bytes je Parameter und wirkt wie ein Bandbreitengewinn. Aus der Trennung folgt die Aufteilung von Prefill und Decode auf verschiedene Geräte.

## Trägt
Die Zuordnung Last zu Speicherklasse als Rechenregel und die Herleitung des Bandbreitenbedarfs je Beschleuniger.

## Trägt nicht
Mengen. HBM-Nachfrage skaliert nicht 1:1 mit der Rechenleistung: Präzision und KV-Kompression dämpfen, Kontextlänge und MoE treiben. Der Nettoeffekt ist offen.

## Bruchindikator
Ein Hersteller weist für Decode im Volumen eine Speicherklasse ohne HBM aus, bei vergleichbarer Latenz.

## Ablesung
Roofline: Williams, Waterman, Patterson, Communications of the ACM 2009, DOI 10.1145/1498765.1498785 (peer-reviewed; DOI nicht nachgeprüft). Decode und Prefill: arXiv 2508.10395 und 2512.08731 (Preprints, Nummern nicht nachgeprüft). Robotik: arXiv 2605.30571 (Preprint, nicht nachgeprüft). Ridge-Points aus einer Sekundärquelle, Warnsignal.

## Verknüpft
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [mtia-ranking-asic-avoids-hbm](../findings/mtia-ranking-asic-avoids-hbm.md)
- [capacity-and-bandwidth-are-not-substitutes](capacity-and-bandwidth-are-not-substitutes.md)
- [hbm-bypass-architectures](../risks/hbm-bypass-architectures.md)
- [hbf-announced-not-demonstrated](../../memory_technology_roadmap/findings/hbf-announced-not-demonstrated.md)
