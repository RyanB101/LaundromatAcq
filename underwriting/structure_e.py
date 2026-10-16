"""Structure E (family partnership, parents' capital + Ryan profits interest) vs D (Ryan's LLC, AFR loan, S-corp yr 2+).
Pulls yearly pre-tax inputs from the model (LibreOffice recalc), recomputes D with the model's own rules (checked
against the Structures sheet), computes E, and adds a bear-case early exit after Year 1.
Run:  python3 structure_e.py <recalc.py>      -> prints a summary and writes structure_e.json
"""
import json, os, shutil, subprocess, sys, tempfile
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
XL = os.path.join(HERE, "Tumble_Wash_Underwriting_Model.xlsx")
META = json.load(open(XL + ".meta.json"))
RECALC = sys.argv[1]
PLAN = dict(OwnerHours=22, OwnerHoursLater=10, MgrHours=40)
CASES = json.load(open(os.path.join(HERE, "cases.json")))["cases"]

# Tax parameters (model inputs, plus the structure thread's E spec)
R_FED, R_NJ, R_OTHER, EBL_S = 0.22, 0.0637, 50000, 256000
P_FED, P_NIIT, P_NJ = 0.37, 0.038, 0.0897
P_ORD = P_FED + P_NIIT                      # passive ordinary income/loss, federal
P_LTCG = 0.20 + P_NIIT                      # capital loss used against long-term gains
SS0, WG, QBI, EXIT_TAX, DISC = 184500, 0.035, 0.20, 0.30, 0.10
LOAN, RATE, FORGIVE, SAL, SCP = 500000, 0.0461, 38000, 60000, 0.183
PREF = 0.05; R_SPLIT = 0.80


def model_rows(over):
    wb = load_workbook(XL)
    for n, dn in wb.defined_names.items():
        if n in over:
            sh, c = dn.attr_text.split("!"); wb[sh][c.replace("$", "")] = over[n]
    t = tempfile.mkdtemp(); p = os.path.join(t, "c.xlsx"); wb.save(p)
    subprocess.run([sys.executable, RECALC, p, "120"], check=True, capture_output=True)
    st = load_workbook(p, data_only=True)["Structures"]
    row = lambda r: [st.cell(r, c).value or 0 for c in range(3, 21)]
    out = dict(ebitda=row(7), h=row(8), wages=row(9), fdep=row(10), njdep=row(11), cf=row(13), exitv=row(14),
               d_family=row(96), d_npv=st[f"C{META['comp']['D']}"].value)
    shutil.rmtree(t)
    return out


def npv(cfs, r=DISC):
    return sum(c / (1 + r) ** t for t, c in enumerate(cfs))


def se_tax(earn, y):
    if earn <= 0: return 0.0
    base = SS0 * (1 + WG) ** (y - 1)
    return min(earn * 0.9235, base) * 0.124 + earn * 0.9235 * 0.029


# ---------- D: same rules as the model's Structures sheet ----------
def run_D(m, last=17, scorp=True):
    fam, ryan, par = [m["cf"][0]], [20000.0], [-500000.0]
    bal, fcf, ncf = LOAN, 0.0, 0.0
    for y in range(1, last + 1):
        e, h, fd, nd = m["ebitda"][y], m["h"][y], m["fdep"][y], m["njdep"][y]
        intr = bal * RATE
        s = scorp and y >= 2
        sal = SAL * (1 + WG) ** max(0, y - 2) if s else 0
        inc = e + h - fd - intr
        emp = sal * (SCP - 0.0765)
        se = sal * SCP if s else se_tax(inc, y)
        qbi = max(0, inc - (sal + emp if s else se / 2)) * QBI
        ti = inc - (emp if s else se / 2) - qbi
        used = min(fcf, max(0, ti)); other = min(-ti, min(R_OTHER, EBL_S)) if ti < 0 else 0
        fcf = fcf - used + max(0, -ti) - other
        fed = (max(0, ti) - used - other) * R_FED
        nji = e + h - nd - intr - emp
        nused = min(ncf, max(0, nji)); ncf = ncf - nused + max(0, -nji)
        nj = (max(0, nji) - nused) * R_NJ
        tax = fed + se + nj
        ptax = intr * (P_ORD + P_NJ)
        xt = m["exitv"][y] * EXIT_TAX
        fam.append(m["cf"][y] + h - tax - ptax - xt)
        par.append(intr - ptax)
        ryan.append(m["cf"][y] + h - tax - intr - xt)
        bal = max(0, bal - FORGIVE)
    return dict(fam=fam, ryan=ryan, par=par, npv=npv(fam), npv_ryan=npv(ryan), npv_par=npv(par), nol_left=fcf)


# ---------- E: partnership, parents' capital, Ryan profits interest ----------
def run_E(m, last=17):
    """GP to Ryan = value of his hours (SE-taxable). Cash after GP: 5% cumulative pref to parents on unreturned capital,
    then 80/20. Shortfalls (capex years) are funded by parents as added capital. Tax: all fed/NJ depreciation and any
    net loss to parents; later income first charges back parents' cumulative net losses, then follows the cash split.
    Exit (yr 17): capital accounts first, then 80/20; exit tax at the model's flat 30%, borne pro rata to exit cash."""
    contrib = -m["cf"][0] + 20000
    fam, ryan, par = [-contrib], [0.0], [-contrib]          # $500k in, $480k spent, $20k stays as partnership cash
    cash = 20000.0
    cap_p, cap_r = contrib, 0.0            # book capital accounts (tax = book; cash contributions only)
    cb_f = cb_n = 0.0                      # parents' cumulative net loss not yet charged back (fed, NJ)
    pref_due = 0.0; min_cap_r = 0.0
    for y in range(1, last + 1):
        e, h, fd, nd = m["ebitda"][y], m["h"][y], m["fdep"][y], m["njdep"][y]
        capex = -(m["cf"][y] - e - m["exitv"][y] - (10000 if y == 17 else 0))  # capex this year (positive)
        # --- cash ---
        cash += e - capex                  # GP paid to Ryan out of e + h (store saves h in wages)
        add = max(0, -cash); cash += add; contrib += add; cap_p += add
        pref_due += PREF * contrib
        dist = cash if y < last else max(0, cash)
        pp = min(dist, pref_due); pref_due -= pp; rest = dist - pp
        dp, dr = pp + rest * (1 - R_SPLIT), rest * R_SPLIT
        cash -= dist
        # --- tax allocation (fed and NJ tracked separately) ---
        def alloc(inc_before_dep, dep, cb):
            sp = -dep; sr = 0.0
            x = max(0, inc_before_dep)
            c = min(x, cb); sp += c; cb -= c; x -= c
            pi = min(x, pp); sp += pi; x -= pi
            sp += x * (1 - R_SPLIT); sr += x * R_SPLIT
            if inc_before_dep < 0: sp += inc_before_dep
            if sp < 0: cb += -sp
            return sp, sr, cb
        spf, srf, cb_f = alloc(e, fd, cb_f)
        spn, srn, cb_n = alloc(e, nd, cb_n)
        cap_p += spf - dp; cap_r += srf - dr; min_cap_r = min(min_cap_r, cap_r)
        # Ryan: GP + distributive share, SE tax on both, QBI on the share only
        se = se_tax(h + srf, y)
        qbi = max(0, srf - se / 2 * (srf / (h + srf) if h + srf > 0 else 0)) * QBI
        r_tax = max(0, h + srf - se / 2 - qbi) * R_FED + se + max(0, h + srn) * R_NJ
        # Parents: passive, losses usable each year against their passive income; QBI limited by wages/UBIA (approx.)
        pqbi = min(max(0, spf) * QBI, 0.5 * m["wages"][y] * (spf / (spf + srf) if spf + srf > 0 else 0))
        p_tax = spf * P_ORD - pqbi * P_FED + spn * P_NJ
        xt = m["exitv"][y] * EXIT_TAX
        xp = xr = 0.0
        if y == last and m["exitv"][y]:
            proceeds = m["exitv"][y] + 10000 + cash
            to_p = min(proceeds, max(0, cap_p)); to_r = min(proceeds - to_p, max(0, cap_r))
            left = proceeds - to_p - to_r
            xp, xr = to_p + left * (1 - R_SPLIT), to_r + left * R_SPLIT
            dp -= 0; ex_tax_p, ex_tax_r = xt * xp / proceeds, xt * xr / proceeds
        else:
            ex_tax_p = ex_tax_r = 0.0
        ryan.append(h + dr + xr - r_tax - ex_tax_r)
        par.append(dp + xp - add - p_tax - ex_tax_p)
        fam.append(ryan[-1] + par[-1])
    return dict(fam=fam, ryan=ryan, par=par, npv=npv(fam), npv_ryan=npv(ryan), npv_par=npv(par),
                min_cap_ryan=min_cap_r, cb_left=cb_f)


# ---------- Bear early exit: run Year 1, sell at year end ----------
def early_exit(m, mult):
    e, h, fd, nd = m["ebitda"][1], m["h"][1], m["fdep"][1], m["njdep"][1]
    capex = -(m["cf"][1] - e)
    price = mult * e + 0.5 * capex
    ar = price - max(0.10 * price, 25000) - 7500
    cost = 470000 + capex
    gain_f, gain_n = ar - (cost - fd), ar - (cost - nd)          # (negative = loss); ordinary (1245 + 1231 nets)
    pretax_family = -480000 + (e + h - capex) + ar + 10000
    # D: Ryan's LLC (not yet S-corp). Parents fund the shortfall with more loan; unpaid balance is discharged.
    intr = LOAN * RATE
    inc = e + h - fd - intr + gain_f
    r_fed = -min(-inc, min(R_OTHER, EBL_S)) * R_FED if inc < 0 else inc * R_FED
    nol = max(0, -inc - R_OTHER)
    r_nj = max(0, e + h - nd - intr + gain_n) * R_NJ                  # NJ business loss can't offset wages; no NJ NOL value
    short = max(0, -(20000 + e + h - intr - capex))
    owed = LOAN + short - FORGIVE                                     # $38k forgiven as a gift at year end
    unpaid = max(0, owed - (ar + 10000))
    # COD on 'unpaid': excluded to the extent Ryan is insolvent, then reduces his NOL dollar for dollar (Sec. 108(b)).
    nol_after = max(0, nol - unpaid)
    p_int = intr * (P_ORD + P_NJ)
    d = dict(ryan_tax=r_fed + r_nj, nol_before=nol, unpaid_loan=unpaid, nol_after_cod=nol_after,
             parents_interest_tax=p_int,
             parents_bad_debt_ltcg=-unpaid * P_LTCG, parents_bad_debt_stcg=-unpaid * (P_FED + P_NIIT))
    d["family_ltcg"] = pretax_family - d["ryan_tax"] - p_int - d["parents_bad_debt_ltcg"]
    d["family_stcg"] = pretax_family - d["ryan_tax"] - p_int - d["parents_bad_debt_stcg"]
    # E: GP to Ryan; all depreciation + sale loss to parents (capital account stays positive), usable now.
    se = se_tax(h, 1)
    r_tax_e = max(0, h - se / 2) * R_FED + se + h * R_NJ
    p_fed = (e - fd + gain_f) * P_ORD
    p_nj = (e - nd + gain_n) * P_NJ
    e_res = dict(ryan_tax=r_tax_e, parents_fed=p_fed, parents_nj=p_nj,
                 family=pretax_family - r_tax_e - p_fed - p_nj)
    return dict(mult=mult, price=price, net_proceeds=ar, pretax_family=pretax_family, fed_sale_gain=gain_f, D=d, E=e_res)


if __name__ == "__main__":
    out = {}
    for name, over in (("base", dict(PLAN)), ("bear", dict(CASES["bear"]))):
        m = model_rows(over)
        D, E, D0 = run_D(m), run_E(m), run_D(m, scorp=False)
        out[name] = dict(model_D_npv=m["d_npv"], D=D, E=E, D_no_scorp=D0)
        print(f"   D without S-corp: {D0['npv']:,.0f}")
        print(f"{name}: model D {m['d_npv']:,.0f} | recomputed D {D['npv']:,.0f} (Ryan {D['npv_ryan']:,.0f} / parents {D['npv_par']:,.0f})"
              f" | E {E['npv']:,.0f} (Ryan {E['npv_ryan']:,.0f} / parents {E['npv_par']:,.0f}); Ryan min capital acct {E['min_cap_ryan']:,.0f}")
        if name == "bear":
            out["bear_exit"] = [early_exit(m, k) for k in (2.0, 2.5)]
            for x in out["bear_exit"]:
                print(json.dumps(x, default=lambda v: round(v)))
    json.dump(out, open(os.path.join(HERE, "structure_e.json"), "w"), indent=1)
