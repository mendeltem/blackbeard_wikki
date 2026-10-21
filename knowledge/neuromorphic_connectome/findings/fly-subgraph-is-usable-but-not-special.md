---
id: fly-subgraph-is-usable-but-not-special
typ: befund
status: getragen
thema: knowledge/neuromorphic_connectome
stand: 2026-10-21
herkunft: Cle-Arbeit, Reservoir/SNN-Linie, 21.10.2026
verweist_auf: [fly-connectome-topology-carries-no-advantage]
---

# Das Fliegen-Subgraph ist ein brauchbares Substrat, aber nichts Besonderes

## Aussage
`fly783.csr` (138.639 Neuronen, 15.091.983 Kanten, Besetzung 0,08 %) laesst
sich auf einer einzelnen 24-GB-Karte als rekurrentes Netz betreiben. Tragfaehig
gemessener Betriebspunkt: LIF mit Surrogate-Gradient, `in_scale = 10,0`,
spektraler Radius 0,9, Feuerrate ~0,12, keine stillen und keine
Dauerfeuer-Neuronen.

Der Nutzen liegt in der **Verfuegbarkeit**, nicht in der Struktur: man kann
echte Konnektom-Sparsity und -Groesse mit einer Methode konfrontieren, ohne
Zugriff auf nicht-oeffentliche Daten. Fuer die eigentliche Frage — traegt die
Verdrahtung? — siehe
[fly-connectome-topology-carries-no-advantage](fly-connectome-topology-carries-no-advantage.md):
nein, unter keiner der vier geprueften Lernregeln.

Wichtige Nebenbeobachtung: `fly783.csr` hat **keine anatomischen
3D-Koordinaten**. Wer raeumliche Aussagen (Hemisphaere, Region, Hirnhaelfte)
braucht, kommt damit nicht weiter und braucht den FlyWire-Atlas bzw. die
Rohdaten — ein anderer Zugriffsweg als diese Datei.

## Traegt
Die Entscheidung, das Konnektom als *Testumgebung* fuer Methoden zu nutzen
(Sparsity, Ereignisrechnung, lokale Lernregeln), ohne daraus einen
Leistungsanspruch abzuleiten. Und als Warnung, wenn jemand "FlyWire" als
Qualitaetsmerkmal statt als Datenherkunft liest.

## Traegt nicht
Keine Leistungsaussage. Keine anatomische Aussage. Keine Aussage ueber
vollstaendige Konnektome (diese Datei ist ein Subgraph-Auszug).

## Bruchindikator
Ein Lauf, in dem `fly783.csr` etwas liefert, das kein anderer Graph gleicher
Dichte liefert. Bisher auf keiner Achse beobachtet.

## Ablesung
Eigene Messung, 21.10.2026, Cle-Arbeit, `reservoir_fly/fly_reservoir.py` und
`snn_fly.py`, `tune_gain.py` fuer den Betriebspunkt. FSDD oeffentlich,
`fly783.csr` aus oeffentlicher Quelle.

## Verknuepft
- [fly-connectome-topology-carries-no-advantage](fly-connectome-topology-carries-no-advantage.md)
