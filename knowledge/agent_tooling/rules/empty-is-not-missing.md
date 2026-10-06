---
id: empty-is-not-missing
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-02
herkunft: Projekt local_models, Bau von vorflug 2026-08-29
verweist_auf: [no-silent-fallback-values]
---

# Leer ist nicht fehlend

## Aussage
Wer eine Vorbedingung prueft, prueft meist auf Existenz: gibt es den Pfad, die
Tabelle, den Eintrag. Der haeufigere Fehlerfall ist aber, dass es ihn **gibt**
und er **leer** ist.

Der Fall, aus dem die Regel stammt: ein Agentenauftrag verlangte 62 und 150
Dateien in zwei Arbeitsverzeichnissen. Beide Verzeichnisse existierten, beide
waren leer, die Quelldaten lagen woanders -- dem Auftrag fehlte eine erste
Stufe, die sie dorthin verlinkt. Kosten, bis das auffiel: zwei Anlaeufe, rund
2 h 50 min Rechenzeit, null erzeugte Dateien.

Das daraufhin gebaute Pruefwerkzeug prueffte in seiner ersten Fassung
`path.exists()`. Damit haette es **genau diesen Fall durchgelassen** -- den
einzigen, fuer den es gebaut wurde. Aufgefallen ist es nur, weil die
Spielumgebung des Tests das Verzeichnis gar nicht angelegt hatte: richtiges
Verhalten des Werkzeugs auf eine falsche Testlage.

Richtig ist: vorhanden **und** nicht leer. Bei Mustern: trifft das Muster
ueberhaupt etwas.

## Traegt
Jede Vorbedingungspruefung vor einem teuren Lauf -- Eingangsdaten, Modellgewichte,
Konfigurationsverzeichnisse, Datenbanktabellen, Warteschlangen.

Und eine zweite Lehre, die weiter traegt als der Einzelfall: **ein Test, dessen
Lage den geprueften Fall nicht herstellt, ist gruen und wertlos.** Jeder
Prueffall baut seine Lage selbst, einschliesslich der leeren Variante.

## Traegt nicht
Eine Aussage darueber, ob der Inhalt brauchbar ist. "Nicht leer" heisst nicht
"richtig" -- eine Datei mit 127 Byte Unsinn ist nicht leer. Dafuer braucht es
eine inhaltliche Pruefung, und die ist ein anderer Eintrag.

## Bruchindikator
Ein Pruefwerkzeug, das in der Praxis nie ablehnt. Dann prueft es entweder das
Falsche oder zu schwach.

Zweiter Indikator: der Test besteht, aber niemand kann sagen, welche Lage er
herstellt.

## Ablesung
Eigene Messung. Erste Fassung mit `exists()`: Testfall gruen, echter Fall
durchgelassen. Zweite Fassung mit "vorhanden und nicht leer": derselbe Fall
abgelehnt, zusaetzlicher Pruefstand mit ausdruecklich leerem Verzeichnis.

Unabhängig bestätigt im Projekt rea (morluto/rea, docs/tool-design.md, 2026-10-05): "Missing evidence is unknown, not empty or false." Siehe [agent-tools-by-task-shape](agent-tools-by-task-shape.md).

## Verknuepft
- [no-silent-fallback-values](no-silent-fallback-values.md)
- [agent-tools-by-task-shape](agent-tools-by-task-shape.md)
