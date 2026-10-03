---
id: rubin-hbm4-wafer-demand-2028-2030
typ: pruefpunkt
status: offen
thema: knowledge/memory_supply
stand: 2026-10-03
herkunft: Projekt AI_news, Gespräch 2026-10-03
verweist_auf: [gpu-memory-absorbs-fab-additions, hbm-eats-wafer-area, dram-wafer-capacity-by-fab, rubin-share-of-blackwell-base]
---

# HBM4- und DRAM-Wafernachfrage durch Rubin und Nachfolger, 2028 bis 2030

## Aussage
Erste Durchrechnung, jede Zahl mit Herkunft. Grundannahme (Vorgabe Mendel): Bis Ende 2028 gibt es so viele Rubin-Packages wie beim Blackwell-Höchststand, rund 10,5 Mio. (9,5 bis 11,4 Mio., aus [rubin-share-of-blackwell-base](../../ai_demand_drivers/open_checks/rubin-share-of-blackwell-base.md)).

**Eingaben**

| Größe | Wert | Herkunft |
|---|---|---|
| HBM je Package | B300 288 GB HBM3E, Rubin 288 GB HBM4, Rubin Ultra 1.024 GB (gekürzt ~683) | Tier 1b, Kürzung TrendForce |
| LPDDR5X je GPU | 750 GB (54 TB je NVL72-Rack / 72) | Herstellerspezifikation, Kürzung berichtet |
| DRAM-Kapazität 2026 | ~2,05 Mio. Wafer/Monat (SKH 620k, Samsung ~675k, Micron ~450k, Rest ~300k) | Branchendienste plus Annahme, siehe [dram-wafer-capacity-by-fab](dram-wafer-capacity-by-fab.md) |
| HBM-Anteil Wafer 2026 | 22 % | Branchendienste, aus [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md) |
| Nvidia-Anteil an HBM-Bits | 65 % | Annahme |
| Blackwell-Lieferung 2026 | ~4 Mio., fast alles B300 | Annahme |
| Anteil Rubin-Lieferungen in 2028 | 55 % der kumulierten Menge | Annahme |

**GB HBM je Wafer, zwei Wege**
- Bottom-up: DDR5-Wafer 1b/1c ~2.500 GB, HBM4 Tauschverhältnis 4 → ~625 GB. Vermutlich zu optimistisch (Spitzenausbeute).
- Kalibriert: 4 Mio. × 288 GB / 0,65 = 1,77 EB HBM3E 2026 auf 22 % × 2,05 Mio. = 451k Wafer/Monat → effektiv 327 GB HBM3E je Wafer. HBM4 × 3/4 = 246 GB, mit +30 % Ausbeute bis 2028 → **320 GB** (Basis). Die beiden Wege liegen Faktor 2,5 auseinander.

**2028 (mittlerer Fall, kalibriert, 320 GB je Wafer)**

    5,8 Mio. Packages × 288 GB = 1,66 EB HBM4
    1,66 EB / 320 GB / 12 = 434k Wafer/Monat Nvidia
    / 0,65 = 668k Wafer/Monat alle HBM-Käufer = 30 % von 2,26 Mio. (Kapazität +5 %/Jahr)
    + LPDDR5X Vera: 159k Wafer/Monat = 7 %
    Wafer für konventionelles DRAM: 2026 1.599k → 2028 1.433k = −10 %

| Mix 2028 | HBM alle Käufer | Anteil DRAM-Wafer | konv. DRAM gegen 2026 |
|---|---|---|---|
| nur Rubin 288 GB | 668k | 30 % | −10 % |
| 30 % Ultra gekürzt 683 GB | 943k | 42 % | −28 % |
| 30 % Ultra 1 TB | 1.180k | 52 % | −42 % |
| nur Rubin, ohne Ausbeute-Gewinn | 868k | 38 % | −23 % |

Kippschwelle 2028: Konventionelles DRAM behält die Fläche von 2026 nur bei rund +9 % Kapazität je Jahr (≈2,43 Mio. Wafer/Monat).

**2029 und 2030** (Nvidia 6,3 und 6,8 Mio. Packages, GB je HBM-Wafer 400 und 460 mit HBM4E, Kapazität +10 %/Jahr)

| GB je Package | 2029 HBM-Anteil / konv. DRAM | 2030 HBM-Anteil / konv. DRAM |
|---|---|---|
| gedeckelt 288 | 23 % / +8 % | 20 % / +25 % |
| 683, dann 1.024 | 55 % / −41 % | 71 % / −63 % |
| 1.024, Feynman 1.536 (Annahme) | 83 % / −84 % | 107 % (unmöglich) |

Verträglich ohne Verdrängung: rund 355 GB je Package (2029), 500 GB (2030).

## Trägt
Die Größenordnung: Schon die Grundannahme (Rubin = Blackwell-Menge, 288 GB) bindet 2028 rund 30 % der DRAM-Wafer in HBM. Jeder Schritt zu mehr GB je Package übersteigt den geplanten Zubau.

## Trägt nicht
Einen Befund. Stückzahlen, GB je Wafer, Nvidia-Anteil und Kapazitätswachstum sind Annahmen. Ausmusterung, Hopper, AMD- und ASIC-Designs sind nur pauschal über den Nvidia-Anteil enthalten. Feynman-Speicher ist unbekannt.

## Bruchindikator
Ein Hersteller nennt HBM-Waferstarts oder Bits je Wafer, oder Nvidia nennt Stückzahlen. Dann sind die Annahmen zu ersetzen.

## Ablesung
Nächste Schritte: (1) GB je HBM4-Wafer aus Die-Größe und Stapelausbeute belegen, (2) Nvidia-Anteil an HBM aus Herstellerumsätzen, (3) Kapazitätszubau aus [dram-wafer-capacity-by-fab](dram-wafer-capacity-by-fab.md) statt pauschal +5/+10 %. Rechenskripte liegen nicht in der Wiki; die Formeln oben reichen zum Nachrechnen.

## Verknüpft
- [gpu-memory-absorbs-fab-additions](../mechanisms/gpu-memory-absorbs-fab-additions.md)
- [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md)
- [dram-wafer-capacity-by-fab](dram-wafer-capacity-by-fab.md)
- [rubin-share-of-blackwell-base](../../ai_demand_drivers/open_checks/rubin-share-of-blackwell-base.md)
