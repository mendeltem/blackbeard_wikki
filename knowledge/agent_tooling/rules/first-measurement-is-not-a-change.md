---
id: first-measurement-is-not-a-change
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-02
herkunft: Projekt AI_Lage, Urteilslauf 2026-09-16
verweist_auf: [unknown-is-not-a-value-in-comparisons, computed-and-judged-must-stay-separable]
---

# Erstmessung ist keine Veränderung

## Aussage
Ein Melder, der Zustandswechsel meldet, vergleicht den heutigen Stand mit dem
gespeicherten. Dabei zählt er zwangsläufig auch den Wechsel aus "unbekannt" in
einen bekannten Zustand als Wechsel. Das ist aber keine Veränderung in der
Sache, sondern nur das Eintreffen von Daten.

Der Fall: ein Lauf vergleicht 16 Thesen gegen ihre Trägerindikatoren und schreibt
bei jedem Statuswechsel ein Urteil. Zwischen zwei Läufen kamen fünf bis dahin
leere Datenquellen dazu. Ergebnis: acht Thesen sprangen von "unbestimmt" auf
"trägt", zwei Prüfungen von "nicht prüfbar" auf "kein Widerspruch". Der Lauf
hätte zehn Urteile geschrieben und zehn Einträge in eine Trefferbilanz gelegt,
die ausdrücklich **nie bereinigt** wird — also zehn dauerhafte Einträge, von
denen keiner eine Vorhersage ist.

Richtig ist: Ein Wechsel ist nur dann ein Anlass, wenn **beide** Zustände
bestimmt sind. Wechsel aus oder nach "unbekannt" werden gemeldet, aber in eine
eigene Kategorie — hier *Messwechsel* — und lösen nichts aus.

Der Kostenunterschied ist nicht der Lauf, sondern das Gedächtnis: ein
überflüssiges Urteil kostet einmal Rechenzeit, ein überflüssiger Eintrag in
einer Bilanz, die nie bereinigt wird, verfälscht jede spätere Auswertung.

## Trägt
Jeden Melder mit Gedächtnis: Alarme auf Schwellen, Statusverfolgung,
Regressionswächter, Trefferbilanzen, alles was "hat sich etwas geändert"
beantwortet und das Ergebnis aufbewahrt.

Besonders in Aufbauphasen, in denen Datenquellen nacheinander angeschlossen
werden — dort ist der Anteil der Erstmessungen an allen Wechseln anfangs nahe
100 Prozent.

## Trägt nicht
Verschweigen. Erstmessungen gehören in die Ausgabe, nur eben als eigene
Kategorie. Wer sie unterdrückt, merkt nicht, wann eine Quelle ausgefallen ist:
der Wechsel **nach** unbekannt ist dieselbe Sorte Ereignis und ebenso wenig ein
Anlass, aber ebenso meldenswert.

Auch keine Aussage über Melder ohne Gedächtnis, die nur den Istzustand zeigen.

## Bruchindikator
Eine Ereignisliste, deren Häufungen mit dem Anschluss neuer Datenquellen
zusammenfallen statt mit Ereignissen in der Sache. Wer das Anschlussdatum der
Quellen neben die Ereignisliste legt und ein Muster sieht, zählt Erstmessungen.

## Ablesung
Eigener Lauf, 2026-09-16, Projekt AI_Lage: 10 Messwechsel, 0 Anlässe, 0
geschriebene Urteile. Vor der Korrektur hätte derselbe Lauf 10 Urteile und 10
Bilanzeinträge erzeugt. Keine fremde Quelle.

## Verknüpft
- [unknown-is-not-a-value-in-comparisons](unknown-is-not-a-value-in-comparisons.md)
- [computed-and-judged-must-stay-separable](computed-and-judged-must-stay-separable.md)
