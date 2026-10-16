# Tax Research: Laundromat Asset Purchase in Jersey City, NJ (closing late 2026 / 2027)

Prepared 2026-10-16. This is research for underwriting, not tax advice. Confirm with a NJ CPA before closing. Items marked **[VERIFY]** could not be fully confirmed against a primary source in this pass.

---

## 0. Headline takeaways

1. **Federal: the purchase can be mostly written off in year one.** 100% bonus depreciation is permanent for property *acquired and placed in service after Jan 19, 2025*, and it covers used equipment bought from an unrelated seller. The Section 179 limit for 2026 is $2,560,000. Washers, dryers, payment systems and most fixtures (5–7 yr) and qualified improvement property (15 yr) all qualify. Goodwill does not; it is amortized over 15 years under Sec. 197.
2. **New Jersey does not allow bonus depreciation, and its Section 179 limit is $25,000.** NJ uses regular MACRS. Two sets of fixed-asset books are needed (Worksheet GIT-DEP).
3. **Structure trap: who buys matters.** Bonus depreciation fails if the asset is acquired from a related party (a parent-to-child transfer is related). It also fails if basis is carried over, for example when the parents buy the assets personally and then contribute them to an LLC. **The operating LLC must be the buyer of record from the unrelated seller.** Parents should fund it as capital or a gift; they should not buy the assets themselves and re-contribute them.
4. **Depreciation losses are only "useful" to someone who is not passive or is passive with passive income.** Losses flow through a partnership LLC by ownership %, subject to basis, then at-risk, then passive (469), then the excess business loss limit (461(l)). In 2026 the 461(l) limit is $256k single and $512k MFJ. Parents who don't work 500+ hours are passive, so the losses would only offset their passive income. The person putting in the hours (the buyer) can use them against other income.
5. **Sales tax:** self-service washer/dryer receipts are **not taxable** in NJ (N.J.A.C. 18:24-15.5). Wash-dry-fold of **clothing** is **not taxable** (18:24-15.3). Commercial linens (hotel, Airbnb and restaurant tablecloths, gym towels) are **taxable at 6.625%** (18:24-15.2). Detergent and vending are taxable.
6. **Bulk sale:** the buyer must file Form C-9600 at least 10 business days before closing. If it doesn't, the buyer becomes liable for the seller's NJ taxes.
7. **Jersey City payroll tax:** 1% of payroll paid by the employer once quarterly payroll reaches $2,500. Wages of JC-resident employees are excluded.

---

## 1. Federal: One Big Beautiful Bill Act (P.L. 119-21, signed July 4, 2025) and 2026 figures

### 1a. Bonus depreciation (IRC 168(k))
- **Rate:** 100%, permanent, for qualified property **acquired after Jan 19, 2025 and placed in service after Jan 19, 2025**. Property placed in service Jan 1–19, 2025 is still at 40%. A taxpayer may elect 40% instead of 100% for the first tax year ending after Jan 19, 2025, and may elect out by class.
  - IRS Pub 946 (2025): https://www.irs.gov/publications/p946
  - IRS Notice 2026-11 (interim guidance; acquisition-date and written-binding-contract rules follow the TCJA-era final regs): https://kpmg.com/us/en/taxnewsflash/news/2026/01/notice-2026-11-interim-guidance-100-percent-depreciation-deduction.html , https://www.bpm.com/insights/irs-notice-2026-11/
- **Acquisition date:** if a written binding contract is signed before Jan 20, 2025, the property is treated as acquired on the contract date and does not get 100%. This is not an issue for a 2026/2027 contract.
- **Used property qualifies** under IRC 168(k)(2)(E)(ii) and Treas. Reg. 1.168(k)-2(b)(3)(iii), provided that:
  - the taxpayer (or a predecessor) did not use the property before acquiring it,
  - it is **not acquired from a related party** under Sec. 267(b)/707(b) (this includes parents, children, siblings, spouse, and >50% controlled entities) or from a member of the same controlled group,
  - basis is **not** carryover/substituted basis (for example, a contribution to a partnership under Sec. 723 is carryover), and
  - basis is not determined by reference to a decedent.
  - **Implication:** the operating entity buys directly from the unrelated seller. Parents personally buying and then contributing the equipment to the LLC would forfeit bonus. The LLC buying from the parents would also fail. [Statutory cite from IRC 168(k)(2)(E)(ii) / 179(d)(2)–(3); Pub 946 chapter 3 "What Is Qualified Property?"]
- **No taxable-income limit** on bonus. It can create or increase a loss (unlike 179).
- **Qualified improvement property (QIP)**, meaning interior improvements to nonresidential buildings placed in service after the building was first placed in service, is **15-year MACRS and bonus-eligible**. It excludes enlargements, elevators/escalators and internal structural framework (Pub 946).

### 1b. Section 179
| Year | Max deduction | Phase-out begins (total 179 property placed in service) |
|---|---|---|
| 2025 (OBBBA) | $2,500,000 | $4,000,000 |
| 2026 (Rev. Proc. 2025-32) | **$2,560,000** | **$4,090,000** |
- Sources: Pub 946 (2025); Rev. Proc. 2025-32 summary: https://www.currentfederaltaxdevelopments.com/blog/2025/10/9/2026-inflation-adjustments-for-tax-professionals-revenue-procedure-2025-32-analysis ; https://blog.portebrown.com/important-tax-figures-for-2026
- **179 is limited to taxable income from active trades or businesses.** Any excess carries forward. For partnerships the limit applies at both the entity and partner level. In year 1 of a new LLC, bonus is usually the better tool; 179 is useful for picking assets selectively.
- 179 also covers QIP, roofs, HVAC, fire/alarm/security on nonresidential property.

### 1c. QBI deduction (Sec. 199A)
- OBBBA made it **permanent at 20%**. Effective for tax years beginning after 2025, the phase-in range widens to $75k single / $150k MFJ, and there is a **$400 minimum deduction** for taxpayers with at least $1,000 of QBI from active businesses in which they materially participate (indexed after 2026). https://www.barnesdennig.com/obbba-impacts-qbi/
- **2026 thresholds** (Rev. Proc. 2025-32):

| Filing status | Threshold (W-2/UBIA limit starts) | Fully phased in |
|---|---|---|
| MFJ | $403,500 | $553,500 |
| MFS | $201,775 | $276,775 |
| Single/other | $201,750 | $276,750 |

- A laundromat is **not** an SSTB, so the deduction is not lost above the threshold. Above the threshold it is capped at the greater of 50% of W-2 wages, or 25% of W-2 wages plus 2.5% of UBIA (unadjusted basis of qualified property). The UBIA leg helps an equipment-heavy laundromat. **For high-income parents, the UBIA of the machines can preserve QBI even with low payroll.**
- QBI is reduced by the depreciation that creates losses. Net QBI losses carry forward.

### 1d. 2026 federal brackets (Rev. Proc. 2025-32)
| Rate | Single | MFJ |
|---|---|---|
| 10% | ≤ $12,400 | ≤ $24,800 |
| 12% | $12,400–$50,400 | $24,800–$100,800 |
| 22% | $50,400–$105,700 | $100,800–$211,400 |
| 24% | $105,700–$201,775 | $211,400–$403,550 |
| 32% | $201,775–$256,225 | $403,550–$512,450 |
| 35% | $256,225–$640,600 | $512,450–$768,700 |
| 37% | > $640,600 | > $768,700 |

Standard deduction 2026: $16,100 single / $32,200 MFJ. Long-term capital gain brackets (0/15/20%) apply to Sec. 1231 gain net of recapture. **[VERIFY]** 2026 20% bracket starts around $613,700 MFJ / $545,500 single. The 3.8% NIIT applies to passive owners' share of income and gain above $250k MFJ / $200k single MAGI (thresholds not indexed).

### 1e. Excess business loss (Sec. 461(l))
- OBBBA made it **permanent**. 2026 limit: **$256,000 single / $512,000 MFJ** (Rev. Proc. 2025-32). Net business losses above that become an NOL carryforward (80% of taxable income limit).
- **[VERIFY]** An earlier House version would have treated the carryover as an EBL in later years. Confirm with a CPA whether the enacted text changed carryover treatment.
- This matters if the buyer has W-2 income and a large year-1 bonus loss. A purchase above about $256k (single) of depreciable assets could produce a loss partly deferred to NOL.

### 1f. SALT cap
- OBBBA raised the cap to **$40,000 for 2025 ($20k MFS), rising 1% per year (2026: $40,400)** through 2029, then back to $10,000 in 2030.
- The cap phases down by 30% of MAGI above $500,000 (2025; about $505,000 in 2026), with a floor of $10,000. https://wiss.com/salt-deduction-cap-40000-nj-ny-taxpayers/ ; https://blog.portebrown.com/important-tax-figures-for-2026
- **Implication:** high-income parents (physicians) are likely still capped at $10k. The NJ BAIT election (section 5d) remains valuable to them. PTET workarounds survived OBBBA.

### 1g. Gift / estate (relevant if parents fund the purchase)
- 2026 annual gift exclusion is **$19,000 per donor per donee**. The lifetime exemption is **$15,000,000** per person (OBBBA, indexed after 2026), with a 40% rate. A gift of, for example, $300k of cash or LLC units requires Form 709 but almost certainly no tax. https://blog.portebrown.com/important-tax-figures-for-2026
- NJ has **no estate tax** (repealed 2018). NJ inheritance tax does not apply to Class A beneficiaries (children). **[VERIFY with estate counsel]**

---

## 2. MACRS class lives for laundromat assets (Rev. Proc. 87-56 / Pub 946 App. B)

| Asset | Class / basis | GDS life | Bonus/179? | Notes |
|---|---|---|---|---|
| Commercial washers, dryers, washer-extractors, folding tables bolted in | Asset class **57.0** Distributive Trades & Services (assets used in retail trade and *personal and professional services*) | **5-yr** (class life 9; ADS 9) | Yes | Industry practice is 5-yr. Some preparers use 7-yr as "no class life." 5-yr is the better-supported position. **[VERIFY with CPA]** (could not pull App. B text in this pass) |
| Card/coin systems, kiosks, bill changers, payment readers | 57.0 (or 00.12 information systems, 5-yr) | 5-yr | Yes | Software bought separately: 36-month straight-line (Sec. 167(f)), bonus-eligible |
| Computers, POS, cameras/DVR | 00.12 / 5-yr property | 5-yr | Yes | |
| Furniture: seating, carts, shelving, office furniture | 57.0 if used in retail/service (5-yr), else 00.11 (7-yr) | 5 or 7-yr | Yes | |
| Water heaters/boilers serving machines | Process equipment (5-yr, 57.0) if dedicated to the machines; **building HVAC/plumbing** = 39-yr real property or 15-yr QIP if an interior improvement | 5 / 15 / 39 | 5/15-yr yes; 39-yr no (179 allowed for HVAC on nonresidential) | Cost segregation argument. Document dedicated use. |
| Leasehold improvements (interior build-out, plumbing runs, floors, ceilings, electrical inside) | **QIP** | 15-yr SL | Yes (bonus and 179) | Tenant-owned improvements. If the lease ends first, the remaining basis is written off on abandonment. |
| Exterior signage (detachable) | 57.0 tangible personal property | 5-yr | Yes | Signs that are structural components = real property |
| Vending machines | 57.0 | 5-yr | Yes | |
| Vehicles (pickup/delivery van) | 00.241/00.22 | 5-yr | Yes (luxury-auto caps unless >6,000 lb GVWR; heavy SUV 179 cap $31,300 in 2025) | |
| Goodwill, going concern, customer base, trade name, workforce, **non-compete** | Sec. 197 intangibles | **15-yr straight-line** amortization | No bonus/179 | A non-compete paid to the seller is 15-yr for the buyer and **ordinary income** to the seller |
| Assignment of lease / leasehold acquisition cost | Sec. 178: amortize over remaining lease term (17 yrs) | | No | |
| Inventory (detergent, vending stock) | Class IV | Expensed as sold | | |

**Allocation strategy:** allocate as much as defensible to Class V equipment and leasehold improvements, based on fair market value supported by an equipment appraisal (age and model list from the photos). The residual goes to Class VI/VII. The seller usually prefers goodwill (capital gain) over equipment (Sec. 1245 ordinary recapture), so allocation is a negotiated point. Lock it in the APA. Under Sec. 1060(a) both parties are bound by a written allocation.

### Form 8594 (Sec. 1060 residual method). Both buyer and seller attach it to their return.
- **I** cash and deposits · **II** actively traded property, CDs, foreign currency · **III** mark-to-market assets and receivables · **IV** inventory · **V** everything else (equipment, furniture, fixtures, leasehold improvements, vehicles) · **VI** Sec. 197 intangibles other than goodwill (non-compete, licenses, customer lists, trade name, workforce) · **VII** goodwill and going concern.
- Source: https://www.irs.gov/instructions/i8594

---

## 3. Passive activity, at-risk, flow-through, SE tax, S-corp salary

### 3a. Loss-limitation ordering for an LLC owner
1. **Basis** (Sec. 704(d) partnership / Sec. 1366(d) S corp). An all-cash, parent-funded deal gives basis equal to the cash contributed. **S-corp shareholders do not get basis for entity debt; partnership members do.**
2. **At-risk** (Sec. 465). Cash equity is at risk. Equipment financing that is nonrecourse is not at risk.
3. **Passive activity** (Sec. 469). Loss is usable against non-passive income only if the owner **materially participates**, determined owner by owner and year by year. Treas. Reg. 1.469-5T(a) sets seven tests. The most relevant are:
   - (1) **500+ hours** in the year;
   - (2) the owner's participation is substantially all of the participation by anyone;
   - (3) **100+ hours and not less than anyone else**, including employees;
   - (5) material participation in any 5 of the preceding 10 years;
   - (7) facts and circumstances (100+ hours; cannot rely on management alone if a paid manager exists).
   - Spousal hours count together. **Parent-to-child hours do not transfer.**
   - LLC members are **no longer treated as limited partners** for this purpose (Garnett, Thompson, Newell case law; Prop. Reg. 1.469-5(e)(3)(i)(B) rewards hours). **[VERIFY final regs status]**
   - IRS Pub 925: https://www.irs.gov/publications/p925 ; Reg: https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.469-5T
4. **Excess business loss** (Sec. 461(l)). See 1e.
- **Passive owners** (likely the parents) can deduct their share only against other passive income, such as rental real estate gains or other passive K-1s. Suspended losses are released in full on a fully taxable disposition of the activity. Physician-owners of their own practice are generally *non-passive* there, so those losses cannot offset practice income. Passive owners also pay **3.8% NIIT** on their share of the laundromat's profit and gain.
- **Special allocations** of depreciation to whoever can use it are possible in a partnership LLC (not an S corp, which must allocate pro rata). They must have "substantial economic effect" (Sec. 704(b)) and bring capital-account and economic consequences.

### 3b. Self-employment tax
- A member who works in the business owes SE tax (15.3% up to the 2026 SS wage base of **$184,500**, then 2.9%, plus 0.9% Additional Medicare above $200k single/$250k MFJ) on their distributive share. This applies to a single-member LLC or to an active member of a multi-member LLC. Passive/investor members of an LLC may argue the limited-partner exclusion (Sec. 1402(a)(13)), but the *Soroban* (2023) line of cases narrowed it to genuinely passive members. **[VERIFY current case status]**
- SS wage base 2026: https://blog.portebrown.com/important-tax-figures-for-2026

### 3c. S corporation
- Owner-employees must be paid **reasonable compensation** through W-2 payroll before distributions. Only the wages bear FICA, and distributions avoid SE tax. Relevant IRS page: https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues
- Drawbacks for this deal: one class of stock (no special allocation of depreciation to parents); no basis for entity debt; distributing appreciated property triggers gain; NJ S-corp pays CBT minimum tax (section 5e); payroll for the owner triggers the JC payroll tax and NJ UI/DI.
- Usually considered only after the business is reliably profitable (roughly >$80–100k profit to the working owner).

---

## 4. Recapture on a later sale
- **Sec. 1245:** gain on equipment up to the depreciation previously taken (including bonus/179) is **ordinary income**, taxed at ordinary rates up to 37%. It is not subject to SE tax and not eligible for installment deferral. Example: equipment bought for $300k, fully bonused, sold for $150k gives $150k of ordinary income.
- Goodwill/Sec. 197 amortization recapture is also ordinary under Sec. 1245. Gain above original cost on goodwill is Sec. 1231/capital.
- QIP (Sec. 1250 property, but 179/bonus taken) gives ordinary recapture of the 179 portion. Unrecaptured 1250 gain is taxed at up to 25% for straight-line depreciation. **[VERIFY treatment of bonus on QIP]**
- 179 recapture also applies if business use drops to 50% or less.
- **NJ:** no capital-gain preference. All gain is taxed at ordinary GIT rates in the "net gains from disposition of property" category. NJ gain differs from federal because NJ basis is higher (no bonus), so NJ recapture is smaller (GIT-DEP Part IV).
- Year-1 bonus is mostly a **timing** benefit plus rate arbitrage: deduct at the buyer's or parents' high bracket now, and recapture later possibly at a lower rate, or never if held until death with step-up under Sec. 1014.

---

## 5. New Jersey

### 5a. NJ Gross Income Tax brackets (unchanged since 2020; same for 2026)
| MFJ taxable income | Rate | Single | Rate |
|---|---|---|---|
| ≤ $20,000 | 1.4% | ≤ $20,000 | 1.4% |
| $20k–$50k | 1.75% | $20k–$35k | 1.75% |
| $50k–$70k | 2.45% | $35k–$40k | 3.5% |
| $70k–$80k | 3.5% | $40k–$75k | 5.525% |
| $80k–$150k | 5.525% | $75k–$500k | 6.37% |
| $150k–$500k | 6.37% | $500k–$1M | 8.97% |
| $500k–$1M | 8.97% | > $1M | 10.75% |
| > $1M | 10.75% | | |
Source: https://ustax.tools/new-jersey-tax-brackets-2026/ (secondary). NJ-1040 instructions confirm the schedule. **[VERIFY against 2026 NJ-1040 instructions]**

### 5b. NJ depreciation: decoupled
- NJ has **disallowed federal bonus depreciation** for GIT since tax years beginning on or after Jan 1, 2004 (P.L. 2004, c.65) and for CBT since 2002 (P.L. 2002, c.40). The only exception is property that took the old 30% allowance.
- NJ Section 179 follows the IRC as of Dec 31, 2002: **max $25,000**, using the federal reduced dollar-limit mechanics, with no carryforward of unused amounts.
- NJ depreciation uses the same MACRS method and life without bonus. The difference is tracked on **Worksheet GIT-DEP**, and partnerships/S corps pass NJ adjustments through on NJ-K-1. At disposition the NJ gain is recomputed.
  - https://nj.gov/treasury/taxation/pdf/current/gitdep.pdf
  - https://www.nj.gov/njbonds/treasury/taxation/decouples2.shtml
- The Division's Dec 2025 OBBBA notice did not change the decoupling. NJ GIT does not use federal AGI. https://njcpa.org/article/2025/12/01/division-of-taxation-clarifies-new-jersey-tax-impact-of-obbba
- **Example:** $300k of 5-yr equipment. Federal year 1 is $300k. NJ year 1 is $25k (179) + 20% MACRS on $275k ≈ $55k, about **$80k** in total. NJ taxable income stays positive while federal shows a loss.

### 5c. NJ: no QBI; income categories; no passive rules
- **NJ has no 199A/QBI deduction.** NJ GIT has no passive-loss rules. Instead it taxes **categories of income**, and a **loss in one category cannot offset income in another** (for example, a laundromat loss cannot offset wages). Losses do not carry forward, except through the Alternative Business Calculation.
- **Alternative Business Calculation (Schedule NJ-BUS-2):** nets the four business categories (net profits from business, partnership distributive share, S-corp pro-rata share, rents/royalties). It allows a loss carryforward (20 years under N.J.S.A. 54A:5-15 **[VERIFY]**) and gives an adjustment of up to 50% of the difference. https://www.nj.gov/treasury/taxation/pdf/current/resbus2.pdf ; https://nj.gov/njbonds/treasury/taxation/pdf/nettingnotice.pdf
- **Implication for the parents:** a laundromat structured as a **partnership** produces a "distributive share of partnership income" item. Within that category it nets against the parents' other partnership K-1s (for example, their practice or investment LLCs if those are partnerships), so an NJ-level loss is usable there.

### 5d. NJ BAIT (Pass-Through Business Alternative Income Tax)
| Distributive proceeds | Rate |
|---|---|
| $0–$250,000 | 5.675% |
| $250,001–$1,000,000 | 6.52% |
| $1,000,001–$5,000,000 | 9.12% |
| > $5,000,000 | 10.9% |
- The election is **annual**, due by the original return due date (Mar 15, 2027 for 2026 calendar year). Members get a refundable NJ credit. Entity-level tax is deductible federally, bypassing the SALT cap.
- https://www.nj.gov/treasury/taxation/baitpte/ (the fetched page showed three tiers; the 9.12% tier at $1M–$5M is from the statute as amended in 2021. **[VERIFY tier]**)
- **Useful?** Only when the entity has positive NJ income and the owners are SALT-capped (the parents likely are, given the MAGI phase-down). Year 1 with heavy depreciation: NJ income is still likely positive because NJ has no bonus, so a small benefit is possible. Low priority; revisit annually.

### 5e. NJ CBT (if the entity elects S or C)
- **C corp:** 9% if ENI > $100k; 7.5% for $50k–$100k; 6.5% at ≤ $50k. A 2.5% surtax applies to income > $10M (not relevant).
- **Minimum tax by NJ gross receipts:** C corp $500 / $750 / $1,000 / $1,500 / $2,000 at <$100k / $100–250k / $250–500k / $500k–1M / ≥$1M. **S corp:** $375 / $562.50 / $750 / $1,125 / $1,500.
- **S corps:** since tax periods beginning after Dec 22, 2022, a federal S election is automatically an NJ S election (opt-out available; TB-105).
  - https://www.nj.gov/njbonds/treasury/taxation/ot4.shtml
  - https://www.crowe.com/insights/tax-news-highlights/nj-updates-s-corp-election-and-partnership-audit-rules

### 5f. NJ partnership filing fee and LLC fees
- **NJ-1065 filing fee:** $150 per owner, for partnerships with **more than two owners** and NJ-source income (max $250,000). It is paid with a 50% prepayment toward the next year. A 2-member LLC pays no per-owner fee; 3 members pay $450/yr plus the prepayment. A single-member LLC is disregarded (no NJ-1065). https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb55.pdf
- **LLC formation:** $125 (Certificate of Formation). **Annual report:** $75/yr through NJ DORES. **[VERIFY current fee]**
- **NJ-1065 nonresident withholding:** applies only to nonresident owners. Not relevant if all owners are NJ residents.

---

## 6. NJ sales and use tax (rate 6.625%)

| Revenue line | Taxable? | Authority |
|---|---|---|
| Self-service washers/dryers (coin, card or app) | **No** | N.J.A.C. 18:24-15.5: "Receipts for the use of washing machines and dryers in a self-service laundromat or laundry room ... are not subject to sales tax." https://regulations.justia.com/states/new-jersey/title-18/chapter-24/subchapter-15/section-18-24-15-5/ |
| Wash-dry-fold / drop-off of **clothing** (retail customers) | **No** | N.J.A.C. 18:24-15.3: cleaning/laundering of clothing is an exception (examples: underwear, sleepwear, work uniforms). Statutory basis is N.J.S.A. 54:32B-3(b)(2). https://regulations.justia.com/states/new-jersey/title-18/chapter-24/subchapter-15/section-18-24-15-3/ |
| Laundering **non-clothing** items: bed linens, comforters, towels, curtains, rugs; **commercial** accounts (hotels, Airbnb/short-term rental linens, restaurant tablecloths, gyms, salons) | **Yes, 6.625%** | N.J.A.C. 18:24-15.2 (laundry services taxable unless clothing; examples include hotel linens and restaurant tablecloths). https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-18-24-15-2 |
| Pickup and delivery charges | Follow the underlying service: not taxable on clothing, taxable on taxable linens | N.J.S.A. 54:32B-2 "sales price" includes delivery charges. **[VERIFY]**. Invoice mixed orders separately. |
| Linen rental | Taxable (rental of TPP) | N.J.A.C. 18:24-15.4 |
| Detergent, softener, bags, hangers (sold OTC or via vending) | **Taxable** | ANJ-16 vending publication names laundry detergent as a taxable nonfood item. Nonfood items ≤ $0.25 are exempt. |
| Vending snacks/candy/soft drinks | **Taxable** if price ≥ $0.26, on **70% of the retail price** (vending food base) | ANJ-16: https://nj.gov/treasury/taxation/pdf/pubs/sales/anj16.pdf |
| Supplies bought for use (detergent used in WDF service, parts) | Use tax applies unless a resale exemption is available. Detergent consumed in an exempt WDF service is **not** resale, so tax is due on the purchase | General rule. **[VERIFY]** |

- **Practical:** register for sales tax (NJ-REG). Collect on commercial/linen work and retail product. File ST-50/51. Vending machines must display operator name/address. The JC Health Department may require a **vending machine license**. https://www.jerseycitynj.gov/cityhall/HousingAndDevelopment/businesses

---

## 7. NJ bulk sale and transfer taxes

- **Form C-9600 (Notification of Sale, Transfer, or Assignment in Bulk):** the **purchaser** (or its attorney) must file it with a copy of the executed contract **at least 10 business days before closing**, by certified, registered or overnight mail. There is no fee.
  - If the buyer **fails** to file, it becomes **liable for the seller's NJ tax debts** (all state taxes, not just sales tax).
  - The Division responds within ~10 business days and may require an **escrow**, which can exceed the price, until the seller obtains a clearance letter.
  - It applies to any sale of business assets outside the ordinary course (inventory, equipment, goodwill), including sales by disregarded entities. FAQ: https://www.nj.gov/treasury/taxation/faqbulksale.shtml ; TB-60: https://nj.gov/treasury/taxation/pdf/pubs/tb/tb60.pdf ; form: https://nj.gov/treasury/taxation/pdf/other_forms/misc/c9600.pdf
  - **Action:** make the APA closing conditional on the Division's response or clearance, and hold back the escrow the Division specifies.
- **Sales tax on the equipment purchase itself:** a bulk transfer of business assets outside the ordinary course is treated as a **casual (isolated) sale, not subject to NJ sales tax** (motor vehicles excepted; they are taxed at MVC titling). https://www.salestaxinstitute.com/resources/new-jersey-sale-exempt-bulk-sale (summarizes a 2004 Division letter). **[VERIFY with counsel]**
- **Realty transfer tax (RTT)/mansion tax:** applies only to deeds for real property. Not applicable to a leasehold business with no real estate conveyed. An **assignment of lease** is generally not subject to RTT. The NJ **controlling-interest transfer tax** applies only to entities owning commercial real property (not applicable). **[VERIFY if the lease is >99 years or includes a purchase option]**
- No separate NJ tax on transfers of business personal property beyond the above.
- **Deal-structure note:** an **asset purchase** (a new LLC buys the assets) avoids inheriting the seller's entity liabilities and gives a stepped-up basis. A purchase of the seller's LLC interests would carry over basis (no bonus) and inherit liabilities.

---

## 8. Jersey City specifics

### 8a. Jersey City Payroll Tax (Employer Payroll Tax, 2019 onward)
- **1% of gross payroll**, paid by the employer (not withheld). It covers for-profit employers with services performed in Jersey City (or supervised from JC).
- **Threshold:** applies once quarterly gross payroll reaches **$2,500**. Above the threshold all wages are taxable, not only the excess. Employers below it must still register.
- **Exclusion:** wages of **JC-resident** employees (zip codes 07302, 07304–07307, 07310–07311). Keep written residency documentation.
- Quarterly returns are due Apr 30 / Jul 31 / Oct 31 / Jan 31 through the HLS portal (https://apps.hlssystems.com/JerseyCity/FilePayrollTax). Interest is 8% on the first $1,500 delinquent and 18% above that.
- **Owner draws of a partnership LLC are not wages**, so they are not subject to it. An S-corp owner salary is.
- Sources: https://taxnews.ey.com/news/2019-0761-jersey-city-new-jersey-quarterly-reporting-form-and-frequently-asked-questions-released ; https://www.ontheclock.com/help/jersey-city-employer-tax-filing
- **Budget impact:** $150k payroll with no JC-resident staff costs $1,500/yr.

### 8b. Other NJ payroll costs (for the payroll model)
- **NJ minimum wage 2026: $15.92/hr** (seasonal/small employers with <6 employees: $15.23). It indexes again Jan 1, 2027. https://njbiz.com/new-jersey-sets-15-92-minimum-wage-for-2026/
- **NJ employer UI/DI/WF** (calendar 2026): taxable wage base **$44,800**; 2027 wage base **$46,400**.
  - New-employer rates (FY Jul 2026–Jun 2027): **UI 2.6825%**, **DI 0.5%**, **WF/SWF 0.1175%**, a combined ~3.30% on the first $44,800 per employee (about $1,478 per employee who earns at least the base).
  - Employee withholdings: UI 0.3825%, DI 0.19%, FLI 0.23%, WF 0.0425%.
  - https://www.nj.gov/labor/ea/employer-services/rate-info
- **Federal:** FICA 7.65% employer share; FUTA 0.6% on the first $7,000 (no NJ credit reduction expected **[VERIFY]**).
- **Workers' compensation insurance is mandatory** in NJ for any employee (laundromat class rates typically ~$1–3 per $100 payroll **[VERIFY quote]**).
- **NJ Earned Sick Leave:** 1 hr per 30 hrs worked, up to 40 hrs/yr, for all employers.
- No health insurance mandate under 50 FTEs (ACA). NJ has no state employer health mandate; NJ residents face an individual mandate.
- **NJ Secure Choice retirement:** employers with **25+** employees that don't offer a plan must enroll employees (not applicable to a typical laundromat). **[VERIFY threshold]**

### 8c. Licensing / permits in Jersey City
- Jersey City has **no general business/mercantile license**. Licenses are activity-specific: Division of Commerce, Health Department (which includes **vending machines**), and Infrastructure.
- A **new owner should confirm**:
  - zoning use (Zoning Determination Letter),
  - the existing **Certificate of Occupancy** via OPRA, and
  - open violations on the property, which stay with the property.
- A new CO is needed only for a change of use or major renovation. Plumbing, electrical or gas work for machine replacement requires construction permits (licensed master plumber/electrician).
  - https://www.jerseycitynj.gov/cityhall/HousingAndDevelopment/businesses
- **[VERIFY]**: I could not find a Jersey City laundromat-specific license ordinance. Some NJ towns, for example Irvington ($888 initial / $347 per year), have one. Call JC Division of Commerce at (201) 547-5578 to confirm.
- State registrations: NJ-REG (sales tax, withholding, UI); DORES annual report; NJ BPU/PSE&G accounts; possibly NJDEP if dry-cleaning solvents are used (not applicable to wet laundry).

### 8d. Property tax pass-through via the lease
- The tenant does not pay property tax directly. A typical NNN or modified-gross retail lease passes a **pro-rata share of real estate taxes** (often as increases over a base year) plus CAM and insurance.
- Jersey City completed a citywide revaluation in 2017–2018 and 2024 **[VERIFY]**. School-funding changes (S2 cuts) drove sharp JC school-tax increases in 2022–2025. **Model 3–5%/yr tax escalations**, and read the lease's tax clause: base year, gross-up, and whether appeal refunds pass through.
- Also check whether the landlord can pass through **PILOT** or special-improvement-district (SID) assessments.

### 8e. Urban Enterprise Zone (Jersey City UEZ)
- Jersey City has a UEZ, administered by the JC Economic Development Corp. A 2021 reform (P.L. 2021, c.? **[VERIFY]**) keeps existing zones designated for 10 years. https://www.jcedc.org/urbanenterprisezonefunding ; https://scarincihollenbeck.com/law-firm-insights/nj-revamped-uez-program
- **Benefits for a certified UEZ business located in the zone:**
  - **Reduced sales tax of 3.3125%** (half rate) on **tangible personal property** sold at the in-zone location (detergent and vending items). It does **not** affect exempt laundry receipts. Whether it extends to taxable *services* such as linen laundering is unclear **[VERIFY]**.
  - **UZ-5 exemption** on purchases of most TPP and services for use at the zone location, up to **$100,000 per calendar year** (since Jan 1, 2022). This could save 6.625% on new machines and parts (~$6,625 on $100k).
  - UZ-4 contractor exemption on construction materials for the zone location, also capped at $100k/yr except for substantial-improvement projects.
  - https://www.nj.gov/treasury/taxation/uezcer.shtml
- **Action:** check whether the store address is inside the JC UEZ boundary, and apply for certification *before* buying replacement machines. Certification typically requires a minimum share of full-time employees from the zone or city and good tax standing. **[VERIFY current criteria]**

---

## 9. Structure implications (cross-reference for the personal-structure thread)
- **Best tax fit (preliminary):** a **multi-member LLC taxed as a partnership** (buyer plus parents, or a parent holding LLC) that buys the assets directly from the seller with parent-contributed cash.
  - Lets depreciation be specially allocated (with economic effect) to whichever owner can use it.
  - Lets the active buyer meet material participation (500+ hrs) so his share is non-passive.
  - The parents' share is passive. It is usable against their passive income, carried forward otherwise, and fully released on sale. NIIT applies on their share of profits.
  - NJ: the partnership category nets with the parents' other partnership K-1s. Filing fee is $0 with ≤2 owners and $150/owner with 3+.
- **Gifting cash or units** to the buyer: Form 709 above $19k per donor per donee. No tax up to the $15M lifetime exemption. Gifting LLC units later at a valuation discount is possible.
- **Avoid:** parents buying the assets in their own names and re-contributing them (loses bonus because of carryover basis). Avoid buying from a related party.
- **S-corp:** consider later, once profit to the working owner is high enough that payroll-tax savings exceed the costs (reasonable salary, JC 1% payroll tax, NJ UI, CBT minimum, loss of special allocations).
- **Equipment financing:** interest is deductible as business interest. The Sec. 163(j) small-business exemption applies under ~$31M receipts. Debt-financed equipment still gets 100% bonus. Partnership recourse/qualified debt adds basis and at-risk; nonrecourse may not add at-risk.

## 10. Open items / verify list
1. 5-yr (57.0) vs 7-yr for washers/dryers: confirm the CPA's position. App. B text could not be pulled.
2. Whether the EBL carryover is treated as an NOL or remains an EBL under the enacted OBBBA.
3. The NJ BAIT 9.12% tier, the $75 LLC annual-report fee, the ABC carryforward period, and the 2026 NJ bracket source.
4. Whether a JC laundromat-specific license exists; whether the store sits in the UEZ boundary and UEZ certification criteria.
5. Sales tax on pickup/delivery charges for exempt clothing service; sales tax on detergent consumed in WDF.
6. The lease tax-escalation clause and the JC tax trend.
