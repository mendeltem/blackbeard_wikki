# agent_tooling: Kurzstand

Stand 2026-10-06. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Werkzeuge, auf deren Ausgabe sich jemand verlässt. Roter Faden: Ein Prüfwerkzeug, dessen eigener Fehler wie ein Befund aussieht, ist das gefährlichste.

**Getragen (alles Regeln):** Kein stiller Rückfallwert. Leer ist nicht fehlend. Unbekannt ist kein Wert in Vergleichen (`null <= 0` ist wahr). Erstmessung ist keine Veränderung. Gerechnetes und Gedeutetes getrennt halten (zwei Schichten).

**Vorschlag (aus dem Projekt rea übernommen):** Werkzeuge nach Aufgabenform schneiden (inspect, search, trace, compare, workflow, observe), Primitive vor Workflows, vollständige Ergebnisse, Belege inline, keine Bestätigungs-Schalter. Ob ein Agent das richtige Werkzeug wählt, zeigt nur eine Spur am echten Host, nicht Schema oder Wortüberlappung. Skills routen zuerst nach Zielart und gehen vor dem Abschluss ihre Checkliste durch. Tests belegen Aussagen (echter E2E vor Integration vor Goldens), nicht Verkabelung; verweigerte Berechtigung ist kein Bestehen.

**Lesen bei:** Code für Messung, Prüfung, Vorbedingungen, Melder, Berichte. MCP-Server, Agenten-Werkzeuge, Skills, Testaufbau.

**Vorschlag, neu 2026-10-07 (Alita):** Ein Waechter prueft die Vorbedingung (Treiber, Karte, Netz), bevor er neu startet; scheitert sie, meldet er einmal und pausiert. 445 Neustarts in fuenf Tagen waren Taetigkeit ohne Wirkung, und ein Fehlertext, der mit einer Zahl verglichen wird, sah aus wie "noch kein Platz".
