"""Additional L101 manuscript/record audit; no new estimate or search."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json

BASE = Path(__file__).parent
d = json.loads((BASE / 'order-four-pole-results.json').read_text())
v = json.loads((BASE / 'order-four-pole-verification.json').read_text())
checks = []


def check(name, ok):
    checks.append({'name': name, 'passed': bool(ok)})


def value(x):
    return F(x['numerator'], x['denominator'])


# Sparse polynomials over Q in u,v,w,u',v',w'. These identities then
# reduce in characteristic 65537 since every denominator is invertible.
zero = (0,) * 6


def var(i):
    e = list(zero)
    e[i] = 1
    return {tuple(e): F(1)}


def add(*terms):
    out = {}
    for p in terms:
        for e, a in p.items():
            out[e] = out.get(e, F(0)) + a
    return {e: a for e, a in out.items() if a}


def scale(p, a):
    return {e: a*b for e, b in p.items() if a*b}


def mul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(x+y for x, y in zip(e, f))
            out[g] = out.get(g, F(0)) + a*b
    return {e: a for e, a in out.items() if a}


def log(p):
    u, w2, w3 = p
    return (u, add(w2, scale(mul(u, u), F(-1, 2))),
            add(w3, scale(mul(u, w2), -1),
                scale(mul(mul(u, u), u), F(1, 3))))


def exp(p):
    a, b, c = p
    return (a, add(b, scale(mul(a, a), F(1, 2))),
            add(c, mul(a, b), scale(mul(mul(a, a), a), F(1, 6))))


u, w2, w3, up, w2p, w3p = map(var, range(6))
p, q = (u, w2, w3), (up, w2p, w3p)
pq = (add(u, up), add(w2, w2p, mul(u, up)),
      add(w3, w3p, mul(u, w2p), mul(w2, up)))
identities = {}
for name, lhs, rhs in (
        ('log multiplication', log(pq), tuple(add(a, b) for a, b in zip(log(p), log(q)))),
        ('exp after log', exp(log(p)), p),
        ('log after exp', log(exp(p)), p)):
    for i, (a, b) in enumerate(zip(lhs, rhs)):
        residual = add(a, scale(b, -1))
        key = f'{name} coordinate {i+1}'
        identities[key] = {str(e): str(c) for e, c in residual.items()}
        check(key, not residual)

Q, B, s = 65537, 769, 67
check('prime certificate', pow(3, 32768, Q) == Q-1 and Q == 2**16+1)
g = pow(3, 64, Q)
check('subgroup and minus one', g == 19139 and pow(g, 1024, Q) == 1
      and pow(g, 512, Q) == Q-1 and (Q-1)//1024 == 64)
for j in range(1, s+1):
    check(f'powered parameter nonvanishing {j}', pow(j, -1, Q)*j % Q == 1)
check('log denominators', all(Q % j for j in (2, 3, 6)))
C, V = comb(1024, 67), comb(835, 67)
U = F(C, Q**3) + (1-F(1, Q**3))*B*V
T = F(Q**28, 2**128)
manuscript_numerator = int(
    '221134051719995758916214425733433775693720201213764938260104095157802500'
    '5970261168784407494466928772074809150947486720')
check('manuscript cap', U == F(manuscript_numerator, 281487861809153)
      == value(d['exact']['upper_cap']))
check('principal and error', value(d['exact']['principal']) == F(C, Q**3)
      and value(d['exact']['error']) == U-F(C, Q**3))
check('all count parameters', d['parameters'] == {
    'Q': Q, 'n': 1024, 'agreement': 67, 'B': B,
    'group_order': (Q-1)*Q**3, 'nonconstant_characters': (Q-1)*(Q**3-1)})
check('all cycle coefficients', len(d['exact']['cycle_coefficients']) == 68
      and all(value(a) == comb(B+j-1, j)
              for j, a in enumerate(d['exact']['cycle_coefficients'])))
lower = 2**128*U.numerator-3676307*Q**28*U.denominator
upper = 3676308*Q**28*U.denominator-2**128*U.numerator
check('strict manuscript cross products', lower > 0 and upper > 0)
check('threshold and ratio', value(d['exact']['threshold']) == T
      and value(d['exact']['cap_to_threshold']) == U/T
      and d['exact']['ratio_integer_lower'] == 3676307)
check('failure margin', d['exact']['failure_margin']
      == U.numerator*T.denominator-T.numerator*U.denominator > 0)

H = tuple(sorted(pow(9, i, 17) for i in range(8)))
small = d['small']
check('small parameters', small['q'] == 17 and small['k'] == 2
      and small['agreement'] == 5 and tuple(small['H']) == H)
categories = Counter()
fiber_counts = Counter()
for i, rec in enumerate(small['pairs']):
    S, r = tuple(rec['S']), rec['r']
    category = 'repeated' if r in S else 'extra' if r in H else 'outside'
    categories[category] += 1
    fiber_counts[tuple(rec['label'])] += 1
    check(f'branch metadata {i}', rec['category'] == category)
    constant = (-1)**5
    for x in S:
        constant = constant*x % 17
    check(f'descent sign {i}', -rec['label'][0]*pow(constant, -1, 17) % 17 == r)
    expected_roots = set(S) | ({r} if r in H else set())
    check(f'root branch {i}', set(rec['support']) == expected_roots
          and len(rec['support']) == (6 if category == 'extra' else 5))
check('complete branch counts', dict(categories) == small['categories']
      == {'repeated': 280, 'outside': 448, 'extra': 168}
      and small['pair_count'] == len(small['pairs']) == 896)
check('center counts and no duplicates',
      small['occupied_centers'] == len(fiber_counts) == 756
      and len(small['lists']) == len({tuple(r['label']) for r in small['lists']}) == 757)
for i, rec in enumerate(small['lists']):
    fs = [tuple(a['f']) for a in rec['list']]
    check(f'no duplicate saved messages {i}', len(fs) == len(set(fs)))
    check(f'incidence reconstruction {i}',
          sum(a['multiplicity'] for a in rec['list']) == rec['incidences']
          == fiber_counts[tuple(rec['label'])]
          and all(a['multiplicity'] == comb(len(a['support']), 5)
                  for a in rec['list']))
check('all six-root sets represented',
      sum(r['six_subsets'] for r in small['lists']) == comb(8, 6))
for name, data, expected in [('constructor', d, 4143), ('reconstruction', v, 2488)]:
    check(f'complete {name} checks',
          data['check_count'] == len(data['checks']) == expected
          and all(x['passed'] is True for x in data['checks']) and not data['failures'])

out = BASE / 'order-four-pole-critical-audit.json'
failures = [x['name'] for x in checks if not x['passed']]
out.write_text(json.dumps({
    'scope': 'L101 only; symbolic proof is recorded in the canonical lemma',
    'symbolic_identity_residuals': identities,
    'strict_lower_cross_product': lower, 'strict_upper_cross_product': upper,
    'ratio_actual_interval': [3676307, 3676308], 'ratio_required': '<=1',
    'checks': checks, 'check_count': len(checks), 'failures': failures,
}, indent=2)+'\n')
print(f'additional audit checks={len(checks)} failures={len(failures)}; certificate: {out}')
print('actual allowance/T in (3676307,3676308); required <=1; estimate remains parked')
if failures:
    print(f'failures={failures}')
    raise SystemExit(1)
