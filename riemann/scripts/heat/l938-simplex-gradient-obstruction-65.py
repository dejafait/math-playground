#!/usr/bin/env python3
"""Exact rational bounds for one two-field subfamily of the step65 test.

This does not test the full degree-13 field space. No floating-point or
Decimal transcendental operation is used. The full certificate is JSON.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from math import comb, factorial, isqrt, prod
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_suffix('.json')
DEN = 2**160
REPORT = {'scope': 'X=c X_Pbar+d X_p2 only; not the full degree-13 class',
          'arithmetic': 'integers, rational interval arithmetic, rational Taylor bounds',
          'checks': [], 'failures': [], 'witnesses': []}


def check(name, condition, actual=None, required=None):
    entry = {'name': name, 'passed': bool(condition)}
    if actual is not None:
        entry['actual'] = actual
    if required is not None:
        entry['required'] = required
    REPORT['checks'].append(entry)
    if not condition:
        REPORT['failures'].append(entry)


def floor_dyadic(x):
    return F((x.numerator*DEN)//x.denominator, DEN)


def ceil_dyadic(x):
    return -floor_dyadic(-x)


class I:
    def __init__(self, lo, hi=None):
        lo, hi = F(lo), F(lo if hi is None else hi)
        assert lo <= hi
        self.lo, self.hi = floor_dyadic(lo), ceil_dyadic(hi)

    @staticmethod
    def cast(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, y):
        y = I.cast(y)
        return I(self.lo+y.lo, self.hi+y.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, y):
        return self + -I.cast(y)

    def __rsub__(self, y):
        return I.cast(y) + -self

    def __mul__(self, y):
        y = I.cast(y)
        vals = [a*b for a in (self.lo, self.hi) for b in (y.lo, y.hi)]
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, y):
        y = I.cast(y)
        assert y.lo*y.hi > 0, 'zero-containing interval divisor'
        return self*I(1/y.hi, 1/y.lo)

    def __pow__(self, n):
        assert n >= 0
        out, z = I(1), self
        while n:
            if n & 1:
                out = out*z
            z = z*z
            n //= 2
        return out

    def data(self):
        return [str(self.lo), str(self.hi)]


def exp_point(x):
    """Positive Taylor series after dyadic reduction; fixed 64 terms."""
    x = F(x)
    if x < 0:
        return I(1)/exp_point(-x)
    reduced, squares = x, 0
    while reduced > F(1, 8):
        reduced /= 2
        squares += 1
    term, total = F(1), F(1)
    for j in range(1, 65):
        term *= reduced/j
        total += term
    next_term = term*reduced/65
    remainder = next_term/(1-reduced/66)
    value = I(total, total+remainder)
    for _ in range(squares):
        value = value*value
    return value


def exp_interval(x):
    return I(exp_point(x.lo).lo, exp_point(x.hi).hi)


def sqrt_interval(x):
    assert x.lo >= 0
    a = isqrt((x.lo.numerator*DEN**2)//x.lo.denominator)
    b = isqrt((x.hi.numerator*DEN**2)//x.hi.denominator)+1
    out = I(F(a, DEN), F(b, DEN))
    assert out.lo**2 <= x.lo and out.hi**2 >= x.hi
    return out


def atan_reciprocal(n):
    total = sum((F((-1)**j, (2*j+1)*n**(2*j+1))
                 for j in range(100)), F(0))
    return I(total, total+F(1, 201*n**201))


def polynomial_eval(p, x):
    out = x*0
    for c in reversed(p):
        out = out*x+c
    return out


def derivative(p):
    return [j*p[j] for j in range(1, len(p))]


def bernstein_coefficients(p, lo, hi):
    n = len(p)-1
    powers = [sum((p[k]*comb(k, j)*lo**(k-j)*(hi-lo)**j
                   for k in range(j, n+1)), F(0)) for j in range(n+1)]
    return [sum((powers[j]*F(comb(i, j), comb(n, j))
                 for j in range(i+1)), F(0)) for i in range(n+1)]


def coarse_bounds(x, scale):
    lo = F((x.lo*scale).__floor__(), scale)
    hi = F((x.hi*scale).__ceil__(), scale)
    assert lo <= x.lo <= x.hi <= hi
    return [str(lo), str(hi)]


def root_bracket(p, lo, hi):
    assert polynomial_eval(p, lo) > 0 > polynomial_eval(p, hi)
    for _ in range(40):
        mid = (lo+hi)/2
        value = polynomial_eval(p, mid)
        assert value != 0, 'unexpected exact root: retain a nondegenerate bracket'
        if value > 0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def theta_score(x, pi):
    """k'(x)/k(x), retaining n=1,...,4 and both full-sum tails."""
    u = sqrt_interval(x)
    assert 0 < u.lo <= u.hi <= F(1, 4)
    e2u, ehalf = exp_interval(2*u), exp_interval(u/2)
    kernel, du_kernel, terms = I(0), I(0), []
    for n in range(1, 5):
        v = pi*n*n*e2u
        common = ehalf*exp_interval(-v)
        a = common*(8*v**2-12*v)
        b = common*(-16*v**3+60*v**2-30*v)
        kernel, du_kernel = kernel+a, du_kernel+b
        terms.append({'n': n, 'v': v.data(), 'K_term': a.data(), 'K_prime_term': b.data()})
    ratio = F(3, 20**11)
    tail_k = F(1216*5**4, 20**25)/(1-ratio)
    tail_du = F(24544*5**6, 20**25)/(1-ratio)
    kernel = kernel+I(0, tail_k)
    du_kernel = du_kernel+I(-tail_du, tail_du)
    assert kernel.lo > 0
    score = du_kernel/(2*u*kernel)
    return score, {'x': x.data(), 'u': u.data(), 'terms': terms,
                   'K_tail_bound': str(tail_k), 'K_prime_tail_bound': str(tail_du),
                   'K': kernel.data(), 'K_prime': du_kernel.data(), 'score': score.data()}


def main():
    src = ROOT/'lemmas/L938-actual-h2-fixed-energy-density-and-cell-test.md'
    assessment = ROOT/'drafts/literature/2026-11-09-l938-simplex-residual-certificate-test-63.md'
    REPORT['input_sha256'] = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                              for p in (src, assessment, Path(__file__))}
    raw = re.findall(r'^\|\s*(-?\d+)\s*\|\s*\(([^)]+)\)\s*\|\s*$', src.read_text(), re.M)
    rows = [(int(c), tuple(map(int, a.split(',')))) for c, a in raw]
    check('34 rows', len(rows) == 34, len(rows), 34)
    check('all row degrees', all(sum(a) == 12 and sum(k*v for k, v in enumerate(a)) == 12
                                for _, a in rows))
    lowering = {}
    for c, a in rows:
        for k in range(1, 7):
            if not a[k]:
                continue
            b = list(a)
            b[k] -= 1
            b[k-1] += 1
            b = tuple(b)
            lowering[b] = lowering.get(b, 0)+c*a[k]
    REPORT['gaussian_lowering_coefficients'] = [
        {'alpha': a, 'coefficient': c} for a, c in sorted(lowering.items())]
    check('all Gaussian-lowering coefficients vanish', all(c == 0 for c in lowering.values()))
    check('every monomial vanishes on a two-coordinate face',
          all(sum(a[1:]) >= 3 for _, a in rows))

    pi = 16*atan_reciprocal(5)-4*atan_reciprocal(239)
    REPORT['pi'] = pi.data()
    check('3<pi<4', 3 < pi.lo < pi.hi < 4)
    check('positive Taylor lower bound exp(3)>20',
          sum((F(3**j, factorial(j)) for j in range(9)), F(0)) > 20)
    check('tail ratio bound (6/5)^6<3', F(6, 5)**6 < 3)
    check('exp(1/2)<2', exp_point(F(1, 2)).hi < 2)

    specifications = [
        (1, 1140694410240000,
         [1485, -2562, 9415, -9996, 6795, -2002, -63], F(3, 2), F(2)),
        (4, 501905540505600000,
         [-3717, 287497, -3221575, 10631299, -5542978, -29318198,
          69213634, -63981834, 29038487, -6214019, 451605, 13111, -1632],
         F(541, 4096), F(271, 2048))]
    responses, quadratic_responses = [], []
    for m, denominator, numerator, initial_lo, initial_hi in specifications:
        coefficients = [F(0)]*13
        row_records = []
        for c, a in rows:
            ks = [k for k, count in enumerate(a) for _ in range(count)]
            counts = [0]*13
            for subset in combinations(range(12), m):
                counts[sum(ks[j] for j in subset)] += 1
            fac = prod(factorial(2*k) for k in ks)
            contribution = [F(c*n, fac*comb(12, m)) for n in counts]
            coefficients = [x+y for x, y in zip(coefficients, contribution)]
            row_records.append({'coefficient': c, 'alpha': a, 'factorial': str(fac),
                                'subset_counts': counts, 'contribution': list(map(str, contribution))})
        expected = [F(n, denominator) for n in numerator]+[F(0)]*(13-len(numerator))
        check(f'm={m}: original factorial-weighted rows reproduce H', coefficients == expected)
        lo, hi = root_bracket(numerator, initial_lo, initial_hi)
        dbern = bernstein_coefficients(derivative(numerator), lo, hi)
        check(f'm={m}: root endpoint signs', polynomial_eval(numerator, lo) > 0 > polynomial_eval(numerator, hi))
        check(f'm={m}: derivative is strictly negative throughout isolator', max(dbern) < 0,
              str(max(dbern)), '<0')
        q = I(lo, hi)
        s = m*q+(12-m)
        a, b = q/s, I(1)/s
        score_a, evidence_a = theta_score(a/4, pi)
        score_b, evidence_b = theta_score(b/4, pi)
        difference = score_a-score_b
        expected_sign = -1 if m == 1 else 1
        check(f'm={m}: full-theta score difference has required strict sign',
              difference.hi < 0 if expected_sign < 0 else difference.lo > 0,
              difference.data(), '<0' if expected_sign < 0 else '>0')
        hprime = I(min(dbern), max(dbern))/denominator
        response = q*hprime*difference/(4*s**12)
        responses.append(response)
        check(f'm={m}: gradient-P response sign', response.lo > 0 if m == 1 else response.hi < 0,
              response.data(), '>0' if m == 1 else '<0')
        p2 = m*a**2+(12-m)*b**2
        weighted_score = m*a*score_a+(12-m)*b*score_b
        weighted_square_score = m*a**2*score_a+(12-m)*b**2*score_b
        quadratic = 3-14*p2+(weighted_square_score-p2*weighted_score)/2
        quadratic_responses.append(quadratic)
        check(f'm={m}: gradient-p2 response is positive', quadratic.lo > 1,
              quadratic.data(), '>1')
        REPORT['witnesses'].append({
            'm': m, 'denominator': str(denominator), 'numerator': numerator,
            'row_reconstruction': row_records, 'initial_bracket': [str(initial_lo), str(initial_hi)],
            'root_bracket': [str(lo), str(hi)],
            'endpoint_values': [str(polynomial_eval(numerator, lo)), str(polynomial_eval(numerator, hi))],
            'derivative_bernstein': list(map(str, dbern)),
            'score_a_evidence': evidence_a, 'score_b_evidence': evidence_b,
            'score_difference': difference.data(), 'gradient_P_response': response.data(),
            'p2': p2.data(), 'gradient_p2_response': quadratic.data()})

    a1, a4 = responses
    b1, b4 = quadratic_responses
    w1, w4 = -a4, a1
    wvertex = (w1*b1+w4*b4)/11
    REPORT['dual'] = {
        'exact_weights': ['-A4', 'A1', '((-A4)*B1+A1*B4)/11'],
        'weight_bounds': [w1.data(), w4.data(), wvertex.data()],
        'rows': ['m=1 algebraic zero', 'm=4 algebraic zero', 'vertex limit'],
        'exact_columns': {'X_Pbar': ['A1', 'A4', '0'],
                          'X_p2': ['B1', 'B4', '-11'],
                          'Pbar': ['0', '0', '0'], 'E_Pbar': ['0', '0', '0'],
                          'radial': ['0', '0', '0']},
        'weighted_radial_value': '0', 'required_for_strict_margin': '>0',
        'scope': 'annihilates the two tested field columns only'}
    REPORT['summary'] = {
        'energy': '1/4', 'root_brackets': [w['root_bracket'] for w in REPORT['witnesses']],
        'score_difference_bounds': [coarse_bounds(I(*w['score_difference']), 1000)
                                    for w in REPORT['witnesses']],
        'A_bounds': [coarse_bounds(a, 10**28) for a in responses],
        'B_bounds': [coarse_bounds(b, 1000) for b in quadratic_responses],
        'positive_weight_bounds': [coarse_bounds(w, 10**28) for w in (w1, w4, wvertex)],
        'radial_value': '0', 'required': '>0'}
    check('all three exact dual weights are strictly positive',
          all(w.lo > 0 for w in (w1, w4, wvertex)))
    REPORT['result'] = 'two-field strict certificate impossible' if not REPORT['failures'] else 'FAILED'
    OUT.write_text(json.dumps(REPORT, indent=2)+'\n')
    print(f"Result: {REPORT['result']}; checks={len(REPORT['checks'])}; failures={len(REPORT['failures'])}")
    print('Actual dual radial value=0; required value>0. Full degree-13 class remains unresolved.')
    print('Gradient-P response bounds: '+str(REPORT['summary']['A_bounds']))
    print('Gradient-p2 response bounds: '+str(REPORT['summary']['B_bounds']))
    print('Exact positive weights and full-kernel bounds: '+str(OUT.relative_to(ROOT)))
    if REPORT['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
