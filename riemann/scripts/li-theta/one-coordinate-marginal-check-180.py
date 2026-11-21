#!/usr/bin/env python3
"""Exact finite algebra for C969a; analytic moment inequalities are in the proof.

Run from the active notebook. No floating point, numerical theta moments,
construction imports, or pre-existing certificates are used.
"""

from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/li-theta/one-coordinate-marginal-check-180.json"
b, h, q = F(1, 4), F(5184), F(72)
delta = h - b
d1, d2 = 4 * h * h / delta**2, h / delta
variables = ("a0", "a1", "c0", "c1", "s")
zero = (0,) * len(variables)


def const(value):
    return {zero: F(value)} if value else {}


def var(index):
    powers = list(zero)
    powers[index] = 1
    return {tuple(powers): F(1)}


def add(*polys):
    result = defaultdict(F)
    for poly in polys:
        for powers, coefficient in poly.items():
            result[powers] += coefficient
    return {powers: value for powers, value in result.items() if value}


def scale(poly, scalar):
    return {powers: value * scalar for powers, value in poly.items() if value * scalar}


def mul(left, right):
    result = defaultdict(F)
    for lp, lc in left.items():
        for rp, rc in right.items():
            result[tuple(x + y for x, y in zip(lp, rp))] += lc * rc
    return {powers: value for powers, value in result.items() if value}


def records(poly):
    return [{"powers": list(powers), "coefficient": str(value)}
            for powers, value in sorted(poly.items())]


a0, a1, c0, c1, s = [var(i) for i in range(5)]
moments = {
    "B0": const(F(1, 2)), "B1": scale(a0, 2), "B2": scale(a1, 4),
    "C0": add(const(F(1, 2)), scale(c0, 2 * delta)),
    "C1": add(scale(c0, 2), scale(c1, 2 * delta)),
}
moment_names = {"B0": "m0", "B1": "m1", "B2": "m2", "C0": "v0", "C1": "v1"}
# Each limit is divided by g=gamma/(4q); s means 1/gamma.
leading = {"B0": const(1), "B1": {}, "B2": {}, "C0": const(1),
           "C1": scale(s, 2 * delta)}
tensors = [
    ("positive_first", d1, ("B1", "B0", "C0")),
    ("positive_second", d2, ("B2", "B0", "C0")),
    ("even_block", -d2, ("B1", "B1", "C0")),
    ("distant_derivative", -d1, ("B0", "B0", "C1")),
]
contracted = defaultdict(F)
placements, term_limits = [], {}
raw_bracket = {}
for name, coefficient, factors in tensors:
    term = {}
    for permutation in permutations(range(3)):
        u, v, w = [factors[i] for i in permutation]
        value = coefficient / 6
        contracted[(moment_names[w], u, v)] += value
        contribution = scale(mul(moments[w], mul(leading[u], leading[v])), 3 * value / d1)
        term = add(term, contribution)
        placements.append({"tensor": name, "permutation": list(permutation),
                           "u": u, "v": v, "integrated": w,
                           "coefficient": str(value),
                           "scaled_limit_contribution": records(contribution)})
    term_limits[name] = records(term)
    raw_bracket = add(raw_bracket, term)

# Independently entered displayed contraction formula for 3 J_2.
displayed = [
    (d1, "m1", "B0", "C0"), (d1, "m0", "B1", "C0"),
    (d1, "v0", "B1", "B0"), (d2, "m2", "B0", "C0"),
    (d2, "m0", "B2", "C0"), (d2, "v0", "B2", "B0"),
    (-2 * d2, "m1", "B1", "C0"), (-d2, "v0", "B1", "B1"),
    (-2 * d1, "m0", "B0", "C1"), (-d1, "v1", "B0", "B0"),
]
expected = defaultdict(F)
for coefficient, moment, f, g in displayed:
    expected[(moment, f, g)] += coefficient / 6
    expected[(moment, g, f)] += coefficient / 6
contraction_residual = {key: contracted[key] - expected[key]
                        for key in contracted.keys() | expected.keys()
                        if contracted[key] != expected[key]}

# Exact normalization: s=1/gamma=2(c0+c1).
normalized = {}
for powers, coefficient in raw_bracket.items():
    replacement = const(coefficient)
    for i, power in enumerate(powers):
        base = add(scale(c0, 2), scale(c1, 2)) if i == 4 else var(i)
        for _ in range(power):
            replacement = mul(replacement, base)
    normalized = add(normalized, replacement)
bracket = add(scale(a0, 2), scale(a1, delta / h),
              scale(c0, -(2 + 4 * delta)), scale(c1, -6 * delta))
upper = add(scale(c0, -4 * delta), scale(c1, -delta * (6 - 1 / h)))
domination_gap = add(scale(add(c0, scale(a0, -1)), 2),
                     scale(add(c1, scale(a1, -1)), delta / h))
normalization_residual = add(normalized, scale(bracket, -1))
domination_residual = add(upper, scale(bracket, -1), scale(domination_gap, -1))
checks = {
    "exactly_24_labeled_placements": len(placements) == 24,
    "complete_contraction_residual_zero": not contraction_residual,
    "normalization_residual_zero": not normalization_residual,
    "moment_domination_residual_zero": not domination_residual,
    "positive_delta": delta > 0,
    "positive_domination_c1_coefficient": 6 - 1 / h > 0,
    "d2_over_d1": d2 / d1 == delta / (4 * h),
    "positive_limit_prefactor": d1 / (48 * q**2) == h / (12 * delta**2) > 0,
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "scope": "Fixed n=2 marginal of complete L969(5); exact finite algebra only.",
    "parameters": {"b": str(b), "h": str(h), "q": str(q), "Delta": str(delta),
                   "d1": str(d1), "d2": str(d2)},
    "polynomial_variables": list(variables),
    "scaling": "raw_bracket = 3 lim[J_2(t,t)/(t exp(qt))^2] / (d1 g^2), g=gamma/(4q)",
    "actual_moments": {factor: records(poly) for factor, poly in moments.items()},
    "placements": placements,
    "contracted_coefficients": [{"moment": key[0], "u": key[1], "v": key[2],
                                 "coefficient": str(value)}
                                for key, value in sorted(contracted.items()) if value],
    "per_tensor_scaled_limits": term_limits,
    "raw_bracket": records(raw_bracket), "normalization": "s=2(c0+c1)",
    "normalized_bracket": records(normalized), "upper_bound": records(upper),
    "upper_minus_bracket": records(domination_gap),
    "residuals": {"contraction": [{"key": list(key), "value": str(value)}
                                  for key, value in sorted(contraction_residual.items())],
                  "normalization": records(normalization_residual),
                  "domination": records(domination_residual)},
    "analytic_requirements": [
        "All slices absolutely integrable; factor moments are those of the actual A.",
        "g>0 and the factor limits in L969(7)-(8) hold with fixed gamma.",
        "c0>=a0>0 and c1>=a1>0 by the nonnegative H_r series, h>b and A>0.",
        "Continuity gives an open negative region from the negative diagonal limit.",
    ],
    "actual_bound": "limit <= -h*gamma^2/[12*Delta] * [4*c0+(6-1/h)*c1] < 0",
    "required_threshold": "Global pointwise nonnegativity would require a nonnegative diagonal limit.",
    "checks": checks, "failures": failures,
}
OUT.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact checks: {sum(checks.values())}/{len(checks)}; labeled placements: {len(placements)}")
print(f"Delta={delta}>0; 6-1/h={6 - 1 / h}>0; all three residuals zero: {not any(certificate['residuals'].values())}")
print("Actual analytic bound: limit <= -h*gamma^2/(12*Delta) [4*c0+(6-1/h)*c1] < 0; required: >=0.")
print("Failures:", failures)
print("Full certificate:", OUT.relative_to(ROOT))
raise SystemExit(bool(failures))
