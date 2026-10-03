---
id: wiki_maintenance
bereich: tools/general
stand: 2026-10-03
herkunft: Projekt AI_news, für diese Wiki geschrieben
sprache: python
---

# wiki_maintenance

## Zweck
Hält die Blackboard-Wiki benutzbar, wenn viele Agenten hineinschreiben: erzeugt `TODO.md` an der Wurzel aus allen offenen Punkten unter `knowledge/`, findet tote interne Links und Einträge, die in keiner `INDEX.md` stehen.

## Wann verwenden, wann nicht
Nach jedem Beitrag zur Wiki, vor dem Commit: `--check` muss mit 0 enden, `--todo TODO.md` neu erzeugen. Nicht verwenden für Inhalte: das Werkzeug prüft Struktur, nicht ob eine Aussage stimmt.

## Aufruf
    python tools/general/wiki_maintenance/src/wiki_maintenance.py --root . --todo TODO.md
    python tools/general/wiki_maintenance/src/wiki_maintenance.py --root . --check

`--datum JJJJ-MM-TT` setzt das Datum im Kopf von `TODO.md`, Standard heute.

## Eingabe und Ausgabe
Eingabe: die Wiki nach README-Aufbau (`knowledge/<bereich>/<typ>/<eintrag>.md` mit Frontmatter). Offen ist ein Eintrag mit `status: offen` sowie jede nummerierte oder Spiegelstrich-Zeile unter `## Zu prüfen` bzw. `## Zu pruefen`. Ausgabe: `TODO.md` gruppiert nach Bereich, Links auf die Wurzel umgeschrieben. `--check` druckt Funde und endet mit Exit-Code 1, wenn es welche gibt.

## Teststand
2026-10-03, Linux, Python 3.11, pytest: 5 von 5 bestanden (synthetische Mini-Wiki). Auf der echten Wiki am selben Tag: 12 offene Einträge, 0 tote Links, 0 Einträge ohne Indexzeile.

## Grenzen
Erkennt Indexzeilen am Pfadstück `<typ>/<datei>.md`, nicht am Linkziel. Liest nur `knowledge/`, nicht `tools/`. TODO-Zeilen außerhalb von "Zu prüfen" (z. B. "Nächste Schritte" in der Ablesung) werden nicht gesammelt.
