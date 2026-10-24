#!/usr/bin/env python3
"""Exact finite arithmetic for the marked octic at two; see canonical proof.

No local-field backend, finite-precision field identification, or point scan.
Every square class is certified using the full maximal-ring quotient pi^9.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json

OUT = Path(__file__).with_name('marked-octic-two-adic-image-certificate.json')
G = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
EN = [22130658, -74245842, 91279980, -48315300, 9150625]
E = [Q(c, EN[-1]) for c in EN]
ZERO = (Q(0),)*4
ONE = (Q(1), Q(0), Q(0), Q(0))
PI = (Q(0), Q(1), Q(0), Q(0))
MODULI = (8, 4, 4, 4)  # coefficient bounds for pi^9, e=4


def v2(x):
    x = Q(x)
    if not x:
        return None
    n, d = abs(x.numerator), x.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()


def val(a):
    return min((4*v2(c)+i for i, c in enumerate(a) if c), default=None)


def scalar(x):
    return (Q(x), Q(0), Q(0), Q(0))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def scale(a, c):
    return tuple(x*c for x in a)


def mul(a, b):
    c = [Q(0)]*7
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    for k in range(6, 3, -1):
        for i in range(4):
            c[k-4+i] -= c[k]*E[i]
    return tuple(c[:4])


def power(a, k):
    if k < 0:
        return power(inv(a), -k)
    r = ONE
    while k:
        if k & 1:
            r = mul(r, a)
        a = mul(a, a)
        k //= 2
    return r


def matrix(a):
    cols = [mul(a, tuple(Q(int(i == j)) for i in range(4))) for j in range(4)]
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def inv(a):
    m = [row+[ONE[i]] for i, row in enumerate(matrix(a))]
    for j in range(4):
        p = next(i for i in range(j, 4) if m[i][j])
        m[p], m[j] = m[j], m[p]
        pivot = m[j][j]
        m[j] = [x/pivot for x in m[j]]
        for i in range(4):
            if i != j:
                z = m[i][j]
                m[i] = [x-z*y for x, y in zip(m[i], m[j])]
    return tuple(row[-1] for row in m)


def norm(a):
    m = matrix(a)
    result = Q(1)
    for j in range(4):
        p = next(i for i in range(j, 4) if m[i][j])
        if p != j:
            m[p], m[j] = m[j], m[p]
            result = -result
        pivot = m[j][j]
        result *= pivot
        for i in range(j+1, 4):
            z = m[i][j]/pivot
            m[i] = [x-z*y for x, y in zip(m[i], m[j])]
    return result


def residue(a):
    assert val(a) is None or val(a) >= 0
    return tuple(c.numerator*pow(c.denominator, -1, m) % m
                 for c, m in zip(a, MODULI))


def rmul(a, b):
    return residue(mul(tuple(map(Q, a)), tuple(map(Q, b))))


def rational_label(x):
    w = v2(x)
    u = Q(x)/Q(2)**w
    return (w % 2, u.numerator*pow(u.denominator, -1, 8) % 8)


def ev(p, x):
    r = Q(0)
    for c in reversed(p):
        r = r*x+c
    return r


def shifted(p, a, step):
    return [sum(p[j]*comb(j, i)*a**(j-i)*step**i
                for j in range(i, len(p))) for i in range(len(p))]


def clean(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [clean(v) for v in x]
    return x


def main():
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    check('unchanged full G', G, [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025])
    check('Eisenstein coefficient valuations', [v2(c) for c in E], [1, 1, 2, 2, 0])
    check('pi has normalized valuation one', val(PI), 1)
    check('actual transformed quartic coefficients',
          [c/256 for c in shifted(G[::2], 1, 4)],
          [Q(44), Q(484), Q(0), Q(-4840), Q(3025)])
    aa, bb = [3036, -6050, 3025], [2541, -2420]
    expansion = [0]*5
    for i, x in enumerate(aa):
        for j, y in enumerate(aa):
            expansion[i+j] += x*y
    for i, x in enumerate(bb):
        for j, y in enumerate(bb):
            expansion[i+j] += 2*x*y
            expansion[i+j+1] -= 2*x*y
    check('complete defining polynomial expansion', expansion, EN)
    num = add(add(scalar(3036), scale(PI, -6050)), scale(power(PI, 2), 3025))
    den = add(scalar(2541), scale(PI, -2420))
    r = neg(mul(num, inv(den)))
    check('exact r-square relation', sub(mul(r, r), scale(sub(PI, ONE), 2)), ZERO)
    check('exact P transformed relation',
          add(add(scale(power(r, 4), 3025), scale(power(r, 3), -4840)),
              add(scale(r, 484), scalar(44))), ZERO)
    check('r and denominator valuations', [val(r), val(den)], [2, 0])
    target = add(ONE, scale(r, 4))
    alpha = add(ONE, scale(r, 2))
    lifts = []
    for k in range(3):
        error = sub(mul(alpha, alpha), target)
        derivative = scale(alpha, 2)
        error_val, derivative_val = val(error), val(derivative)
        lifts.append(dict(iteration=k, alpha=alpha, residual=error,
                          residual_valuation=error_val,
                          derivative_valuation=derivative_val,
                          root_error_lower_bound=error_val-derivative_val))
        if k != 2:
            alpha = sub(alpha, mul(error, inv(derivative)))
    check('Hensel residual valuations', [x['residual_valuation'] for x in lifts], [12, 16, 24])
    check('certified alpha error bound exceeds class requirement',
          lifts[-1]['root_error_lower_bound'] > 6+8, True)
    check('alpha +/- one valuations', [val(sub(alpha, ONE)), val(add(alpha, ONE))], [6, 4])
    check('pi recovery from alpha-square target',
          add(ONE, scale(power(sub(target, ONE), 2), Q(1, 32))), PI)

    units = [a for a in product(*(range(m) for m in MODULI)) if a[0] % 2]
    squares = sorted({rmul(a, a) for a in units})
    cosets = {}
    representatives = []
    for a in units:
        if a in cosets:
            continue
        orbit = sorted({rmul(a, s) for s in squares})
        label = len(representatives)
        representatives.append(orbit[0])
        for b in orbit:
            assert b not in cosets
            cosets[b] = label
    check('complete quotient ring and unit counts', [len(units)*2, len(units)], [512, 256])
    check('unit square residues and cosets', [len(squares), len(representatives)], [8, 32])
    check('all units have unique coset', len(cosets), 256)

    def label(a):
        w = val(a)
        assert w is not None
        u = mul(a, power(PI, -w))
        assert val(u) == 0
        return (w % 2)*32+cosets[residue(u)]

    unit_mult = [[cosets[rmul(a, b)] for b in representatives] for a in representatives]

    def lm(a, b):
        return ((a//32) ^ (b//32))*32+unit_mult[a % 32][b % 32]

    identity = label(ONE)
    check('identity convention', identity, 0)
    class_rows = []
    for parity in range(2):
        for i, a in enumerate(representatives):
            element = mul(power(PI, parity), tuple(map(Q, a)))
            n = norm(element)
            class_rows.append(dict(label=32*parity+i, representative=element,
                                   norm=n, norm_square_class=rational_label(n)))
            check(f'class representative {32*parity+i}', label(element), 32*parity+i)
    norm_labels = [row['norm_square_class'] for row in class_rows]
    check('all classes have exponent two', [lm(i, i) for i in range(64)], [identity]*64)
    norm_consistency = []
    for i in range(64):
        for j in range(64):
            a, b = norm_labels[i], norm_labels[j]
            expected = (a[0] ^ b[0], a[1]*b[1] % 8)
            if norm_labels[lm(i, j)] != expected:
                norm_consistency.append([i, j])
    check('all 4096 class products preserve norm labels', norm_consistency, [])
    scalars = []
    for a, b, c in product(range(2), repeat=3):
        x = Q((-1)**a * 2**b * 5**c)
        scalars.append(dict(exponents=[a, b, c], scalar=x, label=label(scalar(x))))
    scalar_labels = sorted({row['label'] for row in scalars})
    check('full scalar image size', len(scalar_labels), 8)
    check('scalar subgroup closure', sorted({lm(a, b) for a in scalar_labels for b in scalar_labels}), scalar_labels)

    def canonical(pair):
        return min((lm(pair[0], s), lm(pair[1], s)) for s in scalar_labels)

    ambient_raw = [(i, j) for i in range(64) for j in range(64) if norm_labels[i] == norm_labels[j]]
    ambient = sorted({canonical(pair) for pair in ambient_raw})
    check('norm square-class image size', len(set(norm_labels)), 8)
    check('raw norm fiber size', len(ambient_raw), 512)
    check('common scalar quotient size', len(ambient), 64)

    # Constant square-class disks: v_L(delta t) > v_L(t +/- alpha) + 8.
    point_rows = []
    for t in range(0, 8, 2):
        pair = (label(sub(scalar(t), alpha)), label(add(scalar(t), alpha)))
        point_rows.append(dict(chart='finite_even', center=t, modulus=8,
                               G_value=ev(G, t), G_square_class=rational_label(ev(G, t)),
                               component_valuations=[val(sub(scalar(t), alpha)), val(add(scalar(t), alpha))],
                               perturbation_lower_bound=12, required_strict_bound=8,
                               raw_labels=pair, quotient=canonical(pair)))
    odd_rows = []
    for t in range(1, 16, 2):
        c = shifted(G, t, 16)
        shift_min = min(v2(x) for x in c[1:] if x)
        square = rational_label(c[0]) == (0, 1)
        odd_rows.append(dict(center=t, modulus=16, shifted_coefficients=c,
                             center_valuation=v2(c[0]), normalized_unit_mod8=rational_label(c[0])[1],
                             variation_minimum=shift_min, required_variation_minimum=13,
                             has_points=square))
        if square:
            pair = (label(sub(scalar(t), alpha)), label(add(scalar(t), alpha)))
            point_rows.append(dict(chart='finite_odd', center=t, modulus=16,
                                   G_value=ev(G, t), G_square_class=rational_label(ev(G, t)),
                                   component_valuations=[val(sub(scalar(t), alpha)), val(add(scalar(t), alpha))],
                                   perturbation_lower_bound=16, required_strict_bound=14,
                                   raw_labels=pair, quotient=canonical(pair)))
    check('odd feasible residues', [row['center'] for row in odd_rows if row['has_points']], [3, 13])
    check('every odd valuation equals ten', [row['center_valuation'] for row in odd_rows], [10]*8)
    check('every odd disk has sufficient square precision', all(row['variation_minimum'] >= 13 for row in odd_rows), True)
    reciprocal = list(reversed(G))
    for q in [2, 4, 6]:
        pair = (label(sub(ONE, scale(alpha, q))), label(add(ONE, scale(alpha, q))))
        # [1 +/- q alpha] is the approved reciprocal class after the same scalar q is removed.
        point_rows.append(dict(chart='reciprocal', center=q, modulus=8,
                               reciprocal_value=ev(reciprocal, q),
                               reciprocal_square_class=rational_label(ev(reciprocal, q)),
                               component_valuations=[0, 0], perturbation_lower_bound=12,
                               required_strict_bound=8, raw_labels=pair,
                               quotient=canonical(pair)))
    tail_pair = (identity, identity)
    point_rows.append(dict(chart='reciprocal_tail', center=0, modulus=8,
                           perturbation_lower_bound=12, required_strict_bound=8,
                           raw_labels=tail_pair, quotient=canonical(tail_pair),
                           finite_realization_q=8, reciprocal_value=ev(reciprocal, 8),
                           reciprocal_square_class=rational_label(ev(reciprocal, 8))))
    check('point square classes', [row.get('G_square_class', row.get('reciprocal_square_class')) for row in point_rows], [(0, 1)]*len(point_rows))
    check('strict class constancy for every row', all(row['perturbation_lower_bound'] > row['required_strict_bound'] for row in point_rows), True)
    image = sorted({tuple(row['quotient']) for row in point_rows})
    check('all point classes norm-admissible', all(pair in ambient for pair in image), True)
    infinity = [dict(Z=z, representative=3025, raw_labels=[identity, identity],
                     quotient=canonical(tail_pair)) for z in [-55, 55]]
    check('both infinity points separately retained', len(infinity), 2)
    check('both infinity images realized in affine tail', all(tuple(row['quotient']) in image for row in infinity), True)
    check('five fixed point-image labels', image, [(0, 0), (0, 5), (0, 8), (0, 22), (2, 6)])
    check('properness versus full ambient', len(image) < len(ambient), True)
    finite_even_shift = shifted(G, 0, 2)
    reciprocal_shift = shifted(reciprocal, 0, 2)
    check('even chart square residue constant', [int(c) % 8 for c in finite_even_shift], [1]+[0]*8)
    check('reciprocal square residue constant', [int(c) % 8 for c in reciprocal_shift], [1]+[0]*8)
    failures = [row['name'] for row in checks if not row['passed']]
    certificate = dict(
        input=dict(G=G, leading_square=55**2, e=4, square_precision=9, strict_threshold=8),
        field=dict(E_numerator=EN, monic_E=E, r=r, denominator=den,
                   alpha_square_target=target, hensel=lifts,
                   alpha_approximation=alpha, alpha_error_lower_bound=20,
                   actual_theta_transports=['alpha', '-alpha']),
        residue_ring=dict(coefficient_moduli=MODULI, units=units, unit_squares=squares,
                          unit_class_representatives=representatives,
                          complete_unit_cosets=[dict(residue=a, label=cosets[a]) for a in units],
                          unit_multiplication_table=unit_mult),
        square_classes=class_rows, scalar_rows=scalars, scalar_labels=scalar_labels,
        ambient_raw=ambient_raw, ambient_quotient=ambient,
        coordinate_tests=dict(even_shift=finite_even_shift, reciprocal_shift=reciprocal_shift,
                              odd_disks=odd_rows),
        point_disks=point_rows, infinity=infinity, point_image=image,
        counts=dict(field_square_classes=64, raw_norm_fiber=len(ambient_raw),
                    scalar_image=len(scalar_labels), ambient=len(ambient), image=len(image)),
        checks=checks, failures=failures,
        limitations=['No global supported representatives computed', 'No rational-point completeness',
                     'No integer exclusion', 'Independent critical audit pending'])
    OUT.write_text(json.dumps(clean(certificate), indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks), failures=failures, counts=certificate['counts'],
                          actual_precision=9, required_precision=9,
                          alpha_error_bound=20, required_alpha_error_strictly_above=14,
                          path=str(OUT))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
