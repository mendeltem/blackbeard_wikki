---
id: blackboard-short-protocol-long-html
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-11
herkunft: Alita, Nutzerwunsch 2026-10-11; Bestandsaufnahme der Tafel (1614 Eintraege, 920 KB) und Umbau mit Pruefung durch fuenf unabhaengige Agenten
verweist_auf: [back-up-before-first-edit-of-a-foreign-file, never-edit-a-running-bash-script]
---

# Tafel: kurzes Protokoll in Markdown, alles Verstaendliche als gebaute HTML-Seiten

## Aussage
Eine gemeinsame Agenten-Tafel hat zwei Aufgaben, die sich widersprechen: Maschinen lesen sie
(Zeitfenster, letzte N Eintraege, Nummern als Zitat-IDs), Menschen wollen Zusammenhaenge, Zahlen
und Verlaeufe sehen. Beides in einer Markdown-Datei endet in einem unlesbaren Log. Trennung:
- **Markdown = Funktionskern.** Nur ueber das Schreibwerkzeug anhaengen (Sperre, Pruefungen,
  Nummer = groesste vorhandene + 1), 1-3 Zeilen mit Zahl und Einheit, Nutzerentscheidungen mit
  Praefix `ENTSCHEIDUNG:`, dazu ein Verweis auf die HTML-Seite. Nummern sind dauerhafte IDs.
- **HTML = abgeleitet, nie von Hand.** Ein Generator baut Startseite, Projektseiten mit Kennzahlen
  (je mit Quelle und Datum), Abbildungen direkt aus den Ergebnisdateien, offenen Punkten,
  Entscheidungen und Verweisen ins Wiki; ein Protokoll mit Anker je Eintrag. Neubau nach jedem
  Tafeleintrag (systemd-Path-Unit) und alle 30 Minuten (Timer, fuer neue Ergebnisse).
- **Datenschutzfilter im Generator**, nicht im Kopf des Schreibers: Fallkennungen und Initialen
  werden beim Bau ersetzt; die Seiten bleiben lokal und git-ignoriert.

## Belege (Alita, 11.10.2026)
- Vorher: 1614 Eintraege, 920 KB; 42 Eintraege fuer das Werkzeug unsichtbar (Kopfzeilen von Hand,
  Titel im Kopf, `[auto]`), 6 doppelte Nummern, ein Eintrag versehentlich in einer Wiki-Datei,
  98 direkte Anhaenge ohne Sperre. Ursache fast immer: Schreiben am Werkzeug vorbei.
- Sieben Programme lesen die Tafel (Zeitfenster 24 h, letzte 40, letzte 12, letzte 10); Nummern
  werden in 44 Dateien zitiert. Deshalb kein Umnummerieren und Archivieren nur mit byte-genauer
  Gegenpruefung, unter derselben Sperre, mindestens 14 Tage und 200 Eintraege bleiben.
- Bau: 16 Seiten, 13 Abbildungen in rund 4 s; Pruefung: 0 Fallkennungen, 0 tote lokale Links
  (3198 Links), Werkzeug erkennt 1614/1614 Eintraege (vorher 1572).

## Anwendung
Langtext, Tabellen, Plots nie auf die Tafel. Wer etwas Ausfuehrliches mitteilen will, schreibt es
in eine Faktendatei oder Ergebnisdatei, die der Generator liest, und auf die Tafel einen Satz mit Verweis.
