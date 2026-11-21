#!/usr/bin/env python3
"""Exact rational certificate for C019z's scalar sign, no zeta numerics."""
from fractions import Fraction as F
import json
from pathlib import Path


class I:
    def __init__(self, lo, hi=None):
        self.lo, self.hi = F(lo), F(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-other if isinstance(other, I) else -F(other))

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        products = [a * b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I(min(products), max(products))

    __rmul__ = __mul__


def atan_interval(z, terms=20):
    assert 0 < z < 1
    s = sum(((-1) ** k * z ** (2*k+1) / (2*k+1)
             for k in range(terms)), F(0))
    nxt = (-1) ** terms * z ** (2*terms+1) / (2*terms+1)
    return I(min(s, s+nxt), max(s, s+nxt))


def log_interval(x, terms=32):
    assert x >= 1
    z = (x-1)/(x+1)
    s = 2 * sum((z ** (2*k+1)/(2*k+1) for k in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return I(s, s+tail)


def outward(v):
    scale = 10**12
    lo = (v.lo.numerator*scale)//v.lo.denominator
    hi = -((-v.hi.numerator*scale)//v.hi.denominator)
    return I(F(lo, scale), F(hi, scale))


pi = outward(16*atan_interval(F(1, 5)) - 4*atan_interval(F(1, 239)))
A = outward(log_interval(F(2)))
delta = outward(log_interval(F(4, 3)))
x0 = F(8, 25)*pi
b1 = delta + F(1, 2)*outward(I(log_interval(F(15, 4)/pi.hi).lo,
                               log_interval(F(15, 4)/pi.lo).hi))
f0 = F(2, 13)*A*A - F(56, 143)*A*delta + F(1, 22)*delta*delta
early_derivative = -F(166, 143)*A + F(61, 143)*delta
early = f0 + I(-F(1, 200), 0)*early_derivative + I(0, F(1, 40000))*F(131, 286)


def late(b):
    return (F(2, 13)*A*(A-delta)
            + F(1, 286)*(-68*A+16*delta)*b - F(3, 286)*b*b)


f1 = late(b1)
derivative_numerator = -68*A+16*delta
checks = {
    'entry_above_1': x0.lo > 1,
    'entry_below_101_over_100': x0.hi < F(101, 100),
    'late_start_negative': f0.hi < 0,
    'late_decreasing': derivative_numerator.hi < 0,
    'early_upper_below_1_over_100': early.hi < F(1, 100),
    'late_at_6_over_5_below_minus_1_over_100': f1.hi < -F(1, 100),
    'sqrt2_above_7_over_5': F(7, 5)**2 < 2,
    'integral_upper_below_minus_1_over_1000': -F(19, 10000) < -F(1, 1000),
}
values = dict(pi=pi, log2=A, log4over3=delta, x0=x0, b_at_6over5=b1,
              f_at_x0=f0, early_derivative=early_derivative,
              early_upper_enclosure=early, f_at_6over5=f1,
              late_derivative_numerator=derivative_numerator)
out = Path(__file__).with_name('resonant-scalar-sign-certificate-1413.json')
payload = {
    'purpose': 'C019z scalar integral sign only; not the full witness quotient',
    'method': 'Exact Fraction arithmetic; alternating arctangent and positive atanh log series',
    'atan_terms': 20, 'log_terms': 32, 'outward_base_grid': '1/1000000000000',
    'values': {k: {'lo': str(v.lo), 'hi': str(v.hi)} for k, v in values.items()},
    'checks': checks,
    'integral': {'strict_upper': '-19/10000', 'required_strict_upper': '-1/1000'},
    'failures': [k for k, ok in checks.items() if not ok],
}
out.write_text(json.dumps(payload, indent=2)+'\n')
for name in ('f_at_x0', 'early_upper_enclosure', 'f_at_6over5'):
    v = values[name]
    print(f'{name}: [{float(v.lo):.10g}, {float(v.hi):.10g}] (display only; certificate is rational)')
print(f'checks={sum(checks.values())}/{len(checks)} failures={payload["failures"]}')
print('integral strict upper=-19/10000; required strict upper=-1/1000')
print(f'certificate={out}')
assert not payload['failures']
