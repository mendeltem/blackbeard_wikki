---
id: abundant-bad-compute-scarce-good
typ: mechanismus
status: vorschlag
thema: knowledge/china_industrial_strategy
stand: 2026-10-02
herkunft: Projekt ki-anwendungsschicht, Gespräch 2026-09-20
verweist_auf: [bandwidth-bottleneck, energy-advantage-is-connection-speed, absence-of-measurement-is-not-measurement-of-absence]
---

# Reichlich schlechte Rechenleistung, knappe gute

## Aussage
Zwei scheinbar widersprüchliche Befunde aus demselben Monat: Bis zu 80 Prozent neu gebauter chinesischer Rechenkapazität stehen ungenutzt (Lokalpresse, zitiert bei ASPI); der SMIC-Chef nennt die Nutzung der Kapazität „nicht zu Ende gedacht". Zugleich setzte Moonshot für Kimi K3 (2,8 Billionen Parameter, offene Gewichte) 48 Stunden nach dem Start Neuanmeldungen aus, weil der GPU-Verbund an der Grenze war (Caixin, TechNode, Juli 2026); DeepSeek begrenzt gleichzeitige Verbindungen (500 für V4 Pro, 2.500 für Flash) und verzögert unter Last, statt abzulehnen.

Auflösung: Der Leerstand besteht überwiegend aus aktueller Ware (Nvidia H20, Huawei Ascend), verteilt auf Anlagen mit je einigen hundert bis tausend Karten, ohne Hochleistungsvernetzung, ohne Ablaufsteuerung, ohne Betrieb, der Ausfälle wegsteckt; Käufer waren Kommunen und Firmen ohne Netz- und Betriebskompetenz; das Huawei-Ökosystem gilt als „benutzbar, nicht gut benutzbar" mit drei bis fünf Jahren Übergang (ChinaTalk). Ein Modell dieser Größe auszuliefern ist speicherbandbreitenbegrenzt, die Gewichte müssen im Verbund liegen; HBM ist genau die sanktionierte Stufe. Nationaler Bestand und bedienbare Kapazität sind zwei Größen.

## Trägt
Dass Ausfuhrkontrollen die Dauerlast (Auslieferung) härter treffen als den einmaligen Kraftakt (Training). Chinesische Instanz des Axioms [Bandbreiten-Engpass](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md). Und ein Motiv mit Datum für Rechenzeitanmietung im Ausland. Inferenz ist gegenüber schlechter Vernetzung toleranter als Training: Ein Teil des Leerstands wird für kleine dichte Modelle nahe bei Nutzern nutzbar, wenn die Last vom Training zur Auslieferung kippt; nicht der Teil in den westlichen Provinzen (Latenz).

## Trägt nicht
Eine Auslastungszahl. Expertenmodelle (MoE) senken die Rechenlast je Token, nicht den Speicherbedarf; der Nutzen kleiner Modelle auf verstreuter Hardware gilt für dichte Modelle. „Ausverkauft" ist auch eine Geschäftsentscheidung.

## Bruchindikator
Chinesische Labore heben Anmeldestopps auf, ohne dass die inländische HBM-Versorgung sich ändert: Kapazität woanders gefunden.

## Ablesung
ASPI (Denkfabrik), ChinaTalk (Newsletter), Caixin (Wirtschaftspresse), Herstelleraussagen. Kein Tier 1a.

## Verknüpft
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
- [energy-advantage-is-connection-speed](energy-advantage-is-connection-speed.md)
- [absence-of-measurement-is-not-measurement-of-absence](../../ai_application_layer/rules/absence-of-measurement-is-not-measurement-of-absence.md)
