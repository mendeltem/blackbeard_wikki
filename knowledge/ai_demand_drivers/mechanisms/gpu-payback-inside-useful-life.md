---
id: gpu-payback-inside-useful-life
typ: mechanismus
status: vorschlag
thema: knowledge/ai_demand_drivers
stand: 2026-11-10
herkunft: Chat with Mendel (Claude Code), 2026-11-10; theses Mendel, arithmetic Claude
verweist_auf: [older-hbm-hardware-holds-value, financing-limit, refresh-instead-of-new-build, used-accelerator-and-workstation-prices, allocation-beats-datasheet, circular-financing]
---

# GPU payback sits well inside the useful life, so buyers keep ordering

## Statement
Theses Mendel (2026-11-10): "A100 and older are used like never before, in our data centre too, and get dearer."
"Many H100 still work." "Neoclouds like CoreWeave finance themselves within two years." "Nvidia GPUs are
general-purpose and fungible; ASICs are specialised and mostly for in-house use (Google excepted)."

Arithmetic (Claude, 80 % utilisation, all-in cost per H100 incl. server, network and data-centre share
~40 to 55 kUSD, power ~1 kW at ~0.10 USD/kWh = ~0.7 kUSD/year, negligible):

| Rental price | Revenue per GPU-year | All-in payback |
|---|---|---|
| 8 USD/h (2023 on-demand peak) | ~56 kUSD | ~1 year |
| 4 USD/h (2023/24 contracts) | ~28 kUSD | ~1.5 to 2 years |
| 2.35 to 2.50 USD/h (2025/26) | ~16 to 17.5 kUSD | ~2.5 to 3 years |

Useful life observed beyond the write-off period: A100 launched May 2020 (about 6.5 years in Nov 2026) and is still
fully booked; V100 (2017) still runs in research clusters. Hyperscalers depreciate servers over 5 to 6 years.
Failure rate under full training load: Llama 3 run on 16,384 H100 for 54 days had about 220 GPU or HBM faults
(~1.3 %), replaced part by part, cluster kept running.

Chain:

    payback 1 to 3 years  <  useful life 6+ years  ->  each generation earns its price 2 to 5 times
    -> buyers order the next generation  -> demand does not wait for the old fleet to wear out
    fungible GPU (any model, framework, workload; rentable, resellable)  -> high residual value
    -> lower risk for the buyer and collateral for debt-financed neoclouds; an ASIC loses value when the workload changes

## Carries
That the "GPUs age fast, capex cannot pay back" argument has not held for the A100 and H100 generations: the
economic life exceeds the accounting life. Why neoclouds and labs buy aggressively at scarcity prices. Why Nvidia
invests in independent GPU-only buyers (CoreWeave): hyperscalers are customers and rivals (TPU, Trainium, Maia, MTIA).

## Does not carry
That H100 or B200 will age like the A100: too young to know. That neoclouds are profitable: CoreWeave reported high
adjusted EBITDA margins but net losses from interest and depreciation (2024 about -0.9 bn USD, unverified at the
filing). Rental prices fell in 2025 before rising again (see older-hbm-hardware-holds-value); payback on spot rates
is not payback on contracts. Revenue for Nvidia from old fleets: none, the rent goes to the fleet owner.

## Break indicator
H100 one-year rental falls below 1.70 USD/GPU-h (Oct 2025 level) while Rubin ramps: payback then moves past 4 years
on new contracts. Or a neocloud fails to refinance or renew contracts at old rates.

## Source
- Llama 3 failures: Grattafiori et al. 2024, "The Llama 3 Herd of Models", arXiv:2407.21783 (section on reliability).
- A100 launch: Nvidia GTC keynote, 14 May 2020 (press release, Nvidia newsroom).
- Rental prices: see sources in [older-hbm-hardware-holds-value](older-hbm-hardware-holds-value.md); 8 USD/h 2023 peak is a commonly quoted on-demand figure, unverified.
- CoreWeave capacity guarantee by Nvidia (~6.3 bn USD, 2025) and net loss 2024: CoreWeave S-1 and 8-K filings, unverified here.
- Payback table: own arithmetic, 2026-11-10.

## Linked
- [older-hbm-hardware-holds-value](older-hbm-hardware-holds-value.md)
- [financing-limit](financing-limit.md)
- [refresh-instead-of-new-build](refresh-instead-of-new-build.md)
- [used-accelerator-and-workstation-prices](../open_checks/used-accelerator-and-workstation-prices.md)
- [allocation-beats-datasheet](../../compute_bottlenecks/mechanisms/allocation-beats-datasheet.md)
- [circular-financing](../../ai_buyers/risks/circular-financing.md)
