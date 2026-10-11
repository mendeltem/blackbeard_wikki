---
id: hcp-pretraining-plus-valdo-finetuning-small-but-real-gain
typ: befund
status: getragen
thema: knowledge/pvs_detection
stand: 2026-10-11
herkunft: PVS-Arena Alita, Versuch G5 (--vortrainieren auf 200 HCP, --init + lr 3e-4 je VALDO-LOO-Falte), nur T2, DRIPS-Kandidaten >= 0,1, 2026-10-11 14:25
verweist_auf: [cnn-gain-holds-on-valdo-hand-reference-in-zero-shot-transfer, patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision]
---

# Vortraining auf HCP + Feintuning auf VALDO hebt das Patch-CNN um +0,02 -- klein, aber mit Intervall ohne Null

## Aussage
Gleiche Kandidaten, gleiches Protokoll wie die VALDO-interne Kontrolle (G3a): CNN 0,439 statt 0,417 (gepaart +0,022 [+0,008; +0,038], 9/12),
Mischung 0,440 statt 0,425 (+0,015 [+0,002; +0,027], 10/12). Gewinn auf SABRE (Mischung 0,499 -> 0,527), auf RSS nur beim CNN allein.
Nebenbefund Reproduzierbarkeit: die Wahl der Schwellenfaelle hing an Pythons prozess-zufaelligem String-Hash; der unveraenderte GBM schwankte
dadurch um +0,013 zwischen Laeufen. Jetzt crc32; Vergleiche ZWISCHEN aelteren Laeufen tragen +-0,013 Schwellenrauschen, gepaarte Vergleiche
innerhalb eines Laufs nicht.

## Traegt
Der Weg fuer Kohorten ohne grosse eigene Etiketten: CNN auf HCP vortrainieren, auf der Zielkohorte feintunen. Fuer BELOVE (kein T2) heisst
das: Ratings als Etiketten der Zielkohorte sind der Engpass, nicht das Netz.

## Traegt nicht
Groesse des Gewinns im Dreier-Pool (G5b laeuft); Erweiterung auf T1-/FLAIR-Kanaele ist nur kanalweise Teiluebernahme.

## Bruchindikator
G5b (Pool, 7 Kanaele) liegt gepaart unter G4.

## Ablesung
pvs-arena/ergebnisse/valdo-task1/stufe2-cnn-drips-t2only-loo-feintuning, modelle/cnn_hcp_t2; ARBEIT.md 11.10. 14:25.

## Verknuepft
- [cnn-gain-holds-on-valdo-hand-reference-in-zero-shot-transfer](cnn-gain-holds-on-valdo-hand-reference-in-zero-shot-transfer.md)
- [patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision](patch-cnn-second-stage-lifts-hcp-f1-0.66-to-0.70-via-precision.md)
