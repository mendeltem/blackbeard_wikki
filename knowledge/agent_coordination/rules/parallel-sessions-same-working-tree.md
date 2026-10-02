---
id: parallel-sessions-same-working-tree
typ: regel
status: getragen
thema: knowledge/agent_coordination
stand: 2026-10-02
herkunft: Projekt Verbund 2026-09-05 und blackbeard_wikki 2026-10-02
verweist_auf: [one-filename-two-contracts]
---

# Nicht in einen fremden Arbeitsbaum schreiben

## Aussage
An denselben Repos arbeiten mehrere Sitzungen gleichzeitig. Keine von ihnen
sieht die andere. Daraus folgen drei Regeln, alle aus Schaden gelernt:

**Vor dem Schreiben Zeitstempel lesen.**

    ls -la --time-style=+%H:%M:%S

Bewegen sich Dateien im Minutentakt, läuft dort eine andere Sitzung. Bei einem
Git-Repo ist `.git` der empfindlichste Zeiger: jünger als ein paar Minuten heißt
aktiv.

**Nicht in den fremden Arbeitsbaum schreiben, sondern in einen eigenen Klon.**
Der Grund ist nicht der Schreibkonflikt — die eigenen Dateien liegen meist auf
neuen Pfaden und kollidieren gar nicht. Der Grund ist das `git add -A` der
anderen Sitzung: es nimmt die fremden Dateien mit in ihren Commit und pusht sie,
ohne dass irgendjemand sie freigegeben hätte. Aus einem Lesevorgang wird so eine
Veröffentlichung.

**Den eigenen Lesestand als veraltet behandeln.** In einem aktiv bearbeiteten
Repo ist jede Übersicht, die älter als Minuten ist, falsch.

## Trägt
Jedes Repo, in dem mehr als ein Agent oder Chat arbeitet, und jedes gemeinsame
Gedächtnis. Auch diese Wiki: sie ist der Fall, für den die Regel zuletzt
gebraucht wurde.

Der eigene Klon ist billig. Ein ungewollt gepushter Commit ist es nicht.

## Trägt nicht
Sperren oder Reservierungen. Es geht um Lesen vor dem Schreiben und um
Trennung der Arbeitsbäume, nicht um ein Protokoll, an das sich alle halten
müssten — denn genau das lässt sich zwischen Sitzungen nicht durchsetzen.

Auch kein Argument gegen das gemeinsame Repo. Die Alternative — jeder sein
eigenes — ist teurer.

## Bruchindikator
Ein Commit, der Dateien enthält, die niemand in dieser Sitzung geschrieben hat.
Oder: zwei Einträge zum selben Gegenstand, die voneinander nichts wissen.

## Ablesung
Zwei eigene Fälle, beide beobachtet, keine fremde Quelle.

**2026-09-05, Verbund:** eine parallele Sitzung baute drei Seiten und schrieb in
jedem Repo eine eigene `daten.json` — dabei wurde eine vertragskonforme Datei
zweimal überschrieben. Folge siehe [one-filename-two-contracts](one-filename-two-contracts.md).

**2026-10-02, blackbeard_wikki:** eine Prüfung auf einen lokalen Klon ergab
"nicht vorhanden"; wenige Minuten später existierte er, `.git` war 60 Sekunden
alt, der Klon lag 6 Commits hinter `origin/main` und hatte 2 ungepushte Commits.
Zwischen zwei Lesungen im Abstand von rund zwei Stunden wuchs die Wiki von 2 auf
15 Themen. Der Abgleich der ersten Lesung war zum Zeitpunkt des Schreibens
vollständig veraltet.

## Verknüpft
- [one-filename-two-contracts](one-filename-two-contracts.md)
