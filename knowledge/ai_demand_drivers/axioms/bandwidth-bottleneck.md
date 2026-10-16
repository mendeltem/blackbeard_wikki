---
id: bandwidth-bottleneck
typ: axiom
status: getragen
thema: knowledge/ai_demand_drivers
stand: 2026-10-16
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

## Linked
- [open-search-space](open-search-space.md)
- [unverifiable-rival-position](unverifiable-rival-position.md)
- [induced-innovation](../mechanisms/induced-innovation.md)
- [cadence-and-yield-trough](../mechanisms/cadence-and-yield-trough.md)
- [simulation-needs-compute](../mechanisms/simulation-needs-compute.md)
- [hbm-gb-per-mw-three-generations](../findings/hbm-gb-per-mw-three-generations.md)
- [hbm-bypass-architectures](../risks/hbm-bypass-architectures.md) — counterforce
