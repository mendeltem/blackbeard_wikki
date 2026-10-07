---
id: conditions-need-an-expiry-event
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [restart-loop-is-an-alarm-not-a-repair, exit-hook-via-trap-then-verify-in-log]
---

# Jede Sperre und jede zustandsabhaengige Anweisung braucht ein benanntes Verfallsereignis

## Aussage
An einem Tag dreimal dieselbe Wurzel: eine Aussage war beim Aufschreiben richtig und wurde
durch ein Ereignis falsch, ohne dass jemand sie widerrief.
1. Eine Sperre "warte, bis diese fuenf Ergebnisdateien da sind" gab, als sie entstanden,
   genau den Auftrag frei, der die 10-Stunden-Rechnung WIEDERHOLT haette.
2. Eine Sperre auf eine `.rc`-Datei bezeugte "irgendein Lauf ist zu Ende" -- auch ein
   abgebrochener bei 21 von 110 Faellen -- statt "der Lauf ist vollstaendig".
3. Die Anweisung "rechne auf CPU" stand ohne ihren Grund ("weil die GPU belegt ist"); der
   Grund entfiel nach 15 Minuten, die Anweisung lief 12 Stunden weiter: 408 s je Fall statt 8 s,
   Faktor 49 verschenkt.

Zwei Proben beim Setzen:
- Bei einer Sperre: *Was passiert, wenn die Datei entsteht -- will ich DANN, dass genau dieser
  Auftrag laeuft? Und entsteht sie auch, wenn es schiefging?* Sperren gehoeren an
  **Vollstaendigkeit** (Zeilenzahl, Fallzahl, Pflichtfelder), nicht an "etwas ist zu Ende"
  (`.rc`, Prozessende, Zeitpunkt).
- Bei einer zustandsabhaengigen Anweisung: *Woran erkenne ich, dass der Zustand endet, und
  steht der Widerruf im Text?* Richtig: "rechne auf CPU, SOLANGE Lauf X laeuft; danach
  umstellen", nicht "rechne auf CPU".

Eine Ausnahme von einem Kriterium soll sich selbst erledigen: "fehlende Ausgabe gilt nur dort
als entschuldigt, wo NaN sie erklaert" verlangt die Faelle automatisch wieder, sobald die
Reparatur drin ist; eine feste Ausnahmeliste haette sie dauerhaft entschuldigt.

## Traegt
Auftragstexte, Abnahmekriterien, Warteschlangen-Sperren, Cron-Haken, Anweisungen an Unteragenten.

## Traegt nicht
Einmalige, sofort ausgefuehrte Befehle.

## Bruchindikator
---

## Ablesung
Drei Vorfaelle 2026-09-14, Kosten teils real (12 CPU-Stunden), teils knapp vermieden. Tier 1a.

## Verknuepft
- [restart-loop-is-an-alarm-not-a-repair](restart-loop-is-an-alarm-not-a-repair.md)
- [exit-hook-via-trap-then-verify-in-log](exit-hook-via-trap-then-verify-in-log.md)
