#!/usr/bin/env python3
"""Bounded Q3 certificate; Python standard library only. See L821 for proof."""
import json
import decimal
import sys
from decimal import Decimal, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction
from pathlib import Path

PREC = 90
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
NEAR = Context(prec=PREC, rounding=ROUND_HALF_EVEN)
N = 8
CAP = 2048
OUT = Path(__file__).with_name('confluent_compact_612.json')


class I:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)
        assert self.lo.is_finite() and self.hi.is_finite()
        assert self.lo <= self.hi

    @staticmethod
    def of(x):
        if isinstance(x, I):
            return x
        if isinstance(x, Fraction):
            return I(DOWN.divide(Decimal(x.numerator), Decimal(x.denominator)),
                     UP.divide(Decimal(x.numerator), Decimal(x.denominator)))
        return I(x)

    def __add__(self, other):
        b = I.of(other)
        return I(DOWN.add(self.lo, b.lo), UP.add(self.hi, b.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + (-I.of(other))

    def __rsub__(self, other):
        return I.of(other) + (-self)

    def __mul__(self, other):
        b = I.of(other)
        return I(min(DOWN.multiply(x, y) for x in (self.lo, self.hi)
                     for y in (b.lo, b.hi)),
                 max(UP.multiply(x, y) for x in (self.lo, self.hi)
                     for y in (b.lo, b.hi)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = I.of(other)
        assert not b.lo <= 0 <= b.hi, 'division interval includes zero'
        return self * I(DOWN.divide(Decimal(1), b.hi),
                        UP.divide(Decimal(1), b.lo))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        # Only directed basic operations, with no transcendental power.
        out, base = I(1), self
        while n:
            if n % 2:
                out = out * base
            n //= 2
            if n:
                base = base * base
        return out

    def exp(self):
        # Decimal.exp is correctly rounded to nearest/half-even. Widen by
        # one representable number on both sides in that SAME context.
        a, b = NEAR.exp(self.lo), NEAR.exp(self.hi)
        return I(NEAR.next_minus(a), NEAR.next_plus(b))

    def data(self):
        return [str(self.lo), str(self.hi)]


def atan_bounds(q, terms):
    s = sum((Fraction((-1)**k, (2*k+1)*q**(2*k+1))
             for k in range(terms)), Fraction(0))
    t = Fraction((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(s, s+t), max(s, s+t)


def pi_interval():
    a, b = atan_bounds(5, 120)
    c, d = atan_bounds(239, 40)
    lo, hi = 16*a-4*d, 16*b-4*c
    return I(I.of(lo).lo, I.of(hi).hi)


# Polynomials in (u,a,c), a=pi*n^2*exp(2u), c=pi*exp(2u).
def put(p, power, value):
    p[power] = p.get(power, 0) + value
    if not p[power]:
        del p[power]


def step(p):
    out = {}
    for (i, j, k), b in p.items():
        put(out, (i, j, k), i*b)
        put(out, (i+1, j, k), 2*(j+k)*b)
        put(out, (i+1, j+1, k), -2*b)
        put(out, (i+1, j, k+1), 2*b)
    return out


POLYS = [{(0, 2, 0): 8, (0, 1, 0): -12}]
for _ in range(4):
    POLYS.append(step(POLYS[-1]))


def specialized(p, n):
    out = {}
    for (i, j, k), b in p.items():
        put(out, (i, j+k), b*n**(2*j))
    return out


SPECIAL = [[specialized(p, n) for p in POLYS] for n in range(1, N+1)]
COEFF_BOUNDS = [sum(abs(b)*2**i for (i,j,k), b in p.items()) for p in POLYS]
COEFF_MAJORANTS = [20]
for j in range(4):
    COEFF_MAJORANTS.append((5*j+16)*COEFF_MAJORANTS[-1])
assert all(a <= b for a,b in zip(COEFF_BOUNDS, COEFF_MAJORANTS))
PI = pi_interval()
GLOBAL_C = PI * I('0.5', 4).exp()
assert GLOBAL_C.lo > 5 and GLOBAL_C.hi < 200
RATIO_BOUND = I(2**12) * I(-95).exp()
assert RATIO_BOUND.hi < Decimal('0.5')
TAILS = [I(2*b*200**6*9**12)*I(-400).exp() for b in COEFF_MAJORANTS]


def eval_poly(p, u, c):
    return sum((I(b) * u**i * c**j for (i,j), b in p.items()), I(0))


def evaluate(left, right):
    u = I(I.of(left).lo, I.of(right).hi)
    c = PI * (2*u).exp()
    jets = [I(0) for _ in range(5)]
    for n, polynomials in enumerate(SPECIAL, 1):
        w = (-(n*n-1)*c).exp() if n > 1 else I(1)
        for j, p in enumerate(polynomials):
            # Positive factorization avoids a spurious zero denominator
            # on the initial wide box. It is exactly 8a^2-12a.
            value = 4*n*n*c*(2*n*n*c-3) if j == 0 else eval_poly(p, u, c)
            jets[j] += w * value
    finite = [x.data() for x in jets]
    jets = [x + I(t.hi.copy_negate(), t.hi) for x,t in zip(jets, TAILS)]
    assert jets[0].lo > 0
    r = [x/jets[0] for x in jets]
    b2 = r[2]-r[1]**2
    b3 = r[3]-3*r[1]*r[2]+2*r[1]**3
    b4 = r[4]-4*r[1]*r[3]-3*r[2]**2+12*r[1]**2*r[2]-6*r[1]**4
    a2 = c*(2*u+4*u**2)
    a3 = c*(2*u+12*u**2+8*u**3)
    a4 = c*(2*u+28*u**2+48*u**3+16*u**4)
    ell = [u/2-a2+b2, u/2-a3+b3, u/2-a4+b4]
    q = ell[1]**2-ell[0]*ell[2]-2*ell[0]**3
    return {'u': [str(left), str(right)], 'c': c.data(),
            'B_finite_jets': finite, 'B_full_jets': [x.data() for x in jets],
            'logH_derivatives_2_3_4': [x.data() for x in ell], 'Q3': q.data()}


def polynomial_data(p):
    return [{'powers': list(k), 'coefficient': str(v)} for k,v in sorted(p.items())]


def main():
    cert = {'target': 'Q3 for u=exp(v) in [1/4,2]', 'precision': PREC,
            'runtime': {'python': sys.version,
                        'libmpdec': decimal.__libmpdec_version__,
                        'Emin': DOWN.Emin, 'Emax': DOWN.Emax},
            'arithmetic': 'directed Decimal basic arithmetic; nearest exp widened by one ulp',
            'pi': PI.data(), 'pi_recipe': '16 atan(1/5)-4 atan(1/239), alternating 120/40 terms',
            'N': N, 'cap': CAP, 'global_c': GLOBAL_C.data(),
            'tail_ratio_bound': RATIO_BOUND.data(), 'tail_bounds': [x.data() for x in TAILS],
            'tail_coefficient_bounds': COEFF_BOUNDS,
            'tail_analytic_coefficient_majorants': COEFF_MAJORANTS,
            'derivative_polynomials': [polynomial_data(p) for p in POLYS],
            'failures': [{'phase': 'first implementation run',
                          'reason': 'Expanded B0 enclosure on initial wide box crossed zero; no sign conclusion produced.',
                          'repair': 'Use identical positive factorization 4a(2a-3) for B0.'}],
            'negative_point': None, 'terminal_cells': [], 'unresolved': []}
    # Rigorous rational points only; early rejection needs no interval cover.
    cert['point_tests'] = []
    for u in [Fraction(1,4), Fraction(1,2), Fraction(1), Fraction(3,2), Fraction(2)]:
        row = evaluate(u,u)
        cert['point_tests'].append(row)
        if Decimal(row['Q3'][1]) < 0:
            cert['negative_point'] = row
            break
    if cert['negative_point']:
        cert['conclusion'] = 'RIGOROUS_NEGATIVE_POINT'
    else:
        stack = [(Fraction(1,4), Fraction(2))]
        while stack:
            left, right = stack.pop()
            row = evaluate(left, right)
            if Decimal(row['Q3'][0]) >= 0:
                cert['terminal_cells'].append(row)
            elif len(cert['terminal_cells']) + len(stack) + 2 <= CAP:
                mid = (left+right)/2
                stack.extend([(mid,right),(left,mid)])
            else:
                cert['unresolved'].append(row)
                cert['unresolved'].extend(evaluate(a,b) for a,b in stack)
                stack = []
        cells = cert['terminal_cells'] + cert['unresolved']
        cells.sort(key=lambda x: Fraction(x['u'][0]))
        assert Fraction(cells[0]['u'][0]) == Fraction(1,4)
        assert Fraction(cells[-1]['u'][1]) == 2
        assert all(a['u'][1] == b['u'][0] for a,b in zip(cells,cells[1:]))
        assert len(cells) <= CAP
        cert['cover_exactly_verified'] = True
        cert['conclusion'] = 'COMPACT_NONNEGATIVE_COVER' if not cert['unresolved'] else 'INCONCLUSIVE_AT_CAP'
        if not cert['unresolved']:
            cert['uniform_Q3_lower'] = str(min(Decimal(r['Q3'][0]) for r in cells))
            weakest = min(cells, key=lambda r: Decimal(r['Q3'][0]))
            cert['weakest_cell'] = weakest
            assert Decimal(cert['uniform_Q3_lower']) > Decimal('0.2')
    # Inspect the complete certificate values, not a sampled preview.
    rows = cert['point_tests'] + cert['terminal_cells'] + cert['unresolved']
    for row in rows:
        for field in ['c', 'Q3']:
            assert Decimal(row[field][0]) <= Decimal(row[field][1])
        for field in ['B_finite_jets', 'B_full_jets', 'logH_derivatives_2_3_4']:
            assert all(Decimal(lo) <= Decimal(hi) for lo,hi in row[field])
        ell = [I(*pair) for pair in row['logH_derivatives_2_3_4']]
        assert (ell[1]**2-ell[0]*ell[2]-2*ell[0]**3).data() == row['Q3']
    cert['verification'] = {'all_rows_inspected': len(rows),
                            'all_terminal_Q3_bounds_nonnegative': all(Decimal(r['Q3'][0]) >= 0 for r in cert['terminal_cells']),
                            'all_stored_Q3_formulas_recomputed': True,
                            'exact_rational_cover_checked': cert.get('cover_exactly_verified', False),
                            'terminal_count': len(cert['terminal_cells']) + len(cert['unresolved']),
                            'unresolved_count': len(cert['unresolved']),
                            'unresolved_arithmetic_failures': 0}
    bad_signals = [decimal.InvalidOperation, decimal.DivisionByZero,
                   decimal.Overflow, decimal.Underflow, decimal.Subnormal,
                   decimal.Clamped]
    assert all(not ctx.flags[s] for ctx in (DOWN, UP, NEAR) for s in bad_signals)
    cert['verification']['no_exceptional_decimal_flags'] = True
    OUT.write_text(json.dumps(cert, indent=2)+'\n')
    print('Conclusion:', cert['conclusion'])
    print('Terminal intervals:', len(cert['terminal_cells'])+len(cert['unresolved']), '/', CAP)
    print('Unresolved:', len(cert['unresolved']), '; resolved implementation failures:', len(cert['failures']))
    print('Q3 lower bound:', cert.get('uniform_Q3_lower', 'not certified'), '; required: >=0')
    if cert['negative_point']:
        print('Negative point:', cert['negative_point']['u'], 'Q3:', cert['negative_point']['Q3'])
    print('Certificate:', OUT)


if __name__ == '__main__':
    main()
