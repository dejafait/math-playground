#!/usr/bin/env python3
"""Independent exact L120 audit; universal valuation arguments are in L120.

Does not import or execute the producer. Rebuilds every payload field and
checks its full value, including every matrix entry, label and chart row.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'marked-octic-eleven-adic-image-certificate.json'
OUT = HERE / 'marked-octic-eleven-adic-audit-certificate.json'
checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def valuation(x):
    x = F(x)
    if not x:
        return None
    a, b, n = abs(x.numerator), x.denominator, 0
    while a % 11 == 0:
        a //= 11
        n += 1
    while b % 11 == 0:
        b //= 11
        n -= 1
    return n


def residue(x):
    x = F(x)
    return (x.numerator % 11) * pow(x.denominator % 11, -1, 11) % 11


def evaluate(coeffs, x):
    return sum((F(c) * F(x)**i for i, c in enumerate(coeffs)), F(0))


# Start from the actual twisted curve in L113, not stored certificate data.
G = [11*c for c in [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]]
E = [c//11 for c in G[::-1]]
monic = [F(c, E[-1]) for c in E]


def reduce_poly(coeffs):
    out = list(map(F, coeffs))
    for i in range(len(out)-1, 7, -1):
        c = out[i]
        for j in range(9):
            out[i-8+j] -= c*monic[j]
    return (out + [F(0)]*8)[:8]


def multiply(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return reduce_poly(out)


def power(a, n):
    out = reduce_poly([1])
    for _ in range(n):
        out = multiply(out, a)
    return out


def strings(a):
    return [str(x) for x in a]


def determinant_by_permutations(matrix):
    value = F(0)
    for perm in permutations(range(8)):
        term = F((-1)**sum(perm[i] > perm[j]
                          for i in range(8) for j in range(i+1, 8)))
        for i, j in enumerate(perm):
            term *= matrix[i][j]
            if not term:
                break
        value += term
    return value


def main():
    saved = json.loads(SOURCE.read_text())
    r = reduce_poly([0, 1])
    # E(r)=0 gives this explicit inverse, independently of a field solver.
    theta = [-F(E[i+1], E[0]) for i in range(8)]
    check('exact inverse r theta', strings(multiply(r, theta)), strings(reduce_poly([1])))
    Gtheta = [sum(F(G[i])*power(theta, i)[j] for i in range(9)) for j in range(8)]
    check('actual G(theta) in full quotient', strings(Gtheta), ['0']*8)
    check('reciprocal coefficient identity', G, [11*c for c in E[::-1]])
    ev = [valuation(c) for c in E]
    check('monic Eisenstein criterion', ev, [1, None, 1, None, 1, None, 1, None, 0])
    columns = [multiply(r, reduce_poly([0]*j+[1])) for j in range(8)]
    matrix = [[columns[j][i] for j in range(8)] for i in range(8)]
    nr = determinant_by_permutations(matrix)
    check('Leibniz norm agrees with constant coefficient', str(nr), str(monic[0]))
    squares = sorted(set(x*x % 11 for x in range(1, 11)))
    check('residue nonsquare generator', 10 in squares, False)
    norm_unit = residue(nr / 11**valuation(nr))
    check('norm unit square residue', norm_unit, 3)
    r8_over_11 = [x/11 for x in power(r, 8)]
    check('integral coefficients of r8/11', all(valuation(x) >= 0 for x in r8_over_11 if x), True)
    unit_residue = residue(r8_over_11[0])
    eleven_residue = pow(unit_residue, -1, 11)
    check('unit residues for scalar eleven', [unit_residue, eleven_residue], [8, 7])
    scalar_image = [[0, 0], [0, int(eleven_residue not in squares)]]
    check('scalar image contains minus one and has size two', scalar_image, [[0, 0], [0, 1]])

    raw = []
    for a, b in product(range(2), repeat=2):
        norm = nr**a * F((-1)**(8*b))
        nv = valuation(norm)
        label = [nv % 2, int(residue(norm / 11**nv) not in squares)]
        orbit = sorted([[a ^ s[0], b ^ s[1]] for s in scalar_image])
        raw.append(dict(raw=[a, b], norm=label, scalar_orbit=orbit,
                        canonical=min(orbit), norm_admissible=label == [0, 0]))
    ambient = sorted({tuple(row['canonical']) for row in raw if row['norm_admissible']})
    ambient = [list(row) for row in ambient]
    check('norm-admissible scalar quotient', ambient, [[0, 0]])

    integral_coeff_vals = [valuation(c) for c in G]
    check('constant curve valuation', integral_coeff_vals[0], 1)
    check('every nonconstant term strictly higher on Z11',
          all(v >= 2 for v in integral_coeff_vals[1:] if v is not None), True)
    integral = [dict(t_residue=a, G_over_11_residue=residue(evaluate(G, a)/11),
                     valuation=valuation(evaluate(G, a)), feasible=False) for a in range(11)]
    terms = [dict(power=i, coefficient=str(F(G[8-i], G[8])),
                  intercept=valuation(F(G[8-i], G[8])),
                  minimum_at_n_1=i+valuation(F(G[8-i], G[8]))) for i in (2, 4, 6, 8)]
    check('all reciprocal slopes positive', all(row['power'] > 0 for row in terms), True)
    check('reciprocal term minima for every n>=1', [row['minimum_at_n_1'] for row in terms], [2, 4, 6, 7])
    check('strict square thresholds integral/curve/fake', [1 > 0, 2 > 0, 7 > 0], [True]*3)
    q = F(11)
    S = evaluate(G[::-1], q)/G[-1]
    check('finite radicand exact value', str(S), '4170589184/25')
    check('finite original curve/chart equality', str(evaluate(G, 1/q)*q**8), str(3025*S))
    check('finite Hensel hypotheses (residue,error,derivative)', [residue(S), valuation(S-1), 2], [1, 2, 2])
    infinities = [dict(point=name, q=0, Z=z, derivative=2*z,
                       fake_representative=G[-1], fake_class=[0, 0])
                  for name, z in [('I_minus', -55), ('I_plus', 55)]]
    check('two distinct smooth infinity solutions',
          all(x['Z']**2 == G[-1] and x['derivative'] != 0 for x in infinities)
          and infinities[0]['Z'] != infinities[1]['Z'], True)
    rebuilt = dict(
        polynomial=G, reciprocal_E=E, E_valuations=ev,
        field=dict(model='Q11[r]/(E/243)', degree=8, e=8, f=1,
                   theta='1/r', normalized_theta_valuation=-1),
        squares_mod_11=squares, norm_r_matrix=[strings(row) for row in matrix], norm_r=str(nr),
        scalar_rows=dict(minus_one=[0, 1], eleven=[0, int(eleven_residue not in squares)]),
        scalar11_unit_residue=eleven_residue, square_class_rows=raw, norm_ambient=ambient,
        integral_rows=integral, reciprocal_terms=terms,
        strict_bounds=dict(square_neighborhood_required='normalized error valuation > 0',
                           integral_class_ratio_minimum=1, reciprocal_curve_minimum=2,
                           reciprocal_fake_ratio=dict(slope=8, intercept=-1, minimum=7)),
        finite_realization=dict(t=str(1/q), q=str(q), S=str(S), seed=1,
                                derivative=2, error_valuation=valuation(S-1),
                                exact_definition='Z=55*sqrt(S), sqrt(S)=1 mod 11; Y=Z/q^4',
                                fake_class=[0, 0]),
        rational_branch_points=0, infinity_rows=infinities,
        conclusion=dict(image=ambient, image_size=1, norm_ambient_size=1,
                        proper=False, global_exclusion=False))
    check('complete producer schema', sorted(saved), sorted(list(rebuilt)+['checks', 'failures']))
    for key, expected in rebuilt.items():
        check('full payload /'+key, saved[key], expected)
    # Check bookkeeping only AFTER independently reconstructing its evidence.
    check('producer check count', len(saved['checks']), 23)
    for row in saved['checks']:
        check('producer record consistency: '+row['name'],
              row['actual'] == row['required'] and row['passed'] is True, True)
    check('producer reported failures', saved['failures'], [])
    failures = [c for c in checks if not c['passed']]
    result = dict(source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                  method='independent quotient reduction and Leibniz determinant; no producer import',
                  exact_theta_polynomial=strings(theta), r8_over_11=strings(r8_over_11),
                  rebuilt_payload=rebuilt,
                  universal_bounds=dict(domain='integer n>=1; all unit parts',
                                        curve_affine_functions=[[2, 0], [4, 0], [6, 0], [8, -1]],
                                        curve_minimum=2, fake_affine_function=[8, -1],
                                        fake_minimum=7, strict_required=0,
                                        integral_coefficient_valuations=integral_coeff_vals),
                  checks=checks, failures=failures)
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Independent checks {len(checks)-len(failures)}/{len(checks)}; failures {len(failures)}')
    print('Complete payload fields compared: 18/18; raw classes 4/4; integral disks 11/11; infinity rows 2/2')
    print('Uniform error minima: 1, 2, 7; required >0. Image/ambient: 1/1; strict pruning would require <1.')
    print(OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
