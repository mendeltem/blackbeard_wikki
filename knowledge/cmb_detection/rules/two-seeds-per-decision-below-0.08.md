---
id: two-seeds-per-decision-below-0.08
typ: regel
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-07
herkunft: Projekt valdo-t2s (Alita), Startwertreihe 2026-09-21 und Nachpruefung der Seitenlegende 2026-10-07
verweist_auf: [sensitivity-levers-do-not-raise-lesion-f1, first-measurement-is-not-a-change]
---

# Effekte unter dem Startwert-Rauschen gelten nur mit zweitem Startwert

## Aussage
Ein einzelnes U-Net-Training auf VALDO streut zwischen Startwerten um etwa 0,08 F1
(drei Startwerte desselben Rezepts: 0,646 / 0,590 / 0,578; sechs beinahe gleiche Laeufe
im Mittel 0,61). Ein Unterschied unter dieser Groesse ist deshalb erst dann ein Ergebnis,
wenn (a) das gepaarte 95-%-Bootstrap-Intervall ueber Faelle die Null ausschliesst oder
(b) ein zweiter Startwert dieselbe Richtung zeigt. Alles andere ist eine Richtungsangabe.

Konsequenz fuer Berichte: Bausteine nicht als "bestaetigt" bezeichnen, wenn ihr
Ablationsintervall die Null einschliesst. Bei der Nachpruefung der oeffentlichen
Pipeline-Seite am 2026-10-07 betraf das vier Bausteine, die als "kept, confirmed by an
ablation" standen: FRST-Kanal -0,053 [-0,116; +0,004], Gitter z = 2 mm -0,036
[-0,105; +0,032], enge Hirnmaske -0,048 [-0,099; +0,009], Bias-Korrektur -0,022
[-0,097; +0,052]. Sie bleiben in der Kette, weil ihr Entfernen nicht besser war --
aber sie sind nicht belegt, und die Seite sagt das jetzt.

Praktische Form: Entscheidungsregel und Erwartung VOR dem Lauf aufschreiben; jede
Entscheidung ueber einen Baustein mit zwei Startwerten; die zweite Stufe (kleiner
Klassifikator) streut nur 0,003 bis 0,009 und braucht das nicht.

## Traegt
Jeden Vergleich zweier Trainingsvarianten auf wenigen Dutzend Faellen, bei dem das
Zielmass instanzbasiert ist (F1 je Laesion, Zaehlung) -- dort wiegt eine Blutung in
einer kleinen Falte 0,02 F1.

## Traegt nicht
Grosse Testmengen, bei denen das Rauschen eines Trainings gegen das Intervall klein wird;
dort reicht das Intervall.

## Bruchindikator
Eine Startwertreihe desselben Rezepts, die auf VALDO unter 0,03 streut -- dann ist die
Zahl 0,08 zu pessimistisch und die Regel kann gelockert werden.

## Ablesung
Eigene Messung, VALDO 2021 Task 2, drei Startwerte und sechs Nachbarlaeufe. Tier 1a.
Hintergrund zur Metrikwahl: Maier-Hein et al., Metrics reloaded, Nat Methods 2024,
doi:10.1038/s41592-023-02151-z.

## Verknuepft
- [sensitivity-levers-do-not-raise-lesion-f1](../findings/sensitivity-levers-do-not-raise-lesion-f1.md)
- [first-measurement-is-not-a-change](../../agent_tooling/rules/first-measurement-is-not-a-change.md)
