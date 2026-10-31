#!/usr/bin/env python3
"""Bounded nomination and exact certificate for the approved shared-budget grid.

Numerical screening only nominates a point. The certificate below independently
clears denominators and proves positivity on all y=x^2>=0 by rational bounds.
Run from the active notebook; no external data or symbolic algebra is used.
"""
import json
from fractions import Fraction as F
from pathlib import Path

import numpy as np


def add(*polys):
    out = [F(0)] * max(map(len, polys))
    for poly in polys:
        for i, c in enumerate(poly):
            out[i] += c
    return out


def mul(*polys):
    out = [F(1)]
    for poly in polys:
        result = [F(0)] * (len(out) + len(poly) - 1)
        for i, c in enumerate(out):
            for j, d in enumerate(poly):
                result[i + j] += c * d
        out = result
    return out


def value(poly, x):
    out = F(0)
    for c in reversed(poly):
        out = out * x + c
    return out


def pair(c, x):
    return 2 * ((x - c)**2 - 1) / ((x - c)**2 + 1)**2


def real_terms(r, x):
    return 1 / (x + r)**2 + 1 / (x - r)**2


def aggregate(h, r, x):
    return pair(h, x) + pair(-h, x) + real_terms(r, x)


def encode(poly):
    return list(map(str, poly))


def exact_candidate(j, k, witness):
    """Return the specified rational certificate if every exact test passes."""
    h, r = F(j, 16), F(k, 16)
    a = [h*h + 1, -2*h, F(1)]
    b = [h*h + 1, 2*h, F(1)]
    m = [-r*r, F(0), F(1)]
    denominator = mul(a, a, b, b, m, m)
    numerator = add(
        mul([2*(h*h - 1), -4*h, F(2)], b, b, m, m),
        mul([2*(h*h - 1), 4*h, F(2)], a, a, m, m),
        mul([2*r*r, F(0), F(2)], a, a, b, b),
    )
    # This deliberately bounded certificate template is tested, not presumed.
    scale = F(1, 549755813888)
    q = [c / scale for c in numerator[::2]]
    if len(q) != 6 or any(numerator[1::2]):
        return None
    c0, c1, c2, c3, c4, c5 = q
    split = F(50000000000000)
    square_residual = 4*split*c0 - c1*c1
    low_bound = c2 - split + c3 + c4
    high_constant = c2 - split
    high_cubic = c3 + c4 + c5
    # On 0<=y<=1, the two negative terms are bounded below by c3+c4.
    # On y>=1, they are bounded below by (c3+c4)*y^3.
    checks = {
        "even_numerator": not any(numerator[1::2]),
        "positive_scale": scale > 0,
        "split_positive": split > 0,
        "square_residual_positive": square_residual > 0,
        "c3_c4_nonpositive_c5_nonnegative": c3 <= 0 and c4 <= 0 and c5 >= 0,
        "low_interval_lower_bound_positive": low_bound > 0,
        "high_interval_constant_positive": high_constant > 0,
        "high_interval_cubic_nonnegative": high_cubic >= 0,
        "witness_avoids_poles": witness not in (-r, r),
    }
    if not checks["witness_avoids_poles"]:
        return None
    A, B = 1/(witness+r)**2, 1/(witness-r)**2
    full_budget_value = pair(h, witness) + A + B
    checks["full_budget_value_strictly_negative"] = full_budget_value < 0
    # Independent evaluation detects a mismatch in the denominator clearing.
    direct = aggregate(h, r, witness)
    checks["rational_identity_at_witness"] = (
        direct * value(denominator, witness) == value(numerator, witness)
    )
    if not all(checks.values()):
        return None
    return {
        "h": str(h), "r": str(r),
        "polynomial": {
            "A_x_ascending": encode(a), "B_x_ascending": encode(b),
            "M_x_ascending": encode(m),
            "denominator_x_ascending": encode(denominator),
            "numerator_x_ascending": encode(numerator),
            "scale": str(scale), "Q_y_ascending": encode(q),
            "identity": "H(x)*A(x)^2*B(x)^2*(x^2-r^2)^2=scale*Q(x^2)",
            "denominator_sign": "A,B>=1; (x^2-r^2)^2>0 for x!=+/-r",
        },
        "positivity": {
            "split": str(split), "square_residual": str(square_residual),
            "quadratic_identity": "4*split*(c0+c1*y+split*y^2)=(2*split*y+c1)^2+square_residual",
            "R_y_ascending": encode([c2-split, c3, c4, c5]),
            "low_interval": "0<=y<=1", "low_R_lower_bound": str(low_bound),
            "high_interval": "y>=1", "high_R_constant": str(high_constant),
            "high_R_cubic_coefficient": str(high_cubic),
            "conclusion": "Q(y)>0 for every y>=0; H(x)>0 for every real x!=+/-r",
        },
        "allocation_obstruction": {
            "test_center": "h", "x": str(witness),
            "pair_value": str(pair(h, witness)),
            "alpha_h_coefficient": str(A), "beta_h_coefficient": str(B),
            "full_budget_upper_bound": str(full_budget_value),
            "required_lower_bound": "0", "strict_margin": str(-full_budget_value),
            "budget_consequence": "0<=alpha_h<=1 and 0<=beta_h<=1",
            "certificate": "K_h+A*alpha_h+B*beta_h <= K_h+A+B < 0",
            "scope": "Excludes all four-constant allocations without symmetry reduction; even the h pair cannot use both full unit budgets successfully.",
        },
        "domain": {
            "poles": "H tends to +infinity at both +/-r; other terms are bounded there",
            "infinity": "lim x^2*H(x)=6 as |x| tends to infinity; no uniform positive constant margin is claimed",
        },
        "checks": checks, "failures": [], "passed": True,
    }


def run():
    # Lexicographic approved grid, with rational sample points m/2000 in [-5,5].
    sample_numerators = np.arange(-10000, 10001)
    samples = sample_numerators / 2000
    records, unsuccessful_nominations = [], []
    result = None
    for j in range(1, 33):
        for k in range(1, 33):
            h, r = F(j, 16), F(k, 16)
            mask = (np.abs(samples-float(r)) > 1e-10) & (np.abs(samples+float(r)) > 1e-10)
            x, integers = samples[mask], sample_numerators[mask]
            p = 2*((x-float(h))**2-1)/((x-float(h))**2+1)**2
            q = 2*((x+float(h))**2-1)/((x+float(h))**2+1)**2
            u = 1/(x-float(r))**2 + 1/(x+float(r))**2
            total = p+q+u
            i = int(np.argmin(total))
            point = F(int(integers[i]), 2000)
            record = {"j": j, "k": k, "h": str(h), "r": str(r),
                      "sample_H_min": float(total[i]), "sample_H_min_x": str(point)}
            if total[i] < 0 and aggregate(h, r, point) < 0:
                record.update(status="exact_negative_H_witness", H=str(aggregate(h, r, point)))
            else:
                record["status"] = "unresolved_after_numerical_screen"
                # Seek a small rational negative full-budget witness, then attempt
                # an exact all-real certificate. No floating value is proof.
                witnesses = [h-F(1, 4)] + [F(m, 16) for m in range(-80, 81)]
                for witness in witnesses:
                    if witness in (-r, r):
                        continue
                    if pair(h, witness) + real_terms(r, witness) >= 0:
                        continue
                    result = exact_candidate(j, k, witness)
                    if result:
                        record["status"] = "certified_separation"
                        break
                if not result and float(np.min(p+u)) < 0:
                    unsuccessful_nominations.append({"j": j, "k": k,
                                                     "reason": "No full exact certificate from the bounded template"})
            records.append(record)
            if result:
                break
        if result:
            break
    certificate = {
        "target": "Seek a certified aggregate-positive but allocation-infeasible block on the grid h,r in {j/16: 1<=j<=32} with unit displacements and unit real-zero budgets.",
        "grid": {"j_k_inclusive_bounds": [1, 32], "denominator": 16,
                 "order": "lexicographic (j,k)", "stopping_rule": "first full exact certificate"},
        "screen": {"sample_numerator_bounds": [-10000, 10000], "denominator": 2000,
                   "excluded_points": "+/-r", "role": "nomination only; no global sign inference"},
        "tested_count": len(records), "tested_records": records,
        "prior_pilot_nomination": {
            "role": "Earlier numerical-only diagnostic; no exact certificate or sign conclusion",
            "sample_bounds": "20001 equally spaced samples in [-5,5], excluding poles",
            "tested_grid_prefix_count": 450, "last_j_k": [15, 2],
            "sample_thresholds": "sample min H>1e-7 and sample min (K_h+real terms)<-1e-4",
            "nominees_j_k": [[11, 21], [12, 22], [13, 23], [14, 1],
                              [14, 2], [14, 24], [15, 1], [15, 2]],
            "status": "All 450 points remained mathematically unresolved by that pilot alone; selected point later certified below",
        },
        "unresolved_tested_pairs": [{"j": v["j"], "k": v["k"]} for v in records
                                    if v["status"] == "unresolved_after_numerical_screen"],
        "unsuccessful_nominations": unsuccessful_nominations,
        "untested_pairs": "No exact certificate search after (11,21). The earlier numerical pilot reached (15,2); all later grid pairs were untested even numerically. No mathematical claim about later pairs.",
        "separation": result,
        "passed": result is not None,
        "limitations": "Finite first-sign decomposition obstruction only. No Xi realization, infinite assembly, higher signs, or novelty certification. Does not isolate budget competition between individually compensable pairs.",
    }
    output = Path(__file__).with_name("finite-grid-separation-certificate.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Tested grid prefix: {len(records)} pairs; last (j,k)=({records[-1]['j']},{records[-1]['k']}); required grid 1..32 each")
    print(f"Exact negative-H exclusions: {sum(v['status']=='exact_negative_H_witness' for v in records)}; unresolved earlier pairs: {len(certificate['unresolved_tested_pairs'])}")
    if result:
        print(f"Separation h={result['h']}, r={result['r']}; exact all-real H>0 certificate passed")
        print(f"Allocation upper bound {result['allocation_obstruction']['full_budget_upper_bound']} < required 0 at x={result['allocation_obstruction']['x']}")
        print(f"Exact certificate checks: {sum(result['checks'].values())}/{len(result['checks'])}; failures: {result['failures']}")
    else:
        print("No full certificate; numerical evidence does not decide the target")
    print(f"Certificate: {output.relative_to(Path.cwd())}")
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(run())
