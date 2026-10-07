---
id: use-case-places-second-pass
typ: pruefpunkt
status: offen
thema: knowledge/ai_application_layer
stand: 2026-10-07
herkunft: Claude-Code-Sitzung, Ortsrecherche Restkarten (acht Recherche-Agenten, 98 Karten), 2026-10-07
verweist_auf: [use-case-card-corrections-2026-10, one-mapping-file-for-linked-pages]
---

# Einsatzorte: zweiter Durchgang und neue Kartenhinweise

## Aussage
Am 2026-10-07 haben 68 weitere Karten in ai_use_cases_overview Orte bekommen (247 Orte, Commit 4b614a3); damit zeigen 113 von 143 Karten ihren Globus (489 Orte). Das Websuch-Budget der Sitzung (200 Suchen, geteilt von acht Agenten) war früh erschöpft. Viele Orte stammen danach aus PubMed oder aus Kundenseiten der Anbieter, die über bekannte Adressen geöffnet wurden. Jede Quelle wurde geöffnet.

Offen, ohne Orte (30 Karten):
- [ ] Nicht recherchiert, weil das Budget fehlte: co-packaged-optics-cpo, 800-vdc-rack-power, lidar-for-physical-ai, edge-ai-perception-chips, ai-in-chip-design-eda, agentic-chip-verification-eda, 5g-connectivity-for-robotics, foundation-models-for-robotics, world-models-3d-generation, supply-chain-event-data-gs1-epcis-2-0, machine-to-machine-language-opc-ua
- [ ] Gesucht, kein Ort mit Quelle: logistics-orchestration, mine-ordnance-clearance (nur Länderebene), revenue-cycle-prior-authorization, catena-x-automotive-data-space (Erfolgsgeschichten ohne Werk), eu-digital-battery-passport (Kandidat Volvo Ridgeville), electronic-bill-of-lading-ebl (nur Qingdao 2023), vehicle-to-everything-radio-c-v2x, satellite-direct-to-device-link, video-avatar-generation, ai-smart-glasses, 3d-print-failure-detection, ai-language-learning, offline-coding-website-building, local-fine-tuning-of-open-models, distributed-inference-across-local-machines, decentralized-training-on-contributed-gpus
- [ ] Bewusst ohne Orte, weil reine Software-Protokolle: agent-to-agent-protocol-a2a, model-context-protocol-mcp, agent-payments-ap2-acp
- [ ] Dünn (1–2 Orte): facade-window-cleaning-robots, robot-vacuums, local-image-generation, local-image-editing-design, local-3d-scanning-with-gaussian-splatting, generative-3d-models, be-my-ai, defense-isr-drones, space-robotics

Neue Hinweise zu Kartentexten (eingearbeitet 2026-10-07, ai_use_cases_overview 672994a; Quellen beim Einarbeiten selbst geöffnet):
- [x] **Präzisionsspritzen:** Deere meldet über 10 Mio. Acres See & Spray Select in Australien, 74 % weniger Herbizid (Aug. 2026). https://www.heavyquipmag.com/2026/08/19/john-deere-see-and-spray-select-10-million-acres-australia/
- [x] **Aquakultur:** "langsame Verbreitung" überholt: fast 3.000 Stingray-Laser in rund 25 % der norwegischen Fischfarmen (Dez. 2025); Mowi von 80 auf 250 Geräte. https://scanmagazine.co.uk/beyond-the-net-stingrays-high-tech-approach-to-revolutionising-fish-farming-december-2025/ . XpertSea heißt jetzt KAMPI.
- [x] **Exoskelette:** German Bionics aktuelles System heißt EXIA, nicht Apogee. https://germanbionic.com/news/human-centric-robotics-takes-off-supporting-the-people-who-keep-airports-moving
- [x] **KI-Wirkstoffsuche:** Rentosertib Phase III: erster Patient im September 2026 dosiert (Karte: "Juli 2026"); Karte nennt jetzt Start Juli, erster Patient 10.9.2026. 1a: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
- [x] **VR-Schmerztherapie:** Unabhängige NIH-finanzierte Studie (Cedars-Sinai, n=385, npj Digital Medicine Feb. 2026): VR nicht besser als Schein-VR im Primärendpunkt; Karte nennt die Evidenz "ungewöhnlich sauber". https://doi.org/10.1038/s41746-026-02437-4
- [x] **Dentalroboter:** Klinische Literatur 2025–2026 wird von chinesischen autonomen Implantatrobotern dominiert; Karte nennt nur Yomi. https://doi.org/10.1111/jopr.70076
- [x] **Katastrophen-Frühwarnung:** FireSat ist im Orbit (Start 7.7.2026, erste Feuerbilder 16.9.2026). https://earthfirealliance.org/news-article/earth-fire-alliance-and-muon-space-release-first-light-and-first-active-fire-images-from-operational-firesat-constellation/
- [x] **Weltraumrobotik:** MEV-1 seit Mai 2025 am dritten Kunden; Mission Robotic Vehicle mit drei Pods am 21.7.2026 gestartet. https://www.northropgrumman.com/space/space-logistics-services
- [x] **Maschinelle Übersetzung:** DeepL streicht im Mai 2026 rund 25 % der Stellen; Karte nennt "stetiges starkes Wachstum". https://finance.yahoo.com/sectors/technology/articles/deepl-cut-25-workforce-ai-182445900.html
- [x] **Gaussian Splatting:** "HKU" ist die Kunsthochschule Utrecht, nicht die Universität Hongkong.

## Trägt
Die 247 Orte sind mit Quelle eingetragen; verbund_pruefen.py meldet "in Ordnung", Board und Atlas zeigen sie in EN/DE/MN (Browsertest 2026-10-07).

## Trägt nicht
Mehrere Quellen sind Anbieterseiten ohne Datum (Feld yr dann leer); Städte sind teils nur Hauptsitz des Anwenders, Koordinaten teils Stadtmitte. Kein Ort ist gegen eine zweite unabhängige Quelle geprüft. Be-My-Eyes-Orte sind Dienste mit geschultem Personal, nicht Freiwilligen.

## Bruchindikator
Erledigt, wenn jede offene Karte Orte hat oder als ortlos begründet ist und jeder Kartenhinweis eingearbeitet oder verworfen ist.

## Ablesung
Agenten-Rohdaten (orte3/*.jsonl mit notes je Karte), Quellen wie oben.

## Verknüpft
[use-case-card-corrections-2026-10](use-case-card-corrections-2026-10.md), [one-mapping-file-for-linked-pages](../../agent_coordination/rules/one-mapping-file-for-linked-pages.md)
