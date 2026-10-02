---
id: rule-lists-make-small-models-refuse
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [counting-needs-thinking]
---

# Eine Liste von Abbruchgruenden im System-Prompt laesst kleine Modelle abmustern

## Aussage
Qwen3.6-35B-A3B mit abgeschaltetem Thinking ging bei zwei Aufgabentypen **von
0 auf 100 Prozent**, nachdem ein einzelner Absatz aus dem System-Prompt entfernt
wurde.

Der Absatz war eine Eskalationsregel mit Aufzaehlung: eskaliere bei Websuche,
aktuellen Fakten, mehreren Dateien, mehr als 30 Zeilen Code, offener Bewertung.
Das Modell lehnte daraufhin ab:

| Aufgabe | Antwort |
|---|---|
| Commit-Message aus einem Vier-Zeilen-Diff | `ESKALIEREN: mehr als 30 Zeilen Code` |
| Fuenfzeilige Python-Funktion | `ESKALIEREN: Keine Websuche oder aktuelle Fakten` |

Der Versuch, die Regel zu **praezisieren**, machte es schlimmer - die Begruendungen
wurden frei erfunden (`ESKALIEREN: mehrere Dateien geaendert` bei einem
Ein-Datei-Diff). Erst das Entfernen half. Danach beide Aufgaben korrekt.

## Traegt
Bedingungen gehoeren nur zu den Aufgabentypen, die sie brauchen, nicht in einen
gemeinsamen System-Prompt. Und: je kuerzer der System-Prompt, desto besser - auf
CPU-seitigem Prefill zahlt man ihn bei jedem Aufruf.

## Traegt nicht
Ein Urteil ueber grosse Modelle oder ueber dasselbe Modell **mit** Thinking. Beides
ungeprueft. Der Mechanismus ist vermutlich, dass ohne Reasoning-Schritt gemustert
statt begruendet wird - das ist eine Deutung, kein Befund.

## Bruchindikator
Eskalationsquote eines Aufgabentyps dauerhaft ueber etwa 30 Prozent. Dann liegt es
am Zuschnitt oder am Prompt, nicht am Modell.

## Ablesung
Eigene Messung, 10 Aufgaben mit maschineller Pruefung, je drei Laeufe.
Vorher/Nachher am selben Modell, selber Maschine, selbem Tag.

## Verknuepft
- [counting-needs-thinking](../findings/counting-needs-thinking.md)
