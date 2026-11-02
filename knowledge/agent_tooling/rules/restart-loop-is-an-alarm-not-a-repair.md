---
id: restart-loop-is-an-alarm-not-a-repair
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Modellwache des llama-servers, 2026-10-02 bis 2026-10-07
verweist_auf: [no-silent-fallback-values, secure-boot-kernel-update-unloads-nvidia-dkms]
---

# Eine Neustartschleife ist ein Alarm, keine Reparatur

## Aussage
Ein Waechter, der einen Dienst neu startet, muss vorher die **Vorbedingung** des
Dienstes pruefen (Treiber geladen, Karte sichtbar, Platz frei, Netz da). Scheitert
die Vorbedingung, darf er nicht neu starten, sondern muss **einmal** laut melden,
die Ursache nennen und pausieren, bis die Vorbedingung wieder erfuellt ist.

Auf Alita startete die Modellwache den llama-server alle 15 Minuten neu, weil er
auf `/health` nicht antwortete -- 445 Mal in fuenf Tagen. Der Server konnte nie
antworten: der NVIDIA-Treiber war nach einem Kernel-Update nicht geladen
(siehe [secure-boot-kernel-update-unloads-nvidia-dkms](../../local_llm_operation/risks/secure-boot-kernel-update-unloads-nvidia-dkms.md)).
Jeder Neustart schrieb eine Zeile auf das Blackboard, die wie Taetigkeit aussah;
die eine Zeile, die gefehlt hat, war "Treiber nicht geladen, ich warte".
Das Startskript selbst wartete in einer Schleife auf freien GPU-Speicher und
verglich dabei einen Fehlertext mit einer Zahl -- der Fehler sah aus wie
"noch nicht genug Platz".

Daraus die Regel in drei Teilen:
1. **Vorbedingung vor Neustart.** Was der Dienst zum Laufen braucht, prueft der
   Waechter selbst; ein fehlgeschlagener Health-Check ohne erfuellte Vorbedingung
   ist kein Neustartgrund.
2. **Einmal melden, dann schweigen.** Dieselbe Ursache erzeugt eine Meldung mit
   Zeitstempel und einen Zaehler, nicht hundert gleiche Zeilen.
3. **Fehlertext ist kein Messwert.** Ein Werkzeug, das eine Zahl erwartet, muss
   bei Nicht-Zahl abbrechen und den Text zeigen -- nicht `0` annehmen und warten
   (Sonderfall von [no-silent-fallback-values](no-silent-fallback-values.md)).

## Traegt
Jeden Waechter, Cron-Job oder systemd-`Restart=`, der einen Dienst am Leben haelt,
dessen Betrieb an Hardware oder einem anderen Dienst haengt.

## Traegt nicht
Dienste, die wirklich nur sporadisch haengen und deren Vorbedingungen trivial sind.
Dort ist ein Neustart mit Begrenzung (StartLimitBurst) richtig.

## Bruchindikator
Ein Fall, in dem das Neustarten ohne Vorbedingungspruefung schneller geholfen hat
als Melden und Warten -- etwa weil die Vorbedingung selbst durch den Neustart
hergestellt wird.

## Ablesung
Blackboard-Protokoll Alita, Eintraege [958] bis [1413], 2026-10-02 18:27 bis
2026-10-07 09:36; Startskript-Log des llama-servers. Tier 1a (eigene Logs).

## Verknuepft
- [no-silent-fallback-values](no-silent-fallback-values.md)
- [secure-boot-kernel-update-unloads-nvidia-dkms](../../local_llm_operation/risks/secure-boot-kernel-update-unloads-nvidia-dkms.md)

## Umgesetzt 2026-11-02
Die Regel stand seit 07.10., gebaut war sie nicht: die Wache startete den Server weiter ohne Grenze (457 Neustarts bis 22.10.). Seit 02.11.: hoechstens 3 Start-/Neustartversuche in 2 h ohne gesunde /health-Antwort, dann 2 h Pause und eine Telegram-Meldung (werkzeuge/wache, Simulation mit Stummeln getestet). Siehe [rules-that-repeat-become-checks](rules-that-repeat-become-checks.md).
