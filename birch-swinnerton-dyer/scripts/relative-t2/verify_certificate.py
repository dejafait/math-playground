#!/usr/bin/env python3
"""Replay all complete evidence without importing the construction program."""
import hashlib
import json
from fractions import Fraction as Q
from math import gcd, isqrt, prod
from pathlib import Path

SOURCE = Path('scripts/relative-t2/certificate.json')
OUT = Path('scripts/relative-t2/verification.json')
checks = {}


def check(name, condition):
    if not condition:
        checks[name] = False
        OUT.write_text(json.dumps({'checks': checks, 'failures': [name]}, indent=2)+'\n')
        raise AssertionError(name)
    checks[name] = True


def unit(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def multiply(a, b):
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def replay_row(a, op):
    t, i, j, *rest = op
    if t == 'swap':
        a[i], a[j] = a[j], a[i]
    elif t == 'add':
        assert isinstance(rest[0], int) and i != j
        a[i] = [x+rest[0]*y for x, y in zip(a[i], a[j])]
    else:
        assert t == 'neg' and i == j
        a[i] = [-x for x in a[i]]


def replay_column(a, op):
    # Transpose, apply a row operation, transpose back: independently
    # implements the builder's in-place column convention.
    at = [list(x) for x in zip(*a)]
    replay_row(at, op)
    a[:] = [list(x) for x in zip(*at)]


def inverse_op(op):
    if op[0] == 'add':
        return [op[0], op[1], op[2], -op[3]]
    return op


def verify():
    raw = SOURCE.read_bytes()
    c = json.loads(raw)
    ar = c['arithmetic']
    a1, a2, a3, a4, a6 = ar['model']
    check('exact_model', ar['model'] == [0, 1, 1, -2, 0])
    b2, b4, b6, b8 = a1*a1+4*a2, 2*a4+a1*a3, a3*a3+4*a6, \
        a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    c4, c6 = b2*b2-24*b4, -b2**3+36*b2*b4-216*b6
    check('invariants', [b2, b4, b6, b8] == ar['b'] and
          c4 == ar['c4'] and c6 == ar['c6'] and delta == ar['discriminant'] and
          c4**3-c6*c6 == 1728*delta)
    expected_trials = [[k, delta % k] for k in range(2, isqrt(delta)+1)]
    check('complete_primality_certificate', expected_trials == ar['primality_trial']
          and delta > 1 and all(r for _, r in expected_trials))
    check('minimality_and_multiplicative_inputs', delta == 389 and
          gcd(c4, delta) == 1 and ar['conductor'] == delta)
    check('nonCM_input', Q(ar['j']) == Q(c4**3, delta) and Q(ar['j']).denominator > 1)
    f2 = [[x, y, (y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6) % 2]
          for x in range(2) for y in range(2)]
    affine = [[x, y] for x, y, value in f2 if value == 0]
    # F_y = 2y+a1*x+a3 is identically 1 modulo 2; infinity has
    # projective derivative F_Z=1 at [0:1:0]. These check smoothness.
    check('smooth_complete_F2_count', f2 == ar['F2_table'] and
          affine == ar['F2_affine_points'] and a1 % 2 == 0 and a3 % 2 == 1 and
          delta % 2 == 1 and ar['F2_infinity_count'] == 1 and
          ar['a2'] == 3-(len(affine)+1) == -2)
    n = delta
    s = n+1
    p, lifts = c['projective_cosets'], c['SL2_lifts']
    check('complete_projective_cosets', p == [[1, t] for t in range(n)]+[[0, 1]])
    check('all_SL2_lifts', len(lifts) == s and
          all(a*d-b*cc == 1 and [cc, d] == row
              for (a, b, cc, d), row in zip(lifts, p)))

    def idx(cc, dd):
        return (dd*pow(cc % n, -1, n)) % n if cc % n else n

    permutations = [[idx(dd, -cc), idx(dd, -cc-dd), idx(-cc-dd, cc)]
                    for cc, dd in p]
    check('all_S_U_U2_permutations', permutations == c['permutations_S_U_U2'])
    relations = []
    for i, (si, ui, uui) in enumerate(permutations):
        for indices in [[i, si], [i, ui, uui]]:
            row = [0]*s
            for k in indices:
                row[k] += 1
            relations.append(row)
    check('all_relations', relations == c['relations'] and len(relations) == 2*s)
    pr = c['presentation']
    rank, dim = pr['rank'], pr['dimension']
    diag = pr['diagonal']
    a = [r[:] for r in relations]
    for op in pr['row_operations']:
        replay_row(a, op)
    for op in pr['column_operations']:
        replay_column(a, op)
    check('full_integral_diagonal_replay', len(diag) == rank and all(x > 0 for x in diag)
          and dim == s-rank and all(a[i][j] == (diag[i] if i == j and i < rank else 0)
                                   for i in range(2*s) for j in range(s)))
    cc = unit(s)
    for op in pr['column_operations']:
        replay_column(cc, op)
    ci = unit(s)
    for op in reversed(pr['column_operations']):
        replay_column(ci, inverse_op(op))
    check('full_unimodular_coordinate_witness', cc == pr['column_transform'] and
          ci == pr['inverse_column_transform'] and multiply(cc, ci) == unit(s) and
          multiply(ci, cc) == unit(s))
    coords = [row[rank:] for row in cc]
    basis = ci[rank:]
    sat = ci[:rank]
    check('full_saturation_witness', coords == pr['integral_generator_coordinates'] and
          basis == pr['integral_quotient_basis_lifts'] and
          sat == pr['saturated_relation_basis'] and pr['saturation_index'] == prod(diag)
          and pr['coordinate_denominator'] == 1 and
          multiply(basis, coords) == unit(dim) and
          multiply(sat, coords) == [[0]*dim for _ in sat] and
          multiply(relations, coords) == [[0]*dim for _ in relations])
    print('verified full presentation and saturation', flush=True)

    def cusp(pp, qq):
        if qq == 0:
            assert pp != 0
            return [1, 0]
        divisor = gcd(pp, qq)
        pp, qq = pp//divisor, qq//divisor
        return [pp, qq] if qq > 0 else [-pp, -qq]

    def endpoint(matrix, pt):
        aa, bb, cc, dd = matrix
        pp, qq = pt
        return cusp(aa*pp+bb*qq, cc*pp+dd*qq)

    segment_count = 0

    def verify_chain(chain, target):
        nonlocal segment_count
        assert chain['target'] == target and cusp(*target) == target
        prev = [1, 0]
        for seg in chain['segments']:
            aa, bb, cc, dd = seg['lift']
            assert aa*dd-bb*cc == 1
            assert seg['start'] == prev == cusp(bb, dd)
            assert seg['end'] == cusp(aa, cc)
            ii = seg['coset']
            assert ii == idx(cc, dd)
            ha, hb, hc, hd = lifts[ii]
            gamma = [aa*hd-bb*hc, -aa*hb+bb*ha,
                     cc*hd-dd*hc, -cc*hb+dd*ha]
            assert seg['Gamma0_reduction'] == gamma and gamma[2] % n == 0
            assert gamma[0]*gamma[3]-gamma[1]*gamma[2] == 1
            prev = seg['end']
            segment_count += 1
        assert prev == target
        # Check the entire continued fraction, not merely endpoints.
        cf = chain['continued_fraction']
        if target[1] == 0:
            assert cf == [] and chain['segments'] == []
        else:
            assert len(cf) == len(chain['segments']) and cf
            value = Q(cf[-1])
            for digit in reversed(cf[:-1]):
                assert value
                value = digit+1/value
            assert value == Q(*target)

    def verify_path(path, start, end):
        assert path['start'] == start and path['end'] == end
        verify_chain(path['start_chain'], start)
        verify_chain(path['end_chain'], end)
        rr = [0]*s
        for sign, chain in [(-1, path['start_chain']), (1, path['end_chain'])]:
            for seg in chain['segments']:
                rr[seg['coset']] += sign
        assert rr == path['raw']
        result = [sum(rr[i]*coords[i][j] for i in range(s)) for j in range(dim)]
        assert result == path['coordinates']
        return result

    endpoints = [[cusp(bb, dd), cusp(aa, cc)] for aa, bb, cc, dd in lifts]
    check('all_original_generator_endpoint_paths',
          len(c['basepaths']) == s and
          all(verify_path(path, start, end) == coord
              for path, (start, end), coord in zip(c['basepaths'], endpoints, coords)))
    maps = {'J': [[-1, 0, 0, 1]],
            'H2': [[2, 0, 0, 1], [1, 0, 0, 2], [1, 1, 0, 2]]}
    check('geometric_operator_endpoint_maps', maps == c['operator_endpoint_matrices'])
    matrices = {}
    for name, maps_for_op in maps.items():
        paths = c['operator_paths'][name]
        assert len(paths) == s
        image_rows = []
        for (start, end), terms in zip(endpoints, paths):
            assert len(terms) == len(maps_for_op)
            values = [verify_path(path, endpoint(m, start), endpoint(m, end))
                      for path, m in zip(terms, maps_for_op)]
            image_rows.append([sum(row[j] for row in values) for j in range(dim)])
        check(name+'_all_geometric_generator_images',
              image_rows == c['operator_generator_images'][name])
        rel_img = multiply(relations, image_rows)
        check(name+'_all_relation_and_saturation_images',
              rel_img == c['operator_relation_images'][name] == [[0]*dim for _ in relations]
              and multiply(sat, image_rows) == [[0]*dim for _ in sat])
        basis_rows = multiply(basis, image_rows)
        matrices[name] = [list(row) for row in zip(*basis_rows)]
        check(name+'_complete_column_matrix', matrices[name] == c['matrices'][name] and
              multiply(coords, basis_rows) == image_rows)
    j, h = matrices['J'], matrices['H2']
    check('involution_and_commutation', multiply(j, j) == unit(dim) and
          multiply(j, h) == multiply(h, j))
    print('verified all endpoint chains and operators', segment_count, 'segments', flush=True)
    b = [[j[col][row]-int(row == col) for col in range(dim)] for row in range(dim)]
    b += [[h[col][row]-ar['a2']*int(row == col) for col in range(dim)] for row in range(dim)]
    dual = c['dual']
    check('full_relative_dual_matrix', b == dual['B'])
    reduced = [[Q(x) for x in row] for row in b]
    for op in dual['row_operations']:
        typ, i, *tail = op
        if typ == 'swap':
            other = tail[0]
            reduced[i], reduced[other] = reduced[other], reduced[i]
        elif typ == 'scale':
            scalar = Q(tail[0])
            assert scalar
            reduced[i] = [scalar*x for x in reduced[i]]
        else:
            assert typ == 'add'
            other, scalar = tail[0], Q(tail[1])
            assert i != other
            reduced[i] = [x+scalar*y for x, y in zip(reduced[i], reduced[other])]
    pivots = dual['pivots']
    check('complete_rational_rank_replay',
          reduced == [[Q(x) for x in row] for row in dual['rref']] and
          pivots == sorted(set(pivots)) and
          all(reduced[i][pivot] == 1 and all(x == 0 for x in reduced[i][:pivot]) and
              all(reduced[k][pivot] == int(k == i) for k in range(len(reduced)))
              for i, pivot in enumerate(pivots)) and
          all(not any(row) for row in reduced[len(pivots):]))
    free = [i for i in range(dim) if i not in pivots]
    kernel = [[Q(x) for x in row] for row in dual['kernel_basis']]
    check('complete_kernel_basis', len(kernel) == len(free) and
          all([v[j] for j in free] == unit(len(free))[i] and
              all(sum(x*y for x, y in zip(row, v)) == 0 for row in b)
              for i, v in enumerate(kernel)))
    check('dimension_one_threshold', len(pivots) == dual['rank'] == dim-1 and
          len(kernel) == dual['dimension'] == dual['required_dimension'] == 1 and
          c['result'] == 'THRESHOLD_MET' and c['failures'] == [])
    line = c['integration_line']
    values = [sum(x*y for x, y in zip(row, kernel[0])) for row in coords]
    check('all_integral_generator_functional_values',
          [Q(x) for x in line['basis_functional']] == kernel[0] and
          [Q(x) for x in line['integral_generator_values']] == values and
          any(values) and
          all(sum(x*y for x, y in zip(row, values)) == 0 for row in sat) and
          line['scale_to_real_integration'] == 'NONZERO_REAL_UNCOMPUTED' and
          line['Neron_normalized_scale'] == 'NOT_CERTIFIED')
    report = {'certificate_sha256': hashlib.sha256(raw).hexdigest(),
              'checks': checks, 'failures': [],
              'results': {'conductor': n, 'a2': ar['a2'], 'cosets': s,
                          'relation_rows': len(relations), 'relation_rank': rank,
                          'saturation_index': pr['saturation_index'],
                          'relative_dimension': dim, 'path_segments': segment_count,
                          'B_rank': len(pivots), 'kernel_dimension': len(kernel),
                          'required_kernel_dimension': 1}}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('PASS', len(checks), 'complete checks; actual/required kernel dimension',
          len(kernel), '/', 1, '; failures []; reports', SOURCE, OUT)


if __name__ == '__main__':
    verify()
