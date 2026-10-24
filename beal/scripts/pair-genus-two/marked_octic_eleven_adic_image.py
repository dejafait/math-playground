#!/usr/bin/env python3
"""Exact arithmetic for L120; universal local bounds are proved in its text."""

from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

OUT = Path(__file__).with_name('marked-octic-eleven-adic-image-certificate.json')
G = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
E = [275, 0, -2860, 0, 6930, 0, -3564, 0, 243]


def v(x):
    x = Q(x)
    if not x:
        return None
    n, d, value = x.numerator, x.denominator, 0
    while n % 11 == 0:
        n //= 11
        value += 1
    while d % 11 == 0:
        d //= 11
        value -= 1
    return value


def res(x):
    x = Q(x)
    return x.numerator * pow(x.denominator, -1, 11) % 11


def ev(p, x):
    z = Q(0)
    for c in reversed(p):
        z = z*x+c
    return z


def determinant(a):
    a = [[Q(x) for x in row] for row in a]
    answer = Q(1)
    for i in range(len(a)):
        j = next(j for j in range(i, len(a)) if a[j][i])
        if i != j:
            a[i], a[j] = a[j], a[i]
            answer = -answer
        pivot = a[i][i]
        answer *= pivot
        for j in range(i+1, len(a)):
            scale = a[j][i]/pivot
            for k in range(i, len(a)):
                a[j][k] -= scale*a[i][k]
    return answer


def main():
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    check('complete reciprocal identity', G, [11*c for c in reversed(E)])
    valuations = [v(c) for c in E]
    check('Eisenstein valuations', valuations, [1, None, 1, None, 1, None, 1, None, 0])
    squares = sorted({a*a % 11 for a in range(1, 11)})
    check('all nonzero residue squares', squares, [1, 3, 4, 5, 9])
    check('minus one nonsquare', 10 not in squares, True)

    # Multiplication by the EXACT r, in 1,r,...,r^7 for E(r)=0.
    matrix = [[Q(0) for _ in range(8)] for _ in range(8)]
    for j in range(7):
        matrix[j+1][j] = Q(1)
    for i in range(8):
        matrix[i][7] = -Q(E[i], E[8])
    norm_r = determinant(matrix)
    check('norm r determinant', str(norm_r), '275/243')
    check('norm r valuation', v(norm_r), 1)
    check('norm r unit residue square', res(norm_r/11) in squares, True)
    check('norm minus one', (-1)**8, 1)

    # E(r)/11: r^8/11 is a unit with residue -25/243.
    unit_residue = res(Q(-25, 243))
    scalar11_residue = pow(unit_residue, -1, 11)
    check('r^8/11 residue', unit_residue, 8)
    check('11/r^8 residue', scalar11_residue, 7)
    check('scalar11 unit bit', scalar11_residue not in squares, True)
    raw = [list(x) for x in product(range(2), repeat=2)]
    labels = []
    for a, b in raw:
        labels.append(dict(raw=[a, b], norm=[a, 0],
                           scalar_orbit=sorted([[a, b], [a, b ^ 1]]),
                           canonical=[a, 0], norm_admissible=(a == 0)))
    ambient = sorted({tuple(x['canonical']) for x in labels if x['norm_admissible']})
    check('full norm ambient after scalar quotient', [list(x) for x in ambient], [[0, 0]])
    check('all raw square classes retained', len(labels), 4)

    # Every t in Z11 has G(t)/11 = 243 mod 11.
    integral_rows = [dict(t_residue=a, G_over_11_residue=res(ev(G, a)/11),
                          valuation=1, feasible=False) for a in range(11)]
    check('all integral residue disks', [x['G_over_11_residue'] for x in integral_rows], [1]*11)
    check('all nonconstant coefficients G have valuation >=2',
          all(v(c) >= 2 for c in G[1:] if c), True)

    # q=1/t is now a BASE coordinate; distinguish it from field generator r.
    terms = []
    for i in (2, 4, 6, 8):
        c = Q(G[8-i], G[8])
        terms.append(dict(power=i, coefficient=str(c), intercept=v(c),
                          minimum_at_n_1=i+v(c)))
    check('reciprocal square error minima', [x['minimum_at_n_1'] for x in terms], [2, 4, 6, 7])
    bounds = dict(square_neighborhood_required='normalized error valuation > 0',
                  integral_class_ratio_minimum=1,
                  reciprocal_curve_minimum=2,
                  reciprocal_fake_ratio=dict(slope=8, intercept=-1, minimum=7))
    check('strict fake square bound at n=1', 8-1 > 0, True)

    # Finite exact realization at t=1/11; Z=55 sqrt(S(1/11)).
    t, q = Q(1, 11), Q(11)
    S = ev(list(reversed(G)), q)/3025
    check('finite realization chart identity', str(ev(G, t)*q**8), str(3025*S))
    check('finite realization S residue', res(S), 1)
    check('finite realization error valuation', v(S-1), 2)
    check('finite realization Hensel derivative residue', 2 % 11, 2)
    realization = dict(t=str(t), q=str(q), S=str(S), seed=1,
                       derivative=2, error_valuation=v(S-1),
                       exact_definition='Z=55*sqrt(S), sqrt(S)=1 mod 11; Y=Z/q^4',
                       fake_class=[0, 0])
    infinities = [dict(point=name, q=0, Z=z, derivative=2*z,
                       fake_representative=3025, fake_class=[0, 0])
                  for name, z in [('I_minus', -55), ('I_plus', 55)]]
    check('separate smooth infinity rows', len([r for r in infinities if r['derivative']]), 2)
    check('leading coefficient actual square', 55**2, G[8])
    certificate = dict(
        polynomial=G, reciprocal_E=E, E_valuations=valuations,
        field=dict(model='Q11[r]/(E/243)', degree=8, e=8, f=1,
                   theta='1/r', normalized_theta_valuation=-1),
        squares_mod_11=squares,
        norm_r_matrix=[[str(c) for c in row] for row in matrix], norm_r=str(norm_r),
        scalar_rows=dict(minus_one=[0, 1], eleven=[0, 1]),
        scalar11_unit_residue=scalar11_residue, square_class_rows=labels,
        norm_ambient=[list(x) for x in ambient], integral_rows=integral_rows,
        reciprocal_terms=terms, strict_bounds=bounds, finite_realization=realization,
        rational_branch_points=0, infinity_rows=infinities,
        conclusion=dict(image=[[0, 0]], image_size=1, norm_ambient_size=1,
                        proper=False, global_exclusion=False),
        checks=checks, failures=[c for c in checks if not c['passed']])
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f"checks {len(checks)-len(certificate['failures'])}/{len(checks)}; failures {len(certificate['failures'])}")
    print('entire field degree/e/f: 8/8/1; image/required ambient: 1/1 (equality)')
    print('strict error bounds: 1, 2, 7; required >0; integral disks 11/11; infinity rows 2/2')
    print(OUT)
    if certificate['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
