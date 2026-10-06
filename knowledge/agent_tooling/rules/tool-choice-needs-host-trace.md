---
id: tool-choice-needs-host-trace
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-06
herkunft: Projekt rea (morluto/rea, MIT), docs/tool-design.md, Stand b6c21b1 vom 2026-10-05; eigene Fälle aus local_models
verweist_auf: [agent-tools-by-task-shape, self-evolution-gepa-silently-falls-back, laya-router-before-agent, lean-hermes-toolsets]
---

# Ob ein Agent das richtige Werkzeug wählt, zeigt nur eine Spur am echten Host

## Aussage
Ein gültiges Schema, eine schöne Beschreibung oder hohe Wortüberlappung zwischen
Aufgabe und Werkzeugtext beweisen nicht, dass ein Agent das Werkzeug findet und
richtig aufruft. rea verlangt dafür Läufe mit repräsentativen Aufgaben, breit und
direkt formuliert, auf dem Host und Modell, für die das Werkzeug gedacht ist.
Festgehalten wird je Lauf:

- Host und Modell
- der Werkzeugkatalog, den das Modell tatsächlich sah
- gewähltes Werkzeug und Argumente
- Fehler und Wiederholungen
- ob die Aufgabe gelöst wurde

Auch die Größe des Katalogs in Bytes misst weder Nutzbarkeit noch Kontextkosten
für das Modell.

## Trägt
Jede Änderung an Werkzeugnamen, -beschreibungen oder Toolsets für Hermes, OpenCode
oder eigene MCP-Server. Zwei eigene Fälle passen dazu:
- Das Nous-Repo hermes-agent-self-evolution bewertet Skill-Varianten mit einer
  Wortüberlappungs-Metrik, siehe
  [self-evolution-gepa-silently-falls-back](../../local_llm_operation/risks/self-evolution-gepa-silently-falls-back.md).
  Nach dieser Regel misst das nichts über die Werkzeugwahl.
- Laya als Werkzeug innerhalb von Hermes brachte keinen Zeitgewinn, Laya als Weiche
  davor 0,1 s je Entscheidung, siehe
  [laya-router-before-agent](../../local_llm_operation/findings/laya-router-before-agent.md).
  Das zeigte erst der echte Lauf, nicht die Konfiguration.

## Trägt nicht
Wie viele Läufe reichen. rea nennt keine Zahl.

## Bruchindikator
Eine Werkzeugänderung wird als Verbesserung gemeldet, ohne dass eine Spur mit
gewähltem Werkzeug und Ergebnis vorliegt.

## Ablesung
Projekt-Doku: https://github.com/morluto/rea/blob/main/docs/tool-design.md
(Abschnitt "Implement and evaluate") und AGENTS.md (Abschnitt "Testing Guidelines").
Eigene Fälle wie verlinkt.

## Verknüpft
- [agent-tools-by-task-shape](agent-tools-by-task-shape.md)
- [self-evolution-gepa-silently-falls-back](../../local_llm_operation/risks/self-evolution-gepa-silently-falls-back.md)
- [laya-router-before-agent](../../local_llm_operation/findings/laya-router-before-agent.md)
- [lean-hermes-toolsets](../../local_llm_operation/findings/lean-hermes-toolsets.md)
