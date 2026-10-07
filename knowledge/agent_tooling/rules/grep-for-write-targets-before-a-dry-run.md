---
id: grep-for-write-targets-before-a-dry-run
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [back-up-before-first-edit-of-a-foreign-file]
---

# Vor dem Probelauf eines fremden Skripts nach Schreibzielen greppen

## Aussage
Ein fremdes Skript "zum Ausprobieren, ob es durchlaeuft" gestartet -- es schrieb seine
Ergebnisdatei (1 651 B) und erfuellte damit ein Abnahmekriterium des beaufsichtigten Agenten:
die Abnahme sprang von 2/5 auf 3/5, der Monitor meldete "Ergebnisdatei entstanden". Von aussen
sah das Versehen des Aufsehers wie Fortschritt des Agenten aus. Der Beleg (`open(ERG, "w")`)
stand zwei Zeilen vorher in derselben Ausgabe.

Regel: vor dem Ausfuehren eines fremden Skripts in einem EIGENEN Aufruf davor
`grep -nE "open\(.*[\"']w|write_text|json.dump|to_csv|shutil|os.rename|mv " <datei>`.
Faellt ein Schreibziel an, das in einer Abnahme oder einem Ergebnisordner vorkommt: nicht
ausfuehren. Statt "laeuft es durch?" Importe und Funktionen einzeln pruefen oder das
Ausgabeziel auf das Kratzverzeichnis umbiegen. Ist es doch passiert: Datei umbenennen
(nicht loeschen), Stand gegenmessen, Vorgang ins Protokoll.

Grundsatz: Wer eine Abnahme bewertet, darf nichts erzeugen, was sie bewertet. Ein selbst
erfuelltes Kriterium faelscht die Messung wie eine abgeschriebene Zahl.

## Traegt
Aufsicht ueber Agenten mit dateibasierter Abnahme; jedes Skript, das man nicht selbst geschrieben hat.

## Traegt nicht
Skripte, deren Ausgabeziel per Argument ins Kratzverzeichnis zeigt.

## Bruchindikator
---

## Ablesung
Vorfall 2026-09-15. Tier 1a.

## Verknuepft
- [back-up-before-first-edit-of-a-foreign-file](back-up-before-first-edit-of-a-foreign-file.md)
- [tests-prove-claims-not-plumbing](tests-prove-claims-not-plumbing.md)
