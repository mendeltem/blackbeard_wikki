---
id: mtia-ranking-asic-avoids-hbm
typ: befund
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-06
herkunft: Projekt SK Hynix, Recherche-Report HBM Demand and Profitable AI Workloads (03.08.2026), eingetragen 2026-10-06
verweist_auf: [custom-asics-use-hbm, bandwidth-bottleneck, hbm-bypass-architectures, capacity-and-bandwidth-are-not-substitutes, roofline-decides-memory-class]
---

# Metas Ranking-Chip MTIA v1 und v2 verzichtet bewusst auf HBM

## Aussage
Speicher der Hyperscaler-Eigenbeschleuniger nach Zieleinsatz:

| Chip | Zieleinsatz | Speicher | Kapazität | Bandbreite | Quelle |
|---|---|---|---|---|---|
| Meta MTIA v1 | Ranking, Empfehlung | LPDDR5 | 64 GB | 176 GB/s | ISCA 2023, 1b |
| Meta MTIA v2 | Ranking, Empfehlung | LPDDR5 + 256 MB SRAM | 128 GB | 204,8 GB/s | ISCA 2025, 1b |
| Google TPU v5e | Inferenz | HBM | 16 GB | 819 GB/s | Cloud-Doku, 1a |
| Google TPU v5p | Frontier-Training | HBM | 95 GB | 2.765 GB/s | Cloud-Doku, 1a |
| Google TPU v7 Ironwood | Inferenz, Training | HBM3E | 192 GiB | 7.380 GB/s | Cloud-Doku, 1a |
| AWS Trainium3 | Training, Reasoning | HBM3E | 144 GB | 4,9 TB/s | AWS, 1a |
| AWS Inferentia2 | Inferenz | HBM | 32 GB | 820 GB/s | AWS, 1a |
| Microsoft Maia 100 | Inferenz, Training | HBM2E | 64 GB | 1,8 TB/s | Hot Chips 2024, 1b |

Der einzige Chip, der ausschließlich für Ranking und Empfehlung gebaut wurde, kommt ohne HBM aus. Das MTIA-v2-Papier begründet es: großes SRAM mit LPDDR dahinter, HBM vermieden zur Senkung von Kosten und Leistungsaufnahme, weil die Empfehlungsmodelle anders als große Transformer hohe Lokalität haben.

Gegenbeobachtung: Google bedient Ranking über SparseCores auf HBM-TPUs. Die Aussage gilt für Metas dedizierten Chip, nicht für jeden Betreiber.

Stand der Prüfbedingung: der Report setzte als Falsifikator, dass die nächste MTIA-Generation HBM als Primärspeicher nutzt. Der Eintrag custom-asics-use-hbm führt genau das (MTIA 300 und Nachfolger mit HBM, nicht nachgeprüft). Offen ist, ob MTIA 300 dasselbe Ranking bedient oder generative Lasten.

## Trägt
Rentable Ranking-Lasten in klassischer DLRM-Struktur brauchen Kapazität und Latenz, keine HBM-Bandbreite.

## Trägt nicht
Den Schluss "Kapital wandert von HBM weg", siehe capacity-and-bandwidth-are-not-substitutes. Empfehlung wandert selbst zu Transformern (Metas HSTU, arXiv 2402.17152, ICML 2024).

## Bruchindikator
Primärquelle (ISCA, Hot Chips, Meta Engineering Blog) weist HBM als Primärspeicher eines Ranking-Chips aus.

## Ablesung
Konferenzpapiere und Cloud-Dokumentation, Tier 1a und 1b. Werte aus dem Projekt-Report übernommen, gegen die Primärquellen nicht nachgeprüft; DOI der ISCA-Papiere nicht erhoben.

## Verknüpft
- [custom-asics-use-hbm](custom-asics-use-hbm.md)
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [hbm-bypass-architectures](../risks/hbm-bypass-architectures.md)
- [capacity-and-bandwidth-are-not-substitutes](../mechanisms/capacity-and-bandwidth-are-not-substitutes.md)
- [roofline-decides-memory-class](../mechanisms/roofline-decides-memory-class.md)
