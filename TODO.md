# TODO

Automatisch erzeugt von `tools/general/wiki_maintenance` am 2026-10-11. Nicht von Hand bearbeiten:
Änderungen gehören in den jeweiligen Eintrag, danach Liste neu erzeugen.

24 offene Einträge.

## ai_application_layer

- [Mengenbilanz der Beschleuniger](knowledge/ai_application_layer/open_checks/accelerator-mass-balance.md) (pruefpunkt, offen, Stand 2026-10-02)
- [KI-Prüfung im Supply Atlas fortsetzen](knowledge/ai_application_layer/open_checks/supply-atlas-ai-use-level4.md) (pruefpunkt, offen, Stand 2026-10-06)
- [Lücken in ai_use_cases_overview: Kandidatenliste](knowledge/ai_application_layer/open_checks/use-case-overview-gaps.md) (pruefpunkt, offen, Stand 2026-10-05)
  - [ ] Samstag (viel Token-Budget): je Kandidat Webrecherche nach dem Muster des Flughafen-Falls, also Produktion ja/nein, Kennzahl mit Herkunft, Behörde gegen Firmenangabe, Einstufung Reife/Beleg/Wachstum.
  - [ ] Weitere Kandidaten systematisch sammeln: zuerst die Behördenverzeichnisse aus "Suchquellen", dann Lückenliste der Seite (Branchen ohne Karte) Branche für Branche gegen bekannte Produktivfälle halten.
  - [ ] Die zwei möglicherweise zufälligen Treffer gegen die Kartentexte lesen.
  - [ ] Je bestätigter Lücke Kartenentwurf an Mendel, gesammelt eintragen (Schreibzugriff auf ai_use_cases_overview nötig).
- [Einsatzorte: zweiter Durchgang und neue Kartenhinweise](knowledge/ai_application_layer/open_checks/use-case-places-second-pass.md) (pruefpunkt, offen, Stand 2026-10-07)

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

## compute_bottlenecks

- [Zuteilung schlägt Datenblatt](knowledge/compute_bottlenecks/mechanisms/allocation-beats-datasheet.md) (mechanismus, vorschlag, Stand 2026-10-03)
  - [ ] CoWoS-Anteile Nvidia, AMD, Broadcom 2026 und 2027 aus TSMC-Calls oder Herstellerangaben statt Analysten.
  - [ ] AMD-Data-Center-Umsatz in GPU und CPU aufteilen (Segmentangaben, Calls).
  - [ ] Samsung-HBM4-Freigabe für MI455X und tatsächliche Auslieferung.
  - [ ] Erste unabhängige Messung von MI455X (MLPerf) gegen Rubin je GPU.

## lesion_detection_method

- [PVS: die Laesionsmethode anwenden, bevor ein Modell gebaut wird](knowledge/lesion_detection_method/open_checks/pvs-apply-the-lesion-method.md) (pruefpunkt, offen, Stand 2026-10-07)
- [WMH: die Methode aus CMB und PVS noch einmal anwenden](knowledge/lesion_detection_method/open_checks/wmh-apply-the-lesion-method.md) (pruefpunkt, offen, Stand 2026-10-09)
  - [ ] M1-M3 eingereiht 2026-10-09 (lokaler Agent); M4 braucht ~2 Tage GPU und pausiert das Sprachmodell.

## local_llm_operation

- [Entscheidungsmodell als Weiche zwischen Modellprofilen: nur zwischen RESIDENTEN Modellen](knowledge/local_llm_operation/open_checks/decision-model-as-profile-orchestrator.md) (pruefpunkt, offen, Stand 2026-10-08)
- [Weniger Denken bei einem dichten 27B: schneller als das MoE auf 8 GB?](knowledge/local_llm_operation/open_checks/dense-27b-vs-moe-on-8gb.md) (pruefpunkt, offen, Stand 2026-10-04)
- [Lokaler Arbeitsplatz, Stand Oktober 2026: was auf 8 und 24 GB zu messen lohnt](knowledge/local_llm_operation/open_checks/local-stack-landscape-2026-10.md) (pruefpunkt, offen, Stand 2026-10-06)
  - [ ] `--n-cpu-moe` 15–40 mit `llama-bench`, pp512/tg128, `-ub 512` gegen `-ub 4096`.
  - [ ] MTP an/aus, `--spec-draft-n-max` 1/2/3, Akzeptanz bei Code und Prosa.
  - [ ] KV f16/q8/q4 mit `llama-perplexity --kl-divergence` auf eigenen Agent-Logs.
  - [ ] Time-to-first-token ab Turn 2 mit/ohne `--cache-ram`, volles gegen reduziertes Tool-Set.
  - [ ] Laya gegen Arch-Router gegen Embedding+kNN auf den 60 Routing-Fällen in local_models `tools/laya/faelle/route.jsonl`.
  - [ ] 50 gefährliche und 50 harmlose Shell-Befehle: Regelparser gegen Granite Guardian 4.1.
- [Kleiner Harness statt kleineres Modell?](knowledge/local_llm_operation/open_checks/minimal-harness-prompt-size.md) (pruefpunkt, offen, Stand 2026-10-04)
- [Lademodus bei Expert-Offloading: mmap oder none?](knowledge/local_llm_operation/open_checks/mmap-vs-load-mode-none.md) (pruefpunkt, offen, Stand 2026-08-29)
- [Wie viel Thinking brauchen Routineaufgaben im Agenten?](knowledge/local_llm_operation/open_checks/reasoning-effort-for-routine-agent-tasks.md) (pruefpunkt, offen, Stand 2026-10-04)

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

## mri_qc_viewers

- [Den Schichtbetrachter als Tool unter tools/mri/ einstellen](knowledge/mri_qc_viewers/open_checks/slice-viewer-as-shared-tool.md) (pruefpunkt, offen, Stand 2026-10-08)
