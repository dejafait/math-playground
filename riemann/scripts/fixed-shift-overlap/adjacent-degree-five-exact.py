#!/usr/bin/env python3
"""One assessed degree-five Widom specialization; exact rational arithmetic.

Run from the notebook: python3 scripts/fixed-shift-overlap/adjacent-degree-five-exact.py
The certificate contains every subset term, denominator, bound and replay.
The imported Widom and sector theorems are justified in L837, not by samples.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


class Q:
    """a+b*w, w^2=w-1, w=(1+i*sqrt(3))/2."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q) else Q(x)

    def __add__(self, other):
        y = Q.of(other)
        return Q(self.a+y.a, self.b+y.b)

    __radd__ = __add__

    def __neg__(self):
        return Q(-self.a, -self.b)

    def __sub__(self, other):
        return self + -Q.of(other)

    def __mul__(self, other):
        y = Q.of(other)
        return Q(self.a*y.a-self.b*y.b,
                 self.a*y.b+self.b*y.a+self.b*y.b)

    __rmul__ = __mul__

    def conj(self):
        return Q(self.a+self.b, -self.b)

    def norm2(self):
        return self.a*self.a+self.a*self.b+self.b*self.b

    def __truediv__(self, other):
        y = Q.of(other)
        z = self*y.conj()
        return Q(z.a/y.norm2(), z.b/y.norm2())

    def __pow__(self, n):
        assert n >= 0
        ans, x = Q(1), self
        while n:
            if n % 2:
                ans = ans*x
            x, n = x*x, n//2
        return ans

    def __eq__(self, other):
        y = Q.of(other)
        return self.a == y.a and self.b == y.b

    def abs_upper(self):
        # |w|=1, so the triangle inequality gives this rational bound.
        return abs(self.a)+abs(self.b)

    def real(self):
        return self.a+self.b/2

    def data(self):
        return {"a": str(self.a), "b": str(self.b),
                "norm_squared": str(self.norm2()),
                "absolute_upper": str(self.abs_upper())}


def prod(xs):
    ans = Q(1)
    for x in xs:
        ans = ans*x
    return ans


def det(a):
    """Independent exact rational Gaussian elimination for small replay."""
    a = [[F(x) for x in row] for row in a]
    n, ans = len(a), F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            ans = -ans
        d = a[j][j]
        ans *= d
        for i in range(j+1, n):
            ratio = a[i][j]/d
            for k in range(j+1, n):
                a[i][k] -= ratio*a[j][k]
    return ans


x = [Q(4), Q(3), Q(2), Q(0, 1), Q(1, -1)]
labels = ["4", "3", "2", "w", "wbar"]
failures = []
coeff = [Q(1)]
for v in x:
    nxt = [Q(0) for _ in range(len(coeff)+1)]
    for j, c in enumerate(coeff):
        nxt[j] = nxt[j]+c
        nxt[j+1] = nxt[j+1]+c*v
    coeff = nxt
if not all(c.b == 0 and c.a > 0 for c in coeff):
    failures.append("not all six ordinary coefficients positive rational")
differences = [{"i": labels[i], "j": labels[j],
                "difference": (x[i]-x[j]).data()}
               for i in range(5) for j in range(i+1, 5)]
if not all(d["difference"]["norm_squared"] != "0" for d in differences):
    failures.append("roots not distinct")

terms = {}
for shift in (3, 4):
    ts = []
    for subset in combinations(range(5), shift):
        cross = prod(x[i]-x[j] for i in subset
                     for j in range(5) if j not in subset)
        base = prod(x[i] for i in subset)
        c = base**(5-shift)/cross
        ts.append((subset, base, c, cross))
    terms[shift] = ts

lead3 = next(c for s, b, c, d in terms[3] if s == (0, 1, 2))
rest3 = [(s, b, c, d) for s, b, c, d in terms[3] if s != (0, 1, 2)]
rest4 = [(s, b, c, d) for s, b, c, d in terms[4]
         if s not in ((0, 1, 2, 3), (0, 1, 2, 4))]
c4 = next(c for s, b, c, d in terms[4] if s == (0, 1, 2, 3))
c4bar = next(c for s, b, c, d in terms[4] if s == (0, 1, 2, 4))
if c4bar != c4.conj():
    failures.append("leading shift4 coefficients not conjugate")
if x[3]**6 != Q(1):
    failures.append("phase not period6")
for name, ts in (("3", rest3), ("4", rest4)):
    if not all(b.norm2() <= 12**2 for s, b, c, d in ts):
        failures.append("remainder base modulus exceeds12 at shift"+name)
bound3 = sum(c.abs_upper() for s, b, c, d in rest3)
bound4 = sum(c.abs_upper() for s, b, c, d in rest4)
phases = [2*(c4*x[3]**r).real() for r in range(6)]
residue = min(range(6), key=lambda j: phases[j])
onset = 16
error3, error4 = bound3/F(2**onset), bound4/F(2**onset)
margin3, margin4 = lead3.a-error3, -phases[residue]-error4
if not (lead3.b == 0 and margin3 > 0):
    failures.append("shift3 positive margin failed")
if not margin4 > 0:
    failures.append("shift4 negative margin failed")

replay = []
for shift in (3, 4):
    for rank in range(1, 7):
        formula = sum((c*b**rank for s, b, c, d in terms[shift]), Q(0))
        direct = det([[coeff[shift+j-i].a if 0 <= shift+j-i <= 5 else F(0)
                       for j in range(rank)] for i in range(rank)])
        ok = formula == Q(direct)
        replay.append({"shift": shift, "rank": rank,
                       "determinant": str(direct), "formula": formula.data(),
                       "equal": ok})
        if not ok:
            failures.append(f"formula orientation replay failed {shift}/{rank}")

certificate = {
    "arithmetic": "Q(w), w^2=w-1, w=(1+i sqrt(3))/2; all fractions exact",
    "polynomial": "(1+4z)(1+3z)(1+2z)(1+z+z^2)",
    "coefficients": [str(c.a) for c in coeff],
    "pf2": {"theorem": "Katkova math/0505174v1 Theorem B, printed p.5",
            "roots": ["-1/4", "-1/3", "-1/2", "exp(2pi i/3)", "exp(-2pi i/3)"],
            "required": "no zeros in open |arg(z)|<2pi/3; P(0)>0",
            "boundary_allowed": True},
    "variables": {label: v.data() for label, v in zip(labels, x)},
    "pairwise_differences": differences,
    "terms": {str(k): [{"subset": [labels[i] for i in s], "base": b.data(),
                         "coefficient": c.data(), "cross_denominator": d.data()}
                        for s, b, c, d in ts] for k, ts in terms.items()},
    "proof_bounds": {
        "onset": onset, "dominant_base_modulus": 24,
        "remainder_base_modulus_at_most": 12,
        "shift3_leading_coefficient": lead3.data(),
        "shift3_remainder_coefficient_sum_upper": str(bound3),
        "shift3_normalized_error_at_onset": str(error3),
        "shift3_required_margin": ">0", "shift3_actual_margin": str(margin3),
        "shift4_leading_coefficient_for_24w": c4.data(),
        "shift4_period6_normalized_leading": [str(t) for t in phases],
        "shift4_negative_residue": residue,
        "shift4_remainder_coefficient_sum_upper": str(bound4),
        "shift4_normalized_error_at_onset": str(error4),
        "shift4_required_negative_margin": ">0",
        "shift4_actual_negative_margin": str(margin4)},
    "finite_orientation_replays_not_infinite_sign_proofs": replay,
    "failures": failures, "passed": not failures}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2)+"\n")
print("coefficients:", certificate["coefficients"])
print("shift3: C0 =", lead3.a, "; remainder <=", bound3, "* 2^(-r)")
print("shift4: phases =", [str(t) for t in phases])
print("shift4: remainder <=", bound4, "* 2^(-r); negative residue", residue)
print("onset", onset, "; actual margins:", margin3, margin4, "; required: both >0")
print("failures:", failures, "; certificate:", output)
raise SystemExit(bool(failures))
