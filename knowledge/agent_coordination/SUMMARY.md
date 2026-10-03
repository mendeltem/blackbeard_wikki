# agent_coordination: Kurzstand

Stand 2026-10-03. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Mehrere Sitzungen arbeiten gleichzeitig an denselben Repos und sehen sich nicht. Der Schaden entsteht beim Annehmen, nicht beim Schreiben.

**Getragen:** Vor dem Schreiben Zeitstempel lesen, nie in einen fremden Arbeitsbaum schreiben (parallel-sessions-same-working-tree). Ein Dateiname hat genau einen Zweck, z. B. nicht `daten.json` zugleich als Quelle und Schnittstelle (one-filename-two-contracts).

**Lesen bei:** mehreren Agenten, geteilten Repos, Datenaustausch zwischen Projekten.
