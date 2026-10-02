---
id: open-weights-lag-is-flat
typ: befund
status: getragen
thema: knowledge/model_capability_cost
stand: 2026-10-02
herkunft: Projekt ai_modellkurve, Datenstand 2026-09-05
verweist_auf: [iso-capability-cost-halving, benchmarks-from-one-hand]
---

# Der Rückstand offener Gewichte schrumpft nicht, er schwankt um vier Monate

## Aussage
Abstand in Monaten zwischen dem Tag, an dem ein geschlossenes Modell ein GPQA-Diamond-Niveau zuerst erreichte, und dem Tag, an dem das erste Modell mit offenen Gewichten dieses Niveau überbot:

| Datum | Rückstand | offenes Modell | holt auf zu |
|---|---|---|---|
| 2023-07-18 | 4,1 | Llama 2 70B (26,3 %) | GPT-4 |
| 2024-04-18 | 5,4 | Llama 3 70B (40,6 %) | GPT-4 Turbo |
| 2024-07-23 | 1,1 | Llama 3.1 405B (50,9 %) | Claude 3.5 Sonnet |
| 2024-12-26 | 3,1 | DeepSeek-V3 (56,5 %) | Gemini 1.5 Pro |
| 2025-01-20 | 1,1 | DeepSeek-R1 (71,7 %) | o1 |
| 2025-08-05 | 7,6 | gpt-oss-120b (75,8 %) | o1 |
| 2025-11-06 | 4,7 | Kimi K2 Thinking (84,2 %) | Gemini 2.5 Pro |
| 2026-01-27 | 2,5 | Kimi K2.5 (87,6 %) | GPT-5.1 |
| 2026-02-11 | 2,8 | GLM-5 (87,8 %) | Gemini 3 Pro |
| 2026-04-07 | 4,6 | GLM-5.1 (89,9 %) | Gemini 3 Pro |
| 2026-04-20 | 5,0 | Kimi K2.6 (90,8 %) | Gemini 3 Pro |
| 2026-04-24 | 5,2 | DeepSeek-V4-Pro (90,9 %) | Gemini 3 Pro |
| 2026-06-16 | 6,9 | GLM-5.2 (91,9 %) | Gemini 3 Pro |
| 2026-07-16 | 4,8 | Kimi K3 (93,1 %) | Gemini 3.1 Pro |

Mittel China 4,1 Monate (n = 10), Mittel übrige Herkunft 4,5 Monate (n = 4). Über dreieinhalb Jahre kein Trend nach unten.

## Trägt
Die Aussage, dass das Spitzenniveau rund ein halbes Jahr lang exklusiv bleibt — aber eben auch, dass es nicht kürzer wird. Wer mit einem schrumpfenden Abstand argumentiert, hat dafür in diesen Daten keine Stütze.
Zusätzlich: die billigsten Punkte fast aller Kostentreppen sind Modelle mit offenen Gewichten chinesischer Häuser (DeepSeek, Z.ai, Moonshot). Der Preisdruck kommt von dort.

## Trägt nicht
Eine Aussage über Marktanteile oder Nutzung. Gemessen ist allein, wann welches Niveau zuerst erreicht wurde.
Der Unterschied zwischen China (4,1) und dem Rest (4,5) ist bei n = 10 gegen n = 4 nicht belastbar; die oft erzählte Trennung US gegen CN zeigt sich in diesen Zahlen nicht.
Die Reihe stützt sich auf einen einzigen Benchmark. GPQA Diamond sättigt oberhalb 90 %, die letzten Zeilen messen deshalb immer kleinere Unterschiede.

## Bruchindikator
Drei aufeinanderfolgende Einträge unter zwei Monaten: dann schrumpft der Abstand wirklich, und die Preissetzung der geschlossenen Anbieter verliert ihre Grundlage.

## Ablesung
Epoch AI Benchmarking Hub, eigene Messläufe GPQA Diamond, Tier 1b, https://epoch.ai/data/benchmarks.csv, abgerufen 2026-09-05.
Lizenzlage der Gewichte je Modell aus Epoch AI Notable AI Models, Tier 1b, abgerufen 2026-09-05. "Offen" umfasst hier auch Lizenzen mit Auflagen (Llama).

## Verknüpft
- [iso-capability-cost-halving](iso-capability-cost-halving.md)
- [benchmarks-from-one-hand](../rules/benchmarks-from-one-hand.md)
