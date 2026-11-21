---
id: hbm-generation-change-ratchets-cannibalisation
typ: mechanismus
status: vorschlag
thema: knowledge/memory_supply
stand: 2026-11-21
herkunft: Chat with Mendel (claude.ai project DATACENTER RESEARCH), 2026-11-21; thesis Mendel, staircase wording and arithmetic by Claude
verweist_auf: [hbm-eats-wafer-area, cadence-and-yield-trough, gpu-memory-absorbs-fab-additions, no-standard-cycle-without-absorption-check, demand-is-not-earnings, hbm-contract-prices-2027]
---

# Each HBM generation change ratchets wafer cannibalisation up: a staircase, not a wave

## Aussage
Thesis Mendel: DRAM tightness does not arrive smoothly. Each HBM generation change (HBM3E to HBM4, later HBM4E) brings a sudden step in wafer cannibalisation, and the trade press reads the flat stretch in between as "growth is slowing". Mendel reports the same pattern in Nvidia's reported growth since 2023: slowing was announced, then a new push came and it rose again.

A step has two parts that behave differently:

    yield part:      low early yield of the new generation -> more wafers per good stack; fades as yield matures
    structural part: larger die, more TSVs, more banks -> higher trade ratio per bit; stays and grows per generation

Only the yield part normalises. The structural part does not return to the old level. Hence staircase, not wave.

## Trägt
The direction: after a generation change, cannibalisation settles above the previous level. Micron states the trade ratio rises with each generation (3:1 for HBM3E, towards 4:1 through HBM4 into HBM4E).

## Trägt nicht
The size of the step from the generation mix alone. Arithmetic with trade ratios 3 (HBM3E) and 4 (HBM4):

    wafers per HBM bit at 33 % HBM4: 0.67*3 + 0.33*4 = 3.33
    wafers per HBM bit at 60 % HBM4: 0.40*3 + 0.60*4 = 3.60   (+8 %)
    HBM = 22 % of DRAM wafer input (end 2026) -> +8 % of that = 1.8 points of all DRAM wafers
    HBM wafer share 22 % -> 30 % (end 2027)   -> 8 points, mostly HBM bit growth

So on current numbers the mix shift explains about 2 points and volume about 8. The stair is mainly built from HBM volume per accelerator generation, not from the trade ratio.

The trigger of the current price run. DDR5 contract prices started rising in October 2025, HBM4 volume shipments began in Q3 2026 (SK hynix) and February 2026 (Samsung). The generation change can amplify, it did not start this run.

The Nvidia parallel is Mendel's observation and has not been checked against quarterly figures.

TrendForce's own shares imply a constant ratio of about 2.9:1 for 2026 and 2027 (wafer share 22 % and 30 %, bit share 9 % and 13 %), which does not match Micron's 4:1. Unresolved: yield gains, node migration, or different reference dates.

## Bruchindikator
- At the next change (HBM4E or 16-high), conventional DRAM contract prices do not step up although server demand grows no faster: no stair.
- A supplier reports wafer starts per product class and the HBM share falls back after the ramp: wave, not stair.
- Total DRAM wafer input grows more than 11.4 % in 2027 (78/70 - 1): conventional DRAM keeps its wafers despite a 30 % HBM share.
- Quarter-on-quarter contract price increases keep narrowing through an HBM generation ramp and turn negative.

## Ablesung
Trade ratio: Micron statements via TrendForce news and Hot Chips 2026 reporting (Tier 1b via trade press). Wafer and bit shares: TrendForce (industry service, warning signal). Samsung EVP Kim Taewoo via Reuters, 2026-09-29: HBM near 30 % of DRAM wafer capacity in 2027, about 20 % now. Price onset: trade press. Nvidia pattern: blind.

## Verknüpft
- [hbm-eats-wafer-area](hbm-eats-wafer-area.md)
- [cadence-and-yield-trough](../../ai_demand_drivers/mechanisms/cadence-and-yield-trough.md)
- [gpu-memory-absorbs-fab-additions](gpu-memory-absorbs-fab-additions.md)
- [no-standard-cycle-without-absorption-check](../rules/no-standard-cycle-without-absorption-check.md)
- [demand-is-not-earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)
- [hbm-contract-prices-2027](../open_checks/hbm-contract-prices-2027.md)
