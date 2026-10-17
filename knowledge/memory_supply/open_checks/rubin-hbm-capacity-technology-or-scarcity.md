---
id: rubin-hbm-capacity-technology-or-scarcity
typ: pruefpunkt
status: offen
thema: knowledge/memory_supply
stand: 2026-10-17
herkunft: Chat with Mendel (Claude Code, cloud session), 2026-10-16
verweist_auf: [cpu-attached-lpddr-adds-conventional-dram-demand, gpu-memory-absorbs-fab-additions, hbm-gb-per-mw-three-generations, hbm-market-share-and-nvidia-allocation, allocation-beats-datasheet, hbm-eats-wafer-area, second-source-hbm4-arrives-presold]
---

# Rubin's 288 GB HBM: set by stack technology or by DRAM scarcity?

## Statement
Thesis Mendel (2026-10-16): "Rubin has 288 GB, like B300, because DRAM is scarce. If it were not scarce, Rubin
would have significantly more." This is the per-package case of gpu-memory-absorbs-fab-additions ("the design is
adapted to the available HBM"). Two readings, both with evidence:

**Technology and design reading.**
- 288 GB = 8 stacks × 36 GB (12-Hi, 24 Gb dies), per Tom's Hardware and Blocks and Files. 16-Hi HBM4 was not in volume: SK Hynix 16-Hi in customer qualification as of mid-2026 (hbm-market-share-and-nvidia-allocation).
- Nvidia spent the HBM4 step on speed, not capacity: 22 TB/s against 8 TB/s for B300, with pin speeds above the JEDEC baseline that delayed HBM4 mass production (Tom's Hardware).
- Precedent: Nvidia's capacity steps came when denser stacks became producible (H100 80 GB to H200 141 GB with HBM3E, B200 192 GB to B300 288 GB with 12-Hi HBM3E).
- AMD MI455X gets 432 GB HBM4 (12 × 36 GB) in the same market (allocation-beats-datasheet). The stacks exist.

**Scarcity reading.**
- Nvidia takes more than half of HBM. With a fixed bit supply, +50 % GB per GPU means −33 % GPUs. Nvidia is paid per GPU, so under scarcity it rationally holds GB per package. AMD can afford 432 GB at roughly 11 % of the allocation and uses capacity as its selling point.
- 16-Hi needs thinner dies and loses more yield, so it costs more wafer per good GB. In a scarce market suppliers prefer 12-Hi. Technology and scarcity are not separable here.
- Rubin CPX takes prefill to GDDR7: Nvidia actively saves HBM.
- Rubin Ultra reportedly cut from 1 TB to about two thirds (~683 GB) because of HBM scarcity (TrendForce, August 2026, see gpu-memory-absorbs-fab-additions). This is the strongest point for the thesis: scarcity binding on a design during the current shortage.
- Single unconfirmed report of 16 stacks and 576 GB for Vera Rubin (Hankyung via TrendForce, March 2026). If it was planned and dropped, it supports the thesis.

**Update 2026-10-17 (Rubin Ultra readings, all trade press or broker notes):**
- GTC 2026 plan: 4 compute dies, 16 HBM4E stacks, about 1 TB per package.
- Summer 2026 (TrendForce, Korean sell-side 2026-06-18): likely 2 dies plus 8 HBM4E stacks of 12-Hi 48 GB, about
  384 GB; reasons named: packaging reticle limit and HBM stacking yield; spec "not final", to be set after H2 2026
  validation; Nvidia may consider HBM4E 8-Hi because supply is tight and prices rise.
- August 2026 (TechNews): Nvidia testing 192 GB and 256 GB variants, some stepping back from HBM4E to HBM4; reasons
  named: HBM supply, price, and HBM4E complexity lagging the schedule.
- 2026-10-16 (KeyBanc via X): Nvidia samples Rubin Ultra with 384 GB HBM4E (8 x 12-Hi, +33 % vs Rubin's 288 GB), but
  most memory suppliers expect a despec to 256 GB (8 x 8-Hi, -11 % vs Rubin and B300).
- Read: package capacity 1,024 -> 384 -> 256 GB, i.e. -75 % against the GTC plan. 8-Hi instead of 12-Hi is also a
  yield choice, not only a wafer choice. The 683 GB figure cited above is superseded by these readings.
- Effect on bits: 256 instead of 288 GB needs +12.5 % units to hold HBM bits; 256 instead of 384 GB needs +50 %.
  While supply binds, shipped bits are set by capacity, not by the datasheet; the hit falls on the 12-Hi/16-Hi
  premium. If the despec is mainly yield, mature 12-Hi/16-Hi stacking in 2028 adds per-GPU demand onto supply.

Judgment (Claude, 2026-10-16, thin basis): Rubin's 288 GB was set mainly by stack technology and the bandwidth
priority; scarcity is the likelier reason that no higher-capacity variant followed and that Rubin Ultra is cut.
Probability that scarcity is the main constraint on GB per package in 2026/27: about 50 % (first estimate ~30 %,
raised after weighing the Rubin Ultra report).

Why it matters: if scarcity binds, demand per package is latent and above supply. "GB per GPU flat in 2027" is then
a supply ceiling, not weak demand; it supports prices, and any relief is absorbed by more GB per package.

Steps:
1. Final HBM capacity of Rubin Ultra from Nvidia (keynote or datasheet): 1 TB or ~683 GB, and the stated reason.
2. Whether Nvidia brings a higher-capacity Rubin refresh (16-Hi, ~384 GB) before Rubin Ultra once 16-Hi qualifies.
3. Confirm or drop the 16-stack / 576 GB report.
4. SK Hynix and Samsung statements on 16-Hi HBM4/HBM4E volume timing and yield (Q3 2026 calls).

Decision rule: Rubin Ultra ships below 1 TB while 16-Hi is in volume → scarcity binds. Rubin Ultra slips for yield
or packaging reasons while bits would be available → technology binds.

## Carries
Which of two readings to test before using "flat GB per GPU" as an argument either way.

## Does not carry
A finding. All capacity figures are vendor specs via trade press (Tier 1b at best); the Rubin Ultra cut and the
576 GB report are trade press.

## Break indicator
Not applicable, open check. Done when steps 1 and 2 have a Tier 1a or 1b source.

## Source
- Tom's Hardware, HBM4 mass production delayed as Nvidia pushes memory specs higher: https://tomshardware.com/tech-industry/hbm4-mass-production-delayed-as-nvidia-pushes-memory-specs-higher
- Blocks and Files, HBM4 supply (12-Hi, JEDEC 4/8/12/16-Hi): https://www.blocksandfiles.com/hci/2026/01/28/high-bandwidth-memory-v4-supply-takes-shape/4090314
- TrendForce, 2026-03-09 (Hankyung, 16 stacks / 576 GB): https://www.trendforce.com/news/2026/03/09/news-samsung-sk%E2%80%AFhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march
- AMD MI455X 432 GB HBM4: https://www.storagereview.com/news/amd-mi455x-and-helios-432gb-hbm4-72-gpu-racks-and-a-real-answer-to-vera-rubin
- Rubin Ultra cut: TrendForce, August 2026, as cited in gpu-memory-absorbs-fab-additions.
- Rubin Ultra 384 GB, spec not final (TrendForce via KuCoin): https://www.kucoin.com/pt/news/insight/NVDA/6a6f780a9bd794000857a58b
- Korean sell-side note 2026-06-18 (reticle limit, stacking yield): https://stock.pstatic.net/stock-research/industry/61/20260618_industry_907123000.pdf
- Nvidia testing 192/256 GB (TechNews, 2026-08-11): https://technews.tw/2026/08/11/nvidia-reportedly-testing-lower-memory-configs-of-rubin-ultra-as-memory-shortage-bites-back/
- KeyBanc 384 GB sampling, 256 GB expected (via @pequityresearch on X, 2026-10-16): no primary link

## Linked
- [gpu-memory-absorbs-fab-additions](../mechanisms/gpu-memory-absorbs-fab-additions.md)
- [hbm-gb-per-mw-three-generations](../../ai_demand_drivers/findings/hbm-gb-per-mw-three-generations.md)
- [hbm-market-share-and-nvidia-allocation](hbm-market-share-and-nvidia-allocation.md)
- [allocation-beats-datasheet](../../compute_bottlenecks/mechanisms/allocation-beats-datasheet.md)
- [hbm-eats-wafer-area](../mechanisms/hbm-eats-wafer-area.md)
- [second-source-hbm4-arrives-presold](../mechanisms/second-source-hbm4-arrives-presold.md)
