# Equipment: repair or replace (Jersey City laundromat)

Status: **fleet confirmed from the listing (BizBuySell #2564518, Tumble Wash Laundromat), the broker's proforma P&L and Ryan's 12 photos.** Data plates not yet photographed, so exact ages are still the seller's "about 15 years".

What the photos and P&L show:
- **Washers:** 33 Speed Queen stainless front-load *hardmount* washer-extractors (13 x 20 lb, 15 x 40 lb, 5 x 60 lb). They have the older keypad/LED control panels (pre-Quantum), consistent with roughly 2010-2011 build, and card readers on each. They're bolted on a raised tiled concrete curb, numbered at least to 25. They look clean and well kept.
- **Dryers:** white 30 lb double-stack dryers with card readers, brand not legible in the photos. The P&L says 36 dryers and the listing 34. I model 18 stacks (36 pockets), which fits the long dryer wall in the photos.
- **Other equipment:** CCI card system with Cents POS for wash and fold, a seller-owned ATM (included), a soda vending machine, an arcade cabinet, folding tables, carts, TVs, cameras and auto-lock doors.
- **Utilities and upkeep in the P&L:** maintenance $450/mo ($5.4k/yr), gas $2,700/mo, water $2,700/mo, and sewer included in rent. **Electric has no line in the P&L**: the building has one meter, the landlord pays $340 and the store pays the rest. That's a missing expense for the underwriting model. Separate metering is possible at extra cost.
- **Building:** ground floor of a 3-story brick building with apartments above (1147 on the awning; the street photo suggests Summit Ave, inferred). Any new dryer venting, gas or electrical work needs landlord consent and touches a residential building, so permits will get a closer look.

Files in this folder:
- `fleet_inputs.csv`: one row per machine type (count, age, installed cost, life, repair, revenue, utility). Edit this.
- `model.py`: 17-year repair vs. replace model with federal and NJ tax. Assumptions at the top.
- `strategy_summary.csv`: present-value results for the three strategies.
- `capex_schedule.csv`: capex by year for each strategy, for the underwriting model.

## 1. The bottom line

1. **Bonus depreciation is not a reason to replace machines early.** Bonus depreciation doesn't make a machine cheaper. It lets you deduct the full cost in the year you buy it instead of over 5 to 7 years. Since the One Big Beautiful Bill Act made 100% bonus permanent ([BDO](https://www.bdo.com/insights/tax/one-big-beautiful-bill-act-expands-100-depreciation-expensing-opportunities)), that's true whenever you buy. Example: $363k of washers saves about $134k of federal tax (37%) in the year bought, so the after-tax cost is about $229k. Buy them in year 1 and you save $134k in year 1. Buy them in year 4 and you save the same $134k in year 4. Buying early doesn't create extra savings. It just spends $229k sooner and throws away the remaining life of machines that still work. The exceptions: (a) Congress repeals bonus before you buy (section 2a: small effect, Sec. 179 backstops it), or (b) the owners' tax rate is much higher now than it will be later.
2. **The machines you're buying with the store also get 100% bonus.** Used property qualifies if you (or a predecessor) didn't use it before and you didn't buy it from a related party. Buying the existing washers and dryers from an unrelated seller qualifies. So whatever part of the purchase price is allocated to equipment on Form 8594 is written off federally in year one, with no need to buy new machines to get a deduction. This makes the **purchase price allocation** (equipment vs. goodwill, which is amortized over 15 years) the biggest equipment-related tax lever. That belongs in the underwriting and structure threads, and the seller will push the other way because equipment allocation creates depreciation recapture for them.
3. **The deduction only helps if someone can use it.** If the owners don't materially participate, a large equipment write-off becomes a suspended passive loss. That's the structure thread's question (your hours vs. your parents' returns), but it decides whether "replace now for the write-off" is worth anything at all.
4. **New Jersey doesn't follow federal bonus.** NJ Gross Income Tax allows only a $25,000 Sec. 179 deduction and recovers the rest over regular MACRS lives ([Monaco CPA summary of GIT-DEP](https://www.monacocpa.cpa/post/section-179-bonus-depreciation-nj)). Budget for a separate NJ depreciation schedule.
5. **What actually decides it is how long these machines really last, and the evidence says not as long as I first assumed.** A Coin Laundry Association survey puts the *average* life of laundromat washer-extractors and dryers at 12 to 15 years ([American Coin-Op](https://americancoinop.com/articles/replace-equipment-increase-profits-part-1)), and distributors give the same 10 to 15 years ([Coin-O-Matic](https://coinomatic.com/the-lifecycle-of-a-laundry-machine-when-to-repair-replace-or-upgrade/)). Premium machines are rated up to about 30,000 cycles, which at a busy store's 8 to 12 loads a day is roughly 7 to 10 years of heavy use ([Unity, citing Speed Queen](https://buyunitynow.com/how-long-do-commercial-washers-last-lifespan-cycles/)). Owner forums I could reach were mostly about home Speed Queens, not laundromat fleets. The 20-25 year figure I used before is what the best-kept hardmounts reach, not the norm, so I've changed the base case to 18 years. That's above average, given clean Speed Queens and low repair spend. At about 15 years old today, **these washers are near the end of a normal life.** Plan to replace them in roughly years 1 to 4, and let the pre-close inspection set the exact timing. The dryers can wait longer.

## 2. Model results (actual fleet, after-tax PV of 17 years of equipment cost, lower is better)

Each cell shows run to failure / washers now / retool now, after-tax PV in $k. "Run to failure" here means replacing the washers as they reach their life.

| Washer life (from build) | 5% price lift | 10% lift (base) | 20% lift |
|---|---|---|---|
| 15 yrs (industry average): replace in year 1 | 554 / 564 / 612 | 534 / 544 / 592 | 494 / 504 / 552 |
| 18 yrs (base): replace in year ~4 | 524 / 563 / 610 | **508** / 542 / 590 | 476 / 502 / 550 |
| 22 yrs (best case): replace in year ~8 | 495 / 556 / 604 | 483 / 536 / 584 | 460 / 496 / 544 |

The price lift reflects that customers will pay "up to 10-20% more for updated equipment" (CLA white paper, via American Coin-Op).

**Plan to replace the washers in roughly years 1 to 4 and the dryers around year 10. Don't do a full retool on day one.** If the washers really are at the industry-average 15 years, waiting just means replacing them next year, a near tie (about $10k difference). If they hold up like good Speed Queens, waiting saves $35k to $60k. Replacing the dryers on day one costs about $50k more in every case, because dryers last longer. The base path (`capex_schedule.csv`) is about $373k of washers in year 4 and $171k of dryers in year 11, in today's dollars. A full retool now would cost about $530k installed, or $363k for washers only.

*Correction to my earlier draft:* before the P&L arrived I assumed repairs on a 15-year-old fleet ran about $60k a year, which made replacing now look best. The P&L shows $5.4k a year, so I recalibrated repairs to about $8k a year today (including some owner labor), rising 8% per year as the fleet ages. If the seller has been doing repairs himself unpaid, or the data plates show the machines are older than stated, push the retool earlier.

**What this means for the deal:**
- Budget the washer replacement (~$363k-$373k) as near-term capex, likely within the first 1 to 4 years, plus about $171k for dryers later. In reserve terms that's about $30k-$35k a year, but it comes early, so the underwriting model should show it as an early lump, not a smooth reserve.
- The washers are near the end of a normal life, so a near-term washer replacement is a strong, concrete negotiating point on price.
- For Form 8594, 15-year-old Speed Queen hardmounts still have used-market value, so a modest equipment allocation (likely tens of thousands of dollars, to be supported by an appraisal or distributor quote) is defensible and gets 100% bonus federally. The rest goes to goodwill, amortized over 15 years.
- Before closing, have a Speed Queen distributor technician inspect every machine: bearings, door seals and spin, plus dryer burners and drums. A few hundred dollars buys the real remaining-life answer.

Key assumptions (all editable in `model.py`): 8% discount rate (all-cash, cost of equity); 37% federal and 8.97% NJ marginal rates; repair cost about $8k/yr today, growing 8% per year of age; downtime costs $0.60 of revenue per $1 of repair; new washers use 25% less water and energy; washers last 18 years and dryers 25 (from build); new washers support a 10% price increase; no replacements in the last 3 years of the lease; used machines worth 35% of remaining life at lease end.

The 17-year lease fits one replacement cycle well. A washer retool in years 1 to 4 gets 13 to 16 years of use inside the lease, and the new machines add value if you sell the store or renew.

## 2a. What if Congress repeals 100% bonus depreciation before the retool?

**It doesn't change the answer.** I reran the base case assuming bonus depreciation is gone for every purchase after year one, so the year-4 washers and year-11 dryers get ordinary 5-year depreciation federally. Waiting gets about $16k (PV) more expensive ($508k to $524k), but it still beats replacing washers now ($546k) by about $22k and a full retool ($590k) by about $66k. Losing bonus only delays deductions, it doesn't eliminate them.

Why the realistic risk is even smaller than that:
- **Section 179 is a separate, permanent backstop.** It lets you expense equipment up to $2.5M a year (indexed; about $2.56M for 2026) and isn't tied to bonus depreciation. A ~$373k washer retool fits easily. The catch is that Sec. 179 can't exceed taxable income from active trades or businesses. For an LLC that's tested at both the entity and owner level, and owners' wages and other active business income (e.g., your parents' practice) count. Anything over the limit carries forward. Your CPA should confirm how this works in the chosen structure.
- **100% bonus has had support from both parties.** Democrats enacted it too: the 2010 Tax Relief Act signed by President Obama gave 100% expensing for 2010-2011. Repeal in a future tax bill is possible, especially as a revenue raiser, but changes like this have historically applied only to property acquired after an announced date, with binding-contract protection. You'd likely see it coming and could pull purchases forward then.
- **NJ is unaffected either way.** NJ already ignores federal bonus.

So the right trigger for the retool stays machine condition and repair cost, not Washington. If a credible repeal bill with a near effective date shows up and the washers are already within a few years of their planned replacement, pulling the purchase forward then is reasonable.

**Reserve note:** the underwriting thread normalized earnings to about $108k a year, not the broker's $177k. A $30k-$35k annual equipment reserve is about a third of that, so it matters for the price.

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
4. **Mounting.** This store's washers are hardmounts on a raised concrete curb. Speed Queen-for-Speed Queen replacements can often reuse the curb and anchors (confirm the bolt pattern for the new model). Switching brands or going softmount likely means rebuilding the curb. *Hardmount* washers must be bolted to a reinforced concrete base or pedestal. If you swap brands, the old bolt pattern often won't match, which means cutting or pouring new concrete. *Softmount* washers (spring-suspended) sit on a level slab, cost more per machine but much less to install, and are the easier choice when changing brands or layouts.
5. **Permits.** Commercial work in Jersey City falls under the NJ Uniform Construction Code. The "ordinary maintenance" exemption in N.J.A.C. 5:23-2.7 covers swapping *domestic* washers and dryers in dwelling units, and it explicitly excludes alteration or replacement of gas, water and drain piping ([text](https://law.cornell.edu/regulations/new-jersey/N-J-A-C-5-23-2-7)). Expect to pull permits through the Jersey City Division of Construction Code Official (plumbing, electrical, fire/mechanical subcodes as applicable), with inspections at the end. NJ plumbing and gas work must be done by a licensed master plumber, and electrical work by a licensed electrical contractor. The homeowner exemption doesn't apply to a business. The distributor's installer normally pulls the permits.
6. **Downtime plan.** Retool in phases (one row at a time) to keep the store open, and tell customers in advance.

Can you do it yourself? You can do layout, demolition and removal of old machines, setting softmount washers in place, and hooking up hoses and stack dryers to existing, already-permitted connections. That last part is a gray area and needs a quick conversation with the construction office. You can't legally do gas, new plumbing, electrical or venting. Local help is easy to find: northern NJ and NYC have one of the densest laundromat markets in the country, with several brand distributors and independent technicians.

## 5. Financing the machines

Distributors and manufacturers routinely offer equipment financing and leases (usually 5 to 7 years). With all-cash buyers and current rates, cash is likely cheaper. Financing mainly helps keep liquidity, and the bonus depreciation is the same either way, because financed equipment still qualifies. The comparison belongs in the structure thread.

## 6. What I need to finish this

For each machine (or each row of identical machines): a photo of the **data plate** (back or side), showing brand, model and serial, plus counts by size and a wide shot of each row. The serial gives the build year. Dexter, for example: older serials start with century, year and month (2050300... = March 2005); newer ones look like W1.24162 = 2024, day 162 ([decoding thread](https://laundromatresource.com/forums/topic/dexter-model-and-serial-number-breakdown)). Also helpful: the listing's equipment list, utility bills (water, sewer, gas, electric) and the seller's repair records. With those, `fleet_inputs.csv` becomes real and the table above becomes the answer.

All price and life figures are estimates for planning. Confirm prices with distributor quotes, and confirm tax treatment (class life, Form 8594 allocation, NJ schedule) with your CPA.
