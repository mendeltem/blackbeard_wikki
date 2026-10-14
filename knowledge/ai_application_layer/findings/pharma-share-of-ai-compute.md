---
id: pharma-share-of-ai-compute
typ: befund
status: vorschlag
thema: knowledge/ai_application_layer
stand: 2026-10-14
herkunft: Projekt Artificial Intelligence (claude.ai), Gespräch 2026-10-14
verweist_auf: [compute-allocation-by-sector, pharma-runs-closed-frontier-llms, value-created-is-not-value-captured, announced-is-not-built]
---

# Pharma-Anteil am KI-Compute: eher 0,2 bis 1 Prozent, nicht 3 bis 8

## Aussage
Zwei Texte, die Mendel am 2026-10-14 vorlegte (eine LLM-Zusammenfassung und ein „Strategie-Dossier“), setzen Pharma und Life Sciences bei 3 bis 6 bzw. 5 bis 8 Prozent des weltweiten Enterprise- und Inferenz-Compute an. Keiner der beiden nennt eine Quelle. Eine Größenrechnung gegen die belegten Flotten spricht für 0,2 bis 1 Prozent.

Belegte Flotten (Tier 1a):
- Roche: 2.176 Blackwell on-prem zugebaut, gesamt über 3.500 GPUs inklusive Cloud, nach eigener Angabe die größte angekündigte Flotte der Branche (Roche, 16.03.2026).
- Lilly: DGX SuperPOD mit über 1.000 B300 (Lilly IR, 28.10.2025).
- Gefion, Kopenhagen, 1.528 H100: gehört der Danish Centre for AI Innovation (Novo Nordisk Foundation und Staatsfonds EIFO), nicht Novo Nordisk. Novo Nordisk ist einer der Nutzer (DCAI, 2024).

Rechnung:
- Hyperscaler-Capex 2026 rund 690 Mrd. USD, etwa 590 Mrd. Euro (Projekt-Report „Four-Layer Compute Stack“, Sekundärsynthese). 3 Prozent davon sind rund 18 Mrd. Euro pro Jahr.
- Top-20-Pharma, großzügige Annahme: 20.000 GPUs zu rund 45.000 Euro je GPU mit System ergibt rund 0,9 Mrd. Euro, kumuliert über mehrere Jahre.
- Selbst mit dem Faktor 5 für Cloud-Nutzung und Biotechs (Isomorphic, Recursion, Xaira) bleibt der Abstand zu 18 Mrd. Euro im Jahr etwa eine Größenordnung.
- 18 Mrd. Euro entsprächen rund 7 Prozent des globalen Pharma-F&E-Budgets von etwa 260 Mrd. Euro (Annahme, allgemeines Wissen).

## Trägt
Dass Pharma ein sichtbarer, wachsender Käufer mit hohem Signalwert ist (regulierte, konservative Branche kauft eigene Hardware), mengenmäßig aber kein Nachfragetreiber für HBM oder CoWoS. Deckt sich mit der Größenprüfung auf der Karte „Pharma in-house AI factories“ im Use-Case-Board (unter 0,1 Prozent der Hyperscaler-Capex für Roche plus Lilly).

## Trägt nicht
Eine Punktzahl. Die 20.000 GPUs der Top 20, der Cloud-Faktor 5 und der Stückpreis sind Annahmen. Der Nenner ist nicht dasselbe wie „Enterprise-Compute“: Klammert man Hyperscaler-Eigenbedarf und Frontier-Labore aus, steigt der Anteil. Dann ist es aber eine andere Aussage, und die vorgelegten Texte definieren ihren Nenner nicht.

## Bruchindikator
Ein Pharmakonzern oder eine Biotech meldet eine Flotte über 20.000 GPUs, oder ein Cloud-Anbieter weist Life-Sciences-Umsatz mit KI-Rechenzeit über 5 Mrd. Dollar pro Jahr aus. Dann die Rechnung neu aufsetzen.

## Ablesung
Roche-Medienmitteilung 16.03.2026 (Tier 1a): https://www.roche.com/media/releases/med-cor-2026-03-16
Lilly IR 28.10.2025 (Tier 1a): https://investor.lilly.com/node/53176
DCAI zu Gefion (Tier 1a, Betreiber): https://dcai.dk/news/denmark-s-first-ai-supercomputer-is-now-operational
Capex-Nenner: Projekt-Report, Sekundärsynthese, nicht nachgerechnet. Stückpreis, Flottengröße Top 20, Cloud-Faktor: Annahmen.

## Verknüpft
- [compute-allocation-by-sector](../open_checks/compute-allocation-by-sector.md)
- [pharma-runs-closed-frontier-llms](pharma-runs-closed-frontier-llms.md)
- [value-created-is-not-value-captured](../rules/value-created-is-not-value-captured.md)
- [announced-is-not-built](../../compute_bottlenecks/rules/announced-is-not-built.md)
