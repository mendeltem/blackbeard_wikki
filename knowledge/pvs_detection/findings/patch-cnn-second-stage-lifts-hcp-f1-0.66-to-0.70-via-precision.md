---
id: patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: PVS-Arena Alita, Versuch G2 (skripte/zweite_stufe_cnn.py --falten 5 --kanaele t2,maske,pa --cache), HCP-Aging 200 Faelle, referenz_wm, 2026-10-11 11:50
verweist_auf: [patch-cnn-second-stage-adds-nothing-on-valdo, candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57, hcp-aging-labels-are-mostly-unet-silver]
---

# Auf HCP-Aging hebt ein Patch-CNN als zweite Stufe den Trenner von 0,660 auf 0,695 -- fast ganz ueber die Praezision

## Aussage
Gleiches Protokoll wie auf VALDO (5-fach nach Fall, je Startwert 2 Schwellenfaelle zurueckgehalten, 3 Startwerte, 25 Epochen), aber
200 Faelle einer Geometrie (0,8 mm), nur T2, DRIPS-Kandidaten (Posterior >= 0,1), 143.461 Kandidaten: CNN allein 0,693 [0,680; 0,705],
GBM 0,660 [0,648; 0,672], Mischung 0,695 [0,682; 0,707]. Gepaart Mischung - GBM +0,035 [+0,032; +0,038], besser in 191/200.
Der Gewinn ist Praezision (gepoolt 0,821 -> 0,899, Fehlalarme 14.366 -> 7.480) bei gleichem Recall (0,563 -> 0,572); Klasse 1-2
bleibt bei Recall 0,24 -- die kleinen PVS fehlen schon im Kandidatensatz, nicht erst im Trenner. Gegen den alten Trenner F3 (0,668,
in-sample-Schwelle) +0,026, besser in 163/200.

## Traegt
Der Bruchindikator des VALDO-Befunds ist eingetreten: der CMB-Hebel (gemeinsames kleines 3D-CNN auf Kandidaten) traegt auch bei PVS,
sobald genug Positive einer Geometrie vorliegen (~80k statt ~1k). Fuer die HCP-Entwicklungslinie ist Mischung CNN+GBM der neue Stand.
Rezept: Patch 16 mm um den Schwerpunkt, Kanaele T2z/Komponentenmaske/Posterior, Flips + Verschiebung, BCE mit pos_weight, AdamW.

## Traegt nicht
Expertenevidenz: 160/200 HCP-Masken sind U-Net-Silber (nur WM). Ob der Gewinn auf Handreferenzen uebertraegt, zeigt erst
der Uebertrag HCP -> VALDO-T2 (Versuch G3). Recall-Gewinn fuer kleine PVS: keiner; dafuer muss der Kandidatengeber (DRIPS-Schwelle)
empfindlicher werden, dann kann das CNN mehr aussortieren (Versuch G4).

## Bruchindikator
Auf VALDO-T2-Kandidaten (12 Handfaelle) liegt das HCP-trainierte CNN+GBM nicht ueber dem VALDO-eigenen GBM auf denselben Kandidaten.

## Ablesung
pvs-arena/ergebnisse/hcp-aging/stufe2-cnn-drips-t2/{cnn,gbm,mix}/zusammenfassung.json + ergebnis.csv; gepaarte Rechnung und
Fehlalarme je Groessenklasse in ARBEIT.md 11.10. 11:55. Speicherlehre: Komponentenkarten nicht im RAM halten (19,8 GB bei 147 Faellen),
--cache je Fall (.npz, komprimiert, ~15 MB/Fall).

## Nachtrag 2026-10-11 18:05: Nebenbedingung bestanden -- kein Verschmelzungsartefakt
Nach dem VALDO-Befund (touch-based-instance-metrics-need-a-volume-side-condition) nachgerechnet: Vol_pred/Vol_ref 0,79 (GBM) / 0,77 (Mischung),
Mehrfachtreffer-Anteil 5,7 % / 5,5 %, max. 8 Referenzen je Vorhersage, Dice 0,588 -> 0,602. Der Gewinn des CNN ist echt.

## Verknuepft
- [patch-cnn-second-stage-adds-nothing-on-valdo](patch-cnn-second-stage-adds-nothing-on-valdo.md)
- [candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57](candidate-pool-plus-classifier-lifts-valdo-f1-from-0.44-to-0.57.md)
- [hcp-aging-labels-are-mostly-unet-silver](hcp-aging-labels-are-mostly-unet-silver.md)
