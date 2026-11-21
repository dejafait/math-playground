#!/usr/bin/env python3
"""Outward scalar certificate for C997v; NOT a residual lower bound.

Run from riemann: python3 scripts/adaptive-slope/two-center-hermite-envelope-383.py
Only standard-library exact fractions and outward Decimal intervals are used.
"""
import json
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path

getcontext().prec = 80


def down(x):
    return x.next_minus()


def up(x):
    return x.next_plus()


class I:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)

    @staticmethod
    def rational(q):
        q = F(q)
        x = Decimal(q.numerator) / Decimal(q.denominator)
        return I(down(x), up(x))

    def __add__(self, other):
        return I(down(self.lo + other.lo), up(self.hi + other.hi))

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        p = [x*y for x in (self.lo, self.hi) for y in (other.lo, other.hi)]
        return I(down(min(p)), up(max(p)))

    def log(self):
        assert self.lo > 0
        # Decimal.ln is correctly rounded in ROUND_HALF_EVEN; one outward
        # neighboring representable value encloses its exact value.
        return I(down(self.lo.ln()), up(self.hi.ln()))

    def saved(self):
        return {"lower": str(self.lo), "upper": str(self.hi)}


def trig(q, cosine=False):
    """12-term alternating Taylor sum plus its exact next-term bound."""
    q = F(q)
    assert 0 < q < 1
    term = F(1) if cosine else q
    total = F(0)
    for k in range(12):
        total += term
        j = 2*k if cosine else 2*k+1
        term *= -q*q/F((j+1)*(j+2))
    lower, upper = sorted((total, total+term))
    a, b = I.rational(lower), I.rational(upper)
    return I(a.lo, b.hi), {"argument": str(q), "cosine": cosine,
                          "terms": 12, "lower_exact": str(lower),
                          "upper_exact": str(upper)}


q = I.rational
n0 = 1024
h = F(n0+1, 8*n0)
R = F(1, 5)
geometry = {
    "h_max": h,
    "s_minus_R_lower": 1-h*h/2-R,
    "pair_product_lower": R*R-h*h,
    "extra_factor_lower": R-h,
    "upper_window_radius_bound": F(3, 16)+F(3, 4*n0)+h*h/2,
    "lower_window_radius_bound": h+F(1, 4*n0)+h*h/2,
}
cos_h, cos_proof = trig(F(1, 8), cosine=True)
sin_h, sin_proof = trig(F(1, 8))
sin_5, sin5_proof = trig(F(5, 32))
sin_1, sin1_proof = trig(F(1, 32))

# M_n <= (100/7) exp(B n), for the prescribed radius-1/5 contour.
B = (q(F(-3, 16)) + q(F(7, 2))*q(F(100, 79)).log()
     + q(F(10, 79)) + q(F(1, 2))*q(F(125, 3)).log())
upper_spectral = B + q(F(1, 2))*q(F(5, 256)).log()
upper_complete = upper_spectral + q(F(9, 32))
lower_at_onset = B-q(4).log()-q(F(1, 2))*q(n0).log()-q(F(1, 16))

# A LOWER bound on the asymptotic rate of the chosen nonnegative
# sup-times-product/TV UPPER ENVELOPE. It is not a lower bound on error.
left_rate = (q(F(-3, 16))-q(F(7, 2))*(cos_h-q(R)).log()
             -q(F(1, 2))*(q(R*R)+sin_h*sin_h).log())
endpoint_product_rate = q(F(1, 2))*(q(4)*sin_5*sin_1).log()
envelope_barrier = left_rate+endpoint_product_rate+q(F(9, 32))

checks = {
    "s_minus_R_gt_79_100": geometry["s_minus_R_lower"] > F(79, 100),
    "pair_product_gt_3_125": geometry["pair_product_lower"] > F(3, 125),
    "extra_factor_gt_7_100": geometry["extra_factor_lower"] > F(7, 100),
    "upper_radius_lt_79_400": geometry["upper_window_radius_bound"] < F(79, 400),
    "lower_radius_lt_79_400": geometry["lower_window_radius_bound"] < F(79, 400),
    "nodes_enclosed": h < R,
    "B_lt_8_3": B.hi < q(F(8, 3)).lo,
    "coarse_upper_complete_rate_positive": upper_complete.lo > 0,
    "lower_at_onset_lt_minus_1": lower_at_onset.hi < -1,
    "envelope_barrier_gt_3_8": envelope_barrier.lo > q(F(3, 8)).hi,
}
values = {"B": B, "upper_spectral_rate": upper_spectral,
          "upper_complete_rate": upper_complete,
          "lower_complete_rate_at_n0_before_polynomial": lower_at_onset,
          "left_contour_rate": left_rate,
          "endpoint_node_product_rate": endpoint_product_rate,
          "envelope_barrier_rate": envelope_barrier}
out = {
    "scope": "Scalar enclosures for an explicit Hermite upper envelope; no actual-residual lower bound or RH assertion.",
    "n0": n0,
    "geometry_exact": {k: str(v) for k, v in geometry.items()},
    "trigonometric_certificates": [cos_proof, sin_proof, sin5_proof, sin1_proof],
    "values": {k: v.saved() for k, v in values.items()},
    "checks": checks,
    "summary": {"passed": sum(checks.values()), "total": len(checks),
                "failures": [k for k, v in checks.items() if not v],
                "required_complete_rate": "<= -1/64 with strict slack for polynomial prefactors",
                "achieved_coarse_complete_upper_rate": upper_complete.saved(),
                "exact_sup_envelope_lower_rate": envelope_barrier.saved(),
                "decision": "Lower window paid; upper-window absolute contour envelope fails; actual complete residual unresolved."},
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out, indent=2)+'\n')
print(f"Scalar checks: {sum(checks.values())}/{len(checks)}; failures: {out['summary']['failures']}")
print(f"Upper complete envelope exponent: [{upper_complete.lo:.12f}, {upper_complete.hi:.12f}]; required < -0.015625")
print(f"Exact-sup envelope lower exponent: [{envelope_barrier.lo:.12f}, {envelope_barrier.hi:.12f}] > 3/8; this is NOT a residual lower bound")
print(f"Certificate: {path}")
if not all(checks.values()):
    raise SystemExit(1)
