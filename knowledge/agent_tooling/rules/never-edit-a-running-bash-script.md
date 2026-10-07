---
id: never-edit-a-running-bash-script
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: PVS-Arena Alita, DRIPS-Rauchtest 2026-10-07 21:05-21:20
verweist_auf: [back-up-before-first-edit-of-a-foreign-file, exit-hook-via-trap-then-verify-in-log]
---

# Ein laufendes Bash-Skript nie editieren: bash liest die Datei waehrend der Ausfuehrung weiter

## Aussage
Bash liest ein Skript nicht am Anfang komplett ein, sondern Stueck fuer Stueck waehrend es laeuft. Wird die Datei
veraendert, waehrend ein langer Befehl darin (hier `docker run`, 40 s) laeuft, setzt bash danach am alten Byte-Offset
in der NEUEN Datei fort: Zeilenbruchstuecke werden als Befehle gelesen ("syntax error near unexpected token `('"), die
Nacharbeit (Ergebnisdateien verschieben, Tempordner loeschen) entfaellt, und die Ergebnisse liegen verwaist im
Tempordner, waehrend das Log einen Fehler meldet, der mit dem Lauf nichts zu tun hat. Beobachtet beim DRIPS-Runner:
Patch (Resample-Schritt) waehrend eines laufenden Rauchtests eingespielt, der Rauchtest brach mit Syntaxfehler ab,
die fertige Vorhersage lag in tmp/.

## Traegt
Jedes Bash-Skript, das laenger laeuft als die Zeit bis zum naechsten Edit (Runner, Download-Schleifen, Ketten).
Vorschrift: Aenderungen in eine NEUE Datei schreiben (v2) oder warten, bis kein Prozess das Skript mehr ausfuehrt
(`pgrep -f <name>`); Python- und kompilierte Programme sind davon nicht betroffen (ganz eingelesen).

## Traegt nicht
Skripte, die als Funktion in den Speicher geladen oder per `bash -c "$(cat skript)"` gestartet wurden.

## Bruchindikator
Ein bash, das Skripte vollstaendig puffert (nicht bekannt).

## Ablesung
pvs-arena/logs/drips_smoke_belove.log (Syntaxfehler in Zeile 13 der inzwischen geaenderten Datei), tmp/drips.AKSt mit
fertigen Ausgaben; Rekonstruktion 2026-10-07 21:25.

## Verknuepft
- [back-up-before-first-edit-of-a-foreign-file](back-up-before-first-edit-of-a-foreign-file.md)
- [exit-hook-via-trap-then-verify-in-log](exit-hook-via-trap-then-verify-in-log.md)
