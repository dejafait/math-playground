#!/usr/bin/env python3
"""Independent integer-dyadic replay of ALL step414 integration evidence.

No imports of notebook mathematical code; no Decimal arithmetic. Every
integer endpoint represents a multiple of 2^-4096. Complete intermediate
replay intervals and all comparisons are saved, not printed.
"""
from fractions import Fraction as Q
from math import comb, factorial, isqrt
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[2]
BITS = 4096
S = 1 << BITS


def ceildiv(a, b):
    return -((-a)//b)


class R:
    def __init__(self, x=0, hi=None, raw=False):
        if raw:
            self.lo, self.hi = x, hi
        elif isinstance(x, R):
            self.lo, self.hi = x.lo, x.hi
        else:
            x = Q(x)
            self.lo = (x.numerator*S)//x.denominator
            self.hi = ceildiv(x.numerator*S, x.denominator)
        assert self.lo <= self.hi

    def __add__(self, y):
        y = R(y)
        return R(self.lo+y.lo, self.hi+y.hi, raw=True)

    def __neg__(self):
        return R(-self.hi, -self.lo, raw=True)

    def __sub__(self, y):
        return self+-R(y)

    def __mul__(self, y):
        y = R(y)
        v = [x*z for x in (self.lo, self.hi) for z in (y.lo, y.hi)]
        return R(min(v)//S, ceildiv(max(v), S), raw=True)

    def __truediv__(self, y):
        y = R(y)
        assert not y.lo <= 0 <= y.hi, 'zero-containing real divisor'
        return self*R((S*S)//y.hi, ceildiv(S*S, y.lo), raw=True)

    def half(self):
        return R(self.lo//2, ceildiv(self.hi, 2), raw=True)

    def absmax(self):
        return max(abs(self.lo), abs(self.hi))

    def dump(self):
        return [self.lo, self.hi]


class C:
    def __init__(self, re=0, im=0):
        if isinstance(re, C):
            self.re, self.im = re.re, re.im
        else:
            self.re, self.im = R(re), R(im)

    def __add__(self, y):
        y = C(y)
        return C(self.re+y.re, self.im+y.im)

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, y):
        return self+-C(y)

    def __mul__(self, y):
        y = C(y)
        return C(self.re*y.re-self.im*y.im, self.re*y.im+self.im*y.re)

    def __truediv__(self, y):
        y = C(y)
        norm = y.re*y.re+y.im*y.im
        assert norm.lo > 0, 'complex denominator not separated'
        return C((self.re*y.re+self.im*y.im)/norm,
                 (self.im*y.re-self.re*y.im)/norm)

    def conj(self):
        return C(self.re, -self.im)

    def dump(self):
        return {'re': self.re.dump(), 'im': self.im.dump()}


def exp(z):
    z = C(z)
    count = 0
    while z.re.absmax()+z.im.absmax() > S//16:
        z = C(z.re.half(), z.im.half())
        count += 1
    term = total = C(1)
    for j in range(1, 513):
        term = term*z/j
        total = total+term
    # |z| <= 1/16. Geometric majorant for the tail after degree512.
    err = ceildiv(2*S, 16**513*factorial(513))
    total = total+C(R(-err, err, raw=True), R(-err, err, raw=True))
    for _ in range(count):
        total = total*total
    return total


# Exact Gaussian-rational arithmetic used for the primitive coefficients.
def qadd(x, y):
    return (x[0]+y[0], x[1]+y[1])


def qmul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def qscale(x, s):
    return (x[0]*s, x[1]*s)


def qdiv(x, y):
    den = y[0]**2+y[1]**2
    assert den > 0
    return ((x[0]*y[0]+x[1]*y[1])/den,
            (x[1]*y[0]-x[0]*y[1])/den)


def evaluate_exact(p, x):
    v = (Q(0), Q(0))
    for coeff in reversed(p):
        v = qadd(qscale(v, x), coeff)
    return C(*v)


def terms(n):
    p = [Q((-1)**j*comb(n+3, n+1-j), factorial(j)*(n+1))
         for j in range(n+2)]
    p[0] -= Q(1, n+1)
    result, lower = [], C(0)
    for a in ((Q(-1, 4), Q(1)), (Q(-1), Q(1))):
        q = [(Q(0), Q(0))]*(n+3)
        for j in reversed(range(n+2)):
            q[j] = qdiv(qadd((p[j], Q(0)), qscale(q[j+1], -(j+1))), a)
        for j in range(n+2):
            assert qadd(qmul(a, q[j]), qscale(q[j+1], j+1)) == (p[j], 0)
        q.pop()
        for endpoint, sign in ((n, 1), (n+2, -1)):
            result.append({'alpha': (a[0]*endpoint-Q(n, 4), a[1]*endpoint),
                           'coeff': [C(*qscale(v, sign*endpoint**j))
                                     for j, v in enumerate(q)]})
        upper = exp(C(a[0]*(n+2), a[1]*(n+2)))*evaluate_exact(q, n+2)
        bottom = exp(C(a[0]*n, a[1]*n))*evaluate_exact(q, n)
        lower = lower+upper-bottom
    result.append({'alpha': (-Q(n, 4), Q(0)), 'coeff': [lower]})
    return result


def integrate_product(x, y):
    alpha = (x['alpha'][0]+y['alpha'][0], -x['alpha'][1]+y['alpha'][1])
    assert alpha[0] < 0
    poly = [C(0) for _ in range(len(x['coeff'])+len(y['coeff'])-1)]
    for j, u in enumerate(x['coeff']):
        for k, v in enumerate(y['coeff']):
            poly[j+k] = poly[j+k]+u.conj()*v
    left, right = Q(7, 4), Q(9, 4)
    ea = exp(C(alpha[0]*left, alpha[1]*left))
    eb = exp(C(alpha[0]*right, alpha[1]*right))
    a = C(*alpha)
    moments = [(eb-ea)/a]
    for j in range(1, len(poly)):
        moments.append((eb*right**j-ea*left**j-moments[-1]*j)/a)
    total = C(0)
    for u, v in zip(poly, moments):
        total = total+u*v
    return alpha, poly, moments, total


def audit(n):
    path = ROOT/f'scripts/target-radau/finite-penalty-screen-{n}-414.json'
    source = json.loads(path.read_text())
    failures, comparisons = [], []

    def check(condition, label):
        comparisons.append({'field': label, 'pass': bool(condition)})
        if not condition:
            failures.append(label)

    def real_contains(saved, computed, label):
        lo, hi = map(Q, saved)
        check(lo <= Q(computed.lo, S) <= Q(computed.hi, S) <= hi, label)

    def complex_contains(saved, computed, label):
        real_contains(saved['re'], computed.re, label+'/re')
        real_contains(saved['im'], computed.im, label+'/im')

    check(source['n'] == n and source['status'] == 'COMPLETED', 'header')
    check(source['interval'] == ['7/4', '9/4'] and source['target'] == ['1', '1/8'], 'domain')
    ts = terms(n)
    check(len(source['target_terms']) == 5, 'five_terms')
    for j, t in enumerate(ts):
        saved = source['target_terms'][j]
        check(tuple(map(Q, saved['alpha'])) == t['alpha'], f'terms/{j}/alpha')
        check(len(saved['coefficients']) == len(t['coeff']), f'terms/{j}/length')
        for k, v in enumerate(t['coeff']):
            complex_contains(saved['coefficients'][k], v, f'terms/{j}/coeff/{k}')

    output = {'n': n, 'input': str(path.relative_to(ROOT)),
              'input_sha256': sha256(path.read_bytes()).hexdigest(),
              'denominator_bits': BITS,
              'target_terms': [{'alpha': list(map(str, t['alpha'])),
                               'coefficients': [v.dump() for v in t['coeff']]} for t in ts],
              'products': []}
    pairs = [(i, j) for i in range(5) for j in range(i, 5)]
    check([(p['i'], p['j']) for p in source['products']] == pairs, 'fifteen_products')
    d = R(0)
    for pos, (i, j) in enumerate(pairs):
        alpha, poly, ms, val = integrate_product(ts[i], ts[j])
        saved = source['products'][pos]
        mult = 1 if i == j else 2
        prefix = f'products/{i},{j}'
        check(tuple(map(Q, saved['alpha'])) == alpha and saved['case'] == 'nonzero'
              and saved['multiplicity'] == mult and alpha[0] <= -Q(n, 2), prefix+'/case')
        check(len(saved['product_coefficients']) == len(poly)
              and len(saved['moments']) == len(ms), prefix+'/lengths')
        for k, v in enumerate(poly):
            complex_contains(saved['product_coefficients'][k], v, prefix+f'/coeff/{k}')
        for k, v in enumerate(ms):
            complex_contains(saved['moments'][k], v, prefix+f'/moments/{k}')
        complex_contains(saved['integral'], val, prefix+'/integral')
        if i == j:
            check(val.im.lo <= 0 <= val.im.hi, prefix+'/diagonal_real')
        d = d+val.re*mult
        output['products'].append({'i': i, 'j': j, 'alpha': list(map(str, alpha)),
                                  'product_coefficients': [v.dump() for v in poly],
                                  'moments': [v.dump() for v in ms], 'integral': val.dump()})
    real_contains(source['d'], d, 'd')
    root = isqrt(n*S*S)
    check(root*root <= n*S*S < (root+1)**2, 'sqrt_integer_certificate')
    sqrt_n = R(root, root if root*root == n*S*S else root+1, raw=True)
    lam = exp(C(Q(-n, 16))).re
    budget = exp(C(sqrt_n)).re
    # Independent direct exponent instead of multiplying three saved intervals.
    penalty = exp(C(sqrt_n*2+Q(-n, 16))).re
    for field, val in [('lambda', lam), ('B', budget), ('penalty', penalty)]:
        real_contains(source[field], val, field)
    screen = d-penalty
    real_contains(source['screen_d_minus_penalty'], screen, 'screen')
    bound = 162754 if n == 64 else 2252197
    check(Q(screen.hi, S) <= Q(source['F_upper']) < -bound, 'strict_F_upper')
    check(0 <= d.lo and Q(d.hi, S) < (Q(1323, 10**9) if n == 64 else Q(1683, 10**10)), 'safe_d_bound')
    check(Q(penalty.lo, S) > bound, 'safe_penalty_bound')
    for field in ['d', 'lambda', 'B']:
        lo, hi = map(Q, source[field])
        check(hi-lo < Q(1, 2**256), field+'/saved_width')
    lo, hi = map(Q, source['screen_d_minus_penalty'])
    check(hi-lo < Q(1, 2**60), 'screen/saved_width')
    check(source['lanczos_steps'] == 0 and source['not_computed'] ==
          ['G', 'h', 'Gauss endpoint', 'Radau endpoint', 'inverse form'], 'zero_Lanczos')
    check(not source['failures'] and all(source['checks'].values()), 'source_checks')
    output.update({'d': d.dump(), 'sqrt_n': sqrt_n.dump(), 'lambda': lam.dump(),
                   'B': budget.dump(), 'penalty': penalty.dump(), 'screen': screen.dump(),
                   'comparisons': comparisons, 'failures': failures,
                   'comparison_count': len(comparisons),
                   'verdict': 'ACCEPT' if not failures else 'FAIL'})
    out = ROOT/f'scripts/target-radau/audit-penalty-screen-{n}-416.json'
    out.write_text(json.dumps(output))
    # Deliberately coarse printed bounds, checked exactly above.
    print(f'n={n}: {len(comparisons)} complete comparisons; verdict={output["verdict"]}; '
          f'F < {-bound}; saved entry widths < 2^-256, screen width < 2^-60; '
          f'failures={failures}; certificate={out.relative_to(ROOT)}', flush=True)
    return {'n': n, 'comparison_count': len(comparisons), 'failures': failures,
            'verdict': output['verdict'], 'certificate': str(out.relative_to(ROOT)),
            'certificate_sha256': sha256(out.read_bytes()).hexdigest()}


if __name__ == '__main__':
    results = [audit(n) for n in (64, 128)]
    out = ROOT/'scripts/target-radau/audit-penalty-screen-416.json'
    out.write_text(json.dumps({'dyadic_bits': BITS, 'results': results,
                               'failures': [r for r in results if r['failures']]}))
    print('summary certificate:', out.relative_to(ROOT))
    if any(r['failures'] for r in results):
        raise SystemExit(1)
