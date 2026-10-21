"""Independent reconstruction of the saved one-shot certificate."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial, prod
from pathlib import Path
import json

BASE = Path(__file__).parent
data = json.loads((BASE/'order-four-pole-results.json').read_text())
checks = []


def check(name, ok):
    checks.append({'name': name, 'passed': bool(ok)})


def value(x):
    return Fraction(x['numerator'], x['denominator'])


def choose(n, k):
    return prod(range(n-k+1, n+1))//factorial(k)


Q, n, s, B = 65537, 1024, 67, 769
principal = Fraction(choose(n, s), Q**3)
# Unsigned Stirling recurrence counts permutations by their cycle count.
stirling = [1]
for k in range(1, s+1):
    new = [0]*(k+1)
    for j in range(1, k+1):
        new[j] = stirling[j-1]+((k-1)*stirling[j] if j < len(stirling) else 0)
    stirling = new
    coefficient = Fraction(sum(a*B**j for j, a in enumerate(stirling)), factorial(k))
    check(f'unsigned permutation-cycle reconstruction {k}',
          coefficient == value(data['exact']['cycle_coefficients'][k]))
V = coefficient
U = principal+(1-Fraction(1, Q**3))*B*V
T = Fraction(Q**28, 2**128)
check('reconstruct full cap', U == value(data['exact']['upper_cap']))
check('reconstruct principal', principal == value(data['exact']['principal']))
check('reconstruct full error', U-principal == value(data['exact']['error']))
check('reconstruct threshold', T == value(data['exact']['threshold']))
check('reconstruct exact ratio', U/T == value(data['exact']['cap_to_threshold']))
check('strict fixed integer bracket', 3676307*T < U < 3676308*T)
check('positive full failure margin',
      data['exact']['failure_margin'] == U.numerator*T.denominator-T.numerator*U.denominator > 0)

q = 17
H = tuple(sorted(pow(9, j, q) for j in range(8)))
check('full small subgroup', H == tuple(data['small']['H']) and len(set(H)) == 8)


def sym_poly(roots):
    # Monic polynomial coefficients from elementary symmetric sums.
    d = len(roots)
    return tuple(((-1)**(d-i)*sum(prod(J) for J in combinations(roots, d-i))) % q
                 for i in range(d+1))


expected_pairs = set(product(combinations(H, 5), range(1, q)))
recorded_pairs = {(tuple(r['S']), r['r']) for r in data['small']['pairs']}
check('complete pair universe without repetitions',
      recorded_pairs == expected_pairs and len(data['small']['pairs']) == len(expected_pairs))
fibers = defaultdict(Counter)
for i, rec in enumerate(data['small']['pairs']):
    S, r = tuple(rec['S']), rec['r']
    G = sym_poly(S+(r,))
    f = (-G[4] % q, -G[5] % q)
    support = tuple(x for x in H if prod(x-t for t in S+(r,)) % q == 0)
    check(f'full elementary-symmetric pair {i}',
          tuple(rec['G']) == G and tuple(rec['label']) == G[:4]
          and tuple(rec['f']) == f and tuple(rec['support']) == support)
    fibers[G[:4]][f] += 1
N6 = Counter(sym_poly(J)[:4] for J in combinations(H, 6))
saved_lists = {tuple(r['label']): r for r in data['small']['lists']}
check('complete saved center coverage', set(saved_lists) == set(fibers) | {tuple(data['small']['empty_center'])})
for label, rec in saved_lists.items():
    actual = {}
    for a, b in product(range(q), repeat=2):
        G = (*label, -a % q, -b % q, 1)
        support = []
        for x in H:
            y = 0
            for coefficient in reversed(G):
                y = (y*x+coefficient) % q
            if y == 0:
                support.append(x)
        if len(support) >= 5:
            actual[(a, b)] = tuple(support)
    saved = {tuple(r['f']): tuple(r['support']) for r in rec['list']}
    check(f'full independent message list {label}', saved == actual and set(actual) == set(fibers[label]))
    check(f'full terminal correction {label}',
          rec['six_subsets'] == N6[label] and rec['incidences'] == sum(fibers[label].values())
          and len(actual) == sum(fibers[label].values())-5*N6[label]
          and all(r['multiplicity'] == choose(len(r['support']), 5) for r in rec['list']))
check('constructor reports fully passed',
      not data['failures'] and data['check_count'] == len(data['checks'])
      and all(c['passed'] for c in data['checks']))
failures = [r['name'] for r in checks if not r['passed']]
out = BASE/'order-four-pole-verification.json'
out.write_text(json.dumps({'check_count': len(checks), 'checks': checks,
                           'failures': failures, 'ratio_required': '<=1',
                           'ratio_actual_interval': [3676307, 3676308]}, indent=2)+'\n')
print(f'independent checks={len(checks)} failures={len(failures)}; certificate: {out}')
print('actual allowance/T in (3676307,3676308), required <=1; estimate parked')
if failures:
    print(failures)
    raise SystemExit(1)
