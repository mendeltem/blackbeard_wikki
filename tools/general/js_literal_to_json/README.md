---
id: js_literal_to_json
bereich: tools/general
stand: 2026-10-02
herkunft: Projekt ki-anwendungsschicht (daten.py), verallgemeinert
sprache: python
---

# js_literal_to_json

## Zweck
Einzeldatei-Webseiten des Verbunds halten ihre Daten als JavaScript-Konstanten im Quelltext (`const MENGE = [ … ];`). Das Tool schneidet solche Literale aus einer HTML- oder JS-Datei heraus und wandelt sie in gültiges JSON: Kommentare entfernt, blanke Schlüssel quotiert, einfache Anführungszeichen umgesetzt, nachlaufende Kommata entfernt. Kein Node, keine Abhängigkeiten. Damit lässt sich eine `daten.json` aus der Seite erzeugen, statt sie doppelt zu pflegen.

## Wann verwenden, wann nicht
Verwenden, wenn Daten als Objekt- oder Array-Literal mit `const NAME =` am Zeilenanfang stehen und ohne Funktionsaufrufe, Template-Strings oder Ausdrücke auskommen. Nicht verwenden für Literale, die Berechnungen, Funktionen, Bezeichner als Werte (außer `true`, `false`, `null`) oder `\x`-Escapes enthalten; die Umwandlung schlägt dann mit einer JSON-Fehlermeldung fehl statt zu raten.

## Aufruf
    python src/js_literal_to_json.py index.html --const MENGE --const UMSATZ --out daten.json
    python src/js_literal_to_json.py index.html --list

`--list` nennt alle gefundenen `const`-Namen. Ohne `--out` geht das JSON auf die Standardausgabe. Ein Name wird zu einem Schlüssel des Ausgabeobjekts.

## Eingabe und Ausgabe
Eingabe: eine UTF-8-Datei mit `const NAME = <Literal>;`. Ausgabe: ein JSON-Objekt `{"NAME": <Wert>, …}`, Einrückung 1, nicht-ASCII unverändert.

## Teststand
<wird nach Ausführung des Tests eingetragen>

## Grenzen
Nur Literale, keine Ausdrücke. Schlüssel in Zeichenketten bleiben unangetastet (der Vorläufer `daten.py` hatte hier einen Fehler, siehe CHANGELOG). JavaScript-Escapes, die JSON nicht kennt (`\x41`, `\0`), werden nicht umgesetzt. Mehrfach definierte Konstanten: die erste gewinnt.
