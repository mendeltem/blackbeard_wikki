---
id: reference-first-then-metric-then-model
typ: regel
status: getragen
thema: knowledge/lesion_detection_method
stand: 2026-10-07
herkunft: Projekte valdo-t2s (CMB) und wmhseg (WMH), 2026-09 bis 2026-10; uebertragen 2026-10-07
verweist_auf: [two-seeds-per-decision-below-0.08, official-label-2-rule-deletes-the-prediction, measure-tails-paired-not-by-percentile]
---

# Erst die Referenz, dann das Mass, dann das Modell

## Aussage
1. **Referenz.** Ohne von Hand gezeichnete oder von Hand bestaetigte Referenz gibt es keine
   ehrliche Zahl. Ausgaben einer Pipeline sind keine Wahrheit, auch nicht die "beste" von
   elf Einstellungen. Vor dem ersten Modell klaeren: Wer hat was gezeichnet, nach welcher
   Regel, mit welcher Uebereinstimmung zwischen Befundern? VALDO berichtet keine
   Inter-Rater-Zahl; deshalb ist auf CMB offen, wie nah 0,65 F1 an der Etikett-Decke liegt
   (Expertenurteil ueber 201 Kandidaten eingeplant, nicht gemessen).
   Gibt es keine Referenz: eine kleine Stichprobe (20 bis 30 Faelle, zufaellig, nicht die
   ersten N) von Hand bewerten lassen, bevor irgendetwas optimiert wird.
2. **Mass.** Zaehlbare Laesionen misst man je Instanz (Laesions-F1, Treffer bei Ueberlappung
   oder Abstand), gepaart ueber Faelle mit 95-%-Bootstrap-Intervall; Dice allein belohnt
   grosse Laesionen und uebersieht Zaehlfehler. Die Auswerteregel der Referenz (z. B.
   Challenge-Code loescht die Vorhersage auf Label 2) wortgetreu uebernehmen; eine eigene,
   strengere Konvention war 0,006 Dice zu tief. Perzentile der Verteilung bei n = 30 sind
   Rauschen.
3. **Modell.** Erst wenn 1 und 2 stehen. Vorher aufschreiben: Entscheidungsregel,
   Erwartung, Hauptmass.

## Traegt
Jede neue Laesionslinie, besonders solche, die mit "fertigen Pipeline-Ausgaben" beginnt.

## Traegt nicht
Reine Volumetrie grosser Strukturen, dort ist Dice das richtige Mass.

## Bruchindikator
Eine Linie, in der Pipeline-Ausgaben nachtraeglich als Referenz ausreichten (gemessene
Uebereinstimmung mit Handzeichnung ueber dem Rauschboden der Modelle).

## Ablesung
Eigene Erfahrung aus beiden Linien. Metrikwahl: Maier-Hein et al., Metrics reloaded,
Nat Methods 2024, doi:10.1038/s41592-023-02151-z (Tier 1b).

## Verknuepft
- [two-seeds-per-decision-below-0.08](../../cmb_detection/rules/two-seeds-per-decision-below-0.08.md)
- [official-label-2-rule-deletes-the-prediction](../../wmh_segmentation/findings/official-label-2-rule-deletes-the-prediction.md)
- [measure-tails-paired-not-by-percentile](../../wmh_segmentation/rules/measure-tails-paired-not-by-percentile.md)
