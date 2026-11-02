#!/usr/bin/env python3
"""Independent exact finite algebra for the L635 conceptual audit.

Uses no notebook calculation imports. Full homogeneous six-subset
numerators are divided by the product Vandermonde, then differentiated
by the original Q and observer operators without assuming symmetry.
Analytic uniformity and transfer are proved in the canonical audit text.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "full_observer_row_budget_certificate.json"
OUT = HERE / "full_observer_row_budget_audit_certificate.json"
ZERO = (0, 0, 0, 0)


def add(p, nu, value):
    p[nu] = p.get(nu, F(0)) + value
    if not p[nu]:
        del p[nu]


def multiply(p, q):
    result = {}
    for nu, a in p.items():
        for mu, b in q.items():
            add(result, tuple(x+y for x, y in zip(nu, mu)), a*b)
    return result


def difference(i, j):
    a, b = list(ZERO), list(ZERO)
    a[i], b[j] = 1, 1
    return {tuple(a): F(1), tuple(b): F(-1)}


def divide(p, q):
    work, result = dict(p), {}
    leading = max(q)
    while work:
        top = max(work)
        nu = tuple(a-b for a, b in zip(top, leading))
        if min(nu) < 0:
            raise ArithmeticError("Nonzero Vandermonde remainder")
        value = work[top]/q[leading]
        add(result, nu, value)
        for mu, c in q.items():
            add(work, tuple(a+b for a, b in zip(nu, mu)), -value*c)
    if multiply(result, q) != p:
        raise ArithmeticError("Vandermonde multiplication replay failed")
    return result


def indices(degree):
    for a in range(degree+1):
        for b in range(degree-a+1):
            for c in range(degree-a-b+1):
                yield a, b, c, degree-a-b-c


def orbit(nu):
    return sorted({a+b for a, b in product(
        (nu[:2], nu[1::-1]), (nu[2:], nu[:1:-1]))})


def derivative_at_zero(p, nu):
    result = p.get(nu, F(0))
    for k in nu:
        result *= factorial(k)
    return result


def original_operator(p, channel):
    # Q_b = (d_z1^2 + d_z2^2)/2 - d_z1 d_z2.
    q = {(2, 0, 0, 0): F(1, 2), (0, 2, 0, 0): F(1, 2),
         (1, 1, 0, 0): F(-1)}
    observers = ({ZERO: F(1)},
                 {(0, 0, 1, 0): F(1), (0, 0, 0, 1): F(1)},
                 {(0, 0, 1, 1): F(-1)})
    # Channel 1 has the factor i outside its rational coefficient;
    # channel 2 includes i^2=-1 here.
    return sum((c*derivative_at_zero(p, nu)
                for nu, c in multiply(q, observers[channel]).items()), F(0))


def main():
    source_bytes = SOURCE.read_bytes()
    old = json.loads(source_bytes)
    old_rows = {tuple(r["nu"]): r for r in old["rows"]}
    old_divisions = {(tuple(r["nu"]), r["output_degree"]): r
                     for r in old["full_polynomial_replay"]}
    delta = {ZERO: F(1)}
    for i, j in combinations(range(4), 2):
        delta = multiply(delta, difference(i, j))
    subsets = []
    for chosen in combinations(range(4), 2):
        other = tuple(j for j in range(4) if j not in chosen)
        cross = {ZERO: F(1)}
        for i in chosen:
            for j in other:
                cross = multiply(cross, difference(i, j))
        prefactor = divide(delta, cross)
        exponentials = []
        for degree in range(9):
            exp = {}
            for nu in indices(degree):
                c = F(1)
                for j, power in enumerate(nu):
                    c *= (F(1, 2) if j in chosen else F(-1, 2))**power/factorial(power)
                exp[nu] = c
            exponentials.append(exp)
        subsets.append((chosen, other, prefactor, exponentials))

    rows, divisions, lookup = [], [], {}
    maxima = [F(0)]*9
    for degree in range(9):
        for nu in indices(degree):
            if nu[0] < nu[1] or nu[2] < nu[3]:
                continue
            members = orbit(nu)
            weights = []
            for channel, output in enumerate((2, 3, 4)):
                numerator = {}
                exponential_degree = output+4-degree
                if exponential_degree >= 0:
                    for chosen, other, prefactor, exp in subsets:
                        arithmetic = {}
                        for mu in members:
                            power = [0]*4
                            for j, k in zip(chosen+other, mu):
                                power[j] = k
                            add(arithmetic, tuple(power), F((-1)**sum(mu[2:])))
                        term = multiply(multiply(prefactor, arithmetic), exp[exponential_degree])
                        for power, c in term.items():
                            add(numerator, power, c)
                quotient = divide(numerator, delta)
                value = original_operator(quotient, channel)
                weights.append(value)
                prior = old_divisions[(nu, output)]
                prior_q = {tuple(r["nu"]): F(r["value"]) for r in prior["quotient"]}
                divisions.append({"nu": list(nu), "output_degree": output,
                    "quotient": [{"nu": list(k), "value": str(v)} for k, v in sorted(quotient.items())],
                    "original_operator_weight": str(value),
                    "full_quotient_matches": quotient == prior_q,
                    "weight_matches": value == F(prior["weight"]),
                    "homogeneous": all(sum(k) == output for k in quotient)})
            lookup[nu] = tuple(weights)
            o = len(members)
            aa, dd, jj = 180*abs(weights[0])/o, 5040*abs(weights[2])/o, 1008*abs(weights[1])/o
            bound = max(aa, dd)+jj/2
            maxima[degree] = max(maxima[degree], bound)
            prior = old_rows[nu]
            rows.append({"nu": list(nu), "orbit": [list(mu) for mu in members],
                "weights": list(map(str, weights)), "joint_bound": str(bound),
                "all_prior_row_values_match": (degree == prior["degree"] and o == prior["orbit_size"]
                    and weights == list(map(F, prior["weights"]))
                    and aa == F(prior["normalized_abs_c0_diagonal"])
                    and dd == F(prior["normalized_abs_c1_diagonal"])
                    and jj == F(prior["imaginary_cross_upper_bound"])
                    and bound == F(prior["uniform_observer_bound"]))})

    exponent = [F(0)]+[F(4, factorial(k))+(2 if k == 1 else 0) for k in range(1, 9)]
    power, majorant = [F(1)]+[F(0)]*8, [F(1)]+[F(0)]*8
    for j in range(1, 9):
        power = [sum((power[i]*exponent[k-i] for i in range(k+1)), F(0)) for k in range(9)]
        majorant = [a+b/factorial(j) for a, b in zip(majorant, power)]
    costs = [maxima[k]*majorant[k]/100**k for k in range(1, 9)]
    total = sum(costs, F(0))
    checks = {
        "175_complete_orbits": len(rows) == 175 and set(lookup) == set(old_rows),
        "495_multiindices": sum(len(r["orbit"]) for r in rows) == 495,
        "525_full_divisions": len(divisions) == 525,
        "every_quotient_matches": all(r["full_quotient_matches"] for r in divisions),
        "every_original_operator_weight_matches": all(r["weight_matches"] for r in divisions),
        "every_quotient_homogeneous": all(r["homogeneous"] for r in divisions),
        "every_observer_row_matches": all(r["all_prior_row_values_match"] for r in rows),
        "zero_reference": lookup[ZERO] == (F(1, 180), F(0), F(1, 5040)),
        "all_pair_exchange_signs": all(lookup[nu[2:]+nu[:2]] == (w[0], -w[1], w[2])
                                       for nu, w in lookup.items()),
        "maxima_match": maxima == list(map(F, old["degreewise_maxima"])),
        "majorant_matches": majorant == list(map(F, old["majorant_coefficients"])),
        "all_degree_costs_match": costs == list(map(F, old["contraction"]["degree_costs"])),
        "exact_total_matches": total == F(old["contraction"]["total_exact"]),
        "arithmetic_slack_positive": total < F(2, 5),
        "reserve_and_half_budget": F(2, 5)+F(1, 20) == F(9, 20) < F(1, 2),
        "absolute_transfer_power_differences": (F(17, 80)-F(1, 20), F(199, 100)-F(1, 20))
                                                == (F(13, 80), F(97, 50)),
    }
    failures = [key for key, value in checks.items() if not value]
    certificate = {
        "scope": "Independent finite L635 audit; analytic uniformity and transfer require the canonical proofs. No RH or finite-onset certificate.",
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "method": "Full Vandermonde products and homogeneous quotients; original differential operators; no notebook calculation imports.",
        "rows": rows, "full_divisions": divisions,
        "degreewise_maxima": list(map(str, maxima)), "majorant_coefficients": list(map(str, majorant)),
        "contraction": {"degree_costs": list(map(str, costs)), "total_exact": str(total),
            "arithmetic_slack": str(F(2, 5)-total), "eventual_arithmetic_bound": "2/5",
            "relative_transfer_reserve": "1/20", "eventual_full_bound": "9/20", "required_bound": "1/2"},
        "checks": checks, "failures": failures,
    }
    OUT.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"Orbits: {len(rows)}; full divisions: {len(divisions)}; checks: {len(checks)}")
    print(f"Actual sufficient cost: {total}; eventual arithmetic: 2/5; full: 9/20; required: 1/2")
    print(f"Failures: {failures}; certificate: {OUT.relative_to(HERE.parents[1])}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
