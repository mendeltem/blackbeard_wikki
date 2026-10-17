---
id: gb300-ramp-timing-and-rubin-handover
typ: befund
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-17
herkunft: Chat with Mendel (claude.ai project "Artificial Intelligence"), 2026-10-17
verweist_auf: [rubin-shipments-start-q3-fy27, rubin-share-of-blackwell-base, cadence-and-yield-trough]
---

# GB300 ramp timing and the Rubin handover

## Statement
When B300/GB300 volume rose, read from filings and ODM data, and when Rubin takes over.

Reported (Tier 1a, Nvidia releases and calls; fiscal quarters mapped to calendar months):
- Q2 FY26 (May to Jul 2025): GB300 production shipments started; Blackwell Ultra "tens of billions" of revenue;
  inventory 11 -> 15 bn USD to support the ramp.
- Q3 FY26 (Aug to Oct 2025): GB300 crossed GB200, about two thirds of Blackwell revenue. Data center 51.2 bn,
  networking 8.2 bn.
- Q4 FY26 (Nov 2025 to Jan 2026): data center 62.3 bn, networking 11 bn, "Blackwell Ultra ramp".
- Q1 FY27 (Feb to Apr 2026): DC compute 60.4 bn, networking 14.8 bn, growth from "Blackwell 300 products".
- Q2 FY27 (May to Jul 2026): data center 89.0 bn, driven by Blackwell Ultra; networking +138 % YoY.
- Q3 FY27 guide (Aug to Oct 2026): revenue 108 bn, Vera Rubin about 20 % of data center revenue.

Supply chain lag (trade press and broker notes): HBM3E 12-Hi (the B300 stack) shipped from Q4 2024 (SK hynix call,
Tier 1a). Quanta GB300 trial production late Q3 2025, mass production Q4 2025; Morgan Stanley (Nov 2025) GB300 rack
assembly started, 14 to 15k GB racks in Q4 2025 after 8 to 8.5k in Q3; Quanta: GB300 replaced GB200 as main line in
early 2026. Chain: HBM -> Nvidia revenue -> ODM racks, roughly one quarter per step.

Estimate of GB300 revenue (Claude; compute = DC minus networking, Hopper about 2 bn in Q3 FY26; GB300 share of
Blackwell after Q3 FY26 is an assumption of 75 to 90 %):

    Q2 FY26 ~10 (lower bound of "tens of billions")
    Q3 FY26 ~27  (43.0 compute - 2 Hopper = 41 x 2/3)
    Q4 FY26 ~40  (51.3 x 75-85 %)
    Q1 FY27 ~52  (60.4 x 85-90 %)
    Q2 FY27 ~63  (89.0 - ~17.3 networking = 71.7 x 85-90 %)
    Q3 FY27 ~51  (guide-derived: ~100 DC - 20 Rubin - ~20 networking, then 85 %)

At a 65 % GB300 share the peak would be about 47 instead of 63 bn; the shape stays.

Rubin handover: Nvidia guides first Vera Rubin shipments Q3 2026, volume ramp Q4 2026, growth through H1 2027.
Jefferies: Rubin about 12 % of GPU revenue in Q3 FY27, above 40 % in Q4 FY27, possibly the largest contributor in
Q1 FY28. Rough: DC ~115 bn in Q4 FY27 (assumption +15 % QoQ), compute ~93, >40 % -> above 37 bn Rubin. Racks in data
centres one to two quarters later, Feb to Apr 2027, possibly shorter (Rubin compute tray assembly about 5 instead of
about 120 minutes, per analysts). Probability (Claude) that Rubin is at least 35 % of compute revenue in Q4 FY27:
about 70 %.

TrendForce (April 2026): Blackwell over 70 % of Nvidia high-end GPU shipments in 2026, led by GB300/B300; Rubin cut
from 29 to 22 % because of HBM4 qualification and other delays.

## Carries
Timing: Nvidia's GB300 revenue inflected in Aug to Oct 2025, ODM rack volume in Q4 2025 to Q1 2026; GB300 revenue
peaked around May to Jul 2026; Rubin's revenue ramp is Nov 2026 to Jan 2027.

## Does not carry
GB300 dollar figures after Q3 FY26: Nvidia does not split them, these are estimates. Not unit counts. Rack timing
rests on one cycle of lag.

## Break indicator
- Nvidia's Q3 FY27 report (around 2026-11-19) guides Rubin clearly below about 35 % of compute for Q4 FY27.
- ODM monthly revenue (Foxconn, Quanta, Wistron, around the 10th of each month) shows GB300 rack volume rising into
  2027: GB300 plateau longer than assumed.
- Further HBM4 or thermal-lid delays (KeyBanc July 2026, KYEC guidance cut) push Rubin volume into 2027.

## Source
- Nvidia Q4 FY26 release, SEC 8-K (Tier 1a): https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm
- Nvidia Q2 FY26 investor presentation (Tier 1a): https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/NVDA-F2Q26-Quarterly-Presentation-FINAL.pdf
- Nvidia Q3 FY26 call summary: https://vectorshift.ai/research/companies/nvidia/earnings/2026-q3-summary
- Nvidia Q1 FY27 release (via HPCwire): https://www.hpcwire.com/off-the-wire/nvidia-announces-financial-results-for-1st-quarter-fiscal-2027/
- Nvidia Q2 FY27 (via StorageNewsletter, Nasdaq/Zacks): https://www.storagenewsletter.com/2026/08/27/nvidia-fiscal-2q27-financial-results/ , https://www.nasdaq.com/articles/nvidia-q2-earnings-beat-blackwell-ultra-data-center-strength
- SK hynix Q4 2024 call (Tier 1a): https://seekingalpha.com/article/4771229-sk-hynix-inc-hxscf-q4-2024-earnings-call-transcript
- Quanta GB300 timing (Digitimes): https://www.digitimes.com/tag/shipment/0011846.html
- Morgan Stanley rack counts (TechNews): https://technews.tw/?p=1465078
- Quanta Q1 2026 (TVBS): https://news.tvbs.com.tw/english/3177453
- TrendForce April 2026: https://www.trendforce.com/presscenter/news/20260408-13003.html
- Rubin timeline: https://www.digitalcitizen.life/nvidia-confirms-vera-rubin-launch-for-q3-as-blackwell-demand-keeps-climbing/
- Jefferies Rubin share (via Tiger Brokers): https://www.itiger.com/news/1100856992
- KeyBanc delay, KYEC (broker via press): https://invezz.com/nz/news/2026/07/15/tsmc-stock-braces-for-record-earnings-but-this-nvidia-risk-could-derail-the-rally/ , https://longportapp.cn/news/296117430

## Linked
- [rubin-shipments-start-q3-fy27](rubin-shipments-start-q3-fy27.md)
- [rubin-share-of-blackwell-base](../open_checks/rubin-share-of-blackwell-base.md)
- [cadence-and-yield-trough](../mechanisms/cadence-and-yield-trough.md)
