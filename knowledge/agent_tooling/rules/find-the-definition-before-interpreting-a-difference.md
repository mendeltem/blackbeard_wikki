---
id: find-the-definition-before-interpreting-a-difference
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [name-a-component-against-its-code, count-cases-behind-a-pooled-number]
---

# Vor dem Vergleich zweier Zahlen die Definition suchen, nicht die Differenz deuten

## Aussage
Aus den Falten-Metadaten eines Trainings (tp/fp/fn) ein gepooltes F1 von 0,33 gerechnet und
mit den 0,25 des Aggregationsberichts verglichen; erste Deutung: "reproduziert nicht, der
Bericht ist verdaechtig". Falsch: der Bericht zaehlt aus den Vorhersagedateien neu, mit der
offiziellen Zuordnungsregel (6er-Nachbarschaft, Schwerpunkt < 5 mm, eins-zu-eins); die
Metadaten sind die Selbstauskunft des Trainingsskripts nach ANDERER Regel. Zwei Masse, kein
Widerspruch. Davor derselbe Fehler in klein: aus der abgeflachten Anzeige der eigenen Ausgabe
auf die Dateistruktur geschlossen (`KeyError`).

Regel: vor jedem Vergleich zweier Zahlen klaeren, welches Skript, welche Regel, auf welchen
Dateien. Bietet ein Werkzeug eine Nachzaehlung an, diese lesen statt aus Rohzahlen selbst zu
aggregieren -- die eigene Aggregation reproduziert die fremde Regel fast nie. Eine Abweichung
zwischen Selbstauskunft und unabhaengiger Nachzaehlung ist der Normalfall, nicht der Skandal.
Und nie aus der eigenen Bildschirmausgabe auf ein Datenformat schliessen; die Schluessel der
Datei ansehen.

## Traegt
Pruefung fremder Ergebnisse, Reproduktionen, Vergleiche zwischen Berichten.

## Traegt nicht
---

## Bruchindikator
---

## Ablesung
Vorfall 2026-09-15. Tier 1a.

## Verknuepft
- [name-a-component-against-its-code](name-a-component-against-its-code.md)
- [count-cases-behind-a-pooled-number](count-cases-behind-a-pooled-number.md)
- [computed-and-judged-must-stay-separable](computed-and-judged-must-stay-separable.md)
