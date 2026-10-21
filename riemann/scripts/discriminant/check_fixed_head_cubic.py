#!/usr/bin/env python3
"""Exact formal carrier checks for L407; no analytic certification."""
from fractions import Fraction as F
from pathlib import Path
import json

# Exponents: x,y,z,R,Z,Zbar,i. R is Laurent; i^2=-1.
ZERO = (0,) * 7


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
                powers = [a + b for a, b in zip(key, other)]
                sign = (-1) ** (powers[6] // 2)
                powers[6] %= 2
                powers = tuple(powers)
                new[powers] = new.get(powers, F(0)) + sign * value * coeff
        out = {key: value for key, value in new.items() if value}
    return out


def var(index, power=1):
    key = list(ZERO)
    key[index] = power
    return {tuple(key): F(1)}


def star(poly):
    out = {}
    for key, value in poly.items():
        powers = list(key)
        powers[3] *= -1
        powers[4], powers[5] = powers[5], powers[4]
        out[tuple(powers)] = value * (-1) ** powers[6]
    return out


def records(poly):
    return [{"powers": list(key), "coefficient": str(value)}
            for key, value in sorted(poly.items())]


x, y, z, R, Z, Zbar, i = [var(j) for j in range(7)]
b = add(z, scale(x, F(-1, 4)))
plus, minus = add(b, mul(i, y)), add(b, scale(mul(i, y), -1))
M = scale(add(mul(z, z), scale(mul(x, z), F(3, 2)),
              scale(mul(x, x), F(1, 16)), scale(mul(y, y), -1)), F(1, 2))
K = scale(mul(minus, minus), F(1, 2))
positive_response = mul(R, Z)
negative_response = mul(var(3, -1), Zbar)
d = add(mul(M, Z, Zbar),
        scale(add(mul(K, positive_response, positive_response),
                  mul(star(K), negative_response, negative_response)), F(1, 2)))
B0 = scale(add(mul(minus, positive_response),
               mul(plus, negative_response)), F(-1, 2))
P1 = add(mul(M, plus), scale(mul(plus, plus, minus), F(1, 4)))
P0 = scale(mul(plus, plus, plus), F(1, 4))
selected = scale(add(mul(P1, var(3, -1), Zbar, Zbar, Z),
                     mul(P0, var(3, -3), Zbar, Zbar, Zbar)), -1)
paired = scale(add(selected, star(selected)), F(1, 2))
paired_residual = add(mul(d, B0), scale(paired, -1))

# Replace (x,y,z) by -R(D0,D1,D2), then relabel x,y,z as D0,D1,D2.
substituted = {}
for key, value in selected.items():
    degree = sum(key[:3])
    powers = list(key)
    powers[3] += degree
    substituted[tuple(powers)] = value * (-1) ** degree
expected = add(mul(P1, var(3, 2), Zbar, Zbar, Z),
               mul(P0, Zbar, Zbar, Zbar))
substitution_residual = add(substituted, scale(expected, -1))
Q = add(scale(mul(z, z), F(3, 4)), scale(mul(x, z), F(5, 8)),
        scale(mul(x, x), F(3, 64)), scale(mul(y, y), F(-1, 4)))
factorization_residual = add(P1, scale(mul(plus, Q), -1))
tests = {
    "complete_real_pairing": not paired_residual,
    "ordinary_jet_carrier_substitution": not substitution_residual,
    "P1_factorization": not factorization_residual,
    "only_zero_and_single_carriers": sorted({key[3] for key in expected}) == [0, 2],
    "all_critical_degrees_three": all(sum(key[:3]) == 3 for key in expected),
}
certificate = {
    "lemma": "L407", "coefficient_domain": "Q[i] with i^2=-1",
    "variable_order": ["D0", "D1", "D2", "R", "Z", "Zbar", "i"],
    "tests": tests,
    "paired_residual": records(paired_residual),
    "substitution_residual": records(substitution_residual),
    "factorization_residual": records(factorization_residual),
    "P1": records(P1), "P0": records(P0),
    "carrier_R_powers": sorted({key[3] for key in expected}),
    "analytic_bounds_reference_only": {
        "single_carrier_connector_exponent": "71/120",
        "zero_carrier_connector_exponent": "1/2",
        "source_remainder_exponent": "11/20",
        "required_error": "o(H(log H)^2)",
        "proof": "lemmas/L407-fixed-head-cubic-carrier-compatibility.md",
    },
}
path = Path(__file__).with_name("fixed-head-cubic-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
failures = [key for key, passed in tests.items() if not passed]
print(f"Exact checks: {len(tests)-len(failures)}/{len(tests)}; failures: {failures}")
print(f"Formal R powers: {certificate['carrier_R_powers']}, required [0, 2]; residual sizes: {[len(paired_residual), len(substitution_residual), len(factorization_residual)]}, required [0, 0, 0].")
print("Analytic bounds (proved in L407, not by this script): connectors O_N(H^(71/120)); source O_N(H^(11/20)); required o(H(log H)^2).")
print(f"Certificate: {path}")
raise SystemExit(bool(failures))
