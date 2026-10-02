# model_capability_cost

Was ein Fähigkeitsniveau kostet und wie schnell dieser Preis fällt. Die Gegenseite — warum die Nachfrage nach Speicher hoch bleibt — steht in [ai_demand_drivers](../ai_demand_drivers/INDEX.md); dort gilt auch die Regel [Nachfrage ist nicht Earnings](../ai_demand_drivers/rules/demand-is-not-earnings.md), die hier sinngemäß ebenso gilt: ein Preis je Token ist kein Umsatz.

Datengrundlage ist Projekt ai_modellkurve mit Stand 2026-09-05: 90 Modellveröffentlichungen von GPT-3 bis GPT-6 Astra, Benchmarkwerte von Epoch AI, Preise von den Anbieterseiten und aus deren archivierten Fassungen. Vollständige Sammlung mit Quelle je Zahl: https://github.com/mendeltem/ai_modellkurve

Stand 2026-10-02. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Iso-Fähigkeitskosten halbieren sich alle 1,6 bis 7,3 Monate](findings/iso-capability-cost-halving.md) | befund | getragen |
| [2026 fiel der Preis für bereits erreichte Niveaus kaum noch](findings/fixed-levels-stopped-falling-2026.md) | befund | getragen |
| [Der Rückstand offener Gewichte schrumpft nicht](findings/open-weights-lag-is-flat.md) | befund | getragen |
| [Fähigkeit wird auf zwei getrennten Wegen billiger](mechanisms/two-paths-to-cheaper-capability.md) | mechanismus | getragen |
| [Die Modellkostenkurve fällt schneller als die Hardwarekurve](mechanisms/model-cost-falls-faster-than-hardware.md) | mechanismus | getragen |
| [Benchmarkreihen nur aus einer Hand](rules/benchmarks-from-one-hand.md) | regel | getragen |
| [Tatsächlich abgerechnetes Inferenzvolumen](open_checks/billed-inference-volume.md) | pruefpunkt | offen |
