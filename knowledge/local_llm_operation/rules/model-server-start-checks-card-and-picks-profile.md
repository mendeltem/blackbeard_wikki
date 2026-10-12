---
id: model-server-start-checks-card-and-picks-profile
typ: regel
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-12
herkunft: Alita (RTX A5000 24 GB, 62 GB RAM), Einbau 2026-10-12 09:00-09:20 waehrend ein 20-GiB-Training der Schlange lief
verweist_auf: [flash-next-177b-moe-on-24gb-card, foreign-gpu-process-before-measuring, moe-expert-offloading]
---

# Der Modellserver startet nur, wenn die Karte Platz hat, und mit dem Profil, das jetzt passt

## Aussage
Teilen sich Sprachmodell und GPU-Trainings eine Karte, darf der Start des
Modellservers nie blind `systemctl start` sein. Vorher drei Dinge pruefen:

1. **Wer haelt die Karte?** Eine Sperrdatei mit lebender PID (hier
   `~/data/work/.gpu-belegt`, geschrieben von der Rechen-Warteschlange).
   Lebt sie, kommen nur Profile in Frage, die als "neben einem Training
   ladbar" markiert sind (Registry-Feld `sperre_beachten: false`; auf Alita
   das 177B-MoE mit Experten im RAM, 7,5 GiB VRAM).
2. **Wie viel ist frei -- und wie viel davon ist schon versprochen?**
   `nvidia-smi memory.free` luegt in den ersten Minuten eines Laufs: das
   Training hatte beim Einbau nach 29 s noch 0 MiB auf der Karte, 20 GiB
   angemeldet. Deshalb den angemeldeten Bedarf des laufenden Eintrags
   (`--vram` des Halters oder der erste offene Eintrag der Schlange) minus
   das, was der Halter samt Kindprozessen laut `nvidia-smi
   --query-compute-apps` schon belegt, vom freien VRAM abziehen.
3. **Passt ein Profil?** Freier Rest >= `braucht_mib` des Profils -- dieselbe
   Schwelle, auf die das Startskript selbst wartet. Reihenfolge: eingestelltes
   Profil zuerst, dann die uebrigen, groesstes zuerst.

Passt nichts: **nichts starten, rc 3, Meldung mit Halter und Zahlen.**
Nicht einen wartenden Dienst zuruecklassen -- der nimmt sich die Karte in der
Luecke zwischen zwei Laeufen, und der naechste Lauf findet sie voll.

Das gewaehlte Profil gilt nur fuer diesen Start (`systemctl --user
set-environment QUANT=...`, gleich wieder geloescht). Der eingestellte
Standard bleibt, damit die Schlange am Ende und die Wache nach einem Absturz
den Server im gewohnten Profil zurueckholen. Der Agent liest sein
Kontextfenster vom LAUFENDEN Modell (`/v1/models`), nicht aus der Einstellung.

## Traegt
Jeden Agentenstart (`clara`, `agent`) auf einer Maschine, auf der eine
Warteschlange Trainings auf dieselbe Karte legt. Beim Einbau lief ein
20-GiB-Lauf: Entscheidung ohne Reservierung "flash passt (23 314 MiB frei)",
mit Reservierung "nur 2 834 MiB frei, braucht 7 500" -- rc 3, Schlange lief
ungestoert weiter.

## Traegt nicht
Trainings ohne Sperrdatei und ohne angemeldeten Bedarf: dann zaehlt nur der
momentan freie VRAM, und die Luecke zwischen zwei Laeufen bleibt eine Falle.
Auch nicht die Gegenrichtung: laeuft der Agent auf dem kleinen Profil, muss
die Schlange fuer einen schweren Lauf den Server weiterhin anhalten und
wartet dafuer, bis kein Agentenaufruf mehr laeuft (Staffelstab).

## Bruchindikator
Startlog mit "Warte mit dem Laden" waehrend ein Lauf rechnet; ein Lauf, der
mit CUDA-OOM stirbt, waehrend das Sprachmodell antwortet; RAM-Warnung beim
MoE-Profil (40 GiB gewuenscht, 24 verfuegbar neben einem Training): dann
kommen die Experten von der Platte.

## Ablesung
Umsetzung `system/werkzeuge/modellstart` (`--pruefen`, `--warten [s]`,
`--leise`, `QUANT=profil`), eingebaut in `agent.sh` (`--warten`) und `clara
--warten`. Zahlen aus `modellstart --pruefen` am 2026-10-12 09:14 bei
laufendem Turnier-Training (Eintrag 20 GiB) und 23 314 MiB frei.

## Verknuepft
- [flash-next-177b-moe-on-24gb-card](../findings/flash-next-177b-moe-on-24gb-card.md)
- [foreign-gpu-process-before-measuring](foreign-gpu-process-before-measuring.md)
- [moe-expert-offloading](../mechanisms/moe-expert-offloading.md)
