---
id: decision-model-as-profile-orchestrator
typ: pruefpunkt
status: offen
thema: knowledge/local_llm_operation
stand: 2026-10-08
herkunft: Alita, Webrecherche 2026-10-08 zu Laya 0.4.0, Jev, Arch-Router, Routing-Benchmarks; eigene Profilmessungen
verweist_auf: [laya-router-before-agent, flash-next-177b-moe-on-24gb-card, local-stack-landscape-2026-10, lean-hermes-toolsets]
---

# Entscheidungsmodell als Weiche zwischen Modellprofilen: nur zwischen RESIDENTEN Modellen

## Aussage
Ein Entscheidungsmodell (Jev von TypeSafe, offen: Laya von Convai) liefert in
30 bis 100 ms eine Wahl mit Wahrscheinlichkeit statt Text. Als Orchestrator
taugt es nur dort, wo beide Ziele gleichzeitig antworten koennen. Auf einer
24-GB-Karte sind die grossen Profile (27B dicht, 177B-MoE) exklusiv: ein
Wechsel kostet 20 bis 40 s Laden plus Verdraengung des Vorgaengers. Eine
Weiche je Anfrage zwischen diesen Profilen ist darum ein Fehlentwurf; die
Weiche gehoert zwischen das grosse residente Modell, ein kleines residentes
Nebenmodell und das Cloud-Modell.

Stand der Recherche (alles Fremdzahlen, siehe Ablesung):

| Modell | Groesse, Lizenz | Latenz | Treffer (fremd gemessen) |
|---|---|---|---|
| Laya 0.4.0 (Convai, 18.09.2026) | 322-421 Mio., Apache 2.0, CPU-faehig, 0,8-2,5 GB | 33 ms T4, ~60 ms CPU (Victus) | typed decisions 0,77 feinjustiert, **0,36 zero-shot** (Zufall 0,32); AG News 0,95; Banking77 0,43 |
| Jev (TypeSafe, API) | geschlossen, $0,042/M Token | 70-500 ms, Median 0,65 s | typed decisions 0,73; Banking77 0,87; Routing-Bench 67,8 % gegen 74,1 % der Konkurrenz; 40/40 in einem Vier-Stufen-Test |
| Arch-Router-1.5B (Katanemo) | 1,5B, generativ, HF | ~1 s | +7,7 % gegen proprietaere Modelle laut eigener Arbeit |
| Qwen2.5-3B als Klassifikator (arXiv 2604.02367) | 3B | 988 ms Median | 0,78-0,79; Luecke 6-8 Punkte zur Produktionsschwelle 0,85 |

LLMRouterBench (400k Faelle, 33 Modelle) und RouterArena (ICLR 2026) finden,
dass viele Router, auch kommerzielle, eine einfache kNN-Baseline nicht
zuverlaessig schlagen. Laya ist rund 8-mal schneller als Jev und besser
kalibriert (ECE 0,08 gegen 0,25), aber ohne Feinjustierung fast Zufall auf
typisierten Entscheidungen; die 24/30 auf Victus kamen mit nur drei Zielen.

## Traegt
- Weiche VOR dem Agenten (nicht als Tool im Agenten, siehe Victus-Befund)
  mit hoechstens drei Zielen, die ALLE sofort antworten koennen:
  `klein` (residentes Nebenmodell <= 9B), `gross` (laufendes Hauptprofil),
  `schwer` (Cloud). Schwelle p >= 0,8, darunter an `gross`.
- Das Profil `flash` (Flash-Next IQ2_XS, 6 GB VRAM) laesst neben sich ein
  kleines dichtes Modell auf der Karte zu; erst damit gibt es zwei lokale
  Ziele fuer eine Weiche. Mit dem 27B (21 GB) bleibt nur klein-CPU oder Cloud.
- Laya als Dienst (`laya-serve`, CPU, ~1,6 GB RAM): 0,1 s je Entscheidung.
  Ohne Dienst 6-7 s Modellladen je Aufruf.
- Vor jeder Einfuehrung: 60 Faelle mit Soll-Label (local_models
  `tools/laya/faelle/route.jsonl`) gegen Embedding+kNN auf demselben
  Embedding-Server (Port 8001) messen. Gewinnt kNN, braucht es kein Laya.

## Traegt nicht
- Profilwechsel je Anfrage (q4 gegen flash gegen flash-s): Ladezeit und
  Exklusivitaet der Karte machen die Weiche hier sinnlos.
- Zero-shot-Einsatz von Laya fuer feine Kategorien (Banking77 0,43). Mehr
  als drei bis vier Ziele.
- Die Konfidenz als Garantie (Victus: zwei Fehler bei 0,96/0,97).
- Dass Laya 0.4.0 auf Alita ohne weiteres laeuft: es verlangt PyTorch 2.14
  und transformers 5.x, die Umgebung `dl` hat 2.6. Eigene CPU-Umgebung noetig
  (Wheel plus 2,5 GB Gewichte ueber die Telefonleitung).

## Bruchindikator
Auf den 60 Routing-Faellen liegt Laya nicht mindestens 5 Punkte vor
Embedding+kNN, oder schwere Anfragen landen bei p >= 0,8 regelmaessig beim
kleinen Modell.

## Ablesung
Webrecherche 2026-10-08: PyPI laya 0.4.0; flowtivity.ai Laya-gegen-Jev-
Benchmark (T4, eigene Testsaetze des Autors); dev.classmethod.jp Jev-
Routing-Test (40 Faelle, nicht produktiv); arXiv 2604.02367 (SLM-Front-Door-
Routing), 2601.07206 (LLMRouterBench), 2510.00202 (RouterArena), 2506.16655
(Arch-Router). Keine der Zahlen auf Alita gemessen. Eigene Zahl: Profilwechsel
flash ueber start.sh 20 s Ladezeit, 6,1 GB VRAM bei 32k Kontext.

## Verknuepft
- [laya-router-before-agent](../findings/laya-router-before-agent.md)
- [flash-next-177b-moe-on-24gb-card](../findings/flash-next-177b-moe-on-24gb-card.md)
- [local-stack-landscape-2026-10](local-stack-landscape-2026-10.md)
- [lean-hermes-toolsets](../findings/lean-hermes-toolsets.md)
