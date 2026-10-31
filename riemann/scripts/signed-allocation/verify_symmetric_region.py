#!/usr/bin/env python3
"""Exact polynomial checks for L509; the analytic sign proof is in the lemma."""
import json
from fractions import Fraction
from pathlib import Path


def add(*polys):
    out = {}
    for poly in polys:
        for power, coefficient in poly.items():
            out[power] = out.get(power, Fraction(0)) + coefficient
    return {power: c for power, c in out.items() if c}


def scale(poly, coefficient):
    return {power: coefficient * c for power, c in poly.items() if coefficient * c}


def mul(*polys):
    out = {(0, 0): Fraction(1)}
    for poly in polys:
        product = {}
        for (a, y), c in out.items():
            for (b, z), d in poly.items():
                power = (a + b, y + z)
                product[power] = product.get(power, Fraction(0)) + c * d
        out = {power: c for power, c in product.items() if c}
    return out


def derivative_y(poly):
    return {(a, y - 1): y * c for (a, y), c in poly.items() if y}


def encode(poly):
    return [{"a_degree": a, "y_degree": y, "coefficient": str(c)}
            for (a, y), c in sorted(poly.items())]


def evaluate(poly, a, y):
    return sum(c * a**i * y**j for (i, j), c in poly.items())


one = {(0, 0): Fraction(1)}
a = {(1, 0): Fraction(1)}
y = {(0, 1): Fraction(1)}
ym_a = add(y, scale(a, -1))
yp_a = add(y, a)
yp_1 = add(y, one)
N = mul(add(one, scale(y, -1)), ym_a, ym_a)
D = mul(yp_a, yp_1, yp_1)
R = add(scale(mul(y, y), -3), mul(add(one, scale(a, -1)), y), scale(a, 3))
Q = add(mul(y, y), mul(add(a, scale(one, -1)), y), scale(a, 3))

pairs = {
    "derivative_numerator": (
        add(mul(derivative_y(N), D), scale(mul(N, derivative_y(D)), -1)),
        mul(add(a, one), ym_a, yp_1, R)),
    "center_threshold_comparison": (
        add(mul(a, D), scale(N, -1)), mul(add(a, one), y, Q)),
    "one_eighth_bound": (
        add(mul(yp_1, yp_1), scale(mul(y, add(one, scale(y, -1))), -8)),
        mul(add(scale(y, 3), scale(one, -1)), add(scale(y, 3), scale(one, -1)))),
}
identities = {}
for name, (lhs, rhs) in pairs.items():
    difference = add(lhs, scale(rhs, -1))
    identities[name] = {"lhs": encode(lhs), "rhs": encode(rhs),
                        "difference": encode(difference), "passed": not difference}

# a0=7-4 sqrt(3): verify a0^2-14a0+1=0 in Q(sqrt(3)).
u, v = Fraction(7), Fraction(-4)
algebraic_residual = (u*u + 3*v*v - 14*u + 1, 2*u*v - 14*v)
sample_a, sample_y = Fraction(1, 16), Fraction(1, 2)
sample_w = sample_a
sample_f = evaluate(N, sample_a, sample_y) / evaluate(D, sample_a, sample_y)
sample_G = 2 * ((sample_y - 1)/(sample_y + 1)**2
               + sample_w*(sample_y + sample_a)/(sample_y - sample_a)**2)
failures = [name for name, item in identities.items() if not item["passed"]]
if algebraic_residual != (0, 0):
    failures.append("transition_polynomial")
if not sample_f > sample_w or not sample_G < 0:
    failures.append("off_center_negative_witness")

certificate = {
    "purpose": "L509 exact algebra replay; not a substitute for the full real-variable proof",
    "identities": identities,
    "transition": {"a0_basis_1_sqrt3": [str(u), str(v)],
                   "polynomial_residual_basis_1_sqrt3": list(map(str, algebraic_residual))},
    "negative_sample": {"a": str(sample_a), "w": str(sample_w), "x_squared": str(sample_y),
                        "required_w_at_x": str(sample_f), "G": str(sample_G)},
    "failures": failures,
    "passed": not failures,
}
output = Path(__file__).with_name("symmetric-region-certificate.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact identities: {sum(item['passed'] for item in identities.values())}/{len(identities)}")
print(f"Transition residual in Q(sqrt(3)): {algebraic_residual}")
print(f"Negative witness: a=w={sample_a}, x^2={sample_y}; required w={sample_f}; G={sample_G}")
print(f"Failures: {failures}; certificate: {output.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
