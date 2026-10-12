---
id: csf-rule-on-swi-deletes-deep-lesions-synthseg-mislabels
typ: befund
status: getragen
thema: knowledge/cmb_detection
stand: 2026-10-12
herkunft: mb-arena/csf_regel_analyse.py auf den eigenen SWI- und T2*-Kohorten (ergebnisse/csf_regel/), Nutzerfrage 12.10.2026 "die CSF-Segmentation ist wohl fehlerhaft, bessere Segmentation ueber FreeSurfer?"
verweist_auf: [report-healthy-controls-separately, show-what-a-rule-removes-before-trusting-it]
---

# Die Liquor-Regel loescht auf SWI echte Blutungen TIEF im Hirn: SynthSeg verteilt auf SWI das Label "freier Liquor" falsch; FreeSurfer ist keine Option (kein T1)

## Aussage
Gemessen 12.10.2026 an allen Rohkomponenten unseres 3D-U-Nets (vor der Regel), je Komponente Mehrheitslabel aus
SynthSeg (--robust, auf dem SWI- bzw. T2*-Magnitudenbild selbst gerechnet), Abstand des Schwerpunkts zum Hirnmaskenrand und Treffer/Fehlalarm:
1. **Die geloeschten echten Blutungen liegen nicht am Rand.** Auf SWI loescht die Regel jede siebte echte Blutung; deren Abstand
   zum Hirnrand liegt im Median bei ~10 mm, nur ein Sechstel innerhalb von 3 mm. Mehrheitslabel fast immer 24 (freier Liquor),
   nicht Ventrikel. Das ist kein kortikal-subarachnoidaler Grenzfall, sondern **SynthSeg vergibt auf SWI das Label 24 im
   Hirninneren** (dunkle Gefaesse, Suszeptibilitaetsraender, Sulci-Saum werden "Liquor").
2. **Wirkung auf die Kette:** SWI gepoolt ~-0,04 F1 durch die Regel (Treffer sinken staerker als Fehlalarme), T2* ~+0,006.
   Varianten: nur Ventrikel = neutral; "tiefer Liquor" (nur Komponenten > 2/3/5 mm vom Rand loeschen) hilft NICHT (die
   geloeschten Treffer sind ja tief); **Liquor-Maske um ein Voxel erodiert, dann Mehrheitslabel** = beste Variante auf beiden
   Kohorten (SWI +0,002 gegen keine Regel, T2* +0,010; behaelt 57 von 62 bzw. 13 von 15 geloeschten Treffern und nimmt noch
   einen Teil der Fehlalarme weg). Zahlen je Variante in `mb-arena/ergebnisse/csf_regel/*_varianten.csv`.
3. **FreeSurfer (recon-all) ist keine Abhilfe:** die eigenen Kohorten haben KEIN T1 (nur SWI bzw. T2*, bei einem Teil FLAIR,
   dazu HD-BET-Hirnmaske und ROI). SynthSeg auf dem SWI/T2* ist die einzige Gewebekarte; eine bessere braeuchte ein T1
   derselben Sitzung oder eine SWI-trainierte Segmentierung.

## Traegt
Die Entscheidung ueber die Liquor-Regel auf eigenen Kohorten: auf SWI streichen oder durch die erodierte Fassung ersetzen;
auf T2* erodierte Fassung. Jede Regel, die ein Mehrheitslabel aus einer Gewebekarte benutzt, die nicht auf dieser Sequenz validiert ist.

## Traegt nicht
VALDO (dort loescht die Regel 1 Treffer, andere Bildqualitaet); den Klassifikator der zweiten Stufe (unabhaengig von der Regel).

## Bruchindikator
Ein Lauf mit erodierter Liquor-Maske, der auf SWI mehr Treffer verliert als die alte Regel; ein T1 fuer die Kohorten (dann neu messen).

## Ablesung
`mb-arena/csf_regel_analyse.py swi|t2star` (12.10.2026), Komponententabellen `ergebnisse/csf_regel/<kohorte>_komponenten.csv`.
Vereinfachung: FN wurde als Referenzzahl minus Treffer-Komponenten genaehert (zwei Komponenten auf einer Blutung zaehlen hoechstens n_cmb).

## Verknuepft
- [report-healthy-controls-separately](../rules/report-healthy-controls-separately.md)
- [show-what-a-rule-removes-before-trusting-it](../../lesion_detection_method/rules/show-what-a-rule-removes-before-trusting-it.md)
