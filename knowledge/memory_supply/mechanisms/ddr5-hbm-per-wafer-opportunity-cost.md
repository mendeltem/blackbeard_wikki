---
id: ddr5-hbm-per-wafer-opportunity-cost
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-02
herkunft: Gespraech Projekt NVIDIA-Roadmap, 2026-09-16
verweist_auf: [hbm-eats-wafer-area, demand-is-not-earnings]
---

# Opportunitaetskosten je Wafer: DDR5 gegen HBM

## Aussage
Ob ein Wafer als HBM oder als DDR5 mehr einbringt, entscheidet nicht der Preis je GB, sondern der Erloes je Wafer. Weil HBM je Bit mehr Flaeche braucht, gibt es einen Gleichstandspreis:

    Erloes je Wafer = (Basis-GB je Wafer / Tauschverhaeltnis) x Preis je GB
    Gleichstand: Preis(DDR5) = Preis(HBM) / Tauschverhaeltnis

Bei Tauschverhaeltnis 3 bringt ein DDR5-Wafer also schon dann mehr als ein HBM-Wafer, wenn DDR5 je GB mehr als ein Drittel des HBM-Preises kostet. Darueber hat der Hersteller einen Anreiz, Flaeche zurueck zu DDR zu schieben, sofern er nicht vertraglich gebunden ist.

Rechenbeispiel mit Spotpreisen vom 16.09.2026 (Warnsignal, kein Befund): DDR5 16-Gb-Chip 54,30 USD, also rund 27 USD je GB; HBM3E-Stapel mit 36 GB 299,90 USD, also rund 8 USD je GB. Der Gleichstand laege bei rund 2,8 USD je GB fuer DDR5. Der tatsaechliche DDR5-Preis lag weit darueber, der DDR5-Wafer war also rechnerisch der wertvollere.

## Traegt
Erklaert, warum Hersteller trotz HBM-Vorrang weiter konventionelles DRAM fertigen, warum Langfristvertraege noetig sind, damit der HBM-Ausbau gegen die kurzfristige Marge ueberhaupt stattfindet, und warum die Marge eines HBM-Marktfuehrers zugleich am konventionellen Geschaeft haengt.

## Traegt nicht
Keine Aussage ueber Gewinn. Der Erloes je Wafer ignoriert Kosten, Ausbeute, Packaging und Testaufwand, die bei HBM hoeher liegen. Keine Aussage ueber strategischen Wert: Kundenbindung, gemeinsam entwickelte Basis-Chips und der Zugang zur naechsten Generation stehen nicht in dieser Rechnung.

Spotpreise sind kein Vertragspreisniveau. Vertragspreise fuer DDR5 liegen in der Regel darunter, HBM-Preise sind ueber Laufzeiten fixiert.

## Bruchindikator
- HBM-Vertragspreise werden neu verhandelt und naehern sich dem Gleichstand.
- Ein Hersteller begruendet eine Verschiebung von Waferflaeche ausdruecklich mit der Marge je Wafer.
- Das Tauschverhaeltnis faellt durch bessere Ausbeute oder Hybrid Bonding, dann sinkt der Gleichstandspreis.

## Ablesung
Spotpreise ueber Aggregatoren auf DRAMeXchange-Basis, Tier Trade Press, also Warnsignal. Tier 1a waeren ASP- und Mix-Angaben in Quartalsberichten und Calls.

## Verknuepft
- [hbm-eats-wafer-area](hbm-eats-wafer-area.md)
- [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)
