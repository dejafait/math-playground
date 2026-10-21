"""Capped range enclosure of precisely L426's I. Standard library only.

All proof decisions use integers. Endpoints are multiples of 10^-24.
The certificate includes every product cell, not a sample or a preview.
Correct execution of Python integer arithmetic/isqrt is the contract.
"""
import json
from fractions import Fraction as F
from itertools import product
from math import factorial, isqrt
from pathlib import Path

SCALE = 10**24
CAP = 32768


def ceildiv(a, b):
    return -((-a)//b)


class I:
    __slots__ = ('lo', 'hi')

    def __init__(self, lo, hi=None, raw=False):
        if raw:
            self.lo, self.hi = lo, hi
        else:
            x = F(lo)
            self.lo = x.numerator*SCALE//x.denominator
            self.hi = ceildiv(x.numerator*SCALE, x.denominator)
        assert self.lo <= self.hi

    @staticmethod
    def lift(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, x):
        x = I.lift(x)
        return I(self.lo+x.lo, self.hi+x.hi, True)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo, True)

    def __sub__(self, x):
        return self + (-I.lift(x))

    def __rsub__(self, x):
        return I.lift(x) + (-self)

    def __mul__(self, x):
        x = I.lift(x)
        v = [a*b for a in (self.lo, self.hi) for b in (x.lo, x.hi)]
        return I(min(v)//SCALE, ceildiv(max(v), SCALE), True)

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = I.lift(x)
        assert x.lo > 0, 'nonpositive divisor'
        return self * I(SCALE*SCALE//x.hi, ceildiv(SCALE*SCALE, x.lo), True)

    def square(self):
        lo = 0 if self.lo <= 0 <= self.hi else min(self.lo*self.lo, self.hi*self.hi)
        hi = max(self.lo*self.lo, self.hi*self.hi)
        return I(lo//SCALE, ceildiv(hi, SCALE), True)

    def sqrt(self):
        assert self.lo >= 0, 'negative radicand'
        lo, hi = isqrt(self.lo*SCALE), isqrt(self.hi*SCALE)
        if hi*hi < self.hi*SCALE:
            hi += 1
        return I(lo, hi, True)

    def power(self, n):
        assert n >= 0
        out = I(1)
        for _ in range(n):
            out = out*self
        return out

    def intersect(self, x):
        return I(max(self.lo, x.lo), min(self.hi, x.hi), True)

    def enc(self):
        return {'lower': str(F(self.lo, SCALE)), 'upper': str(F(self.hi, SCALE))}


def pi_interval():
    # L037's Machin identity and alternating remainder, with 48 terms.
    def atan(q):
        x = F(1, q)
        v = sum(((-1)**k*x**(2*k+1)/ (2*k+1) for k in range(48)), F(0))
        r = x**97/97
        return I(v) + I(0, ceildiv(r.numerator*SCALE, r.denominator), True)
    return 16*atan(5)-4*atan(239)


PI = pi_interval()
UNIT = I(-SCALE, SCALE, True)


def trig(x, cosine=False):
    # Taylor polynomial at a scalar midpoint; |derivative|<=1 propagates
    # the whole argument interval. Degree 96, |x|<=7, remainder <=7^97/97!.
    assert 0 <= x.lo <= x.hi <= 7*SCALE
    m = (x.lo+x.hi)//2
    z = I(m, m, True)
    term = I(1) if cosine else z
    total = term
    start = 0 if cosine else 1
    for k in range(1, 49):
        term = -term*z.square()/((start+2*k-1)*(start+2*k))
        total = total+term
    err = I(F(7**97, factorial(97))).hi + max(m-x.lo, x.hi-m)
    return I(total.lo-err, total.hi+err, True).intersect(UNIT)


def exp_negative(x):
    assert x.lo >= 0
    def point(n):
        k = 0
        while n > SCALE//8:
            # Keep exact n/2^k by doing the division through intervals below.
            k += 1
            if n <= (SCALE//8)*(2**k):
                break
        z = I(n, n, True)/(2**k)
        term = total = I(1)
        for j in range(1, 19):
            term = -term*z/j
            total = total+term
        err = I(F(1, 8**19*factorial(19))).hi
        total = I(total.lo-err, total.hi+err, True)
        for _ in range(k):
            total = total.square()
        return total.intersect(I(0, SCALE, True))
    return I(point(x.hi).lo, point(x.lo).hi, True)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), I(0))


def mv(a, v):
    return [dot(row, v) for row in a]


def matrix_product(a, b):
    return [[dot(row, col) for col in zip(*b)] for row in a]


def rotate(a, basis, gaps=None):
    n = len(a)
    if gaps is None:
        tau = sum((a[j][j] for j in range(n)), I(0))/n
        gaps = [a[j][j]-tau for j in range(n)]
    if any(g.lo <= 0 <= g.hi for g in gaps):
        raise ValueError('unresolved original/complementary equality')
    i, j = next((i, j) for i in range(n) for j in range(n)
                if gaps[i].hi < 0 < gaps[j].lo)
    low, high, off = -gaps[i], gaps[j], a[i][j]
    rad = (off.square()+high*low).sqrt()
    # The original positive root; rationalization preserves exactly its sign.
    eta = low/(rad+off) if off.lo >= 0 else (rad-off)/high
    norm = (1+eta.square()).sqrt()
    first = [((basis[i][k]+eta*basis[j][k])/norm).intersect(UNIT) for k in range(3)]
    second = [((-eta*basis[i][k]+basis[j][k])/norm).intersect(UNIT) for k in range(3)]
    rest = [second]+[basis[k] for k in range(n) if k not in (i, j)]
    return first, rest, (i, j)


d = I(1)/(6*I(5).sqrt())
D = (I(F(81, 80))+2*d).sqrt()
P = [[(1+d)/D, I(0), -I(1)/(12*D)],
     [I(0), I(1)/I(12).sqrt(), I(0)],
     [-I(1)/(12*D), I(0), (I(F(1, 80))+d)/D]]
COORD = [[I(int(i == j)) for j in range(3)] for i in range(3)]
ROW_BOUNDS = [I(1), I(F(1, 12)).sqrt(), I(F(1, 80)).sqrt()]


def selector(cell, count):
    angle = 2*PI*I(F(cell, count))
    angle = I(angle.lo, (2*PI*I(F(cell+1, count))).hi, True)
    c, s = trig(angle, True), trig(angle)
    c2, s2, cs = c.square(), s.square(), c*s
    j = [[c2/16, -cs/4, c2/4+s2/2],
         [-cs/4, -c2, cs], [c2/4+s2/2, cs, c2]]
    a = matrix_product(matrix_product(P, j), P)
    try:
        tau = sum((a[j][j] for j in range(3)), I(0))/3
        gaps = [a[j][j]-tau for j in range(3)]
        first, rest, pair = rotate(a, COORD, gaps)
        # L425's exact trace identity: complementary gaps are (-D_k,D_k).
        # This avoids recomputing an equal trace with dependent intervals.
        unused = next(k for k in range(3) if k not in pair)
        b = [[dot(v, mv(a, w)) for w in rest] for v in rest]
        second, final, _ = rotate(b, rest, [-gaps[unused], gaps[unused]])
        vectors = [first, second, final[0]]
        out = []
        for u in vectors:
            v = mv(P, u)
            v = [v[k].intersect(I(-ROW_BOUNDS[k].hi, ROW_BOUNDS[k].hi, True)) for k in range(3)]
            out.append(v)
        return out, None
    except (ValueError, AssertionError) as exc:
        return None, str(exc)


def source_coefficients(directory):
    data = json.loads((directory/'response-modulus-second-moment-certificate.json').read_text())
    assert not data['failures'] and all(data['checks'].values())
    def get(rec):
        return I(I(F(rec['lower'])).lo, I(F(rec['upper'])).hi, True)
    b = data['bounds']
    c = {int(j): get(v) for j, v in b['C'].items()}
    s, t, b13, b14 = [get(b[j]) for j in ('S', 'T', 'B13', 'B14')]
    alpha = (b14-t)/(b14-b13)
    theta = {j: (s-c[1])/(c[j+1]/c[j]-c[1]) for j in (13, 14)}
    assert 0 < alpha.lo <= alpha.hi < SCALE
    assert all(0 < v.lo <= v.hi < SCALE for v in theta.values())
    def g(w):
        gj = {j: 1-theta[j]+theta[j]*w.power(j)/c[j] for j in (13, 14)}
        return alpha*gj[13]+(1-alpha)*gj[14]
    return g, {'alpha': alpha.enc(), 'theta': {str(k): v.enc() for k, v in theta.items()},
               'source_bounds': b}


def q_range(g, v):
    root = (3*g).sqrt()
    a, b, d0 = [root*x for x in v]
    aa, bb = a.square(), b.square()
    poly = bb*(1-2*aa)+a*d0*(1-2*bb)
    return exp_negative(aa+bb)*poly


def main():
    directory = Path(__file__).parent
    g, coefficients = source_coefficients(directory)
    # Every omitted prime power: |log factor|<=q/(1-q).
    primes = [n for n in range(7, 201) if all(n % j for j in range(2, isqrt(n)+1))]
    tail = I(0)
    for p in primes:
        q = I(1)/(p*p*I(p).sqrt())
        tail = tail+q/(1-q)
    # Integral bound for sum_(n>200) n^-5/2, then uniform geometric denominator.
    residual = (I(2)/(3*200*I(200).sqrt()))/(1-I(1)/(201*201*I(201).sqrt()))
    tail = tail+residual
    assert tail.hi < SCALE
    # exp(+-tail) inside [1-tail,1/(1-tail)]; square for W.
    tail_factor = I((1-tail).square().lo, (I(1)/(1-tail).square()).hi, True)
    response_cells = []
    for indices in product(range(4), repeat=3):
        w = I(1)
        for p, k in zip((2, 3, 5), indices):
            angle = I((PI*I(F(k, 4))).lo, (PI*I(F(k+1, 4))).hi, True)
            co = trig(angle, True)
            q = I(1)/(p*p*I(p).sqrt())
            w = w*(I(1)/(1-2*q*co+q.square()))
        w = w*tail_factor
        gv = g(w)
        assert gv.lo > 0
        response_cells.append((indices, w, gv))
    selector_cells = [selector(k, 512) for k in range(512)]
    assert len(response_cells)*len(selector_cells) == CAP
    result = I(0)
    unresolved_budget = I(0)
    strict_budget = I(0)
    records = []
    for indices, w, gv in response_cells:
        # Unit u gives |d|<=sqrt(3g K33). Calculus gives
        # |(1-2x)e^-x|<=1, y e^-y<=1/2, sqrt(x)e^-x<=1/2.
        bound = (1+(3*gv/80).sqrt())/2
        fallback = I(-bound.hi, bound.hi, True)
        for k, (vectors, reason) in enumerate(selector_cells):
            value = fallback if vectors is None else sum(
                (q_range(gv, v).intersect(fallback) for v in vectors), I(0))/3
            result = result+value/CAP
            if vectors is None:
                unresolved_budget = unresolved_budget+value/CAP
            else:
                strict_budget = strict_budget+value/CAP
            records.append({'prime_cells': indices, 'selector_cell': k,
                            'kind': 'full_state_bound' if vectors is None else 'strict_both_stages',
                            'range': value.enc()})
    full_g = [gv for _, _, gv in response_cells]
    zero_excluded = result.lo > 0 or result.hi < 0
    unresolved = [{'cell': k, 'reason': reason} for k, (_, reason) in enumerate(selector_cells) if reason]
    out = {
        'status': 'RIGOROUS_RANGE_ENCLOSURE_CONTAINS_ZERO' if not zero_excluded else 'UNVERIFIED_NONZERO_CANDIDATE',
        'target': "L426 exact I; L423 exact mixture; L419 ordered two-stage rule",
        'method': '10^-24 outward integer intervals; complete range integration',
        'implementation_contract': 'Correct Python integer, Fraction and isqrt execution; no floating proof decisions.',
        'cell_cap': CAP, 'cell_count': len(records), 'cell_mass': '1/32768',
        'prime_coordinates': [2, 3, 5], 'prime_partition': 'four equal subintervals of [0,pi]; exact cosine reflection',
        'selector_partition': '512 equal intervals of [0,2pi]',
        'pi': PI.enc(), 'coefficients': coefficients,
        'full_log_tail': tail.enc(), 'log_tail_residual_above_200': residual.enc(),
        'full_squared_modulus_tail_factor': tail_factor.enc(),
        'response_cells': [{'indices': ix, 'W': w.enc(), 'g': gv.enc()} for ix, w, gv in response_cells],
        'g_full_range': I(min(v.lo for v in full_g), max(v.hi for v in full_g), True).enc(),
        'selector_cells': [{'cell': k, 'reason': reason,
                            'P_times_u': None if vectors is None else
                            [[v.enc() for v in vector] for vector in vectors]}
                           for k, (vectors, reason) in enumerate(selector_cells)],
        'unresolved_selector_cells': unresolved, 'unresolved_selector_mass': str(F(len(unresolved), 512)),
        'strict_contribution': strict_budget.enc(), 'unresolved_contribution': unresolved_budget.enc(),
        'integral': result.enc(), 'zero_excluded': zero_excluded,
        'checks': {'complete_product_coverage': len(records) == CAP,
                   'positive_g_all_cells': all(gv.lo > 0 for _, _, gv in response_cells),
                   'valid_tail_log_bound': 0 <= tail.lo <= tail.hi < SCALE,
                   'source_checks_pass': True},
        'failures': [] if zero_excluded else ['Final enclosure contains zero; I value/sign/nonvanishing undecided.'],
        'cells': records,
    }
    path = directory/'bulk-haar-integral-enclosure-188.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Cell cap / actual:', CAP, len(records))
    print('Actual I enclosure:', result.enc(), 'Required: lower>0 or upper<0.')
    print('Full log-tail:', tail.enc(), 'Unresolved selector mass:', out['unresolved_selector_mass'])
    print('Strict / unresolved contributions:', strict_budget.enc(), unresolved_budget.enc())
    print('Failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()
