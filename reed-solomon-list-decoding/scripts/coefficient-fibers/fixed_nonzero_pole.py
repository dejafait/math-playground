"""One approved translated-pole dictionary and absolute-sieve certificate."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, prod
from pathlib import Path
import json

OUT = Path(__file__).with_name('fixed-nonzero-pole-results.json')
checks = []


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})


def rat(x):
    x = Fraction(x)
    return {'numerator': x.numerator, 'denominator': x.denominator}


Q, n, s, B = 65537, 1024, 67, 769
D = (Q-1)*Q**2
C = comb(n, s)
T = Fraction(Q**28, 2**128)
E0 = comb(B+s-1, s)
orders = [2**a for a in range(1, 17)]
check('generator outside H', pow(3, 32768, Q) == Q-1 and pow(3, n, Q) != 1)
check('subgroup generator', pow(3, 64, Q) == 19139)
check('strict joint-modulus rounding', 9*Q < B*B)
check('all powers nonzero modulo characteristic', all(j % Q for j in range(1, s+1)))
check('full character count', 1 + sum(d//2 for d in orders)
      + (Q-1)*(Q**2-1) == D)
check('binomial factorial reconstruction', C == prod(range(n-s+1, n+1))//factorial(s))
pascal = [1]+[0]*s
for _ in range(n):
    for k in range(s, 0, -1):
        pascal[k] += pascal[k-1]
check('binomial Pascal reconstruction', C == pascal[s])

exceptional = []
for d in orders:
    weights = [n if j % d == 0 else B for j in range(1, s+1)]
    coeff = [Fraction(1)]
    for k in range(1, s+1):
        coeff.append(sum(weights[j-1]*coeff[k-j] for j in range(1, k+1))/k)
    # Independent formal product (1-t)^(-B)*(1-t^d)^(-(n-B)/d).
    expansion = [Fraction(0)]*(s+1)
    factor = Fraction(1)
    for ell in range(s//d+1):
        if ell:
            factor *= Fraction(n-B+(ell-1)*d, d*ell)
        for k in range(d*ell, s+1):
            expansion[k] += factor*comb(B+k-d*ell-1, k-d*ell)
    for k in range(s+1):
        check(f'order {d} complete cycle coefficient {k}', coeff[k] == expansion[k])
    check(f'order {d} weights', all(B <= w <= n for w in weights))
    exceptional.append({'order': d, 'multiplicity': d//2,
                        'cycle_weights': weights,
                        'coefficients': [rat(x) for x in coeff],
                        'subset_bound': rat(coeff[s])})

constant_term = sum(Fraction(r['multiplicity'])*Fraction(**{
    'numerator': r['subset_bound']['numerator'],
    'denominator': r['subset_bound']['denominator']}) for r in exceptional)/D
principal = Fraction(C, D)
nonconstant = (1-Fraction(1, Q**2))*E0
U = principal + nonconstant + constant_term
ratio = U/T
lo = ratio.numerator//ratio.denominator
check('allowance exceeds threshold', U > T)
check('strict ratio bracket', lo*T < U < (lo+1)*T)
check('nonconstant term already exceeds threshold', nonconstant > T)
check('constant contribution nonnegative', constant_term >= 0)


def mul(a, b, q):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % q
    return tuple(c)


def root_product(roots, q):
    p = (1,)
    for z in roots:
        p = mul(p, (-z % q, 1), q)
    return p


def ev(p, z, q):
    out = 0
    for c in reversed(p):
        out = (out*z+c) % q
    return out


q, ns, ss, ks, pole = 17, 8, 5, 2, 3
H = tuple(sorted({pow(9, j, q) for j in range(ns)}))
check('small pole excluded', pole not in H and len(H) == ns)
fibers = defaultdict(dict)
for S in combinations(H, ss):
    shifted = tuple((x-pole) % q for x in S)
    g = root_product(shifted, q)
    c, b, a = g[:3]
    # f in Z=X-pole, with cancellation of monic leading terms.
    f = tuple(-g[j] % q for j in range(3, ss))
    check(f'small quotient identity {S}', all(
        (z**ss+a*z*z+b*z+c-z**3*ev(f, z, q)-ev(g, z, q)) % q == 0
        for z in range(q)))
    P = prod(shifted) % q
    u = sum(pow(z, -1, q) for z in shifted) % q
    v = sum(pow(z*w % q, -1, q) for z, w in combinations(shifted, 2)) % q
    check(f'small translated signs {S}',
          (c, b, a) == (-P % q, P*u % q, -P*v % q))
    fibers[(a, b, c)][f] = S

all_messages = list(product(range(q), repeat=ks))
message_values = {f: tuple(ev(f, (x-pole) % q, q) for x in H) for f in all_messages}
occupied = []
for a, b, c in product(range(q), range(q), range(1, q)):
    Y = tuple(((x-pole)**ss+a*(x-pole)**2+b*(x-pole)+c)
              *pow(pow(x-pole, 3, q), -1, q) % q for x in H)
    actual = {}
    for f, values in message_values.items():
        support = tuple(x for x, y, val in zip(H, Y, values) if y == val)
        if len(support) >= ss:
            actual[f] = support
    expected = fibers.get((a, b, c), {})
    check(f'entire small list {(a, b, c)}', actual == expected)
    if expected:
        occupied.append({'label_abc': [a, b, c], 'list': [
            {'message_in_Z': list(f), 'support': list(S)} for f, S in sorted(expected.items())]})
check('all small subsets retained', sum(len(v) for v in fibers.values()) == comb(ns, ss))

certificate = {
    'parameters': {'Q': Q, 'n': n, 's': s, 'B': B, 'full_group_order': D},
    'binomial': C, 'threshold': rat(T), 'nonconstant_subset_bound': E0,
    'exceptional_orders': exceptional,
    'principal': rat(principal), 'nonconstant': rat(nonconstant),
    'constant_only': rat(constant_term), 'uniform_upper': rat(U),
    'ratio': rat(ratio), 'strict_ratio_interval': [lo, lo+1],
    'positive_failure_margin': rat(U-T),
    'small_case': {'field': q, 'H': H, 'pole': pole, 'k': ks, 's': ss,
                   'centers_checked': q*q*(q-1), 'messages_per_center': q**ks,
                   'occupied_fibers': occupied},
    'checks': checks, 'check_count': len(checks),
    'failures': [c for c in checks if not c['passed']],
}
OUT.write_text(json.dumps(certificate, indent=2)+'\n')
print(f"Checks: {len(checks)}; failures: {len(certificate['failures'])}")
print(f'Actual upper/T: strictly between {lo} and {lo+1}; required: <=1')
print(f'Full certificate: {OUT}')
if certificate['failures']:
    raise SystemExit(1)
