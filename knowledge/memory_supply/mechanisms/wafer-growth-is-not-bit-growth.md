---
id: wafer-growth-is-not-bit-growth
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-06
herkunft: Projekt SK Hynix, Datei sk_hynix_fabs_stand_2026-08-06, nachgerechnet 2026-10-06
verweist_auf: [hbm-eats-wafer-area, sk-hynix-expansion-approved-vs-announced, price-per-bit-decline-threshold, gpu-memory-absorbs-fab-additions]
---

# Waferwachstum ist nicht Bitwachstum: das Verdopplungsziel in Bits

## Aussage
SK Hynix nennt im Filing das Ziel, die Waferkapazität in fünf Jahren zu verdoppeln (Filing Juli 2026, Horizont 2031, unter Marktvorbehalt).

    CAGR Wafer = 2^(1/5) - 1 = 14,87 % p.a.

Geht ein Anteil f der Zusatzkapazität auf HBM und braucht HBM je Bit das r-Fache an Waferfläche:

    Bitwachstum = Waferwachstum x [ (1 - f) + f / r ]

| f | r = 2 | r = 3 | r = 4 |
|---|---|---|---|
| 0,3 | 12,6 % | 11,9 % | 11,5 % |
| 0,5 | 11,2 % | 9,9 % | 9,3 % |
| 0,7 | 9,7 % | 7,9 % | 7,1 % |

Der Pfad ist hinten gewichtet: vor 2028 tritt kaum Zusatzkapazität in Produktion.

## Trägt
Die Größenordnung: aus knapp 15 % Waferwachstum werden 7 bis 13 % Bitwachstum, je nach HBM-Anteil. Das Filing bestätigt die Richtung selbst (HBM erfordere größeren Wafereinsatz).

## Trägt nicht
Die Höhe von r und f. Beide sind Annahmen; r ist aus Die-Fläche, Stapelhöhe und Kapazität je Die herzuleiten, nicht abzulesen. Node-Migration käme additiv hinzu, dafür fehlt eine Tier-1a-Größe. Ohne die absolute Ausgangsbasis liefert das Ziel eine Rate, keine Menge. Korrektur: die Projektdatei sk_hynix_ist_und_plan nennt für f = 0,7 und r = 2 den Wert 9,8 %; gerechnet sind es 14,87 x 0,65 = 9,7 %.

## Bruchindikator
SK Hynix weist Wafer- und Bit-Wachstum getrennt aus und das Verhältnis liegt außerhalb der Tabelle, oder das Verdopplungsziel fällt (siehe sk-hynix-expansion-approved-vs-announced).

## Ablesung
Ziel: SK hynix Form F-1, Amendment No. 2, SEC, 06.07.2026, Reg. No. 333-296987, Tier 1a. https://www.sec.gov/Archives/edgar/data/2120882/000119312526295501/d32785df1a.htm Formel und Tabelle: eigene Rechnung, Annahmen f und r.

## Verknüpft
- [hbm-eats-wafer-area](hbm-eats-wafer-area.md)
- [sk-hynix-expansion-approved-vs-announced](../findings/sk-hynix-expansion-approved-vs-announced.md)
- [price-per-bit-decline-threshold](../../memory_earnings/mechanisms/price-per-bit-decline-threshold.md)
- [gpu-memory-absorbs-fab-additions](gpu-memory-absorbs-fab-additions.md)
