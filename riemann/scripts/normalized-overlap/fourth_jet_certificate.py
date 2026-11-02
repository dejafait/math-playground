#!/usr/bin/env python3
"""Directed-decimal certificate; run from riemann. No optional packages.

Full justification of the integration and tail bounds is in L602.
Decimal exp is correctly rounded (ROUND_HALF_EVEN); one adjacent decimal
on either side encloses its exact value. All other arithmetic is directed.
"""
import argparse
import json
import math
from decimal import Context, Decimal, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from pathlib import Path

PRECISION = 45
DOWN = Context(prec=PRECISION, rounding=ROUND_FLOOR)
UP = Context(prec=PRECISION, rounding=ROUND_CEILING)


class I:
    def __init__(self, lo, hi=None):
        self.lo = Decimal(lo)
        self.hi = self.lo if hi is None else Decimal(hi)
        assert self.lo <= self.hi

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        b = I.cast(other)
        return I(DOWN.add(self.lo, b.lo), UP.add(self.hi, b.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, other):
        return self + -I.cast(other)

    def __rsub__(self, other):
        return I.cast(other) + -self

    def __mul__(self, other):
        b = I.cast(other)
        pairs = [(a, c) for a in (self.lo, self.hi) for c in (b.lo, b.hi)]
        return I(min(DOWN.multiply(a, c) for a, c in pairs),
                 max(UP.multiply(a, c) for a, c in pairs))

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = I.cast(other)
        assert not b.lo <= 0 <= b.hi, 'division by an interval containing zero'
        return self * I(DOWN.divide(Decimal(1), b.hi),
                        UP.divide(Decimal(1), b.lo))

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        out = I(1)
        for _ in range(n):
            out = out * self
        return out

    def exp(self):
        return I(DOWN.next_minus(DOWN.exp(self.lo)),
                 UP.next_plus(UP.exp(self.hi)))

    def record(self):
        return {'lo': str(self.lo), 'hi': str(self.hi)}


def frac(q):
    return I(q.numerator) / q.denominator


def atan_reciprocal(n, terms=40):
    total = I(0)
    for j in range(terms):
        total += I((-1)**j) / ((2*j+1)*n**(2*j+1))
    # Alternating series remainder lies between zero and the next term.
    nxt = I((-1)**terms) / ((2*terms+1)*n**(2*terms+1))
    return total + I(min(Decimal(0), nxt.lo), max(Decimal(0), nxt.hi))


def polynomials():
    p = [Fraction(0), Fraction(-12), Fraction(8)]
    out = []
    for j in range(7):
        out.append(p)
        p = [(p[i]*(Fraction(1, 2)+2*i) if i < len(p) else 0)
             - (2*p[i-1] if i else 0) for i in range(len(p)+1)]
    return out


def product_coefficients(j, r):
    out = {}
    for l in range(j+1):
        for h in range(r+1):
            pair = tuple(sorted((j-l+h, l+r-h)))
            out[pair] = out.get(pair, 0) + (-1)**l*math.comb(j, l)*math.comb(r, h)
    return {pair: c for pair, c in out.items() if c}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cells', type=int, default=1024)
    parser.add_argument('--output', default='scripts/normalized-overlap/fourth-jet-certificate.json')
    args = parser.parse_args()
    assert args.cells > 0 and args.cells & (args.cells-1) == 0
    pi = 16*atan_reciprocal(5)-4*atan_reciprocal(239)
    assert pi.lo > 3 and pi.hi < 4
    assert I(1).exp().hi < 3 and I(4).exp().lo > 54
    assert I(-243).exp().hi < Decimal('0.5')
    ps = polynomials()
    ms = [sum(abs(c) for c in p) for p in ps]
    ips = [[frac(c) for c in p] for p in ps]
    ratios = [(I(6)/5)**(2*(j+2))*I(-33).exp() for j in range(7)]
    assert all(r.hi < Decimal('0.5') for r in ratios)
    theta_tails = [6*frac(ms[j])*75**(j+2)*I(-75).exp() for j in range(7)]
    co = {(j, r): product_coefficients(j, r) for j in (0, 2, 4) for r in range(3)}

    def kernels(u, order):
        z = (2*u).exp()
        front = (u/2).exp()
        result = [I(0) for _ in range(order+1)]
        for n in range(1, 5):
            v = pi*(n*n)*z
            ev = (-v).exp()
            for j in range(order+1):
                val = I(0)
                for c in reversed(ips[j]):
                    val = val*v+c
                result[j] += front*val*ev
        return [v+I(theta_tails[j].hi.copy_negate(), theta_tails[j].hi)
                for j, v in enumerate(result)]

    def q(k, j, r):
        return sum((c*k[a]*k[b] for (a, b), c in co[j, r].items()), I(0))

    integrals = {(j, m): I(0) for j in (0, 2, 4) for m in (0, 2)}
    h = I(2)/args.cells
    error_scale = h**3/24
    error_sums = {key: I(0) for key in integrals}
    for cell in range(args.cells):
        lo = h*cell
        hi = h*(cell+1)
        box = I(lo.lo, hi.hi)
        mid = h*(I(cell)+I(1)/2)
        km = kernels(mid, 4)
        kb = kernels(box, 6)
        for j in (0, 2, 4):
            qm = q(km, j, 0)
            qb, qp, qpp = (q(kb, j, r) for r in range(3))
            for m in (0, 2):
                fmid = qm if m == 0 else mid**2*qm
                fpp = qpp if m == 0 else 2*qb+4*box*qp+box**2*qpp
                error = error_scale*fpp
                integrals[j, m] += 2*(h*fmid+error)
                error_sums[j, m] += 2*error

    real_tails = {}
    for j in (0, 2, 4):
        coefficient = sum(abs(c)*4*ms[a]*ms[b]*(2*(a+2))**(a+2)*(2*(b+2))**(b+2)
                          for (a, b), c in co[j, 0].items())
        bound = 2*frac(coefficient)/6*I(-162).exp()
        real_tails[j] = bound
        for m in (0, 2):
            integrals[j, m] += I(bound.hi.copy_negate(), bound.hi)

    b0, a0 = integrals[0, 0], integrals[0, 2]
    b2, a2 = integrals[2, 0], integrals[2, 2]
    b4, a4 = integrals[4, 0], integrals[4, 2]
    v0 = a0/b0
    v2 = (a2-v0*b2)/b0
    v4 = (a4-v0*b4-6*v2*b2)/b0
    determinant = v0*v4-v2**2
    verdict = ('POSITIVE' if determinant.lo > 0 else
               'NEGATIVE' if determinant.hi < 0 else 'INCONCLUSIVE')
    certificate = {
        'target': "V(0)V''''(0)-V''(0)^2",
        'arithmetic': {'method': 'directed Decimal; adjacent correctly-rounded exponentials',
                       'precision': PRECISION, 'pi_method': 'Machin alternating series, 40 terms each',
                       'pi': pi.record()},
        'configuration': {'interval': [0, 2], 'cells': args.cells, 'theta_modes': 4,
                          'quadrature': 'interval midpoint with second derivative Peano bound'},
        'polynomials': [[str(c) for c in p] for p in ps],
        'polynomial_absolute_coefficient_sums': [str(m) for m in ms],
        'omitted_theta_derivative_uniform_bounds': [t.record() for t in theta_tails],
        'theta_geometric_ratios': [r.record() for r in ratios],
        'unbounded_integral_tail_bounds': {str(j): t.record() for j, t in real_tails.items()},
        'integrals': {f'{"b" if m == 0 else "a"}{j}': v.record() for (j, m), v in integrals.items()},
        'midpoint_error_sums': {f'{"b" if m == 0 else "a"}{j}': v.record() for (j, m), v in error_sums.items()},
        'jet': {'v0': v0.record(), 'v2': v2.record(), 'v4': v4.record(),
                'determinant': determinant.record()},
        'threshold': '0', 'verdict': verdict, 'failures': [],
        'qualification': 'Necessary condition only. No positive definiteness or RH conclusion.'
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print('determinant:', determinant.record(), 'required threshold: 0')
    print('verdict:', verdict, 'failures:', certificate['failures'], 'certificate:', path)


if __name__ == '__main__':
    main()
