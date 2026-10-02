---
id: counting-needs-thinking
typ: befund
status: getragen
thema: knowledge/local_llm_operation
stand: 2026-08-29
herkunft: Projekt local_models, Victus, 2026-08-29
verweist_auf: [rule-lists-make-small-models-refuse, vendor-sampling-params-no-gain]
---

# Zaehlen braucht Thinking, und kostet das Zwanzigfache

## Aussage
Qwen3.6-35B-A3B scheitert ohne Thinking zuverlaessig an Aufgaben mit Laengen,
Anzahlen oder Positionen - und zwar **plausibel aussehend**.

Aufgabe: Regex fuer deutsche IBANs. Drei Anlaeufe ohne Thinking, drei verschiedene
falsche Antworten (26 Ziffern, 29 Ziffern, einmal ganz ohne Laenderkennung). Mit
Thinking beim ersten Anlauf korrekt:

```
DE\d{2}(?:\s?\d{4}){4}\s?\d{2}
```

Gegengeprueft: matcht `DE89 3704 0044 0532 0130 00` mit und ohne Leerzeichen,
verwirft eine zu kurze und eine franzoesische IBAN.

| | Ergebnis | Zeit | Token |
|---|---|---|---|
| ohne Thinking | falsch | 4,7 s | 64 |
| mit Thinking | korrekt | 92,7 s | 2582 |

## Traegt
Thinking als Vorgabe **pro Aufgabentyp** setzen, nicht global. Alles mit Laengen,
Anzahlen oder Positionen bekommt es, der Rest nicht.

## Traegt nicht
Dass Thinking allgemein bessere Ergebnisse liefert. Bei Umformulieren, Uebersetzen
und Klassifikation brachte es nichts und kostete die zwanzigfache Wartezeit.

## Bruchindikator
Ein Ergebnis, das richtig aussieht und bei der Gegenprobe durchfaellt. Das ist der
teure Fehlermodus - nicht offensichtlicher Unsinn, sondern etwas, das man pruefen
muss. Jede Zaehl-Ausgabe gehoert maschinell gegengeprueft, egal welcher Modus.

## Ablesung
Eigene Messung, llama.cpp b10603, `chat_template_kwargs: {"enable_thinking": ...}`.
Gegenprobe der Regex per Skript gegen vier Beispiele.

## Verknuepft
- [rule-lists-make-small-models-refuse](../findings/rule-lists-make-small-models-refuse.md)
- [vendor-sampling-params-no-gain](../findings/vendor-sampling-params-no-gain.md)
