---
id: sk-hynix-fab-footprint-f1
typ: befund
status: getragen
thema: knowledge/memory_supply
stand: 2026-10-06
herkunft: Projekt SK Hynix, Datei sk_hynix_fabs_stand_2026-08-06, eingetragen 2026-10-06
verweist_auf: [dram-wafer-capacity-by-fab, backend-and-base-die-are-separate-capacity, sk-hynix-china-fabs-annual-license]
---

# SK Hynix: zehn Wafer-Fabs, HBM ist keine Fab-Kategorie

## Aussage
Stand 31.03.2026 laut Filing: 10 Wafer-Fabs, davon 6 DRAM und 4 NAND.

| Standort | Fab | Produkt | Betrieb seit |
|---|---|---|---|
| Icheon | M10, M14, M16 | DRAM | 2005, 2015, 2021 |
| Cheongju | M11, M12, M15 | NAND | 2008, 2012, 2018 |
| Cheongju | M15X | DRAM, vorrangig HBM | Reinraum Okt. 2025, Wafereinsatz Q1 2026, im Hochlauf, EUV |
| Wuxi (China) | C2, C2F | DRAM | 2006, 2019 |
| Dalian (China) | Dalian | NAND | Kauf von Intel, Dez. 2021 |

Backend getrennt: eigene Assembly und Test in Icheon, Cheongju, Chongqing; dazu HITECH Semiconductor in Wuxi (Gemeinschaftsunternehmen, Anteil 45,0 %, fremdbetrieben). Betrieb in Volllast, 365 Tage, drei Schichten.

Das Filing kennt auf Fab-Ebene nur DRAM und NAND. HBM entsteht im Backend (TSV, Stapelung, MR-MUF) aus DRAM-Wafern. "Fab X produziert HBM" ist eine Kategorienverwechslung; einzige Ausnahme ist M15X, dessen Zweck das Filing selbst nennt.

## Trägt
Die Liste der Standorte und die Trennung Fab gegen Backend aus einer Tier-1a-Quelle.

## Trägt nicht
Waferkapazität je Fab, Node-Mix, Allokation je HBM-Generation, Backend-Kapazität in Stacks, die absolute Ausgangsbasis. Nichts davon steht im Filing. Zahlen dazu aus Branchendiensten bleiben Warnsignal, siehe dram-wafer-capacity-by-fab.

## Bruchindikator
Ein Folgebericht (20-F, DART) nennt Kapazität je Werk oder eine geänderte Zuordnung.

## Ablesung
SK hynix Form F-1, Amendment No. 2, SEC, 06.07.2026, Reg. No. 333-296987, Tier 1a. https://www.sec.gov/Archives/edgar/data/2120882/000119312526295501/d32785df1a.htm Zahlen aus der Projektdatei vom 06.08.2026 übernommen, die das Filing ausgewertet hat; für diesen Eintrag nicht erneut gegen das Filing gelesen.

## Verknüpft
- [dram-wafer-capacity-by-fab](../open_checks/dram-wafer-capacity-by-fab.md)
- [backend-and-base-die-are-separate-capacity](../rules/backend-and-base-die-are-separate-capacity.md)
- [sk-hynix-china-fabs-annual-license](sk-hynix-china-fabs-annual-license.md)
