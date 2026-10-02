---
id: one-filename-two-contracts
typ: regel
status: getragen
thema: knowledge/agent_coordination
stand: 2026-10-02
herkunft: Projekt Verbund, Datenvertrag 2026-09-05 bis 2026-09-16
verweist_auf: [parallel-sessions-same-working-tree, empty-is-not-missing]
---

# Ein Dateiname, ein Zweck

## Aussage
Sobald mehrere Projekte Daten austauschen, entsteht ein naheliegender Name —
`daten.json` — und zwei Ansprüche darauf: die Datenquelle, aus der eine Seite
sich selbst speist, und die Außenschnittstelle, über die andere sie lesen.
Solange ein Projekt allein steht, fällt das nicht auf. Sobald mehrere Agenten
dieselben Repos bauen, besetzt jeder den Namen für seinen Zweck.

Der Fall: zehn Seiten in neun Repos sollten je eine vertragskonforme
`daten.json` liefern. In drei Repos war `daten.json` zuerst die Datenquelle der
Seite; der Vertrag landete daneben in `daten-verbund.json`. Die lesende Seite
zeigte auf `daten.json`, fand dort eine gültige JSON-Datei ohne das Feld
`indikatoren` — und meldete **nichts**. Kein Fehler, kein Abbruch, nur drei
Quellen mit null Indikatoren, die aussahen wie Quellen, die eben noch nichts zu
sagen haben.

Drei Maßnahmen, zusammen:

1. **Eigener Name für die Schnittstelle.** Wer exportiert, exportiert unter
   einem Namen, den sonst niemand will.
2. **Namensraum prüfen, nicht nur Form.** Die Datei nennt, für wen sie spricht
   (`seite: "energie"`), und jeder Schlüssel trägt dieses Präfix
   (`energie.energisierte_gw`). Der Leser prüft beides gegen das, was er
   erwartet hat.
3. **Verweigern statt übernehmen.** Eine Datei, die den Vertrag verletzt, wird
   nicht eingelesen, sondern mit Grund gemeldet.

Punkt 3 ist der entscheidende: ohne ihn ist eine falsch benannte Datei von einer
leeren nicht zu unterscheiden — siehe
[empty-is-not-missing](../../agent_tooling/rules/empty-is-not-missing.md).

## Trägt
Jeden Datenaustausch zwischen Repos, die von verschiedenen Sitzungen gebaut
werden. Auch Konfigurations- und Zwischenstandsdateien: `config.json`,
`state.json`, `index.json` haben dasselbe Problem.

## Trägt nicht
Ein Projekt, das für sich steht. Dort ist `daten.json` der richtige Name, und
eine Umbenennung auf Vorrat ist Aufwand ohne Ertrag.

Auch keine Aussage über das Format. Der Vertrag kann beliebig aussehen; es geht
darum, dass er einen eigenen Namen hat und beim Lesen geprüft wird.

## Bruchindikator
Ein Leser, der bei der falschen Datei still weitermacht. Prüfprobe: dem Leser
eine bewusst falsche Datei vorlegen — sagt er nichts, prüft er nicht.

Zweiter Indikator: eine Quelle, die über Wochen null Einträge liefert, ohne dass
jemand sagen kann, ob sie leer ist oder falsch gelesen wird.

## Ablesung
Eigene Messung, Projekt AI_Lage. Am 2026-09-16 waren 3 von 10 Quellen betroffen;
das Leswerkzeug mit Vertragsprüfung meldete sie namentlich, danach 10 von 10
konform, 24 Indikatoren statt 3. Keine fremde Quelle.

## Verknüpft
- [parallel-sessions-same-working-tree](parallel-sessions-same-working-tree.md)
- [empty-is-not-missing](../../agent_tooling/rules/empty-is-not-missing.md)
