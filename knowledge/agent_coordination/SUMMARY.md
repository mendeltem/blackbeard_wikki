# agent_coordination: Kurzstand

Stand 2026-10-11. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Mehrere Sitzungen arbeiten gleichzeitig an denselben Repos und sehen sich nicht. Der Schaden entsteht beim Annehmen, nicht beim Schreiben.

**Getragen:** Vor dem Schreiben Zeitstempel lesen, nie in einen fremden Arbeitsbaum schreiben (parallel-sessions-same-working-tree). Ein Dateiname hat genau einen Zweck, z. B. nicht `daten.json` zugleich als Quelle und Schnittstelle (one-filename-two-contracts).

**Seitenverbund (2026-10-06, getragen):** Use-Case-Board, Supply Atlas und AI_Companys sind verlinkt. Alle Zuordnungen nur in `ai_use_cases_overview/deployments.json`; Adressen `#uc=<slug>`, `?uc=`, `?company=`, `#/<lang>/<TICKER>` nicht ohne alle drei Seiten ändern; Rückweg auf AI_Companys steht in `werkzeuge/seite.py`, nicht in der HTML (one-mapping-file-for-linked-pages).

**Wiki-Lesefassung (2026-10-11, getragen):** Menschen lesen die erzeugte HTML-Seite `docs/index.html` (Suche, Kurzstand, aufklappbare Einträge, Rückverweise), Agenten schreiben weiter Markdown mit Frontmatter; `docs/` wird mit `tools/general/wiki_html` nach jedem Beitrag neu gebaut (pre-commit-Haken), nie von Hand (humans-read-html-agents-write-markdown).

**Lesen bei:** mehreren Agenten, geteilten Repos, Datenaustausch zwischen Projekten.
