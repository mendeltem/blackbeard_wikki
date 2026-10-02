# blackbeard_wikki

Blackboard für Agenten: gemeinsame Setzungen, Mechanismen, Risiken und offene Prüfpunkte. Ein Agent liest hier, bevor er neu recherchiert, und schreibt zurück, was er festgelegt oder gerechnet hat.

Einstieg: [INDEX.md](INDEX.md). Jedes Thema ist ein Unterordner mit eigenem `INDEX.md` und den Typ-Ordnern darunter, zum Beispiel `ai_demand_drivers/axioms/`.

## Typen

| Typ | Ordner | Bedeutung |
|---|---|---|
| axiom | `axioms/` | Setzung des Auftraggebers. Kein Befund. Wird im Basisszenario getragen und nicht angegriffen. |
| mechanismus | `mechanisms/` | Wirkungskette, die aus Axiomen folgt oder sie verbindet. Darf geprüft und gerechnet werden. |
| risiko | `risks/` | Kraft, die gegen die Position wirkt. Nie als Stütze lesen. |
| regel | `rules/` | Vorschrift, wie Einträge zu verwenden sind. |
| pruefpunkt | `open_checks/` | Offener Rechen- oder Erhebungsschritt. |

## Status

- `getragen`: gilt.
- `vorschlag`: noch nicht vom Auftraggeber bestätigt, oder enthält eine als Annahme markierte Schwelle.
- `offen`: nicht gerechnet oder nicht erhoben.
- `gebrochen`: Bruchindikator hat ausgelöst. Eintrag bleibt stehen, mit Datum und Quelle.

## Protokoll für Agenten

1. Vor einer Recherche `INDEX.md` und den `INDEX.md` des Themas lesen und die passenden Einträge öffnen.
2. Ein Axiom nie als Befund ausgeben. Jedes Ergebnis, das an einem Axiom hängt, als gesetzt kennzeichnen.
3. Den Abschnitt "Trägt nicht" beachten. Ein Eintrag darf nicht über seinen Geltungsbereich hinaus verwendet werden.
4. Neue Einträge: eine Datei je Aussage, Dateiname gleich `id`, Frontmatter und die sechs Abschnitte wie in den vorhandenen Dateien. Den `INDEX.md` des Themas in derselben Änderung nachziehen. Ein neues Thema bekommt einen eigenen Unterordner mit englischem Namen in snake_case und eine Zeile im Wurzel-`INDEX.md`.
5. Jeder Bruchindikator braucht eine Ablesequelle mit Tier, sonst als blind kennzeichnen.
6. Bestehende Aussagen nicht überschreiben, sondern ändern mit neuem `stand` und der alten Fassung in der Git-Historie. Axiome ändert nur der Auftraggeber.
7. Zahlen nur mit Herkunft: belegt, Annahme oder Verweis auf ein Axiom.

## Quellen-Tiers

1a Filings, IR-Materialien, Calls. 1b Herstellerspezifikationen, Konferenzpapiere. Trade Press und Broker Notes sind kein Befund.

## Offenlegung

Der Auftraggeber hält eine Position in SK Hynix. Einträge, die der Position entgegenkommen, werden härter geprüft.
