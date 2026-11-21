#!/usr/bin/env python3
"""Independent exact replay from Q_j; no analytic or curvature certification."""
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def plus(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def times(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def derivative(p):
    return trim([i*p[i] for i in range(1, len(p))] or [0])


class Rat:
    def __init__(self, num, den=(1,)):
        self.num = trim((num,) if isinstance(num, int) else num)
        self.den = trim(den)
        assert self.den != (0,)

    def __add__(self, other):
        other = rat(other)
        return Rat(plus(times(self.num, other.den),
                        times(other.num, self.den)), times(self.den, other.den))

    __radd__ = __add__

    def __neg__(self):
        return Rat(tuple(-a for a in self.num), self.den)

    def __sub__(self, other):
        return self + (-rat(other))

    def __rsub__(self, other):
        return rat(other) + (-self)

    def __mul__(self, other):
        other = rat(other)
        return Rat(times(self.num, other.num), times(self.den, other.den))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = rat(other)
        return Rat(times(self.num, other.den), times(self.den, other.num))

    def __rtruediv__(self, other):
        return rat(other)/self

    def __pow__(self, n):
        out = Rat(1)
        for _ in range(n):
            out = out*self
        return out

    def diff(self):
        return Rat(plus(times(derivative(self.num), self.den),
                        tuple(-a for a in times(self.num, derivative(self.den)))),
                   times(self.den, self.den))

    def at(self, value):
        def ev(p):
            out = 0
            for a in reversed(p):
                out = out*value+a
            return out
        return Fraction(ev(self.num), ev(self.den))


def rat(x):
    return x if isinstance(x, Rat) else Rat(x)


def shift(p):
    return [sum(p[i]*comb(i, j) for i in range(j, len(p)))
            for j in range(len(p))]


t = Rat((0, 1))
q = {j: 4*j*(3*t+j)/(t*(t+j)**2) for j in (1, 2)}
# d^2/dx^2 q(x^2) = 2 q'(t) + 4t q''(t).
qxx = {j: 2*q[j].diff()+4*t*q[j].diff().diff() for j in (1, 2)}
identities = {}


def check_identity(name, left, right):
    identities[name] = list((left-right).num)


for j in (1, 2):
    check_identity(f"Q{j}_partial_fractions", q[j],
                   Rat(4)/t-4/(t+j)+8*j/(t+j)**2)
    check_identity(f"Q{j}_second_derivative", qxx[j],
                   24*j*(10*t**3+5*j*t**2+4*j*j*t+j**3)/(t**2*(t+j)**4))

H = (t+1)*(t+2)
check_identity("D_primitive_derivative", q[2]-q[1],
               -4*(Rat(1)/H-2*t*H.diff()/H**2))
check_identity("D_regular_formula", q[2]-q[1],
               4*(3*t**2+3*t-2)/H**2)
r = q[2]/q[1]
ell = qxx[1]/q[1]
s = qxx[2]/qxx[1]
N = 10*t**3+5*t**2+4*t+1
F = t*(t+1)**2*(3*t+1)
check_identity("r_formula", r, 2*(3*t+2)*(t+1)**2/((3*t+1)*(t+2)**2))
check_identity("ell_formula", ell, 6*N/F)
check_identity("s_formula", s,
               2*(10*t**3+10*t**2+16*t+8)*(t+1)**4/(N*(t+2)**4))
r_sign = (-2, 9, 15)
ell_sign = (-1, -10, -36, -48, -21, -30, -30)
P5 = (0, 4, 12, -43, -114, -55)
check_identity("log_r_derivative", r.diff()/r,
               Rat(r_sign)/((t+1)*(t+2)*(3*t+1)*(3*t+2)))
check_identity("ell_derivative", ell.diff(), 6*Rat(ell_sign)/F**2)
check_identity("s_minus_r", s-r, 2*(t+1)**2*Rat(P5)/(N*(t+2)**4*(3*t+1)))
corner = q[1].at(1)*qxx[2].at(1)-q[2].at(1)*qxx[1].at(1)
checks = {name: value == [0] for name, value in identities.items()}
checks.update({
    "ell_derivative_all_coefficients_negative": all(a < 0 for a in ell_sign),
    "r_derivative_shift_all_coefficients_positive": all(a > 0 for a in shift(r_sign)),
    "s_minus_r_shift_all_coefficients_negative": all(a < 0 for a in shift(P5)),
    "kernel_corner": corner == Fraction(-784, 27),
})
certificate = {
    "scope": "Exact univariate rational identities from Q_j and sign polynomials; analytic claims audited in C034d.",
    "method": "Integer polynomial cross multiplication; t=x^2; spatial second derivative is 2*d_t+4*t*d_t^2.",
    "implementation_repair": "First execution stopped before any check or certificate with TypeError on int/Rat; added reflected division. No mathematical failure was inferred.",
    "identity_difference_numerators": identities,
    "sign_coefficients_ascending": {
        "ell_derivative_without_6": list(ell_sign),
        "r_derivative_shifted": shift(r_sign),
        "s_minus_r_inner": list(P5),
        "s_minus_r_inner_shifted": shift(P5),
    },
    "corner": {"Q1": str(q[1].at(1)), "Q2": str(q[2].at(1)),
               "Q1_second": str(qxx[1].at(1)), "Q2_second": str(qxx[2].at(1)),
               "K": str(corner)},
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
    "actual_bound": "K(x,y)<0 on [1,infinity)^2; C<=R+2 integral integral p_+(x)p_-(y)(-K(x,y)).",
    "required_bound": "R+2 integral integral p_+(x)p_-(y)(-K(x,y))<=S4^3/5 for all sigma in [1,2].",
    "threshold_certified": False,
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Exact audit: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print("Actual: negative rational kernel and retained signed remainder; no numerical curvature upper bound.")
print("Required: full signed right side <=S4^3/5 uniformly on [1,2]; NOT certified.")
print(f"Certificate: {out.relative_to(Path.cwd())}")
if certificate["failures"]:
    raise SystemExit(1)
