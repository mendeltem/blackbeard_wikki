---
id: iso-capability-cost-halving
typ: befund
status: getragen
thema: knowledge/model_capability_cost
stand: 2026-10-02
herkunft: Projekt ai_modellkurve, Datenstand 2026-09-05
verweist_auf: [two-paths-to-cheaper-capability, model-cost-falls-faster-than-hardware, benchmarks-from-one-hand, fixed-levels-stopped-falling-2026, token-billing-scales-with-tasks]
---

# Iso-Fähigkeitskosten halbieren sich alle 1,6 bis 7,3 Monate

## Aussage
Für ein festes Fähigkeitsniveau kostet eine Million Ausgabetoken beim jeweils billigsten Modell, das dieses Niveau erreicht:

| Niveau | erster Punkt | letzter Punkt | Faktor | Monate je Halbierung | Stufen |
|---|---|---|---|---|---|
| SWE-bench Verified ≥ 30 % | 10,00 USD (GPT-4o, 2024-11-20) | 1,98 USD (DeepSeek-V4-Pro, 2026-04-24) | 5,1 | 7,3 | 4 |
| SWE-bench Verified ≥ 50 % | 15,00 USD (Claude 3.7 Sonnet, 2025-02-24) | 1,98 USD (DeepSeek-V4-Pro, 2026-04-24) | 7,6 | 4,8 | 4 |
| SWE-bench Verified ≥ 70 % | 75,00 USD (Claude Opus 4, 2025-05-22) | 1,98 USD (DeepSeek-V4-Pro, 2026-04-24) | 37,9 | 2,1 | 4 |
| GPQA Diamond ≥ 30 % | 60,00 USD (GPT-4, 2023-03-14) | 0,40 USD (GPT-5 nano, 2025-08-07) | 150,0 | 4,0 | 5 |
| GPQA Diamond ≥ 50 % | 15,00 USD (Claude 3.5 Sonnet, 2024-06-20) | 0,40 USD (GPT-5 nano, 2025-08-07) | 37,5 | 2,6 | 6 |
| GPQA Diamond ≥ 70 % | 60,00 USD (o1, 2024-12-17) | 0,42 USD (DeepSeek-V3.2, 2025-12-01) | 142,9 | 1,6 | 4 |
| GPQA Diamond ≥ 90 % | 12,00 USD (Gemini 3 Pro, 2025-11-18) | 0,66 USD (DeepSeek-V4-Flash, 2026-07-31) | 18,2 | 2,0 | 4 |

Halbwertszeit abgelesen: erster gegen letzten Punkt der Treppe, geteilt durch die Zahl der Halbierungen dazwischen. Nicht angepasst, keine Regression.

## Trägt
Die Mengenseite jeder Nachfragethese. Fällt der Preis je Fähigkeitseinheit um Faktor 38 bis 150 in zwei Jahren, wird bei gleichem Budget ein Vielfaches an Token nachgefragt. Das ist der Mechanismus, über den Capex in Auslastung umschlägt, ohne dass Erlöse je Token steigen.

## Trägt nicht
Eine Aussage über Inferenzerlöse. Ein Preis je Token ist kein Umsatz; wie viele Token tatsächlich abgerechnet werden, steht nirgends ([billed-inference-volume](../open_checks/billed-inference-volume.md)).
Auch keine Aussage über Kosten je gelöster Aufgabe: Denkmodelle rechnen unsichtbare Zwischenschritte als Ausgabetoken ab, die Kosten je Aufgabe liegen deutlich über dem Preis je Mio. Token.
Treppen mit vier Stufen sind grob. Die 2,1 Monate bei SWE ≥ 70 % stammen aus vier Punkten über elf Monate und sind die unsicherste Zeile der Tabelle.

## Bruchindikator
Eine Treppe bleibt über zwölf Monate ohne neue Stufe, obwohl Modelle auf dem Niveau erscheinen. Dann fällt der Preis je Fähigkeit nicht mehr, und die Mengenseite trägt nicht weiter. Für die 2025 erreichten Niveaus ist das 2026 bereits eingetreten, siehe [fixed-levels-stopped-falling-2026](fixed-levels-stopped-falling-2026.md).

## Ablesung
Benchmarkwerte: Epoch AI Benchmarking Hub, eigene Messläufe, Tier 1b, https://epoch.ai/data/benchmarks.csv, abgerufen 2026-09-05.
Preise: Preisseiten der Anbieter (OpenAI, Anthropic, Google, DeepSeek, xAI, Z.ai, Moonshot), Tier 1b, sowie archivierte Fassungen derselben Seiten über web.archive.org. Abgerufen 2026-09-05.
Vollständige Sammlung mit Quelle je Zahl: https://github.com/mendeltem/ai_modellkurve, `daten.json`.
Datenstand 2026-09-05, also vier Wochen vor dem Stand dieses Eintrags. Modelle nach diesem Datum fehlen.

## Verknüpft
- [two-paths-to-cheaper-capability](../mechanisms/two-paths-to-cheaper-capability.md)
- [model-cost-falls-faster-than-hardware](../mechanisms/model-cost-falls-faster-than-hardware.md)
- [benchmarks-from-one-hand](../rules/benchmarks-from-one-hand.md)
- [fixed-levels-stopped-falling-2026](fixed-levels-stopped-falling-2026.md)
- [billed-inference-volume](../open_checks/billed-inference-volume.md)
- [token-billing-scales-with-tasks](../../ai_buyers/mechanisms/token-billing-scales-with-tasks.md) — die Gegenrichtung: mehr Modellaufrufe je Aufgabe gegen fallenden Preis je Token
