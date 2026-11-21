#!/usr/bin/env python3
"""Exact scalar certificate for C020b; no witness or zeta sampling."""
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

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert 0 < other.lo
        return self * I(1/other.hi, 1/other.lo)


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
pi = outward(16*atan_interval(F(1, 5))-4*atan_interval(F(1, 239)))
A = outward(log_point(F(2)))
z = F(8, 25)*pi
r3 = 18*pi/(25*sqrt2)
r4 = 25*sqrt2/(8*pi)
log_z, log_r3, log_r4 = map(log_interval, (z, r3, r4))
C2 = -F(3, 13)*A*(z-1-log_z)
C3 = -F(2, 11)*A*(sqrt2-1-F(1, 2)*A+(sqrt2-1)*log_r3)
C4 = F(1, 13)*A*(F(1, 2)*sqrt2-F(4, 25)*pi
                  +(sqrt2-1)*A-F(1, 2)*sqrt2*log_r4)
Csum = C2+C3+C4
# C019z (3) is a mathematical input, not proved by this scalar script.
partial_upper = 2*Csum-F(19, 10000)
checks = {
    'sqrt2_bracket_by_squares': sqrt2.lo**2 < 2 < sqrt2.hi**2,
    'a1_no_positive_count': 2*pi.hi/25 < 1,
    'a2_entry_inside_source_interval': 2*pi.hi*4/100 < 1 < z.lo,
    'a2_switch_above_source_interval': z.hi < sqrt2.lo,
    'a3_entry_inside_source_interval': 2*pi.hi*9/100 < 1 < 2*pi.lo*9/25,
    'a3_switch_inside_source_interval': 2*pi.hi*9/100 < sqrt2.lo < sqrt2.hi < 2*pi.lo*9/25,
    'a4_entry_below_source_interval': 2*pi.lo*16/100 > 1,
    'a4_switch_inside_source_interval': 2*pi.hi*16/100 < sqrt2.lo < sqrt2.hi < 2*pi.lo*16/25,
    'C2_negative': C2.hi < 0,
    'C3_negative': C3.hi < 0,
    'C4_above_13_over_1000': C4.lo > F(13, 1000),
    'Csum_below_minus_19_over_1000': Csum.hi < -F(19, 1000),
    'partial_upper_below_minus_39_over_1000': partial_upper.hi < -F(39, 1000),
}
values = dict(sqrt2=sqrt2, pi=pi, log2=A, z=z, ratio3=r3,
              ratio4=r4, log_z=log_z, log_ratio3=log_r3,
              log_ratio4=log_r4, C2=C2, C3=C3, C4=C4,
              Csum=Csum, partial_upper=partial_upper)
out = Path(__file__).with_name('matched-saddle-sign-certificate-1416.json')
payload = {
    'purpose': 'C020b fixed a=1,2,3,4 matched saddle families only; full quotient unpaid',
    'method': 'Exact Fraction intervals; Machin arctangent and atanh log series; square-root bracket',
    'atan_terms': 20, 'log_terms': 32, 'outward_grid': '1/1000000000000',
    'input_qualification': 'C019z I < -19/10000 used only in partial_upper; not verified by this script',
    'values': {k: {'lo': str(outward(v).lo), 'hi': str(outward(v).hi)}
               for k, v in values.items()},
    'required': {'Csum_strict_upper': '-19/1000',
                 'partial_strict_upper': '-39/1000'},
    'checks': checks,
    'failures': [k for k, ok in checks.items() if not ok],
}
out.write_text(json.dumps(payload, indent=2)+'\n')
for name in ('C2', 'C3', 'C4', 'Csum', 'partial_upper'):
    v = outward(values[name])
    print(f'{name}: [{v.lo}, {v.hi}]')
print('Required: Csum < -19/1000; I + 2*Csum < -39/1000 using C019z')
print(f'checks={sum(checks.values())}/{len(checks)} failures={payload["failures"]}')
print(f'certificate={out}')
assert not payload['failures']
