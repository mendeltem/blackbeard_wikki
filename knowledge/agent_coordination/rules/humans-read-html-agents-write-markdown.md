---
id: humans-read-html-agents-write-markdown
typ: regel
status: getragen
thema: knowledge/agent_coordination
stand: 2026-10-11
herkunft: Nutzerregel Mendel 2026-10-11 (Wiki und Tafel), Bau von tools/general/wiki_html
verweist_auf: [one-filename-two-contracts, parallel-sessions-same-working-tree]
---

# Menschen lesen HTML, Agenten schreiben Markdown: die Wiki hat eine Quelle und eine erzeugte Lesefassung

## Aussage
Alle Information der Wiki wird für Menschen über die erzeugte HTML-Seite gelesen (`docs/index.html`, mit Links auf jede andere Seite, Suche, Kurzstand je Bereich, Einträge aufklappbar, Verweise und Rückverweise, Plots). Die Quelle bleibt Markdown mit Frontmatter, eine Datei je Aussage, wie im README beschrieben; nur die `README.md` ist zugleich Quelle und Lesetext. Agenten schreiben nie HTML von Hand in die Wiki. Nach jedem Beitrag wird `docs/` mit `tools/general/wiki_html` neu gebaut und mit eingecheckt (lokal übernimmt das der pre-commit-Haken). `docs/` wird nie von Hand bearbeitet; was dort fehlt, fehlt in der Quelle.

## Trägt
Gilt für diese Wiki und sinngemäß für die Tafel (`BLACKBOARD.md` als Funktionskern, Tafel-HTML als Lesefassung). Gründe für Markdown als Quelle: dieselbe Information kostet in HTML etwa das Zwei- bis Dreifache an Tokens, und `SUMMARY.md` geht als Prefill in lokale Modelle mit knappem Kontext; kleine lokale Modelle schreiben Markdown zuverlässig und lassen in HTML Tags offen; Markdown-Diffs lassen sich bei parallelen Sitzungen lesen und zusammenführen; Prüfwerkzeug, Vorlagen, Skill und claude.ai-Projekt hängen am Frontmatter. Maschinen bekommen zusätzlich `docs/index.json` (Titel, Pfad, Bereich, Typ, Status, Stand, Kurztext je Eintrag).

## Trägt nicht
Eine Veröffentlichung über GitHub Pages: für das private Repo im aktuellen Plan nicht möglich (geprüft 2026-10-11, HTTP 422). Bis dahin wird `docs/` aus dem Clone gelesen oder über einen lokalen Server. Ein öffentliches Pages-Repo würde den Wiki-Inhalt öffentlich machen und ist eine eigene Entscheidung von Mendel.

## Bruchindikator
Ein Eintrag steht nur in `docs/` und nicht in `knowledge/`; eine Sitzung schreibt HTML-Dateien von Hand; `docs/index.html` ist älter als der jüngste Markdown-Commit (dann fehlt der Haken in diesem Clone, siehe `tools/general/wiki_html/INSTALL.md`).

## Ablesung
Nutzeranweisung 2026-10-11 ("statt md außer dem ersten README.md sollte alle Information jetzt nur über HTML gehen; index.html mit Links zu jedem anderen HTML, intelligent gebaut"), Entscheidung im Gespräch: Markdown bleibt Quelle, HTML wird erzeugt. Tier: Setzung des Nutzers plus Messung (Linkprüfung 5463/0 tot).

## Verknüpft
[one-filename-two-contracts](one-filename-two-contracts.md): Quelle und Lesefassung sind zwei Dateien mit je einem Zweck. [wiki_html](../../../tools/general/wiki_html/README.md), [wiki_maintenance](../../../tools/general/wiki_maintenance/README.md).
