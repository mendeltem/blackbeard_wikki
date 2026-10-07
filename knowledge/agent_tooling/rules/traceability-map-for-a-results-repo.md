---
id: traceability-map-for-a-results-repo
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Repo cmb-valdo-chain (docs/TRACEABILITY.md), 2026-10-07
verweist_auf: []
---

# Ein Ergebnis-Repo braucht EINE Karte: Zahl -> Daten -> Befehl -> Datei -> Abschnitt

## Aussage
Wenn ein Repository Zahlen berichtet (README-Tabelle), reicht es nicht, dass Laborbuch, Befehlsliste und
Literaturliste existieren. Es braucht eine Seite, die sie verbindet, mit vier Tabellen:
1. **Daten**: Herkunft (Zitat, DOI), Lizenz, was davon benutzt wird (Split, Seed), wo es auf der Maschine liegt.
2. **Code und Methode**: je Baustein die Quelle (Paper, Original-Commit oder eigene Messung), die Datei im Repo
   und der Abschnitt, in dem die Abweichung oder Messung steht.
3. **Der Weg**: je Schritt der Kette Eingabe, Befehl, Ausgabe, was er belegt, wo es steht; am besten aus der
   Schrittliste des Laufwerkzeugs abgeleitet (hier `kern.py STEPS` mit done-check je Schritt).
4. **Jede berichtete Zahl**: Daten, Befehl, Ergebnisdatei, Entscheidungsabschnitt; dazu die Bewertungsregeln,
   die fuer alle Zahlen gelten.
Dazu: was automatisch protokolliert wird (meta.json je Lauf, Warteschlangenlog, Umgebung, Pruefsummen) und
die bekannten Luecken, ungeschoent. Literatur traegt je Eintrag ein Flag (an der Quelle geprueft / aus Notiz / aus
dem Gedaechtnis), damit niemand Ungeprueftes zitiert.

## Traegt
Jedes Repo, das Zahlen fuer ein Paper oder eine Abschlussarbeit liefert, auch mit privaten Daten (dann nur Summen
und Pfade, nie Bilder).

## Traegt nicht
Reine Werkzeug-Repos ohne berichtete Ergebnisse.

## Bruchindikator
Eine Zahl im README, die nicht in einer Zeile der vierten Tabelle steht.

## Ablesung
Nutzeranforderung 07.10. ("alle Wege und Quellen nachvollziehbar"); Vorlage `docs/TRACEABILITY.md` in
cmb-valdo-chain. Setzung, kein Messwert.

## Verknuepft
--
