# Running the model on a new listing

Five scripts, all driven by one `deal.json` per deal. The Tumble Wash deal file (`../deals/tumble-wash/deal.json`) is a complete, working example: rebuilt through these scripts, it reproduces the original Tumble Wash workbook, cases and structure results exactly.

| Script | What it does | Writes (into the deal folder) |
|---|---|---|
| `equipment_model.py` | Repair vs. replace for the fleet, after tax; builds the 4 capex scenarios | `capex_scenarios.json`, `capex_schedule.csv`, `strategy_summary.csv` |
| `build_model.py` | Builds the Excel underwriting model (Summary, Seller Recast, Valuation, Projection, Structures, Depreciation, Comps, Inputs) | `<output>.xlsx` + `.meta.json` |
| `cases.py` | Bear / base / bull and a forced sale after Year 1 | `cases.json` |
| `structure_e.py` | Family partnership (structure E, E1/E2, with and without Ryan's S corp) vs. the AFR-loan structure D, plus a bad-Year-1 sale | `structure_e.json` |
| `snapshot.py` | Runs a standard scenario set and pastes the results table onto the Summary sheet | updates the `.xlsx` |

**Needs:** Python 3 with `openpyxl`, and LibreOffice for recalculation. `cases.py`, `structure_e.py` and `snapshot.py` take the recalc script as an optional last argument; the default is the xlsx skill's `/mnt/skills/public/xlsx/scripts/recalc.py`, which exists in Claude sessions.

## Steps

1. **Copy the template:** `cp -r deals/_template deals/<short-name>` (from `framework/`).
2. **Fill `deal.json`** from the listing and the broker P&L (README steps 1–2). Every `null` must be replaced; the build stops and lists any it finds. All money is annual unless the name says otherwise.
   - `horizon_years`: remaining lease years you can count on (3–20). The projection, depreciation and exit all key off it.
   - `inputs`: the required inputs, plus any generic default you want to change (full list below).
   - `notes`: optional text shown next to an input on the Inputs sheet (sources, caveats).
   - `broker_pnl`: the broker's annual amount for each line (keys: `ss wf anc rent wages burden water gas rep ins card pos wfs cogs tel misc pro lic psvc mkt cont`), an optional `why` per line, and the broker's `stated_noi`. Lines you leave out count as $0.
   - `comps`: `[location, price, gross, cash flow, notes, status, source]`, subject first. `benchmarks_extra` adds rows to the Comps sheet's benchmark list.
   - `valuation`: offer and walk-away multiples of underwritten NOI (default 3.0x / 3.5x) and the market multiples shown.
   - `cases`: `plan` (Ryan's hours plan, applied to every case), `bear` and `bull` overrides. `snapshot_extra`: more `[label, {overrides}]` rows for the Summary table.
   - Optional: `equipment` (overrides `equipment_model.py` assumptions, e.g. `{"disc": 0.08, "bear_age_shift": 3}`), `structure` (`pref`, `ryan_split`, `scorp_salary_later`), `forced_sale` (multiples and selling costs).
3. **Fill `fleet_inputs.csv`:** one row per machine type and size, with count, age (from serial numbers), installed replacement cost (distributor quote), useful life (washers 15–18, dryers ~25), repair, revenue and utility per unit. `kind` is `washer` or `dryer`.
4. **Run, from the deal folder:**
   ```
   python3 ../../model/equipment_model.py deal.json
   python3 ../../model/build_model.py deal.json
   python3 ../../model/cases.py deal.json
   python3 ../../model/structure_e.py deal.json
   python3 ../../model/snapshot.py deal.json
   ```
   `build_model.py` must run after `equipment_model.py` (it reads `capex_scenarios.json`) unless `deal.json` has its own `capex_scenarios`. The other three need the built workbook. `snapshot.py` takes a few minutes (one LibreOffice recalculation per case).
5. **Read the Summary sheet first**, then Seller Recast (where the broker's numbers changed and why), then Valuation.

## Things the model assumes
- **State tax logic is New Jersey's:** state depreciation allows only the `NJ179` Section 179 cap and no bonus, and business losses don't offset wages. For a state that follows federal bonus, set `NJ179` very high (e.g. 10,000,000) and set `RyanNJ` / `ParentNJ` to that state's rates. Local payroll taxes sit inside `Burden` and `SCorpPayroll`.
- Tax figures are 2026 (`EBLSingle`, `SSBase`, annual exclusion, AFR). Update them each year.
- NOI is absentee: every attended hour is paid. SDE adds back the hours Ryan works himself (`OwnerHours`, `OwnerHoursLater` after `HandoffYear`).
- Structures A–D are on the Structures sheet; the standing structure (E1 + Ryan's S corp) is computed by `structure_e.py`, which reads the model's yearly lines. E uses `LoanAmt` as the parents' capital contribution.
- `equipment_model.py` stops replacing machines in the last 3 lease years and keeps repairing instead. Scenario 4 (bear) is "run to failure" with every machine `bear_age_shift` years older than stated.

## Input reference
Inputs marked required have no generic default. Everything else can be overridden in `deal.json` `inputs`.

| Name | Input | Default |
|---|---|---|
| **Deal** | | |
| `Price` | Purchase price | **required** |
| `ClosingCosts` | Closing costs (legal, accounting/QoE, inspection, bulk-sale filing) | $20,000 |
| `WorkingCap` | Opening working capital (card float, supplies, cash reserve) | $10,000 |
| `AllocEquip` | Form 8594 allocation: machines, card system, ATM, vending (Class V) | **required** |
| `AllocLHI` | Form 8594 allocation: leasehold improvements (curbs, tile, plumbing troughs, venting) | **required** |
| `AllocNoncompete` | Form 8594 allocation: seller non-compete | **required** |
| **Revenue (Year 1, annual, from the broker P&L unless noted)** | | |
| `SelfServe` | Self-serve washer/dryer revenue | **required** |
| `WFLbsMonth` | Wash-dry-fold pounds per month | **required** |
| `WFPrice` | Wash-dry-fold price per lb (Year 1) | **required** |
| `WFPriceNew` | Wash-dry-fold price per lb after increase | **required** |
| `WFPriceYear` | Year the W&F price increase takes effect | 2 |
| `WFVolLoss` | W&F volume lost when price rises | 10.00% |
| `DryClean` | Drop-off dry cleaning revenue | $0.00 |
| `ATM` | ATM revenue | $0.00 |
| `SoapVend` | Soap vending revenue | $0.00 |
| `SnackVend` | Snack/soda vending revenue | $0.00 |
| `GameVend` | Game (quarter pusher / arcade) revenue | $0.00 |
| `AncRealize` | Share of ancillary (non-laundry) revenue underwritten | 85.00% |
| `SSGrowth` | Self-serve revenue growth per year (price + volume) | 3.00% |
| `WFGrowth` | W&F revenue growth per year after the step-up | 3.00% |
| `AncGrowth` | Ancillary revenue growth per year | 2.00% |
| `RetoolLift` | Self-serve revenue lift from a fully new washer/dryer fleet | 5.00% |
| **Operating expenses (Year 1)** | | |
| `RentYr1` | Rent incl. NNN, CAM and any utilities the lease covers (annual) | **required** |
| `RentEsc` | Rent escalation per year | 3.00% |
| `PaidHours` | Paid attendant hours per week (absentee model) | **required** |
| `Wage` | Attendant wage per hour (Year 1) | $17.50 |
| `WageGrowth` | Wage growth per year | 3.50% |
| `Burden` | Employer payroll burden (FICA, FUTA, state UI/DI, local payroll tax, workers' comp, sick leave) | 16.00% |
| `WaterYr1` | Water and sewer (annual) | **required** |
| `GasElecYr1` | Gas + electric (annual) | **required** |
| `ElecExtra` | Additional electric not in the broker P&L (annual) | $0.00 |
| `UtilCont` | Utility contingency (unverified bills) | 10.00% |
| `UtilInfl` | Utility cost inflation per year | 4.00% |
| `UtilSave` | Utility saving with a fully new fleet | 20.00% |
| `RepairsYr1` | Repairs & maintenance, current fleet (Year 1) | **required** |
| `RepairsAging` | Repair cost growth per year while fleet ages | 8.00% |
| `RepairsNewPct` | Repairs on a new fleet, % of revenue | 2.00% |
| `Insurance` | Insurance: property, GL, equipment breakdown, umbrella | $7,500 |
| `CardFeePct` | Card processing fees, % of laundry revenue | 1.50% |
| `POS` | POS / card system fees | $0.00 |
| `WFSupplyLb` | W&F supplies per lb | $0.04 |
| `VendCOGS` | Vending COGS, % of soap + snack revenue | 34.00% |
| `DCCost` | Dry cleaning cost, % of dry cleaning revenue | 50.00% |
| `TeleAlarmTrash` | Phone/Wi-Fi, alarm, fire alarm, trash | $2,500 |
| `MiscSupplies` | Misc. supplies | $1,800 |
| `ProFees` | Accounting, tax prep, legal | $5,000 |
| `Licenses` | Licenses, LLC annual report, vending/health permits | $1,000 |
| `PayrollSvc` | Payroll service | $1,200 |
| `Marketing` | Marketing (Google profile, signage, flyers, W&F promos) | $3,000 |
| `ContPct` | General contingency, % of revenue | 1.00% |
| `ExpInfl` | General expense inflation | 3.00% |
| **Owner time (Ryan)** | | |
| `OwnerHours` | Hours per week Ryan works in the store (replacing paid attendants) | 40 |
| **Owner hand-off and delivery/commercial growth (defaults = off; see Summary scenario table)** | | |
| `HandoffYear` | Year Ryan steps back to a management role | 2 |
| `OwnerHoursLater` | Ryan's hours per week in the store after the hand-off | 40 |
| `MgrHours` | Day-manager hours per week (lead attendant who covers Ryan's shifts) from hand-off | 0 |
| `MgrPremium` | Day-manager pay premium over attendant wage, per hour | $4.50 |
| `DelivStart` | First year of the pickup/delivery + commercial program | 2 |
| `DelivLbsRamp` | Delivery/commercial pounds per month, first year | 0 |
| `DelivLbsFull` | Delivery/commercial pounds per month, later years | 0 |
| `DelivPrice` | Delivery/commercial price per lb | $1.95 |
| `LbsPerHour` | Pounds processed (wash, dry, fold) per labor hour | 30 |
| `DelivLaborShare` | Share of processing labor that is new paid hours (rest absorbed by idle attendant time) | 60.00% |
| `DelivUtilLb` | Utilities per lb processed | $0.10 |
| `DriverHours` | Driver hours per week once the program runs | 20 |
| `DriverWage` | Driver wage per hour | $20.00 |
| `VehicleCost` | Van lease, fuel, commercial auto insurance per year | $12,000 |
| **Equipment capital plan** | | |
| `CapexScenario` | Capex scenario (1 = keep & repair; 2 = washers now; 3 = full retool at close; 4 = bear: machines fail early). See Depreciation sheet. | 1 |
| `CapexInfl` | Equipment price inflation per year (capex schedule is in today's dollars) | 3.00% |
| `EquipLife` | Federal/state MACRS recovery period for machines (5 or 7) | 5 |
| `Bonus` | Federal bonus depreciation % | 100.00% |
| `NJ179` | State Section 179 limit per year (NJ: $25k, no bonus) | $25,000 |
| **Tax rates and limits** | | |
| `RyanFed` | Ryan: federal marginal income tax rate | 22.00% |
| `RyanNJ` | Ryan: state marginal rate | 6.37% |
| `RyanOtherInc` | Ryan: other income available to absorb business losses (federal) | $50,000 |
| `EBLSingle` | Excess business loss limit, single | $256,000 |
| `SSBase` | Social Security wage base | $184,500 |
| `QBIRate` | QBI deduction rate (Sec. 199A) | 20.00% |
| `ParentFed` | Parents: federal marginal rate | 37.00% |
| `NIIT` | Net investment income tax on passive income | 3.80% |
| `ParentNJ` | Parents: state marginal rate | 8.97% |
| `ParentPassive` | Parents: other net passive income each year (structure C only) | $250,000 |
| `ParentNJBiz` | Parents: other state partnership/business income for netting (structure C only) | $250,000 |
| `ExitTax` | Blended tax rate on exit proceeds | 30.00% |
| **Family capital (structure D loan terms; structure E uses the same amount as parents' capital)** | | |
| `LoanAmt` | Parents' funding (D: AFR loan to Ryan's LLC; E: capital into OpCo) | price + $50,000 |
| `LoanRate` | Loan interest rate (AFR) | 4.61% |
| `LoanForgive` | Principal forgiven each year (annual-exclusion gifts) | $38,000 |
| `SCorpYear` | First year taxed as an S-corp | 2 |
| `RyanSalary` | Ryan's reasonable salary from the S-corp (Year of election) | $60,000 |
| `SCorpPayroll` | Payroll taxes on Ryan's salary (FICA both halves + state UI/DI + local payroll tax) | 18.30% |
| **Valuation** | | |
| `DiscRate` | Discount rate (after-tax, all-cash equity) | 10.00% |
| `PreTaxTarget` | Target pre-tax unlevered return for max-price test | 15.00% |
| `ExitMult` | Exit value at end of Year N, multiple of Year-N EBITDA | 1.5 |
