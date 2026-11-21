#!/usr/bin/env python3
"""Exact polynomial checks for C467n; no numerical or analytic certification."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

# Sparse polynomials over Q, with monomials represented by sorted name tuples.
def add(*terms):
    out = {}
    for p in terms:
        for mon, value in p.items():
            out[mon] = out.get(mon, F(0)) + value
    return {mon: value for mon, value in out.items() if value}

def mul(*terms):
    out = {(): F(1)}
    for p in terms:
        nxt = {}
        for ma, va in out.items():
            for mb, vb in p.items():
                mon = tuple(sorted(ma + mb))
                nxt[mon] = nxt.get(mon, F(0)) + va * vb
        out = {mon: value for mon, value in nxt.items() if value}
    return out

def con(value):
    return {(): F(value)} if value else {}

def var(name):
    return {(name,): F(1)}

def neg(p):
    return mul(con(-1), p)

def sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))

def det(rows):
    return add(*(mul(con(sign(p)), *(rows[i][p[i]] for i in range(3))) for p in permutations(range(3))))

def cols_det(columns):
    return det([[columns[j][i] for j in range(3)] for i in range(3)])

def serialize(p):
    return [{"monomial": list(mon), "coefficient": str(value)} for mon, value in sorted(p.items())]

checks = []
def check(name, residual, required="zero polynomial over Q"):
    checks.append({"name": name, "actual_residual": serialize(residual), "required": required, "passed": not residual})

s, d = var("s"), var("d")
abar = {j: var("a_" + j) for j in "tch"}
gam = {j: var("g_" + j) for j in "tch"}
dd = {j: var("d_" + j) for j in "tch"}
z = {}
for j in "tch":
    middle = add(abar[j], mul(con(F(-1, 2)), gam[j]))
    z[j] = [add(middle, neg(mul(s, dd[j]))), add(middle, mul(s, dd[j])), add(abar[j], gam[j])]
z["s"] = [neg(d), d, {}]

def wedge(a, b):
    return add(mul(abar[a], gam[b]), neg(mul(abar[b], gam[a])))

for label, order, expected in [
    ("spatial A", "csh", mul(con(3), d, wedge("c", "h"))),
    ("mixed U", "tsh", mul(con(3), d, wedge("t", "h"))),
    ("mixed V", "tcs", mul(con(-3), d, wedge("t", "c"))),
    ("mixed B", "tch", mul(con(3), s, det([[abar[j] for j in "tch"], [dd[j] for j in "tch"], [gam[j] for j in "tch"]]))),
]:
    check(label, add(cols_det([z[j] for j in order]), neg(expected)))

for name, order, expected in [("phi_t A", [0, 1, 2, 3], 1), ("phi_c U", [1, 0, 2, 3], -1), ("phi_s B", [2, 0, 1, 3], 1), ("phi_h V", [3, 0, 1, 2], -1)]:
    check("wedge sign " + name, con(sign(order) - expected))

k, r = var("k"), var("r")
amp = add(mul(con(F(1, 3)), k, k), con(6))
cubic = add(mul(r, r, r), neg(mul(amp, r)), mul(con(F(-2, 27)), k, k, k))
den = add(mul(con(3), r, r), neg(amp))
num = mul(con(F(2, 3)), k, add(r, mul(con(F(1, 3)), k)))
disc = add(mul(con(4), amp, amp, amp), mul(con(F(-4, 27)), k, k, k, k, k, k))
disc_target = mul(con(8), add(mul(k, k, k, k), mul(con(18), k, k), con(108)))
check("cubic discriminant", add(disc, neg(disc_target)))
check("physical-time root derivative modulo cubic", add(mul(con(F(1, 2)), add(mul(r, den), neg(mul(k, num)))), mul(con(-6), r), mul(con(F(-3, 2)), cubic)))
check("s-velocity identity modulo cubic", add(mul(con(2), amp, add(r, mul(con(F(1, 3)), k))), neg(mul(r, den)), mul(con(-4), k), mul(con(3), cubic)))
check("positive obstruction factor numerator at k=1", add(mul(con(6), add(r, con(F(1, 3)))), mul(con(-6), r), con(-2)))

f, fp, fpp, h = map(var, ("f", "fp", "fpp", "h"))
left = add(f, mul(con(F(-1, 3)), h, fp), mul(con(F(1, 18)), h, h, fpp))
right = add(f, mul(con(F(2, 3)), h, fp), mul(con(F(2, 9)), h, h, fpp))
product = mul(left, left, right)
def h_coefficient(p, degree):
    return {tuple(v for v in mon if v != "h"): value for mon, value in p.items() if mon.count("h") == degree}
check("initial bump linear coefficient", h_coefficient(product, 1))
curvature = add(mul(f, f, fpp), neg(mul(f, fp, fp)))
check("initial bump quadratic coefficient", add(h_coefficient(product, 2), mul(con(F(-1, 3)), curvature)))

result = {
    "scope": "Exact algebra supporting C467n(12),(20),(21),(26),(28),(32); not a proof of root-flow hypotheses, limiting arguments or independent review.",
    "checks": checks,
    "checks_passed": sum(item["passed"] for item in checks),
    "checks_required": len(checks),
    "failures": [item["name"] for item in checks if not item["passed"]],
    "analytic_obligations": ["actual smooth coefficient expansion and trace identification", "nonzero real denominators only in the positive interior", "differentiated scaled remainders", "joint smoothness and sequential limits", "positive bump component contradiction"],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(f"Exact algebra: {result['checks_passed']}/{result['checks_required']} passed; required residual in every check: zero polynomial.")
print(f"Failures: {result['failures']}; full certificate: {path}")
raise SystemExit(bool(result["failures"]))
