---
id: case-ids-are-dataset-local-prefix-when-pooling
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-11
herkunft: PVS-Arena Alita, Versuch G3b (Uebertrag HCP-Aging -> VALDO), 2026-10-11 12:18
verweist_auf: [kill-by-pid-fetched-in-a-separate-command, empty-is-not-missing]
---

# Fall-Kennungen sind datensatz-lokal -- beim Zusammenlegen zweier Saetze die Schluessel praefixieren und die Zaehlung pruefen

## Regel
`sub-101` gibt es in HCP-Aging (sub-001..sub-200) UND in VALDO Task 1 (sub-101..sub-106, sub-2xx). Wer Trainings- und Testsatz in
dasselbe Woerterbuch legt, ueberschreibt stumm: sechs Testfaelle ersetzten sechs Trainingsfaelle, der Testsatz schrumpfte auf 6, und
die ersetzten Faelle lagen im Training UND im Test (Leck). Kein Fehler, kein Warnhinweis -- nur die Zeile "Training 200 Test 6".
Deshalb: 1) Schluessel beim Zusammenlegen praefixieren (`T|sub-101`), Dateinamen und Berichts-IDs erst beim Schreiben wieder
abstreifen. 2) Nach dem Laden die erwarteten Zahlen ausgeben und PRUEFEN (Training n, Test m, Summe = Eingabe). 3) Kurztests mit
absichtlich kollidierenden Kennungen fahren, nicht nur mit disjunkten (der erste Kurztest mit sub-001..006 fand den Fehler nicht).

## Belege
- 11.10. 12:18: logs/versuch_g3b.log "Uebertrag: Training 200 Test 6", Patches 142.801 statt 143.461 (= 6 HCP-Faelle fehlten);
  Lauf nach 15 min abgebrochen, Praefix eingebaut, Kurztest mit HCP sub-101..106 als Training -> "Training 6 Test 12".

## Verknuepft
- [kill-by-pid-fetched-in-a-separate-command](kill-by-pid-fetched-in-a-separate-command.md)
- [empty-is-not-missing](empty-is-not-missing.md)
