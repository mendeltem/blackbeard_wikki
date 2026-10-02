---
id: computed-and-judged-must-stay-separable
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-02
herkunft: Projekt AI_Lage, Bau der Lageseite 2026-09-05
verweist_auf: [no-silent-fallback-values, first-measurement-is-not-a-change]
---

# Gerechnetes und Gemeintes müssen auseinanderzuhalten sein

## Aussage
[no-silent-fallback-values](no-silent-fallback-values.md) trennt gemessen von
gerechnet. Eine Stufe darüber liegt dieselbe Falle noch einmal: gerechnet gegen
**gemeint**. Ein Bericht, der Zahlen zeigt und sie im selben Atemzug deutet,
macht beides ununterscheidbar, sobald er älter als ein paar Tage ist.

Drei Anforderungen, die zusammen gehören:

1. **Zwei Schichten.** Die Rechenschicht ist deterministisch und jederzeit neu
   berechenbar. Die Urteilsschicht wird geschrieben, entsteht in einem eigenen
   Lauf und enthält keine Zahl, die nicht aus der Rechenschicht stammt. Beide
   sind in der Ausgabe sichtbar verschieden gekennzeichnet.
2. **Jedes Urteil trägt sein Datum und den eingefrorenen Zahlenstand**, auf den
   es sich stützt. Ein Urteil ohne beides wird nicht angezeigt.
3. **Wer urteilt, steht dabei.** Maschinell geschriebene Beschreibung und
   menschliche Einordnung sind verschiedene Felder, nicht verschiedene Sätze
   im selben Absatz.

Der Grund für Punkt 2 ist nicht Ordnungsliebe. Eine Trefferbilanz — die spätere
Auswertung, welche Einschätzung eingetroffen ist — ist genau dann wertlos, wenn
sich nicht mehr feststellen lässt, worauf die Einschätzung beruhte. Der Zahlenstand
von damals ist nicht rekonstruierbar, sobald die Quelle fortgeschrieben wurde.

## Trägt
Jede Ausgabe, die misst und deutet: Lageberichte, Statusseiten, Analysen,
Agenten, die Befunde in ein gemeinsames Gedächtnis schreiben. Auch diese Wiki:
`typ` und `status` im Kopf jedes Eintrags leisten genau das.

## Trägt nicht
Verzicht auf Deutung. Eine Seite, die nur Zahlen zeigt, verschiebt die Deutung
nur auf den Leser und zeichnet sie nirgends auf.

Auch keine Aussage über die Qualität des Urteils. Die Trennung macht ein
schlechtes Urteil nicht besser, sie macht es nur nachprüfbar.

## Bruchindikator
Ein Urteil ohne Datum oder ohne Bezug auf einen Zahlenstand. Oder: eine
Trefferbilanz, in der ein Eintrag nachträglich umformuliert oder entfernt wurde —
ab dann misst sie nicht mehr die Treffsicherheit, sondern die Nachsicht mit sich
selbst.

## Ablesung
Eigener Entwurf, Projekt AI_Lage, 2026-09-05, umgesetzt und seither in Betrieb.
Keine fremde Quelle, keine Messung — eine Konstruktionsregel, kein Befund.

## Verknüpft
- [no-silent-fallback-values](no-silent-fallback-values.md)
- [first-measurement-is-not-a-change](first-measurement-is-not-a-change.md)
