---
id: hbm-bypass-architectures
typ: risiko
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Projekt Artificial Intelligence (KI-Compute-Stack), Report AI Accelerators Beyond NVIDIA (Mai 2026), eingetragen 2026-10-02
verweist_auf: [bandwidth-bottleneck, custom-asics-use-hbm, induced-innovation]
---

# Architekturen ohne HBM

## Aussage
Einige Inferenz-Beschleuniger umgehen HBM: Groq (nur SRAM auf dem Chip, 230 MB), Cerebras WSE-3 (44 GB SRAM auf dem Wafer), d-Matrix Corsair (SRAM plus 256 GB LPDDR5X), Tenstorrent (GDDR6). Dazu kommt die Aufteilung der Inferenz: AWS lässt den Prefill auf Trainium (HBM) und den Decode auf Cerebras (SRAM) laufen.

## Trägt
Gegenkraft zum Axiom bandwidth-bottleneck. Der Decode ist der bandbreitenlastige Schritt, genau er wandert in dieser Aufteilung von HBM weg.

## Trägt nicht
Größe. Der Report setzt den Anteil dieser Architekturen an der Inferenz unter 2 %, ohne Quelle. Groq braucht laut Report rund 576 Chips für ein 70-Milliarden-Parameter-Modell.

## Bruchindikator
keiner eigenen. Deckt sich mit dem Bruchindikator des Axioms bandwidth-bottleneck (Inferenzlast wandert auf andere Speicher).

## Ablesung
Umsätze und Kapazitätsverträge der Anbieter, Tier 1a, soweit börsennotiert (Cerebras). Anteil an der Inferenzlast: blind. Zahlen aus dem Projekt-Report übernommen, gegen die Primärquelle nicht nachgeprüft.

## Verknüpft
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [custom-asics-use-hbm](../findings/custom-asics-use-hbm.md)
- [induced-innovation](../mechanisms/induced-innovation.md)
