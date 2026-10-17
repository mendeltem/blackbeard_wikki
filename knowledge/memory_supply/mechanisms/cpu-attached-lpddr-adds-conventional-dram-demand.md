---
id: cpu-attached-lpddr-adds-conventional-dram-demand
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-10-17
herkunft: Chat with Mendel (claude.ai project "Artificial Intelligence"), 2026-10-17
verweist_auf: [hbm-eats-wafer-area, gpu-memory-absorbs-fab-additions, ddr5-hbm-per-wafer-opportunity-cost, rubin-hbm-capacity-technology-or-scarcity, bandwidth-bottleneck]
---

# CPU-attached LPDDR adds conventional DRAM demand on top of HBM

## Statement
Thesis Mendel (2026-10-17): the host CPU's memory is a second, so far uncounted DRAM sink that comes on top of the
GPU-driven HBM shortage. With Vera Rubin the CPU side grows faster than the HBM side, and it draws on the same
conventional DRAM pool that the HBM wafer shift already squeezes.

Why the CPU gets more memory: the LPDDR5X behind Vera serves as a capacity tier for the GPU (offloaded KV cache for
long contexts and multi-step agents, reached coherently over NVLink-C2C) and as working memory for agent workloads
that run on the CPU (tool calls, sandboxes, RL environments, data preparation). This is a capacity role, not CPU
compute on memory, so the von Neumann bottleneck of classic CPUs does not argue against it.

Specs (Tier 1b, vendor):
- Grace: up to 480 GB LPDDR5X, 512 GB/s. Vera: up to 1.5 TB LPDDR5X (8 SOCAMM modules), 1.2 TB/s.
- NVL72 rack: GB300 about 17 TB LPDDR5X (36 Grace), Vera Rubin up to 54 TB (36 Vera).
- CPU:GPU ratio unchanged at 1:2 in NVL72. HGX Rubin NVL8 uses an x86 host, no Vera.
- Reported (TrendForce, June 2026): SOCAMM capacity in the Vera Rubin superchip halved. Nvidia (August 2026) only
  restated "up to 1.5 TB". Shipped configuration open.

Calculation per GPU (wafer-equivalent in GB of standard DRAM; HBM3E factor 3, HBM4 factor 4, LPDDR factor 1, from
hbm-eats-wafer-area; these factors are assumptions):

    B300:               288 x 3 + 240 = 1,104
    Rubin, SOCAMM half: 288 x 4 + 375 = 1,527  (+38 %)
    Rubin, full 1.5 TB: 288 x 4 + 750 = 1,902  (+72 %)

    Increase per GPU 423 to 798, of which HBM +288, CPU LPDDR +135 to +510
    -> CPU side carries 32 to 64 % of the per-GPU increase, while HBM stays 60 to 75 % of the level.

Scale (assumptions): KeyBanc (July 2026) 1.7 to 1.8 M Rubin units in 2026, read as packages, all in NVL72 (too high:
part NVL8, Rubin delayed) -> 0.85 to 0.9 M Vera hosts x 0.75 to 1.5 TB = 0.6 to 1.35 EB LPDDR5X. Against about 40 EB
global DRAM capacity 2026 (Commercial Times via TrendForce, trade press) that is 1.5 to 3.4 % of bits and wafers.
HBM for comparison: about 9 % of bits, 22 % of wafers in 2026 (TrendForce).

Extra demand outside this count: Vera sold as a standalone server (LPX), and x86 servers for agent workloads with
DDR5. Nvidia CFO (Q2 FY27 call): CPU revenue expected to more than double in fiscal 2028. SK hynix 3Q25: shipments
of server DDR5 of 128 GB and more more than doubled QoQ.

Judgment (Claude, 2026-10-17): fastest-growing DRAM sink in Nvidia's stack, not the largest. Probability that
Nvidia's CPU-attached DRAM overtakes HBM in wafer use by 2028: below 10 %. Probability that CPU-side server DRAM in
total (all vendors) is a main driver of the conventional DRAM shortage in 2027: about 60 %.

Channel for memory makers (Mendel 2026-10-17: "new bullish sign for next year"): with bits capped by wafer capacity,
the extra demand acts mainly through the price of conventional DRAM, not through volume. TrendForce: since 1Q26 a
DDR5 64 GB RDIMM wafer earns more than an HBM wafer, so suppliers allocate by price
(ddr5-hbm-per-wafer-opportunity-cost).

## Carries
The direction: per GPU, Rubin needs about 40 to 70 % more DRAM wafer than B300, and a third to two thirds of the
increase is conventional DRAM at the CPU. Demand pressure on conventional DRAM comes from two sides at once.

## Does not carry
Shipped volumes or prices. The SOCAMM configuration is unresolved, the wafer factors are rules of thumb, unit counts
are a broker estimate. The KV-cache rationale is architecture reading; no Nvidia figure quantifies it.

## Break indicator
- Nvidia ships Vera Rubin with clearly less than 750 GB per CPU as standard: CPU share of the increase falls toward 30 %.
- Standalone Vera and agent-server volumes stay small (no million-unit scale by 2027).
- KV cache moves to other tiers (flash, CXL pools, GDDR7 prefill like Rubin CPX) instead of CPU LPDDR.

## Source
- Nvidia NVL72 and Grace specs (Tier 1b): https://www.gigabyte.com/FileUpload/Global/WebPage/1052/NVIDIA_2026_1H_V2.pdf
- Vera 1.5 TB, 54 TB per rack (vendor spec via partner page, Tier 1b): https://www.cudocompute.com/products/nvidia-vera-rubin
- Grace vs Vera capacity and bandwidth, Nvidia statement August 2026, TrendForce June report (trade press): https://xenospectrum.com/en/nvidia-vera-memory-config/
- Standalone Vera (trade press): https://rutab.net/b/hardware/2026/05/19/nvidia-nachala-postavki-processorov-vera-dlya-sistem-ii_2.html
- Nvidia Q2 FY27, CPU revenue outlook (trade press quoting the call): https://hothardware.com/news/nvidias-ai-empire-crushes-q2-estimates-data-center-demand
- KeyBanc 1.7 to 1.8 M Rubin units (broker via press): https://invezz.com/nz/news/2026/07/15/tsmc-stock-braces-for-record-earnings-but-this-nvidia-risk-could-derail-the-rally/
- 40 EB DRAM 2026, HBM factor 4 (trade press): https://www.trendforce.com/news/2025/12/26/news-ai-reportedly-to-consume-20-of-global-dram-wafer-capacity-in-2026-hbm-gddr7-lead-demand/
- HBM wafer and bit share, DDR5 vs HBM per-wafer revenue (TrendForce): https://dramexchange.com/WeeklyResearch/PrinterFriendly/2/12718.html
- SK hynix 3Q25 press release (Tier 1a): https://technode.global/?p=110728

## Linked
- [hbm-eats-wafer-area](hbm-eats-wafer-area.md)
- [gpu-memory-absorbs-fab-additions](gpu-memory-absorbs-fab-additions.md)
- [ddr5-hbm-per-wafer-opportunity-cost](ddr5-hbm-per-wafer-opportunity-cost.md)
- [rubin-hbm-capacity-technology-or-scarcity](../open_checks/rubin-hbm-capacity-technology-or-scarcity.md)
- [bandwidth-bottleneck](../../ai_demand_drivers/axioms/bandwidth-bottleneck.md)
