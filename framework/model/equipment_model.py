"""Repair-vs-replace model for a laundromat fleet.
Put fleet_inputs.csv (one row per machine type) in the deal folder, optionally override the
assumptions below with an "equipment" block in deal.json, then run:
    python3 equipment_model.py ../deals/<deal>/deal.json
Writes into the deal folder: strategy_summary.csv, capex_schedule.csv, and capex_scenarios.json
(the 4 capex scenarios build_model.py reads)."""
import csv, json, os, sys
if len(sys.argv) < 2:
    sys.exit("usage: python3 equipment_model.py <path to deal.json>")
DEAL_PATH = os.path.abspath(sys.argv[1])
HERE = os.path.dirname(DEAL_PATH)  # deal folder: inputs read from and outputs written to here
DEAL = json.load(open(DEAL_PATH))
A = dict(
    horizon=17,            # years left on lease (taken from deal.json horizon_years)
    disc=0.08,             # discount rate (all-cash, cost of equity)
    fed_rate=0.37,         # federal marginal rate (only usable if losses aren't suspended as passive)
    nj_rate=0.0897,        # NJ GIT bracket $500k-$1M
    repair_growth=0.08,    # repair cost grows 8%/yr of machine age (calibrated to ~$8k/yr today vs P&L $5.4k maintenance)
    downtime_per_repair_dollar=0.6,  # lost revenue per $1 repair spend (older machines sit broken)
    new_utility_savings=0.25,        # water/energy saving of new vs ~12yr-old washers
    new_revenue_uplift=0.10,         # vend price uplift on washers after retool (CLA: customers pay 10-20% more for updated equipment)
    salvage_old_pct=0.05,            # what old machines fetch when pulled
    residual_used_pct=0.35,          # value of remaining life at lease end/exit (used-market haircut)
    nj_179=25000,                    # NJ GIT Sec.179 cap; rest on 5-yr MACRS (NJ decoupled from bonus)
    bear_age_shift=3,                # bear scenario: machines behave this many years older than stated
)
if not DEAL.get("horizon_years"):
    sys.exit("deal.json needs horizon_years (remaining lease years you can count on)")
A["horizon"] = int(DEAL["horizon_years"])
A.update(DEAL.get("equipment", {}))
MACRS5 = [0.20, 0.32, 0.192, 0.1152, 0.1152, 0.0576]

def load():
    with open(os.path.join(HERE, "fleet_inputs.csv")) as f:
        return [dict(r, **{k: float(r[k]) for k in r if k not in ("machine_type", "kind")}) for r in csv.DictReader(f)]

def tax_shield(capex_by_year, A):
    """Federal: 100% bonus in year bought (OBBBA, permanent). NJ: $25k 179 then 5-yr MACRS."""
    shield = [0.0] * (A["horizon"] + 6)
    for y, c in enumerate(capex_by_year):
        if c <= 0: continue
        shield[y] += c * A["fed_rate"]
        e179 = min(c, A["nj_179"]); shield[y] += e179 * A["nj_rate"]
        for i, p in enumerate(MACRS5):
            shield[y + i] += (c - e179) * p * A["nj_rate"]
    return shield

def run(fleet, strategy, A):
    H = A["horizon"]
    capex = [0.0] * (H + 1); opex = [0.0] * (H + 1); terminal = 0.0
    for m in fleet:
        replace_now = strategy == "retool_now" or (strategy == "washers_now" and m["kind"] == "washer")
        for _ in range(int(m["count"])):
            age = 0.0 if replace_now else m["est_age_yrs"]
            if replace_now:
                capex[0] += m["replace_cost_installed"] - m["replace_cost_installed"] * A["salvage_old_pct"] * 0.5
            for y in range(1, H + 1):
                if age >= m["useful_life_yrs"] and y <= H - 3:  # replace like-for-like; in last 3 lease yrs keep repairing
                    capex[y] += m["replace_cost_installed"]; age = 0.0
                repair = m["annual_repair_new"] * (1 + A["repair_growth"]) ** age
                downtime = repair * A["downtime_per_repair_dollar"]
                new = age < 8
                util = m["annual_utility_per_unit"] * (1 - A["new_utility_savings"] if (new and m["kind"] == "washer") else 1)
                uplift = m["annual_revenue_per_unit"] * A["new_revenue_uplift"] if (new and m["kind"] == "washer") else 0
                opex[y] += repair + downtime + util - uplift
                age += 1
            remaining = max(0.0, m["useful_life_yrs"] - age) / m["useful_life_yrs"]
            terminal += remaining * m["replace_cost_installed"] * A["residual_used_pct"]
    shield = tax_shield(capex, A)
    d = lambda y: (1 + A["disc"]) ** -y
    pv_capex = sum(c * d(y) for y, c in enumerate(capex))
    pv_opex = sum(o * d(y) for y, o in enumerate(opex))
    pv_term = terminal * d(H)
    pv_shield = sum(s * d(y) for y, s in enumerate(shield))
    # opex is deductible too
    pv_opex_at = pv_opex * (1 - A["fed_rate"] - A["nj_rate"])
    return dict(strategy=strategy, capex_total=round(sum(capex)), capex_yr0=round(capex[0]),
                pv_capex=round(pv_capex), pv_opex_net=round(pv_opex), pv_terminal=round(pv_term),
                pv_cost_pretax=round(pv_capex + pv_opex - pv_term),
                pv_tax_shield_capex=round(pv_shield),
                pv_cost_aftertax=round(pv_capex - pv_shield + pv_opex_at - pv_term)), capex

if __name__ == "__main__":
    fleet = load()
    rows, sched = [], {}
    for s in ("run_to_failure", "washers_now", "retool_now"):
        r, c = run(fleet, s, A); rows.append(r); sched[s] = c
    with open(os.path.join(HERE, "strategy_summary.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    with open(os.path.join(HERE, "capex_schedule.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["year"] + list(sched))
        for y in range(A["horizon"] + 1): w.writerow([y] + [round(sched[s][y]) for s in sched])
    # 4 scenarios for build_model.py: 1-3 = the strategies above; 4 = bear (run to failure, fleet older than stated)
    bear = run([dict(m, est_age_yrs=m["est_age_yrs"] + A["bear_age_shift"]) for m in fleet], "run_to_failure", A)[1]
    def first_years(c):
        return ", ".join(f"yr {y}" for y, v in enumerate(c) if v > 0) or "none"
    scen = [("Keep & repair; replace as machines wear out", sched["run_to_failure"]),
            ("Washers at close; dryers as they wear out", sched["washers_now"]),
            ("Full retool at close", sched["retool_now"]),
            (f"Bear: fleet {A['bear_age_shift']} yrs older than stated", bear)]
    out = [{"label": f"{lbl} ({first_years(c)})", "by_year": {str(y): round(v) for y, v in enumerate(c) if v > 0}} for lbl, c in scen]
    json.dump(out, open(os.path.join(HERE, "capex_scenarios.json"), "w"), indent=1)
    for r in rows: print(r)
    # sensitivity on revenue uplift and fleet age
    for up in (0.0, 0.05, 0.10):
        for age in (6, 12, 18):
            A2 = dict(A, new_revenue_uplift=up)
            fl = [dict(m, est_age_yrs=age) for m in fleet]
            res = {s: run(fl, s, A2)[0]["pv_cost_aftertax"] for s in ("run_to_failure", "washers_now", "retool_now")}
            print(f"uplift {up:.0%} age {age}: " + ", ".join(f"{k} {v:,}" for k, v in res.items()))
