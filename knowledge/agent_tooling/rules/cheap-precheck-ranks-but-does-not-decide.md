---
id: cheap-precheck-ranks-but-does-not-decide
typ: regel
status: vorschlag
thema: knowledge/agent_tooling
stand: 2026-10-07
herkunft: Claude-Code-Sitzung Alita, Aufsicht ueber einen lokalen Agenten (WMH-Linie), 2026-09-14 bis 2026-09-23
verweist_auf: [first-n-of-a-sorted-list-is-a-block]
---

# Eine billige Vorpruefung ordnet und beschreibt, sie entscheidet nicht

## Aussage
Aus einer 3-Minuten-CPU-Messung (Spanne des mittleren Laesionskontrasts zwischen Kohorten)
eine Rangliste von sieben Intensitaetsskalen gebaut, daraus GPU-Laeufe eingereiht und andere
ausgeschlossen. Der eingereihte Falsifikationstest fiel negativ aus: Rang 1 war ueberall
gesichert schlechter, Rang 7 ueberall neutral. Das Werkzeug beschrieb die Bildstatistik richtig
und schloss trotzdem falsch auf die Netzleistung -- das Netz sieht den Kontrast JE FALL zur
Umgebung, nicht das Kohortenmittel. Zwei "Bestaetigungen" (Robustheitsprobe, Obergrenze) hatten
das Muster allgemein erscheinen lassen.

Regel: eine Vorpruefung darf Laeufe ordnen, nicht ausschliessen, bis sie ihren eigenen
Falsifikationstest bestanden hat. Die Vorhersage VOR dem Lauf aufschreiben, damit das
Scheitern sichtbar wird -- hier hat genau das funktioniert.

## Traegt
Jede Heuristik, die GPU-Stunden sparen soll, indem sie Kandidaten vorab aussortiert.

## Traegt nicht
Vorpruefungen, deren Zusammenhang mit der Zielgroesse bereits an Laeufen gemessen ist.

## Bruchindikator
---

## Ablesung
Vorfall 2026-09-23 bis 2026-09-28. Tier 1a.

## Verknuepft
- [first-n-of-a-sorted-list-is-a-block](first-n-of-a-sorted-list-is-a-block.md)
- [two-seeds-per-decision-below-0.08](../../cmb_detection/rules/two-seeds-per-decision-below-0.08.md)
