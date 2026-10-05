---
id: airport-biometric-checkin-use-case
typ: pruefpunkt
status: offen
thema: knowledge/ai_application_layer
stand: 2026-10-05
herkunft: Gespräch Projekt AI_news, 2026-10-05
verweist_auf: [value-created-is-not-value-captured, absence-of-measurement-is-not-measurement-of-absence]
---

# Flughafen: biometrischer Check-in als Use Case erfassen

## Aussage
Die Übersichtsseite [ai_use_cases_overview](https://mendeltem.github.io/ai_use_cases_overview/) (Repo mendeltem/ai_use_cases_overview, 97 Use Cases in 15 Clustern, Stand September 2026, je Karte Reifegrad, Belegqualität, Wachstum und Quelle) enthält keinen Use Case zum schnellen Check-in am Flughafen. Geprüft am 2026-10-05 per Volltextsuche im Quelltext (Flughafen, Airport, Check-in, Boarding, Biometrie, Gesichtserkennung, Passkontrolle, EasyPass/E-Gate, SITA): kein Treffer. Luftfahrt kommt nur als eVTOL-Karte und als Branchenzeile "Luftverkehr" (Flottenplanung, Crew, Wartung, Flugsicherung) vor.

## Zu prüfen
1. Was läuft in Produktion: Gesichtserkennung bei Check-in, Gepäckabgabe, Sicherheitskontrolle und Boarding; automatisierte Grenzkontrolle (E-Gates, EU Entry/Exit System). Je Fall Betreiber, Anbieter, Flughäfen, Start.
2. Kennzahl je Fall mit Herkunft: Durchlaufzeit je Passagier, Wartezeit, Passagiere je Stunde und Spur, Nutzungsquote. Herstellerangaben (Marketing) von Betreiber- und Behördenzahlen trennen.
3. Reifegrad, Belegqualität und Wachstum nach den Achsen der Übersichtsseite einstufen.
4. Einordnung in einen Cluster der Seite: Security & fraud oder Mobility & transport.
5. Karte für ai_use_cases_overview entwerfen und Mendel zur Freigabe vorlegen (Schreibzugriff auf das Repo nötig).

## Stand der Recherche 2026-10-05
Schritte 1 bis 4 erledigt, Kartenentwurf liegt vor (Cluster 9 Security & fraud, Reife prod, Beleg 3, Wachstum strong). Kernzahlen, je mit Herkunft:
- Singapur ICA: passlose automatische Spuren, ~93 Mio Abfertigungen bis 30.06.2025, im Schnitt 25 s auf 10 s, Ziel 95 % automatisiert (Behörde; Zielerreichung nicht gefunden).
- CBP: Gesichtsabgleich an allen US-Flughäfen bei internationaler Ankunft, >98 % Trefferquote (Behörde, über Presse).
- EU Entry/Exit System: seit 10.04.2026 voll in Betrieb, über 145 Mio Ein- und Ausreisen erfasst (EU-Kommission, Seite Juli 2026, über Suchauszug); Schlangen an einzelnen Übergängen nach dem Start (House of Commons Library).
- TSA/Delta Touchless ID: Gepäckabgabe bis 75 %, Sicherheitskontrolle bis 60 % schneller als PreCheck (Firmenangabe Delta), ~11 Drehkreuze, TSA-Ausbau auf 65 Flughäfen 2026.
- Hamad Doha mit Qatar Airways und SITA: über 700 biometrische Kontaktpunkte (SITA, Juli 2026).
- SITA IT Insights 2025: biometrische Grenzkontrolle an 54 % der Flughäfen (Branchenumfrage; zählt Flughäfen, nicht Passagiere).
Offen: Anteil der Passagiere, die tatsächlich biometrisch abgefertigt werden; mongolische Übersetzung; Schreibzugriff auf ai_use_cases_overview.

## Trägt nicht
Noch keine Aussage über Verbreitung oder Wirkung. Dass der Fall auf der Seite fehlt, sagt nichts über seine Größe.

## Bruchindikator
Die Karte ist auf der Seite eingetragen, dann wird dieser Prüfpunkt geschlossen.

## Ablesung
Volltextsuche im Repo mendeltem/ai_use_cases_overview, Stand des Klons 2026-10-05. Inhalte des Use Case noch blind.

## Verknüpft
- [value-created-is-not-value-captured](../rules/value-created-is-not-value-captured.md)
- [absence-of-measurement-is-not-measurement-of-absence](../rules/absence-of-measurement-is-not-measurement-of-absence.md)
