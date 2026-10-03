# TODO

Automatisch erzeugt von `tools/general/wiki_maintenance` am 2026-10-03. Nicht von Hand bearbeiten:
Änderungen gehören in den jeweiligen Eintrag, danach Liste neu erzeugen.

12 offene Einträge.

## ai_application_layer

- [Mengenbilanz der Beschleuniger](knowledge/ai_application_layer/open_checks/accelerator-mass-balance.md) (pruefpunkt, offen, Stand 2026-10-02)

## ai_buyers

- [Anthropic S-1: Zahlen gegenpruefen](knowledge/ai_buyers/open_checks/anthropic-s1-figures.md) (pruefpunkt, offen, Stand 2026-10-02)
  - [ ] Umsatz je Geschaeftsjahr und Quartal gegen die Laufraten in [anthropic-revenue-runrate](knowledge/ai_buyers/findings/anthropic-revenue-runrate.md) halten. Erwartung: gebuchter Umsatz deutlich unter der Laufrate.
  - [ ] Bruttomarge und Rechenkosten. Bestaetigt der Prospekt die berichteten rund 40 Prozent?
  - [ ] Aufteilung nach API, Abonnements und Grosskunden, gegen die berichteten rund 80 Prozent API.
  - [ ] Vertragliche Mindestabnahmen (purchase obligations, oft in den Anhangangaben) gegen die berichteten Zusagen in [anthropic-compute-commitments](knowledge/ai_buyers/findings/anthropic-compute-commitments.md), inklusive Faelligkeiten je Jahr.
  - [ ] Kundenkonzentration und Einnahmen aus Firmen, die zugleich investiert sind, siehe [circular-financing](knowledge/ai_buyers/risks/circular-financing.md).
  - [ ] Verlustvortrag und Liquiditaet.

## ai_demand_drivers

- [Capex gegen operativen Cashflow je Hyperscaler, 2026](knowledge/ai_demand_drivers/open_checks/capex-vs-operating-cash-flow-2026.md) (pruefpunkt, offen, Stand 2026-10-02)
- [GB HBM je MW über drei Generationen](knowledge/ai_demand_drivers/open_checks/hbm-gb-per-mw.md) (pruefpunkt, offen, Stand 2026-10-02)
- [Rubin-Anteil an der Blackwell-Basis: nach Stück und nach FLOPS](knowledge/ai_demand_drivers/open_checks/rubin-share-of-blackwell-base.md) (pruefpunkt, offen, Stand 2026-10-02)

## local_llm_operation

- [Lademodus bei Expert-Offloading: mmap oder none?](knowledge/local_llm_operation/open_checks/mmap-vs-load-mode-none.md) (pruefpunkt, offen, Stand 2026-08-29)

## manufacturing_costs

- [Physical AI: Teiletransport zwischen Maschinen](knowledge/manufacturing_costs/open_checks/physical-ai-material-handling.md) (pruefpunkt, offen, Stand 2026-10-02)

## memory_earnings

- [Micron FQ4: HBM gegen konventionelles DRAM](knowledge/memory_earnings/open_checks/micron-fq4-hbm-split.md) (pruefpunkt, offen, Stand 2026-10-02)

## memory_supply

- [DRAM-Waferkapazitaet je Werk](knowledge/memory_supply/open_checks/dram-wafer-capacity-by-fab.md) (pruefpunkt, offen, Stand 2026-10-02)
  - [ ] Fuer jede Zeile eine Tier-1a-Quelle finden (Quartalsbericht, Call, Investorentag) oder die Zeile als unbelegt markieren.
  - [ ] Umruestung von Zubau trennen. Ein Knotenwechsel bringt Bits, aber keine zusaetzlichen Wafer. Fuer die Flaechenrechnung zaehlt nur neuer Reinraum.
  - [ ] Netto-Zuwachs an Waferflaeche je Jahr 2026 bis 2030 rechnen und gegen den HBM-Anteil aus [hbm-eats-wafer-area](knowledge/memory_supply/mechanisms/hbm-eats-wafer-area.md) stellen.
  - [ ] Rohstoffseite pruefen: Fuer blanke Siliziumwafer wird eine Angebotsluecke von 8 Prozent (2026) bis 24 Prozent (2028) berichtet. Quelle und Tier klaeren.
- [HBM-Marktanteil und Nvidias HBM4-Allokation](knowledge/memory_supply/open_checks/hbm-market-share-and-nvidia-allocation.md) (pruefpunkt, offen, Stand 2026-10-02)
  - [ ] Für jede Anteilszeile eine primärnahe Quelle statt Analystenschätzung finden,
  - [ ] Die Nvidia-Allokationsanteile gegen gemeldete HBM-Umsätze der drei Hersteller
  - [ ] Prüfen, ob Samsungs HBM4-Zertifizierung in reale Auslieferung mündet; eine
  - [ ] Anteil gegen die Flächenrechnung aus
- [HBM4- und DRAM-Wafernachfrage durch Rubin und Nachfolger, 2028 bis 2030](knowledge/memory_supply/open_checks/rubin-hbm4-wafer-demand-2028-2030.md) (pruefpunkt, offen, Stand 2026-10-03)

## model_capability_cost

- [Tatsächlich abgerechnetes Inferenzvolumen](knowledge/model_capability_cost/open_checks/billed-inference-volume.md) (pruefpunkt, offen, Stand 2026-10-02)
