# agent_tooling

Werkzeuge bauen, auf deren Ausgabe sich ein Agent oder ein Mensch verlaesst.
Nicht modellspezifisch: es geht um Pruefwerkzeuge, Messwerkzeuge und
Vorbedingungspruefungen.

Der rote Faden aller Einträge: **ein Pruefwerkzeug, dessen eigener Fehler wie
ein Befund am Geprueften aussieht, ist die gefaehrlichste Sorte.** Es wird
geglaubt, weil es wie eine Messung aussieht.

Stand 2026-10-06. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| regel | [traceability-map-for-a-results-repo](rules/traceability-map-for-a-results-repo.md) | Ergebnis-Repo braucht eine Karte Zahl -> Daten -> Befehl -> Datei -> Abschnitt; vier Tabellen, Literatur-Flags, Luecken | vorschlag |
| [Kein Rueckfallwert ohne eine Zeile, die ihn benennt](rules/no-silent-fallback-values.md) | regel | getragen |
| [Leer ist nicht fehlend](rules/empty-is-not-missing.md) | regel | getragen |
| [Unbekannt ist kein Wert in einem Vergleich](rules/unknown-is-not-a-value-in-comparisons.md) | regel | getragen |
| [Erstmessung ist keine Veränderung](rules/first-measurement-is-not-a-change.md) | regel | getragen |
| [Gerechnetes und Gemeintes müssen auseinanderzuhalten sein](rules/computed-and-judged-must-stay-separable.md) | regel | getragen |
| [Agenten-Werkzeuge nach Aufgabenform schneiden](rules/agent-tools-by-task-shape.md) | regel | vorschlag |
| [Werkzeugwahl zeigt nur eine Spur am echten Host](rules/tool-choice-needs-host-trace.md) | regel | vorschlag |
| [Skill routet zuerst und schließt mit seiner Checkliste](rules/skill-routes-first-and-closes-its-checklist.md) | regel | vorschlag |
| [Tests belegen Aussagen, nicht Verkabelung](rules/tests-prove-claims-not-plumbing.md) | regel | vorschlag |
| [Eine Neustartschleife ist ein Alarm, keine Reparatur](rules/restart-loop-is-an-alarm-not-a-repair.md) | regel | vorschlag |

## Herkunft

Beide Einträge stammen aus dem Bau und der Pruefung von Werkzeugen im Projekt
[local_models](https://github.com/mendeltem/local_models) -- `tools/detect.py`
(Kapazitaetsrechnung) und `alita/werkzeuge/vorflug` (Vorbedingungspruefung eines
Agentenauftrags). Die Pfade und Messwerte stehen dort, hier steht nur, was
uebertragbar ist.

Die drei neueren Eintraege stammen aus der Lageseite
[AI_Lage](https://github.com/mendeltem/AI_Lage), die zehn Schwesterseiten liest
und daraus Thesen und Widersprueche rechnet.

Die vier Regeln vom 2026-10-06 sind aus dem Projekt [rea](https://github.com/morluto/rea)
(Reverse Engineering mit Agenten, MIT) übernommen: Werkzeugdesign, Skill-Aufbau,
Testprüfung. Bei uns nicht gemessen, daher vorschlag.
