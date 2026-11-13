# Daily memory price and AI demand log

Written every day at 06:00 by `werkzeuge/speicher-indikatoren` on the workstation (since 2026-11-13; moved from a claude.ai routine). Only observed values and reported facts, no own forecasts.

## speicher_indikatoren_log.csv: one row per day and price item

| Column | Meaning |
|---|---|
| date | day of the run |
| obs_date | "Last Update" of the TrendForce table; weekly and contract values stay old for days or weeks |
| category | DRAM_spot, DRAM_contract, DRAM_module_weekly, GDDR_weekly, NAND_spot, NAND_contract, NAND_wafer_weekly, memory_card_spot, SSD_contract |
| indicator | item name as TrendForce prints it |
| value | session average (contract tables: average), USD as shown; TrendForce does not print the currency on the page |
| change | change printed next to it ("Session Change" or "Average Change"); for daily spot the change to the previous session |
| source, tier, url | TrendForce price page; tier 2 = established secondary source |
| note | high and low of the table, update time (GMT+8) |

Sources: [TrendForce DRAM prices](https://www.trendforce.com/price/dram) (DRAMeXchange spot and contract, module, GDDR) and [TrendForce NAND prices](https://www.trendforce.com/price/flash) (NAND spot and contract, wafer, memory card, PC-client SSD contract). The tables are parsed by rule from the page; no language model touches a number.

## nachfrage_meldungen_log.csv: at most five new reports per day

Topics: capex, accelerator, hbm, nand_ssd, contract, policy_fab. Found by plain web search; a language model (Clé) only picks and summarises from the search results and must copy the URL. `tier` is set from the domain, not by the model: 1a filings and investor relations, 1b company newsroom, 2 TrendForce and established press, 3 everything else (blogs, aggregators). A tier-3 report is a lead, not a finding (see [demand is not earnings](../../ai_demand_drivers/rules/demand-is-not-earnings.md)). A URL is logged only once.
