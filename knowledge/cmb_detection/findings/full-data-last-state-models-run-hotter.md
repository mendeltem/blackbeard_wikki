---
id: full-data-last-state-models-run-hotter
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), scripts/final_models.sh und final_cross_scores.sh, Kreuztests 2026-10-07
verweist_auf: [one-shared-candidate-classifier-for-all-cohorts, training-loss-does-not-rank-networks-or-schedules]
---

# Ein auf allen Faellen trainiertes Netz ohne inneren Checkpoint gibt hoehere Wahrscheinlichkeiten aus -- der feste Arbeitspunkt der Faltenmodelle passt dann nicht mehr

## Aussage
Fuer ein Produkt wurden die U-Nets auf ALLEN Faellen je Kohorte trainiert (keine Falten,
60 Epochen Cosinus, letzter Stand, zwei Startwerte gemittelt). In der eigenen Domaene sind sie
so gut wie die Faltenmodelle (in-sample T2* 0,654 gegen out-of-fold 0,663: keine
Ueberanpassung). Auf einem fremden Scanner aber bricht der feste Arbeitspunkt ein:
VALDO-Vollmodell auf einer klinischen T2*-Kohorte bei Schwelle 0,3 **F1 0,415**
(P 0,28, S 0,77, 21 Fehlalarme je Fall) gegen 0,622 fuer das Fuenffalten-Ensemble in
derselben Bewertung. Das F1-Gitter des Vollmodells hat sein Maximum bei Schwelle 0,6-0,7
(0,637 mit Liquor-Regel), kreuzgewaehlt 0,629 = Faltenensemble. Es ist eine
**Kalibrierungsverschiebung**, kein Qualitaetsverlust: die Netze sind "heisser".
Wahrscheinliche Ursache: der innere Checkpoint der Faltenmodelle waehlt den Stand mit dem
besten Laesions-F1 (eher frueh, praeziser); der letzte Stand nach vollem Abfall der Lernrate
hat die Trainingslaesionen haerter gelernt (in-sample S 0,83, FP 3,4 je Fall gegen 1,5 OOF).

Die zweite Stufe (Kandidaten ab 0,15, gemeinsamer 3D-CNN-Klassifikator) faengt es weitgehend
ab: 3889 Kandidaten, F1 0,604 bei Klassifikator-Schwelle 0,30 (0,681 bei 0,5, aber auf
denselben Daten gewaehlt).

## Traegt
Jede Auslieferung eines Netzes, dessen Arbeitspunkt auf anderen Trainingslaeufen bestimmt
wurde: Schwelle NICHT uebernehmen, sondern auf dem neuen Lauf nachmessen -- oder die
Faltenmodelle selbst ausliefern (jedes Bild steckt in vier von fuenf Mitgliedern) oder das
Vollmodell mit einer kleinen inneren Menge fuer den Checkpoint trainieren.

## Traegt nicht
Innerhalb der Trainingsdomaene bei kreuzgewaehlter Schwelle: dort gleichauf.

## Bruchindikator
Ein Vollmodell, dessen F1-Gitter sein Maximum bei derselben Schwelle hat wie die
Faltenmodelle, oder eine Messung, in der der letzte Stand in der Fremddomaene gleich gut ist.

## Ablesung
Eigene Messung, Laesions-F1 gepoolt, 75 T2*-Faelle / 828 CMB einer klinischen Kohorte
(nur Summen); VALDO 72 Faelle in-sample. Tier 1a.

## Verknuepft
- [one-shared-candidate-classifier-for-all-cohorts](one-shared-candidate-classifier-for-all-cohorts.md)
- [training-loss-does-not-rank-networks-or-schedules](training-loss-does-not-rank-networks-or-schedules.md)
