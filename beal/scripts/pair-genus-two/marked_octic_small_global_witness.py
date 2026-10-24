#!/usr/bin/env python3
"""Fixed eight-product test; imports L122's audited exact local arithmetic.

Full global matrices, norm factorizations, local residues and all eight
rows are written to disk. This is not supported-class enumeration.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from hashlib import sha256
import json

import marked_octic_two_adic_image as local

BASE = Path(__file__).parent
OUT = BASE / 'marked-octic-small-global-witness-certificate.json'
SOURCE = BASE / 'marked-octic-two-adic-image-certificate.json'
F = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
MONIC = [Q(x, 275) for x in F]
S = (2, 3, 5, 11)


def gmul(a, b):
    c = [Q(0)] * 15
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    for k in range(14, 7, -1):
        for i in range(8):
            c[k-8+i] -= c[k]*MONIC[i]
    return tuple(c[:8])


def determinant(matrix):
    m = [list(row) for row in matrix]
    value = Q(1)
    trace = []
    for j in range(len(m)):
        p = next((i for i in range(j, len(m)) if m[i][j]), None)
        if p is None:
            return Q(0), trace
        if p != j:
            m[j], m[p] = m[p], m[j]
            value = -value
        pivot = m[j][j]
        value *= pivot
        trace.append(dict(column=j, swapped_row=p, pivot=pivot))
        for i in range(j+1, len(m)):
            z = m[i][j]/pivot
            m[i] = [a-z*b for a, b in zip(m[i], m[j])]
    return value, trace


def gnorm(a):
    columns = [gmul(a, tuple(Q(i == j) for i in range(8))) for j in range(8)]
    matrix = [[columns[j][i] for j in range(8)] for i in range(8)]
    value, trace = determinant(matrix)
    return dict(matrix=matrix, elimination=trace, norm=value)


def factor(x):
    assert x
    exponents = {}
    n, d = abs(x.numerator), x.denominator
    for p in S:
        v = 0
        while n % p == 0:
            n //= p
            v += 1
        while d % p == 0:
            d //= p
            v -= 1
        exponents[p] = v
    return dict(sign=1 if x > 0 else -1, exponents=exponents,
                numerator_remainder=n, denominator_remainder=d,
                square=x > 0 and n == d == 1 and all(v % 2 == 0 for v in exponents.values()))


def main():
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required, passed=actual == required))

    source = json.loads(SOURCE.read_text())
    check('unchanged full polynomial', source['input']['G'], [11*x for x in F])
    check('local actual theta', source['field']['actual_theta_transports'], ['alpha', '-alpha'])
    check('strict square threshold', source['input']['strict_threshold'], 8)
    check('alpha root error', source['field']['alpha_error_lower_bound'], 20)
    cosets = {tuple(row['residue']): row['label'] for row in source['residue_ring']['complete_unit_cosets']}
    unit_table = source['residue_ring']['unit_multiplication_table']
    scalar_labels = source['scalar_labels']
    point_image = {tuple(pair) for pair in source['point_image']}
    check('complete unit labels', len(cosets), 256)
    check('point image is audited five-element set', sorted(point_image), [(0, 0), (0, 5), (0, 8), (0, 22), (2, 6)])

    def label(a):
        w = local.val(a)
        assert w is not None
        normalized = local.mul(a, local.power(local.PI, -w))
        residue = local.residue(normalized)
        return dict(valuation=w, normalized_residue=residue, label=32*(w % 2)+cosets[residue])

    def lm(a, b):
        return 32*((a//32) ^ (b//32))+unit_table[a % 32][b % 32]

    def canonical(pair):
        orbit = sorted((lm(pair[0], s), lm(pair[1], s)) for s in scalar_labels)
        return min(orbit), orbit

    alpha = tuple(map(Q, source['field']['alpha_approximation']))
    r = tuple(map(Q, source['field']['r']))
    check('exact r square identity', local.mul(r, r), local.scale(local.sub(local.PI, local.ONE), 2))
    check('alpha residual valuation', local.val(local.sub(local.mul(alpha, alpha), local.add(local.ONE, local.scale(r, 4)))), 24)
    local_gens = [
        (alpha, local.neg(alpha)),
        (local.sub(local.ONE, alpha), local.add(local.ONE, alpha)),
        (local.add(local.ONE, alpha), local.sub(local.ONE, alpha)),
    ]
    gen_rows = []
    for name, pair in zip(('theta', '1-theta', '1+theta'), local_gens):
        components = [label(a) for a in pair]
        margins = [20-row['valuation'] for row in components]
        check(name+' strict relative precision', all(m > 8 for m in margins), True)
        gen_rows.append(dict(name=name, approximate_components=pair, components=components,
                             relative_error_lower_bounds=margins, required_strictly_above=8))

    one = tuple(map(Q, [1]+[0]*7))
    gens = [tuple(map(Q, a)) for a in ([0, 1]+[0]*6, [1, -1]+[0]*6, [1, 1]+[0]*6)]
    # u=275 theta is integral: 275^8*(F(u/275)/275) is monic.
    integral_equation = [F[i]*275**(7-i) for i in range(8)]+[1]
    check('integral monic equation coefficients', all(isinstance(x, int) for x in integral_equation), True)
    gen_norms = [gnorm(a) for a in gens]
    check('generator exact full norms', [x['norm'] for x in gen_norms], [Q(243, 275), Q(1024, 275), Q(1024, 275)])
    rows = []
    for abc in product(range(2), repeat=3):
        element = one
        pair = (0, 0)
        for bit, gen, lgen in zip(abc, gens, gen_rows):
            if bit:
                element = gmul(element, gen)
                pair = tuple(lm(pair[i], lgen['components'][i]['label']) for i in range(2))
        nr = gnorm(element)
        expected = Q(1)
        for bit, gn in zip(abc, gen_norms):
            expected *= gn['norm']**bit
        check('norm multiplicativity '+str(abc), nr['norm'], expected)
        fac = factor(nr['norm'])
        check('nonzero full norm '+str(abc), nr['norm'] != 0, True)
        check('support norm remainder '+str(abc), [fac['numerator_remainder'], fac['denominator_remainder']], [1, 1])
        # degree <=3, so 275^d delta is an integer polynomial in u.
        degree = max(i for i, c in enumerate(element) if c)
        integral_coordinates = [c*275**(degree-i) for i, c in enumerate(element[:degree+1])]
        check('cleared integral expression '+str(abc), all(c.denominator == 1 for c in integral_coordinates), True)
        quotient, orbit = canonical(pair)
        eligible = fac['square']
        rows.append(dict(exponents=abc, coordinates=element,
                         clearing_denominator=275**degree, integral_u_coordinates=integral_coordinates,
                         norm_evidence=nr, norm_factorization=fac, supported=True,
                         global_norm_admissible=eligible, raw_local_labels=pair,
                         common_scalar_orbit=orbit, quotient=quotient,
                         in_two_adic_point_image=(quotient in point_image) if eligible else None))
    eligible_rows = [row for row in rows if row['global_norm_admissible']]
    rejected = [row['exponents'] for row in eligible_rows if not row['in_two_adic_point_image']]
    check('complete family size', len(rows), 8)
    check('eligible exponent vectors', [row['exponents'] for row in eligible_rows], [(0, 0, 0), (0, 1, 1)])
    exact_delta = local.scale(r, -4)
    exact_label = label(exact_delta)
    delta_row = next(row for row in rows if row['exponents'] == (0, 1, 1))
    check('exact diagonal delta agrees with generator product labels', delta_row['raw_local_labels'], (exact_label['label'],)*2)
    collisions = []
    for i, row in enumerate(rows):
        for other in rows[:i]:
            if row['quotient'] == other['quotient']:
                collisions.append([other['exponents'], row['exponents']])
    failures = [c['name'] for c in checks if not c['passed']]
    cert = dict(input=dict(F=F, leading_coefficient_G=3025, degree=8, support=S,
                           integral_generator='u=275 theta', integral_equation=integral_equation),
                local_input=dict(path=SOURCE.name, sha256=sha256(SOURCE.read_bytes()).hexdigest()),
                generator_norms=gen_norms, local_generators=gen_rows,
                exact_diagonal_delta=dict(expression='1-theta^2=-4r in both factors',
                                          components=exact_delta, square_evidence=exact_label),
                rows=rows, local_collisions=collisions, rejected_exponent_vectors=rejected,
                counts=dict(rows=8, support_certified=8, norm_admissible=len(eligible_rows), rejected=len(rejected)),
                checks=checks, failures=failures,
                limitations=['No supported-group completeness', 'No simultaneous local survival',
                             'No rational-point completeness', 'No integer exclusion', 'Independent critical audit pending'])
    OUT.write_text(json.dumps(local.clean(cert), indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks), failures=failures, counts=cert['counts'],
                          rejected_exponent_vectors=rejected,
                          relative_precision_minimum=min(min(g['relative_error_lower_bounds']) for g in gen_rows),
                          required_strictly_above=8, path=str(OUT))))
    for row in rows:
        print(''.join(map(str, row['exponents'])), 'N='+str(row['norm_evidence']['norm']),
              'support=certified', 'norm_square='+str(row['global_norm_admissible']),
              'local='+str(row['quotient']), 'point_image='+str(row['in_two_adic_point_image']))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
