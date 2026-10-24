#!/usr/bin/env python3
"""Full arithmetic replay, with integer residue arithmetic and Leibniz norms.

Does not import producer code. This is arithmetic verification in the same
research step, not the later independent critical mathematical audit.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations, product
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).parent
SOURCE = ROOT/'marked-octic-two-adic-image-certificate.json'
OUT = ROOT/'marked-octic-two-adic-image-replay.json'
C = json.loads(SOURCE.read_text())
E = list(map(Q, C['field']['monic_E']))
MOD = [8, 4, 4, 4]
ONE = (Q(1), Q(0), Q(0), Q(0))
PI = (Q(0), Q(1), Q(0), Q(0))


def times(a, b):
    out = [Q(0)]*7
    for k in range(7):
        out[k] = sum((a[i]*b[k-i] for i in range(4) if 0 <= k-i < 4), Q(0))
    for k in [6, 5, 4]:
        lead = out[k]
        for j in range(5):
            out[k-4+j] -= lead*E[j]
    return tuple(out[:4])


def plus(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scaled(a, c):
    return tuple(x*c for x in a)


def vp(x):
    x = Q(x)
    n, d, w = x.numerator, x.denominator, 0
    assert n
    while n % 2 == 0:
        n //= 2
        w += 1
    while d % 2 == 0:
        d //= 2
        w -= 1
    return w


def vl(a):
    return min(4*vp(x)+i for i, x in enumerate(a) if x)


def power(a, n):
    out = ONE
    for _ in range(n):
        out = times(out, a)
    return out


PI_INV = tuple(-x/E[0] for x in [E[1], E[2], E[3], Q(1)])


def normalize(a):
    w = vl(a)
    u = times(a, power(PI_INV if w >= 0 else PI, abs(w)))
    return w % 2, tuple(x.numerator*pow(x.denominator, -1, m) % m for x, m in zip(u, MOD))


def rtimes(a, b):
    # All divisions are by the odd leading coefficient; work modulo eight.
    ec = [x.numerator*pow(x.denominator, -1, 8) % 8 for x in E]
    out = [sum(a[i]*b[k-i] for i in range(4) if 0 <= k-i < 4) % 8 for k in range(7)]
    for k in [6, 5, 4]:
        lead = out[k]
        for j in range(5):
            out[k-4+j] = (out[k-4+j]-lead*ec[j]) % 8
    return tuple(out[i] % MOD[i] for i in range(4))


def nlabel(x):
    w = vp(x)
    unit = Q(x)/Q(2)**w
    return [w % 2, unit.numerator*pow(unit.denominator, -1, 8) % 8]


checks, failures = 0, []


def check(name, actual, expected):
    global checks
    checks += 1
    if actual != expected:
        failures.append(dict(name=name, actual=str(actual), expected=str(expected)))


check('inverse uniformizer identity', times(PI, PI_INV), ONE)
units = list(product(range(1, 8, 2), range(4), range(4), range(4)))
squares = sorted({rtimes(x, x) for x in units})
check('all unit squares', squares, [tuple(x) for x in C['residue_ring']['unit_squares']])
coset = {tuple(row['residue']): row['label'] for row in C['residue_ring']['complete_unit_cosets']}
reps = [tuple(x) for x in C['residue_ring']['unit_class_representatives']]
for i, rep in enumerate(reps):
    check(f'whole unit coset {i}', sorted(x for x in units if coset[x] == i), sorted(rtimes(rep, s) for s in squares))
table = [[coset[rtimes(a, b)] for b in reps] for a in reps]
check('entire class product table', table, C['residue_ring']['unit_multiplication_table'])


def label(a):
    parity, unit = normalize(a)
    return parity*32+coset[unit]


def lm(a, b):
    return ((a//32) ^ (b//32))*32+table[a % 32][b % 32]


norm_labels = []
for row in C['square_classes']:
    a = tuple(map(Q, row['representative']))
    columns = [times(a, tuple(Q(i == j) for i in range(4))) for j in range(4)]
    answer = Q(0)
    for p in permutations(range(4)):
        inversions = sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
        term = Q((-1)**inversions)
        for i in range(4):
            term *= columns[p[i]][i]
        answer += term
    check(f'full determinant norm {row["label"]}', answer, Q(row['norm']))
    check(f'norm square class {row["label"]}', nlabel(answer), row['norm_square_class'])
    check(f'full representative label {row["label"]}', label(a), row['label'])
    norm_labels.append(nlabel(answer))
for row in C['scalar_rows']:
    check(f'scalar transport {row["scalar"]}', label((Q(row['scalar']), Q(0), Q(0), Q(0))), row['label'])
scalars = C['scalar_labels']


def canon(pair):
    return min((lm(pair[0], s), lm(pair[1], s)) for s in scalars)


raw = [(a, b) for a in range(64) for b in range(64) if norm_labels[a] == norm_labels[b]]
ambient = sorted({canon(pair) for pair in raw})
check('entire raw norm fiber', raw, [tuple(x) for x in C['ambient_raw']])
check('entire common-scalar quotient', ambient, [tuple(x) for x in C['ambient_quotient']])
r = tuple(map(Q, C['field']['r']))
target = plus(ONE, scaled(r, 4))
for i, row in enumerate(C['field']['hensel']):
    a = tuple(map(Q, row['alpha']))
    error = plus(times(a, a), scaled(target, -1))
    check(f'whole Hensel residual {i}', error, tuple(map(Q, row['residual'])))
    check(f'Hensel error valuation {i}', vl(error), row['residual_valuation'])
    if i:
        previous = tuple(map(Q, C['field']['hensel'][i-1]['alpha']))
        previous_error = tuple(map(Q, C['field']['hensel'][i-1]['residual']))
        check(f'exact Newton equation {i}',
              times(scaled(previous, 2), plus(a, scaled(previous, -1))), scaled(previous_error, -1))
alpha = tuple(map(Q, C['field']['alpha_approximation']))
G = C['input']['G']
for row in C['coordinate_tests']['odd_disks']:
    a = row['center']
    coeffs = [sum(G[j]*comb(j, k)*a**(j-k)*16**k for j in range(k, 9)) for k in range(9)]
    check(f'complete odd-disk polynomial {a}', coeffs, row['shifted_coefficients'])
    check(f'odd-disk variation {a}', min(vp(x) for x in coeffs[1:] if x), row['variation_minimum'])
    check(f'odd-disk feasibility {a}', nlabel(coeffs[0]) == [0, 1], row['has_points'])
image = []
for row in C['point_disks']:
    t = row['center']
    if row['chart'].startswith('finite'):
        pair = (label(plus((Q(t), Q(0), Q(0), Q(0)), scaled(alpha, -1))),
                label(plus((Q(t), Q(0), Q(0), Q(0)), alpha)))
    else:
        pair = (label(plus(ONE, scaled(alpha, -t))), label(plus(ONE, scaled(alpha, t))))
    check(f'disk raw labels {row["chart"]} {t}', list(pair), row['raw_labels'])
    check(f'disk scalar projection {row["chart"]} {t}', list(canon(pair)), row['quotient'])
    image.append(canon(pair))
check('entire point image', sorted(set(image)), [tuple(x) for x in C['point_image']])
check('both separate infinity rows', [(x['Z'], x['quotient']) for x in C['infinity']], [(-55, [0, 0]), (55, [0, 0])])
report = dict(source=SOURCE.name, source_sha256=sha256(SOURCE.read_bytes()).hexdigest(),
              checks=checks, failures=failures,
              complete_evidence=dict(unit_cosets=32, exact_norm_determinants=64,
                                     raw_norm_pairs=len(raw), quotient_pairs=len(ambient),
                                     odd_disks=8, feasible_disk_rows=10, infinity_rows=2),
              actual_image=len(set(image)), ambient_required_comparison=len(ambient),
              independent_critical_audit='pending')
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(dict(checks=checks, failures=failures, image=len(set(image)),
                      ambient=len(ambient), path=str(OUT))))
if failures:
    raise SystemExit(1)
