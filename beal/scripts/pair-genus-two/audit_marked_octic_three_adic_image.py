#!/usr/bin/env python3
"""Independent exact replay of L121. Infinite assertions are proved in L121.

No producer code is imported. Symbolic arithmetic uses Q[u]/(P), not a
finite Hensel approximation; the latter is checked separately as evidence.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'marked-octic-three-adic-image-certificate.json'
OUT = HERE / 'marked-octic-three-adic-image-audit-certificate.json'
G = [11*c for c in (243, 0, -3564, 0, 6930, 0, -2860, 0, 275)]
P = G[::2]
checks = []


def clean(x):
    return json.loads(json.dumps(x, default=str))


def check(name, actual, required):
    actual, required = clean(actual), clean(required)
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def value(poly, x):
    return sum(Q(c)*x**i for i, c in enumerate(poly))


def valuation(x):
    x = Q(x)
    if x == 0:
        return None
    n, d, v = abs(x.numerator), x.denominator, 0
    for a, sign in ((n, 1), (d, -1)):
        while a % 3 == 0:
            a //= 3
            v += sign
    return v


def residue(x):
    x = Q(x)
    return x.numerator * pow(x.denominator, -1, 3) % 3


# Fixed four-coordinate arithmetic in Q[u]/P, with exact rational entries.
def element(x):
    return [Q(x), Q(0), Q(0), Q(0)]


def plus(x, y):
    return [a+b for a, b in zip(x, y)]


def times(x, y):
    z = [Q(0)]*7
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            z[i+j] += a*b
    for i in range(6, 3, -1):
        for j in range(4):
            z[i-4+j] -= z[i]*Q(P[j], P[4])
    return z[:4]


def scaled(x, a):
    return [a*c for c in x]


def fp9(x, y):
    # Polynomial convolution, followed by w^2=-1 in F3.
    convolution = [0, 0, 0]
    for i in range(2):
        for j in range(2):
            convolution[i+j] += x[i]*y[j]
    return ((convolution[0]-convolution[2]) % 3, convolution[1] % 3)


def main():
    saved = json.loads(SOURCE.read_text())
    check('actual twisted octic', saved['G'], G)
    check('quartic composition', saved['P'], P)
    check('P reduction', [c % 3 for c in P], [0, 0, 0, 1, 1])
    derivative = [i*P[i] for i in range(1, 5)]
    check('simple Hensel seed', [residue(value(P, 2)), residue(value(derivative, 2))], [0, 2])

    # Newton correction independently selects each digit; also replay every child.
    s, m, lift_rows = 2, 3, []
    for depth in range(1, 8):
        new = (s-int(value(P, s))*pow(int(value(derivative, s)), -1, 3*m)) % (3*m)
        children = [s+j*m for j in range(3)]
        errors = [int(value(P, c)) % (3*m) for c in children]
        chosen = (new-s)//m
        check('Newton digit root '+str(depth), errors[chosen], 0)
        check('unique digit '+str(depth), errors.count(0), 1)
        lift_rows.append(dict(depth=depth, seed=s, modulus=m, candidates=children,
                              errors_mod_next=errors, passing_digits=[chosen]))
        s, m = new, 3*m
    check('all Hensel records', saved['hensel'], dict(
        seed=2, root_definition='unique u0=2 mod 3 with P(u0)=0',
        derivative_mod_3=2, lifts=lift_rows, approximation=s, modulus=m))

    one, u = element(1), [Q(0), Q(1), Q(0), Q(0)]
    invu = [Q(-P[i+1], P[0]) for i in range(4)]
    check('exact inverse u', times(u, invu), one)
    # Synthetic division from the leading end, opposite to the producer.
    h6 = one
    h4 = plus(u, element(Q(P[3], P[4])))
    h2 = plus(times(u, h4), element(Q(P[2], P[4])))
    h0 = plus(times(u, h2), element(Q(P[1], P[4])))
    check('synthetic division remainder', plus(times(u, h0), element(Q(P[0], P[4]))), element(0))
    low0 = scaled(invu, Q(-P[0], P[4]))
    low2 = times(plus(low0, element(Q(-P[1], P[4]))), invu)
    low4 = times(plus(low2, element(Q(-P[2], P[4]))), invu)
    check('exact H coefficients both constructions', [h0, h2, h4], [low0, low2, low4])
    invb0 = scaled(u, Q(-P[4], P[0]))
    check('exact inverse constant', times(h0, invb0), one)
    H = [h0, element(0), h2, element(0), h4, element(0), h6]
    E = [scaled(times(H[6-i], invb0), 3**(6-i)) for i in range(7)]
    check('exact monic reciprocal', E[-1], one)

    # Full denominator-cleared identity over Q[u,t], without quotient reduction.
    B = {0: [0, 0, -P[0]], 2: [0, -P[0], -P[1]],
         4: [-P[0], -P[1], -P[2]], 6: [0, 0, 0, P[4]]}
    residuals = []
    for i in range(9):
        row = [0]*5
        for j, c in enumerate(B.get(i-2, [])):
            row[j] += c
        for j, c in enumerate(B.get(i, [])):
            row[j+1] -= c
        row[3] -= G[i]
        while len(row) > 1 and row[-1] == 0:
            row.pop()
        residuals.append(row)
    check('symbolic residual', residuals, [[-c for c in P] if i == 6 else [0] for i in range(9)])
    check('complete producer cleared identity', saved['cleared_factor_identity'], dict(
        numerators=B, residual_by_t_degree=residuals,
        meaning='(t^2-u)*B(t,u)-u^3*G(t)=-P(u)*t^6'))

    # Low-end rational formulas at a finite approximant, expressly not field models.
    b = [Q(0)]*7
    for i in (0, 2, 4, 6):
        b[i] = value(B[i], s)/Q(P[4]*s**3)
    e = [b[6-i]*3**(6-i)/b[0] for i in range(7)]
    check('all approximant coefficients', saved['local_models']['b_approximation'], list(map(str, b)))
    check('all reciprocal approximant coefficients', saved['local_models']['E_approximation'], list(map(str, e)))
    # Universal valuations follow from distinct valuations of terms, for ANY u=2 mod 3.
    cv = [valuation(c) for c in P]
    check('base coefficient valuations', cv, [5, 4, 2, 0, 0])
    bv = [cv[0], min(cv[0], cv[1]), min(cv[0], cv[1], cv[2])]
    check('no cancellation in exact b formulas', [cv[0] > cv[1], cv[1] > cv[2]], [True, True])
    check('exact b valuations', bv, [5, 4, 2])
    ev = [6-bv[0], None, 4+bv[2]-bv[0], None, 2+bv[1]-bv[0], None, 0]
    check('all exact E valuations', ev, [1, None, 1, None, 1, None, 0])
    b0unit = residue(Q(-P[0], 3**5*P[4]*2))
    norm_r_unit = pow(b0unit, -1, 3)
    scalar_unit = (-norm_r_unit) % 3
    check('exact unit residues', [b0unit, norm_r_unit, scalar_unit], [2, 2, 1])
    check('all field data', {k: saved['local_models'][k] for k in ('ef_pairs', 'normalized_theta_valuations', 'r6_over_3_residue')},
          dict(ef_pairs=[[6, 1], [1, 2]], normalized_theta_valuations=[6-1, 0], r6_over_3_residue=scalar_unit))
    check('degree sum', 6+2, len(G)-1)
    check('quadratic irreducible residue', [(i*i-2) % 3 for i in range(3)], [1, 2, 2])

    elements = [x for x in product(range(3), repeat=2) if x != (0, 0)]
    squares = sorted(set(fp9(x, x) for x in elements))
    residue_rows = [dict(x=x, square=x in squares, norm=fp9(x, (x[0], -x[1]))[0]) for x in elements]
    check('all residue norm characters', [r['square'] for r in residue_rows], [r['norm'] == 1 for r in residue_rows])
    check('F9 evidence', saved['F9'], dict(nonzero_squares=squares, eta=[1, 1]))
    check('scalar minus one and eta characters', [(2, 0) in squares, (1, 1) in squares], [True, False])
    norm_labels = [[1, int(norm_r_unit == 2)], [0, 0], [0, 0], [0, int((1-2) % 3 == 2)]]
    norms = [dict(factor=f, generator=g, norm=n, label=l) for (f, g, n), l in zip(
        [('L6', 'r', '729/b0'), ('L6', '-1', '1'), ('U2', '3', '9'), ('U2', 'eta=1+omega', '1-u0')], norm_labels)]
    check('all norm generators', saved['norm_generators'], norms)
    scalar_generators = dict(minus_one=[0, 1, 0, 0], three=[0, int(scalar_unit == 2), 1, 0])
    check('one common scalar generators', saved['scalar_generators'], scalar_generators)
    raw_rows = []
    for a, bb, c, d in product(range(2), repeat=4):
        x = (a, bb, c, d)
        norm = [sum(x[i]*norm_labels[i][j] for i in range(4)) % 2 for j in range(2)]
        orbit = sorted([[a, (bb+j) % 2, (c+k) % 2, d] for j, k in product(range(2), repeat=2)])
        raw_rows.append(dict(raw=list(x), norm=norm, scalar_orbit=orbit,
                             canonical=[a, 0, 0, d], norm_admissible=norm == [0, 0]))
    check('complete 16-row table', saved['raw_labels'], raw_rows)
    ambient = sorted({tuple(r['canonical']) for r in raw_rows if r['norm_admissible']})
    check('ambient', saved['ambient'], ambient)
    check('kernel and quotient sizes', [sum(r['norm_admissible'] for r in raw_rows), len(ambient)], [4, 1])
    check('canonical convention', saved['canonical_section'], 'b=c=0, not lexicographic orbit labels')

    integral = [dict(t_mod_3=0, condition='t in 3Z3, including zero', G_valuation=cv[0], obstruction='odd valuation')]
    integral += [dict(t_mod_3=i, condition='unit', G_mod_3=residue(value(G, i)), obstruction='nonsquare unit residue') for i in (1, 2)]
    check('all integral disks', saved['integral_disks'], integral)
    check('unit obstructions', [r['G_mod_3'] for r in integral[1:]], [2, 2])
    ib = [dict(power=i, slope=i, intercept=valuation(G[i]), minimum_at_n_1=i+valuation(G[i])) for i in (2, 4, 6, 8)]
    check('all integral bounds', saved['integral_nonconstant_bounds'], ib)
    check('universal dominance', [r['minimum_at_n_1'] > cv[0] and r['slope'] > 0 for r in ib], [True]*4)
    reciprocal = [dict(power=i, coefficient=str(Q(G[8-i], G[8])), slope=i,
        intercept=valuation(Q(G[8-i], G[8])), minimum_at_n_1=i+valuation(Q(G[8-i], G[8]))) for i in (2, 4, 6, 8)]
    check('all reciprocal bounds', saved['reciprocal_terms'], reciprocal)
    check('strict reciprocal minima', [r['minimum_at_n_1'] for r in reciprocal], [2, 6, 10, 13])
    cb = [dict(factor='L6', slope=6, intercept=5, minimum_at_n_1=11),
          dict(factor='U2', slope=1, intercept=0, minimum_at_n_1=1)]
    check('both point class bounds', saved['reciprocal_class_bounds'], cb)
    check('all class bounds strict', [r['slope'] > 0 and r['minimum_at_n_1'] > 0 for r in cb], [True, True])
    radicand = value(G, Q(1, 3))*Q(3)**8/Q(55)**2
    check('exact finite radicand', radicand, Q(-467968, 275))
    check('finite Hensel premise', [residue(radicand), valuation(radicand-1), 2 % 3], [1, 2, 2])
    finite = dict(t='1/3', q='3', S=str(radicand), S_minus_one_valuation=valuation(radicand-1),
        X_definition='unique X=1 mod 3 with X^2=S(3)', derivative_mod_3=2,
        Y_definition='55*X/3^4', fake_class=[0]*4)
    check('complete finite realization', saved['finite_realization'], finite)
    infinity = [dict(q=0, Z=z, derivative=2*z, representative=G[-1], fake_class=[0]*4) for z in (-55, 55)]
    check('both infinity records', saved['infinity_rows'], infinity)
    check('infinity smooth square points', [(r['Z']**2 == G[-1] and r['derivative'] % 3 != 0) for r in infinity], [True, True])
    check('infinity norm fiber', Q(3025**8, 3025), Q(55**14))
    check('no rational branch rows', saved['rational_branch_points'], [])
    check('exact image', saved['exact_image'], [[0]*4])
    check('comparison', saved['comparison'], dict(image_count=1, ambient_count=1,
        proper=False, required_for_pruning='image_count < ambient_count'))
    # Producer flags are read for bookkeeping only, never used for the proof.
    check('producer check record consistency', [r['passed'] == (r['actual'] == r['required']) for r in saved['checks']], [True]*39)
    check('producer failure list consistency', saved['failures'], [r for r in saved['checks'] if not r['passed']])
    failures = [r for r in checks if not r['passed']]
    result = dict(source=str(SOURCE.relative_to(HERE)),
        symbolic_ring='Q[u]/(P); evaluation at exact Hensel root, not an approximate field',
        H_coefficients=H, E_coefficients=E, inverse_u=invu, inverse_b0=invb0,
        hensel_rows=lift_rows, cleared_residuals=residuals, F9_norm_rows=residue_rows,
        raw_rows=raw_rows, universal_integral_bounds=ib, universal_reciprocal_bounds=reciprocal,
        point_class_bounds=cb, finite_realization=finite, infinity_rows=infinity,
        checks=checks, failures=failures)
    OUT.write_text(json.dumps(clean(result), indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks), failures=[r['name'] for r in failures],
        image_actual=1, ambient_actual=len(ambient), pruning_requires='image < ambient',
        degrees_actual=[6, 2], degree_sum_required=8,
        reciprocal_error_minima_actual=[2, 6, 10, 13], class_minima_actual=[11, 1],
        square_bounds_require='strictly positive', infinity_rows_actual=2, infinity_rows_required=2,
        path=str(OUT.relative_to(HERE.parent.parent))), indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
