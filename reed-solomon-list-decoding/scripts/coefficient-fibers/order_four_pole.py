"""One assessed fourth-order-pole cap; exact arithmetic and full small lists."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, prod
from pathlib import Path
import json

OUT = Path(__file__).with_name('order-four-pole-results.json')
checks = []


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})


def rat(x):
    return {'numerator': x.numerator, 'denominator': x.denominator}


Q, n, s, B = 65537, 1024, 67, 769
C, error_binomial = comb(n, s), comb(B+s-1, s)
T = Fraction(Q**28, 2**128)
principal = Fraction(C, Q**3)
error = (1-Fraction(1, Q**3))*B*error_binomial
U = principal+error
ratio = U/T
ratio_floor = ratio.numerator//ratio.denominator
check('strict character rounding', (B-1)**2 < 9*Q < B**2)
check('all cycle powers invertible', all(j % Q != 0 for j in range(1, s+1)))
check('principal residual cancellation of Q-1',
      Fraction((Q-1)*C, (Q-1)*Q**3) == principal)
check('nonconstant character count',
      Fraction((Q-1)*(Q**3-1), (Q-1)*Q**3) == 1-Fraction(1, Q**3))
check('binomial independent factorial reconstruction',
      C == prod(range(n-s+1, n+1))//factorial(s))
row = [1]+[0]*s
for _ in range(n):
    for j in range(s, 0, -1):
        row[j] += row[j-1]
check('binomial complete Pascal reconstruction', C == row[s])
# The unsigned cycle exponential satisfies k*c_k=B*sum_{j=1}^k c_{k-j}.
cycles = [Fraction(1)]
for k in range(1, s+1):
    cycles.append(Fraction(B, k)*sum(cycles))
    check(f'complete cycle coefficient {k}', cycles[k] == comb(B+k-1, k))
check('sieve retains factorial', cycles[s]*factorial(s) == prod(range(B, B+s)))
check('cap exceeds required threshold', U > T)
check('exact integer ratio bracket', ratio_floor*T < U < (ratio_floor+1)*T)


def mul(a, b, q):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % q
    return tuple(c)


def roots_poly(S, q):
    a = (1,)
    for x in S:
        a = mul(a, (-x % q, 1), q)
    return a


def log_coords(a, q):
    c = a[0]
    ci = pow(c, -1, q)
    u, v, w = ((a[i]*ci) % q for i in (1, 2, 3))
    return (c, u, (v-u*u*pow(2, -1, q)) % q,
            (w-u*v+u**3*pow(3, -1, q)) % q)


q, ns, ks, ss = 17, 8, 2, 5
H = tuple(sorted({pow(9, j, q) for j in range(ns)}))
check('small proper subgroup', len(H) == ns and pow(9, ns, q) == 1 and 16 in H)
fibers = defaultdict(Counter)
candidate_polys = defaultdict(dict)
pair_records = []
categories = Counter()
for S in combinations(H, ss):
    pS = roots_poly(S, q)
    for r in range(1, q):
        g = mul(pS, (-r % q, 1), q)
        label = g[:4]
        f = (-g[4] % q, -g[5] % q)
        support = tuple(x for x in H if
                        (pow(x, 6, q)+sum(label[j]*pow(x, j, q) for j in range(4))
                         -pow(x, 4, q)*(f[0]+f[1]*x)) % q == 0)
        expected = tuple(sorted(set(S) | ({r} if r in H else set())))
        check(f'pair identity {len(pair_records)}',
              support == expected and g[0] != 0 and g[6] == 1
              and (-label[0]*pow(pS[0], -1, q)) % q == r)
        logS, logr, logg = log_coords(pS, q), log_coords((-r % q, 1, 0, 0), q), log_coords(g, q)
        check(f'log multiplication {len(pair_records)}',
              logg == (logS[0]*logr[0] % q,
                       *((logS[j]+logr[j]) % q for j in range(1, 4))))
        fibers[label][f] += 1
        candidate_polys[label][f] = g
        category = 'repeated' if r in S else 'extra' if r in H else 'outside'
        categories[category] += 1
        pair_records.append({'S': S, 'r': r, 'label': label, 'f': f,
                             'G': g, 'support': support, 'category': category})

six = Counter(roots_poly(J, q)[:4] for J in combinations(H, ss+1))
occupied = set(fibers)
empty = next(a for a in product(range(q), repeat=4) if a[0] != 0 and a not in occupied)
labels = sorted(occupied | {empty})
list_records = []
for label in labels:
    # Independent converse check: enumerate every message, without factoring G.
    actual = {}
    for f in product(range(q), repeat=ks):
        agreement = tuple(x for x in H if
                          (pow(x, 6, q)+sum(label[j]*pow(x, j, q) for j in range(4))
                           -pow(x, 4, q)*(f[0]+f[1]*x)) % q == 0)
        if len(agreement) >= ss:
            actual[f] = agreement
    check(f'entire small list {label}', set(actual) == set(fibers[label]))
    M = sum(fibers[label].values())
    check(f'extra-root correction {label}', len(actual) == M-ss*six[label])
    check(f'exact incidence multiplicity {label}',
          all(fibers[label][f] == comb(len(J), ss) for f, J in actual.items()))
    list_records.append({'label': label, 'incidences': M, 'six_subsets': six[label],
                         'list': [{'f': f, 'support': J, 'multiplicity': fibers[label][f]}
                                  for f, J in sorted(actual.items())]})
check('all small residual branches retained', set(categories) == {'repeated', 'extra', 'outside'})
check('complete small pair coverage', len(pair_records) == comb(ns, ss)*(q-1))
check('complete small six-subset coverage', sum(six.values()) == comb(ns, ss+1))
failures = [c['name'] for c in checks if not c['passed']]
result = {
    'parameters': {'Q': Q, 'n': n, 'agreement': s, 'B': B,
                   'group_order': (Q-1)*Q**3, 'nonconstant_characters': (Q-1)*(Q**3-1)},
    'exact': {'subset_count': C, 'cycle_coefficients': [rat(x) for x in cycles],
              'error_binomial': error_binomial, 'principal': rat(principal),
              'error': rat(error), 'upper_cap': rat(U), 'threshold': rat(T),
              'cap_to_threshold': rat(ratio), 'ratio_integer_lower': ratio_floor,
              'failure_margin': U.numerator*T.denominator-T.numerator*U.denominator},
    'decision': 'PARK_THIS_ABSOLUTE_SIEVE_ESTIMATE; no actual-list lower bound',
    'small': {'q': q, 'H': H, 'k': ks, 'agreement': ss,
              'pair_count': len(pair_records), 'categories': dict(categories),
              'occupied_centers': len(occupied), 'empty_center': empty,
              'pairs': pair_records, 'lists': list_records},
    'checks': checks, 'check_count': len(checks), 'failures': failures,
}
OUT.write_text(json.dumps(result, indent=2)+'\n')
print(f'checks={len(checks)} failures={len(failures)}; full certificate: {OUT}')
print(f'actual upper allowance / required threshold is in ({ratio_floor}, {ratio_floor+1}); required <=1')
print(f'small coverage: {len(pair_records)} pairs, {len(labels)} complete lists; branches={dict(categories)}')
print(f'decision={result["decision"]}')
if failures:
    print(f'failures={failures}')
    raise SystemExit(1)
