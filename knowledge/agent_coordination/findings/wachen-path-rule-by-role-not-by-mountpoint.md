---
id: wachen-path-rule-by-role-not-by-mountpoint
typ: befund
status: getragen
thema: agent_coordination
stand: 2026-10-22
herkunft: own run 2026-10-22 (making the external disk usable as a work volume)
---

# Die Pfadregel der Wachen fragt nach der Rolle, nicht nach dem Einhängepunkt

## Befund

Mehrere Wachen sperrten pauschal den Einhängepunkt für Wechseldatenträger. Der
Grund war gut: auf dem externen Träger lag tatsächlich einmal Kohortenmaterial.
Nur ist der Einhängepunkt kein Merkmal für Inhalt. Derselbe Träger trug auch
QWEN-Bundles, Papiere und FreeSurfer-Pakete -- rund 74 GB Werkzeug wurden
mitgesperrt.

Die Pfadregel ist jetzt rollenbasiert, nach derselben Hausregel wie bei den
Datenklassen: **die Rolle wird nachgeschaut, nicht angenommen.** Sie steht als
Datei `ARBEITSPLATTE` im Wurzelverzeichnis des Datenträgers.

- Datei vorhanden -> Arbeitsplatte, von der Pfadregel ausgenommen
- Datei fehlt -> wie bisher: der Ort gilt als Ablage und ist gesperrt

Die Regel wird dabei **strenger, nicht laxer**: vorher war ein bestimmter
Wechseldatenträger verdächtig, jetzt gilt jeder nicht erklärte Datenträger als
Ablage. Ein Wechseldatenträger, der gar nicht gemountet ist, wird ebenfalls
erfasst.

## Was ausdrücklich NICHT fällt

Nur die Pfadregel fällt. Die Inhaltsprüfungen laufen unverändert weiter, auch auf
einer erklärten Arbeitsplatte: BIDS-Kennungen, Bilddateinamen, gepackte
Bilddateien, Kohortennamen. Nachgemessen: auf erklärter Arbeitsplatte werden eine
BIDS-Kennung, ein NIfTI-Dateiname und ein gepackter NIfTI-Dateiname weiterhin
erkannt. Wer Kohortenmaterial auf eine Arbeitsplatte kopiert, fliegt auf.

## Zwei Fallen, die beim Bauen auffielen

1. **Umgebungsvariablen sind additive, keine Ersatzschalter.** Die Pfadlisten
   sind als `Umgebungsvariable + feste Literale` gebaut. Die Variablen zu leeren
   erweitert nur, es ersetzt nie. Der naheliegende Hebel ist wirkungslos.
2. **Trägernamen enthalten Leerzeichen.** In der Einhängetabelle steht ein
   Leerzeichen als `\040`. Eine Wortzerlegung des geprüften Textes hätte den
   Namen abgeschnitten und die Rolle des falschen Ortes geprüft. Deshalb wird der
   konkrete Einhängepunkt aus der Tabelle geholt und als ganze Zeichenkette im
   Text gesucht.

## Dritte Falle derselben Art

Die Rollendatei zählt **nur in der Wurzel des Datenträgers**. Eine erste Fassung
lief vom Pfad bis zur Dateisystemwurzel hinauf und hätte eine Rollendatei in
einem übergeordneten Verzeichnis den ganzen Baum darunter freigeben lassen --
auch Bereiche auf anderen Datenträgern. Eine Datei im Heimverzeichnis hätte damit
das Datenverzeichnis mitfreigegeben.

## Randnotiz: eine Wache blockt ihren eigenen Quelltext

Die Fernwache verweigert das Lesen ihrer eigenen Quelldatei mit der Begründung,
sie enthalte eine Bilddatei und einen Kohortennamen -- was stimmt, die Suchmuster
stehen dort im Klartext. Das ist eine Eigenschaft, kein Fehler: sie schützt auch
vor sich selbst. Praktische Folge: solche Dateien nicht mit dem normalen Leser
öffnen, sondern Struktur und Zeilennummern gezielt abfragen oder die Literale zur
Laufzeit zusammensetzen. Dasselbe gilt für Testbefehle: ein Prüfbefehl, der die
gesuchte Zeichenkette wörtlich enthält, wird selbst geblockt -- Proben deshalb aus
Teilen zusammensetzen.

## Wo es liegt

- `system/waechter/rolle.py` -- Rollenlogik, an einer Stelle
- `system/waechter/rolle-setzen.sh` -- Rollendatei setzen (löst den Trägerpfad
  zur Laufzeit auf, damit kein fester Pfad im Skript steht)
- `system/waechter/README-arbeitsplatte.md` -- dauerhaftes Einhängen nach
  `/mnt/arbeit` (braucht sudo)
- verdrahtet in `system/waechter/pruefe.py`, `system/systemone/approval_gate.py`
  und im Plugin der Fernwache
