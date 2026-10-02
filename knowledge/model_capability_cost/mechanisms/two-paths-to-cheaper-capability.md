---
id: two-paths-to-cheaper-capability
typ: mechanismus
status: getragen
thema: knowledge/model_capability_cost
stand: 2026-10-02
herkunft: Projekt ai_modellkurve, Datenstand 2026-09-05
verweist_auf: [iso-capability-cost-halving]
---

# Fähigkeit wird auf zwei getrennten Wegen billiger

## Aussage
Eine fallende Iso-Kostenkurve entsteht aus zwei Vorgängen, die auseinandergehalten werden müssen:

1. **Echte Preissenkung.** Dasselbe Modell wird billiger. Klarster Beleg: OpenAI senkte den o3-Preis am 10.06.2025 um 80 Prozent von 10 / 40 auf 2 / 8 USD je Mio. Token und nannte als einzigen Grund den optimierten Inferenzstapel — "same exact model, just cheaper". Zweiter Beleg: Gemini 1.5 Pro von 3,50 / 10,50 USD (Stand 2024-07-01) auf 1,25 / 5,00 USD (Stand 2024-11-16).
2. **Modellwechsel.** Ein anderes Modell erreicht dasselbe Niveau billiger. Beispiel: Claude Opus 4.5 erreichte im November 2025 einen höheren SWE-bench-Wert als Opus 4.1 zu 5 / 25 statt 15 / 75 USD.

Der zweite Weg ist der häufigere: in den sieben Treppen aus [iso-capability-cost-halving](../findings/iso-capability-cost-halving.md) sind von 32 Stufen nur zwei echte Preissenkungen (o3 am 10.06.2025, Gemini 1.5 Pro am 16.11.2024). Das liegt auch an der Quellenlage: eine Preissenkung ist nur sichtbar, wenn für dasselbe Modell zwei datierte Preisstände belegt sind, und das gilt für 9 der 90 Modelle.

## Trägt
Die Trennung von Hardware- und Modellargument. Weg 1 misst, wie viel billiger dieselbe Rechenleistung geworden ist; dort wirken Auslastung, Quantisierung, Inferenzoptimierung und Anbietermarge. Weg 2 misst, wie viel weniger Rechenleistung für dasselbe Ergebnis nötig ist; dort wirken Architektur, Destillation und Training. Nur Weg 1 lässt sich sinnvoll gegen eine Chipkurve halten.

## Trägt nicht
Eine Aussage über Kosten des Anbieters. Eine Preissenkung kann Marge abgeben statt Kostenvorteil weiterzureichen; aus dem Preis allein ist das nicht zu trennen. Umgekehrt kann ein Anbieter einen Kostenvorteil behalten, und die Treppe bleibt stehen, obwohl Rechnen billiger wurde.

## Bruchindikator
Weg 1 verschwindet ganz: über zwölf Monate keine Preissenkung an einem bestehenden Modell. Dann wird nur noch über neue Modelle verbilligt, und die Anbieter geben Effizienzgewinne nicht mehr weiter.

## Ablesung
o3-Senkung: OpenAI Developers, 2026-06-10, Tier 1b, https://x.com/OpenAIDevs/status/1932532777565446348.
Gemini-1.5-Pro-Preise: archivierte Fassungen von ai.google.dev/pricing vom 2024-07-01 und 2024-11-16, Tier 1b.
Opus-4.5-Preis: Anthropic, Ankündigung vom 2025-11-24, Tier 1b, https://www.anthropic.com/news/claude-opus-4-5.
Alles abgerufen 2026-09-05.

## Verknüpft
- [iso-capability-cost-halving](../findings/iso-capability-cost-halving.md)
