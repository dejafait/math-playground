"""One fixed M=128 degree-two full Hall cut; proof and contracts in L912.

Decimal encloses setup quantities; exact integer intervals accumulate every
cell without arithmetic truncation. No adaptive mesh or degree selection.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from time import monotonic

from equal_neighbor_budget_135 import I, pi_bounds, self_check, sin_cos, symmetric

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "full-cut-taylor-166.json"
SCALE = 10**40
M = 128


def fixed(x):
    # Fraction conversion is exact; no ambient Decimal context is used.
    a, b = Fraction(x.lo)*SCALE, Fraction(x.hi)*SCALE
    return (a.numerator//a.denominator, -((-b.numerator)//b.denominator))


def mul(a, b):
    p = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(p), max(p)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def times(a, n):
    return (a[0]*n, a[1]*n) if n >= 0 else (a[1]*n, a[0]*n)


def interval(a, denominator):
    lo = I.rational(Fraction(a[0], denominator))
    hi = I.rational(Fraction(a[1], denominator))
    return I(lo.lo, hi.hi)


def main():
    self_check()
    assert Fraction(fixed(I.rational(Fraction(-1, 3)))[0], SCALE) <= Fraction(-1, 3)
    assert mul((-2, 3), (-5, 7)) == (-15, 21)
    pi = pi_bounds()
    h = pi/(64*M)
    nt, nq = 32*M, 9*M
    # L910's full even holomorphic K=4W. This is a global strip bound.
    complex_bound = 16*pi*pi*(-7*pi/8).exp()
    assert complex_bound.hi < 11 and (7*pi/8).lo > I.rational(Fraction(9, 4)).hi
    amplitude_remainder = 256*11**2*h**3
    exp75 = I(-75).exp()
    tails = [160000*exp75, 80000000*exp75, 30000000000*exp75]
    # All three majorants have successive n>=5 ratio less than 1/2.
    ratio = I.rational(Fraction(6, 5))**8*I(-33).exp()
    assert ratio.hi < I.rational(Fraction(1, 2)).lo
    assert 2*37632*5**8 < 30000000000

    jets = []
    for k in range(nt+nq):
        u = h*k
        e2 = (2*u).exp()
        result = [I(0), I(0), I(0)]
        for n in range(1, 5):
            v = pi*n*n*e2
            polynomials = [8*v**2-12*v,
                           -16*v**3+60*v**2-30*v,
                           32*v**4-224*v**3+330*v**2-75*v]
            factor = (u/2-v).exp()
            result = [r+p*factor for r, p in zip(result, polynomials)]
        result = [r+symmetric(e) for r, e in zip(result, tails)]
        if k == 0:
            assert result[1].lo <= 0 <= result[1].hi
            result[1] = I(0)  # Full analytic evenness, not head evenness.
        jets.append([fixed(r) for r in result])

    tw = []
    d = h/2
    j0, j2, j4 = 2*d, 2*d**3/3, 2*d**5/5
    for i in range(nt):
        c = h*I.rational(Fraction(2*i+1, 2))
        tw.append([fixed(2*(c*c*j0+j2)), fixed(4*c*j2),
                   fixed(2*(c*c*j2+j4))])
    trig = [list(sin_cos(pi*j/(2*M), pi)) for j in range(nq+1)]
    for k in range(10):
        j = k*M
        for a, exact in enumerate(((0, 1, 0, -1)[k % 4], (1, 0, -1, 0)[k % 4])):
            assert trig[j][a].lo <= exact <= trig[j][a].hi
            trig[j][a] = I(exact)
    qw = []
    absolute_cosine_integral = I(0)
    for j in range(nq):
        sa, ca = trig[j]
        sb, cb = trig[j+1]
        q0 = (sb-sa)/16
        q1 = h*(sb+sa)/16+(cb-ca)/256
        q2 = h*h*(sb-sa)/16+2*h*(cb+ca)/256-2*(sb-sa)/4096
        ell = (j+M)//(2*M)
        sign = (-1)**ell
        assert (q0.lo > 0) if sign > 0 else (q0.hi < 0)
        absolute_cosine_integral = absolute_cosine_integral+sign*q0
        qw.append([fixed(q0), fixed(q1), fixed(q2)])

    # Full scaled polynomial integrals, separately retained by lobe and term.
    totals = [[(0, 0) for _ in range(6)] for _ in range(5)]
    orders = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
    start = monotonic()
    for j in range(nq):
        ell = (j+M)//(2*M)
        subtotal = [(0, 0) for _ in range(6)]
        for i in range(nt):
            a, b = jets[i+j+1], jets[abs(i-j)]
            if i-j < 0:
                b = [b[0], times(b[1], -1), b[2]]
            p00 = mul(a[0], b[0])
            p10, p01 = mul(a[1], b[0]), mul(a[0], b[1])
            p20, p11, p02 = mul(a[2], b[0]), mul(a[1], b[1]), mul(a[0], b[2])
            # Eight times the six ordinary (not factorial-normalized) coefficients.
            even = add(p20, p02)
            coeff = (times(p00, 8), times(add(p10, p01), 8),
                     times(sub(p10, p01), 4), times(add(even, times(p11, 2)), 4),
                     times(sub(p20, p02), 4), sub(even, times(p11, 2)))
            for k, (at, aq) in enumerate(orders):
                weight = mul(tw[i][at], qw[j][aq])
                subtotal[k] = add(subtotal[k], mul(coeff[k], weight))
        totals[ell] = [add(a, b) for a, b in zip(totals[ell], subtotal)]
        if (j+1) % 128 == 0:
            print(f"q cells {j+1}/{nq}; fixed grid, elapsed {monotonic()-start:.1f}s", flush=True)

    denominator = 8*SCALE**4
    terms = [[interval(v, denominator) for v in row] for row in totals]
    polynomial_lobes = [sum(row, I(0)) for row in terms]
    polynomial_cut = 2*sum(polynomial_lobes, I(0))
    # 2 outside is the full-cut reflection; 2t^2 is already in tw.
    t_mass = pi**3/12
    remainder_cut = 2*amplitude_remainder*t_mass*absolute_cosine_integral
    espace = 131072*I(-106).exp()*I.rational(
        Fraction(9, 4*231)+Fraction(3, 231**2)+Fraction(2, 231**3))
    spatial_cut = 2*espace*absolute_cosine_integral
    full_cut = polynomial_cut+symmetric(remainder_cut+spatial_cut)

    old_path = HERE / "variable-hall-cuts-137-m128.json"
    old_bytes = old_path.read_bytes()
    old = json.loads(old_bytes)
    a0 = I(old["result"]["A0"]["lower"], old["result"]["A0"]["upper"])
    assert a0.lo > 0 and old["mesh"] == M
    normalized = full_cut/a0
    decision = "NEGATIVE" if full_cut.hi < 0 else ("PASS" if full_cut.lo >= 0 else "INCONCLUSIVE")
    rational_pass = full_cut.lo > I.rational(Fraction(1, 100000)).hi
    result = {
        "scope": "L905 full cut only, x=16,y=0,F={-2,-1,0,1},T=pi/2,M=128,degree=2",
        "contracts": "L037 Decimal and exact integer interval accumulation; no formal verification",
        "method": "Full even analytic K; center jets including all theta tails; Cauchy remainder",
        "mesh": M, "t_cells": nt, "q_cells": nq, "boxes": nt*nq,
        "scale": str(SCALE), "sum_denominator": str(denominator),
        "pi": pi.data(), "h": h.data(),
        "bounds": {"complex_K_bound": complex_bound.data(), "Cauchy_radius": "1/4",
                   "majorant_ratio": ratio.data(), "full_jet_theta_tails": [v.data() for v in tails],
                   "amplitude_remainder": amplitude_remainder.data(), "t_weight_mass": t_mass.data(),
                   "absolute_cosine_mass": absolute_cosine_integral.data(),
                   "full_cut_taylor_error": remainder_cut.data(),
                   "spatial_density_error": espace.data(), "full_cut_spatial_error": spatial_cut.data()},
        "normalizer": {"A0": a0.data(), "source": old_path.name,
                       "sha256": hashlib.sha256(old_bytes).hexdigest(), "basis": "audited L905/step139"},
        "result": {"polynomial_lobe_terms": [[v.data() for v in row] for row in terms],
                   "polynomial_lobes": [v.data() for v in polynomial_lobes],
                   "polynomial_cut": polynomial_cut.data(), "complete_raw_cut_A0_H": full_cut.data(),
                   "H": normalized.data(), "decision": decision,
                   "required": "A0*H(F)>=0", "strict_rational_lower_gt_1e_minus5": rational_pass,
                   "failures": ["Zero-containing full cut"] if decision == "INCONCLUSIVE" else []},
        "evidence": {"full_jet_fixed_intervals": jets, "t_weight_fixed_intervals": tw,
                     "q_weight_fixed_intervals": qw, "exact_lobe_term_accumulators": totals},
    }
    OUTPUT.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"decision": decision, "raw": full_cut.data(), "required": "lower>=0 passes only this cut",
                      "remainder": remainder_cut.data(), "failures": result["result"]["failures"],
                      "certificate": str(OUTPUT)}), flush=True)


if __name__ == "__main__":
    main()
