---
id: rubin-share-of-blackwell-base
typ: pruefpunkt
status: offen
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Projekt AI_news (Gespräch Rubin gegen Blackwell), 2026-09-30 bis 2026-10-01
verweist_auf: [rubin-shipments-start-q3-fy27, hbm-gb-per-mw-three-generations, accelerator-mass-balance, announced-is-not-built]
---

# Rubin-Anteil an der Blackwell-Basis: nach Stück und nach FLOPS

## Aussage
Offene Rechnung: Wie groß ist die ausgelieferte Rubin-Menge im Verhältnis zur kumulierten Blackwell-Menge? Erster Durchgang mit Stichtag 30.09.2026, jede Zahl mit Herkunft:

| Größe | Wert | Herkunft |
|---|---|---|
| Rubin-Umsatz bis Stichtag | 8 bis 13 Mrd. $ | Annahme: 20 Mrd. Quartalsprognose, Stichtag bei zwei Dritteln, Hochlauf hinten gewichtet |
| Preis je Rubin-Package inkl. Rackanteil | ca. 100.000 $ | Annahme |
| Rubin-Packages bis Stichtag | 80.000 bis 130.000 | gerechnet |
| Blackwell-Packages bis Ende 2025 | ca. 3,2 Mio. | Presse/Analysten. Jensens "6 Mio." (GTC 2025) zählen Dies, zwei je Package |
| Blackwell-Packages Jan bis Sep 2026 | 2,5 bis 3,5 Mio. | Annahme, gestützt auf DC-Umsatz 75 und 89 Mrd. in Q1 und Q2 GJ2027 |
| Blackwell kumuliert | 5,7 bis 6,7 Mio. | gerechnet |

Nach Stück: 80k / 6,7M = 1,2 % bis 130k / 5,7M = 2,3 %. Zum Quartalsende (rund 200.000) etwa 3 %.
Nach Umsatz: rund 10 Mrd. gegen rund 330 Mrd. Blackwell-DC-Umsatz seit Q4 GJ2025, etwa 3 %.

Nach FLOPS, dicht, FP4: B200 ca. 10 PF, B300 ca. 15 PF (Tier 1b). Blackwell-Mittel bei 3,2 Mio. B200 und 3 Mio. B300: (3,2 × 10 + 3 × 15) / 6,2 = 12,4 PF. Basis 6,2 Mio. × 12,4 PF = 77 ZFLOPS. Rubin 35 PF (NVFP4 Training) oder 50 PF (NVFP4 Inferenz, mit adaptiver Kompression, Tier 1b).

    100k × 35 PF / 77 ZF = 4,5 %
    100k × 50 PF / 77 ZF = 6,5 %
    Spanne 3,4 % bis 9,2 %; zum Quartalsende 9 % bis 13 %

FP8 gegengerechnet (Rubin ca. 16 PF, nur Blog-Schätzung; Blackwell-Mittel 4,75 PF): 5,4 %. Der FLOPS-Anteil liegt beim etwa Dreifachen des Stückanteils.

Kippschwelle: Über 10 % FLOPS-Anteil zum 30.09. nur bei mehr als ca. 220.000 Rubin (35 PF) bzw. ca. 155.000 (50 PF).

## Trägt
Größenordnung: Rubin ist Ende September 2026 im installierten Bestand eine Randgröße, nach Stück unter 3 %, nach FLOPS unter 10 %. Die größte Unsicherheit ist die Stückzahl, nicht die Leistung je Chip.

## Trägt nicht
Einen Befund. Die Stückzahlen beider Generationen kommen aus Presse und Broker-Notes oder aus Annahmen, nach Wiki-Regel kein Befund. Spitzen-FLOPS sind keine nutzbare Leistung, Rubin hat zusätzlich rund dreimal die Speicherbandbreite von B200 (22 TB/s HBM4). Widerspruch zu [hbm-gb-per-mw-three-generations](../findings/hbm-gb-per-mw-three-generations.md): Dort ist Rubin mit 50 PF als "dicht" gerechnet (27,8 PF je kW × 1,8 kW). Hier gilt 35 PF als der mit B300 vergleichbare dichte Wert. Welcher stimmt, ist offen.

## Bruchindikator
Nvidia nennt Stückzahlen oder Rack-Zahlen für Rubin. Oder das 10-Q zum Q3 GJ2027 weist einen Rubin-Umsatz aus, der die Spanne verlässt.

## Ablesung
Rubin-Anteil am DC-Umsatz: Tier 1a zweiter Hand ([rubin-shipments-start-q3-fy27](../findings/rubin-shipments-start-q3-fy27.md)). FLOPS je Chip: Tier 1b. Stückzahlen und Preise: blind bzw. Presse. Nächster Schritt: 10-Q Q3 GJ2027 lesen, Rubin-Preis je Rack aus OEM-Angaben beschaffen, Blackwell-Packages je Quartal aus TSMC-CoWoS-Kapazität gegenrechnen.

## Verknüpft
- [rubin-shipments-start-q3-fy27](../findings/rubin-shipments-start-q3-fy27.md)
- [hbm-gb-per-mw-three-generations](../findings/hbm-gb-per-mw-three-generations.md)
- [accelerator-mass-balance](../../ai_application_layer/open_checks/accelerator-mass-balance.md)
- [announced-is-not-built](../../compute_bottlenecks/rules/announced-is-not-built.md)
