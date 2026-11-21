#!/usr/bin/env python3
"""Independent C029t audit; standard library, no original code imports.

Sparse Q[sqrt(2), pi] coefficients, Gaussian-rational operator expansion,
triangular monomial inversion and rational interval contour checks.
Original certificates are read-only comparison evidence, never oracles
for coefficients or success. Saved rational centers are proposals only.
"""
from fractions import Fraction as Q
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
OUT = HERE / 'shift-inverse-audit-2036.json'


def clean(a):
    return {k: v for k, v in a.items() if v}


def lin(*terms):
    result = {}
    for factor, polynomial in terms:
        for key, value in polynomial.items():
            result[key] = result.get(key, Q(0)) + factor * value
    return clean(result)


def decode(a):
    return clean({(j, e): Q(row[key]) for j, row in enumerate(a)
                  for e, key in enumerate(('rational', 'sqrt2'))})


def enc(a):
    return {f'{j},{e}': str(v) for (j, e), v in sorted(a.items())}


def ia(a, b):
    return a[0] + b[0], a[1] + b[1]


def im(a, b):
    candidates = [x * y for x in a for y in b]
    return min(candidates), max(candidates)


def si(a, c):
    return im(a, (c, c))


def interval_json(a):
    return {'lower': str(a[0]), 'upper': str(a[1])}


def parse_interval(a):
    return Q(a['lower']), Q(a['upper'])


def gauss(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0]


def power(z, n):
    answer = Q(1), Q(0)
    for _ in range(n):
        answer = gauss(answer, z)
    return answer


def floor_grid(a, digits):
    return Q((a * 10**digits).__floor__(), 10**digits)


def ceil_grid(a, digits):
    return -floor_grid(-a, digits)


def upper(a):
    return max(abs(a[0]), abs(a[1]))


def lower(a):
    return Q(0) if a[0] <= 0 <= a[1] else min(abs(a[0]), abs(a[1]))


def main():
    files = ['shift-inverse-halfplane-2034.json', 'shift_inverse_halfplane_2034.py',
             'tilted-boundary-metric-2010.json', 'tilted_boundary_metric_2010.py',
             'tilted_bezoutian_n6_2014.py']
    hashes = {p: hashlib.sha256((HERE / p).read_bytes()).hexdigest() for p in files}
    old = json.loads((HERE / files[0]).read_text())
    source = json.loads((HERE / files[2]).read_text())
    checks, evidence = {}, {}

    def test(name, condition):
        checks[name] = bool(condition)

    def save(stage):
        evidence.update(status=stage, checks=checks,
                        failures=[k for k, ok in checks.items() if not ok],
                        input_sha256=hashes,
                        audit_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        OUT.write_text(json.dumps(evidence, indent=2) + '\n')

    def guard(stage):
        save(stage)
        if evidence['failures']:
            print('Audit failed:', evidence['failures'], '; certificate:', OUT.name)
            raise SystemExit(1)

    test('original_script_hash', hashes[files[1]] == old['script_sha256'])
    for name, digest in old['input_sha256'].items():
        test('original_pinned_' + name, hashes[name] == digest)

    # Independently form rational pi bounds from finite alternating sums.
    def atan(d):
        partial = sum((Q((-1)**j, (2*j+1)*d**(2*j+1)) for j in range(48)), Q(0))
        return partial, partial + Q(1, 97*d**97)

    mach = ia(si(atan(5), Q(16)), si(atan(239), Q(-4)))
    pi_iv = floor_grid(mach[0], 60), ceil_grid(mach[1], 60)
    b = isqrt(2*10**120)
    s_iv = Q(b, 10**60), Q(b+1, 10**60)
    for label, actual in [('pi', pi_iv), ('sqrt2', s_iv)]:
        test(label+'_input_and_certificate', actual == parse_interval(source[label+'_interval'])
             == parse_interval(old[label+'_interval']))
    test('pi_enclosure', pi_iv[0] <= mach[0] < mach[1] <= pi_iv[1])
    test('sqrt2_enclosure', 0 < s_iv[0]**2 < 2 < s_iv[1]**2)
    test('input_widths', pi_iv[1]-pi_iv[0] == s_iv[1]-s_iv[0] == Q(1, 10**60))
    evidence['pi_interval'] = interval_json(pi_iv)
    evidence['sqrt2_interval'] = interval_json(s_iv)

    # Evaluate by sparse power sums, independently of original Horner code.
    def evaluate(a):
        value = Q(0), Q(0)
        for (j, e), q in sorted(a.items()):
            term = Q(1), Q(1)
            for _ in range(j):
                term = im(term, pi_iv)
            if e:
                term = im(term, s_iv)
            value = ia(value, si(term, q))
        return value

    # Also reconstruct the exact original Horner enclosure for comparison.
    def horner(a):
        value = Q(0), Q(0)
        for j in range(max((key[0] for key in a), default=-1), -1, -1):
            value = ia(im(value, pi_iv), ia((a.get((j, 0), Q(0)),)*2,
                                         si(s_iv, a.get((j, 1), Q(0)))))
        return value

    bern = [Q(1)]
    for m in range(1, 19):
        bern.append(-sum((Q(comb(m+1, k))*bern[k] for k in range(m)), Q(0))/(m+1))
    phases = [(1, 0), (1, 1), (-1, 0), (-1, -1)]
    u = []
    for n in range(9):
        terms = {}
        for h in range(n+1):
            scalar = -Q(factorial(n)*4**h*(4**(h+1)-1)*2**(h+1),
                        factorial(n-h)*factorial(2*h+2))*bern[2*h+2]
            for e, phase in enumerate(phases[(n-h) % 4]):
                terms[h+1, e] = scalar*phase
        u.append(clean(terms))
        test(f'input_u_{n}', u[n] == decode(source['u_over_S_polynomials'][n]))
    a = []
    for n in range(7):
        beta = lin((8*n*n+12*n+7, u[n]), ((2*n+3)*(2*n+5), u[n+2]),
                   *(([(4*n*(n-1), u[n-2])]) if n >= 2 else []))
        weight = Q(factorial(6), factorial(6-n)*6**n)
        a.append(lin((weight, beta)))
        test(f'input_beta_{n}', beta == decode(source['beta_over_S_polynomials'][n]))
        test(f'input_A_{n}', a[n] == decode(source['a_over_S_polynomials'][n]))
        test(f'input_weight_{n}', weight == Q(source['weights'][n]))

    # Basis coefficients by the stated recurrence, no imported helpers.
    p = [[Q(1)]]
    for k in range(6):
        row = [Q(0)] + p[k]
        if k:
            for j in range(k):
                row[j] -= Q(2*k+1, 2)*p[k-1][j]
        p.append([v/(k+1) for v in row])
    test('basis_coefficients', p == [[Q(v) for v in row] for row in old['basis']])
    test('basis_actual_degrees', all(len(row) == k+1 and row[-1] == Q(1, factorial(k))
                                     for k, row in enumerate(p)))

    # Expand both shifted monomials with Gaussian-rational coefficients,
    # then multiply by (3/4 +/- it/2). No parity shortcut is used.
    matrix = [[Q(0) for _ in range(7)] for _ in range(8)]
    for k in range(7):
        column = [(Q(0), Q(0)) for _ in range(8)]
        for direction in (-1, 1):
            for j in range(k+1):
                z = tuple(comb(k, j)*v for v in power((Q(0), Q(2*direction)), k-j))
                const = gauss(z, (Q(3, 4), Q(0)))
                linear = gauss(z, (Q(0), Q(-direction, 2)))
                column[j] = tuple(column[j][e] + const[e] for e in (0, 1))
                column[j+1] = tuple(column[j+1][e] + linear[e] for e in (0, 1))
        test(f'operator_real_column_{k}', all(v[1] == 0 for v in column))
        for j in range(8):
            matrix[j][k] = column[j][0]
    test('no_degree_seven_operator_term', matrix[7] == [Q(0)]*7)
    matrix = matrix[:7]
    test('all_49_operator_entries', matrix == [[Q(v) for v in row] for row in old['operator_matrix']])
    eigen = [Q(4*k+3, 2) for k in range(7)]
    test('distinct_positive_eigenvalues', len(set(eigen)) == 7 and min(eigen) > 0)
    test('saved_eigenvalues', eigen == list(map(Q, old['eigenvalues'])))
    test('triangularity_and_diagonal', all(matrix[j][k] == 0 for j in range(7) for k in range(j))
         and [matrix[k][k] for k in range(7)] == eigen)
    for k in range(7):
        test(f'polynomial_eigenidentity_{k}', all(
            sum((matrix[j][l]*p[k][l] for l in range(k+1)), Q(0))
            == (eigen[k]*p[k][j] if j <= k else 0) for j in range(7)))

    target = [lin(*[(p[k][j], a[k]) for k in range(j, 7)]) for j in range(7)]
    c = [{} for _ in range(7)]
    for j in reversed(range(7)):
        residual = lin((Q(1), target[j]), *[(-matrix[j][k], c[k]) for k in range(j+1, 7)])
        c[j] = lin((1/matrix[j][j], residual))
    for j in range(7):
        test(f'U_coefficient_{j}', target[j] == decode(old['U_coefficients'][j]))
        test(f'h_coefficient_{j}', c[j] == decode(old['h_coefficients'][j]))
        spectral = lin(*[(p[k][j]/eigen[k], a[k]) for k in range(j, 7)])
        test(f'spectral_inverse_{j}', c[j] == spectral)
        residual = lin(*[(matrix[j][k], c[k]) for k in range(7)], (-1, target[j]))
        test(f'exact_identity_coefficient_{j}', residual == {} == decode(old['identity_residual'][j]))
    civ = [horner(v) for v in c]
    for j in range(7):
        test(f'h_horner_interval_{j}', civ[j] == parse_interval(old['h_intervals'][j]))
        test(f'U_horner_interval_{j}', horner(target[j]) == parse_interval(old['U_intervals'][j]))
        test(f'displayed_coefficient_{j}', parse_interval(old['h_outer_12'][j])
             == (floor_grid(civ[j][0], 12), ceil_grid(civ[j][1], 12)))
    test('both_actual_degrees_six', evaluate(c[6])[1] < 0 and evaluate(target[6])[1] < 0)
    evidence.update(operator_matrix=[[str(v) for v in row] for row in matrix],
                    eigenvalues=list(map(str, eigen)),
                    h_coefficients=[enc(v) for v in c], U_coefficients=[enc(v) for v in target],
                    h_intervals=[interval_json(v) for v in civ],
                    independent_power_sum_intervals=[interval_json(evaluate(v)) for v in c])
    guard('COEFFICIENTS_AUDITED')

    disks = []
    expected_centers = [('-107.14057083', '0'), ('3.04261451', '-5.04707187'),
                        ('3.04261451', '5.04707187'), ('12.90364942', '-2.79469559'),
                        ('12.90364942', '2.79469559'), ('28.18741410', '0')]
    for index, center in enumerate(expected_centers):
        z = tuple(map(Q, center))
        r = Q(1, 100000)
        saved = old['disks'][index]
        compact = old['rouche_table'][index]
        test(f'center_radius_{index}', list(map(Q, saved['center'])) == list(z)
             == list(map(Q, compact['center'])) and Q(saved['radius']) == Q(compact['radius']) == r)
        taylor, sparse_taylor = [], []
        for j in range(7):
            re, imv = (Q(0), Q(0)), (Q(0), Q(0))
            sparse_re, sparse_im = {}, {}
            for k in range(j, 7):
                t = tuple(comb(k, j)*v for v in power(z, k-j))
                re, imv = ia(re, si(civ[k], t[0])), ia(imv, si(civ[k], t[1]))
                sparse_re = lin((1, sparse_re), (t[0], c[k]))
                sparse_im = lin((1, sparse_im), (t[1], c[k]))
            taylor.append((re, imv))
            sparse_taylor.append((evaluate(sparse_re), evaluate(sparse_im)))
            test(f'complete_taylor_{index}_{j}', re == parse_interval(saved['taylor'][j]['real'])
                 and imv == parse_interval(saved['taylor'][j]['imag']))
        ell = max(lower(taylor[1][0]), lower(taylor[1][1]))
        upper_bounds = [upper(re)+upper(imv) for re, imv in taylor]
        left = ell*r
        right = sum((v*r**j for j, v in enumerate(upper_bounds) if j != 1), Q(0))
        test(f'full_saved_bounds_{index}', left == Q(saved['linear_lower'])
             and right == Q(saved['remainder_upper']) and left-right == Q(saved['strict_gap']))
        rounded_ell = floor_grid(ell, 12)
        rounded_u = [ceil_grid(v, 12) for v in upper_bounds]
        test(f'all_compact_modulus_bounds_{index}', rounded_ell == Q(compact['linear_modulus_lower_outer_12'])
             == Q(saved['linear_modulus_lower_outer_12']) and rounded_u
             == list(map(Q, compact['taylor_modulus_upper_outer_12']))
             == list(map(Q, saved['taylor_modulus_upper_outer_12'])))
        compact_left = rounded_ell*r
        compact_right = sum((v*r**j for j, v in enumerate(rounded_u) if j != 1), Q(0))
        test(f'compact_totals_{index}', compact_left == Q(compact['compact_left']) == Q(saved['compact_left'])
             and compact_right == Q(compact['compact_right']) == Q(saved['compact_right']))
        test(f'strict_original_rouche_{index}', compact_left > compact_right >= 0 and left > right)
        for label, value in [('linear_lower', left), ('remainder_upper', right), ('gap', left-right)]:
            test(f'table_rounding_{label}_{index}', parse_interval(saved[label+'_outer_12'])
                 == (floor_grid(value, 12), ceil_grid(value, 12)))
        # A second contour test expands symbolic h(z+w) BEFORE interval
        # evaluation. This does not depend on saved Horner Taylor values.
        independent_left = max(lower(sparse_taylor[1][0]), lower(sparse_taylor[1][1]))*r
        independent_right = sum(((upper(re)+upper(imv))*r**j
                                  for j, (re, imv) in enumerate(sparse_taylor) if j != 1), Q(0))
        test(f'independent_symbolic_rouche_{index}', independent_left > independent_right >= 0)
        below, above = z[1]+r < -2, z[1]-r > -2
        test(f'line_classification_{index}', below != above and below == saved['below_line']
             == compact['below_line'] and above == saved['above_line'] == compact['above_line'])
        test(f'saved_multiplicity_count_{index}', saved['multiplicity_count'] == compact['multiplicity_count'] == 1)
        disks.append(dict(center=list(map(str, z)), radius=str(r),
                          taylor=[{'real': interval_json(re), 'imag': interval_json(imv)} for re, imv in taylor],
                          symbolic_taylor=[{'real': interval_json(re), 'imag': interval_json(imv)} for re, imv in sparse_taylor],
                          compact_left=str(compact_left), compact_right=str(compact_right),
                          independent_left=str(independent_left), independent_right=str(independent_right),
                          strict_gap_lower_12=str(floor_grid(left-right, 12)),
                          below_line=below, above_line=above, multiplicity_count=1))
    separations = []
    for i in range(6):
        for j in range(i):
            d2 = sum(((Q(disks[i]['center'][k])-Q(disks[j]['center'][k]))**2 for k in (0, 1)), Q(0))
            wanted = 4*Q(disks[i]['radius'])**2
            test(f'disjoint_{i}_{j}', d2 > wanted)
            match = [v for v in old['separations'] if v['i'] == i and v['j'] == j]
            test(f'saved_separation_{i}_{j}', len(match) == 1 and Q(match[0]['distance_squared']) == d2
                 and Q(match[0]['required_strict_lower']) == wanted)
            separations.append(dict(i=i, j=j, distance_squared=str(d2), threshold=str(wanted)))
    count = sum(v['multiplicity_count'] for v in disks if v['below_line'])
    test('six_disks_exhaust_degree', len(disks) == 6 and sum(v['multiplicity_count'] for v in disks) == 6)
    test('exact_halfplane_count', count == old['halfplane_count'] == 2 and old['required_maximum'] == 1)
    test('no_line_crossing', all(v['below_line'] != v['above_line'] for v in disks))
    test('prefactor_root', gauss((Q(0), Q(3, 2)), (Q(0), Q(1, 2))) == (Q(-3, 4), Q(0)))
    test('nonzero_real_part_degree', evaluate(c[6])[1] < 0 and matrix[6][6] == Q(27, 2))
    evidence.update(disks=disks, separations=separations,
                    compact_summary=[{key: v[key] for key in ('center', 'radius', 'compact_left',
                                      'compact_right', 'strict_gap_lower_12', 'below_line')} for v in disks],
                    summary={'inverse_degree': 6, 'target_degree': 6, 'disks': 6,
                             'halfplane_count': count, 'required_maximum': 1,
                             'boundary_zeros': 0, 'de_bruijn_pair_bound': 2,
                             'scope': 'independent finite known-method reproduction; not an eventual law'})
    guard('AUDIT_PASSED')
    print('Audit PASSED:', len(checks), 'checks; failures:', evidence['failures'])
    print('All seven inverse coefficients and all 42 complex Taylor coefficients agree.')
    print('Six disjoint simple-root disks exhaust degree 6; actual count below -2i:', count, '; required <=1.')
    for d in disks:
        print('Center', d['center'], '; strict gap >=', d['strict_gap_lower_12'], '; below:', d['below_line'])
    print('Certificate:', OUT.relative_to(HERE.parent.parent))


if __name__ == '__main__':
    main()
