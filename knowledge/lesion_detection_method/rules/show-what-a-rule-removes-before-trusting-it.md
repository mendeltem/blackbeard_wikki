---
id: show-what-a-rule-removes-before-trusting-it
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-08
herkunft: Projekt valdo-t2s (CMB), Liquor-Regel im Schichtbetrachter 2026-10-08; uebertragen 2026-10-08
verweist_auf: [csf-rule-removes-false-alarms-without-loss, operating-points-do-not-transfer, reference-first-then-metric-then-model, false-alarms-cluster-by-anatomy]
---

# Eine anatomische Regel wird erst sichtbar gemacht, dann geglaubt: zeigen, was sie entfernt, getrennt nach Treffer und Fehlalarm

## Aussage
Eine harte Nachbearbeitungsregel ("Komponente im Liquor verwerfen") sieht in der
Summenzahl gut aus und kann trotzdem auf einer anderen Kohorte echte Laesionen
loeschen. Die Summenzahl zeigt das nicht, weil Gewinn (entfernte Fehlalarme) und
Verlust (entfernte Treffer) gegeneinander aufgerechnet werden. Darum gehoert zu jeder
Regel eine Anzeige im Betrachter, die DREI Dinge getrennt zeigt: die Karte, auf der
die Regel beruht (hier die SynthSeg-Liquorklassen als Fuellung), die Komponenten, die
sie als Fehlalarm entfernt, und die Komponenten, die sie entfernt, obwohl sie eine
Referenz beruehren. Dazu Zaehler je Schicht, je Fall und gepoolt.

Gemessen 2026-10-08 (Regel auf der rohen Vorhersage des Siegernetzes, nicht
angewendet, nur gezeigt):

| Kohorte | Faelle | Regel entfernt Fehlalarme | Regel entfernt echte Blutungen | von Treffern gesamt |
|---|---|---|---|---|
| VALDO T2* (oeffentlich) | 57 | 27 | 1 | 90 |
| eigene SWI-Kohorte | nur relativ | ja | rund 15 % der Treffer | nur relativ |
| eigene T2*-Kohorte | nur relativ | ja | rund 3 % der Treffer | nur relativ |

Auf SWI loescht die Regel jede siebte echte Blutung, auf dem eigenen T2* jede 36. Die Summenzahl der Kette hatte
das als "SWI: Klassifikator statt Regel, +0,044" verbucht; erst die Anzeige macht
sichtbar, WO das passiert (Ventrikelwand, Sulcus-naher Kortex) und ob die Karte
oder die Regel schuld ist.

## Traegt
- Jede Regel, die auf einer abgeleiteten Karte beruht (Gewebe, Atlas, Maske):
  Karte und Regelwirkung als schaltbare Ebenen in den Betrachter, bevor die Regel
  in die Kette kommt oder auf eine neue Kohorte geht.
- Die Trennung Treffer/Fehlalarm je entfernter Komponente ist die Zahl, die
  entscheidet; die Summenzahl nicht.
- Der Gewinn der Anzeige ist auch diagnostisch: liegt die entfernte Blutung in
  einem Voxelsaum der Karte, ist die Karte zu grob (Aufloesung, Resampling); liegt
  sie mitten im Label, ist die Regel falsch fuer diese Anatomie.

## Traegt nicht
- Regeln ohne Referenz auf der Zielkohorte: dort laesst sich nur der Gewinn zeigen,
  nicht der Verlust. Dann die Regel als "ungeprueft" fuehren.
- Die Anzeige ersetzt keine gepaarte Messung; sie sagt, wo man messen muss.

## Bruchindikator
Eine Kohorte, auf der die Anzeige keinen entfernten Treffer zeigt, die gepaarte
Messung aber einen Sensitivitaetsverlust durch die Regel misst (dann stimmt die
Zuordnung Komponente-Referenz im Betrachter nicht mit der Metrik ueberein).

## Ablesung
Eigene Messung; Betrachter `cmb/review/build_slice_viewer.py --csf-overlay`
(Projekt valdo-t2s), SynthSeg robust auf 1 mm, auf das Arbeitsgitter mit naechstem
Nachbarn gebracht. Eigene Kohorten nur als Summen, nie Einzelfaelle.

## Verknuepft
- [csf-rule-removes-false-alarms-without-loss](../../cmb_detection/findings/csf-rule-removes-false-alarms-without-loss.md)
- [operating-points-do-not-transfer](operating-points-do-not-transfer.md)
- [reference-first-then-metric-then-model](reference-first-then-metric-then-model.md)
- [false-alarms-cluster-by-anatomy](../mechanisms/false-alarms-cluster-by-anatomy.md)
