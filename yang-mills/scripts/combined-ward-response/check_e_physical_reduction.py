"""Exact polynomial and spectral-tail arithmetic checks for L134."""

from fractions import Fraction
import json
from pathlib import Path


def add(a, b):
    result = dict(a)
    for power, value in b.items():
        result[power] = result.get(power, 0) + value
        if result[power] == 0:
            del result[power]
    return result


def scale(a, value):
    return {power: coefficient * value for power, coefficient in a.items()
            if coefficient * value}


def mul(a, b):
    result = {}
    for pa, ca in a.items():
        for pb, cb in b.items():
            power = tuple(x + y for x, y in zip(pa, pb))
            result[power] = result.get(power, 0) + ca * cb
    return {power: coefficient for power, coefficient in result.items()
            if coefficient}


def encode(a):
    return {",".join(map(str, power)): coefficient
            for power, coefficient in sorted(a.items())}


one = {(0, 0, 0): 1}
X, Y, Z = ({(1, 0, 0): 1}, {(0, 1, 0): 1}, {(0, 0, 1): 1})
L = add(add(X, Y), Z)
squares = add(add(mul(X, X), mul(Y, Y)), mul(Z, Z))
# P_j=4 L p_j, Q=8 L q, H_j=4 L h_j.
px = add(add(scale(L, -2), mul(X, L)), scale(mul(X, X), -1))
py = add(add(scale(L, -2), mul(Y, L)), scale(mul(Y, Y), -1))
q = add(scale(L, -4), scale(squares, -1))
hx = mul(add(scale(one, 4), scale(X, -1)), add(L, scale(X, -1)))
hy = mul(add(scale(one, 4), scale(Y, -1)), add(L, scale(Y, -1)))
diff = add(X, scale(Y, -1))
identities = [
    ("8L(q-p3)", add(q, scale(py, -2)),
     add(scale(mul(L, L), -1), scale(mul(X, Z), 2))),
    ("4L(p2-p3)", add(px, scale(py, -1)), mul(diff, Z)),
    ("4L(h2-h3)", add(hx, scale(hy, -1)),
     scale(mul(diff, add(Z, scale(one, 4))), -1)),
]
records = [dict(identity=name, actual=encode(actual), required=encode(required),
                difference=encode(add(actual, scale(required, -1))),
                passed=actual == required)
           for name, actual, required in identities]
C_U = Fraction(1296 * 165 * 3, 4)
C_W = Fraction(1512 * (18150 + 165 + 18150), 4)
combined = C_U + Fraction(7, 4) * C_W
bound = combined * 1640736 * 2717908992 / 20**27
required = Fraction(1, 10**12)


def rational(value):
    return dict(numerator=value.numerator, denominator=value.denominator)


certificate = dict(
    method="exact integer polynomial coefficients and rational arithmetic",
    qualification="No retained scalar/physical integration or processor audit.",
    polynomial_identities=records,
    tail=dict(cutoff=96, C_U=rational(C_U), C_W=rational(C_W),
              combined_amplitude=rational(combined), full_probe_norm=1640736,
              H_prefactor=2717908992, exponential_majorant=rational(Fraction(1, 20**27)),
              actual=rational(bound), required=rational(required), passed=bound < required),
)
certificate["passed"] = all(record["passed"] for record in records) and bound < required
path = Path(__file__).with_name("e-physical-tail-arithmetic-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact polynomial identities: {sum(r['passed'] for r in records)}/{len(records)}")
print(f"K=96 full E spectral omission bound: {float(bound):.9g}; required <{float(required):.9g}")
print(f"Failures: {[r['identity'] for r in records if not r['passed']]}")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(0 if certificate["passed"] else 1)
