#!/usr/bin/env python3
"""Exact bounded residue/normalized-branch certificate; no numeric Q7 roots."""
from itertools import product
from pathlib import Path
import json

P = 7
OUT = Path(__file__).with_name('joint-fiber-certificate.json')


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b, modulus=None):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim([x % modulus for x in c] if modulus else c)


def divrem(a, b):
    a, b = trim([x % P for x in a]), trim([x % P for x in b])
    q = [0] * max(1, len(a)-len(b)+1)
    inv = pow(b[-1], -1, P)
    while a != [0] and len(a) >= len(b):
        d, z = len(a)-len(b), a[-1]*inv % P
        q[d] = z
        for j, x in enumerate(b):
            a[d+j] = (a[d+j]-z*x) % P
        a = trim(a)
    return trim(q), a


def monic(a):
    return trim([x*pow(a[-1], -1, P) % P for x in a])


def gcd(a, b):
    while b != [0]:
        a, b = b, divrem(a, b)[1]
    return monic(a)


def sub(a, b):
    return trim([((a[i] if i < len(a) else 0) -
                  (b[i] if i < len(b) else 0)) % P
                 for i in range(max(len(a), len(b)))])


def powmod(a, n, f):
    ans = [1]
    while n:
        if n & 1:
            ans = divrem(mul(ans, a, P), f)[1]
        a = divrem(mul(a, a, P), f)[1]
        n //= 2
    return ans


def factor(a):
    a, factors = monic(a), []
    for d in range(1, (len(a)-1)//2+1):
        for c in product(range(P), repeat=d):
            b, e = list(c)+[1], 0
            while len(a) >= len(b) and divrem(a, b)[1] == [0]:
                a = divrem(a, b)[0]
                e += 1
            if e:
                factors.append((b, e))
            if len(a)-1 < 2*d:
                break
        if len(a)-1 < 2*d:
            break
    if a != [1]:
        factors.append((a, 1))
    return factors


def irreducible_certificate(f):
    n = len(f)-1
    prime_divisors = [q for q in range(2, n+1)
                      if n % q == 0 and all(q % r for r in range(2, q))]
    final = sub(powmod([0, 1], P**n, f), divrem([0, 1], f)[1])
    tests = [{'q': q, 'gcd': gcd(f, sub(powmod([0, 1], P**(n//q), f), [0, 1]))}
             for q in prime_divisors]
    return {'degree': n, 'frobenius_final_remainder': final,
            'proper_subdegree_gcds': tests,
            'passes': final == [0] and all(t['gcd'] == [1] for t in tests)}


def evaluate(a, x):
    v = 0
    for z in reversed(a):
        v = v*x+z
    return v


def valuation(n):
    assert n != 0
    v = 0
    while n % P == 0:
        n //= P
        v += 1
    return v


def derivative(a):
    return [i*a[i] for i in range(1, len(a))]


def lift(a, seed, precision=3):
    x, modulus, steps = seed, P, []
    assert evaluate(a, x) % P == 0 and evaluate(derivative(a), x) % P != 0
    for k in range(2, precision+1):
        choices = [x+j*modulus for j in range(P)
                   if evaluate(a, x+j*modulus) % (P*modulus) == 0]
        assert len(choices) == 1
        x, modulus = choices[0], P*modulus
        steps.append({'precision': k, 'root': x, 'modulus': modulus,
                      'error_valuation': valuation(evaluate(a, x)),
                      'derivative_residue': evaluate(derivative(a), x) % P})
    return {'seed': seed, 'seed_error': evaluate(a, seed),
            'seed_error_valuation': valuation(evaluate(a, seed)),
            'seed_derivative_residue': evaluate(derivative(a), seed) % P,
            'steps': steps, 'root_mod_343': x}


phi = [1]
for _ in range(5):
    phi = mul(phi, [1, 1, 3])
phi = mul(phi, [1, -5])
q4 = [1]
for _ in range(4):
    q4 = mul(q4, [1, 1, 3])
derivative_expected = mul([0, 0, -165], q4)
checks = {'degree_eleven': len(phi)-1 == 11,
          'derivative_identity': derivative(phi) == derivative_expected}
regular = []
for s in range(2, 7):
    f = phi[:]
    f[0] -= s
    factors = factor(f)
    recon = [phi[-1] % P]
    stored = []
    for a, e in factors:
        cert = irreducible_certificate(a)
        checks[f'regular_{s}_factor_{len(stored)}_irreducible'] = cert['passes']
        for _ in range(e):
            recon = mul(recon, a, P)
        stored.append({'coefficients_low_first': a, 'multiplicity': e,
                       'irreducibility': cert})
    checks[f'regular_{s}_reconstruction'] = recon == [x % P for x in f]
    checks[f'regular_{s}_squarefree'] = gcd(f, derivative(f)) == [1]
    tuples = [[a, b, c] for a, b, c in product(range(1, P), repeat=3)
              if (a**3+b**5-c**11) % P == 0 and
              b**5*pow(c**11, -1, P) % P == s]
    roots = [t for t in range(P) if evaluate(f, t) % P == 0]
    checks[f'regular_{s}_fewer_than_three_roots'] = len(roots) < 3
    regular.append({'scalar': s, 'leading_unit': phi[-1] % P,
                    'complete_factors': stored, 'rational_residue_roots': roots,
                    'all_unit_primitive_residue_tuples': tuples})

# One branch only: A=7, C=1, s=-342; B^5=-342 and B=1 mod7.
s = 1-P**3
g = [0] * len(phi)
g[0] = -1
for i in range(1, len(phi)):
    numerator = -phi[i]*P**i
    assert numerator % P**3 == 0
    g[i] = numerator//P**3
g = trim(g)
checks['normalized_reduction'] = trim([x % P for x in g]) == [6, 0, 0, 6]
roots = [u for u in range(P) if evaluate(g, u) % P == 0]
checks['normalized_three_simple_roots'] = roots == [3, 5, 6] and all(
    evaluate(derivative(g), u) % P != 0 for u in roots)
checks['scaled_identity_all_coefficients'] = all(
    P**3*g[i] == (1-phi[0]-P**3 if i == 0 else -phi[i]*P**i)
    for i in range(len(g)))
b_poly = [-s, 0, 0, 0, 0, 1]
b_error = evaluate(b_poly, 1)
checks['common_B_strict_hensel'] = valuation(b_error) == 3 and evaluate(derivative(b_poly), 1) % P == 5
quadratic = [3, 0, 1]
checks['quadratic_split_simple_roots'] = all(
    evaluate(quadratic, u) % P == 0 and evaluate(derivative(quadratic), u) % P != 0
    for u in [2, 5])
# Critical points are t=0 and q(t)=0; their phi values are 1 and 0.
checks['whole_fiber_etale'] = s != 0 and s != 1 and phi[0] == 1
data = {'coefficient_order': 'low first', 'prime': P, 'phi': phi,
        'regular': regular,
        'quadratic': {'polynomial': quadratic, 'lifts': [lift(quadratic, u) for u in [2, 5]]},
        'branch': {'A': 7, 'C': 1, 'scalar': s, 'one_minus_scalar': P**3,
                   'B_polynomial': b_poly, 'B_seed': 1, 'B_error': b_error,
                   'B_error_valuation': valuation(b_error), 'B_derivative_residue': 5,
                   'B_lift': lift(b_poly, 1),
                   'normalized_g': g, 'g_reduction': trim([x % P for x in g]),
                   'roots': [lift(g, u) for u in roots],
                   'required_rational_factors': 3, 'certified_rational_factors': len(roots),
                   'complement_degree': 8, 'max_normalized_precision': P**3},
        'checks': checks, 'failures': [k for k, v in checks.items() if not v]}
OUT.write_text(json.dumps(data, indent=2)+'\n')
print('regular factor degrees:', [[(len(f['coefficients_low_first'])-1, f['multiplicity'])
                                  for f in r['complete_factors']] for r in regular])
print('branch scalar:', s, '; rational factors actual/required:', len(roots), '/', 3,
      '; complementary degree:', 8)
print('normalized precision actual/cap:', P**3, '/', P**3)
print('checks:', len(checks), '; failures:', data['failures'])
print('certificate:', OUT)
assert not data['failures']
