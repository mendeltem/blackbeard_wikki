---
id: fixed-levels-stopped-falling-2026
typ: befund
status: getragen
thema: knowledge/model_capability_cost
stand: 2026-10-02
herkunft: Projekt ai_modellkurve, Datenstand 2026-09-05
verweist_auf: [iso-capability-cost-halving, billed-inference-volume]
---

# 2026 fiel der Preis für bereits erreichte Niveaus kaum noch

## Aussage
Verhältnis des Preises am Jahresanfang zu dem am Jahresende, je Fähigkeitsniveau, das am Jahresanfang schon erreichbar war:

| Jahr | SWE-bench ≥ 30 % | SWE-bench ≥ 70 % | GPQA ≥ 50 % | GPQA ≥ 70 % | GPQA ≥ 90 % | erstmals erreicht in diesem Jahr |
|---|---|---|---|---|---|---|
| 2024 | — | — | — | — | — | SWE ≥ 30 %, GPQA ≥ 50 %, GPQA ≥ 70 % |
| 2025 | × 7,5 | — | × 2,8 | × 142,9 | — | SWE ≥ 50 %, SWE ≥ 70 %, GPQA ≥ 90 % |
| 2026 | × 1,0 | × 1,5 | × 1,0 | × 1,0 | × 18,2 | SWE ≥ 80 % |

Bis einschließlich Stand 2026-09-05 ist der Zugewinn des Jahres 2026 fast vollständig in Niveaus gewandert, die 2025 noch niemand erreichte. Für die alten Niveaus steht die Treppe still.

## Trägt
Die Lesart, dass der Preisverfall je Fähigkeit nicht gleichmäßig läuft, sondern an der Front stattfindet. Wer eine Anwendung auf einem 2025er Niveau betreibt, hat 2026 keine Kostenentlastung bekommen.

## Trägt nicht
Eine Trendwende. Es sind neun Monate eines Jahres, bei vier bis sechs Stufen je Treppe. Eine einzige Veröffentlichung eines billigen Modells auf altem Niveau macht die Zeile wieder zunichte.
Auch keine Aussage über die Gesamtausgaben: wandern Nutzer auf das neue, teurere Spitzenniveau, steigen die Ausgaben trotz fallender Preise an der Front.

## Bruchindikator
Ein Modell unterbietet im vierten Quartal 2026 den Preis von 1,98 USD je Mio. Ausgabetoken auf SWE-bench ≥ 30 % oder ≥ 70 % deutlich. Dann war der Stillstand eine Lücke im Veröffentlichungstakt, kein Sättigungseffekt.

## Ablesung
Gerechnet aus derselben Sammlung wie [iso-capability-cost-halving](iso-capability-cost-halving.md): Epoch AI Benchmarking Hub Tier 1b, Anbieterpreisseiten Tier 1b, Stand 2026-09-05.
Die Spalten mit "—" sind nicht leer, weil nichts gemessen wurde, sondern weil das Niveau am Jahresanfang noch nicht erreichbar war.

## Verknüpft
- [iso-capability-cost-halving](iso-capability-cost-halving.md)
- [billed-inference-volume](../open_checks/billed-inference-volume.md)
