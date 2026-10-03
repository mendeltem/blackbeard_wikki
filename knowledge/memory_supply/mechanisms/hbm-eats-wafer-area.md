---
id: hbm-eats-wafer-area
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-02
herkunft: Projekt NVIDIA-Roadmap, Seite waferklemme.html, 2026-09
verweist_auf: [bandwidth-bottleneck, demand-is-not-earnings, ddr5-hbm-per-wafer-opportunity-cost]
---

# HBM frisst Waferflaeche

## Aussage
HBM wird nicht neben konventionellem DRAM gefertigt, sondern aus derselben Waferflaeche. Je Bit braucht HBM wegen TSVs, Testlogik, Stapelverlusten und schlechterer Ausbeute das Drei- bis Vierfache an Flaeche. Der Bit-Anteil von HBM faellt deshalb deutlich kleiner aus als sein Wafer-Anteil, und ein wachsender HBM-Anteil schrumpft die Bitmenge fuer DDR und LPDDR, selbst wenn die Gesamtkapazitaet in Wafern waechst.

Rechenweg:

    Bits je Wafer = Basis-Bits je Wafer / Tauschverhaeltnis
    Tauschverhaeltnis: DDR5 1x, GDDR7 rund 1,7x, HBM3E rund 3x, HBM4 rund 4x
    Flaeche fuer DDR = Gesamtkapazitaet x (1 - HBM-Wafer-Anteil)

Groessenordnungen, auf denen dieser Eintrag beruht (Annahmen, siehe Ablesung): HBM-Anteil an der DRAM-Waferzufuhr 18 Prozent (2025), 22 Prozent (2026), rund 30 Prozent (2027), bei einem Bit-Anteil von etwa 8, 9 und 13 Prozent.

Zerlegung des Tauschverhältnisses (Report SK Hynix and the Memory Supercycle, Mai 2026, Sekundärquelle; übernommen aus dem aufgelösten Eintrag hbm-wafer-penalty): HBM-Die 35 bis 45 Prozent größer als DDR5 bei gleicher Kapazität, Ausbeute 20 bis 30 Prozent niedriger (inklusive TSV), Durchlauf 1,5 bis 2 Monate länger. Für HBM4E wird ein Verhältnis über 4 erwartet.

## Traegt
Die Richtung: Steigt der HBM-Wafer-Anteil schneller als die Gesamtkapazitaet, sinkt die absolute Bitmenge fuer konventionelles DRAM. Bei plus 5 Prozent Kapazitaet im Jahr und dem genannten Anteilspfad schrumpft die DDR-Flaeche bis 2027 um knapp 6 Prozent.

## Traegt nicht
Die konkreten Prozentwerte. Sie stammen aus Branchendiensten und sind kein Befund. Auch keine Aussage ueber Preise: Knappheit an Bits ist nicht Preisniveau, dafuer gilt [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md).

Das Tauschverhaeltnis ist eine Faustzahl. Es aendert sich mit Lagenzahl, Ausbeute und Knoten und muesste je Generation neu bestimmt werden.

## Bruchindikator
- Ein Hersteller weist Wafer- und Bit-Anteil von HBM getrennt aus und die Werte liegen deutlich neben den Annahmen.
- Hybrid Bonding oder 3D-DRAM senken die Flaeche je HBM-Bit messbar, dann faellt das Tauschverhaeltnis.
- Der HBM-Wafer-Anteil stagniert, weil Hersteller Flaeche zurueck zu DDR verschieben, siehe [ddr5-hbm-per-wafer-opportunity-cost](ddr5-hbm-per-wafer-opportunity-cost.md).

## Ablesung
Anteile und Tauschverhaeltnisse aus Branchendiensten (TrendForce, The Elec) und Presseberichten, also Warnsignal, kein Befund. Tier 1a waere eine Aufteilung der Waferstarts je Produktklasse in einem Quartalsbericht oder Call.

## Verknuepft
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
- [ddr5-hbm-per-wafer-opportunity-cost](ddr5-hbm-per-wafer-opportunity-cost.md)
- [dram-wafer-capacity-by-fab](../open_checks/dram-wafer-capacity-by-fab.md)
