"""Independent complete L912 audit on its unchanged M=128, degree-two grid.

All original files are read-only. Recompute setup by formal series and
centered moments, prove containment (not overlap) in every saved interval,
then generate coefficients algebraically and replay every exact cell sum.
L037's Decimal/exp contract remains trusted; no formal verification claim.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
from time import monotonic

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
import certify_hankel as arithmetic

I = arithmetic.I
for ctx in (arithmetic.DOWN, arithmetic.UP, arithmetic.NEAR):
    ctx.prec = 100

SOURCE = HERE / "full-cut-taylor-166.json"
OUTPUT = HERE / "full-cut-audit-168.json"
S = 10**40
DEN = 8*S**4
checks = []
report = {"scope": "L912 exact fixed grid and degree; complete independent audit",
          "contracts": "L037 Decimal/exp, 100-digit audit setup, exact integer replay; not formal verification",
          "checks": checks, "failures": [], "evidence": {}}


def check(name, condition):
    checks.append({"name": name, "pass": bool(condition)})
    if not condition:
        report["failures"].append(name)
        save()
        raise AssertionError(name)


def save():
    OUTPUT.write_text(json.dumps(report, indent=2)+"\n")


def fp(x):
    return F(x.lo), F(x.hi)


def pair(x):
    return F(x["lower"]), F(x["upper"])


def includes(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def iprod(a, b):
    # Sign split is independent of the original four-corner multiplication.
    x, y = a
    u, v = b
    if x >= 0:
        if u >= 0:
            return x*u, y*v
        if v <= 0:
            return y*u, x*v
        return y*u, y*v
    if y <= 0:
        if u >= 0:
            return x*v, y*u
        if v <= 0:
            return y*v, x*u
        return x*v, x*u
    if u >= 0:
        return x*v, y*v
    if v <= 0:
        return y*u, x*u
    return min(x*v, y*u), max(x*u, y*v)


def isum(xs):
    low, high = 0, 0
    for x, y in xs:
        low += x
        high += y
    return low, high


def scaled(a, n):
    return (n*a[0], n*a[1]) if n >= 0 else (n*a[1], n*a[0])


def dec(a):
    return I(I.rational(a[0]).lo, I.rational(a[1]).hi).data()


def pmul(a, b):
    return [sum((a[k]*b[n-k] for k in range(n+1)), I(0)) for n in range(3)]


def pexp(a):
    # Normalized Taylor coefficients, derived by B'=A'B.
    b = [a[0].exp()]
    for n in (1, 2):
        b.append(sum((k*a[k]*b[n-k] for k in range(1, n+1)), I(0))/n)
    return b


def center_jet(u, pi):
    # e^(2(u+z)), e^((u+z)/2), and e^(-pi*n^2*e^(2(u+z))).
    e2 = pexp([2*u, I(2), I(0)])
    half = pexp([u/2, I.rational(F(1, 2)), I(0)])
    total = [I(0), I(0), I(0)]
    for n in range(1, 5):
        v = [pi*n*n*x for x in e2]
        v2 = pmul(v, v)
        p = [8*v2[k]-12*v[k] for k in range(3)]
        summand = pmul(p, pexp([-x for x in v]))
        total = [total[k]+summand[k] for k in range(3)]
    return [factorial(k)*x for k, x in enumerate(pmul(half, total))]


def trigonometry(pi_multiple, pi):
    # Exact rational period reduction; independent direct Taylor sums.
    r = pi_multiple - 2*((pi_multiple+1)//2)
    check(f"trig reduction {pi_multiple}", -1 <= r <= 1)
    x = I.rational(r)*pi
    sine = sum((I.rational(F((-1)**k, factorial(2*k+1)))*x**(2*k+1)
                for k in range(41)), I(0))
    cosine = sum((I.rational(F((-1)**k, factorial(2*k)))*x**(2*k)
                  for k in range(41)), I(0))
    er = I(x.magnitude())**82/factorial(82)
    error = I(er.hi.copy_negate(), er.hi)
    return sine+error, cosine+error


def coefficient_matrix():
    # Ordinary bivariate coefficients, multiplied by eight.
    orders = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
    pairs = tuple((r, s) for r in range(3) for s in range(3-r))
    matrix = [[F(0) for _ in pairs] for _ in orders]
    for col, (r, s) in enumerate(pairs):
        for a in range(r+1):  # eta powers taken from du and dv
            for b in range(s+1):
                row = orders.index((r+s-a-b, a+b))
                matrix[row][col] += F(8*comb(r, a)*comb(s, b)*(-1)**b,
                                      2**(a+b)*factorial(r)*factorial(s))
    check("generated coefficient denominators", all(v.denominator == 1 for row in matrix for v in row))
    return orders, pairs, [[int(v) for v in row] for row in matrix]


def main():
    raw = SOURCE.read_bytes()
    c = json.loads(raw)
    report["source_sha256"] = hashlib.sha256(raw).hexdigest()
    report["arithmetic_source_sha256"] = hashlib.sha256(Path(arithmetic.__file__).read_bytes()).hexdigest()
    arithmetic.self_check()
    for x in range(-3, 4):
        for y in range(x, 4):
            for u in range(-3, 4):
                for v in range(u, 4):
                    vals = [a*b for a in (x, y) for b in (u, v)]
                    check(f"signed product {x},{y},{u},{v}", iprod((x, y), (u, v)) == (min(vals), max(vals)))

    check("grid and counts", (c["mesh"], c["t_cells"], c["q_cells"], c["boxes"]) == (128, 4096, 1152, 4718592))
    check("exact denominator", int(c["scale"]) == S and int(c["sum_denominator"]) == DEN)
    ev = c["evidence"]
    jets, ts, qs = [ev[k] for k in ("full_jet_fixed_intervals", "t_weight_fixed_intervals", "q_weight_fixed_intervals")]
    check("all arrays complete", [len(x) for x in (jets, ts, qs)] == [5248, 4096, 1152])
    check("all endpoints integers and ordered", all(len(row) == 3 and all(
        len(p) == 2 and type(p[0]) is int and type(p[1]) is int and p[0] <= p[1] for p in row)
        for array in (jets, ts, qs) for row in array))
    pi = arithmetic.pi_bounds()
    h = pi/8192
    check("independent pi containment", includes(pair(c["pi"]), fp(pi)))
    check("independent h containment", includes(pair(c["h"]), fp(h)))
    tail = [a*I(-75).exp() for a in (160000, 80000000, 30000000000)]
    bounds = c["bounds"]
    cbound = 16*pi**2*(-7*pi/8).exp()
    check("global complex bound containment", includes(pair(bounds["complex_K_bound"]), fp(cbound)))
    check("global bound threshold", cbound.hi < 11 and (7*pi/8).lo > I.rational(F(9, 4)).hi)
    check("Cauchy radius", bounds["Cauchy_radius"] == "1/4" and pi.lo > 1)
    ratio = I.rational(F(6, 5))**8*I(-33).exp()
    check("theta ratio containment", includes(pair(bounds["majorant_ratio"]), fp(ratio)))
    check("second-tail constants", F(32)+F(224, 3)+F(330, 9)+F(75, 27) < 147 and
          147*256 == 37632 and 2*37632*5**8 < 30000000000 and ratio.hi < I.rational(F(1, 2)).lo)
    for r in range(3):
        check(f"theta tail {r} enclosure", includes(pair(bounds["full_jet_theta_tails"][r]), fp(tail[r])))

    independent_jets = []
    for k, row in enumerate(jets):
        j = center_jet(k*h, pi)
        j = [x+I(e.hi.copy_negate(), e.hi) for x, e in zip(j, tail)]
        if k == 0:
            check("independent full odd derivative contains zero", j[1].lo <= 0 <= j[1].hi)
            report["evidence"]["odd_head_plus_tail_before_parity"] = j[1].data()
            j[1] = I(0)
        for r, x in enumerate(j):
            check(f"jet containment {k}:{r}", includes((F(row[r][0], S), F(row[r][1], S)), fp(x)))
        independent_jets.append([x.data() for x in j])
    report["evidence"]["independent_full_jets"] = independent_jets
    print("Every full center jet independently enclosed and contained", flush=True)

    # T_r = 2*h^(r+3)*integral_-1/2^1/2 (i+1/2+z)^2 z^r dz.
    def rational_moment(n):
        return F(0) if n % 2 else F(1, (n+1)*2**n)

    independent_t = []
    for i, row in enumerate(ts):
        tc = F(2*i+1, 2)
        vals = []
        for r in range(3):
            coeff = 2*(tc**2*rational_moment(r)+2*tc*rational_moment(r+1)+rational_moment(r+2))
            x = I.rational(coeff)*h**(r+3)
            check(f"t moment containment {i}:{r}", includes((F(row[r][0], S), F(row[r][1], S)), fp(x)))
            vals.append(x.data())
        independent_t.append(vals)
    report["evidence"]["independent_t_moments"] = independent_t

    # Evaluate the very same Q_r using an independent centered cosine series.
    # Only moment evaluation changes; amplitude Taylor degree remains two.
    moment_coeffs = [[I(0) if (n+r) % 2 else
                     I.rational(F(2*16**n, factorial(n)*(n+r+1)))*h**(n+r+1)
                     for n in range(21)] for r in range(3)]
    moment_errors = [I.rational(F(2*16**21, factorial(21)*(22+r)))*h**(22+r) for r in range(3)]
    independent_q = []
    for j, row in enumerate(qs):
        # 16*q0 = 16*(2*j+1)*pi/8192 = (2*j+1)*pi/512.
        sn, co = trigonometry(F(2*j+1, 512), pi)
        cycle = (co, -sn, -co, sn)
        vals = []
        for r in range(3):
            x = sum((cycle[n % 4]*moment_coeffs[r][n] for n in range(21)), I(0))
            er = moment_errors[r]
            x += I(er.hi.copy_negate(), er.hi)
            check(f"q moment containment {j}:{r}", includes((F(row[r][0], S), F(row[r][1], S)), fp(x)))
            vals.append(x.data())
        sign = 1 if (j+128)//256 % 2 == 0 else -1
        check(f"strict q sign {j}", row[0][0] > 0 if sign == 1 else row[0][1] < 0)
        independent_q.append(vals)
    report["evidence"]["independent_q_moments"] = independent_q
    orders, derivpairs, matrix = coefficient_matrix()
    report["evidence"]["coefficient_matrix"] = {"orders": orders, "derivative_pairs": derivpairs, "eight_times_coefficients": matrix}
    print("All signed moments contained; algebraic coefficient matrix generated", flush=True)
    save()

    # All array values used below are now validated by containment, not by overlap.
    sparse = [[(idx, n) for idx, n in enumerate(row) if n] for row in matrix]
    totals = [[[0, 0] for _ in orders] for _ in range(5)]
    rows = []
    negative_centers = zero_centers = cells = 0
    started = monotonic()
    for j in range(1152):
        rowsum = [[0, 0] for _ in orders]
        for i in range(4096):
            aa = jets[i+j+1]
            bb = jets[abs(i-j)]
            if i < j:
                bb = [scaled(x, (-1)**r) for r, x in enumerate(bb)]
                negative_centers += 1
            elif i == j:
                zero_centers += 1
            products = [iprod(aa[r], bb[s]) for r, s in derivpairs]
            for term, (tr, qr) in enumerate(orders):
                coeff = isum(scaled(products[idx], n) for idx, n in sparse[term])
                value = iprod(coeff, iprod(ts[i][tr], qs[j][qr]))
                rowsum[term][0] += value[0]
                rowsum[term][1] += value[1]
            cells += 1
        ell = (j+128)//256
        for term in range(6):
            totals[ell][term][0] += rowsum[term][0]
            totals[ell][term][1] += rowsum[term][1]
        rows.append(rowsum)
        if (j+1) % 128 == 0:
            print(f"Independent exact replay: {j+1}/1152 q rows; {monotonic()-started:.1f}s", flush=True)
    report["evidence"]["independent_exact_q_row_term_accumulators"] = rows
    report["evidence"]["independent_exact_lobe_term_accumulators"] = totals
    check("every cell and parity case", cells == 4718592 and negative_centers == 1152*1151//2 and zero_centers == 1152)
    check("all exact accumulators identical", totals == ev["exact_lobe_term_accumulators"])
    for ell in range(5):
        for term in range(6):
            check(f"scaled reported lobe term {ell}:{term}", includes(pair(c["result"]["polynomial_lobe_terms"][ell][term]),
                  (F(totals[ell][term][0], DEN), F(totals[ell][term][1], DEN))))
        lobe = isum(totals[ell])
        check(f"reported lobe {ell}", includes(pair(c["result"]["polynomial_lobes"][ell]), (F(lobe[0], DEN), F(lobe[1], DEN))))
    allsum = isum(a for row in totals for a in row)
    polynomial = tuple(F(2*x, DEN) for x in allsum)
    check("polynomial scaling and reflection", includes(pair(c["result"]["polynomial_cut"]), polynomial))
    R = I.rational(sum((F(comb(3, r)*factorial(r)*factorial(3-r)*4**3*11**2, 6)
                       for r in range(4)), F(0)))*h**3
    tmass = pi**3/12
    exact_qmass = I.rational(F(9, 16))
    ET = 2*R*tmass*exact_qmass
    Es = 131072*I(-106).exp()*I.rational(F(9, 924)+F(3, 231**2)+F(2, 231**3))
    ES = 2*exact_qmass*Es
    for key, x in (("amplitude_remainder", R), ("t_weight_mass", tmass),
                   ("absolute_cosine_mass", exact_qmass), ("full_cut_taylor_error", ET),
                   ("spatial_density_error", Es), ("full_cut_spatial_error", ES)):
        check(f"independent error bound containment {key}", includes(pair(bounds[key]), fp(x)))
    error = F(ET.hi)+F(ES.hi)
    completed = (polynomial[0]-error, polynomial[1]+error)
    check("independent complete raw interval containment", includes(pair(c["result"]["complete_raw_cut_A0_H"]), completed))
    check("complete raw rational bounds", completed[0] > F(15, 10**6) and completed[1] < F(27, 10**6))
    # Check the saved calculation's own outward error operations too.
    saved_error = pair(bounds["full_cut_taylor_error"])[1]+pair(bounds["full_cut_spatial_error"])[1]
    saved_poly = pair(c["result"]["polynomial_cut"])
    saved_raw = pair(c["result"]["complete_raw_cut_A0_H"])
    check("saved full error inclusion", includes(saved_raw, (saved_poly[0]-saved_error, saved_poly[1]+saved_error)))
    check("saved raw rational bounds", saved_raw[0] > F(15, 10**6) and saved_raw[1] < F(27, 10**6))
    oldpath = HERE / c["normalizer"]["source"]
    oldbytes = oldpath.read_bytes()
    check("audited normalizer source identity", oldpath.name == "variable-hall-cuts-137-m128.json" and
          hashlib.sha256(oldbytes).hexdigest() == c["normalizer"]["sha256"])
    check("exact audited A0 field reuse", json.loads(oldbytes)["result"]["A0"] == c["normalizer"]["A0"])
    a0 = pair(c["normalizer"]["A0"])
    check("normalizer strictly positive", a0[0] > 0)
    normalized = (completed[0]/a0[1], completed[1]/a0[0])
    check("independent normalized containment", includes(pair(c["result"]["H"]), normalized))
    check("saved normalized inclusion", includes(pair(c["result"]["H"]), (saved_raw[0]/a0[1], saved_raw[1]/a0[0])))
    hh = pair(c["result"]["H"])
    check("normalized rational bounds", hh[0] > F(69, 10**5) and hh[1] < F(116, 10**5))
    report["evidence"]["independent_bounds"] = {"amplitude_remainder": R.data(), "taylor_error": ET.data(),
                                                   "spatial_error": ES.data(), "polynomial": dec(polynomial)}
    check("original certificate preserved", SOURCE.read_bytes() == raw)
    report["result"] = {"check_count": len(checks), "all_cells": cells, "negative_centers": negative_centers,
                        "zero_centers": zero_centers, "raw": dec(completed), "normalized": dec(normalized),
                        "required": "raw lower > 0; all arrays contained and all exact accumulators equal",
                        "decision": "AUDITED_FINITE_PASS", "failures": report["failures"]}
    save()
    print(json.dumps({"result": report["result"], "certificate": str(OUTPUT)}), flush=True)


if __name__ == "__main__":
    main()
