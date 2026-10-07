---
id: noise-floor-before-effects
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekt valdo-t2s (CMB), Startwertreihe 2026-09-21, Turnier-Verlaeufe 2026-10-02; uebertragen 2026-10-07
verweist_auf: [two-seeds-per-decision-below-0.08, training-loss-does-not-rank-networks-or-schedules, first-measurement-is-not-a-change]
---

# Erst den Rauschboden messen, dann Effekte deuten

## Aussage
Bevor der erste Vergleich zweier Varianten gilt, dasselbe Rezept mit drei Startwerten
rechnen. Auf CMB streute ein U-Net-Training 0,578 bis 0,646 F1 (etwa 0,08); vier
Bausteine, die als "bestaetigt" galten (FRST-Kanal, Gitter, enge Maske, Bias-Korrektur),
lagen bei Nachpruefung mit Intervall im Rauschen. Eine CPU-Vorpruefung, die Varianten
ordnete, wurde vom GPU-Lauf widerlegt (Rang 1 schlechter, Rang 7 neutral): Vorpruefungen
ordnen, sie entscheiden nicht.

Daraus drei Vorschriften:
- Ein Effekt unter dem Rauschboden gilt nur mit zweitem Startwert in derselben Richtung
  oder mit Intervall ohne Null. Eine erste Messung ist eine Richtungsangabe.
- Der Trainingsverlust ordnet nichts: gleicher Verlust bei F1 0,176 gegen 0,404; laengeres
  Training senkt den Verlust, nicht den Out-of-fold-Wert; Fruehstopp auf dem inneren Mass
  feuert auf Startwert-Rauschen. Feste Epochenzahl, Entscheidung nur out-of-fold.
- Entscheidungsregel und Erwartung VOR dem Lauf aufschreiben. Auf CMB lag die Erwartung
  viermal falsch (Mischen, Zentrumskarte, Feintuning, "Kleinhirn-Luecke"); ohne Vorab-
  Regel haette jede davon als Gewinn gelesen werden koennen.

Eine kleine zweite Stufe (Kandidaten-Klassifikator) streut nur 0,003 bis 0,009 und
braucht die Startwertreihe nicht.

## Traegt
Vergleiche auf wenigen Dutzend Faellen mit instanzbasiertem Mass, bei dem eine Laesion
in einer kleinen Falte 0,02 wiegt.

## Traegt nicht
Grosse Testmengen, auf denen das Rauschen eines Trainings gegen das Intervall klein wird.

## Bruchindikator
Eine Startwertreihe desselben Rezepts, die unter 0,03 streut; dann reicht das Intervall.

## Ablesung
Eigene Messungen VALDO 2021 Task 2. Tier 1a.

## Verknuepft
- [two-seeds-per-decision-below-0.08](../../cmb_detection/rules/two-seeds-per-decision-below-0.08.md)
- [training-loss-does-not-rank-networks-or-schedules](../../cmb_detection/findings/training-loss-does-not-rank-networks-or-schedules.md)
- [first-measurement-is-not-a-change](../../agent_tooling/rules/first-measurement-is-not-a-change.md)
