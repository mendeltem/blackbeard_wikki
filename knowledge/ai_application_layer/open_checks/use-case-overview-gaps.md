---
id: use-case-overview-gaps
typ: pruefpunkt
status: offen
thema: knowledge/ai_application_layer
stand: 2026-10-05
herkunft: Gespräch Projekt AI_news, 2026-10-05
verweist_auf: [airport-biometric-checkin-use-case]
---

# Lücken in ai_use_cases_overview: Kandidatenliste

## Aussage
Der Flughafen-Check-in fehlte in der Übersichtsseite (siehe [airport-biometric-checkin-use-case](airport-biometric-checkin-use-case.md)). Ein sparsamer Erstdurchlauf am 2026-10-05 hat 30 bekannte, produktiv laufende KI-Anwendungen per Stichwortsuche gegen die Karten der Seite (Block `const UC`) gehalten, ohne Webrecherche. Kandidaten ohne Treffer in den Karten:

Ohne jeden Treffer: Kreditscoring/Underwriting, Hörgeräte mit KI, Smartphone-Fotografie (Computational Photography), Tutoring und adaptives Lernen, Liefer-Dispatch (Essenslieferung, Paketrouten), Briefsortierung mit Handschrifterkennung, kassenloser Handel (Just Walk Out).

Nur in der Lückenliste oder einem Nebensatz, ohne eigene Karte: Flugsicherung, Kennzeichenerkennung und Maut, Barrierefreiheit (Be My Eyes u. a.), Content-Moderation.

Treffer möglicherweise zufällig, Karte prüfen: Hafenautomation ("port" kann "support" sein), Gleisinspektion ("track" kann "tracking" sein).

## Zu prüfen
1. Samstag (viel Token-Budget): je Kandidat Webrecherche nach dem Muster des Flughafen-Falls, also Produktion ja/nein, Kennzahl mit Herkunft, Behörde gegen Firmenangabe, Einstufung Reife/Beleg/Wachstum.
2. Weitere Kandidaten systematisch sammeln: Lückenliste der Seite (Branchen ohne Karte) Branche für Branche gegen bekannte Produktivfälle halten.
3. Die zwei möglicherweise zufälligen Treffer gegen die Kartentexte lesen.
4. Je bestätigter Lücke Kartenentwurf an Mendel, gesammelt eintragen (Schreibzugriff auf ai_use_cases_overview nötig).

## Trägt nicht
Dass die Kandidaten groß sind oder auf die Seite gehören. Die Liste stammt aus allgemeinem Wissen, ohne Quellen, und die Stichwortsuche kann Karten unter anderem Namen übersehen.

## Bruchindikator
Alle Kandidaten sind geprüft und eingetragen oder begründet verworfen.

## Ablesung
Lokale Stichwortsuche im Repo mendeltem/ai_use_cases_overview, Stand des Klons 2026-10-05. Inhalte blind.

## Verknüpft
- [airport-biometric-checkin-use-case](airport-biometric-checkin-use-case.md)
