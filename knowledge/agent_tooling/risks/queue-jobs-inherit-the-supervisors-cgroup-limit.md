---
id: queue-jobs-inherit-the-supervisors-cgroup-limit
typ: risiko
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-12
herkunft: Alita, journalctl dauerlauf.service und systemd-oomd 2026-10-11 18:48 bis 2026-10-12 09:21, cgroup memory.pressure 09:50
verweist_auf: [conditions-need-an-expiry-event]
---

# Rechenauftraege erben die Speichergrenze des Aufsehers, und oomd toetet dann beide

## Aussage
Startet ein Dienst mit `MemoryHigh` (hier der Dauerlauf, 32 GiB) die
Rechen-Warteschlange als Kindprozess, laufen alle Trainings in derselben
cgroup. Braucht ein Training mehr (angemeldet 34 GiB, RSS 33 GiB), passiert
nicht ein sauberer Abbruch, sondern eine Kette:

1. Die cgroup haengt an `MemoryHigh`, der Kernel drosselt und raeumt
   (memory.events `high` 444 665 mal).
2. Das erzeugt Speicherdruck (memory.pressure 30-38 % im Leerlauf des Agenten).
3. `systemd-oomd` (Ubuntu-Vorgabe fuer `user@.service`: kill bei > 50 % fuer
   20 s) toetet die ganze Einheit, mit `KillMode=control-group` also auch
   Schlange und Training: "Killed dauerlauf.service due to memory pressure
   for user@1000.service being 74.52% > 50.00%".
4. `Restart=always` startet den Aufseher nach 30 s neu, die Schlange nimmt das
   Training von vorn: 25 Neustarts im 3-4-Minuten-Takt am 11.10. 18:48 bis
   21:49, fuenf weitere am 12.10. 08:01 bis 09:21. Kein Lauf kam durch.

Die Warteschlange hatte den Bedarf (34 GiB) gekannt und gegen den freien
System-RAM geprueft (62 GiB) -- nicht gegen die Grenze der cgroup, in der
sie selbst sitzt.

## Traegt
Jede Aufseher-Dienst-Konstruktion mit cgroup-Grenzen, aus der heraus schwere
Laeufe gestartet werden. Abhilfen, in dieser Reihenfolge: schwere Laeufe in
eine eigene cgroup (`systemd-run --user --scope`), Bedarfspruefung gegen
`memory.high` der eigenen cgroup, Grenze des Aufsehers nur fuer den
Aufseher selbst.

## Umgesetzt (2026-10-12, Alita)
Der Dauerlauf startet die Schlange per `systemd-run --user --scope -p
MemoryMax=56G` (kein MemoryHigh) ausserhalb seiner cgroup; `--abarbeiten`
haelt eine eigene flock-Sperre, damit ein neu gestarteter Aufseher nicht
parallel rechnet; die Schlange warnt, wenn der angemeldete RAM ueber
`memory.high`/`memory.max` der eigenen cgroup liegt; die Unit traegt kein
MemoryHigh mehr. Messlatte: `fehlerbilanz --seit 7`, Spalte Kills (25 am
11.10., 9 am 12.10. vor der Aenderung).

## Traegt nicht
Den kernel-OOM bei wirklich vollem RAM; der schlaegt unabhaengig von cgroup-
Grenzen zu.

## Bruchindikator
`journalctl --user -u <aufseher>`: "systemd-oomd killed N process(es)",
Restart-Zaehler steigt im Minutentakt; Staffelstab-Uebergaben ohne
"zurueck"-Zeile (41 Uebergaben, 9 Rueckmeldungen in 7 Tagen).

## Ablesung
Journal mit Datum, dauerlauf.log nur mit Uhrzeit; Druckwerte aus
`/sys/fs/cgroup/.../dauerlauf.service/memory.pressure`.

## Verknuepft
- [conditions-need-an-expiry-event](../rules/conditions-need-an-expiry-event.md)

**Nachtrag 2026-10-12 (nachmittags):** Zweites Loch im selben Werkzeug: `grossauftrag --abarbeiten` hielt nie die Haupt-flock der direkten Laeufe. Ein direkter `grossauftrag --gib 30` (recon-all, 3 x 26 GB) und ein eingereihter Lauf waeren nachts gleichzeitig gestartet (OOM, zwei recon-all auf derselben Sitzung). Jetzt prueft --abarbeiten je Lauf die flock nicht blockierend: ist sie gehalten, bleibt der Eintrag offen (rc 6) und kommt am naechsten Rundenende dran, damit der dauerlauf nicht stundenlang steht. Sicherung grossauftrag.vor-20261012-abarbeiten-flock.
