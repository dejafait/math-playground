#!/usr/bin/env python3
"""Audit L921's printed tuple; no import/execution of its generating program."""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parents[2]
DEG = 6


def product(a, b):
    return [sum((a[j] * b[n-j] for j in range(n+1)), Q(0))
            for n in range(DEG+1)]


def det(matrix):
    """Exact Gaussian elimination with row swaps, including singular minors."""
    a = [row[:] for row in matrix]
    answer = Q(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            answer = -answer
        value = a[k][k]
        answer *= value
        for i in range(k+1, len(a)):
            factor = a[i][k] / value
            for j in range(k+1, len(a)):
                a[i][j] -= factor * a[k][j]
            a[i][k] = Q(0)
    return answer


def encoded(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {k: encoded(v) for k, v in x.items()}
    if isinstance(x, list):
        return [encoded(v) for v in x]
    return x


def decoded(x):
    if isinstance(x, str):
        return Q(x)
    if isinstance(x, list):
        return [decoded(v) for v in x]
    return x


def main():
    checks = {}

    def check(name, assertion):
        checks[name] = bool(assertion)

    # Literal displayed raw moments, not generated logarithmic coordinates.
    y = list(map(Q, ['1', '2', '2999997/250000', '2999997/25000',
        '20999790000063/12500000000', '37802645999811/1250000000',
        '415386279060290993763/625000000000000']))
    g = [Q((-1)**n, factorial(2*n))*y[n] for n in range(7)]
    w = [Q(0)] + g[1:]
    power = [Q(1)] + [Q(0)]*DEG
    log_g, inv = [Q(0)]*7, [Q(1)] + [Q(0)]*DEG
    for k in range(1, 7):
        power = product(power, w)
        for n in range(7):
            log_g[n] += Q((-1)**(k+1), k)*power[n]
            inv[n] += (-1)**k*power[n]
    S = [Q(0)] + [-n*log_g[n] for n in range(1, 7)]
    expected_S = list(map(Q, ['1', '1/1000000', '1/1000000',
                              '2/1000000', '5/1000000', '13/1000000']))
    expected_inv = list(map(Q, ['1', '1', '1000001/2000000',
        '66667/400000', '333342000001/8000000000000',
        '66680666669/8000000000000',
        '22278111119666667/16000000000000000000']))
    check('literal_moment_normalization', y[0] == 1 and y[1] > 0)
    check('independent_finite_log', S[1:] == expected_S)
    check('independent_geometric_inverse', inv == expected_inv)
    convolution = product(g, inv)
    check('inverse_product', convolution == [Q(1)] + [Q(0)]*6)
    check('inverse_log_derivative', all(n*inv[n] == sum(
        S[k]*inv[n-k] for k in range(1, n+1)) for n in range(1, 7)))

    matrices = {
        'M3': [[y[i+j] for j in range(4)] for i in range(4)],
        'N2': [[y[i+j+1] for j in range(3)] for i in range(3)],
        'H2': [[S[i+j+2] for j in range(3)] for i in range(3)]}
    minors = {}
    old = json.loads((BASE/'scripts/heat/l918-joint-origin-relaxation-209.json').read_text())
    text = (BASE/'lemmas/L921-joint-origin-finite-moment-relaxation-obstruction.md').read_text()
    for name, matrix in matrices.items():
        records = []
        for size in range(1, len(matrix)+1):
            for indices in combinations(range(len(matrix)), size):
                value = det([[matrix[i][j] for j in indices] for i in indices])
                records.append({'indices': list(indices), 'determinant': value})
                check(name+'_minor_'+''.join(map(str, indices)),
                      value >= 0 if name == 'H2' else value > 0)
        minors[name] = records
        check(name+'_complete_original_minor_values',
              encoded(records) == old['principal_minors'][name])
        check(name+'_complete_original_matrix', matrix == decoded(old['matrices'][name]))
        if name != 'H2':
            table = text.split('Principal minor of '+name+' |', 1)[1].split('\n\n', 1)[0]
            rows = re.findall(r'^\| ([0-3](?:,[0-3])*) \| ([0-9/]+) \|$', table, re.M)
            printed = {tuple(map(int, idx.split(','))): Q(value) for idx, value in rows}
            check(name+'_every_printed_table_entry', len(rows) == len(records) and all(
                printed.get(tuple(r['indices'])) == r['determinant'] for r in records))

    v = [Q(1), Q(-3), Q(1)]
    norm = sum(x*x for x in v)
    cc = [[v[i]*v[j]/norm for j in range(3)] for i in range(3)]
    H = matrices['H2']
    null = [sum(H[i][j]*v[j] for j in range(3)) for i in range(3)]
    check('three_normalized_null_rows', null == [Q(0)]*3)
    check('normalization_and_nonzero_c2', norm == 11 and sum(cc[i][i] for i in range(3)) == 1 and cc[2][2] == Q(1, 11))
    check('rank_exactly_two', det(H) == 0 and det([row[:2] for row in H[:2]]) > 0)
    p, q, b, r = v[0], v[1], S[2], S[3]
    row_values = [-p*b-q*r, p*q*b+(q*q-p)*r,
                  (p*p-p*q*q)*b+(2*p*q-q**3)*r]
    check('three_joint_row_formulas', row_values == S[4:7])
    A, B = [[b, r], [r, -p*b-q*r]], [[Q(1), Q(0), -p], [Q(0), Q(1), -q]]
    congruence = [[H[i][j]-sum(B[k][i]*A[k][l]*B[l][j]
                   for k in range(2) for l in range(2)) for j in range(3)] for i in range(3)]
    check('congruence', congruence == [[Q(0)]*3 for _ in range(3)])
    J_terms = [[cc[i][j]*((i+j+2)*inv[i+j+2]+inv[i+j+1]) for j in range(3)] for i in range(3)]
    J = sum(sum(row) for row in J_terms)
    weights = [p*p, 2*p*q, q*q+2*p, 2*q, Q(1)]
    reduced_J = sum(weights[n-2]*(n*inv[n]+inv[n-1]) for n in range(2, 7))/norm
    claimed_J = Q('-6533305000003999999/88000000000000000000')
    check('direct_and_reduced_J', J == reduced_J == claimed_J)
    check('strict_bounds_and_required_threshold', Q(-3, 40) < J < Q(-7, 100) < 0)
    for field, value in [('y0_through_y6', y), ('g_coefficients', g),
                         ('S1_through_S6', S[1:]), ('inverse_coefficients', inv)]:
        check('original_'+field, value == decoded(old[field]))
    check('original_log_residual_complete', decoded(old['finite_log_residual']) == [Q(0)]*6)
    check('original_inverse_residual_complete', decoded(old['finite_inverse_residual']) == [Q(0)]*7)
    check('original_normalization_complete', decoded(old['normalization']['products_ci_cj']) == cc
          and decoded(old['normalization']['vector_numerator']) == v
          and Q(old['normalization']['norm_squared']) == norm
          and Q(old['normalization']['sum_ci_squared']) == 1
          and Q(old['normalization']['c2_squared']) == Q(1, 11))
    check('original_joint_rows_complete', decoded(old['joint_rows']['null_rows_before_normalization']) == null
          and decoded(old['joint_rows']['congruence_residual']) == congruence)
    check('original_J_all_values', decoded(old['J']['terms']) == J_terms
          and Q(old['J']['value']) == Q(old['J']['joint_value']) == J
          and Q(old['J']['strict_lower_bound']) == Q(-3, 40)
          and Q(old['J']['strict_upper_bound']) == Q(-7, 100)
          and Q(old['J']['required_nonnegative_threshold']) == 0)

    failures = [name for name, passed in checks.items() if not passed]
    counts = {name: {'total': len(records),
        'positive': sum(r['determinant'] > 0 for r in records),
        'zero': sum(r['determinant'] == 0 for r in records)} for name, records in minors.items()}
    certificate = {'scope': 'Independent audit of the single L921 finite tuple only; no theta realization.',
        'method': 'Literal raw moments; finite log and geometric inverse; pivoted Gaussian determinants. No original program imported.',
        'y': y, 'g': g, 'S': S[1:], 'inverse': inv, 'inverse_product': convolution,
        'matrices': matrices, 'principal_minors': minors, 'minor_counts': counts,
        'normalization': {'numerator': v, 'squared_norm': norm, 'products': cc},
        'null_rows': null, 'congruence_residual': congruence,
        'J': {'direct': J, 'reduced': reduced_J, 'terms': J_terms,
              'lower': Q(-3, 40), 'upper': Q(-7, 100), 'required': Q(0)},
        'checks': checks, 'failures': failures, 'passed': not failures}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(encoded(certificate), indent=2)+'\n')
    print('PASS' if not failures else 'FAIL', 'L921 independent fixed-witness audit')
    print('J =', J, '; required >= 0; exact bounds:', Q(-3, 40), '< J <', Q(-7, 100))
    print('Principal minors:', json.dumps(counts, sort_keys=True))
    print('Checks:', len(checks), '; failures:', failures)
    print('Certificate:', path.relative_to(BASE))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
