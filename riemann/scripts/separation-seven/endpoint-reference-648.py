#!/usr/bin/env python3
"""Exact rational certificate for the fixed C999z tolerance rule, step648.

Only the new scalar specialization is checked. The .239999 reference
floor is an inherited, qualified C999k input, not replayed here.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
import json


class I:
    def __init__(self, lo, hi=None):
        self.lo = F(lo)
        self.hi = self.lo if hi is None else F(hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    def __sub__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.lo - other.hi, self.hi - other.lo)

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        products = [x*y for x in (self.lo, self.hi)
                    for y in (other.lo, other.hi)]
        return I(min(products), max(products))

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert other.lo > 0
        return self * I(1/other.hi, 1/other.lo)

    def __pow__(self, n):
        assert n >= 0 and self.lo >= 0
        return I(self.lo**n, self.hi**n)


def decimal_bound(x, rounding):
    with localcontext() as c:
        c.prec = 18
        c.rounding = rounding
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def encode(interval):
    return {'lo': str(interval.lo), 'hi': str(interval.hi),
            'display_lo': decimal_bound(interval.lo, ROUND_FLOOR),
            'display_hi': decimal_bound(interval.hi, ROUND_CEILING)}


def main():
    checks = []

    def check(condition, name):
        checks.append({'name': name, 'pass': bool(condition)})

    # ln(3)=2 atanh(1/2), with the entire positive-series tail.
    count = 100
    x = F(1, 2)
    log_lower = 2*sum((x**(2*k+1)/F(2*k+1)
                       for k in range(count)), F(0))
    log_tail = 2*x**(2*count+1)/(F(2*count+1)*(1-x*x))
    a = I(log_lower, log_lower+log_tail)/4

    # Rational outward enclosure of 3^(1/8), certified by integer powers.
    denominator = 2**128
    lower, upper = denominator, 2*denominator
    while upper-lower > 1:
        middle = (lower+upper)//2
        if middle**8 <= 3*denominator**8:
            lower = middle
        else:
            upper = middle
    check(lower**8 < 3*denominator**8 < upper**8,
          'complete eighth-root enclosure')
    root = I(F(lower, denominator), F(upper, denominator))
    delta = I(F(1, 100))
    H = I(F(303, 16))
    Ca = I(4)*a/root/((I(1)-I(1)/root**2)*(I(1)-I(1)/root**4))
    m_rule = I(2)*H*a**2/delta
    m, J = 286, 14
    tail_previous = Ca/root**(4*(J-1))
    tail_selected = Ca/root**(4*J)
    eta = H*a**2/m + tail_selected
    beta = I(F(239999, 10**6))-delta-eta
    beta_coarse = F(219999, 10**6)
    check(285 < m_rule.lo and m_rule.hi < 286,
          'smallest integer m in fixed rule is 286')
    check(tail_previous.lo > F(1, 200),
          'J=13 fails the prescribed half-tolerance tail rule')
    check(tail_selected.hi < F(1, 200),
          'smallest integer J in fixed rule is 14')
    check(eta.hi < F(1, 100), 'complete response error below 1/100')
    check(beta.lo > beta_coarse > 0, 'coarse floor .219999 is paid')
    failures = [c['name'] for c in checks if not c['pass']]
    certificate = {
        'step': '2026-11-12-endpoint-reference-construction-648',
        'method': 'Fraction arithmetic, complete atanh tail and integer root powers',
        'qualified_input': 'C999k Section2/audit6: R>=.239999 I; no replay here',
        'parameters': {'m': m, 'J': J, 'delta': '1/100'},
        'intervals': {name: encode(value) for name, value in
                      [('a', a), ('root_3_1_8', root), ('Ca', Ca),
                       ('m_rule', m_rule), ('tail_J13', tail_previous),
                       ('tail_J14', tail_selected), ('eta', eta),
                       ('inherited_floor_minus_delta_minus_eta', beta)]},
        'required': {'m_rule': '(285,286)', 'tail_J13': '>1/200',
                     'tail_J14': '<=1/200', 'eta': '<=1/100',
                     'beta_coarse': '.219999>0'},
        'checks': checks, 'failures': failures,
        'summary': {'m': m, 'J': J, 'eta_upper': encode(eta)['display_hi'],
                    'eta_required_upper': '.01',
                    'm_rule_interval': [encode(m_rule)['display_lo'],
                                        encode(m_rule)['display_hi']],
                    'm_rule_required': '(285,286)',
                    'tail_J13_lower': encode(tail_previous)['display_lo'],
                    'tail_J14_upper': encode(tail_selected)['display_hi'],
                    'tail_required_upper': '.005',
                    'floor_lower': encode(beta)['display_lo'],
                    'coarse_required_floor': '.219999',
                    'checks_passed': len(checks)-len(failures),
                    'failures': failures},
    }
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(certificate['summary'], sort_keys=True))
    print('certificate:', path.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
