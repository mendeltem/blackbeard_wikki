---
id: older-hbm-hardware-holds-value
typ: mechanismus
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-10-16
herkunft: Chat with Mendel (Claude Code, cloud session), 2026-10-16; theses Mendel from a Gemini chat on SK Hynix of the same day
verweist_auf: [refresh-instead-of-new-build, datacenter-beats-workstation-per-token, ddr5-hbm-per-wafer-opportunity-cost, hbm-eats-wafer-area, financing-limit, gold-rush-demand, demand-is-not-earnings, used-accelerator-and-workstation-prices]
---

# Older HBM hardware holds its value: hyperscalers retire it, capex-limited buyers absorb it

## Statement
Thesis Mendel (2026-10-16): "Even if one player stops investing, many others need it; every memory becomes more
valuable, even the A100." "Big data centres buy for power efficiency, many other firms do not care about power and
buy what is available, because it is scarce." "If workstation GPU and DRAM prices keep rising, cloud firms can sell
old GPUs at a profit." "The RTX 5090 selling at ~6,000 per card shows how scarce local workstations are."

Chain:

    HBM takes DRAM wafer area -> less GDDR7/DDR5 for workstation and consumer parts -> local VRAM scarce and dear
    hyperscalers price in power (OpEx, 24/7 load) -> retire older accelerators early
    labs, universities, SMEs, compliance-bound local inference price in purchase (CapEx, low utilisation, power as overhead)
    -> they absorb the retired cards -> resale and rental prices of older HBM cards hold or rise instead of falling

Two buyer classes see the same card differently. For a hyperscaler running at full load, energy per token decides
(datacenter-beats-workstation-per-token). For a buyer with a fixed hardware budget and 20 to 40 % utilisation,
VRAM per euro and delivery time decide.

Indicators so far (trade press and secondary reports, not a finding):
- SemiAnalysis H100 one-year rental index: 1.70 USD/GPU-h (October 2025) to 2.35 (March 2026), +38 %, as summarised by Tiger Newspress. Contracts reportedly renewed at old rates, some to 2028.
- Nvidia CFO reportedly cited +20 % rental prices for H100 and +15 % for A100 (second-hand report, May 2026, period unclear).
- RTX 5090 (32 GB GDDR7): MSRP 1,999 USD unchanged; EU street prices above 5,000 EUR (Guru3d); Korean flagship models up to ~7.3 M KRW, RTX 5090D in China above twice MSRP (TrendForce, 2026-08-04), attributed to GDDR7 cost and supply.

Counter-readings in the same sources:
- In 2025 the direction was the opposite: AWS cut H100 on-demand rates by ~44 % in mid-2025 (vendor blogs). The turn is recent.
- A vendor blog (Jarvislabs, March 2026) puts used A100 80 GB at 4,000 to 9,000 USD against 7,000 to 15,000 new: a discount, not appreciation. The Gemini chat's "bought at 12,000 to 15,000, resold at 10,000 to 14,000 USD" has no source.

## Carries
That a hyperscaler refresh does not dump older bandwidth into a glut while DRAM wafers are short: the retired
installed base keeps running elsewhere, so refresh adds demand at the top without subtracting it at the bottom.
Complements refresh-instead-of-new-build (which counts new bits at the top) and ddr5-hbm-per-wafer-opportunity-cost
(which explains why the lower tiers get squeezed). Second effect: for neoclouds a high resale value of older fleets
is collateral and liquidity, which loosens the financing-limit for them while it lasts.

## Does not carry
New HBM bits: a resold A100 contains no new wafer. Revenue for SK Hynix, Micron or Samsung: rising rental and resale
prices are paid to fleet owners, not memory makers (demand-is-not-earnings). Rental price is not resale price; the
rental index measures the first. No contradiction with datacenter-beats-workstation-per-token, which is about energy
per token for large loads; this entry is about buyers for whom power is not the binding cost. The price rise can be a
temporary shortage premium (gold-rush-demand) that reverses once Rubin volume and new DRAM capacity arrive.

## Break indicator
Any of: the H100 one-year rental index falls back below its October 2025 level (1.70 USD/GPU-h) while Rubin ramps;
RTX 5090 EU street price returns to within 20 % of MSRP; used A100 80 GB trades below ~4,000 USD. Then the
scarcity premium on older hardware is gone and the thesis reduces to ordinary depreciation.

## Source
Thesis: Mendel, 2026-10-16 (chat). Indicators, all trade press or vendor blogs, not re-read at the original:
- Tiger Newspress on the SemiAnalysis index: https://www.itiger.com/news/1185188896 ; original: https://newsletter.semianalysis.com/p/the-great-gpu-shortage-rental-capacity
- Nvidia CFO rental-price remark (second-hand): https://ocpartnership.org/expert-time/Nvidia-CFO-Highlights-20-Surge-in-GPU-Rental-Prices-as-AI-Chip-Shortage-Intensifies-21-7630
- UOB CIO note, June 2026 (rental prices rising across B200, H100/H200, A100): https://www.uob.com.sg/assets/web-resources/private/pdfs/compute-is-revenue.pdf
- RTX 5090: https://www.guru3d.com/story/geforce-rtx-5090-street-prices-in-eu-now-exceed/ ; https://www.trendforce.com/news/2026/08/04/news-nvidia-rtx-50-prices-in-korea-may-rise-up-to-30-from-aug-on-higher-tsmc-wafer-and-gddr7-memory-costs/
- Used A100: https://jarvislabs.ai/blog/a100-price
Primary readings still missing: see used-accelerator-and-workstation-prices.

## Linked
- [refresh-instead-of-new-build](refresh-instead-of-new-build.md)
- [datacenter-beats-workstation-per-token](datacenter-beats-workstation-per-token.md)
- [ddr5-hbm-per-wafer-opportunity-cost](../../memory_supply/mechanisms/ddr5-hbm-per-wafer-opportunity-cost.md)
- [hbm-eats-wafer-area](../../memory_supply/mechanisms/hbm-eats-wafer-area.md)
- [financing-limit](financing-limit.md)
- [gold-rush-demand](../risks/gold-rush-demand.md)
- [demand-is-not-earnings](../rules/demand-is-not-earnings.md)
- [used-accelerator-and-workstation-prices](../open_checks/used-accelerator-and-workstation-prices.md)
