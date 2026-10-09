---
id: data-move-by-rename-symlink-and-protocol
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-09
herkunft: Alita, Umbau ~/data in DATEN/{OPEN,PRIVAT}/{ORIGINAL,DERIVATIVES} und PROJEKT (Werkzeug system/werkzeuge/datenumzug)
verweist_auf: [back-up-before-first-edit-of-a-foreign-file, conditions-need-an-expiry-event, grep-for-write-targets-before-a-dry-run]
---

# Datenumzug: umbenennen, Symlink zurueck, Protokoll fuer den Rueckweg

## Aussage
Ein Forschungsbaum mit Tausenden fest verdrahteter Pfade (Skripte, Auftraege mit `BRAUCHT:`, Cron, Agenten-Skills)
wird nur so umgezogen: **auf demselben Dateisystem umbenennen, am alten Ort sofort einen Symlink setzen und jede
Operation in ein Protokoll schreiben**, aus dem ein `--rueckgaengig` die Schritte rueckwaerts abspielt.
Nichts kopieren, nichts loeschen. Vorher ein Trockenlauf, der je Projekt zeigt, welche Bloecke wohin gehen.

## Was beim Trennen von Code und Daten zaehlt
- **Ganze Unterordner ohne Code** wandern als Block, einzelne Bild- oder Gewichtsdateien neben Code einzeln.
  Dateinamen wie `x.py.vor-0919` gelten als Code (Endung irgendwo im Namen), sonst wandern Sicherungskopien mit den Daten.
- **Einteilung oeffentlich/intern: im Zweifel intern.** Ordner, die oeffentliche und eigene Faelle mischen
  (LOCO, Endmodelle auf allen Daten), stehen als ausdrueckliche Pfadliste im Werkzeug, nicht nur als Muster.
- **Muster pruefen, bevor man ihnen traut:** `swi` traf `swinvit`, `turnier` schob alle oeffentlichen Turnierlaeufe
  nach intern. Erst die Bilanz je Projekt lesen, dann die Muster schaerfen (gemessen: 8 statt 44 GB intern in der VALDO-Linie).
- **Git-Repos:** neue Symlinks in `.git/info/exclude`, sonst werden sie committet.
- **Schreibgeschuetzte Rohdatenordner** (r-x) nur fuer den einen Umzug oeffnen und sofort wieder schliessen.

## Was ein Symlink bricht
- `rsync -r`/`-rt` ohne `-L` **ueberspringt** Symlinks still: Sicherungen vorher auf `-rtL` stellen.
- Docker-Bind-Mounts loesen nur den eingehaengten Pfad selbst auf; Symlinks **darin**, die aus dem Mount herauszeigen,
  sind im Container tot.
- `find` ohne `-L` sieht unter dem alten Pfad nichts mehr; Zaehlungen danach mit `-L` oder am neuen Ort.

## Nachpruefung (gehoert ins Werkzeug, nicht in die Erinnerung)
Tote Links, `BRAUCHT:`-Pfade aller offenen Auftraege, echte Datendateien unter PROJEKT, Antwort der QC-Server.

## Stand
Werkzeug und Index-Generator (`datenindex`: README je Ordner, Index im Home) fertig und am Abbild getestet; die
Ausfuehrung startet der Nutzer, weil die Rechtepruefung des Agenten einen Massenumzug als irreversibel einstuft.
