---
id: hbm-bypass-architectures
typ: risiko
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-14
herkunft: Projekt Artificial Intelligence (KI-Compute-Stack), Report AI Accelerators Beyond NVIDIA (Mai 2026), eingetragen 2026-10-02
verweist_auf: [bandwidth-bottleneck, custom-asics-use-hbm, induced-innovation, datacenter-beats-workstation-per-token, every-sector-grows-sum-counts]
---

# Architekturen ohne HBM

## Aussage
Einige Inferenz-Beschleuniger umgehen HBM: Groq (nur SRAM auf dem Chip, 230 MB), Cerebras WSE-3 (44 GB SRAM auf dem Wafer), d-Matrix Corsair (SRAM plus 256 GB LPDDR5X), Tenstorrent (GDDR6). Dazu kommt die Aufteilung der Inferenz: AWS lässt den Prefill auf Trainium (HBM) und den Decode auf Cerebras (SRAM) laufen.

## Trägt
Gegenkraft zum Axiom bandwidth-bottleneck. Der Decode ist der bandbreitenlastige Schritt, genau er wandert in dieser Aufteilung von HBM weg.

## Nachtrag 2026-10-14
Nvidia teilt die Inferenz selbst auf: Prefill (rechenlastig) auf Rubin CPX mit GDDR7, Decode (bandbreitenlastig) bleibt auf HBM. Die Last verschiebt sich innerhalb des Rechenzentrums auf andere Speicherarten, nicht aus ihm heraus (siehe datacenter-beats-workstation-per-token). Für die Speicherthese insgesamt egal, für den HBM-Anteil nicht. Einschätzung im Gespräch: 10 bis 15 %, dass das bis 2030 sichtbar wird, gesenkt von 20 %, weil die Hauptlast (Simulation, Weltmodelle, Robotik-Training) große Modelle auf großen Clustern sind (every-sector-grows-sum-counts). Ablesung: HBM-Anteil am DRAM-Umsatz gegen Inferenz-Umsatz.

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
- [datacenter-beats-workstation-per-token](../mechanisms/datacenter-beats-workstation-per-token.md)
- [every-sector-grows-sum-counts](../mechanisms/every-sector-grows-sum-counts.md)
