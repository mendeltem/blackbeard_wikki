---
id: exit-hook-via-trap-then-verify-in-log
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [conditions-need-an-expiry-event]
---

# Nachlauf als trap EXIT einhaengen, einmal ausloesen und im Log nachsehen

## Aussage
Ein Sicherungsblock wurde an ein Synchronisationsskript angehaengt, das ueber vier
`exit`-Zweige verlaesst (kein Repository / nichts geaendert / gepusht / Push fehlgeschlagen).
Der Block stand hinter allen und war toter Code. Gemeldet war: "die Sicherung laeuft ab jetzt
taeglich" -- sie haette es nie getan. Aufgefallen nur, weil jemand nachsah, ob die erwartete
Zeile im Log steht.

Regel: in ein Skript mit mehr als einem Ausgang gehoert der Nachlauf als
`trap <funktion> EXIT`, direkt nach dem Log-Kopf definiert -- dann laeuft er auf jedem Zweig.
Nach dem Einrichten einmal AUSLOESEN und im Log die erwartete Zeile suchen; bei Cron-Haken den
unauffaelligsten Zweig testen (hier "nichts geaendert"), nicht den Erfolgsfall. Ein Haken, der
nicht laeuft, ist schlimmer als keiner: man verlaesst sich darauf. Dasselbe Muster wie bei
Sperren ohne Verfallsereignis -- die Einrichtung bezeugt sich selbst, statt gemessen zu werden.

## Traegt
Shell-Skripte mit Nachlauf (Sicherung, Aufraeumen, Melden), Cron- und systemd-Haken.

## Traegt nicht
---

## Bruchindikator
---

## Ablesung
Vorfall 2026-09-23. Tier 1a.

## Verknuepft
- [conditions-need-an-expiry-event](conditions-need-an-expiry-event.md)
- [restart-loop-is-an-alarm-not-a-repair](restart-loop-is-an-alarm-not-a-repair.md)
