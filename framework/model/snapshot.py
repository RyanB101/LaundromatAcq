"""Runs scenario/sensitivity cases through LibreOffice and pastes a static table onto the Summary sheet.
Run after build_model.py:  python3 snapshot.py ../deals/<deal>/deal.json [recalc.py]
Cases: a generic set (offers at 90% / 80% of price, capex scenarios, utility and revenue stress, owner hours,
no renewal), the deal's bear/base/bull from deal.json "cases", then deal.json "snapshot_extra" ([label, overrides]).
"""
import json, os, shutil, subprocess, sys, tempfile
from openpyxl import load_workbook
from openpyxl.styles import Font

DEAL_PATH = os.path.abspath(sys.argv[1])
HERE = os.path.dirname(DEAL_PATH)
DEAL = json.load(open(DEAL_PATH))
XL = os.path.join(HERE, DEAL.get("output", "Underwriting_Model.xlsx"))
META = json.load(open(XL + ".meta.json"))
RECALC = sys.argv[2] if len(sys.argv) > 2 else "/mnt/skills/public/xlsx/scripts/recalc.py"
IN = DEAL["inputs"]
P = IN["Price"]
_C = DEAL.get("cases", {})
PLAN = _C.get("plan", {})
CASES = [
    (f"Base: ask ${P:,.0f}, keep & repair machines", {}),
    (f"Offer ${round(P * 0.9, -4):,.0f} (90% of ask)", {"Price": round(P * 0.9, -4)}),
    (f"Offer ${round(P * 0.8, -4):,.0f} (80% of ask)", {"Price": round(P * 0.8, -4)}),
    ("Replace washers at close (scenario 2)", {"CapexScenario": 2}),
    ("Full retool at close (scenario 3)", {"CapexScenario": 3}),
    ("Machines fail early (scenario 4)", {"CapexScenario": 4}),
    ("Utilities +20% vs. the P&L", {"WaterYr1": IN["WaterYr1"] * 1.2, "GasElecYr1": IN["GasElecYr1"] * 1.2}),
    ("Revenue 10% below the P&L", {"SelfServe": IN["SelfServe"] * 0.9, "WFLbsMonth": IN["WFLbsMonth"] * 0.9}),
    ("Ryan works 0 hrs (fully absentee)", {"OwnerHours": 0}),
    ("No lease renewal (exit value $0)", {"ExitMult": 0}),
] + ([("Ryan's plan (owner hours, day manager)", dict(PLAN))] if PLAN else []) + [
    ("BEAR case (cases.py)", dict(PLAN, **_C.get("bear", {}))),
    ("BASE case (cases.py)", dict(PLAN)),
    ("BULL case (cases.py)", dict(PLAN, **_C.get("bull", {}))),
] + [(lbl, o) for lbl, o in DEAL.get("snapshot_extra", [])]

def refs(wb):
    out = {}
    for n, dn in wb.defined_names.items():
        sheet, cell = dn.attr_text.split("!")
        out[n] = (sheet, cell.replace("$", ""))
    return out


def run_case(over):
    wb = load_workbook(XL)
    rf = refs(wb)
    for k, v in over.items():
        sh, cell = rf[k]
        wb[sh][cell] = v
    tmp = tempfile.mkdtemp()
    p = os.path.join(tmp, "case.xlsx")
    wb.save(p)
    subprocess.run([sys.executable, RECALC, p, "90"], check=True, capture_output=True)
    v = load_workbook(p, data_only=True)
    sr, pj, stc = v["Seller Recast"], v["Projection"], v["Structures"]
    res = {
        "noi": sr[f"D{META['noi_row']}"].value,
        "irr": pj[f"C{META['irr_row']}"].value,
        "npvA": stc[f"C{META['comp']['A']}"].value,
        "irrA": stc[f"D{META['comp']['A']}"].value,
        "npvB": stc[f"C{META['comp']['B']}"].value,
        "npvC": stc[f"C{META['comp']['C']}"].value,
        "npvD": stc[f"C{META['comp']['D']}"].value,
    }
    shutil.rmtree(tmp)
    return res


rows = [(lbl, run_case(o)) for lbl, o in CASES]
wb = load_workbook(XL)
sm = wb["Summary"]
r = META["snap_row"] + 1
heads = ["Case", "Yr-1 NOI", "Pre-tax IRR", "A: NPV", "A: IRR", "B: NPV", "C: NPV", "D: NPV"]
for j, h in enumerate(heads):
    sm.cell(r, 2 + j, h).font = Font(name="Arial", bold=True, size=10)
r += 1
fmts = ['$#,##0;($#,##0)', '0.0%', '$#,##0;($#,##0)', '0.0%', '$#,##0;($#,##0)', '$#,##0;($#,##0)', '$#,##0;($#,##0)']
for lbl, res in rows:
    sm.cell(r, 2, lbl).font = Font(name="Arial", size=10)
    for j, k in enumerate(("noi", "irr", "npvA", "irrA", "npvB", "npvC", "npvD")):
        c = sm.cell(r, 3 + j, res[k])
        c.number_format = fmts[j]
        c.font = Font(name="Arial", size=10)
    r += 1
sm.cell(r, 2, "Static values from snapshot.py; each case changes only the listed inputs from the base. NPV at the Inputs discount rate.").font = Font(name="Arial", italic=True, size=9, color="595959")
sm.column_dimensions["G"].width = 14
sm.column_dimensions["H"].width = 14
sm.column_dimensions["I"].width = 14
wb.save(XL)
subprocess.run([sys.executable, RECALC, XL, "90"], check=True)
for lbl, res in rows:
    print(lbl, {k: (round(v, 3) if isinstance(v, float) else v) for k, v in res.items()})
