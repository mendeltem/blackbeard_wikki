---
id: unknown-is-not-a-value-in-comparisons
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-02
herkunft: Projekt AI_Lage, Codeprüfung 2026-09-16
verweist_auf: [no-silent-fallback-values, empty-is-not-missing]
---

# Unbekannt ist kein Wert in einem Vergleich

## Aussage
Ein fehlender Wert verschwindet nicht, wenn man ihn vergleicht — er wird still
zu einer Zahl. In JavaScript:

    null <= 0   →  true
    null >= 0   →  true
    null == 0   →  false

Die ersten beiden Zeilen sind der Fallstrick: `null` wird für relationale
Vergleiche nach 0 umgewandelt, für den Gleichheitsvergleich nicht. Eine Prüfung
auf "steigt nicht" ist damit für eine **fehlende** Reihe wahr.

Der Fall, aus dem die Regel stammt: eine Widerspruchsprüfung über zwei
Datenquellen, Form

    deckungsquote < 100 && capexTrend > 0 && deckungsTrend <= 0

Die Deckungsquote hatte genau einen Messpunkt, der Trend war deshalb `null`,
`null <= 0` war wahr — die Prüfung meldete einen Widerspruch zwischen zwei
Seiten, obwohl sie die Richtung einer der beiden gar nicht kannte. Die Meldung
las sich wie ein Befund über die Sache und war ein Befund über die eigene
Lückenbehandlung.

Dieselbe Falle in Python, nur dass sie dort absichtlich aussieht:

    (trend(x) or 0) <= 0

`or 0` ist hier kein Rückfallwert für eine Anzeige, sondern eine Behauptung
über eine Richtung, die niemand gemessen hat.

Richtig ist: Fehlt ein Eingang, den die Prüfung braucht, ist die Prüfung **nicht
rechenbar** und sagt, welcher Eingang fehlt. Sie liefert kein Ergebnis.

## Trägt
Jede Prüfung, die eine Richtung, eine Differenz oder einen Schwellenvergleich
braucht und ihre Eingänge aus Datenquellen zieht, die jemand anderes pflegt.
Besonders dort, wo die Eingänge nach und nach dazukommen: solange eine Quelle
erst einen Messpunkt hat, ist jede Trendaussage über sie unbekannt, nicht falsch.

## Trägt nicht
Sprachen und Systeme, in denen Unbekanntes durch den Vergleich hindurch
unbekannt bleibt — SQL mit `NULL`, Pandas mit `NaN` in Vergleichen. Dort ist das
Ergebnis nicht wahr, sondern unbekannt beziehungsweise falsch, und der Fehler
äußert sich anders.

Auch kein Argument gegen Vorgabewerte in reinen Anzeigehilfen. Es geht um
Vergleiche, deren Ergebnis eine Aussage auslöst.

## Bruchindikator
Eine Prüfung, die in der Praxis nie "nicht rechenbar" ausgibt, obwohl ihre
Eingänge aus Quellen unterschiedlicher Reife stammen. Dann verrechnet sie
Lücken zu Ergebnissen.

Zweiter Indikator: ein `<=`, `>=` oder `or 0` auf einem Wert, der aus einer
Zeitreihe mit möglicherweise einem einzigen Punkt stammt.

## Ablesung
Eigene Codeprüfung, 2026-09-16, Projekt AI_Lage: zwei Prüfungen betroffen, eine
davon meldete einen Widerspruch allein aus der Lücke. Nach der Korrektur
meldeten beide "nicht prüfbar" mit Nennung der fehlenden Reihe. Keine fremde
Quelle.

## Verknüpft
- [no-silent-fallback-values](no-silent-fallback-values.md)
- [empty-is-not-missing](empty-is-not-missing.md)
