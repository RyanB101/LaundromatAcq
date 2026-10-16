"""Bear / base / bull cases and a forced early sale. Run: python3 cases.py <recalc.py>
Writes cases.json and prints a summary. Each case = overrides of Inputs (named ranges)."""
import json, os, shutil, subprocess, sys, tempfile
from openpyxl import load_workbook
HERE = os.path.dirname(os.path.abspath(__file__))
XL = os.path.join(HERE, "Tumble_Wash_Underwriting_Model.xlsx")
META = json.load(open(XL + ".meta.json")); RECALC = sys.argv[1]
PLAN = {"OwnerHours": 22, "OwnerHoursLater": 10, "MgrHours": 40}  # Ryan: ~22 hrs/wk Yr 1, ~10 after, day manager
CASES = {
 "bear": dict(PLAN, SelfServe=194400, SSGrowth=0.02, WFLbsMonth=7200, WFPriceNew=1.40, AncRealize=0.7,
              ElecExtra=12000, RepairsYr1=15000, CapexScenario=4, RetoolLift=0.0, ExitMult=1.5),
 "base": dict(PLAN),
 "bull": dict(PLAN, UtilCont=0, AncRealize=1.0, WFPriceNew=1.65, SelfServe=226800, SSGrowth=0.035, RepairsYr1=8000,
              DelivLbsRamp=1500, DelivLbsFull=4000, RetoolLift=0.10, ExitMult=2.5),
}
def run(over):
    wb = load_workbook(XL)
    rf = {n: (d.attr_text.split("!")[0], d.attr_text.split("!")[1].replace("$", "")) for n, d in wb.defined_names.items()}
    for k, v in over.items(): wb[rf[k][0]][rf[k][1]] = v
    t = tempfile.mkdtemp(); p = os.path.join(t, "c.xlsx"); wb.save(p)
    subprocess.run([sys.executable, RECALC, p, "90"], check=True, capture_output=True)
    v = load_workbook(p, data_only=True); pj, st = v["Projection"], v["Structures"]
    row = lambda r: [pj.cell(r, c).value for c in range(3, 21)]  # yr0..yr17
    lab = {pj.cell(r, 2).value: r for r in range(5, 90) if pj.cell(r, 2).value}
    g = lambda name: row(lab[name])
    out = dict(rev=g("Total revenue"), noi=g("EBITDA / net operating income (absentee)"),
               sde=g("Owner-operator cash flow (SDE) = EBITDA + Ryan's hours"), capex=g("Equipment capex (selected scenario)"),
               irr=pj[f"C{META['irr_row']}"].value,
               npvD=st[f"C{META['comp']['D']}"].value, irrD=st[f"D{META['comp']['D']}"].value,
               npvA=st[f"C{META['comp']['A']}"].value, irrA=st[f"D{META['comp']['A']}"].value)
    shutil.rmtree(t); return out
res = {k: run(o) for k, o in CASES.items()}
# Forced sale: decide ~month 6, close ~month 12 (laundromats take 3-9 months to sell).
EXIT = {"bear": (2.0, 2.5), "base": (2.75, 3.25), "bull": (3.25, 3.75)}  # quick-sale / likely multiple of buyer-verified absentee NOI
EQUIP_RECOVERY = 0.5
BUY_COSTS, WC, BROKER, SELL_LEGAL, RATE = 20000, 10000, 0.10, 7500, 0.22 + 0.0637
for k, r in res.items():
    noi1, sde1 = r["noi"][1], r["sde"][1]
    e = {}
    for tag, m in zip(("quick", "likely"), EXIT[k]):
        # Machines replaced before the sale (bear: washers die in yr 1) are cash out; a buyer pays back ~half via a higher price.
        capex_pre = -sum(r["capex"][:2])
        price = m * noi1 + EQUIP_RECOVERY * capex_pre
        fee = max(BROKER * price, 25000)
        proceeds = price - fee - SELL_LEGAL
        pretax = -(450000 + BUY_COSTS + WC) - capex_pre + sde1 + proceeds + WC
        e[tag] = dict(mult=m, capex_pre=capex_pre, price=price, fee=fee, proceeds=proceeds, pretax=pretax,
                      aftertax_approx=pretax * (1 - RATE) if pretax < 0 else pretax)
    r["exit"] = e
json.dump({"cases": CASES, "results": res}, open(os.path.join(HERE, "cases.json"), "w"), indent=1, default=float)
for k, r in res.items():
    continue
    print(k, "rev1", round(r["rev"][1]), "noi1", round(r["noi"][1]), "noi3", round(r["noi"][3]), "noi10", round(r["noi"][10]),
          "sde1", round(r["sde"][1]), "sde3", round(r["sde"][3]), "capex", round(-sum(r["capex"])), "irr", round(r["irr"], 3),
          "irrD", round(r["irrD"], 3) if isinstance(r["irrD"], float) else r["irrD"], "npvD", round(r["npvD"]), "irrA", r["irrA"])
    for tag, e in r["exit"].items(): print("   exit", tag, {a: round(b) if b > 100 else b for a, b in e.items()})
