---
id: buyback-leverage-at-low-pe
typ: mechanismus
status: getragen
thema: knowledge/memory_earnings
stand: 2026-10-02
herkunft: Gespraech Projekt NVIDIA-Roadmap, 2026-09
verweist_auf: [sk-hynix-shareholder-return-policy, sk-hynix-adr-issuance-2026, low-pe-at-earnings-peak]
---

# Rueckkaufhebel bei niedrigem KGV

## Aussage
Die Wirkung eines Rueckkaufs auf den Gewinn je Aktie haengt am Kehrwert des KGV, nicht an der absoluten Summe:

    Anteil zurueckgekaufter Aktien r = Ausschuettungsquote x Gewinnrendite = Ausschuettungsquote / KGV
    EPS-Wachstum = (1 + Gewinnwachstum) / (1 - r) - 1

Dieselbe Ausschuettungsquote wirkt bei KGV 5 rund viermal so stark wie bei KGV 21. Beispiel: halber Gewinn in Rueckkaeufe, KGV 5,3 ergibt r = 9,4 Prozent und damit plus 10,4 Prozent EPS allein aus der Aktienzahl; KGV 21 ergibt r = 2,3 Prozent und plus 2,4 Prozent.

Drei Bedingungen, damit die Rechnung gilt:
1. Die Aktien werden eingezogen, nicht als eigene Aktien gehalten.
2. Gezahlt wird aus freiem Cashflow, nicht aus dem Gewinn. Bei hohem Investitionsbedarf ist der ausschuettbare Betrag kleiner als der Gewinn.
3. Keine gegenlaeufige Emission, siehe [sk-hynix-adr-issuance-2026](../findings/sk-hynix-adr-issuance-2026.md).

## Traegt
Die Rechnung ist eine Identitaet und gilt unabhaengig von der Firma. Sie erklaert, warum eine Ausschuettungspolitik, die am FCF-Anteil haengt, bei niedrigem KGV stark auf den EPS wirkt.

## Traegt nicht
Keine Aussage ueber den Kurs. Steigt der Kurs, kauft dieselbe Summe weniger Aktien, der Effekt bremst sich selbst. Ein niedriges KGV ist zudem oft die Erwartung fallender Gewinne, siehe [low-pe-at-earnings-peak](../risks/low-pe-at-earnings-peak.md); faellt der Gewinn, war der Rueckkauf teuer bezogen auf den spaeteren Gewinn.

## Bruchindikator
Aktienzahl im Abschluss sinkt langsamer als Rueckkauf minus Emission. Dann werden Aktien gehalten statt eingezogen, oder es gibt Mitarbeiterprogramme in relevanter Groesse.

## Ablesung
Reine Arithmetik. Eingangsgroessen (Ausschuettungsquote, FCF, Aktienzahl) aus Abschluss und Policy, Tier 1a.

## Verknuepft
- [sk-hynix-shareholder-return-policy](../findings/sk-hynix-shareholder-return-policy.md)
- [sk-hynix-adr-issuance-2026](../findings/sk-hynix-adr-issuance-2026.md)
- [low-pe-at-earnings-peak](../risks/low-pe-at-earnings-peak.md)
