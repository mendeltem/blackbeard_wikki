---
id: vendor-sampling-params-no-gain
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [counting-needs-thinking]
---

# Die Sampling-Empfehlung der Modellkarte bringt bei kurzen Aufgaben nichts

## Aussage
Die Qwen3.6-Modellkarte empfiehlt fuer den Instruct-Modus
`temperature=0.7, top_p=0.8, top_k=20, min_p=0.0, presence_penalty=1.5`.
Gegen strenges Sampling (`temperature=0`, keine Penalties) getestet, fuenf
mechanische Aufgaben je drei Laeufe:

| | Treffer | Reproduzierbarkeit |
|---|---|---|
| streng (`temp=0`) | 15/15 | dreimal identische Ausgabe |
| Modellkarte | 15/15 | 2-3 verschiedene Varianten je Aufgabe |

Kein Qualitaetsunterschied, aber Determinismus nur bei `temp=0`.

## Traegt
Fuer Extraktion, Klassifikation, Uebersetzung und andere formatgebundene Aufgaben
streng fahren. Reproduzierbarkeit ist dort ein Wert an sich - man kann Ausgaben
vergleichen und Regressionen erkennen.

## Traegt nicht
Lange, freie Texte. Die `presence_penalty=1.5` der Karte zielt laut Karte auf
**endlose Wiederholungen in langen Generierungen** - ein Fehlermodus, den dieser
Test mit kurzen Ausgaben gar nicht ausloest. Dort bleibt die Empfehlung plausibel
und ungeprueft. Deshalb Status `vorschlag`, nicht `getragen`.

## Bruchindikator
Wiederholungsschleifen oder Sprachmischung in laengeren Ausgaben. Dann
`presence_penalty` zwischen 0 und 2 probieren.

## Ablesung
Eigene Messung gegen die Hersteller-Modellkarte auf Hugging Face
(`Qwen/Qwen3.6-35B-A3B`, Abschnitt Best Practices), Stand 2026-08-29.
Stichprobe klein: 5 Aufgaben, 3 Laeufe, ein Modell, eine Maschine.

## Verknuepft
- [counting-needs-thinking](../findings/counting-needs-thinking.md)
