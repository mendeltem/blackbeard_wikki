---
id: gpu-memory-absorbs-fab-additions
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-03
herkunft: These Mendel, durchgerechnet im Projekt AI_news, 2026-10-03
verweist_auf: [open-search-space, unverifiable-rival-position, bandwidth-bottleneck, hbm-eats-wafer-area, ddr5-hbm-per-wafer-opportunity-cost, rubin-hbm4-wafer-demand-2028-2030, capex-discipline-after-2023, cxmt-ramp, financing-limit, hbm-gb-per-mw-three-generations, no-standard-cycle-without-absorption-check]
---

# Mehr Speicher je GPU frisst den Fab-Zubau

## Aussage
These (Mendel, 2026-10-03): DRAM-Wafer bleiben bis 2030 knapp, weil zusätzliche Kapazität nicht als Überangebot ankommt, sondern sofort in mehr Speicher je GPU fließt. Der Standard-Schweinezyklus (Knappheit → Capex → Überangebot → Preisverfall) setzt voraus, dass die Nachfrage je Einheit fest ist. Bei KI-Beschleunigern ist sie das nicht: Das Design wird an das verfügbare HBM angepasst.

Wirkungskette:

    HBM-Wafer/Monat = Packages/Jahr × GB HBM je Package / GB je HBM-Wafer / 12 / Nvidia-Anteil an HBM
    Wafer für konv. DRAM = Kapazität − HBM-Wafer − LPDDR-Wafer der KI-CPUs
    Knappheit bleibt, solange (GB je Package × Packages) schneller wächst als (GB je Wafer × Kapazität)

Größenordnung (Rechnung in [rubin-hbm4-wafer-demand-2028-2030](../open_checks/rubin-hbm4-wafer-demand-2028-2030.md)):
- GB HBM je Package je Generation: 192 (B200) → 288 (B300, Rubin) → 683 bis 1.024 (Rubin Ultra) → Feynman offen. Faktor 3 bis 5.
- GB je HBM-Wafer im selben Zeitraum: rund 320 (HBM4) → 400 bis 460 (HBM4E). Faktor rund 1,4.
- Selbst bei +10 % DRAM-Kapazität je Jahr passen ohne Verdrängung von konventionellem DRAM nur rund 355 GB je Package (2029) bzw. 500 GB (2030). 1 TB je Package bei 6 bis 7 Mio. Packages im Jahr bräuchte 2029 rund 2 Mio. HBM-Wafer im Monat, etwa die gesamte DRAM-Kapazität von 2026.
- HBM4 braucht für dieselben 288 GB rund 33 % mehr Wafer als HBM3E (Tauschverhältnis 4 statt 3). Rubin erhöht die Wafernachfrage also schon ohne mehr GB.
- Zusätzlich: Vera-CPU mit 1,5 TB LPDDR5X (54 TB je NVL72-Rack, 750 GB je GPU) zieht rund 7 % der DRAM-Wafer aus dem konventionellen Pool.

Beleg für die Richtung: Rubin Ultra wird laut TrendForce (August 2026) wegen HBM-Knappheit von 1 TB auf rund zwei Drittel gekürzt, auch die Vera-LPDDR-Ausstattung wird Berichten zufolge gekürzt. Die Nachfrage je Package liegt also schon heute über dem Angebot. Jede freie Kapazität hat einen wartenden Abnehmer.

## Trägt
- Warum ein Fab-Zubau 2027 bis 2030 (Yongin, P5, ID1, M15X) nicht automatisch zum Überangebot führt: Die Lücke zwischen gewünschtem und lieferbarem Speicher je Package ist größer als jeder geplante Zubau.
- Warum der Standardzyklus als Default-Argument nicht reicht, siehe Regel [no-standard-cycle-without-absorption-check](../rules/no-standard-cycle-without-absorption-check.md).
- Wo die Knappheit ankommt, entscheiden die Hersteller über die Waferaufteilung: entweder wird HBM rationiert (weniger GB je Package, weniger Ultra), oder konventionelles DRAM wird verdrängt (DDR/LPDDR-Preise steigen). Siehe [ddr5-hbm-per-wafer-opportunity-cost](ddr5-hbm-per-wafer-opportunity-cost.md).

Warum die Stückzahl halten soll (gesetzt, nicht belegt): Die Bedingung des Mechanismus, dass GB je Package × Stückzahl weiter steigt, stützt sich auf die drei Axiome in [ai_demand_drivers](../../ai_demand_drivers/INDEX.md):
1. [Offener Suchraum](../../ai_demand_drivers/axioms/open-search-space.md): Zusätzliche Rechenleistung findet Ertrag, die Nachfrage ist in keiner Anwendungsklasse gesättigt.
2. [Unprüfbare Gegnerposition (Investitionszwang, Wettrüsten)](../../ai_demand_drivers/axioms/unverifiable-rival-position.md): Kein Spieler kann die Position des Gegners prüfen, Investieren ist dominant. Auf Staatenebene sehr stabil, auf Firmenebene weniger.
3. [Bandbreiten-Engpass](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md): Der Speicher ist der Engpass, deshalb fließt jede Entlastung zuerst in mehr und schnelleren Speicher je Beschleuniger.

Diese drei sind Setzungen von Mendel. Was hier daran hängt, ist als gesetzt zu lesen. Gegenkraft ist die [Finanzierungsgrenze](../../ai_demand_drivers/mechanisms/financing-limit.md): Wollen ist nicht Können, der Bruch kann auf Firmenebene erzwungen kommen.

## Trägt nicht
- Unbedingt. Der Mechanismus braucht, dass GB je Package × Stückzahl weiter steigt. Fällt die Stückzahl, weil die Käufer an die [Finanzierungsgrenze](../../ai_demand_drivers/mechanisms/financing-limit.md) stoßen, wirkt der Zubau entlastend (Gegenargument, geschätzt rund 30 %).
- Für konventionelles DRAM allein: CXMT baut DDR/LPDDR aus, liefert aber kein HBM an Nvidia ([cxmt-ramp](../risks/cxmt-ramp.md)). HBM kann knapp bleiben, während DDR sich entspannt (rund 25 %).
- Dass Nvidia Speicher maximiert. Bis B300 ist GB HBM je MW seit 2020 nicht gestiegen ([hbm-gb-per-mw-three-generations](../../ai_demand_drivers/findings/hbm-gb-per-mw-three-generations.md)). Der Sprung kommt erst mit Rubin Ultra, und der ist noch nicht ausgeliefert.
- Die Prozentzahlen. Sie hängen an Annahmen (siehe Prüfpunkt). Robust ist nur das Verhältnis Faktor 3 bis 5 gegen Faktor 1,4.

Wahrscheinlichkeiten (Einschätzung des rechnenden Agenten, 2026-10-03, nicht Mendels): Mechanismus wirkt, solange die Stückzahl hält, rund 70 %. HBM-Wafer knapp bis Ende 2030 rund 60 %. DRAM insgesamt durchgehend knapp bis 2030 rund 45 %.

## Bruchindikator
- Nvidias nächste Generation hält oder senkt GB je Package, obwohl mehr HBM verfügbar ist.
- DDR5-Vertragspreise fallen zwei Quartale in Folge.
- Hersteller melden einen sinkenden HBM-Anteil an den Waferstarts.
- Hyperscaler-Capex flacht ab oder fällt ([capex-vs-operating-cash-flow-2026](../../ai_demand_drivers/open_checks/capex-vs-operating-cash-flow-2026.md)).

## Ablesung
Speicher je Package: Herstellerspezifikationen, Tier 1b. Kürzung Rubin Ultra und Vera-LPDDR: TrendForce und Presse, Warnsignal. Kapazitäten und HBM-Wafer-Anteil: Branchendienste. GB je Wafer, Stückzahlen, Nvidia-Anteil: Annahmen.

## Verknüpft
- [open-search-space](../../ai_demand_drivers/axioms/open-search-space.md) (Axiom 1)
- [unverifiable-rival-position](../../ai_demand_drivers/axioms/unverifiable-rival-position.md) (Axiom 2, Wettrüsten)
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md) (Axiom 3)
- [rubin-hbm4-wafer-demand-2028-2030](../open_checks/rubin-hbm4-wafer-demand-2028-2030.md)
- [no-standard-cycle-without-absorption-check](../rules/no-standard-cycle-without-absorption-check.md)
- [hbm-eats-wafer-area](hbm-eats-wafer-area.md)
- [ddr5-hbm-per-wafer-opportunity-cost](ddr5-hbm-per-wafer-opportunity-cost.md)
- [capex-discipline-after-2023](capex-discipline-after-2023.md)
- [cxmt-ramp](../risks/cxmt-ramp.md)
- [financing-limit](../../ai_demand_drivers/mechanisms/financing-limit.md)
- [hbm-gb-per-mw-three-generations](../../ai_demand_drivers/findings/hbm-gb-per-mw-three-generations.md)
