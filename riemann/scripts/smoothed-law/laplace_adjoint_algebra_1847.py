#!/usr/bin/env python3
"""Exact polynomial checks for attempt1847; no zero data or sign certificate for C."""
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a):
        c[i] += v
    for i, v in enumerate(b):
        c[i] += v
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c


def scale(a, s):
    return [s*v for v in a]


def mul(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return c


def power(a, n):
    c = [1]
    for _ in range(n):
        c = mul(c, a)
    return c


def diff(a):
    return [i*a[i] for i in range(1, len(a))] or [0]


def shift_one(a):
    return [sum(a[i]*comb(i, j) for i in range(j, len(a)))
            for j in range(len(a))]


def value(a, t):
    return sum(v*t**i for i, v in enumerate(a))


t = [0, 1]
n1, n2 = [1, 4, 5, 10], [8, 16, 10, 10]
den_l = mul(mul(t, power([1, 1], 2)), [1, 3])
l_deriv = add(mul(diff(n1), den_l), scale(mul(n1, diff(den_l)), -1))
s_minus_r = add(mul(mul(n2, power([1, 1], 2)), [1, 3]),
                scale(mul(mul(n1, power([2, 1], 2)), [2, 3]), -1))
r_deriv_sign = [-2, 9, 15]
checks = {
    "ell_derivative_strictly_negative_t_positive": all(c < 0 for c in l_deriv),
    "s_minus_r_strictly_negative_t_ge_1": all(c < 0 for c in shift_one(s_minus_r)),
    "r_derivative_strictly_positive_t_ge_1": all(c > 0 for c in shift_one(r_deriv_sign)),
    "s_minus_r_inner_at_1": value(s_minus_r, 1) == -196,
}
# ell'(t)=6*l_deriv/den_l^2;
# s-r=2*(t+1)^2*s_minus_r/[n1*(t+2)^4*(3t+1)].
certificate = {
    "scope": "Exact rational algebra only; C034c(20) remains unproved.",
    "coefficient_order": "ascending powers of t; shifted means t=u+1",
    "ell_numerator_without_6": n1,
    "ell_denominator": den_l,
    "ell_derivative_numerator_without_6": l_deriv,
    "s_minus_r_inner_numerator": s_minus_r,
    "s_minus_r_inner_shifted": shift_one(s_minus_r),
    "r_derivative_sign_shifted": shift_one(r_deriv_sign),
    "at_x_y_1": {
        "Q1": "4", "Q2": "40/9", "Q1_second": "30",
        "Q2_second": "704/27", "symmetric_kernel": str(Fraction(4*704, 27)-Fraction(40*30, 9)),
    },
    "checks": checks,
    "failures": [k for k, ok in checks.items() if not ok],
    "actual_bound": "Bulk curvature <= 2 integral integral p_+(x)p_-(y)(-K(x,y)) dx dy, x,y>=1",
    "required_bound": "Full curvature including all origin corrections <= S4^3/5 uniformly on [1,2]",
    "threshold_certified": False,
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact rational checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print("Actual: negative rational bulk kernel on [1,infinity)^2; signed-profile cross term remains.")
print("Required: full curvature <= S4^3/5; NOT certified.")
print(f"Certificate: {out.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)
