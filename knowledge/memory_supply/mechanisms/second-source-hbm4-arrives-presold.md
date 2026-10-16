---
id: second-source-hbm4-arrives-presold
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-16
herkunft: Chat with Mendel (Claude Code, cloud session), 2026-10-16; thesis Mendel
verweist_auf: [fab-lead-time-examples, gpu-memory-absorbs-fab-additions, hbm-market-share-and-nvidia-allocation, no-standard-cycle-without-absorption-check, asml-memory-share-of-litho-2026, sk-hynix-llm-chat-figures-checked-2026-10, low-pe-at-earnings-peak, demand-is-not-earnings, hbm-contract-prices-2027, rubin-hbm-capacity-technology-or-scarcity]
---

# Second-source HBM4 arrives slowly and pre-sold, so it does not press 2027 prices

## Statement
Thesis Mendel (2026-10-16): "Samsung and Micron cannot suddenly conjure that much HBM4; it simply takes too long."

Chain:

    second-source HBM4 volume limited by yield and customer qualification, not by DRAM wafers
    back-end lines (TSV, stacking, test) take about 12 to 18 months, greenfield fabs 4 to 5 years
    what does arrive is contracted a year ahead -> no uncommitted surplus in 2027
    -> the "second source erodes SK Hynix's HBM margin" route does not work in 2027

Samsung's bottleneck is not wafers (largest DRAM capacity of the three) but HBM yield and Nvidia qualification.
All three were certified for Rubin HBM4 in June 2026 (hbm-market-share-and-nvidia-allocation); certification is not
volume.

Indicators (trade press and local reports, not a finding):
- TrendForce, 2026-08-25: HBM prices potentially up to +50 % in 2027; Nvidia reportedly plans server price increases of more than 15 % in early 2027, which strengthens the memory makers in negotiations.
- Samsung reportedly asks about 4 USD per Gb for HBM4 against about 1.50 USD for HBM3E (×2.7 per bit) and has secured a large share of its 2027 orders; price talks reported as in the final stage (2026-10-06).
- Micron reportedly contracted most of its 2027 HBM volume at higher prices; SK Hynix still negotiating (German trade press).
- Nvidia HBM4 allocation (analysts): SK Hynix mid-50s to two thirds, Samsung mid-20s, Micron about 20 %.

## Carries
For 2027: margin erosion at SK Hynix through second-source HBM4 is unlikely; while all three are sold out the
pricing power stays with the suppliers. Judgment (Claude, 2026-10-16): probability that SK Hynix's operating margin
falls below 60 % in at least one quarter of 2027 about 20 % (before this point ~30 %). The remaining route is
conventional DRAM: the 2026 tool wave at ASML (asml-memory-share-of-litho-2026) turns into wafers in 2027/28.

Second consequence: the HBM3E to HBM4 transition supplies part of the price/mix increase that the +15 %-per-quarter
scenario needs (calculation in sk-hynix-llm-chat-figures-checked-2026-10). Judgment: probability of a 440 bn USD
operating-profit run rate by Q4 2027 about 10 % (before ~5 %).

## Does not carry
2028 and later. From mid-2027 the 2028 contracts are negotiated; by then Samsung's yields, convertible wafer
capacity and new fabs (Yongin from 2027, Micron New York and Idaho) can shift the balance. Market share: with three
certified suppliers, SK Hynix's share can fall even if the price does not. Asking prices are not contract prices.
Earnings: price per bit is the variable that matters, see demand-is-not-earnings; volume statements alone do not
carry it.

## Break indicator
Reported 2027 HBM4 contract prices per bit at or below 2026 HBM3E levels; or Samsung's share of Nvidia HBM4 above
about 35 % for 2027; or 2028 contract prices per Gb flat or falling against 2027.

## Source
Thesis: Mendel, 2026-10-16 (chat). Indicators, trade press, not re-read at the original:
- TrendForce, 2026-08-25: https://www.trendforce.com/news/2026/08/25/news-nvidias-reported-15-server-hike-boosts-samsung-sk-hynix-with-hbm-prices-potentially-up-50-in-2027/
- Samsung HBM4 price talks, 2026-10-06 (local reports via SamMobile-fans): https://sammyfans.com/2026/10/06/samsung-hbm4-price-talks-enter-final-stage
- Micron 2027 HBM volume contracted: https://www.it-daily.net/?p=189921
- Korea Herald on 2027 HBM terms: https://www.koreaherald.com/article/10895833
- Back-end lead time 12 to 18 months: general knowledge, no source; fab lead times: fab-lead-time-examples.
Primary readings: hbm-contract-prices-2027.

## Linked
- [fab-lead-time-examples](../findings/fab-lead-time-examples.md)
- [gpu-memory-absorbs-fab-additions](gpu-memory-absorbs-fab-additions.md)
- [hbm-market-share-and-nvidia-allocation](../open_checks/hbm-market-share-and-nvidia-allocation.md)
- [no-standard-cycle-without-absorption-check](../rules/no-standard-cycle-without-absorption-check.md)
- [asml-memory-share-of-litho-2026](../findings/asml-memory-share-of-litho-2026.md)
- [sk-hynix-llm-chat-figures-checked-2026-10](../../memory_earnings/findings/sk-hynix-llm-chat-figures-checked-2026-10.md)
- [low-pe-at-earnings-peak](../../memory_earnings/risks/low-pe-at-earnings-peak.md)
- [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)
- [hbm-contract-prices-2027](../open_checks/hbm-contract-prices-2027.md)
- [rubin-hbm-capacity-technology-or-scarcity](../open_checks/rubin-hbm-capacity-technology-or-scarcity.md)
