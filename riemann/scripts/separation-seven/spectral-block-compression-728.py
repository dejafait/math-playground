#!/usr/bin/env python3
"""Fixed 17-node dyadic Gaussian construction. Full evidence, not scalar work.

Interval endpoints use correctly directed Decimal basic arithmetic. Numpy
supplies guesses only; disjoint certified sign changes prove root locations.
The arithmetic counter is a subtotal, not a certified all-work upper bound.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
PREC = 256
DOWN = Context(prec=PREC, rounding=ROUND_FLOOR)
UP = Context(prec=PREC, rounding=ROUND_CEILING)
OPS = {'decimal_basic': 0, 'decimal_comparisons': 0, 'fraction_high_level': 0}
M, K, EM = 17, 72, 64
START = time.monotonic()


class I:
    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, D) else D(lo)
        self.hi = self.lo if hi is None else (hi if isinstance(hi, D) else D(hi))
        assert self.lo <= self.hi

    @staticmethod
    def q(q):
        q = F(q)
        OPS['decimal_basic'] += 2
        return I(DOWN.divide(D(q.numerator), D(q.denominator)),
                 UP.divide(D(q.numerator), D(q.denominator)))

    def __add__(self, b):
        b = b if isinstance(b, I) else I(b)
        OPS['decimal_basic'] += 2
        return I(DOWN.add(self.lo, b.lo), UP.add(self.hi, b.hi))

    __radd__ = __add__

    def __neg__(self):
        return I(self.hi.copy_negate(), self.lo.copy_negate())

    def __sub__(self, b):
        return self + -(b if isinstance(b, I) else I(b))

    def __rsub__(self, b):
        return -self + b

    def __mul__(self, b):
        b = b if isinstance(b, I) else I(b)
        OPS['decimal_basic'] += 8
        OPS['decimal_comparisons'] += 6
        lows = [DOWN.multiply(x, y) for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        highs = [UP.multiply(x, y) for x in (self.lo, self.hi) for y in (b.lo, b.hi)]
        return I(min(lows), max(highs))

    __rmul__ = __mul__

    def __truediv__(self, b):
        b = b if isinstance(b, I) else I(b)
        OPS['decimal_comparisons'] += 2
        assert b.lo > 0 or b.hi < 0, 'division interval contains zero'
        OPS['decimal_basic'] += 2
        return self * I(DOWN.divide(D(1), b.hi), UP.divide(D(1), b.lo))

    def power(self, n):
        assert n >= 0
        result, base = I(1), self
        while n:
            if n & 1:
                result = result * base
            n >>= 1
            if n:
                base = base * base
        return result

    def sign(self):
        OPS['decimal_comparisons'] += 2
        return 1 if self.lo > 0 else (-1 if self.hi < 0 else 0)

    def midpoint(self):
        OPS['decimal_basic'] += 2
        return DOWN.divide(DOWN.add(self.lo, self.hi), D(2))

    def width(self):
        OPS['decimal_basic'] += 1
        return UP.subtract(self.hi, self.lo)

    def export(self):
        return [str(self.lo), str(self.hi)]


def rat_op(n=1):
    OPS['fraction_high_level'] += n


# Exact Bernoulli coefficients; these operations are not unit-cost integers.
bern = [F(1)]
for n in range(1, 2*EM+1):
    bern.append(-sum(F(comb(n+1, j))*bern[j] for j in range(n))/F(n+1))
    rat_op(2*n+2)
periodic_bound = abs(bern[2*EM]) + sum(F(comb(2*EM, j))*abs(bern[j]) for j in range(2*EM+1))
rat_op(4*EM+3)


def log_ratio(u, v):
    # z=(v-u)/(v+u) is in (0,1/3); log(v/u)=2 atanh(z).
    zq = (v-u)/(v+u)
    rat_op(3)
    assert 0 < zq < F(1, 3)
    z = I.q(zq)
    z2 = z*z
    term, total = z, I(0)
    for i in range(256):
        total = total + term/I(2*i+1)
        term = term*z2
    # R <= 2*z^513/(513*(1-z^2)); upper bound z<1/3.
    remainder = I.q(F(2, 513*3**513)*F(9, 8))
    return total*2 + I(0, remainder.hi)


def moments(J):
    if J < 256:
        raw = [F(0) for _ in range(2*M+1)]
        for j in range(J, 2*J):
            x = F(4*j+1, 4*J)
            value = 1/(J*x*x)
            rat_op(4)
            for p in range(2*M+1):
                raw[p] += value
                value *= x
                rat_op(2)
        xm = [I.q(v) for v in raw]
        inverse_errors = ['0', '0']
    else:
        u, v = F(4*J+1, 4), F(8*J+1, 4)
        invu, invv = I.q(1/u), I.q(1/v)
        rat_op(2)
        diff = invu-invv
        s1 = log_ratio(u, v) + diff/2
        s2 = diff + (invu*invu-invv*invv)/2
        for r in range(1, EM):
            s1 = s1 + I.q(bern[2*r]/(2*r))*(invu.power(2*r)-invv.power(2*r))
            s2 = s2 + I.q(bern[2*r])*(invu.power(2*r+1)-invv.power(2*r+1))
            rat_op()
        # Exact DLMF 2.10.1 remainder with |B_2m-Btilde_2m| bounded
        # by absolute coefficients on [0,1]. Integral extended to infinity.
        r1 = periodic_bound/(2*EM)*u**(-2*EM)
        r2 = periodic_bound*u**(-2*EM-1)
        rat_op(6)
        e1, e2 = I.q(r1), I.q(r2)
        xm = [(s2+I(e2.hi.copy_negate(), e2.hi))*I(J), s1+I(e1.hi.copy_negate(), e1.hi)]
        inverse_errors = [str(r2*J), str(r1)]
        # Telescoping (j+c+1)^(q+1)-(j+c)^(q+1), not enumeration.
        sums = []
        for q in range(2*M-1):
            sq = (v**(q+1)-u**(q+1)-sum(F(comb(q+1, p))*sums[p] for p in range(q)))/(q+1)
            rat_op(2*q+6)
            sums.append(sq)
            xm.append(I.q(sq/J**(q+1)))
            rat_op(2)
    # t=2x-3. Exact binomial coefficients; interval cancellation retained.
    tm = []
    for n in range(2*M+1):
        val = I(0)
        for q in range(n+1):
            val = val + xm[q]*I(comb(n, q)*2**q*(-3)**(n-q))
        tm.append(val)
    return tm, inverse_errors


def inner(a, b, mu, shift=0):
    val = I(0)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            val = val + ai*bj*mu[i+j+shift]
    return val


def orthogonal(mu):
    polynomials, norms = [], []
    p, prev = [I(1)], [I(0)]
    for n in range(M):
        h = inner(p, p, mu)
        assert h.lo > 0, ('norm positivity', n, h.export())
        polynomials.append(p)
        norms.append(h)
        alpha = inner(p, p, mu, 1)/h
        beta = h/norms[n-1] if n else I(0)
        nxt = [I(0)]+p
        for i, pi in enumerate(p):
            nxt[i] = nxt[i]-alpha*pi
        if n:
            for i, pi in enumerate(prev):
                nxt[i] = nxt[i]-beta*pi
        prev, p = p, nxt
    return p, polynomials, norms


def evaluate(poly, t):
    value = poly[-1]
    for a in reversed(poly[:-1]):
        value = value*t+a
    return value


def roots(poly):
    # Library computation supplies guesses only and is outside counted subtotal.
    guesses = np.polynomial.polynomial.polyroots([float(a.midpoint()) for a in poly])
    assert len(guesses) == M and all(abs(complex(g).imag) < 1e-10 for g in guesses)
    result = []
    for guess in sorted(float(complex(g).real) for g in guesses):
        center = D(str(guess))
        left = DOWN.subtract(center, D('1e-7'))
        right = UP.add(center, D('1e-7'))
        assert D(-1) < left < right < D(1)
        sl, sr = evaluate(poly, I(left)).sign(), evaluate(poly, I(right)).sign()
        assert sl*sr == -1, ('root guess not certified by signs', guess, sl, sr,
                            evaluate(poly, I(left)).export(), evaluate(poly, I(right)).export())
        while UP.subtract(right, left) > D('1e-40'):
            middle = DOWN.divide(DOWN.add(left, right), D(2))
            OPS['decimal_basic'] += 3
            sign = evaluate(poly, I(middle)).sign()
            assert sign != 0, 'insufficient polynomial coefficient precision'
            if sign == sl:
                left = middle
            else:
                right = middle
        if result:
            assert result[-1].hi < left
        result.append(I(left, right))
    return result


def block(k):
    J = 2**k
    mu, inverse_errors = moments(J)
    poly, orth, norms = orthogonal(mu)
    rr = roots(poly)
    nodes, wsum, err = [], I(0), I(0)
    for root in rr:
        kernel = I(0)
        for p, h in zip(orth, norms):
            value = evaluate(p, root)
            kernel = kernel+value*value/h
        assert kernel.lo > 0
        weight = I(1)/kernel/I(4*J)
        assert weight.lo > 0
        wsum = wsum+weight
        # Use exact finite decimals at the bracket midpoints as output constants.
        t, w = root.midpoint(), weight.midpoint()
        radius_t = max(UP.subtract(t, root.lo), UP.subtract(root.hi, t))
        radius_w = max(UP.subtract(w, weight.lo), UP.subtract(weight.hi, w))
        # rate=J*(t+3); min normalized t+3>2, hence uniform exponential
        # sensitivity <=radius_t (valid for all r>=0).
        err = err+I(radius_w)+I(w)*I(radius_t)
        rate = I(J)*(I(t)+3)
        assert rate.lo > 0 and rate.lo == rate.hi, 'finite decimal rate not exact at fixed precision'
        nodes.append({'t': str(t), 'weight': str(w), 'rate': str(rate.lo),
                      'root_bracket': root.export(), 'weight_enclosure': weight.export(),
                      'root_endpoint_signs': [evaluate(poly, I(root.lo)).sign(), evaluate(poly, I(root.hi)).sign()]})
    exact_mass = mu[0]/I(4*J)
    assert wsum.lo <= exact_mass.hi and exact_mass.lo <= wsum.hi
    return {'k': k, 'J': J, 'inverse_moment_EM_bounds': inverse_errors,
            'moments_t': [v.export() for v in mu],
            'orthogonal_polynomials': [[v.export() for v in p] for p in orth],
            'norms': [v.export() for v in norms], 'degree17_polynomial': [v.export() for v in poly],
            'nodes': nodes, 'coefficient_kernel_error_upper': str(err.hi),
            'mass_enclosure': exact_mass.export(), 'weight_sum_enclosure': wsum.export()}


report = {'scope': 'C998u unchanged G; uniform kernel preparation only; not scalar or signed S3',
          'parameters': {'B': 2**23, 'm': M, 'K': K, 'precision_decimal_digits': PREC, 'EM_order': EM},
          'blocks': [], 'failures': [], 'full_construction_cost_certified': False,
          'operation_counter_qualification': 'subtotal of Decimal basic/comparison and high-level Fraction calls; excludes integer algorithms, numpy guesses, host control, allocation and output; not all-work bound',
          'source_sha256': sha256(HERE.read_bytes()).hexdigest()}
try:
    for k in range(5, K):
        row = block(k)
        report['blocks'].append(row)
        if k in (5, 7, 8, 20, 40, 60, 71):
            print('certified block', k, 'root count', len(row['nodes']), 'Decimal arithmetic subtotal', OPS['decimal_basic'], flush=True)
except Exception as exc:
    report['failures'].append(type(exc).__name__+': '+str(exc))

theory = F(30*2**46, 5**34)+F(2**46, 4*2**72-3)
report['theoretical'] = {'rank': 32+67*17, 'weighted_gaussian_bound': str(F(30*2**46, 5**34)),
                         'weighted_tail_bound': str(F(2**46, 4*2**72-3)),
                         'sum_upper_bound': str(theory), 'required': '1/10000000',
                         'analytic_budget_pass': theory < F(1, 10**7)}
coefficient = sum((D(row['coefficient_kernel_error_upper']) for row in report['blocks']), D(0))
# Summation above is reporting only; exact rational conversion pays its rounding.
coefficient_exact = sum((F(row['coefficient_kernel_error_upper']) for row in report['blocks']), F(0))
report['coefficient_error_weighted_bound'] = str(coefficient_exact*2**46)
report['complete_gaussian_block_count'] = len(report['blocks'])
report['all_67_blocks_certified'] = len(report['blocks']) == 67 and not report['failures']
report['full_uniform_budget_pass'] = report['all_67_blocks_certified'] and theory+coefficient_exact*2**46 < F(1, 10**7)
report['operation_subtotals'] = OPS
report['required_operation_cap'] = 10**8
report['elapsed_seconds_not_work_proof'] = time.monotonic()-START
report['unpaid'] = ['complete finite construction operation ledger and storage bound',
                    'independent conceptual/arithmetic audit', 'density quadrature and signed coupling',
                    'full scalar evaluation, local term and remaining 9e-7']
OUT.write_text(json.dumps(report, indent=2)+'\n')
print('Blocks:', len(report['blocks']), '/67; failures:', report['failures'])
print('Rank:', report['theoretical']['rank'], '; weighted analytic bound:', float(theory), '; required <=1e-7')
print('Full uniform error passed:', report['full_uniform_budget_pass'], '; construction work cap: UNPAID')
print('Operation subtotals:', OPS, '; allowed all-work cap:', 10**8)
print('Certificate:', OUT.relative_to(HERE.parent.parent.parent))
