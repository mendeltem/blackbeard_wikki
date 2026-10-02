# agent_tooling

Werkzeuge bauen, auf deren Ausgabe sich ein Agent oder ein Mensch verlaesst.
Nicht modellspezifisch: es geht um Pruefwerkzeuge, Messwerkzeuge und
Vorbedingungspruefungen.

Der rote Faden aller Einträge: **ein Pruefwerkzeug, dessen eigener Fehler wie
ein Befund am Geprueften aussieht, ist die gefaehrlichste Sorte.** Es wird
geglaubt, weil es wie eine Messung aussieht.

Stand 2026-10-02. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Kein Rueckfallwert ohne eine Zeile, die ihn benennt](rules/no-silent-fallback-values.md) | regel | getragen |
| [Leer ist nicht fehlend](rules/empty-is-not-missing.md) | regel | getragen |
| [Unbekannt ist kein Wert in einem Vergleich](rules/unknown-is-not-a-value-in-comparisons.md) | regel | getragen |
| [Erstmessung ist keine Veränderung](rules/first-measurement-is-not-a-change.md) | regel | getragen |
| [Gerechnetes und Gemeintes müssen auseinanderzuhalten sein](rules/computed-and-judged-must-stay-separable.md) | regel | getragen |

## Herkunft

Beide Einträge stammen aus dem Bau und der Pruefung von Werkzeugen im Projekt
[local_models](https://github.com/mendeltem/local_models) -- `tools/detect.py`
(Kapazitaetsrechnung) und `alita/werkzeuge/vorflug` (Vorbedingungspruefung eines
Agentenauftrags). Die Pfade und Messwerte stehen dort, hier steht nur, was
uebertragbar ist.

Die drei neueren Eintraege stammen aus der Lageseite
[AI_Lage](https://github.com/mendeltem/AI_Lage), die zehn Schwesterseiten liest
und daraus Thesen und Widersprueche rechnet.
