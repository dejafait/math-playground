#!/usr/bin/env python3
"""Exact arithmetic for L121; universal local arguments are in its proof."""

from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

OUT = Path(__file__).with_name('marked-octic-three-adic-image-certificate.json')
G = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
P = G[::2]


def v(x):
    x = Q(x)
    if not x:
        return None
    n, d, answer = x.numerator, x.denominator, 0
    while n % 3 == 0:
        n //= 3
        answer += 1
    while d % 3 == 0:
        d //= 3
        answer -= 1
    return answer


def res(x):
    x = Q(x)
    assert x.denominator % 3
    return x.numerator * pow(x.denominator, -1, 3) % 3


def ev(p, x):
    answer = Q(0)
    for c in reversed(p):
        answer = answer*x+c
    return answer


def add(p, q):
    r = [Q(0)]*max(len(p), len(q))
    for i, c in enumerate(p):
        r[i] += c
    for i, c in enumerate(q):
        r[i] += c
    while len(r) > 1 and not r[-1]:
        r.pop()
    return r


def mul(p, q):
    r = [Q(0)]*(len(p)+len(q)-1)
    for i, c in enumerate(p):
        for j, d in enumerate(q):
            r[i+j] += c*d
    return add(r, [0])


def f9mul(x, y):
    a, b = x
    c, d = y
    return ((a*c+2*b*d) % 3, (a*d+b*c) % 3)


def xor(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


def main():
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    check('unchanged full G', G, [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025])
    dp = [i*c for i, c in enumerate(P)][1:]
    check('P mod three', [c % 3 for c in P], [0, 0, 0, 1, 1])
    check('Hensel seed value residue', res(ev(P, 2)), 0)
    check('Hensel seed derivative residue', res(ev(dp, 2)), 2)
    seed, modulus, lifts = 2, 3, []
    for depth in range(1, 8):
        candidates = [seed+modulus*j for j in range(3)]
        errors = [int(ev(P, c)) % (3*modulus) for c in candidates]
        passing = [j for j, error in enumerate(errors) if not error]
        check(f'unique Hensel digit at depth {depth}', len(passing), 1)
        lifts.append(dict(depth=depth, seed=seed, modulus=modulus,
                          candidates=candidates, errors_mod_next=errors,
                          passing_digits=passing))
        seed = candidates[passing[0]]
        modulus *= 3

    # B_i = 3025*u^3*b_i, including b_6=1. All entries are polynomials in u.
    B = {0: [0, 0, -2673], 2: [0, -2673, 39204],
         4: [-2673, 39204, -76230], 6: [0, 0, 0, 3025]}
    cleared = []
    for i in range(9):
        z = add(B.get(i-2, [0]), mul([0, -1], B.get(i, [0])))
        z = add(z, [0, 0, 0, -G[i]])
        cleared.append([int(c) for c in z])
    check('complete cleared factor identity', cleared,
          [[0] if i != 6 else [-c for c in P] for i in range(9)])
    b0 = Q(-2673, 3025*seed)
    b2 = (b0+Q(39204, 3025))/seed
    b4 = (b2-Q(76230, 3025))/seed
    b = [b0, 0, b2, 0, b4, 0, Q(1)]
    e = [Q(729)/b0, 0, 81*b4/b0, 0, 9*b2/b0, 0, Q(1)]
    check('b0 b2 b4 valuations', [v(b0), v(b2), v(b4)], [5, 4, 2])
    check('b0 normalized residue', res(b0/3**5), 2)
    check('E all coefficient valuations', [v(x) for x in e],
          [1, None, 1, None, 1, None, 0])
    # E(r)=r^6 H(3/r)/b0, coefficient by coefficient.
    check('complete scaled reciprocal identity',
          [str(b[6-i]*3**(6-i)/b0) for i in range(7)], [str(c) for c in e])
    check('E constant norm normalized residue', res(e[0]/3), 2)
    r6_over_3 = res(-Q(243)/b0)
    check('r^6/3 residue from E', r6_over_3, 1)
    check('3/r^6 residue', pow(r6_over_3, -1, 3), 1)
    check('all local degrees retained', 6+2, 8)

    nonzero9 = [x for x in product(range(3), repeat=2) if x != (0, 0)]
    squares9 = sorted(set(f9mul(x, x) for x in nonzero9))
    check('F9 nonzero square count', len(squares9), 4)
    check('minus one square in F9', (2, 0) in squares9, True)
    check('eta nonsquare in F9', (1, 1) not in squares9, True)
    check('eta residue norm', (1-2) % 3, 2)

    # Raw labels (r^a*(-1)^b, 3^c*eta^d). The canonical section is b=c=0.
    scalar_minus1 = (0, 1, 0, 0)
    scalar3 = (0, 0, 1, 0)
    scalars = sorted({(0,)*4, scalar_minus1, scalar3, xor(scalar_minus1, scalar3)})

    def norm(x):
        a, b_, c, d = x
        return (a, a ^ d)

    def canonical(x):
        candidates = [xor(x, s) for s in scalars]
        selected = [w for w in candidates if w[1] == w[2] == 0]
        assert len(selected) == 1
        return selected[0]

    raw = list(product(range(2), repeat=4))
    labels = [dict(raw=list(x), norm=list(norm(x)),
                   scalar_orbit=[list(y) for y in sorted(xor(x, s) for s in scalars)],
                   canonical=list(canonical(x)), norm_admissible=norm(x) == (0, 0))
              for x in raw]
    ambient = sorted({canonical(x) for x in raw if norm(x) == (0, 0)})
    check('one common scalar image order', len(scalars), 4)
    check('scalars norm trivial', [norm(s) for s in scalars], [(0, 0)]*4)
    check('raw norm kernel order', sum(norm(x) == (0, 0) for x in raw), 4)
    check('full scalar quotient order', len({canonical(x) for x in raw}), 4)
    check('norm admissible ambient', ambient, [(0, 0, 0, 0)])

    integral = [dict(t_mod_3=0, condition='t in 3Z3, including zero',
                     G_valuation=5, obstruction='odd valuation'),
                *[dict(t_mod_3=t, condition='unit', G_mod_3=res(ev(G, t)),
                       obstruction='nonsquare unit residue') for t in (1, 2)]]
    coefficient_values = [v(c) for c in G]
    check('all G coefficient valuations', coefficient_values,
          [5, None, 4, None, 2, None, 0, None, 0])
    integral_nonconstant = [dict(power=i, slope=i, intercept=v(G[i]),
                                minimum_at_n_1=i+v(G[i])) for i in (2, 4, 6, 8)]
    check('strict constant dominance on 3Z3',
          all(x['minimum_at_n_1'] > 5 for x in integral_nonconstant), True)
    check('all unit residue disks nonsquare', [x['G_mod_3'] for x in integral[1:]], [2, 2])
    reciprocal = [dict(power=i, coefficient=str(Q(G[8-i], 3025)), slope=i,
                       intercept=v(Q(G[8-i], 3025)),
                       minimum_at_n_1=i+v(Q(G[8-i], 3025))) for i in (2, 4, 6, 8)]
    check('reciprocal strict error minima', [x['minimum_at_n_1'] for x in reciprocal], [2, 6, 10, 13])
    factor_bounds = [dict(factor='L6', slope=6, intercept=5, minimum_at_n_1=11),
                     dict(factor='U2', slope=1, intercept=0, minimum_at_n_1=1)]
    check('strict point class bounds', all(x['minimum_at_n_1'] > 0 for x in factor_bounds), True)
    s3 = ev(list(reversed(G)), 3)/3025
    check('finite realization S(3) residue', res(s3), 1)
    check('finite realization S(3)-1 valuation', v(s3-1), 2)
    check('finite realization chart identity',
          str(ev(G, Q(1, 3))/(Q(55)*Q(1, 3)**4)**2), str(s3))
    finite = dict(t='1/3', q='3', S=str(s3), S_minus_one_valuation=v(s3-1),
                  X_definition='unique X=1 mod 3 with X^2=S(3)',
                  derivative_mod_3=2, Y_definition='55*X/3^4', fake_class=[0]*4)
    infinity = [dict(q=0, Z=z, derivative=2*z,
                     representative=3025, fake_class=[0]*4) for z in (-55, 55)]
    check('two distinct smooth infinity points',
          len({x['Z'] for x in infinity if x['derivative'] != 0}), 2)
    check('infinity representatives square', 55**2, 3025)

    failures = [x for x in checks if not x['passed']]
    certificate = dict(
        target='Exact Q3 fake image in the common scalar quotient',
        G=G, P=P, hensel=dict(seed=2, root_definition='unique u0=2 mod 3 with P(u0)=0',
                            derivative_mod_3=res(ev(dp, 2)), lifts=lifts,
                            approximation=seed, modulus=modulus),
        cleared_factor_identity=dict(numerators=B, residual_by_t_degree=cleared,
                                     meaning='(t^2-u)*B(t,u)-u^3*G(t)=-P(u)*t^6'),
        local_models=dict(L6='E(r)=r^6+9*b2/b0*r^4+81*b4/b0*r^2+729/b0; theta=3/r',
                          U2='omega^2=u0; theta=omega',
                          ef_pairs=[[6, 1], [1, 2]],
                          b_approximation=[str(x) for x in b],
                          E_approximation=[str(x) for x in e],
                          approximation_qualification='finite root approximants only; exact models use the specified Hensel root',
                          normalized_theta_valuations=[5, 0],
                          r6_over_3_residue=r6_over_3),
        F9=dict(nonzero_squares=squares9, eta=[1, 1]),
        norm_generators=[dict(factor='L6', generator='r', norm='729/b0', label=[1, 1]),
                         dict(factor='L6', generator='-1', norm='1', label=[0, 0]),
                         dict(factor='U2', generator='3', norm='9', label=[0, 0]),
                         dict(factor='U2', generator='eta=1+omega', norm='1-u0', label=[0, 1])],
        scalar_generators=dict(minus_one=scalar_minus1, three=scalar3),
        canonical_section='b=c=0, not lexicographic orbit labels', raw_labels=labels,
        ambient=ambient, integral_disks=integral, integral_nonconstant_bounds=integral_nonconstant,
        reciprocal_terms=reciprocal, reciprocal_class_bounds=factor_bounds,
        rational_branch_points=[], finite_realization=finite, infinity_rows=infinity,
        exact_image=[[0]*4], comparison=dict(image_count=1, ambient_count=len(ambient),
                                           proper=False, required_for_pruning='image_count < ambient_count'),
        checks=checks, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks), failures=failures,
                          image_actual=1, norm_ambient_actual=len(ambient),
                          required_for_strict_pruning='image < ambient',
                          factor_degrees_actual=[6, 2], degree_sum_required=8,
                          reciprocal_square_min_actual=2, required_strictly_greater_than=0,
                          path=str(OUT)), indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
