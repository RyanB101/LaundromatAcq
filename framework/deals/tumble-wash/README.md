# Worked example: Tumble Wash (sold to another buyer, October 2026)

Tumble Wash & Dry, 1147 Summit Ave, Jersey City Heights. BizBuySell #2564518. $450k asking, cash only.

This folder is the Tumble Wash deal re-run through the framework scripts. It reproduces the original project files exactly (every computed cell of the workbook, `cases.json` and `structure_e.json`), so it doubles as the test that the kit works. Labels on a few rows are now generic (for example "Gas + electric" instead of "PSE&G gas + electric").

| File | What it is |
|---|---|
| `deal.json` | Every deal-specific input, note, broker P&L line, comp and case for Tumble Wash. Use it as the model for filling in a new deal |
| `fleet_inputs.csv` | The fleet: 33 Speed Queen washers (13 x 20 lb, 15 x 40 lb, 5 x 60 lb) and 18 double-stack 30 lb dryers, all ~15 years old |
| `capex_scenarios.json`, `capex_schedule.csv`, `strategy_summary.csv` | Equipment model output |
| `Tumble_Wash_Underwriting_Model.xlsx` | The underwriting model, with the scenario snapshot on the Summary sheet |
| `cases.json`, `structure_e.json` | Bear/base/bull with a forced sale, and the structure comparison |

Headline results: underwritten absentee NOI ~$108k vs. the broker's $177,720; ask = 4.2x real NOI; fair value ~$324k–$378k; base-case family NPV ~$210k under the partnership + S corp vs. ~$94k under the AFR loan (model's D); bear case loses most of the capital.

The original analysis, written for the live deal, stays in the project folder:
- [underwriting/](/mnt/project-files/underwriting/) (model, research on comps, opex and tax, listing)
- [equipment/README.md](/mnt/project-files/equipment/README.md)
- [competition/competition_report.md](/mnt/project-files/competition/competition_report.md) and [demand_research.md](/mnt/project-files/competition/demand_research.md)
- [market-comps/README.md](/mnt/project-files/market-comps/README.md)
- [pros-cons/tumble-wash-pros-and-cons.md](/mnt/project-files/pros-cons/tumble-wash-pros-and-cons.md)
- [operations/running-a-laundromat.md](/mnt/project-files/operations/running-a-laundromat.md) and [owner-perspectives.md](/mnt/project-files/operations/owner-perspectives.md)
- [structure/ownership-structure-memo.md](/mnt/project-files/structure/ownership-structure-memo.md)
- [broker/broker-playbook.md](/mnt/project-files/broker/broker-playbook.md)
