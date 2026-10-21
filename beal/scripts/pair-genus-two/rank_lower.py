"""One bounded exact divisor search and torsion-aware Kummer detector.

Standard library only. Coefficients are ascending. This is a lower
detector, never a Selmer/rank upper-bound or point-completeness algorithm.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, gcd, isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
F = [-308, -2288, 341, 3388, 1034, -704, -275]
checks = {}


def check(name, value):
    assert name not in checks
    checks[name] = bool(value)


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    r = [0] * max(0, len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            r[i+j] += u*v
    return trim(r)


def ev(a, x):
    r = 0
    for u in reversed(a):
        r = r*x+u
    return r


def divrem(a, b, p=None):
    a, b = trim(a), trim(b)
    q = [0]*max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        j = len(a)-len(b)
        v = (a[-1]*pow(b[-1], -1, p)) % p if p else Q(a[-1])/b[-1]
        q[j] = v
        for k, u in enumerate(b):
            a[j+k] -= v*u
            if p:
                a[j+k] %= p
        a = trim(a)
    return trim(q), a


def pgcd(a, b, p=None):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, divrem(a, b, p)[1]
    if not a:
        return []
    v = pow(a[-1], -1, p) if p else 1/Q(a[-1])
    return [(x*v) % p if p else x*v for x in a]


def power(a, n, g, p):
    r = [1]
    while n:
        if n & 1:
            r = divrem(mul(r, a), g, p)[1]
        a = divrem(mul(a, a), g, p)[1]
        n //= 2
    return r


def submod(a, b, p):
    return trim([v % p for v in add(a, [-x for x in b])])


def irreducibility(a, p):
    n = len(a)-1
    prime_divisors = [q for q in range(2, n+1)
                      if n % q == 0 and all(q % d for d in range(2, isqrt(q)+1))]
    x = divrem([0, 1], a, p)[1]
    residual = submod(power([0, 1], p**n, a, p), x, p)
    gs = [pgcd(a, submod(power([0, 1], p**(n//q), a, p), x, p), p)
          for q in prime_divisors]
    return {'frobenius_residual': residual, 'proper_degree_gcds': gs,
            'prime_divisors_of_degree': prime_divisors,
            'passed': not residual and all(h == [1] for h in gs)}


def factor(a, p):
    r, factors = a[:], []
    for x in range(p):
        if len(r) > 1 and ev(r, x) % p == 0:
            h = [(-x) % p, 1]
            r, rem = divrem(r, h, p)
            assert not rem
            factors.append(h)
    # With no linear factors, degree <=5: only a quadratic split remains.
    if len(r) >= 5:
        for b in range(p):
            for a0 in range(p):
                if len(r) < 5:
                    break
                h = [a0, b, 1]
                q, rem = divrem(r, h, p)
                if not rem:
                    factors.append(h)
                    r = q
    if len(r) > 1:
        factors.append(r)
    return factors


def encoded(v):
    if isinstance(v, Q):
        return [v.numerator, v.denominator]
    if isinstance(v, dict):
        return {k: encoded(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)):
        return [encoded(x) for x in v]
    return v


# Independent Taylor expansion; identity X^6 f(2+c/X)=c^2 g(X).
taylor = [sum(F[i]*comb(i, j)*2**(i-j) for i in range(j, 7))
          for j in range(7)]
c = taylor[1]
G = [taylor[6-i]*c**(4-i) for i in range(5)] + [1]
check('root_at_two', taylor[0] == 0)
check('c_equals_minus_36300', c == -36300)
check('model_coefficient_identity',
      all(c*c*G[i] == taylor[6-i]*c**(6-i) for i in range(6)))
check('monic_integral_quintic', len(G) == 6 and G[-1] == 1 and all(isinstance(v, int) for v in G))
check('odd_model_squarefree', pgcd(G, [i*G[i] for i in range(1, 6)]) == [1])

points, quadratic, columns = [], [], []
column_index = {}
rejections = {'branch_points': 0, 'quadratic_repeated_roots': 0,
              'quadratic_meets_branch': 0, 'odd_branch_support': 0}
point_tests = 0


def register(A, B, origin):
    A, B = trim(A), trim(B)
    rem = divrem(add(G, [-x for x in mul(B, B)]), A)[1]
    coprime = pgcd(A, G) == [1]
    check('transport_'+origin, not rem and len(B) < len(A) and A[-1] == 1)
    if not coprime:
        rejections['odd_branch_support'] += 1
        return None, rem
    key = tuple(A)
    if key not in column_index:
        column_index[key] = len(columns)
        columns.append({'id': len(columns), 'a': A, 'b': B,
                        'degree': len(A)-1, 'origin': origin,
                        'odd_remainder': rem, 'gcd_with_g': [1]})
    return column_index[key], rem


for n in range(1, 501):
    for m in range(-500, 501):
        if gcd(m, n) != 1:
            continue
        point_tests += 1
        h = sum(F[i]*m**i*n**(6-i) for i in range(7))
        if h < 0:
            continue
        w = isqrt(h)
        if w*w != h:
            continue
        T = Q(m, n)
        if w == 0:
            rejections['branch_points'] += 1
            points.append({'m': m, 'n': n, 'W_numerator': 0, 'branch': True})
            continue
        for ww in (w, -w):
            W = Q(ww, n**3)
            X, Y = Q(c)/(T-2), Q(c*c)*W/(T-2)**3
            check('point_inverse_'+str(len(points)), 2+Q(c)/X == T and Q(c)*Y/X**3 == W)
            A, B = [-X, Q(1)], [Y]
            idx, rem = register(A, B, 'P'+str(len(points)))
            points.append({'m': m, 'n': n, 'W_numerator': ww,
                           'branch': False, 'odd_a': A, 'odd_b': B,
                           'odd_remainder': rem, 'column': idx})

quadratic_tests = 0
quadratic_pairs = 0
for a1 in range(-25, 26):
    for a0 in range(-25, 26):
        quadratic_pairs += 1
        a = [a0, a1, 1]
        if a1*a1 == 4*a0:
            rejections['quadratic_repeated_roots'] += 1
            continue
        # Integer remainder of the sextic, no rational arithmetic needed.
        r0, r1 = 0, 0
        for v in reversed(F):
            r0, r1 = v-a0*r1, r0-a1*r1
        if (r1 == 0 and r0 == 0) or (r1 != 0 and r0*r0-a1*r0*r1+a0*r1*r1 == 0):
            rejections['quadratic_meets_branch'] += 1
            continue
        for b1 in range(-500, 501):
            quadratic_tests += 1
            b0s = []
            if b1 == 0:
                if r1 == 0 and r0 >= 0 and isqrt(r0)**2 == r0:
                    b0s = sorted(set([Q(isqrt(r0)), Q(-isqrt(r0))]))
            else:
                num, den = r1+a1*b1*b1, 2*b1
                if num*num-(a0*b1*b1+r0)*den*den == 0:
                    b0s = [Q(num, den)]
            for b0 in b0s:
                b = [b0, Q(b1)]
                original_rem = divrem(add(F, [-x for x in mul(b, b)]), a)[1]
                aa2 = 4+2*a1+a0
                assert aa2 != 0
                A = [Q(c*c, aa2), Q(c*(4+a1), aa2), Q(1)]
                B = divrem([0, 0, Q(b1), (2*b1+b0)/c], A)[1]
                idx, rem = register(A, B, 'D'+str(len(quadratic)))
                check('original_divisor_'+str(len(quadratic)), not original_rem)
                quadratic.append({'a': a, 'b': b, 'original_remainder': original_rem,
                                  'odd_a': A, 'odd_b': B, 'odd_remainder': rem,
                                  'column': idx})

prime_records, detectors, excluded_coordinates = [], [], []
primes = [p for p in range(3, 102, 2) if all(p % d for d in range(2, isqrt(p)+1))]
for p in primes:
    gm = [v % p for v in G]
    if pgcd(gm, [i*gm[i] % p for i in range(1, 6)], p) != [1]:
        prime_records.append({'p': p, 'good': False, 'reason': 'not squarefree'})
        continue
    fs = factor(gm, p)
    product = [1]
    for h in fs:
        product = [v % p for v in mul(product, h)]
    irreds = [irreducibility(h, p) for h in fs]
    check('factorization_'+str(p), product == gm and all(v['passed'] for v in irreds))
    prime_records.append({'p': p, 'good': True, 'g_mod_p': gm, 'factors': fs,
                          'irreducibility': irreds, 'rational_torsion_allowance': len(fs)-1})
    for root in range(p):
        if ev(gm, root) % p:
            continue
        vals, bits, problems = [], [], []
        for col in columns:
            if any(v.denominator % p == 0 for v in col['a']):
                problems.append({'column': col['id'], 'reason': 'denominator'})
                continue
            aa = [v.numerator*pow(v.denominator, -1, p) % p for v in col['a']]
            value = ev(aa, root)*(-1)**col['degree'] % p
            if value == 0:
                problems.append({'column': col['id'], 'reason': 'zero evaluation'})
                continue
            character = pow(value, (p-1)//2, p)
            assert character in (1, p-1)
            vals.append(value)
            bits.append(int(character != 1))
        if problems:
            excluded_coordinates.append({'p': p, 'root': root, 'problems': problems})
        else:
            detectors.append({'p': p, 'root': root, 'values': vals, 'bits': bits,
                              'derivative': ev([i*gm[i] for i in range(1, 6)], root) % p})

# Exact row operations on common coordinates, preserving a replayable trace.
matrix = [v['bits'][:] for v in detectors]
rref = [v[:] for v in matrix]
operations, pivots = [], []
rank = 0
for j in range(len(columns)):
    pivot = next((i for i in range(rank, len(rref)) if rref[i][j]), None)
    if pivot is None:
        continue
    if pivot != rank:
        rref[rank], rref[pivot] = rref[pivot], rref[rank]
        operations.append(['swap', rank, pivot])
    for i in range(len(rref)):
        if i != rank and rref[i][j]:
            rref[i] = [x ^ y for x, y in zip(rref[i], rref[rank])]
            operations.append(['xor', i, rank])
    pivots.append([rank, j])
    rank += 1
check('rref', all(row[j] == int(i == k) for k, j in pivots for i, row in enumerate(rref)))
t = min(v['rational_torsion_allowance'] for v in prime_records if v['good'])
torsion_witness = next(v for v in prime_records if v['good'] and v['rational_torsion_allowance'] == t)
failures = [name for name, ok in checks.items() if not ok]
result = {'input': 'L110 exact sextic', 'f': F,
          'model': {'c': c, 'taylor_at_two': taylor, 'g': G,
                    'forward': 'X=c/(T-2),Y=c^2*W/(T-2)^3',
                    'inverse': 'T=2+c/X,W=c*Y/X^3'},
          'search': {'point_height_cap': 500, 'quadratic_coefficient_cap': 25,
                     'b1_cap': 500, 'b0_domain': 'rational; determined exactly, no size cap',
                     'point_tests': point_tests, 'quadratic_pairs': quadratic_pairs,
                     'quadratic_b1_tests': quadratic_tests, 'completed': True,
                     'rejections': rejections},
          'points': points, 'quadratic_divisors': quadratic, 'columns': columns,
          'finite_factorizations': prime_records, 'torsion_upper_witness': torsion_witness,
          'detectors': detectors,
          'excluded_coordinates': excluded_coordinates,
          'matrix': matrix, 'row_operations': operations, 'rref': rref, 'pivots': pivots,
          'summary': {'points_including_signs_and_branches': len(points),
                      'quadratic_divisors_including_signs': len(quadratic),
                      'columns': len(columns), 'common_coordinates': len(detectors),
                      'd': rank, 't_upper': t, 'd_minus_t': rank-t,
                      'required': 2, 'threshold_met': rank-t >= 2,
                      'checks': len(checks), 'failures': failures}, 'checks': checks}
out = HERE/'rank-lower-certificate.json'
out.write_text(json.dumps(encoded(result), indent=2)+'\n')
print(json.dumps(result['summary'], sort_keys=True))
print('Search complete:', point_tests, 'reduced rational tests;', quadratic_pairs,
      'quadratic pairs;', quadratic_tests, 'slope tests')
print('Rejections:', json.dumps(rejections, sort_keys=True))
print('Full certificate:', out.relative_to(HERE.parent.parent))
print('SHA256:', sha256(out.read_bytes()).hexdigest())
if failures:
    raise SystemExit(1)
