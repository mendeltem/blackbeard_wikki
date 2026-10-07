---
id: name-a-component-against-its-code
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [find-the-definition-before-interpreting-a-difference]
---

# Bevor ein Baustein in einem Bericht einen Namen bekommt, die definierende Stelle im Code lesen

## Aussage
Ein "3D-ResNet" in Berichten, Protokoll und Replikationsdokument war ein schlichtes 3D-CNN ohne
Residualverbindungen; der Name stammte aus einem Docstring, geschrieben aus der Absicht ("soll
ein kleines ResNet werden"). Die Nachpruefung fand zwei weitere: "60 feste Epochen" (fest war
der Plan; geladen wurde der beste Zwischenstand), "Hirnmasken aus HD-BET" (119 von 136 waren
mitgelieferte Dateien). Keine Zahl war falsch; alle drei Namen haetten im Paper gestanden.

Regel: vor dem Benennen die Klasse, das `forward` oder die Laderoutine lesen und den Namen daran
messen; bei Herkunftsangaben (Masken, Karten) zaehlen, was Symlink auf eine Quelle ist. Ein
Glossar der verwendeten Namen mit Codestelle fuehren.

## Traegt
Berichte, Protokolle, Veroeffentlichungen, Readmes, die Verfahren benennen.

## Traegt nicht
---

## Bruchindikator
---

## Ablesung
Vorfall 2026-09-21. Tier 1a.

## Verknuepft
- [find-the-definition-before-interpreting-a-difference](find-the-definition-before-interpreting-a-difference.md)
- [traceability-map-for-a-results-repo](traceability-map-for-a-results-repo.md)
