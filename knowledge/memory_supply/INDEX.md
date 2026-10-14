# memory_supply

Angebotsseite des Speichers: Waferflaeche, Werke, Knoten und was die Flaechenaufteilung zwischen HBM und konventionellem DRAM fuer Bits und Preise bedeutet. Die Nachfrageseite steht in [ai_demand_drivers](../ai_demand_drivers/INDEX.md), die Ergebnisrechnung in [memory_earnings](../memory_earnings/INDEX.md).

Vor jedem Argument mit dem Standardzyklus (Knappheit, Capex, Überangebot) gilt die Regel [Kein Standardzyklus ohne Absorptionsprüfung](rules/no-standard-cycle-without-absorption-check.md): erst zeigen, dass der Zubau nicht von mehr Speicher je GPU aufgefressen wird ([Mechanismus](mechanisms/gpu-memory-absorbs-fab-additions.md)).

Stand 2026-10-14. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [HBM frisst Waferflaeche](mechanisms/hbm-eats-wafer-area.md) | mechanismus | vorschlag |
| [Opportunitaetskosten je Wafer: DDR5 gegen HBM](mechanisms/ddr5-hbm-per-wafer-opportunity-cost.md) | mechanismus | vorschlag |
| [DRAM-Waferkapazitaet je Werk](open_checks/dram-wafer-capacity-by-fab.md) | pruefpunkt | offen |
| [Capex-Disziplin nach den Verlusten 2023](mechanisms/capex-discipline-after-2023.md) | mechanismus | vorschlag |
| [Fab-Vorlaufzeiten: zwei Beispiele mit 4 bis 5 Jahren](findings/fab-lead-time-examples.md) | befund | vorschlag |
| [ASML: Speicher fast die Hälfte der Systemumsätze, +75 % im Jahr 2026](findings/asml-memory-share-of-litho-2026.md) | befund | getragen |
| [Kapazitätshochlauf in China (CXMT, YMTC)](risks/cxmt-ramp.md) | risiko | vorschlag |
| [HBM-Marktanteil und Nvidias HBM4-Allokation](open_checks/hbm-market-share-and-nvidia-allocation.md) | pruefpunkt | offen |
| [Mehr Speicher je GPU frisst den Fab-Zubau](mechanisms/gpu-memory-absorbs-fab-additions.md) | mechanismus | vorschlag |
| [HBM4- und DRAM-Wafernachfrage durch Rubin und Nachfolger, 2028 bis 2030](open_checks/rubin-hbm4-wafer-demand-2028-2030.md) | pruefpunkt | offen |
| [Kein Standardzyklus ohne Absorptionsprüfung](rules/no-standard-cycle-without-absorption-check.md) | regel | getragen |
| [Die eigene Darstellung ist keine Quelle](rules/own-visualisation-is-not-a-source.md) | regel | vorschlag |
