---
id: back-up-before-first-edit-of-a-foreign-file
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [grep-for-write-targets-before-a-dry-run]
---

# Vor der ersten Aenderung an einer fremden Datei eine Sicherung mit Stempel

## Aussage
Eine fremde Abnahmedatei an einem Vormittag fuenfmal geaendert, kein einziges Mal vorher
gesichert -- waehrend ich im selben Zeitraum bei anderen genau diese Disziplin pruefte. Ohne
Versionskontrolle (kein Projekt im Arbeitsverzeichnis hatte ein `.git`) ist die Konvention
`.vor-<stempel>` der einzige Rueckweg; wer sie nicht einhaelt, macht jede Aenderung
unumkehrbar und merkt es erst, wenn er zurueck will.

Regel: vor der ERSTEN Aenderung einer Datei, die mir nicht gehoert,
`cp <datei> <datei>.vor-<HHMM>-<wer>`. Einmal je Sitzung und Datei genuegt; es geht um den
Rueckweg, nicht um jede Zwischenstufe. Gilt fuer Abnahmedateien, Auftragstexte, Skripte,
Protokolle. Beim Pruefen fremder Aenderungen mitzaehlen, ob eine Sicherung von HEUTE existiert:
`find <dir> -maxdepth 1 -name "<datei>.vor-*" -newermt "$(date +%F)"`.
Wo git vorhanden ist, ersetzt ein Commit vor der Aenderung die Kopie.

## Traegt
Jede Datei ausserhalb der Versionskontrolle, die ein anderer Agent oder Mensch liest.

## Traegt nicht
Dateien unter git mit sauberem Arbeitsbaum.

## Bruchindikator
---

## Ablesung
Vorfall 2026-09-15. Tier 1a.

## Verknuepft
- [grep-for-write-targets-before-a-dry-run](grep-for-write-targets-before-a-dry-run.md)
