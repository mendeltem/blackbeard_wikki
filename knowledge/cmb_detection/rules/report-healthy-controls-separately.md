---
id: report-healthy-controls-separately
typ: regel
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-12
herkunft: Nutzer 12.10.2026 am T2*-Betrachter (Stick CMB_qc): "man muss die Gesunden getrennt rechnen"
verweist_auf: [qc-pages-explain-every-number-on-hover, qc-build-order-for-a-new-lesion-type]
---

# Faelle ohne Referenzlaesion (Gesunde) werden getrennt berichtet: Fehlalarme je Fall und Fall-Spezifitaet, kein F1

## Aussage
Ein Fall ohne Referenzlaesion hat kein F1: mit einem Fehlalarm ist es 0, ohne Fehlalarm undefiniert. Wer Gesunde
in ein "F1 je Fall, Mittel" mischt, zieht die Zahl nach unten und sagt nichts ueber die Erkennung. Deshalb:
1. **Zwei Gruppen** in jeder Zusammenfassung und Fallliste: Faelle mit Referenzlaesionen (F1 je Fall, Mittel;
   gepooltes F1; FP je Fall) und Gesunde (FP je Fall; Anteil mit >= 1 Fehlalarm; Fall-Spezifitaet = Anteil ohne Fehlalarm).
2. Das **gepoolte F1 ueber alle Faelle** darf zusaetzlich stehen (die Fehlalarme der Gesunden sind echte Fehlalarme),
   aber mit Angabe, dass es beide Gruppen enthaelt.
3. In der Fallliste bekommen Gesunde eine eigene Ueberschrift und zeigen nur "FP n" oder "clean"; die Kopfzeile sagt
   "healthy control", nicht "F1 0.00".
4. Fuer Berichte und Paper: F1-Mittel je Fall nur ueber Laesionsfaelle; Gesunde als Spezifitaetszahl daneben.

Umgesetzt im Generator `cmb/review/build_slice_viewer.py` (summary(), buildList(), Kopfzeile), 12.10.2026; alle vier
Stick-Seiten per `--refresh-html` neu gebaut. Beispielhafte Wirkung (eigene Kohorten, nur Richtung): das Fallmittel
stieg von 0,37 bzw. 0,47 (mit Gesunden) auf 0,63 bzw. 0,64 (nur Laesionsfaelle); das gepoolte F1 aenderte sich kaum.

## Traegt
Jede Laesionsdetektion mit Kontrollfaellen (CMB, PVS, WMH-Null-Faelle); jede QC-Seite und jede Tabelle mit "F1 je Fall".

## Traegt nicht
Datensaetze ohne Kontrollfaelle (VALDO Task 2 hat in jedem Fall Blutungen); voxelweise Dice-Masse.

## Bruchindikator
Eine Seite oder Tabelle, in der ein Fall mit "Ref 0" ein F1 traegt oder in ein Fallmittel eingeht.

## Ablesung
Nutzer am Stick-Betrachter 12.10.2026 09:48 (Screenshot), Generator-Aenderung und Neubau 12.10. 10:40-10:50.

## Verknuepft
- [qc-pages-explain-every-number-on-hover](../../mri_qc_viewers/rules/qc-pages-explain-every-number-on-hover.md)
- [qc-build-order-for-a-new-lesion-type](../../mri_qc_viewers/rules/qc-build-order-for-a-new-lesion-type.md)
