#!/usr/bin/env python3
"""Supplement the full replay with strict shapes, source convention and a minor.

Run from the notebook root, in addition to verify_certificate.py.
No imports from either construction or replay program.
"""
import hashlib
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

SOURCE = Path('scripts/relative-t2/certificate.json')
OUT = Path('scripts/relative-t2/audit.json')
report = {'checks': {}, 'failures': []}


def require(name, condition):
    if not condition:
        raise AssertionError(name)
    report['checks'][name] = True


def integers(value, length):
    return (type(value) is list and len(value) == length
            and all(type(x) is int for x in value))


def matrix(value, rows, cols, rational=False):
    assert type(value) is list and len(value) == rows
    for row in value:
        assert type(row) is list and len(row) == cols
        if rational:
            assert all(type(x) is str for x in row)
            for x in row:
                Fraction(x)
        else:
            assert integers(row, cols)


def integral_operations(operations, size):
    for op in operations:
        assert type(op) is list and op[0] in ('swap', 'neg', 'add')
        assert len(op) == (4 if op[0] == 'add' else 3)
        assert all(type(x) is int for x in op[1:])
        assert 0 <= op[1] < size and 0 <= op[2] < size
        assert (op[1] == op[2]) == (op[0] == 'neg')


def audit():
    raw = SOURCE.read_bytes()
    c = json.loads(raw)
    report['certificate_sha256'] = hashlib.sha256(raw).hexdigest()
    p, dual = c['presentation'], c['dual']
    s, r, d = 390, 325, 65
    require('instance_dimensions', p['rank'] == r and p['dimension'] == d)
    for value, rows, cols in [
        (c['projective_cosets'], s, 2), (c['SL2_lifts'], s, 4),
        (c['permutations_S_U_U2'], s, 3), (c['relations'], 2*s, s),
        (p['column_transform'], s, s), (p['inverse_column_transform'], s, s),
        (p['saturated_relation_basis'], r, s),
        (p['integral_generator_coordinates'], s, d),
        (p['integral_quotient_basis_lifts'], d, s), (dual['B'], 2*d, d)]:
        matrix(value, rows, cols)
    require('diagonal_multiplicities', integers(p['diagonal'], r)
            and p['diagonal'].count(1) == 324 and p['diagonal'].count(2) == 1
            and p['saturation_index'] == 2)
    integral_operations(p['row_operations'], 2*s)
    integral_operations(p['column_operations'], s)
    for name, terms in [('J', 1), ('H2', 3)]:
        matrix(c['operator_endpoint_matrices'][name], terms, 4)
        matrix(c['operator_generator_images'][name], s, d)
        matrix(c['operator_relation_images'][name], 2*s, d)
        matrix(c['matrices'][name], d, d)
        assert len(c['operator_paths'][name]) == s
        assert all(len(paths) == terms for paths in c['operator_paths'][name])
    matrix(dual['rref'], 2*d, d, rational=True)
    matrix(dual['kernel_basis'], 1, d, rational=True)
    assert integers(dual['pivots'], d-1)
    assert all(0 <= j < d for j in dual['pivots'])
    for op in dual['row_operations']:
        assert type(op) is list and op[0] in ('swap', 'scale', 'add')
        assert len(op) == (4 if op[0] == 'add' else 3)
        assert type(op[1]) is int and 0 <= op[1] < 2*d
        if op[0] in ('swap', 'add'):
            assert type(op[2]) is int and 0 <= op[2] < 2*d and op[1] != op[2]
        if op[0] in ('scale', 'add'):
            assert type(op[-1]) is str
            scalar = Fraction(op[-1])
            assert op[0] != 'scale' or scalar != 0
    for key, length in [('basis_functional', d), ('integral_generator_values', s)]:
        matrix([c['integration_line'][key]], 1, length, rational=True)
    require('all_matrix_and_operation_shapes_types_bounds', True)

    def cusp(pt):
        assert integers(pt, 2)
        a, b = pt
        assert pt == [1, 0] if b == 0 else b > 0 and gcd(a, b) == 1

    assert len(c['basepaths']) == s
    paths = list(c['basepaths'])
    for name in ('J', 'H2'):
        paths.extend(path for terms in c['operator_paths'][name] for path in terms)
    segment_count = 0
    for path in paths:
        cusp(path['start'])
        cusp(path['end'])
        assert integers(path['raw'], s) and integers(path['coordinates'], d)
        for key in ('start_chain', 'end_chain'):
            chain = path[key]
            cusp(chain['target'])
            assert integers(chain['continued_fraction'], len(chain['continued_fraction']))
            for seg in chain['segments']:
                cusp(seg['start'])
                cusp(seg['end'])
                assert integers(seg['lift'], 4) and integers(seg['Gamma0_reduction'], 4)
                assert type(seg['coset']) is int and 0 <= seg['coset'] < s
                segment_count += 1
    require('all_path_shapes_types_bounds', len(paths) == 1950 and segment_count == 8142)

    # Source tau=(1,-1;1,0), with tau^2=(0,-1;1,-1)=U.
    # Thus tau and U generate the same cyclic orbit in PSL_2, in reverse order.
    def idx(a, b):
        a, b = a % 389, b % 389
        assert a or b
        return b*pow(a, -1, 389) % 389 if a else 389

    source_rows = []
    for i, (a, b) in enumerate(c['projective_cosets']):
        tau, tau2 = idx(a+b, -a), idx(b, -a-b)
        assert tau == c['permutations_S_U_U2'][i][2]
        assert tau2 == c['permutations_S_U_U2'][i][1]
        row = [0]*s
        for k in (i, tau, tau2):
            row[k] += 1
        assert row == c['relations'][2*i+1]
        source_rows.append([i, tau, tau2])
    report['source_tau_orbits'] = source_rows
    require('all_390_source_tau_relation_matches', True)

    # Independent rank proof: a nonzero 64-square minor modulo prime 101,
    # plus an exact nonzero integer nullvector, reconstructed from J,H2.
    j, h = c['matrices']['J'], c['matrices']['H2']
    b = [[j[k][i]-(i == k) for k in range(d)] for i in range(d)]
    b += [[h[k][i]+2*(i == k) for k in range(d)] for i in range(d)]
    require('independently_reconstructed_B', b == dual['B'])
    prime = 101
    assert all(prime % k for k in range(2, isqrt(prime)+1))
    a = [[x % prime for x in row] for row in b]
    ids, selected, columns, pivots, operations = list(range(2*d)), [], [], [], []
    rank = 0
    for col in range(d):
        pivot = next((i for i in range(rank, 2*d) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        ids[rank], ids[pivot] = ids[pivot], ids[rank]
        operations.append(['swap', rank, pivot])
        selected.append(ids[rank])
        columns.append(col)
        pivots.append(a[rank][col])
        inv = pow(a[rank][col], -1, prime)
        for i in range(rank+1, 2*d):
            factor = a[i][col]*inv % prime
            if factor:
                a[i] = [(a[i][k]-factor*a[rank][k]) % prime for k in range(d)]
                operations.append(['subtract', i, rank, factor])
        rank += 1
    require('independent_mod_101_rank_64', rank == 64)
    minor = [[b[i][k] for k in columns] for i in selected]
    # Recheck the selected minor directly, retaining its entire determinant log.
    m, det, determinant_log = [[x % prime for x in row] for row in minor], 1, []
    for k in range(rank):
        pivot = next(i for i in range(k, rank) if m[i][k])
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            det = -det
            determinant_log.append(['swap', k, pivot])
        value = m[k][k]
        det = det*value % prime
        inv = pow(value, -1, prime)
        for i in range(k+1, rank):
            factor = m[i][k]*inv % prime
            if factor:
                m[i] = [(m[i][j]-factor*m[k][j]) % prime for j in range(rank)]
                determinant_log.append(['subtract', i, k, factor])
    require('nonzero_64_square_minor_mod_101', det != 0)
    v = [2*Fraction(x) for x in dual['kernel_basis'][0]]
    assert all(x.denominator == 1 for x in v)
    v = [int(x) for x in v]
    residuals = [sum(row[k]*v[k] for k in range(d)) for row in b]
    require('exact_rank_upper_bound_64', any(v) and residuals == [0]*(2*d))
    report['rank_witness'] = {
        'prime': prime, 'rank': rank, 'required_rank': 64,
        'selected_rows': selected, 'selected_columns': columns, 'minor': minor,
        'minor_determinant_mod_prime': det, 'minor_elimination': determinant_log,
        'minor_triangular_form_mod_prime': m, 'full_forward_elimination': operations,
        'full_echelon_mod_prime': a, 'integer_nullvector': v,
        'exact_nullvector_residuals': residuals}
    report['results'] = {'paths': len(paths), 'segments': segment_count,
                         'relative_dimension': d, 'kernel_dimension': d-rank,
                         'required_kernel_dimension': 1, 'saturation_index': 2}


if __name__ == '__main__':
    try:
        audit()
    except Exception as error:
        report['failures'].append(str(error) or type(error).__name__)
        raise
    finally:
        OUT.write_text(json.dumps(report, indent=2)+'\n')
        print('audit checks', len(report['checks']), 'failures', report['failures'],
              'actual/required kernel dimension',
              report.get('results', {}).get('kernel_dimension'), '/', 1,
              'full evidence', OUT)
