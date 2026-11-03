---
id: archive-tier-copy-hash-both-sides-then-symlink
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-11
herkunft: Alita, /home zu 97 % voll; Werkzeug system/werkzeuge/archivieren, Archivstufe auf externer SSD (exFAT)
verweist_auf: [data-move-by-rename-symlink-and-protocol, grep-for-write-targets-before-a-dry-run, first-n-of-a-sorted-list-is-a-block]
---

# Archivstufe: kopieren, beide Seiten hashen, erst dann loeschen und verlinken

## Aussage
Wenn Daten die interne Platte **verlassen** (anderes Dateisystem, externer Traeger), reicht Umbenennen nicht mehr
(siehe [[data-move-by-rename-symlink-and-protocol]]). Dann gilt: **kopieren, auf beiden Seiten SHA-256 ueber jede
Datei bilden, die Listen byteweise vergleichen, und nur bei Gleichstand das Original loeschen und am alten Ort
einen Symlink auf das Archiv setzen.** Jede Operation in ein Protokoll (TSV), aus dem Index-Seiten und ein
`--rueckgaengig` erzeugt werden. Ein Ordner, der nicht geprueft anderswo liegt, wird nicht geloescht (Tafelregel 5).

## Warum nicht einfach `mv` oder `rsync --remove-source-files`
- `mv` ueber Dateisystemgrenzen ist Kopieren plus Loeschen ohne Pruefung; ein USB-Aussetzer mitten drin
  hinterlaesst eine halbe Datei, die wie eine ganze aussieht (Tafelregel 2).
- `rsync -c` vergleicht nur Quelle gegen Ziel waehrend des Kopierens, nicht das, was spaeter auf dem Traeger liegt.
  Die gespeicherte Pruefsummenliste (`.PRUEFSUMMEN.sha256` im Archivordner) erlaubt eine spaetere Nachpruefung
  ohne Quelle (`--pruefen`).

## Was der Traeger kaputt macht (gemessen 11.10.)
- **exFAT speichert keine Symlinks, Rechte oder Besitzer.** Symlinks werden uebersprungen und als `Pfad<TAB>Ziel`
  in `.SYMLINKS.txt` notiert; `--rueckgaengig` legt sie wieder an. Eine venv mit `lib64 -> lib` wuerde mit `-L`
  verdoppelt, ohne Notiz ginge sie verloren.
- **Code, der spaeter auf dem archivierten Ordner weiterlaeuft, scheitert an `symlink()`** (Lauf 30.10., gefunden 02.11.):
  eine Pipeline legte pro Fall einen Symlink an (`Path.symlink_to`), nach dem Archivieren auf exFAT warf das
  `OSError: [Errno 1] Operation not permitted` fuer alle 96 Faelle. Das Skript fing den Fehler pro Fall ab, schrieb ihn
  in die Statustabelle und lief "fertig" durch; Abschlussmeldung kam trotzdem. **Regel:** vor dem Archivieren eines
  noch genutzten Ordners `grep -rn "symlink\|os.link"` im zugehoerigen Code; Abhilfe `try: symlink except OSError: copyfile`.
  Und nach jedem Lauf die Statusspalte zaehlen, nicht nur die Fertigmeldung lesen.
  **Wiederholung 03.11.:** derselbe Lauf hatte einen zweiten Symlink im Bash-Teil (`ln -sf` fuer den Stapelordner);
  der grep oben trifft `ln -s` nicht, SynthSeg lief auf 0 Bildern und meldete wieder "fertig". Ein Ersatzordner mit
  unverdaechtigem Pfad lag ebenfalls auf exFAT (Elternordner war selbst ein Link aufs Archiv). Also: `grep -n "ln -s\|symlink\|os.link"`
  ueber ALLE Skripte der Kette, Zielordner per `df -T` pruefen, und jeder Schritt zaehlt seine Eingaben und bricht bei 0 ab.
- **Zeitstempel sind auf exFAT grob** (10 ms, teils 2 s): `rsync -t --modify-window=2`, sonst kopiert jeder Lauf alles neu.
- **Eine zweite Platte war defekt und sah leer und benutzbar aus:** eingehaengt, 1,9 TB frei, `ls` leer. Erst der
  Schreibtest (`touch` -> Ein-/Ausgabefehler) und SMART ueber udisks (5 848 neu zugewiesene, 10 528 schwebende Sektoren,
  Lesefehler im Dateisystembereich) zeigten es. **Vor dem ersten Archivlauf: Schreibtest, SMART, Durchsatz messen**
  (SanDisk Extreme: 588 MB/s schreiben, ~1 GB/s lesen an USB 10 Gbit; 3,1 GB mit Pruefung in 13 s).

## Vorbedingungen, die das Werkzeug prueft (nicht der Mensch)
Quelle ist Verzeichnis und kein Symlink; keine offenen Dateideskriptoren oder Arbeitsverzeichnisse von Prozessen
unter der Quelle (`/proc/*/fd`, `/proc/*/cwd`); Archivplatte eingehaengt; freier Platz > Quelle + 1 GiB.
Vorher von Hand: Treffer der Quelle in offenen Auftraegen und Skripten aktiver Projekte zaehlen -- ein Wortteil wie
`microbleed` trifft 96 Skripte und sagt nichts, ein Ordnername wie `gitter_d` trifft 87 Stellen und sagt: Symlink noetig.

## Was wandert, was bleibt
- Wandert: gleiche Modelle in weiteren Quantisierungen (hier 89 GB von 160), abgeschlossene Turniere und alte
  Trainingsgitter einer eingefrorenen Kette, Stick-Kopien, verwaiste venvs, Projekte ohne Aenderung seit Wochen.
- Bleibt: alles mit offenen Handles oder Treffern in laufenden Auftraegen; gemeinsam genutzte Ordner
  (ein Projekt liest die Konfiguration eines anderen); Caches werden geloescht, nicht archiviert (16 GB pip/uv).
- Kleine Altordner unter 1 GB sind eine Frage der Ordnung, nicht des Platzes -- Nutzerentscheidung, hier: bleiben.

## Nebenwirkung, die man benennen muss
Eine taegliche Sicherung, die Symlinks folgt (`rsync -rtL`) und auf **dieselbe** externe Platte schreibt, kopiert
archivierte Ordner von der SSD auf die SSD. Das ist keine Sicherung mehr, nur Platz. Hier betroffen: der
Turnierordner (28 GB) liegt nach dem Umzug zweimal auf dem Traeger. Patientenkohorten auf einem unverschluesselten
USB-Traeger sind eine Entscheidung des Nutzers, nicht des Werkzeugs; das Werkzeug schreibt sie ins Protokoll.

## Stand
`archivieren QUELLE UNTERPFAD | --pruefen | --rueckgaengig | --index`; Protokoll `ARCHIV/PROTOKOLL.tsv`,
Index `~/ARCHIV.md` und `ARCHIV/README.md`, README je Archivordner. Erster Lauf 11.10.2026: 16 Ordner, 223 GiB (gemessen, PROTOKOLL.tsv),
/home von 97 % auf 71 % (27 -> 259 GB frei).
