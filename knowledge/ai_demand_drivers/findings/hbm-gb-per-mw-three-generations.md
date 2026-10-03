---
id: hbm-gb-per-mw-three-generations
typ: befund
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-02
herkunft: Projekt AI-Lage-Verbund (Seite roadmap), 2026-10-02
verweist_auf: [hbm-gb-per-mw, refresh-instead-of-new-build, induced-innovation, bandwidth-bottleneck, hbm-eats-wafer-area]
---

# GB HBM je MW: seit sechs Jahren kein Zuwachs, mit Rubin ein Rückgang

## Aussage

Rechnung zum offenen Prüfpunkt [hbm-gb-per-mw](../open_checks/hbm-gb-per-mw.md).
HBM-Kapazität je Beschleuniger geteilt durch dessen TDP, SXM-/OAM-Variante,
dichte Werte. GDDR6-Generationen bleiben draußen, sie tragen kein HBM.

| Generation | Jahr | HBM GB | TDP W | GB je W | GB je MW | ggü. Vorgänger |
|---|---|---|---|---|---|---|
| Ampere A100 | 2020 | 80 | 400 | 0,2000 | 200.000 | — |
| Hopper H100 | 2022 | 80 | 700 | 0,1143 | 114.286 | −42,9 % |
| Hopper H200 | 2023 | 141 | 700 | 0,2014 | 201.429 | +76,2 % |
| Blackwell B200 | 2024 | 192 | 1.000 | 0,1920 | 192.000 | −4,7 % |
| Blackwell Ultra B300 | 2025 | 288 | 1.400 | 0,2057 | 205.714 | +7,1 % |
| Rubin R200 | 2026 | 288 | ~1.800 | 0,1600 | 160.000 | −22,2 % |

Die drei letzten **ausgelieferten** Generationen, nach denen der Prüfpunkt fragt:
B200 192.000 → B300 205.714 → R200 160.000 GB je MW. Netto B200 → R200
**−16,7 %**. Über sechs Jahre, A100 2020 gegen R200 2026: **−20,0 %**.

Die Gegenbewegung steckt in der Rechenleistung, nicht im Speicher. Im selben
Schritt B200 → R200 steigt die dichte Rechenleistung je Watt von 10,0 auf
27,8 PFLOPS je kW, **+178 %**, während GB je PFLOPS von 19,2 auf 5,8 fällt,
**−70 %**. Der Beschleuniger wurde rechendichter, nicht speicherdichter.

Angekündigt, nicht ausgeliefert: Rubin Ultra VR300 mit 1 TB HBM4e bei ~2.300 W
wären 0,4452 GB je W, 445.217 GB je MW, **+178 %** gegenüber Rubin. Das würde
die Richtung umkehren. Die Angabe stammt aus Roadmap-Folien der GTC und ist
bis zum Marktstart nicht verbindlich.

## Trägt

Die Antwort auf die erste Hälfte des Prüfpunkts: **Refresh allein trägt die
Bitnachfrage nicht.** Wer einen alten Beschleuniger im gleichen Leistungsbudget
gegen einen neuen tauscht, kauft dabei nicht mehr HBM-Bits, seit sechs Jahren
nicht. Zusätzliche Bitnachfrage muss deshalb aus zusätzlichen Megawatt kommen,
nicht aus dichterem Ersatz. Damit hängt die HBM-Bitnachfrage am Netzanschluss,
und [lead-times-datacenter-vs-fab](../mechanisms/lead-times-datacenter-vs-fab.md)
wird für HBM zum tragenden, nicht zum nebenläufigen Mechanismus.

Zusammen mit der Angebotsseite ergibt das eine Klemme von beiden Enden:
[hbm-eats-wafer-area](../../memory_supply/mechanisms/hbm-eats-wafer-area.md)
rechnet, dass jedes HBM-Bit drei- bis viermal die Waferfläche eines DDR-Bits
kostet. Wenn gleichzeitig jedes zusätzliche HBM-Bit ein zusätzliches Megawatt
braucht, ist die HBM-Menge nach oben durch den Netzanschluss und nach unten
durch die aufgegebene DDR-Bitmenge begrenzt. Beide Grenzen sind unabhängig
voneinander, und keine der beiden wird durch Refresh gelockert.

## Trägt nicht

Die zweite Hälfte des Prüfpunkts. Der Bruchindikator dort liest ein fallendes
GB je MW als "Einsparung läuft". Diese Rechnung belegt das **nicht**. Sie zeigt
eine Verschiebung des Entwurfspunkts — Rechenleistung wuchs schneller als
Speicher —, und das ist etwas anderes als Forschung, die HBM gezielt ersetzt.
Beide Lesarten sind mit diesen Zahlen vereinbar; die Rechnung unterscheidet
sie nicht.

Ebenfalls nicht getragen: eine Aussage über Bandbreite. Gerechnet ist
Kapazität. Die Bandbreite je Beschleuniger stieg von 8 auf 22 TB/s, je PFLOPS
fiel sie von 0,80 auf 0,44 TB/s — eigene Rechnung, hier nicht geprüft.

Keine Aussage zur Rackebene. GB200 NVL72 kommt auf 112.500 GB je MW, GB300
NVL72 auf 166.667, aber der Nenner ist ein anderer: Rackleistung enthält CPUs,
Switches und Kühlung. VR200 NVL72 ist nicht rechenbar, die Rackleistung ist
nicht veröffentlicht. Für NVL576 Kyber passen die Angaben nicht zusammen
(365 TB bei 576 × 1.024 GB = 589.824 GB), die Zahl ist deshalb nicht reines HBM
und bleibt ungerechnet.

Eine frühere Rack-Rechnung (Eintrag hbm-gb-per-mw-first-pass, Projekt KI-Compute-Stack, hier aufgegangen) setzte VR200 NVL72 nach Sekundärreports auf 190 bis 230 kW und kam auf 90 bis 109 TB HBM je MW gegen 97 bis 115 bei Blackwell NVL72 (120 bis 142 kW): auf Rack-Ebene flach statt fallend. Gleichstand bei rund dem 1,5-Fachen der Blackwell-Rackleistung (180 bis 213 kW). Die Rackleistung ist nicht von NVIDIA veröffentlicht, deshalb kein Ersatz für die Rechnung je Beschleuniger.

## Bruchindikator

Der Befund hängt an **einer** approximativen Zahl: Rubins TDP, von NVIDIA als
"~1.800 W" angegeben.

- Liegt Rubins reale TDP bei **1.400 W**, ist GB je W gleich dem von B300 — die Reihe steigt dann weiter.
- Liegt sie bei **1.500 W oder darunter**, ist GB je W mindestens gleich dem von B200 — der Rückgang verschwindet.
- Erst oberhalb von 1.500 W fällt die Reihe tatsächlich.

Der Befund bricht also, sobald eine belastbare Rubin-TDP unter 1.500 W
vorliegt. Zweiter Bruch: liefert Rubin Ultra tatsächlich 1 TB HBM4e bei
~2.300 W aus, kehrt sich die Richtung um und Refresh trägt wieder.

## Ablesung

Tier 1b. Vergleichstabelle der Seite roadmap
(https://mendeltem.github.io/nvidia-roadmap/#vergleich, Datenstand August 2026),
die NVIDIA-Datenblätter, Architektur-Whitepapers und GTC-Präsentationen
auswertet. Methodik der Seite: dichte Werte ohne Sparsity-Verdopplung,
SXM-/OAM-Variante.

Einschränkung, die den Status `vorschlag` begründet: Die Einzelspezifikationen
sind nicht von mir gegen NVIDIAs Originaldokumente nachgelesen, sondern aus
dieser Tabelle übernommen. Die Werte für Rubin und Rubin Ultra sind dort
ausdrücklich als Näherung gekennzeichnet (~1.800 W, ~2.300 W). Die Rechnung
selbst ist Arithmetik und reproduzierbar.

## Verknüpft

- [hbm-gb-per-mw](../open_checks/hbm-gb-per-mw.md) — der Prüfpunkt, den diese Rechnung beantwortet
- [refresh-instead-of-new-build](../mechanisms/refresh-instead-of-new-build.md)
- [induced-innovation](../mechanisms/induced-innovation.md)
- [bandwidth-bottleneck](../axioms/bandwidth-bottleneck.md)
- [lead-times-datacenter-vs-fab](../mechanisms/lead-times-datacenter-vs-fab.md)
- [hbm-eats-wafer-area](../../memory_supply/mechanisms/hbm-eats-wafer-area.md) — die Angebotsseite derselben Frage
