#!/usr/bin/env python3
"""Exact scalar comparison for C020a; no sampled zeta or witness values."""
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
        products = [a*b for a in (self.lo, self.hi)
                    for b in (other.lo, other.hi)]
        return I(min(products), max(products))

    __rmul__ = __mul__


def outward(v):
    scale = 10**12
    lo = v.lo.numerator*scale // v.lo.denominator
    hi = -((-v.hi.numerator*scale) // v.hi.denominator)
    return I(F(lo, scale), F(hi, scale))


def atan_interval(z, terms=20):
    assert 0 < z < 1
    s = sum(((-1)**k*z**(2*k+1)/(2*k+1)
             for k in range(terms)), F(0))
    nxt = (-1)**terms*z**(2*terms+1)/(2*terms+1)
    return I(min(s, s+nxt), max(s, s+nxt))


def log_point(x, terms=32):
    assert x >= 1
    z = (x-1)/(x+1)
    s = 2*sum((z**(2*k+1)/(2*k+1) for k in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return I(s, s+tail)


def log_interval(x):
    return outward(I(log_point(x.lo).lo, log_point(x.hi).hi))


sqrt2 = I(F(1414213562373, 10**12), F(1414213562374, 10**12))
assert sqrt2.lo**2 < 2 < sqrt2.hi**2
pi = outward(16*atan_interval(F(1, 5))-4*atan_interval(F(1, 239)))
A = outward(log_point(F(2)))
delta = outward(log_point(F(4, 3)))
ratio = I(25*sqrt2.lo/(8*pi.hi), 25*sqrt2.hi/(8*pi.lo))
log_ratio = log_interval(ratio)
end_b = delta + F(1, 2)*log_ratio
f0 = F(2, 13)*A*A-F(56, 143)*A*delta+F(1, 22)*delta*delta
early_derivative = -F(166, 143)*A+F(61, 143)*delta
late_derivative = -68*A+16*delta
end_f = (F(2, 13)*A*(A-delta)
         +F(1, 286)*late_derivative*end_b-F(3, 286)*end_b*end_b)
C4 = F(1, 13)*A*(F(1, 2)*sqrt2-F(4, 25)*pi
                  +(sqrt2-1)*A-F(1, 2)*sqrt2*log_ratio)
integral_lower = -F(7, 250)*(sqrt2-1)
margin = C4 + integral_lower
checks = {
    'sqrt2_enclosed_by_squares': sqrt2.lo**2 < 2 < sqrt2.hi**2,
    'entry_inside_band': 1 < F(8, 25)*pi.lo < F(8, 25)*pi.hi < sqrt2.lo,
    'switch_above_one_tenth': sqrt2.lo > F(8, 25)*pi.hi,
    'switch_below_one_fifth': sqrt2.hi < F(32, 25)*pi.lo,
    'lower_count_positive_at_one_tenth': pi.lo > F(25, 8),
    'early_derivative_negative': early_derivative.hi < 0,
    'late_derivative_negative': late_derivative.hi < 0,
    'early_f_above_minus_7_over_250': f0.lo > -F(7, 250),
    'late_f_above_minus_7_over_250': end_f.lo > -F(7, 250),
    'C4_above_13_over_1000': C4.lo > F(13, 1000),
    'combined_margin_above_1_over_1000': margin.lo > F(1, 1000),
}
values = dict(sqrt2=sqrt2, pi=pi, log2=A, log4over3=delta,
              log_ratio=log_ratio, f_at_x0=f0,
              early_derivative=early_derivative,
              late_derivative=late_derivative, b_at_sqrt2=end_b,
              f_at_sqrt2=end_f, C4=C4,
              integral_lower=integral_lower, combined_margin=margin)
out = Path(__file__).with_name('coherent-saddle-sign-certificate-1415.json')
payload = {
    'purpose': 'C020a selected CA saddle plus C019z resonance only; full quotient unpaid',
    'method': 'Exact rational intervals; Machin arctangent and atanh log series; rational square-root bracket',
    'atan_terms': 20, 'log_terms': 32, 'outward_grid': '1/1000000000000',
    'values': {k: {'lo': str(outward(v).lo), 'hi': str(outward(v).hi)}
               for k, v in values.items()},
    'checks': checks,
    'required': {'C4_strict_lower': '13/1000',
                 'f_strict_lower': '-7/250',
                 'combined_margin_strict_lower': '1/1000'},
    'failures': [k for k, ok in checks.items() if not ok],
}
out.write_text(json.dumps(payload, indent=2)+'\n')
for name in ('f_at_sqrt2', 'C4', 'combined_margin'):
    value = outward(values[name])
    print(f'{name}: [{value.lo}, {value.hi}]')
print('Required: f > -7/250; C4 > 13/1000; combined margin > 1/1000')
print(f'checks={sum(checks.values())}/{len(checks)} failures={payload["failures"]}')
print(f'certificate={out}')
assert not payload['failures']
