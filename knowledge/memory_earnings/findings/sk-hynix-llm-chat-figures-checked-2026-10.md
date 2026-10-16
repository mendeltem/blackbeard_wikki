---
id: sk-hynix-llm-chat-figures-checked-2026-10
typ: befund
status: vorschlag
thema: knowledge/memory_earnings
stand: 2026-10-16
herkunft: Chat with Mendel (Claude Code, cloud session), 2026-10-16; check of a Gemini chat transcript on SK Hynix (sk_hynix_analyse.pdf, 23 pages, 2026-10-16) presented by Mendel
verweist_auf: [sk-hynix-q2-2026-oneoff-and-tax, operating-margin-three-makers, low-pe-at-earnings-peak, hbm-gb-per-mw-three-generations, hbm-eats-wafer-area, rubin-shipments-start-q3-fy27, demand-is-not-earnings, older-hbm-hardware-holds-value, second-source-hbm4-arrives-presold]
---

# SK Hynix figures from an LLM chat (Gemini, 2026-10-16): reported numbers hold, the derived ones mix units

## Statement
Mendel presented a Gemini chat on SK Hynix trend, earnings, valuation and HBM demand. The chat cites no sources.
Its reported figures match SK Hynix's own releases. Its derived figures (growth series, multiple, per-GPU memory,
rack size) mix metrics, exchange rates or units and should not be reused as they stand.

**Reported figures (hold):**

| Chat says | Reported | Verdict |
|---|---|---|
| FY2025 revenue 97.15 T KRW, net 42.92 T KRW, OP ~33 bn USD | revenue 97.1467 T, OP 47.2063 T, net 42.9479 T KRW (release 2026-01-28) | holds; 33 bn USD implies ~1,430 KRW/USD |
| Q1 2026 net 40.35 T KRW | revenue 52.5763 T, OP 37.6103 T (71.5 %), net 40.3459 T KRW (release 2026-04-23) | holds, but see growth series |
| Q2 2026 revenue >79 T KRW, OP 60.54 T KRW, margin 76 % | 79.3187 T, 60.5426 T, 76.3 % (see sk-hynix-q2-2026-oneoff-and-tax) | holds |
| TTM revenue >126 bn USD | 24.45 + 32.83 + 52.58 + 79.32 = 189.2 T KRW = 141.8 bn USD at 1,334 KRW/USD | holds (loose) |

Cross-check: Q3 2025 to Q2 2026 OP, 11.3834 + 19.1696 + 37.6103 + 60.5426 = 128.7 T KRW, equals the trailing
OP already used in operating-margin-three-makers.

**Derived figures (do not reuse as stated):**

1. *Growth series mixes metrics and FX.* The chat's series "Q1 ~27 bn USD, Q2 44.8 bn USD, Q3e 54.8 bn USD" puts
   Q1 **net** profit next to Q2 **operating** profit. Q1 is converted at ~1,483 KRW/USD (40.35 / 27.2), Q2 at ~1,351
   (60.54 / 44.8). Like for like, operating profit at one rate (1,334 KRW/USD): Q1 28.2 bn USD, Q2 45.4 bn USD,
   **+61 %** QoQ (in KRW: 37.61 to 60.54 T).
2. *"P/E below 6" is not a P/E.* It is market cap 1,050 bn USD / (Q2 OP × 4 = 179 bn USD) = 5.9: pre-tax operating
   profit of the record quarter, annualised. With the derived recurring conversion OP × 0.765
   (sk-hynix-q2-2026-oneoff-and-tax) it is 1,050 / 137 = **7.7**, which is the "forward P/E on annualised quarter"
   case in low-pe-at-earnings-peak. The adjusted trailing P/E in operating-margin-three-makers is ~13
   (price 2026-09-18).
3. *Market cap 1,050 bn USD (October 2026)* is not checked here. At 709,854,891 shares and 1,334 KRW/USD it needs a
   price of ~1,973,000 KRW; on 2026-09-18 (1,838,000 KRW) the market cap was 1,304.7 T KRW = 978 bn USD.
4. *"Rubin up to 288 GB HBM4, +50 % memory per GPU"* compares with B200 (192 GB). B300 has shipped with 288 GB since
   2025, so per GPU the step is 0 %, and per MW −22 % (hbm-gb-per-mw-three-generations).
5. *"NVL576: 576 GPUs instead of 72 in NVL72"* compares GPU dies with packages. Nvidia counts dies from Rubin on;
   Rubin Ultra NVL576 is 144 packages of 4 dies. Like for like it is 144 vs 72 packages, ×2, not ×8.
6. *"HBM die needs 2 to 3 times the wafer area of DDR5"* is below the wiki's ~3× (HBM3E) and ~4× (HBM4) per bit
   (hbm-eats-wafer-area).
7. *"Nvidia Rubin output 2026/27 about 200,000 to 300,000 GPUs"* has no source and looks low: Nvidia guided Rubin at
   ~20 % of Q3 FY27 data-centre revenue, ~20 bn USD in one quarter (rubin-shipments-start-q3-fy27). 300,000 units in
   that one quarter alone would need an average price above ~67,000 USD per GPU; 200,000 above 100,000 USD.
   Assumption-based, no unit count is reported.
8. *"Full-year EBITDA margin ~56 %"* contradicts H1 2026: operating margin alone was 74.4 % (98.15 / 131.90 T KRW),
   and EBITDA margin is at least the operating margin. It would need a collapse in H2. Likely a stale estimate.
9. *Q3 2026 date "28 October"*: consistent with the wiki's 27.10. SK hynix's 6-K of 2026-10-14 puts the call
   materials on the IR site on 28 October Seoul time; US calendars list 27 October after close.

**Not checkable or not admissible:** Q3 2026 consensus OP 74.1 T KRW (consensus is not a source here), S&P outlook
raised to positive, "HBM for 2026 and much of 2027 sold out and allocated". On the last point: SK hynix said on an
investor call in February 2026 that all 2026 HBM is sold out (company statement, read via press); for 2027 there are
only press reports citing industry sources and the CEO's July 2026 remark that 2027 will be the tightest supply year
(Reuters, via press). Not Tier 1a for 2027.

**Scenario arithmetic (correct, premise carries everything):** +15 % OP per quarter from ~55 bn USD gives
63.2 / 72.7 / 83.6 / 96.2 / 110.6 bn USD (Q4 2026 to Q4 2027), 363 bn USD for 2027, run-rate 442 bn USD,
×0.765 = 339 bn USD net. Every number follows from three assumptions: the Q3 consensus as start, a constant +15 %
per quarter, a constant 76 % margin.

**What the scenario requires (added 2026-10-16, same chat):** 110 bn USD per quarter at 1,334 KRW/USD is 146.7 T KRW,
×2.42 on Q2 2026 OP. At 76 % margin, revenue must go from 79.3 to 193.1 T KRW per quarter, ×2.43 in six quarters.
Bit growth is an assumption (SK Hynix does not guide it this way): at 20 % per year, six quarters give ×1.31, so
price and mix per bit must rise ×1.85; at 30 % per year ×1.48 and ×1.64. For comparison, revenue rose ×3.6 from
Q2 2025 to Q2 2026, so the step is not without precedent; it needs the 2026 price jump to repeat, not just hold.
Part of it comes from HBM3E to HBM4 (reported asking price ~4 against ~1.50 USD/Gb, see
second-source-hbm4-arrives-presold). Assuming HBM per bit ×2.2 and an HBM revenue share of 40 % (50 %), conventional
DRAM price/mix must still rise ×1.62 (×1.50) at 20 % bit growth, or ×1.27 (×1.08) at 30 %. The HBM share of
revenue is not reported; both shares are assumptions. If conventional DRAM prices stay flat in 2027 and bit growth
stays near 20 %, the scenario fails even with HBM4 doubling.

## Carries
Which numbers from that chat can be reused: the reported quarterly and annual figures (with the reported values
above). Which cannot: the USD growth series, the "P/E below 6", the per-GPU memory step and the NVL576 comparison.
Rule of thumb for KRW figures: one exchange rate for a whole series, stated with date.

## Does not carry
A view on whether SK Hynix is cheap or expensive, or on the scenario's likelihood. The chat's qualitative arguments
(bandwidth bottleneck, HBM wafer intensity, Nvidia's annual cadence, Jevons) are already in the wiki with sources
(ai_demand_drivers, memory_supply); this entry adds nothing to them. The chat's claims about used GPUs and
workstation prices are handled in older-hbm-hardware-holds-value.

## Break indicator
The Q3 2026 report (27/28 October 2026) restates Q1 or Q2 2026 figures, or the 6-K gives a different date.

## Source
- SK hynix FY2025 release 2026-01-28 (Tier 1a, read via Digitimes and StorageNewsletter): https://www.digitimes.com/news/a20260128PR200.html, https://www.storagenewsletter.com/2026/02/10/sk-hynix-fiscal-4q25-and-fy25-financial-results/
- SK hynix 1Q26 release 2026-04-23 (Tier 1a, PR Newswire copy via Barchart): https://www.barchart.com/story/news/1462801/sk-hynix-announces-1q26-financial-results
- Q2 2026, trailing OP, share count and price: existing wiki entries (linked).
- Q3 2025 revenue 24.4489 T and OP 11.3834 T KRW: SK hynix release 2025-10-29, from memory, not re-read; the OP matches the wiki's trailing sum to the digit.
- Q3 date: SK hynix Form 6-K 2026-10-14 (Tier 1a, via search snippet; sec.gov not reachable from this environment): https://www.sec.gov/Archives/edgar/data/0002120882/000119312526420934/d413172d6k.htm
- FX: ~1,334 KRW/USD on 2026-10-12 (30rates.com, not an official source); EUR/USD 1.1188 on 2026-10-13 (Banque de France): https://www.banque-france.fr/en/statistics/rates-and-prices/exchange-rates-daily-parities-2026-10-13
- HBM sold-out statements: Asia Economy 2025-10-29 on the Q3 2025 call, https://view.asiae.co.kr/en/article/2025102910334843684 ; press summaries of the February 2026 call and July 2026 CEO remarks (trade press, not a finding).
- Nvidia die counting (NVL144/NVL576): GTC 2025 keynote, general knowledge, not re-read (Tier 1b).
- The chat itself: LLM output without sources, lowest tier. Not stored in the wiki (it also contains personal details).

## Linked
- [sk-hynix-q2-2026-oneoff-and-tax](sk-hynix-q2-2026-oneoff-and-tax.md)
- [operating-margin-three-makers](operating-margin-three-makers.md)
- [low-pe-at-earnings-peak](../risks/low-pe-at-earnings-peak.md)
- [hbm-gb-per-mw-three-generations](../../ai_demand_drivers/findings/hbm-gb-per-mw-three-generations.md)
- [hbm-eats-wafer-area](../../memory_supply/mechanisms/hbm-eats-wafer-area.md)
- [rubin-shipments-start-q3-fy27](../../ai_demand_drivers/findings/rubin-shipments-start-q3-fy27.md)
- [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)
- [older-hbm-hardware-holds-value](../../ai_demand_drivers/mechanisms/older-hbm-hardware-holds-value.md)
- [second-source-hbm4-arrives-presold](../../memory_supply/mechanisms/second-source-hbm4-arrives-presold.md)
