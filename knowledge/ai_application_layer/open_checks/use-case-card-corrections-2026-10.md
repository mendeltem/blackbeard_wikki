---
id: use-case-card-corrections-2026-10
typ: pruefpunkt
status: offen
thema: knowledge/ai_application_layer
stand: 2026-10-06
herkunft: Claude-Code-Sitzung, Ortsrecherche für ai_use_cases_overview (fünf Recherche-Agenten, 38 Karten), 2026-10-06
verweist_auf: [use-case-overview-gaps, one-mapping-file-for-linked-pages]
---

# Kartentexte in ai_use_cases_overview: veraltete oder widersprochene Angaben

## Aussage
Bei der Suche nach Einsatzorten für 38 Karten sind Quellen aufgetaucht, die Kartentexte widerlegen oder überholen. Die Karten wurden nicht geändert; die Orte stehen in `deployments.json`. Die Punkte unten sind zu prüfen und dann in der Karte (EN/DE/MN) nachzuziehen. Alle Quellen wurden von den Agenten geöffnet; Tier steht dabei.

Widerspruch zur Karte:
- [ ] **eVTOL:** "EHang fliegt kommerziell in China" stimmt nicht mehr. EHang Q1-2026-Bericht (Juni 2026): öffentliche Ticketflüge noch nicht gestartet; nach einem Absturz eines anderen Herstellers in Peking (26.6.2026) Zulassungen gestoppt, Umsatzprognose 2026 am 25.8. zurückgezogen. 1a: https://www.sec.gov/Archives/edgar/data/0001759783/000119312526262868/d123612dex991.htm
- [ ] **Autonome Schiffe:** Yara Birkeland fuhr 2024 noch mit drei Mann Besatzung, Autonomie-Test bis Anfang 2026 verlängert. 1a: https://www.yara.com/knowledge-grows/yara-birkeland-two-years-on/ . Japan (MEGURI2040) hat seit März 2026 vier Schiffe im kommerziellen Level-4-Betrieb, mehr als Norwegen: https://en.nippon-foundation.or.jp/news/articles/2026/20260327-112130.html
- [ ] **Autonome Trucks:** "zwei kommerzielle Strecken" veraltet; Aurora meldet 10 Strecken (Feb. 2026), weiter mit Beobachter im Führerhaus. Trade Press: https://www.ttnews.com/articles/aurora-earnings-q4-2025
- [ ] **Lieferdrohnen:** "2 gegen 8 Minuten" nicht in der schwedischen Studie; dort Median 3 min 14 s Vorsprung, Drohne in 67 % zuerst (Lancet Digital Health 2023). https://news.ki.se/drones-enabled-the-use-of-defibrillators-before-ambulance-arrival
- [ ] **Humanoide:** Unitree-IPO (STAR Market, Aug. 2026) brachte rund 6,1 Mrd. Yuan (~0,9 Mrd. USD), nicht "~14,7 Mrd. USD". https://news.rthk.hk/rthk/en/component/k2/1865616-20260810.htm . BMW nennt Figure 03 in Spartanburg selbst Pilot. 1a: https://www.press.bmwgroup.com/global/article/detail/T0458778EN/
- [ ] **Restaurant-Küchen:** Sweetgreen hat sich nicht zurückgezogen: 35 von 287 Filialen mit Infinite Kitchen (28.6.2026), Lizenz von Wonder, Spyce-Verkauf am 29.12.2025 abgeschlossen. 1a: https://www.sec.gov/Archives/edgar/data/0001477815/000162828026054522/sg-20260628.htm
- [ ] **Netzbetrieb/Lastprognose:** PJM/Google Tapestry zielt auf die Anschlusswarteschlange (Planung), nicht auf operative Lastprognose. https://insidelines.pjm.com/pjm-google-tapestry-join-forces-to-apply-ai-to-enhance-regional-planning
- [ ] **Energiehandel:** Die AUD ~40 Mio. bei Hornsdale sind Aurecons Schätzung entfallener FCAS-Kosten 2016/2017, keine gemessene Einsparung durch Autobidder. https://hornsdalepowerreserve.com.au/
- [ ] **Seismik:** Für "Shell mit C3 AI Seismik-Agenten" keine Quelle gefunden; Shells belegte Seismik-KI ist SparkCognition. Equinor nennt keine Entdeckung, die auf das KI-Werkzeug zurückgeht.
- [ ] **Fusion-Surrogate:** Für QLKNN-jetexp-15D war der volle JINTRAC-Lauf nur 60-100x schneller; 10^3-10^5x gilt für die Transportaufrufe. Preprint: https://arxiv.org/abs/2105.01168
- [ ] **Disruptionsvorhersage:** Der Echtzeit-Prädiktor an EAST ist ein Random Forest, kein tiefes Netz.
- [ ] **Straßenreinigung:** Belegte Straßeneinsätze sind WeRide und Autowise.ai; Gaussian Robotics ist überwiegend Innenreinigung, Trombia nur Pilot.
- [ ] **Plastik:** The Ocean Cleanup Ende 2025 kumuliert über 45 Mio. kg, nicht 50 Mio.+. https://theoceancleanup.com/updates/

Neuere Zahlen (Karte nachziehen):
- [ ] Offshore: Shell überwacht seit Verlängerung 4.6.2026 über 13 000 Anlagen mit C3 AI, nicht 10 000. Equinor Prevent: 700+ Maschinen, 24 000 Sensoren.
- [ ] Waldbrandkameras: Xcel Colorado über 130 Kameras (Karte 81); APS-Zahl "65 bis Ende 2026" nicht bestätigt (gefunden: über 30 bis Sommer 2025).
- [ ] Gehweg-Roboter: Starship zieht sich von US-Campussen zurück (Juni 2026); Serve Robotics fehlt als großer Betreiber, Nuro ist kein Gehweg-Roboter.
- [ ] Lagerroboter: Kroger und Sobeys schlossen im Jan. 2026 vier Ocado-Lager; 23 weltweit. Geek+ 81 000 Roboter.
- [ ] Straßenschäden: vialytics über 600 Kommunen in sieben Ländern (März 2025, Firmenangabe).
- [ ] Wetter: NOAA (Dez. 2025) und DWD (AICON, März 2026) betreiben KI-Modelle operativ, nicht nur ECMWF.
- [ ] Ampeln: Surtrac gehört seit 2022 Miovision.

## Trägt
Eine Liste, die man Karte für Karte abarbeiten kann. Jede Zeile hat eine Quelle.

## Trägt nicht
Die Agenten haben die Karten nur gegen die Quellen gelesen, die sie für die Orte suchten. Eine fehlende Zeile heißt nicht, dass die übrige Karte stimmt. Das Websuch-Budget der Sitzung (200) war am Ende erschöpft; autonomous-rail-yards und milking-robots blieben ohne Orte, die Wabtec-Zahl "50 Standorte" ungeprüft.

## Bruchindikator
Erledigt, wenn alle Kästchen abgehakt oder als falsch verworfen sind.

## Ablesung
Agenten-Rohdaten der Sitzung (card_notes je Karte), Quellen wie oben. Trade Press ist hier Hinweis, kein Befund.

## Verknüpft
[use-case-overview-gaps](use-case-overview-gaps.md), [one-mapping-file-for-linked-pages](../../agent_coordination/rules/one-mapping-file-for-linked-pages.md)
