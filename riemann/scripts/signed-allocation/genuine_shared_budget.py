#!/usr/bin/env python3
"""One approved candidate; exact all-real certificates, no external packages.

Bernstein leaves cover [-2,2] (individual) and [0,4] (aggregate y).
Positive power coefficients after translation certify both unbounded tails.
The complete rational polynomials, leaves and original 4-variable dual are saved.
"""
import json
from fractions import Fraction as F
from math import comb
from pathlib import Path


def add(*ps):
    q = [F(0)] * max(map(len, ps))
    for p in ps:
        for i, c in enumerate(p):
            q[i] += c
    return q


def mul(*ps):
    q = [F(1)]
    for p in ps:
        z = [F(0)] * (len(q) + len(p) - 1)
        for i, a in enumerate(q):
            for j, b in enumerate(p):
                z[i+j] += a*b
        q = z
    return q


def affine(p, a, b):
    """Coefficients of p(a+b*t)."""
    return [sum(p[j]*comb(j, i)*a**(j-i)*b**i
                for j in range(i, len(p))) for i in range(len(p))]


def val(p, t):
    return sum(c*t**i for i, c in enumerate(p))


def bernstein(p, lo, hi):
    q = affine(p, lo, hi-lo)
    n = len(p)-1
    return [sum(q[i]*F(comb(k, i), comb(n, i)) for i in range(k+1))
            for k in range(n+1)]


def certify_interval(p, lo, hi, depth=0):
    b = bernstein(p, lo, hi)
    if min(b) > 0:
        return [{"lo": lo, "hi": hi, "bernstein": b,
                 "lower_bound": min(b)}]
    if depth == 12:
        raise ArithmeticError(f"Unresolved interval {lo},{hi}")
    mid = (lo+hi)/2
    return (certify_interval(p, lo, mid, depth+1)
            + certify_interval(p, mid, hi, depth+1))


def pair(c, x):
    return 2*((x-c)**2-1)/((x-c)**2+1)**2


def encode(v):
    if isinstance(v, F):
        return str(v)
    if isinstance(v, dict):
        return {k: encode(w) for k, w in v.items()}
    if isinstance(v, list):
        return [encode(w) for w in v]
    return v


def main():
    h, r, s = F(11, 16), F(5, 4), F(9, 32)
    a = [h*h+1, -2*h, F(1)]
    b = [h*h+1, 2*h, F(1)]
    m = [-r*r, F(0), F(1)]
    ka = [2*(h*h-1), -4*h, F(2)]
    kb = [2*(h*h-1), 4*h, F(2)]
    real_num = [2*r*r, F(0), F(2)]
    individual = add(mul(ka, m, m), mul(real_num, a, a))
    aggregate_x = add(mul(ka, b, b, m, m),
                      mul(kb, a, a, m, m), mul(real_num, a, a, b, b))
    aggregate_y = aggregate_x[::2]
    assert not any(aggregate_x[1::2])
    certs = {}
    for name, p, lo, hi in [
            ("individual", individual, F(-2), F(2)),
            ("aggregate_y", aggregate_y, F(0), F(4))]:
        leaves = certify_interval(p, lo, hi)
        tails = {"right": affine(p, hi, F(1))}
        if name == "individual":
            tails["left"] = affine(p, lo, F(-1))
        for t in tails.values():
            assert t[0] > 0 and min(t) >= 0
        assert leaves[0]["lo"] == lo and leaves[-1]["hi"] == hi
        assert all(z["hi"] == w["lo"] for z, w in zip(leaves, leaves[1:]))
        certs[name] = {"polynomial_ascending": p, "leaves": leaves,
                       "tails_power_coefficients": tails,
                       "required": "Every Bernstein coefficient >0; tail constant >0 and all tail coefficients >=0"}
    A, B, K = 1/(s+r)**2, 1/(s-r)**2, pair(h, s)
    # Original variable order ah, a_minus_h, bh, b_minus_h; Mv<=d.
    matrix = [[-A, F(0), -B, F(0)], [F(0), -B, F(0), -A],
              [F(1), F(1), F(0), F(0)], [F(0), F(0), F(1), F(1)]]
    matrix += [[-F(i == j) for i in range(4)] for j in range(4)]
    rhs = [K, K, F(1), F(1)] + [F(0)]*4
    weights = [F(1), F(1), B, B, B-A, F(0), F(0), B-A]
    annihilation = [sum(w*row[j] for w, row in zip(weights, matrix))
                    for j in range(4)]
    dual = sum(w*d for w, d in zip(weights, rhs))
    assert min(weights) >= 0 and annihilation == [0]*4 and dual < 0
    assert 1 <= r < F(21, 16) and r.denominator <= 4096
    assert s not in (-r, r) and A < B
    # Exact identity checks at the selected witness supplement the algebra.
    individual_direct = K+A+B
    aggregate_direct = K+pair(-h, s)+A+B
    assert val(individual, s) == individual_direct*val(m, s)**2*val(a, s)**2
    assert val(aggregate_y, s*s) == aggregate_direct*val(m, s)**2*val(a, s)**2*val(b, s)**2
    evidence = {
        "target": "Seek an exact rational symmetric two-pair block with all-real positive aggregate and individually feasible full budgets, but no conserved four-constant allocation.",
        "h": h, "r": r, "candidate_count_actual": 1, "candidate_cap": 8,
        "candidate_reason": "Required first candidate r=5/4; numerical interval diagnostic nominated s=9/32; exact certification succeeded, so stop",
        "pair_rows_actual": 2, "pair_row_cap_per_candidate": 32,
        "sample_diagnostic": "60001 equally spaced x in [-3,3], poles/zero excluded; nomination only, not sign evidence or LP rows",
        "full_domain_certificates": certs,
        "dual": {"variable_order": ["alpha_h", "alpha_minus_h", "beta_h", "beta_minus_h"],
                 "row_order": ["pair h at s", "pair -h at -s", "alpha budget", "beta budget",
                               "alpha_h>=0", "alpha_minus_h>=0", "beta_h>=0", "beta_minus_h>=0"],
                 "s": s, "A": A, "B": B, "K": K, "matrix": matrix, "rhs": rhs,
                 "multipliers": weights, "transpose_times_multipliers": annihilation,
                 "dual_value": dual, "required_dual_value": "<0",
                 "individual_full_budget_at_s": individual_direct,
                 "K_plus_B": K+B},
        "tails": {"individual_x_squared_limit": F(4), "aggregate_x_squared_limit": F(6)},
        "failures": [], "passed": True,
        "limitations": "Finite first-sign example; independent audit pending; no Xi realization, higher signs, semi-infinite completeness or novelty certification",
    }
    path = Path(__file__).with_name("genuine-shared-budget-certificate.json")
    path.write_text(json.dumps(encode(evidence), indent=2)+"\n")
    print(f"Candidates 1/8; pair rows 2/32. Exact certificates passed; failures [].")
    for name, c in certs.items():
        print(f"{name}: {len(c['leaves'])} leaves, all Bernstein bounds >0; tail bounds passed.")
    print(f"Dual value {dual}<0 required; individual full-budget at s {individual_direct}>0.")
    print(f"Full certificate: {path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
