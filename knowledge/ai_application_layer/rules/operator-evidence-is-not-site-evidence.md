---
id: operator-evidence-is-not-site-evidence
typ: regel
status: vorschlag
thema: knowledge/ai_application_layer
stand: 2026-10-06
herkunft: Claude-Code-Sitzung, KI-Prüfung Supply Atlas, 2026-10-06
verweist_auf: [supply-atlas-ai-use-level5, absence-of-measurement-is-not-measurement-of-absence]
---

# Konzernbeleg ist kein Standortbeleg

## Aussage
„Samsung nutzt KI in seinen Fabs“ belegt nicht, dass KI in Samsung Xi'an läuft.
Ein Beleg auf Konzernebene wird nie stillschweigend auf einzelne Werke übertragen,
sondern getrennt geführt: `site` (Quelle nennt den Standort) gegen `operator`
(Quelle nennt nur den Konzern oder ein anderes Werk).

In der Prüfung der 128 Atlas-Standorte war das die häufigste Verwechslung:
39 von 128 Fällen sind nur auf Konzernebene belegt, darunter alle großen
Speicher- und Logikfabs. Oft nennt die Quelle ausdrücklich ein *anderes* Werk
(LONGi Jiaxing statt Ordos, Tongwei Meishan statt Leshan, Tesla Nevada statt Shanghai).

## Trägt
- Getrennte Zählung in Übersichten und Karten.
- Verknüpfungen zwischen Use Cases und Standorten nur über `site`-Fälle (so umgesetzt in deployments.json).

## Trägt nicht
- Den Umkehrschluss, an operator-Standorten liefe keine KI.

## Bruchindikator
Ein Konzern veröffentlicht eine Werksliste mit KI-Anwendungen je Standort; dann lassen sich operator-Fälle direkt nachziehen.

## Ablesung
Eigene Auswertung, siehe supply-atlas-ai-use-level5.

## Verknüpft
[supply-atlas-ai-use-level5](../findings/supply-atlas-ai-use-level5.md),
[absence-of-measurement-is-not-measurement-of-absence](absence-of-measurement-is-not-measurement-of-absence.md)
