# Equipment: repair or replace (Jersey City laundromat)

Status: **framework done, fleet still a placeholder.** No photos, listing or equipment list were in the project as of 2026-10-16. Every dollar figure below that depends on the actual machines comes from a placeholder fleet (`fleet_inputs.csv`: 26 washers, 14 stack dryers, 4 large dryers, all assumed 12 years old) and industry price estimates. Swap in the real machines from the data plates and rerun `python3 model.py`.

Files in this folder:
- `fleet_inputs.csv`: one row per machine type (count, age, installed cost, life, repair, revenue, utility). Edit this.
- `model.py`: 17-year repair vs. replace model with federal and NJ tax. Assumptions at the top.
- `strategy_summary.csv`: present-value results for the three strategies.
- `capex_schedule.csv`: capex by year for each strategy, for the underwriting model.

## 1. The bottom line

1. **Bonus depreciation is not a reason to replace machines now.** The One Big Beautiful Bill Act made 100% bonus depreciation *permanent* for property acquired and placed in service after Jan 19, 2025 ([BDO](https://www.bdo.com/insights/tax/one-big-beautiful-bill-act-expands-100-depreciation-expensing-opportunities)). There is no deadline to beat, and a machine bought in year 6 gets the same 100% write-off as one bought today. The only "use it before it's gone" risk is a future Congress repealing it, which is political, not scheduled.
2. **The machines you're buying with the store also get 100% bonus.** Used property qualifies if you (or a predecessor) didn't use it before and you didn't buy it from a related party. Buying the existing washers and dryers from an unrelated seller qualifies. So whatever part of the purchase price is allocated to equipment on Form 8594 is written off federally in year one, with no need to buy new machines to get a deduction. This makes the **purchase price allocation** (equipment vs. goodwill, which is amortized over 15 years) the biggest equipment-related tax lever. That belongs in the underwriting and structure threads, and the seller will push the other way because equipment allocation creates depreciation recapture for them.
3. **The deduction only helps if someone can use it.** If the owners don't materially participate, a large equipment write-off becomes a suspended passive loss. That's the structure thread's question (your hours vs. your parents' returns), but it decides whether "replace now for the write-off" is worth anything at all.
4. **New Jersey doesn't follow federal bonus.** NJ Gross Income Tax allows only a $25,000 Sec. 179 deduction and recovers the rest over regular MACRS lives ([Monaco CPA summary of GIT-DEP](https://www.monacocpa.cpa/post/section-179-bonus-depreciation-nj)). Budget for a separate NJ depreciation schedule.
5. **What actually decides it is fleet age and revenue, not tax.** On the placeholder fleet, the three strategies land within about 2% of each other on an after-tax present-value basis. Fleet age swings the answer (table below). New machines pay off through lower water, sewer and gas, fewer broken machines, and the ability to raise vend prices or add larger pockets, not through the write-off.

## 2. Model results (placeholder fleet, after-tax PV of 17 years of equipment cost, lower is better)

| Revenue uplift from new washers | Fleet age 6 yrs | Fleet age 12 yrs | Fleet age 18 yrs |
|---|---|---|---|
| 0% | **Run to failure** ($968k) | **Retool now** ($1,067k) vs. run to failure $1,075k | **Retool now** ($1,067k) vs. $1,090k |
| 5% | **Run to failure** ($940k) vs. retool $1,032k | **Retool now** ($1,032k) vs. $1,047k | **Retool now** ($1,032k) vs. $1,055k |
| 10% | **Run to failure** ($911k) vs. retool $997k | **Retool now** ($997k) vs. $1,019k | **Retool now** ($997k) vs. $1,020k |

How to read it: if the machines are under ~8 years old, keep and repair them; a full retool would throw away roughly $90k of value. If they're 12+ years old, a retool in year one is modestly cheaper, and more so if new machines let you raise prices. A full retool of this placeholder fleet costs about **$470k installed**; replacing washers only is about **$306k**. Dryers last 20 to 30 years and almost always justify repair, so "washers now, dryers as they fail" is the usual middle path.

Key assumptions (all editable in `model.py`): 8% discount rate (all-cash, cost of equity); 37% federal and 8.97% NJ marginal rates; repair cost grows 12% per year of age; downtime costs $0.60 of revenue per $1 of repair; new washers use 25% less water and energy; washers last 15 years and dryers 22; no replacements in the last 3 years of the lease; used machines worth 35% of remaining life at lease end.

The 17-year lease fits one replacement cycle well. A retool now gets close to full use of the machines inside the lease. A retool around year 8 to 10 leaves useful life on the floor when the lease ends, unless you renew or sell the store with the equipment.

## 3. When to repair vs. replace a single machine

Replace when any of these is true:
- The repair costs more than about 50% of a new machine's price, or it's the second major repair in a year.
- Parts are discontinued (common on 20+ year old washers and old coin-only controls).
- The machine is down often enough that customers notice ("out of order" is the most common complaint in laundromat reviews).
- Store layout needs a size you don't have: Jersey City customers with bedding and family loads pay for 40 to 80 lb washers.

Repair (yourself) when the machine is a known brand with available parts. These are the usual owner jobs: door gaskets and boots, belts, drain valves, inlet valves, coin and card readers, control board swaps, dryer igniters, sail switches, thermostats and lint screens. Most manufacturers and distributors run owner training, and a parts account with the brand's distributor is the first thing to set up. Washers fail mainly at bearings and seals (a big job on large front-loaders, often a technician job). Dryers are simple machines and rarely need replacing.

What not to do yourself: anything touching gas piping, new electrical circuits, new dryer venting or concrete bases. In NJ those need licensed trades and permits (next section).

## 4. Installing new machines

Steps for a retool, in order:
1. **Check the lease.** Most commercial leases require landlord consent for alterations, utility work or new penetrations (dryer vents through walls or the roof). Get this before ordering.
2. **Pick a distributor.** Each brand sells through an exclusive territory distributor that quotes the equipment, designs the layout, checks utilities, handles install and warranty, and often arranges financing. Get quotes from two or three brands (Speed Queen, Electrolux/Wascomat, Dexter, Continental Girbau, Huebsch). Use each manufacturer's distributor locator for the Hudson County territory. Trade press shows Equipment Marketers was appointed as a Continental and an Electrolux/Wascomat distributor in this region; confirm their current territory. For independent repair of any brand, [New Jersey Commercial Laundry Repair](https://laundryassociation.org/for-owners/laundry-equipment-services/distributors-directory/name/new-jersey-commercial-laundry-repair/) (Manasquan, (732) 226-7053) is listed in the Coin Laundry Association directory.
3. **Utility survey.** The distributor or engineer checks:
   - Water supply size and pressure, and hot water capacity. A new washer fleet may need a bigger or newer water heater (often 10% to 20% of a retool's cost).
   - Drain capacity. Laundromats drain into an open trough, which usually needs a lint screen or interceptor; check with JCMUA.
   - Electrical service. Washers run on 208/240V single or three phase, and a retool can require new circuits or a service upgrade.
   - Gas line sizing for the dryers, plus makeup air.
   - Dryer exhaust: rigid metal duct with length and elbow limits, individual or properly sized common ducts.
4. **Mounting.** *Hardmount* washers must be bolted to a reinforced concrete base or pedestal. If you swap brands, the old bolt pattern often won't match, which means cutting or pouring new concrete. *Softmount* washers (spring-suspended) sit on a level slab, cost more per machine but much less to install, and are the easier choice when changing brands or layouts.
5. **Permits.** Commercial work in Jersey City falls under the NJ Uniform Construction Code. The "ordinary maintenance" exemption in N.J.A.C. 5:23-2.7 covers swapping *domestic* washers and dryers in dwelling units, and it explicitly excludes alteration or replacement of gas, water and drain piping ([text](https://law.cornell.edu/regulations/new-jersey/N-J-A-C-5-23-2-7)). Expect to pull permits through the Jersey City Division of Construction Code Official (plumbing, electrical, fire/mechanical subcodes as applicable), with inspections at the end. NJ plumbing and gas work must be done by a licensed master plumber, and electrical work by a licensed electrical contractor. The homeowner exemption doesn't apply to a business. The distributor's installer normally pulls the permits.
6. **Downtime plan.** Retool in phases (one row at a time) to keep the store open, and tell customers in advance.

Can you do it yourself? You can do layout, demolition and removal of old machines, setting softmount washers in place, and hooking up hoses and stack dryers to existing, already-permitted connections. That last part is a gray area and needs a quick conversation with the construction office. You can't legally do gas, new plumbing, electrical or venting. Local help is easy to find: northern NJ and NYC have one of the densest laundromat markets in the country, with several brand distributors and independent technicians.

## 5. Financing the machines

Distributors and manufacturers routinely offer equipment financing and leases (usually 5 to 7 years). With all-cash buyers and current rates, cash is likely cheaper. Financing mainly helps keep liquidity, and the bonus depreciation is the same either way, because financed equipment still qualifies. The comparison belongs in the structure thread.

## 6. What I need to finish this

For each machine (or each row of identical machines): a photo of the **data plate** (back or side), showing brand, model and serial, plus counts by size and a wide shot of each row. The serial gives the build year. Dexter, for example: older serials start with century, year and month (2050300... = March 2005); newer ones look like W1.24162 = 2024, day 162 ([decoding thread](https://laundromatresource.com/forums/topic/dexter-model-and-serial-number-breakdown)). Also helpful: the listing's equipment list, utility bills (water, sewer, gas, electric) and the seller's repair records. With those, `fleet_inputs.csv` becomes real and the table above becomes the answer.

All price and life figures are estimates for planning. Confirm prices with distributor quotes, and confirm tax treatment (class life, Form 8594 allocation, NJ schedule) with your CPA.
