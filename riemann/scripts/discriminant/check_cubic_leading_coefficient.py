#!/usr/bin/env python3
"""Exact finite algebra for L408; analytic endpoint estimates are not tested."""
from fractions import Fraction as F
from math import factorial, gcd
from pathlib import Path
import json

ZERO = (0, 0, 0)


def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = out.get(key, F(0)) + value
    return {key: value for key, value in out.items() if value}


def scale(poly, value):
    return {key: value * coeff for key, coeff in poly.items() if value * coeff}


def mul(*polys):
    out = {ZERO: F(1)}
    for poly in polys:
        new = {}
        for key, value in out.items():
            for other, coeff in poly.items():
                powers = tuple(a + b for a, b in zip(key, other))
                new[powers] = new.get(powers, F(0)) + value * coeff
        out = {key: value for key, value in new.items() if value}
    return out


def records(poly):
    return [{"powers": list(key), "coefficient": str(value)}
            for key, value in sorted(poly.items())]


X = {(1, 0, 0): F(1)}
Y = {(0, 1, 0): F(1)}
Z = {(0, 0, 1): F(1)}
D2 = add(scale(Z, -1), scale(Y, -1), scale(X, F(-1, 4)))
A = add(Y, scale(X, F(1, 2)))  # D1=i*A, hence D1^2=-A^2
Jplus = add(D2, scale(X, F(-1, 4)), scale(A, -1))
Jminus = add(D2, scale(X, F(-1, 4)), A)
M = scale(add(mul(D2, D2), scale(mul(X, D2), F(3, 2)),
              scale(mul(X, X), F(1, 16)), mul(A, A)), F(1, 2))
P1 = add(mul(M, Jplus), scale(mul(Jplus, Jplus, Jminus), F(1, 4)))
Q = add(mul(Y, Y), scale(mul(Y, Z), F(3, 2)),
        scale(mul(Z, Z), F(3, 4)), scale(mul(X, Z), F(-1, 4)))
P1_factored = scale(mul(add(X, scale(Y, 2), Z), Q), -1)
residual = add(P1, scale(P1_factored, -1))
terms = []
total = F(0)
for nu, coeff in sorted(P1.items()):
    p = [0] * nu[0] + [1] * nu[1] + [2] * nu[2]
    d = sum(p)
    moment = F((-1) ** d, factorial(d + 2))
    for order in p:
        moment *= factorial(order)
    contribution = coeff * moment
    total += contribution
    terms.append({"nu": list(nu), "ordinary_orders": p, "d": d,
                  "weight_coefficient": str(coeff), "polar_moment": str(moment),
                  "contribution": str(contribution)})

# Orthogonality reduces the full three-class phase sum to a two-class count.
# Its exact normalized value is sum_a gcd(a,u)/u^2; compare the count directly.
moduli = []
for u in range(1, 41):
    count = sum((a * b) % u == 0 for a in range(1, u + 1)
                for b in range(1, u + 1))
    gcd_sum = sum(gcd(a, u) for a in range(1, u + 1))
    moduli.append({"u": u, "pair_count": count, "gcd_sum": gcd_sum,
                   "A_u": str(F(gcd_sum, u * u)), "equal": count == gcd_sum})
tests = {
    "P1_complete_factorization": not residual,
    "Jplus_exact": Jplus == add(scale(Z, -1), scale(Y, -2), scale(X, -1)),
    "Jminus_exact": Jminus == scale(Z, -1),
    "all_monomials_cubic": all(sum(nu) == 3 for nu in P1),
    "complete_polar_sum": total == F(17, 20160),
    "positive_polar_sum": total > 0,
    "finite_residue_count_checks": all(row["equal"] for row in moduli),
}
certificate = {
    "lemma": "L408", "domain": "exact rational arithmetic",
    "variables": ["h0", "h1/log H", "h2/(log H)^2"],
    "P1": records(P1), "factorization_residual": records(residual),
    "polar_terms": terms, "polar_sum": str(total), "tests": tests,
    "residue_count_checks": moduli,
    "analytic_obligations_reference_only": {
        "weight_error": "O_N(H log H)",
        "smooth_divisor_error": "O_{u,nu,psi}(X(log X)^(d+1)+X^(1/2))",
        "sharp_transfer": "fixed boundary width, H limit first, width limit second",
        "required_total_error": "o_N(H(log H)^2)",
        "proof": "lemmas/L408-fixed-head-cubic-positive-leading-coefficient.md",
    },
}
path = Path(__file__).with_name("cubic-leading-coefficient-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
failures = [key for key, passed in tests.items() if not passed]
print(f"Exact checks: {len(tests)-len(failures)}/{len(tests)}; failures: {failures}")
print(f"Signed polar coefficient: {total}; required: complete signed value (zero allowed).")
print(f"Factorization residual size: {len(residual)}; required: 0. Moduli checked: 1..40.")
print("Analytic error required: o_N(H(log H)^2); see written proof, not this certificate.")
print(f"Certificate: {path}")
raise SystemExit(bool(failures))
