---
id: pharma-runs-closed-frontier-llms
typ: befund
status: vorschlag
thema: knowledge/ai_application_layer
stand: 2026-10-14
herkunft: Projekt Artificial Intelligence (claude.ai), Gespräch 2026-10-14
verweist_auf: [pharma-share-of-ai-compute, value-created-is-not-value-captured]
---

# Pharma betreibt geschlossene Frontier-LLMs, nicht nur offene Modelle hinter der Firewall

## Aussage
Die verbreitete Behauptung, Pharma nutze Text-LLMs wegen Patentschutz ausschließlich als selbst gehostete Open-Source-Modelle oder in isolierten VPCs, ist falsch.

- Novo Nordisk betreibt NovoScribe auf Basis von Claude produktiv. Laut Anthropic-Fallstudie dauert ein Entwurf eines klinischen Studienberichts etwa zehn Minuten statt über zehn Wochen. Die Schreibzeit sinkt um 90 Prozent, der Aufwand für Geräteprotokolle um 95 Prozent.
- Am 16.09.2026 kündigten Novo Nordisk und Anthropic eine breitere F&E-Kooperation an: Frontier-Modelle, Pilotprojekte mit Claude Science, KI-gestützte Softwareentwicklung. Finanzdaten und Ergebniszahlen fehlen.

Gültig bleibt der andere Teil der Behauptung: Pharma trainiert Text-LLMs praktisch nicht selbst vor, Fine-Tuning auf eigenen Daten kommt vor. Die oft genannten „Bio-LLMs“ ESM und MoLFormer stammen nicht aus der Pharma. ESM-2 kommt von Meta (Lin et al., Science 2023, DOI 10.1126/science.ade2574), MoLFormer von IBM (Ross et al., Nature Machine Intelligence 2022, DOI 10.1038/s42256-022-00580-7). Beide DOIs wurden nicht erneut geöffnet.

## Trägt
Dass die Anwendungsschicht in der Pharma zuerst im Papierkram produktiv wird (regulatorische Dokumente), nicht in der Molekülentdeckung. Dass Inferenz-Nachfrage aus Pharma über die Frontier-Anbieter läuft und dort mitgezählt wird, nicht als eigene Pharma-Flotte.

## Trägt nicht
Die Effizienzzahlen. Sie stammen aus einer Herstellerfallstudie und sind nicht unabhängig gemessen. Die Pressemitteilung vom 16.09.2026 nennt keine Zahlen. Ein Fall belegt keine Branchenquote.

## Bruchindikator
Novo Nordisk oder Anthropic ziehen den Einsatz zurück, oder eine Aufsichtsbehörde (EMA, FDA) schränkt LLM-erstellte Studienberichte ein.

## Ablesung
Pressemitteilung Novo Nordisk/Anthropic 16.09.2026 (Tier 1a, Firmenmitteilung): https://via.ritzau.dk/files/90446/15165610/540810/en
Anthropic-Fallstudie Novo Nordisk (Herstellerangabe, Zahlen wiedergegeben nach Unite.AI, Fachpresse, kein Befund für sich): https://unite.ai/novo-nordisk-taps-anthropics-claude-to-speed-drug-discovery

## Verknüpft
- [pharma-share-of-ai-compute](pharma-share-of-ai-compute.md)
- [value-created-is-not-value-captured](../rules/value-created-is-not-value-captured.md)
