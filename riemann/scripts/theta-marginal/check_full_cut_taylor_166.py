"""Internal complete-evidence checks for step166; no new grid or cut.

Exact rational aggregation and independent centered-series moment checks.
Does not replace the separate critical audit or replay all cell products.
"""
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from equal_neighbor_budget_135 import I, pi_bounds, sin_cos, symmetric

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "full-cut-taylor-166.json"
OUTPUT = HERE / "full-cut-taylor-checks-166.json"


def pair(d):
    return F(d["lower"]), F(d["upper"])


def contains(d, a):
    x, y = pair(d)
    return x <= a[0] <= a[1] <= y


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def main():
    raw = SOURCE.read_bytes()
    c = json.loads(raw)
    checks = []

    def check(name, condition):
        checks.append({"name": name, "pass": bool(condition)})
        if not condition:
            OUTPUT.write_text(json.dumps({"checks": checks, "failure": name}, indent=2)+"\n")
            raise AssertionError(name)

    check("fixed target and counts", (c["mesh"], c["t_cells"], c["q_cells"], c["boxes"]) ==
          (128, 4096, 1152, 4718592))
    ev = c["evidence"]
    jets, ts, qs = (ev[k] for k in ("full_jet_fixed_intervals", "t_weight_fixed_intervals",
                                  "q_weight_fixed_intervals"))
    check("complete arrays", (len(jets), len(ts), len(qs)) == (5248, 4096, 1152))
    check("all stored endpoints ordered integers", all(
        len(row) == 3 and all(len(p) == 2 and isinstance(p[0], int) and
                             isinstance(p[1], int) and p[0] <= p[1] for p in row)
        for array in (jets, ts, qs) for row in array))
    check("exact full odd derivative at zero", jets[0][1] == [0, 0])
    scale = int(c["scale"])
    denom = int(c["sum_denominator"])
    check("accumulator denominator", denom == 8*scale**4)
    totals = ev["exact_lobe_term_accumulators"]
    check("all exact lobe-term arrays", len(totals) == 5 and all(len(row) == 6 for row in totals))
    polynomial = (F(0), F(0))
    for ell, row in enumerate(totals):
        lobe = (F(0), F(0))
        for term, a in enumerate(row):
            v = F(a[0], denom), F(a[1], denom)
            check(f"lobe {ell} term {term} exact scaling", contains(c["result"]["polynomial_lobe_terms"][ell][term], v))
            lobe = add(lobe, v)
        check(f"lobe {ell} complete term sum", contains(c["result"]["polynomial_lobes"][ell], lobe))
        polynomial = add(polynomial, (2*lobe[0], 2*lobe[1]))
    check("full reflected polynomial exact sum", contains(c["result"]["polynomial_cut"], polynomial))
    p = pair(c["result"]["polynomial_cut"])
    e = sum(pair(c["bounds"][k])[1] for k in ("full_cut_taylor_error", "full_cut_spatial_error"))
    complete = (p[0]-e, p[1]+e)
    check("complete error subtraction and addition", contains(c["result"]["complete_raw_cut_A0_H"], complete))
    a0 = pair(c["normalizer"]["A0"])
    check("positive normalizer", a0[0] > 0)
    cp = pair(c["result"]["complete_raw_cut_A0_H"])
    check("positive raw cut without normalization", cp[0] > F(15, 10**6) and cp[1] < F(27, 10**6))
    check("normalized division", contains(c["result"]["H"], (cp[0]/a0[1], cp[1]/a0[0])))
    hp = pair(c["result"]["H"])
    check("strict normalized rational bounds", hp[0] > F(69, 10**5) and hp[1] < F(116, 10**5))
    old = HERE / c["normalizer"]["source"]
    check("normalizer byte identity", hashlib.sha256(old.read_bytes()).hexdigest() == c["normalizer"]["sha256"])
    check("normalizer matches original full field", json.loads(old.read_bytes())["result"]["A0"] == c["normalizer"]["A0"])

    # All setup moment evidence is inspected by independent expressions.
    pi = pi_bounds()
    h = pi/8192

    def monomial_integral(power, radius):
        return I(0) if power % 2 else 2*radius**(power+1)/(power+1)

    tsum, qsum, qabs = (F(0), F(0)), (F(0), F(0)), (F(0), F(0))
    alternate_q = []
    for i, row in enumerate(ts):
        tc = h*I.rational(F(2*i+1, 2))
        for r, a in enumerate(row):
            v = 2*(tc**2*monomial_integral(r, h/2)+
                   2*tc*monomial_integral(r+1, h/2)+monomial_integral(r+2, h/2))
            x, y = F(a[0], scale), F(a[1], scale)
            check(f"t moment {i}:{r} independent expansion overlaps", x <= F(v.hi) and F(v.lo) <= y)
        tsum = add(tsum, (F(row[0][0], scale), F(row[0][1], scale)))
    mass = pair(c["bounds"]["t_weight_mass"])
    check("full t mass agreement", tsum[0] <= mass[1] and mass[0] <= tsum[1])
    for j, row in enumerate(qs):
        s, co = sin_cos(16*(2*j+1)*h, pi)
        vals = []
        for r, a in enumerate(row):
            # Taylor polynomial of cos(16(q0+z)) through degree 12.
            cycle = (co, -s, -co, s)
            v = sum((cycle[n % 4]*I.rational(F(16**n, factorial(n)))*
                     monomial_integral(n+r, h) for n in range(13)), I(0))
            er = I.rational(F(2*16**13, (14+r)*factorial(13)))*h**(14+r)
            v = v+symmetric(er)
            vals.append(v.data())
            x, y = F(a[0], scale), F(a[1], scale)
            check(f"q moment {j}:{r} independent series overlaps", x <= F(v.hi) and F(v.lo) <= y)
        alternate_q.append(vals)
        v = (F(row[0][0], scale), F(row[0][1], scale))
        sign = (-1)**((j+128)//256)
        check(f"q cell {j} weight sign", v[0] > 0 if sign > 0 else v[1] < 0)
        qsum = add(qsum, v)
        qabs = add(qabs, v if sign > 0 else (-v[1], -v[0]))
    check("signed q mass exact value", qsum[0] <= F(1, 16) <= qsum[1])
    check("absolute q mass exact value", qabs[0] <= F(9, 16) <= qabs[1])
    check("reported absolute mass exact value", contains(c["bounds"]["absolute_cosine_mass"], (F(9, 16), F(9, 16))))
    failures = [v["name"] for v in checks if not v["pass"]]
    OUTPUT.write_text(json.dumps({"source_sha256": hashlib.sha256(raw).hexdigest(),
        "scope": "Internal consistency, all moment arrays and exact aggregate scaling; not full cell replay or critical audit",
        "checks": checks, "alternate_q_moment_enclosures": alternate_q, "failures": failures,
        "result": {"check_count": len(checks), "raw_cut": c["result"]["complete_raw_cut_A0_H"],
                   "required": "raw lower>=0", "failures": failures}}, indent=2)+"\n")
    print(json.dumps({"checks": len(checks), "failures": failures, "raw": c["result"]["complete_raw_cut_A0_H"],
                      "required": "raw lower>=0", "certificate": str(OUTPUT)}))


if __name__ == "__main__":
    main()
