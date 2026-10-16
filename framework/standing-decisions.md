# Standing decisions

Decisions made on Tumble Wash that carry over to the next deal unless something about it changes them. Sources: [ownership-structure-memo.md](/mnt/project-files/structure/ownership-structure-memo.md) (final version, Oct 16, 2026) and [broker-playbook.md](/mnt/project-files/broker/broker-playbook.md). Re-check the tax figures each year, and take the structure to the CPA and a business attorney for each deal.

## 1. Ownership structure: family partnership with Ryan's S corp

**Setup**
1. **OpCo LLC** buys the store's assets and is taxed as a partnership. It is the buyer named on the purchase agreement and on the state bulk-sale notice (NJ: Form C-9600).
2. **Ryan's own LLC, electing S-corp status**, is OpCo's manager and holds Ryan's interest in it.
3. **The parents contribute the capital personally** (about price + $50k for closing costs, working capital and a cushion), plus later equipment replacements as added capital. There is no loan, no interest and no forgiveness. If the money comes from one of their businesses, it's booked as a distribution to them first, and their CPA confirms the business has no other owners.
4. **Ryan's S corp receives** a guaranteed payment for running the store, plus a **profits interest**. The profits interest isn't taxed when granted (Rev. Proc. 93-27); file a protective 83(b) election. The S corp pays Ryan a reasonable salary (Tumble Wash plan: ~$55k in Year 1 at ~22 hrs/wk, ~$25k at ~10 hrs/wk).
5. **Cash waterfall:** guaranteed payment to Ryan's S corp, then a **5% cumulative preferred return** to the parents on unreturned capital, then **80% Ryan / 20% parents**. At exit, the parents' unreturned capital and pref come first, then 80/20.
6. **Tax allocations follow the waterfall ("target allocations").** Depreciation and losses go to the parents while their capital account is positive, so they land against the parents' passive income right away. Ryan's taxable income tracks his cash.
7. **Hours:** Ryan materially participates (500+ logged hours a year, a contemporaneous log), so his share is nonpassive. The parents are passive, which works because they have passive income to absorb losses.

**Why this structure:** on Tumble Wash it gave about $210k of family after-tax NPV in the base case against $107k for the runner-up (an AFR loan to Ryan's LLC), and was $150k+ better in the bear case. Every write-off, including bonus depreciation on the purchased equipment and on early machine replacements, lands on the parents at ~50%. It also avoids the IRS treating a forgiven "loan" as a gift.

**When to re-check it:** it wins when (a) the parents have passive income to absorb losses and (b) big equipment spending comes early. Run `model/structure_e.py` on every deal. If the store needs no capex for many years and is very profitable, the loan structure narrows the gap.

**What the attorney must handle each time:**
- **Sec. 2701.** A child's profits interest next to the parents' preferred interest can be valued as a gift. Make the pref a "qualified payment": fixed rate, cumulative, paid at least annually.
- The operating agreement: target-allocation language, capital accounts, the waterfall, and Ryan's S corp as manager.
- Expected cost: ~$5–15k one-time legal; ~$3–5k/yr more compliance than a single-member LLC (partnership return, S-corp return, a K-1 per owner).

**Unchanged rules:**
- Buy assets, not the seller's company. File the bulk-sale notice on time (NJ: 10 business days before closing).
- Cap any lease guaranty at 12–24 months of rent or use a "good guy" guaranty; never guaranty the full term.
- Form both LLCs and get EINs at least ~3 weeks before closing, with the operating agreement signed before money moves.
- Close early in a calendar year when possible, so Year 1 is a full year for the 500-hour test. Don't lose a store over it.
- Keep Ryan's ~$50k role at the parents' practice real and logged.
- Lock the purchase-price allocation (Form 8594) in the purchase agreement. Equipment gets 100% federal bonus (used property from an unrelated seller qualifies); NJ allows only a $25k Sec. 179 and no bonus.

## 2. Buyer profile: how Ryan presents himself

Stated honestly on every call and in every offer:
- A commercial real estate broker (commission-based) moving into owning and operating a business. Leases, landlords, diligence and closings are his day job.
- **The operating partner.** The parents are the **family capital partners**; the store sits in a family-owned LLC that Ryan manages and runs.
- **All cash, no financing contingency**, proof of funds ready.
- **Hands-on:** in the store heavily in Year 1 (plan ~20–25 hrs/wk), then ~10 hrs/wk with a day manager. Not a passive investment.
- Flexible on closing date, with an attorney and accountant lined up.

**Don't say:** "my parents are paying for it" as an opener (say "family capital partner"), that it's passive, a price before the records are in, or anything you'd have to walk back later.

## 3. Proof of funds: the honest version

- **Offer stage:** send the existing proof-of-funds letter (in the name of the parents' practice LLC). If the broker wants more, add a short signed letter from the parents saying they are providing the equity capital and Ryan is the operator with authority to negotiate. Draft:

  > To whom it may concern: We, [parents' names], are providing the equity capital for [Ryan last name] and/or assigns to purchase the assets of [store name, address], for up to $[price + 50k]. The funds are available now and are not conditioned on outside financing. Ryan will manage and operate the business and has full authority to negotiate this purchase. Contact: [phone/email]. [Signatures, date]

- **Never** show the parents' statement as if it were Ryan's, or crop their names off it. The wire, the purchase agreement and the attorneys will all show where the money comes from.
- **Describe it as:** "an all-cash purchase backed by family capital. I'm the operator and the managing partner."
- **The offer names** "Ryan [last name] and/or assigns." No entities are needed yet.
- **Money moves only twice:** the deposit, and 3–5 business days before closing, as the parents' capital contribution to OpCo.

## 4. Offer terms and protections (in the LOI from day one)

| Term | Standing position |
|---|---|
| Price | Set after the visit and records. Open near the model's opening offer; walk above its walk-away price |
| Financing | All cash, no financing contingency |
| Deposit | 5–10% into the buyer's attorney's escrow, refundable during diligence |
| Diligence | 14–21 days |
| Closing | On the seller's timing; prefer early in a calendar year |
| Staff | Offer to keep everyone |
| Training | 2–4 weeks on site plus 60–90 days of phone support, in the purchase agreement |
| Training holdback | $10–20k held in escrow, released when training is done |
| Non-compete | Seller stays out of laundromats within ~3 miles for 5 years |
| Revenue floor | Price assumes trailing-12-month self-serve revenue of at least a stated figure per the card-system reports, with a price-adjustment formula if lower |
| Walk rights | Landlord won't consent on reasonable terms; utility bills materially change profit; the machine inspection finds major problems |
| Indemnity holdback | Ask for 5–10% for 6–12 months; drop it if it costs the deal and lean on the card-system data |

## 5. Operating plan carried into every model

- Ryan works ~22 hrs/wk in Year 1 and ~10 hrs/wk after, with a ~40 hr/wk day manager from Year 2 (`cases.plan` in `deal.json`).
- The model's NOI pays staff for every attended hour (absentee basis); SDE adds back the value of the hours Ryan works himself.
- Long-term owner role: management, books, marketing, commercial accounts. Delivery through couriers or a part-time driver, not Ryan driving.
- Plan 10–15 hrs/wk even for a store marketed as absentee.
