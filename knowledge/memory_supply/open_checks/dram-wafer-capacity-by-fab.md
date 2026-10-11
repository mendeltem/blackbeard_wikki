---
id: dram-wafer-capacity-by-fab
typ: pruefpunkt
status: offen
thema: knowledge/memory_supply
stand: 2026-10-02
herkunft: Projekt NVIDIA-Roadmap, Seite fabriken.html, 2026-09
verweist_auf: [hbm-eats-wafer-area, lead-times-datacenter-vs-fab, own-visualisation-is-not-a-source]
---

# DRAM-Waferkapazitaet je Werk

## Aussage
Offener Erhebungsschritt: belegte 300-mm-Waferstarts je Monat, je Hersteller und Werk, getrennt nach DRAM und NAND, mit Termin und Status. Ohne diese Zahlen bleibt die Angebotsseite geschaetzt.

Stand der Sammlung, jede Zeile mit Herkunft:
- SK Hynix gesamt: rund 620k Wafer je Monat DRAM, Ziel 1.000k bis 2030. Ziel firmenseitig genannt, Heute-Wert aus Branchendiensten.
- SK Hynix M15X, Cheongju: HBM4, Serie seit Februar 2026, 10k wachsend auf 55k bis 60k zum Jahresende 2026. Eckpunkte firmenseitig und ueber Branchendienste, der Monatsverlauf dazwischen ist gerechnet.
- SK Hynix M14 und M16, Icheon: Umruestung auf 1c, plus rund 140k, 2027. Branchendienste.
- SK Hynix Yongin Fab 1: plus 360k bis H1 2030, sechs Reinraeume. Firmenangabe und Branchendienste.
- Samsung gesamt: rund 650k bis 700k Wafer je Monat DRAM, kein veroeffentlichtes Gesamtziel. Branchendienste.
- Samsung P4 Pyeongtaek: neue Linie 100k, plus 120k geplant, 2026. P5 betriebsbereit 2028, Groesse nicht genannt. Branchendienste.
- Micron: keine Gesamtzahl veroeffentlicht. Belegt ist nur HBM, 40k bis 50k auf 100k bis Ende 2026. ID1 Boise erste Wafer Mitte 2027.

Noch gar nicht erfasst, weder Zahl noch Herkunft. Reine Arbeitsliste, keine Daten:
- Kioxia und SanDisk, NAND: Yokkaichi und Kitakami, gemeinsam betrieben. Der groesste NAND-Verbund der Welt fehlt in der Sammlung oben vollstaendig.
- CXMT, DRAM: Hefei, plus ein dritter Standort in Peking im Bau. Der Hochlauf steht als Risiko in [cxmt-ramp](../risks/cxmt-ramp.md), aber ohne Waferzahl.
- YMTC, NAND: Wuhan.
- Nanya und Winbond, Taiwan: DRAM und Spezialspeicher, kleine Mengen, aber sie zaehlen gegen die Flaechenrechnung.
- Rueckseite: HBM-Stapelung und Test sind ein eigener Engpass und werden nicht in Wafern gemessen. Trennen von der Waferzahl, sonst wird doppelt gezaehlt.

## Zu pruefen
1. Fuer jede Zeile eine Tier-1a-Quelle finden (Quartalsbericht, Call, Investorentag) oder die Zeile als unbelegt markieren.
2. Umruestung von Zubau trennen. Ein Knotenwechsel bringt Bits, aber keine zusaetzlichen Wafer. Fuer die Flaechenrechnung zaehlt nur neuer Reinraum.
3. Netto-Zuwachs an Waferflaeche je Jahr 2026 bis 2030 rechnen und gegen den HBM-Anteil aus [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md) stellen.
4. Rohstoffseite pruefen: Fuer blanke Siliziumwafer wird eine Angebotsluecke von 8 Prozent (2026) bis 24 Prozent (2028) berichtet. Quelle und Tier klaeren.

## Bruchindikator
Ein Hersteller nennt Waferstarts selbst. Dann ersetzt ein Befund diese Sammlung.

## Ablesung
Derzeit ueberwiegend Branchendienste (TrendForce, The Elec, DigiTimes) und Presseberichte, also Warnsignal, kein Befund. Zusammengetragen auf der Seite fabriken.html des Projekts NVIDIA-Roadmap.

Warnung: Der Globus in Supply_Atlas3D zeigt seit 2026-10-02 eine Speicher-Ebene mit 41 Standorten und einer Waferzahl je Standort. Diese Zahlen sind Modellschaetzungen eines Agenten, nicht erhoben. Sie duerfen diese Sammlung weder fuellen noch bestaetigen. Siehe [own-visualisation-is-not-a-source](../rules/own-visualisation-is-not-a-source.md). Brauchbar ist dort nur die Liste der Standorte als Arbeitsliste.

## Verknuepft
- [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md)
- [lead-times-datacenter-vs-fab](../../ai_demand_drivers/mechanisms/lead-times-datacenter-vs-fab.md)
- [own-visualisation-is-not-a-source](../rules/own-visualisation-is-not-a-source.md)
