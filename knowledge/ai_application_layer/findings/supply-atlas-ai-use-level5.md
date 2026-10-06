---
id: supply-atlas-ai-use-level5
typ: befund
status: vorschlag
thema: knowledge/ai_application_layer
stand: 2026-10-06
herkunft: Claude-Code-Sitzung, Webrecherche mit sechs Agenten, 2026-10-06
verweist_auf: [operator-evidence-is-not-site-evidence, supply-atlas-ai-use-level4, absence-of-measurement-is-not-measurement-of-absence]
---

# KI-Einsatz an den 128 wichtigsten Standorten des Supply Atlas

## Aussage
Alle 128 Standorte der höchsten Stufe (lv 5) im
[Supply Atlas](https://mendeltem.github.io/Supply_Atlas3D/) wurden auf
dokumentierten KI-Einsatz geprüft. Maßstab: maschinelles Lernen, Bildverarbeitung,
autonome Fahrzeuge/Bohrer, KI-Wartung oder KI-Prozessoptimierung. Automatisierung
oder „Smart Factory“ ohne ausdrückliche KI-/ML-Angabe zählt nicht.

| Klasse | Anzahl | Bedeutung |
|---|---|---|
| site | 42 | KI am Standort selbst belegt |
| operator | 39 | KI beim Betreiber belegt, nicht für diesen Standort |
| none | 27 | kein öffentlicher Beleg gefunden |
| infra | 13 | Standort ist selbst KI-Infrastruktur (Rechenzentren) |
| open | 3 | nicht geprüft (Suchbudget erschöpft): Vindhyachal, Surgut-2, Gansu Jiuquan |
| na | 4 | Meerengen, kein Betreiber |

Muster: Am häufigsten belegt sind KI-Hochöfen (POSCO, Baowu), autonome
Minenflotten (Pilbara, Nevada, Bayan Obo), chinesische Containerterminals
(Yangshan, Qingdao, Ningbo) und WEF-Lighthouse-Werke (CATL, ASE). Bei Chip- und
Speicherfabriken belegen TSMC, Samsung, SK hynix und Micron KI fast nur auf
Konzernebene, nicht je Fab.

Ergebnis steht je Standort im Atlas (Feld `AI_USE`, Tooltip, Detailfenster mit Quelle,
Schalter „KI-Einsatz hervorheben“).

## Trägt
- Aussagen der Form „an Standort X ist KI dokumentiert“ für die 42 site-Fälle, jeweils mit Quelle im Atlas.
- Die Beobachtung, dass Konzernmeldungen selten einen Standort nennen.

## Trägt nicht
- Dass an den 27 none-Standorten keine KI läuft (siehe absence-of-measurement-is-not-measurement-of-absence).
- Einen Anteil für die ganze Industrie: nur lv 5, nicht zufällig gezogen.
- Schwache site-Fälle als gleichwertig: Weda Bay (nur Werbetext), Baotou (nur Newsletter), Hyundai Ulsan (angekündigt), Cigar Lake (Prototyp), Port Hedland (KI nur beim Schlepperbetreiber).

## Bruchindikator
Eine Nachprüfung findet bei mehr als jedem fünften site-Fall keine standortbezogene Quelle.

## Ablesung
Überwiegend Trade Press, Firmenpressemitteilungen, WEF-Lighthouse-Seiten und
chinesische Staatsmedien; kaum Tier 1a. Je Standort ein Satz und eine URL in
`Supply_Atlas3D/index.html` (`const AI_USE`). Recherche mit Websuche,
Stand 2026-10-06. SMIC Shanghai von site auf none gestuft (einzige Quelle 2007, kein ML).

## Verknüpft
[operator-evidence-is-not-site-evidence](../rules/operator-evidence-is-not-site-evidence.md),
[supply-atlas-ai-use-level4](../open_checks/supply-atlas-ai-use-level4.md),
[absence-of-measurement-is-not-measurement-of-absence](../rules/absence-of-measurement-is-not-measurement-of-absence.md)
