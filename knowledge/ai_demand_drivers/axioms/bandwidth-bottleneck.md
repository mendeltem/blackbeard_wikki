---
id: bandwidth-bottleneck
typ: axiom
status: getragen
thema: knowledge/ai_demand_drivers
stand: 2026-11-25
herkunft: Gespräch Projekt SK Hynix, 2026-10-02; widened to the growing gap and ranked first by Mendel, chat 2026-10-16
verweist_auf: [open-search-space, unverifiable-rival-position, induced-innovation, cadence-and-yield-trough, simulation-needs-compute, hbm-gb-per-mw-three-generations, hbm-bypass-architectures]
---

# Bandwidth bottleneck (von Neumann bottleneck), widening: axiom 1 of 3

## Statement
Axiom 1, the most important of the three (Mendel, 2026-10-16: "the most important axiom is that the von Neumann
bottleneck keeps getting wider").

Memory bandwidth limits accelerator throughput, and the gap between compute and the bandwidth that feeds it widens
with every generation: compute grows faster (3D packaging, more cores, lower precision) than memory can deliver.
Under power and floor-space scarcity buyers buy the part with the highest throughput; demand concentrates on the
newest HBM generation, and every bandwidth improvement is absorbed at once. Not provable, carried.

Why first: the other two axioms (open-search-space, unverifiable-rival-position) explain why money flows into
compute at all; that would serve logic and foundry as much as memory. Only this axiom routes the money specifically
into memory. The widening makes bandwidth the relatively scarcer of two inputs that only work together, and the
scarcer input earns the rent.

Readings in its direction (data, not part of the axiom):
- Gholami et al., "AI and Memory Wall", IEEE Micro 2024 (peer-reviewed; arXiv 2403.14123; DOI not verified here): over 20 years peak server FLOPS grew ×3.0 per two years, DRAM bandwidth ×1.6, interconnect ×1.4; cumulative about 60,000× against 100× and 30×. Gap per two years 3.0 / 1.6 ≈ 1.9, over ten years 1.875^5 ≈ 23.
- hbm-gb-per-mw-three-generations: B200 to Rubin, bandwidth per accelerator 8 to 22 TB/s, per dense PFLOPS 0.80 to 0.44 TB/s (−45 %).
  Update 2026-11-25: the 22 TB/s was the announced value; the first production hardware is specified with 19.2 TB/s
  (ServeTheHome, 31.10.2026, trade press; the maker gave no reason). With the dense PFLOPS of that finding unchanged
  this gives 0.38 instead of 0.44 TB/s per dense PFLOPS (own calculation, not re-read from a maker's table).
- Where the bandwidth comes from (film check 2026-11-25): speed of a connection = number of data lines x speed per line.
  DDR5 module: 64 lines, 51.2 GB/s at grade 6400. HBM3 (JESD238, 2022): 1,024 lines, 819 GB/s per stack, 16 times the
  module. HBM4 (JESD270-4, April 2025): 2,048 lines, up to 8 Gb/s per line, 2 TB/s per stack, at most 64 GB per stack.
- Bandwidth and capacity move apart (same check): Blackwell to Blackwell Ultra capacity x1.5 (192 to 288 GB), bandwidth
  x1.0 (8 TB/s). Blackwell Ultra to Rubin capacity x1.0 (288 GB), bandwidth x2.4 (8 to 19.2 TB/s). H100 to Rubin
  capacity x3.6, bandwidth x5.7. A wider connection does not by itself need more bytes: this is the reading behind
  "Does not carry: DRAM in general".
- Thesis tested 2026-11-25 (Mendel, 24.11.2026: "the main reason why DRAM demand explodes is that we widen the
  bottleneck"). Observed: DRAM industry revenue 1Q26 97 billion US dollars (+81 % on the quarter, contract prices of
  conventional DRAM +93 to 98 %), 2Q26 154.73 billion (+59.5 %) while "DRAM bit shipments grew only modestly"; HBM
  contract prices were declining in 2026; HBM and server modules together 51 % of DRAM bit supply in 2026 (estimate).
  The revenue jump of these two quarters is therefore price, not bits. The sources name three causes (AI servers
  taking HBM and large server modules; the move from training to inference, which shifts demand to general servers;
  HBM using about three times the wafers of DDR5 for the same capacity, which removes supply). No source opened
  measures the share of each cause. Status of "main reason": hypothesis, not observed.

## Carries
Demand for bandwidth memory (HBM), derived via the roofline model. Pricing power of memory relative to compute
while the gap widens.

## Does not carry
DRAM in general. If inference moves to capacity-dominated memory, bit demand stays high but wafer use per bit falls.
Also not more memory per unit of compute: the readings show bandwidth per PFLOPS falling. The axiom reaches memory
makers through scarcity and price and through the growth of compute, not through more bytes per FLOP.

## Break indicator
Inference load moves measurably to SOCAMM, LPDDR or DDR5-RDIMM. For the widening: bandwidth per dense PFLOPS of the
newest Nvidia accelerator rises over two consecutive generations (the gap narrows).

## Source
Product commentary SK Hynix and Micron, Tier 1a. Memory configuration in vendor specifications, Tier 1b. Long-run
rates: Gholami et al. 2024, https://arxiv.org/abs/2403.14123
Added 2026-11-25 (all opened 24.11.2026; the three TrendForce items are press releases of a market researcher, the
others trade press or maker pages; none peer-reviewed):
- Backus J, 1978. Can programming be liberated from the von Neumann style? Communications of the ACM 21(8), 613-641 (origin of the term; DOI and PMID not looked up). https://www.dcs.gla.ac.uk/~wpc/grcs/backus.pdf
- NVIDIA, H100 product specifications (80 GB, 3.35 TB/s). https://www.nvidia.com/en-us/data-center/h100/
- George W, 05.09.2025. Memory speed terminology guide, Puget Systems (DDR5-6400 = 51.2 GB/s). https://www.pugetsystems.com/blog/2025/09/05/memory-speed-terminology-guide/
- Robinson C, 28.01.2022. JEDEC publishes JESD238 HBM3 spec, ServeTheHome. https://www.servethehome.com/jedec-publishes-jesd238-hbm3-spec-for-next-gen-accelerators/
- TrendForce News, 21.04.2025. JEDEC finalizes HBM4 standard (JESD270-4). https://www.trendforce.com/news/?p=38154
- Salvator D, Bhargava R, Devleker K, 19.03.2025. NVIDIA Blackwell Ultra for the era of AI reasoning (288 GB). https://developer.nvidia.com/blog/nvidia-blackwell-ultra-for-the-era-of-ai-reasoning
- Mann T, 18.03.2025. Nvidia's Blackwell Ultra, The Register (bandwidth stays 8 TB/s). https://www.theregister.com/2025/03/18/nvidia_blackwell_ultra/
- Smith R, 31.10.2026. NVIDIA updates Rubin GPU specs as first production hardware arrives, ServeTheHome (19.2 TB/s). https://www.servethehome.com/?p=106378
- TrendForce, 01.06.2026. 1Q26 DRAM industry up 81% QoQ. https://www.trendforce.com/presscenter/news/20260601-13070.html
- TrendForce, 07.09.2026. DRAM industry revenue rises 59.5% QoQ in 2Q26. https://www.trendforce.com/presscenter/news/20260907-13219.html
- TrendForce, 25.08.2026. Memory prices soar (51 % of bit supply; estimate). https://www.trendforce.com/presscenter/news/20260825-13198.html
- Prickett Morgan T, 27.06.2024. Micron gears up for its potential datacenter memory boom, The Next Platform (three times the wafers). https://www.nextplatform.com/2024/06/27/micron-gears-up-for-its-potential-datacenter-memory-boom/
Unverified: the maker's own table for Blackwell (192 GB is derived from 288 / 1.5; some reports give 180 GB usable).
Film with these numbers: "The von Neumann bottleneck and why AI wants a wider tube", 7:01, built 24.11.2026 (not published).

## Linked
- [open-search-space](open-search-space.md)
- [unverifiable-rival-position](unverifiable-rival-position.md)
- [induced-innovation](../mechanisms/induced-innovation.md)
- [cadence-and-yield-trough](../mechanisms/cadence-and-yield-trough.md)
- [simulation-needs-compute](../mechanisms/simulation-needs-compute.md)
- [hbm-gb-per-mw-three-generations](../findings/hbm-gb-per-mw-three-generations.md)
- [hbm-bypass-architectures](../risks/hbm-bypass-architectures.md) — counterforce
