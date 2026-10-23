# agent_coordination

Mehrere Agenten und Chats arbeiten gleichzeitig an denselben Repos, ohne
voneinander zu wissen. Hier steht, was dabei schiefgeht und was dagegen hilft.

Abgrenzung zu [agent_tooling](../agent_tooling/INDEX.md): dort geht es um ein
Werkzeug und seine Ausgabe, hier um zwei Sitzungen und ein gemeinsames Repo.

Der rote Faden: **der Schaden entsteht nicht beim Schreiben, sondern beim
Annehmen.** Ein überschriebener Stand, ein fremder Commit, eine stumm falsch
gelesene Datei — in allen drei Fällen hat niemand einen Fehler gemacht, der
sichtbar geworden wäre.

Stand 2026-10-11. Ein Eintrag je Datei.

| Eintrag | Typ | Status |
|---|---|---|
| [Main rule: all work is in English](rules/everything-in-english.md) | regel | getragen |
| [Main rule: three data classes decide what may leave the institution](rules/three-data-classes-decide-what-may-leave-the-institution.md) | regel | vorschlag |
| [Do not log case-level content](rules/do-not-log-case-level-content.md) | regel | vorschlag |
| [/tmp is not volatile and session stores persist](findings/tmp-is-not-volatile-and-session-stores-persist.md) | befund | getragen |
| [Derived artifacts carry their source class](findings/derived-artifacts-carry-their-source-class.md) | befund | getragen |
| [Wachen: Pfadregel nach Rolle, nicht nach Einhängepunkt](findings/wachen-path-rule-by-role-not-by-mountpoint.md) | befund | getragen |
| [Research passes invent plausible PMIDs](findings/research-passes-invent-plausible-pmids.md) | befund | getragen |
| [Nicht in einen fremden Arbeitsbaum schreiben](rules/parallel-sessions-same-working-tree.md) | regel | getragen |
| [Ein Dateiname, ein Zweck](rules/one-filename-two-contracts.md) | regel | getragen |
| [Verknüpfte Seiten: eine Zuordnungsdatei, feste Adressen, Rückweg im Generator](rules/one-mapping-file-for-linked-pages.md) | regel | getragen |
| [Menschen lesen HTML, Agenten schreiben Markdown](rules/humans-read-html-agents-write-markdown.md) | regel | getragen |

## Herkunft

Beide Einträge stammen aus dem Bau des Verbunds — zehn Seiten in neun Repos mit
einem gemeinsamen Datenvertrag, gebaut von mehreren Sitzungen parallel
([AI_Lage](https://github.com/mendeltem/AI_Lage) ist die lesende Hauptseite) —
und aus der Arbeit an dieser Wiki selbst am 2026-10-02.
