---
id: model-cost-falls-faster-than-hardware
typ: mechanismus
status: getragen
thema: knowledge/model_capability_cost
stand: 2026-10-02
herkunft: Projekt ai_modellkurve, Datenstand 2026-09-05
verweist_auf: [iso-capability-cost-halving, two-paths-to-cheaper-capability]
---

# Die Modellkostenkurve fällt schneller als die Hardwarekurve

## Aussage
Hardwareseite: dichter KI-Durchsatz je GPU 1,0× für A100 (2020) gegen 48× für GB300 (2025). Rechnerisch eine Verdopplung etwa alle zehn Monate.
Modellseite: Preis je Mio. Ausgabetoken beim billigsten Modell eines festen Fähigkeitsniveaus halbiert sich alle 1,6 bis 7,3 Monate.

Die Modellkurve fällt also um den Faktor 1,4 bis 6 schneller. Das ist kein Widerspruch: in sie gehen neben der Hardware auch Architektur, Destillation, Quantisierung, Auslastung und Anbietermarge ein.

## Trägt
Die Warnung an jede Rechnung, die Kosten je Aufgabe aus einer Chip- oder Fertigungskurve fortschreibt. Wer das tut, unterschätzt den Preisverfall auf der Modellebene systematisch — und damit auch, wie schnell eine Anwendung wirtschaftlich wird.
Umgekehrt für die Erlösseite: wer Inferenzerlöse je Fähigkeitseinheit aus der Hardwarekurve ableitet, überschätzt sie.

## Trägt nicht
Eine Kausalaussage. Es sind zwei getrennt gemessene Kurven, nicht eine Zerlegung. Welcher Anteil des Modellvorsprungs aus Architektur, welcher aus Marge stammt, ist aus Preisen nicht zu trennen ([two-paths-to-cheaper-capability](two-paths-to-cheaper-capability.md)).
Die Hardwarezahl ist eine Spitzenangabe des Herstellers für das jeweils beste Zahlenformat, kein gemessener Durchsatz unter Last.

## Bruchindikator
Die Modellkurve nähert sich der Hardwarekurve an oder fällt darunter. Dann ist der Architekturvorsprung ausgereizt, und die Kosten je Fähigkeit hängen wieder allein am Silizium. Für die 2025 erreichten Niveaus ist das 2026 bereits der Fall.

## Ablesung
Hardwarezahlen: Schwesterseite nvidia-roadmap, Herstellerangaben Tier 1b, https://mendeltem.github.io/nvidia-roadmap/. Die Verdopplungszeit ist daraus gerechnet, nicht dort ausgewiesen.
Modellzahlen: siehe [iso-capability-cost-halving](../findings/iso-capability-cost-halving.md), Stand 2026-09-05.

## Verknüpft
- [iso-capability-cost-halving](../findings/iso-capability-cost-halving.md)
- [two-paths-to-cheaper-capability](two-paths-to-cheaper-capability.md)
