# Laundromat acquisition framework

A repeatable way to take a laundromat listing from "this looks interesting" to an offer, built from the Tumble Wash deal (1147 Summit Ave, Jersey City, October 2026; it sold to another buyer). Tumble Wash is kept as the worked example at the end of this page. Its original files stay where they were in the project folder.

**What's in the kit**

| File | Use it for |
|---|---|
| [README.md](README.md) (this page) | The nine steps, in order |
| [checklist.md](checklist.md) | Documents to request, and the red flags to look for in them |
| [standing-decisions.md](standing-decisions.md) | Decisions that carry over to every deal: ownership structure, buyer profile, proof of funds, offer terms |
| [broker-call-script.md](broker-call-script.md) | First broker call, follow-up email and texts |
| [model/HOW-TO.md](model/HOW-TO.md) | Running the underwriting model, cases, structure and equipment scripts on a new listing |
| `deals/_template/` | Blank `deal.json` and `fleet_inputs.csv` to copy for a new deal |
| `deals/tumble-wash/` | Tumble Wash re-run through the kit (the worked example) |

**How long it takes:** steps 1 to 3 give a go/no-go on the numbers in a day once the broker P&L is in hand. Steps 4 to 9 can run in parallel; in the project, each one was its own thread.

---

## The steps

### 1. Listing intake
Save the listing (PDF and text) and every photo the broker sends. Write down the facts in one place:
- Ask, financing terms, stated revenue and SDE or cash flow, square footage.
- Rent, what it includes (NNN, CAM, sewer, utilities), escalations, and years left. Note whether the years include options.
- Hours, unattended hours, staff and their hours, and the seller's own hours.
- Revenue by line: self-serve, wash-dry-fold (pounds and price), delivery, vending, ATM, games, dry cleaning.
- Machines: count by type and size, brand, and stated age. Note any count that differs between the listing and the P&L.
- Payment system (card, coin, app) and POS, because they decide how verifiable revenue is.
- Seller's tenure and stated reason for selling.

Anything that doesn't add up goes straight onto the red-flags list ([checklist.md](checklist.md)).

**Output:** `deals/<name>/listing/` with the PDF, a text copy, and a facts summary.

### 2. Broker P&L normalization
Rebuild the broker's P&L line by line before trusting any multiple:
- Re-add the broker's own lines. Tumble Wash's P&L total was $15,300 a year short of its own lines.
- Add what broker P&Ls usually leave out: payroll tax and workers' comp, electric (shared meters), sewer, accounting and legal, licenses, payroll service, marketing and a contingency.
- Pay every attended hour, including the seller's, at a wage that keeps staff (check the state minimum wage for Year 1).
- Replace low repair and insurance figures with realistic ones for the fleet's age.
- Haircut unverifiable cash lines (vending, games, ATM, dry cleaning).

**Output:** the `broker_pnl` block of `deal.json`. The model's *Seller Recast* sheet shows broker vs. underwritten, line by line, with a reason for each difference.

### 3. Underwriting model
Fill in `deals/<name>/deal.json` and run the model ([model/HOW-TO.md](model/HOW-TO.md)). It produces:
- The *Summary* sheet: underwritten NOI and SDE, ask as a multiple of real NOI, pre-tax IRR, after-tax NPV by ownership structure, fair-value range, opening offer and walk-away price.
- A scenario table: offers below ask, capex timing, utility and revenue stress, owner hours, no lease renewal, and the bear, base and bull cases.
- `structure_e.json`: the family partnership (the standing structure) against the loan alternative, including a sale after a bad Year 1.

**Decision point:** if the underwritten NOI at the ask is above about 4x, or the bear case loses most of the capital, the price has to move or the deal is a pass.

### 4. Equipment: repair or replace
Get each machine's brand, model, serial number (data plate photo) and size, then fill `fleet_inputs.csv` and run `equipment_model.py`. It compares running to failure, replacing washers at close, and a full retool, after tax, and writes the four capex scenarios the model uses.
- Base washer life on the industry average of 12 to 15 years, not the best case (18 to 25).
- Before closing, pay a distributor technician to inspect every machine. That inspection sets the capex timing.

### 5. Competition and demand check
Map every laundromat within a mile (rating, review count, hours, prices, chain or independent) and the trade area's people: population within half a mile and a mile, renter share, and housing built before 1980 (a proxy for no in-unit laundry). Then answer two questions:
- Is the store's claimed revenue a believable share of the area's laundry spending?
- Who is the direct threat (a chain renovating nearby, a newer store a block away), and how much self-serve volume could it take? Stress-test self-serve at −15%.

Also list nearby commercial wash-and-fold prospects and work out the most likely real reason the seller is leaving.

### 6. Market comps
Collect 30+ current and recently sold listings in the metro (price, gross, SDE, rent, lease left, sq ft, machines and age, financing). Compare the subject on:
- Price ÷ normalized SDE, not the broker's SDE
- Price ÷ revenue
- Broker SDE as a % of revenue (anything well above the ~35% median means the SDE is inflated)
- Rent as a % of revenue
- Lease years left and equipment age

Look out for a better deal that turns up during the search.

### 7. Pros and cons
Write up the lived side for this buyer: what the days are like, staff, customers, the building and neighbors, physical work, and life fit. Rate each negative on how likely it is and how much it would hurt, then list cheap ways to test it before committing (shifts in the store, visits at off-hours, meeting staff, the machine inspection).

### 8. Ownership structure
Start from the standing structure ([standing-decisions.md](standing-decisions.md)): a family partnership where the parents contribute the capital and Ryan holds a profits interest through his own S corp. Re-run `structure_e.py` on the deal to confirm it still beats the loan alternative. It wins when the parents have passive income and big equipment spending comes early. Then take it to the CPA and attorney.

### 9. Broker approach and call script
Use [broker-call-script.md](broker-call-script.md). The goal of the first call is to be the buyer the broker wants to bring offers from: cash, certain, flexible, and hands-on. Get the lease and card-system data moving and book a visit. Don't name a price until the records are in. The written offer carries the protections from day one (see [standing-decisions.md](standing-decisions.md)).

---

## Worked example: Tumble Wash (October 2026)

Tumble Wash & Dry, 1147 Summit Ave, Jersey City Heights. BizBuySell #2564518, $450k asking, cash only, ~2,000 sf, 33 washers and 34 dryers about 15 years old, $2,758/mo rent with 17 years left. The broker's P&L claimed $177,720 a year. **It sold to another buyer before an offer went in.**

| Step | What came out of it | Files |
|---|---|---|
| 1. Intake | Listing, 12 photos, the broker P&L transcribed. The P&L said 36 dryers and the listing 34; electric had no cost line on a shared building meter | [listing.txt](/mnt/project-files/underwriting/listing/listing.txt), [inputs notes](/mnt/project-files/.notes/inputs.md) |
| 2. P&L normalization | Real absentee NOI about **$108k**, not $177k. Missing payroll tax and workers' comp, electric, low repairs and insurance, and a P&L total $15,300 short of its own lines | *Seller Recast* sheet in the model |
| 3. Underwriting | Fair value about $324k–$378k. Open around $320k, walk above about $380k. Ask = 4.2x real NOI. Bear case loses most of the capital | [model](/mnt/project-files/underwriting/Tumble_Wash_Underwriting_Model.xlsx), [cases.json](/mnt/project-files/underwriting/cases.json), kit re-run in `deals/tumble-wash/` |
| 4. Equipment | Washers near the end of a normal life: about $373k of washers in years 1–4 and $171k of dryers around year 11. Don't retool on day one | [equipment/README.md](/mnt/project-files/equipment/README.md) |
| 5. Competition | 29 laundromats within a mile, Bubbles 2 one block away with 220 reviews to Tumble Wash's 44. Revenue was a believable fair share, with no moat. Seller likely burned out and leaving before the machine replacement | [competition_report.md](/mnt/project-files/competition/competition_report.md), [demand_research.md](/mnt/project-files/competition/demand_research.md) |
| 6. Comps | At 4.2x normalized SDE, fair rather than cheap. The lease was the standout: rent 8.9% of revenue (best of 36) and 17 years left (longest found). A renovated Hudson County store (#2411455) surfaced as a rival | [market-comps/README.md](/mnt/project-files/market-comps/README.md), [comps.csv](/mnt/project-files/market-comps/comps.csv) |
| 7. Pros and cons | Biggest risks: profit nearer $108k than $177k, goodwill tied to the seller's family, and a crowded block. Biggest upside: a working store to learn on, with skills that carry into real estate | [pros and cons](/mnt/project-files/pros-cons/tumble-wash-pros-and-cons.md), [operator's guide](/mnt/project-files/operations/running-a-laundromat.md) |
| 8. Structure | Family partnership plus Ryan's S corp beat the AFR loan: about $210k vs. $107k family NPV in the base case, and $150k+ better in the bear case | [ownership-structure-memo.md](/mnt/project-files/structure/ownership-structure-memo.md), [structure_e.json](/mnt/project-files/underwriting/structure_e.json) |
| 9. Broker approach | Call script, offer terms and an honest proof-of-funds plan for broker John Bedosky | [broker-playbook.md](/mnt/project-files/broker/broker-playbook.md) |

**Lessons that went into the kit:** ask for the lease and 24–36 months of card-system reports on the first call; recast the P&L before reading any multiple; and move fast on a store you like. Tumble Wash sold before an offer went in.
