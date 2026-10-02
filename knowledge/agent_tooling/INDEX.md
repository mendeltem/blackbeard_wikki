# agent_tooling

Werkzeuge bauen, auf deren Ausgabe sich ein Agent oder ein Mensch verlaesst.
Nicht modellspezifisch: es geht um Pruefwerkzeuge, Messwerkzeuge und
Vorbedingungspruefungen.

Der rote Faden beider Einträge: **ein Pruefwerkzeug, dessen eigener Fehler wie
ein Befund am Geprueften aussieht, ist die gefaehrlichste Sorte.** Es wird
geglaubt, weil es wie eine Messung aussieht.

Stand 2026-10-02. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Kein Rueckfallwert ohne eine Zeile, die ihn benennt](rules/no-silent-fallback-values.md) | regel | getragen |
| [Leer ist nicht fehlend](rules/empty-is-not-missing.md) | regel | getragen |

## Herkunft

Beide Einträge stammen aus dem Bau und der Pruefung von Werkzeugen im Projekt
[local_models](https://github.com/mendeltem/local_models) -- `tools/detect.py`
(Kapazitaetsrechnung) und `alita/werkzeuge/vorflug` (Vorbedingungspruefung eines
Agentenauftrags). Die Pfade und Messwerte stehen dort, hier steht nur, was
uebertragbar ist.
