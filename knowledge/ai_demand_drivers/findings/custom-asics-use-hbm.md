---
id: custom-asics-use-hbm
typ: befund
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Projekt Artificial Intelligence (KI-Compute-Stack), Report AI Accelerators Beyond NVIDIA (Mai 2026), eingetragen 2026-10-02
verweist_auf: [bandwidth-bottleneck, hbm-bypass-architectures]
---

# Hyperscaler-ASICs verbauen HBM

## Aussage
HBM je Chip laut Report: Google TPU v7 Ironwood 192 GB HBM3E, AWS Trainium3 144 GB HBM3E, AMD MI355X 288 GB HBM3E, Meta MTIA 300 rund 216 GB, MTIA 400 und 450 je 288 GB, MTIA 500 384 bis 512 GB. Meta MTIA 100 und 200 liefen auf LPDDR5 (Ranking und Empfehlung), ab MTIA 300 wechselt Meta auf HBM.

## Trägt
Marktanteilsverluste von NVIDIA an Eigenentwicklungen der Hyperscaler senken die HBM-Nachfrage nicht. Der Wechsel von Meta ist ein Fall, der das Axiom bandwidth-bottleneck stützt.

## Trägt nicht
Stückzahlen. Der Speicher je Chip sagt nichts darüber, wie viele Chips gebaut werden. Ein Fall (Meta) ist keine Regel.

## Bruchindikator
Eine neue Hyperscaler-Generation für generative Inferenz kommt ohne HBM aus.

## Ablesung
Herstellerangaben (Blogs, Datenblätter), Tier 1b. Zahlen aus dem Projekt-Report übernommen, gegen die Primärquelle nicht nachgeprüft.

## Verknüpft
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [hbm-bypass-architectures](../risks/hbm-bypass-architectures.md)
