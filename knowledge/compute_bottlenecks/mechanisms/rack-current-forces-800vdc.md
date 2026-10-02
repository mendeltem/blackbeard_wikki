---
id: rack-current-forces-800vdc
typ: mechanismus
status: vorschlag
thema: knowledge/compute_bottlenecks
stand: 2026-10-02
herkunft: Projekt Artificial Intelligence (KI-Compute-Stack), Report 800-VDC Rack Power for NVIDIA Rubin and Kyber (Juli 2026), eingetragen 2026-10-02
verweist_auf: [bottleneck-migration]
---

# Rackstrom erzwingt 800 V Gleichspannung

## Aussage
Bei gleicher Leistung fällt der Strom mit der Spannung:

    1 MW / 54 V = 18.519 A
    1 MW / 800 V = 1.250 A   (Faktor 14,8)

Bei 54 V ist ein Rack im MW-Bereich wegen des Kupferquerschnitts nicht mehr sinnvoll zu bauen. Zeitlich laut Report: Rubin NVL144 (zweites Halbjahr 2026, 190 bis 230 kW) läuft noch auf 54 V, 800 V kommt mit Rubin Ultra Kyber (rund 600 kW, zweites Halbjahr 2027).

## Trägt
Die Richtung (höhere Verteilspannung) folgt aus der Rechnung. Umsätze aus 800 V fallen nach dem Report 2027 und 2028 an, nicht 2026.

## Trägt nicht
Welcher Standard gewinnt (NVIDIA 800 V einpolig gegen OCP ±400 V) und welcher Hersteller. Die Partnerliste von NVIDIA mit 14 Halbleiterfirmen ist kein Liefervertrag.

## Bruchindikator
Kyber verschiebt sich, oder Racks über 500 kW gehen mit 54 V in Serie.

## Ablesung
Rechnung aus Nennwerten. Termine: NVIDIA-Ankündigungen, Tier 1b. Zahlen aus dem Projekt-Report übernommen, gegen die Primärquelle nicht nachgeprüft.

## Verknüpft
- [bottleneck-migration](bottleneck-migration.md)
