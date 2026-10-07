# agent_tooling: Kurzstand

Stand 2026-10-07. Prefill für Chats und Agenten. Details in [INDEX.md](INDEX.md). Status je Eintrag dort.

Werkzeuge, auf deren Ausgabe sich jemand verlässt. Roter Faden: Ein Prüfwerkzeug, dessen eigener Fehler wie ein Befund aussieht, ist das gefährlichste.

**Getragen (alles Regeln):** Kein stiller Rückfallwert. Leer ist nicht fehlend. Unbekannt ist kein Wert in Vergleichen (`null <= 0` ist wahr). Erstmessung ist keine Veränderung. Gerechnetes und Gedeutetes getrennt halten (zwei Schichten).

**Vorschlag (aus dem Projekt rea übernommen):** Werkzeuge nach Aufgabenform schneiden (inspect, search, trace, compare, workflow, observe), Primitive vor Workflows, vollständige Ergebnisse, Belege inline, keine Bestätigungs-Schalter. Ob ein Agent das richtige Werkzeug wählt, zeigt nur eine Spur am echten Host, nicht Schema oder Wortüberlappung. Skills routen zuerst nach Zielart und gehen vor dem Abschluss ihre Checkliste durch. Tests belegen Aussagen (echter E2E vor Integration vor Goldens), nicht Verkabelung; verweigerte Berechtigung ist kein Bestehen.

**Lesen bei:** Code für Messung, Prüfung, Vorbedingungen, Melder, Berichte. MCP-Server, Agenten-Werkzeuge, Skills, Testaufbau.

**Vorschlag, neu 2026-10-07 (Alita):** Ein Waechter prueft die Vorbedingung (Treiber, Karte, Netz), bevor er neu startet; scheitert sie, meldet er einmal und pausiert. 445 Neustarts in fuenf Tagen waren Taetigkeit ohne Wirkung, und ein Fehlertext, der mit einer Zahl verglichen wird, sah aus wie "noch kein Platz".

**Regel (2026-10-07):** Ein `pip freeze` ist ein Protokoll, keine Installationsdatei (Build-Kennungen wie +cu124 und %2B brechen pip sofort). Auszuliefern ist die minimale, gepinnte Liste der echten Importe; getestet ist sie erst aus einem frischen Clone in neuer Umgebung bis zum Selbsttest, Log ins Repo.

**Vorschlag, neu 2026-10-07 (Aufsicht ueber einen lokalen Agenten, neun Regeln aus neun Vorfaellen):** Jede Sperre und jede zustandsabhaengige Anweisung bekommt beim Setzen ein Verfallsereignis; Sperren an Vollstaendigkeit haengen, nicht an "zu Ende" (eine `.rc`-Sperre oeffnete fuer einen abgebrochenen Lauf, eine CPU-Anweisung ueberlebte ihren Grund um 12 Stunden, Faktor 49). Die ersten N einer sortierten Liste sind ein Block (dreimal daneben, Vollzaehlung kostete 15 s). Vor dem Probelauf eines fremden Skripts nach Schreibzielen greppen -- ein "Trockenlauf" erfuellte ein Abnahmekriterium des Beaufsichtigten. Vor der ersten Aenderung einer fremden Datei `.vor-<stempel>` anlegen. Nachlauf als `trap EXIT`, einmal ausloesen, Logzeile suchen (ein angehaengter Block hinter vier `exit` war tot). Billige Vorpruefungen ordnen, entscheiden nicht (CPU-Rangliste vom GPU-Lauf widerlegt). Vor der Deutung einer gepoolten Zahl die tragenden Faelle zaehlen (3 Faelle = 28 % aller Laesionen). Namen am Code messen ("3D-ResNet" ohne Residuen). Erst die Definition zweier Zahlen suchen, dann die Differenz deuten (zwei Zuordnungsregeln, kein Widerspruch).

**Regel (2026-10-07):** "Installierbar" heisst frische Umgebung nur mit den README-Befehlen plus Gewichte vom Release, ein CI-Job auf fremdem Runner und jede CLI-Option einmal getestet; externe Programme (FSL) brauchen ihre Umgebungsvariablen vom Paket selbst, sonst haengen sie stumm.
