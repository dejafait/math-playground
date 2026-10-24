#!/usr/bin/env python3
"""Independent L122 audit: polynomial Euclid, Sylvester norms, full data checks.

Standard library only; imports neither producer nor replay. Mathematical
exhaustiveness and Hensel arguments are in canonical L122, not check flags.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from hashlib import sha256
from pathlib import Path
from math import comb
import json

ROOT = Path(__file__).parent
SOURCE = ROOT / 'marked-octic-two-adic-image-certificate.json'
OUT = ROOT / 'marked-octic-two-adic-image-audit-certificate.json'
C = json.loads(SOURCE.read_text())
G = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
EN = [22130658, -74245842, 91279980, -48315300, 9150625]
E = [Q(x, EN[-1]) for x in EN]
MOD = [8, 4, 4, 4]


def trim(a):
    a = list(map(Q, a))
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([x*c for x in a])


def mul(a, b):
    if not a or not b:
        return []
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def divrem(a, b):
    a, b = trim(a), trim(b)
    q = [Q(0)]*max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        j, c = len(a)-len(b), a[-1]/b[-1]
        q[j] = c
        a = add(a, [Q(0)]*j+scale(b, -c))
    return trim(q), a


def red(a):
    return divrem(a, E)[1]


def fm(a, b):
    return red(mul(a, b))


def inv(a):
    old, new, s0, s1 = E, red(a), [], [Q(1)]
    while new:
        q, r = divrem(old, new)
        old, new = new, r
        s0, s1 = s1, add(s0, scale(mul(q, s1), -1))
    assert len(old) == 1
    return red(scale(s0, 1/old[0]))


def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    out = [Q(1)]
    for _ in range(n):
        out = fm(out, a)
    return out


def vec(a):
    return trim(a)+[Q(0)]*(4-len(trim(a)))


def vp(a):
    a = Q(a)
    assert a
    n, d = abs(a.numerator), a.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()


def vl(a):
    return min(4*vp(x)+i for i, x in enumerate(a) if x)


def modq(x, m):
    x = Q(x)
    return x.numerator*pow(x.denominator, -1, m) % m


def nlabel(x):
    w = vp(x)
    return [w % 2, modq(Q(x)/Q(2)**w, 8)]


def clean(a):
    if isinstance(a, Q):
        return str(a)
    if isinstance(a, dict):
        return {str(k): clean(v) for k, v in a.items()}
    if isinstance(a, (list, tuple)):
        return [clean(v) for v in a]
    return a


checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=clean(actual), required=clean(required),
                       passed=clean(actual) == clean(required)))


def compare(name, value):
    check('complete source section '+name, value, C[name])


def shift(p, a, h):
    return [sum(p[j]*comb(j, k)*a**(j-k)*h**k for j in range(k, len(p)))
            for k in range(len(p))]


def evaluate(p, a):
    return sum((Q(c)*a**i for i, c in enumerate(p)), Q(0))


check('Eisenstein all coefficients', [vp(x) for x in E], [1, 1, 2, 2, 0])
A, B, X = [3036, -6050, 3025], [2541, -2420], [0, 1]
check('full E numerator identity', add(mul(A, A), scale(mul([-1, 1], mul(B, B)), -2)), list(map(Q, EN)))
check('full transformed P', [Q(c, 256) for c in shift(G[::2], 1, 4)], list(map(Q, [44, 484, 0, -4840, 3025])))
r = scale(fm(A, inv(B)), -1)
check('explicit r', vec(r), list(map(Q, [468, -1126, Q(2585, 3), Q(-5500, 27)])))
check('r squared', fm(r, r), list(map(Q, [-2, 2])))
check('r quartic equation', add(add(scale(power(r, 4), 3025), scale(power(r, 3), -4840)), add(scale(r, 484), [44])), [])
check('r and denominator valuations', [vl(r), vl(B)], [2, 0])
target = add([1], scale(r, 4))
check('pi recovery', add([1], scale(fm(add(target, [-1]), add(target, [-1])), Q(1, 32))), list(map(Q, X)))
alpha = add([1], scale(r, 2))
lifts = []
for i in range(3):
    error = add(fm(alpha, alpha), scale(target, -1))
    d = scale(alpha, 2)
    lifts.append(dict(iteration=i, alpha=vec(alpha), residual=vec(error),
                      residual_valuation=vl(error), derivative_valuation=vl(d),
                      root_error_lower_bound=vl(error)-vl(d)))
    if i < 2:
        alpha = add(alpha, scale(fm(error, inv(d)), -1))
check('all strict Hensel inequalities', [z['residual_valuation'] > 2*z['derivative_valuation'] for z in lifts], [True]*3)
check('residual valuations', [z['residual_valuation'] for z in lifts], [12, 16, 24])
check('two conjugate distance valuations', [vl(add(alpha, [-1])), vl(add(alpha, [1]))], [6, 4])
field = dict(E_numerator=EN, monic_E=E, r=vec(r), denominator=vec(B),
             alpha_square_target=vec(target), hensel=lifts,
             alpha_approximation=vec(alpha), alpha_error_lower_bound=20,
             actual_theta_transports=['alpha', '-alpha'])
compare('field', field)

# Independently build the entire multiplication tensor, then use integer
# modular arithmetic. Coordinate reduction is by the proved pi^9 ideal.
tensor = [[tuple(modq(c, 8) for c in vec(red([0]*(i+j)+[1])))
           for j in range(4)] for i in range(4)]


def rm(a, b):
    return tuple(sum(a[i]*b[j]*tensor[i][j][k] for i in range(4) for j in range(4)) % MOD[k]
                 for k in range(4))


units = list(product(range(1, 8, 2), range(4), range(4), range(4)))
squares = sorted({rm(a, a) for a in units})
orbits = {tuple(sorted({rm(a, s) for s in squares})) for a in units}
reps = sorted(o[0] for o in orbits)
lookup = {a: i for i, rep in enumerate(reps) for a in {rm(rep, s) for s in squares}}
check('complete disjoint cosets', [len(units), len(squares), len(orbits), len(lookup), sorted(map(len, orbits))],
      [256, 8, 32, 256, [8]*32])
table = [[lookup[rm(a, b)] for b in reps] for a in reps]
ring = dict(coefficient_moduli=MOD, units=units, unit_squares=squares,
            unit_class_representatives=reps,
            complete_unit_cosets=[dict(residue=a, label=lookup[a]) for a in units],
            unit_multiplication_table=table)
compare('residue_ring', ring)


def label(a):
    w = vl(a)
    u = vec(fm(a, power(X, -w)))
    assert vl(u) == 0
    return 32*(w % 2)+lookup[tuple(modq(x, m) for x, m in zip(u, MOD))]


def lm(i, j):
    return 32*((i//32) ^ (j//32))+table[i % 32][j % 32]


def determinant(m):
    """Fraction-free elimination over Q, retaining full trace."""
    a = [list(map(Q, row)) for row in m]
    previous, sign, trace = Q(1), 1, []
    for k in range(len(a)-1):
        row = next(i for i in range(k, len(a)) if a[i][k])
        if row != k:
            a[k], a[row] = a[row], a[k]
            sign = -sign
        pivot = a[k][k]
        trace.append(dict(column=k, swap_row=row, pivot=pivot, previous=previous))
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j] = (a[i][j]*pivot-a[i][k]*a[k][j])/previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1], trace


norm_evidence, class_rows = [], []
for p in range(2):
    for i, rep in enumerate(reps):
        element = fm(power(X, p), list(map(Q, rep)))
        # Norm = resultant(monic E, element). This uses the full Sylvester
        # matrix, independently of both earlier multiplication determinants.
        d = len(element)-1
        matrix = [[Q(0)]*(4+d) for _ in range(4+d)]
        for j in range(d):
            matrix[j][j:j+5] = E[::-1]
        for j in range(4):
            matrix[d+j][j:j+d+1] = element[::-1]
        norm, trace = determinant(matrix)
        row = dict(label=32*p+i, representative=vec(element), norm=norm, norm_square_class=nlabel(norm))
        class_rows.append(row)
        norm_evidence.append(dict(label=32*p+i, sylvester=matrix, trace=trace, norm=norm))
        check('representative label '+str(32*p+i), label(element), 32*p+i)
compare('square_classes', class_rows)
nl = [row['norm_square_class'] for row in class_rows]
products = [[lm(i, j) for j in range(64)] for i in range(64)]
check('full norm homomorphism', [[i, j] for i in range(64) for j in range(64)
      if nl[lm(i, j)] != [nl[i][0] ^ nl[j][0], nl[i][1]*nl[j][1] % 8]], [])
check('norm fibers', sorted(Counter(map(tuple, nl)).values()), [8]*8)
scalars = [dict(exponents=[a, b, c], scalar=Q((-1)**a*2**b*5**c),
                label=label([Q((-1)**a*2**b*5**c)])) for a, b, c in product(range(2), repeat=3)]
compare('scalar_rows', scalars)
sl = sorted(row['label'] for row in scalars)
compare('scalar_labels', sl)
check('complete scalar subgroup', sorted({lm(i, j) for i in sl for j in sl}), sl)


def canon(pair):
    return min((lm(pair[0], s), lm(pair[1], s)) for s in sl)


raw = [(i, j) for i in range(64) for j in range(64) if nl[i] == nl[j]]
ambient = sorted({canon(pair) for pair in raw})
compare('ambient_raw', raw)
compare('ambient_quotient', ambient)
check('free common scalar orbits', sorted({len({(lm(i, s), lm(j, s)) for s in sl}) for i, j in raw}), [8])
even, reciprocal = shift(G, 0, 2), shift(G[::-1], 0, 2)
check('every coefficient even chart modulo 8', [c % 8 for c in even], [1]+[0]*8)
check('every coefficient reciprocal chart modulo 8', [c % 8 for c in reciprocal], [1]+[0]*8)
odd = []
for a in range(1, 16, 2):
    coeff = shift(G, a, 16)
    odd.append(dict(center=a, modulus=16, shifted_coefficients=coeff,
                    center_valuation=vp(coeff[0]), normalized_unit_mod8=nlabel(coeff[0])[1],
                    variation_minimum=min(vp(c) for c in coeff[1:] if c),
                    required_variation_minimum=13, has_points=nlabel(coeff[0]) == [0, 1]))
compare('coordinate_tests', dict(even_shift=even, reciprocal_shift=reciprocal, odd_disks=odd))
check('full odd exclusion/realization thresholds', [(r['center_valuation'], r['variation_minimum']) for r in odd], [(10, 13)]*8)
rows = []
for chart, centers, modulus in [('finite_even', range(0, 8, 2), 8), ('finite_odd', [3, 13], 16)]:
    for t in centers:
        aa, bb = add([t], scale(alpha, -1)), add([t], alpha)
        pair = (label(aa), label(bb))
        w = [vl(aa), vl(bb)]
        rows.append(dict(chart=chart, center=t, modulus=modulus, G_value=evaluate(G, t),
                         G_square_class=nlabel(evaluate(G, t)), component_valuations=w,
                         perturbation_lower_bound=4*vp(modulus), required_strict_bound=max(w)+8,
                         raw_labels=pair, quotient=canon(pair)))
for q in [2, 4, 6]:
    aa, bb = add([1], scale(alpha, -q)), add([1], scale(alpha, q))
    pair = (label(aa), label(bb))
    w = [vl(aa), vl(bb)]
    rows.append(dict(chart='reciprocal', center=q, modulus=8, reciprocal_value=evaluate(G[::-1], q),
                     reciprocal_square_class=nlabel(evaluate(G[::-1], q)), component_valuations=w,
                     perturbation_lower_bound=12, required_strict_bound=max(w)+8,
                     raw_labels=pair, quotient=canon(pair)))
rows.append(dict(chart='reciprocal_tail', center=0, modulus=8, perturbation_lower_bound=12,
                 required_strict_bound=8, raw_labels=(0, 0), quotient=canon((0, 0)),
                 finite_realization_q=8, reciprocal_value=evaluate(G[::-1], 8),
                 reciprocal_square_class=nlabel(evaluate(G[::-1], 8))))
compare('point_disks', rows)
check('all strict component bounds', [r['perturbation_lower_bound'] > r['required_strict_bound'] for r in rows], [True]*10)
check('all center realizations', [r.get('G_square_class', r.get('reciprocal_square_class')) for r in rows], [[0, 1]]*10)
check('alpha precision strict', 20 > 6+8, True)
image = sorted({tuple(r['quotient']) for r in rows})
compare('point_image', image)
check('image norm membership', all(a in ambient for a in image), True)
infinity = [dict(Z=z, representative=3025, raw_labels=[label([3025])]*2,
                 quotient=canon((label([3025]), label([3025])))) for z in [-55, 55]]
compare('infinity', infinity)
check('separate smooth infinity equations', [(z*z == G[-1], 2*z != 0) for z in [-55, 55]], [(True, True)]*2)
compare('input', dict(G=G, leading_square=55**2, e=4, square_precision=9, strict_threshold=8))
compare('counts', dict(field_square_classes=64, raw_norm_fiber=len(raw), scalar_image=len(sl), ambient=len(ambient), image=len(image)))
check('required image and ambient', [len(image), len(ambient)], [5, 64])
failures = [r for r in checks if not r['passed']]
report = dict(source=SOURCE.name, source_sha256=sha256(SOURCE.read_bytes()).hexdigest(),
              checks=checks, failures=failures, field=field, residue_ring=ring,
              norm_sylvester_evidence=norm_evidence, complete_class_products=products,
              square_classes=class_rows, scalar_rows=scalars, ambient_raw=raw, ambient_quotient=ambient,
              coordinate_tests=dict(even_shift=even, reciprocal_shift=reciprocal, odd_disks=odd),
              point_disks=rows, infinity=infinity, point_image=image,
              precision=dict(residue_actual=9, residue_required=9, alpha_actual=20, alpha_strict_threshold=14,
                             disks_actual=[12, 16, 12], disks_strict_threshold=[8, 14, 8]),
              comparison=dict(image=len(image), ambient=len(ambient)),
              limitations=['No global class removed', 'No supported group enumeration', 'No rational or integer point completeness'])
OUT.write_text(json.dumps(clean(report), indent=2)+'\n')
print(json.dumps(dict(checks=len(checks), failures=[r['name'] for r in failures],
                      actual_image=len(image), required_ambient=len(ambient), precision=report['precision'], path=str(OUT))))
if failures:
    raise SystemExit(1)
