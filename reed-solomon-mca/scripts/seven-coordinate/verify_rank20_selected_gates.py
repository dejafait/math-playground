"""Independent polynomial-entry, column-rank and all-pivot replay.

No producer imports. The reused verifier utilities construct g by polynomial
multiplication/Horner evaluation and use column elimination for rank/minors.
Every rank and gate is checked afresh; historical artifacts are read-only.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json

from verify_active_rank19_complete_loci import (P, S, H, J, PAIRS, QUADS,
    digest, dot, rank, determinant, block, plane)

HERE = Path(__file__).resolve().parent
MANIFEST = [[60, 666], [65, 671], [145, 696], [295, 197], [300, 202], [314, 382]]


def independent_nullspace(matrix):
    # Forward rows, reverse columns: independent of producer's reverse rows.
    a = [r[:] for r in matrix]
    pivots = []
    for c in reversed(range(len(a[0]))):
        r = len(pivots)
        pivot = next((k for k in range(r, len(a)) if a[k][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        a[r] = [x*pow(a[r][c], -1, P) % P for x in a[r]]
        for k in range(len(a)):
            if k != r:
                factor = a[k][c]
                a[k] = [(x-factor*y) % P for x, y in zip(a[k], a[r])]
        pivots.append(c)
    free = sorted(set(range(len(a[0])))-set(pivots))
    basis = []
    for c in free:
        v = [int(n == c) for n in range(len(a[0]))]
        for r, pivot in enumerate(pivots):
            v[pivot] = -a[r][c] % P
        basis.append(v)
    return len(pivots), basis


def proportional(a, b):
    pivot = next(i for i, x in enumerate(b) if x)
    ratio = a[pivot]*pow(b[pivot], -1, P) % P
    assert ratio and a == [ratio*x % P for x in b]
    return ratio


def run():
    path = HERE/'rank20-selected-gates.json'
    before = digest(path)
    cert = json.loads(path.read_bytes())
    assert cert['modulus'] == P and cert['H'] == H and cert['S'] == S
    assert not cert['failures'] and cert['selected_manifest'] == MANIFEST
    assert digest(HERE/'rank20_selected_gates.py') == cert['code_sha256']
    for name, value in cert['helper_sha256'].items():
        assert digest(HERE/name) == value
    audit = json.loads((HERE/cert['audit_path']).read_bytes())
    assert digest(HERE/cert['audit_path']) == cert['audit_sha256']
    assert not audit['failures'] and audit['replay_returncode'] == 0
    assert all(c['passed'] for c in audit['checks'])
    assert audit['artifact_hashes_before'] == audit['artifact_hashes_after']
    bound = {**audit['artifact_hashes_after'], **audit['code_hashes']}
    assert all(digest(HERE/name) == value for name, value in bound.items())
    source_path = HERE/cert['source_path']
    assert digest(source_path) == cert['source_sha256'] == audit['artifact_hashes_after'][source_path.name]
    source = json.loads(source_path.read_bytes())
    assert len(source['records']) == 599
    assert sum(r['status'] == 'screen_failure' for r in source['records']) == 239
    selected = [(i, r) for i, r in enumerate(source['records'])
                if r['status'] == 'screen_failure' and r['rank'] == 20]
    assert [[r['third_index'], r['fourth_index']] for i, r in selected] == MANIFEST
    assert len(cert['records']) == len(selected) == 6
    universe = list(product(combinations(S, 2), combinations(J, 2)))
    first = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
    initial = set(sum((list(i+k) for i, k in first), []))
    eligible = [r for r in universe if all(len(set(r[0]+r[1]) & set(i+k)) <= 1 for i, k in first)]
    disjoint = [r for r in eligible if not set(r[0]+r[1]) & initial]
    thirds = [r for r in eligible if r not in disjoint and r != ((1, 22), (75, 79))]
    assert [len(universe), len(eligible), len(disjoint), len(thirds)] == [756, 382, 30, 351]
    replay = []
    total_plucker_pivots = total_projection_pivots = 0
    for (position, old), rec in zip(selected, cert['records']):
        n, f = index = [old['third_index'], old['fourth_index']]
        rows = [{'I': list(i), 'K': list(k)} for i, k in first+[thirds[n], universe[f]]]
        assert rec['source_record_position'] == position and rec['historical_index'] == index
        assert rec['rows'] == rows and old['four_rows'] == [[r['I'], r['K']] for r in rows]
        assert all(len(set(a['I']+a['K']) & set(b['I']+b['K'])) <= 1
                   for a, b in combinations(rows, 2))
        blocks = [block(row['I'], row['K']) for row in rows]
        matrix = [r for q, g, z, ext in blocks for r in ext]
        assert matrix == rec['original_matrix'] and rank(matrix) == 20
        fresh_rank, fresh_basis = independent_nullspace(matrix)
        assert fresh_rank == 20 and len(fresh_basis) == 1
        [p] = rec['kernel_basis']
        assert rec['kernel_basis'] == old['kernel_basis']
        proportional(fresh_basis[0], p)
        assert p[rec['free_columns'][0]] == 1 and len(rec['free_columns']) == 1
        assert [dot(r, p) for r in matrix] == rec['kernel_residuals'] == [0]*24
        assert len(rec['rank_minor_rows']) == len(rec['rank_minor_columns']) == 20
        minor = [[matrix[r][c] for c in rec['rank_minor_columns']] for r in rec['rank_minor_rows']]
        assert determinant(minor) == rec['rank_minor_residue'] != 0
        skew = [[0]*7 for _ in S]
        for (a, b), value in zip(PAIRS, p):
            skew[a][b], skew[b][a] = value, -value % P
        plucker = [(skew[a][b]*skew[c][d]-skew[a][c]*skew[b][d]+skew[a][d]*skew[b][c]) % P
                   for a, b, c, d in QUADS]
        assert plucker == rec['plucker_values'] == [0]*35 and rec['decomposable']
        point = rec['plane_and_all_row_gates']
        nonzero_pivots = [pair for pair, value in zip(PAIRS, p) if value]
        u, v = plane(p, nonzero_pivots[0])
        assert point['pivot_indices'] == list(nonzero_pivots[0])
        assert point['u'] == u and point['v'] == v and point['bivector'] == p
        hlines, row_reports = [], []
        for row, (q, g, z, ext), gate in zip(rows, blocks, point['row_gates']):
            qu, qv = [dot(c, u) for c in q], [dot(c, v) for c in q]
            minors = [(qu[a]*qv[b]-qu[b]*qv[a]) % P for a, b in combinations(range(4), 2)]
            assert qu == gate['Q_u'] and qv == gate['Q_v']
            assert minors == gate['projection_minors'] == [0]*6
            assert any(qu+qv) and gate['projection_rank'] == 1
            pivot = next(k for k in range(4) if qu[k] or qv[k])
            alpha, beta = -qv[pivot] % P, qu[pivot]
            h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
            assert any(h) and [alpha, beta] == gate['direction_coefficients']
            assert h == gate['intersection_vector'] and all(dot(c, h) == 0 for c in q)
            lam = h[S.index(z)]*pow(g[z], -1, P) % P
            error = {x: (h[S.index(x)]-lam*g[x]) % P for x in row['I']}
            error.update({x: -lam*g[x] % P for x in row['K']})
            weights = [error[x] for x in row['I']+row['K']]
            assert lam == gate['lambda_value'] != 0 and all(weights)
            assert weights == gate['error_weights'] and weights[:2] == gate['overlap_weights']
            identity = [((h[S.index(x)] if x in S else 0)-error.get(x, 0)-lam*g[x]) % P for x in H]
            moments = [sum(((h[S.index(x)] if x in S else 0)-error.get(x, 0))*pow(x, d, P)
                           for x in H) % P for d in range(1, 9)]
            assert identity == gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16
            assert moments == gate['moment_residuals'] == [0]*8
            assert gate['failed_gates'] == [] and gate['passes']
            assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha, 'C_coefficient': -beta % P}
            # Independent original eight-moment matrix on (plane,error) coefficients.
            moment_matrix = [[sum(u[S.index(x)]*pow(x, d, P) for x in S) % P,
                              sum(v[S.index(x)]*pow(x, d, P) for x in S) % P]
                             +[-pow(x, d, P) % P for x in row['I']+row['K']]
                             for d in range(1, 9)]
            mrank, mbasis = independent_nullspace(moment_matrix)
            assert mrank == rank(moment_matrix) == 5 and len(mbasis) == 1
            proportional(mbasis[0], [alpha, beta]+weights)
            hlines.append(h)
            row_reports.append({'direction': [alpha, beta], 'lambda': lam, 'weights': weights,
                                'moment_matrix_rank': mrank, 'moment_kernel': mbasis[0]})
        assert len(point['row_gates']) == 4 and point['passes_intrinsic_gates']
        assert rec['disposition'] == 'intrinsic_survivor'
        # All nonzero exterior pivots and quotient pivots give the same lines.
        pivot_reports = []
        for pivot in nonzero_pivots:
            uu, vv = plane(p, pivot)
            lines = []
            for row_number, (q, g, z, ext) in enumerate(blocks):
                aa, bb = [dot(c, uu) for c in q], [dot(c, vv) for c in q]
                assert rank([[x, y] for x, y in zip(aa, bb)]) == 1
                for k in range(4):
                    if aa[k] or bb[k]:
                        hh = [(-bb[k]*x+aa[k]*y) % P for x, y in zip(uu, vv)]
                        ratio = proportional(hh, hlines[row_number])
                        lines.append([row_number, k, ratio])
            total_projection_pivots += len(lines)
            pivot_reports.append({'pivot': list(pivot), 'projection_line_ratios': lines})
        total_plucker_pivots += len(pivot_reports)
        # Four full supports must give distinct directions; test explicitly.
        directions = [r['direction'] for r in row_reports]
        assert all((a*d-b*c) % P for (a, b), (c, d) in combinations(directions, 2))
        replay.append({'historical_index': index, 'original_minor_residue': rec['rank_minor_residue'],
                       'u': u, 'v': v, 'rows': rows, 'row_reports': row_reports,
                       'all_pivot_reports': pivot_reports, 'disposition': 'intrinsic_survivor'})
    expected_summary = {'required_occurrences': 6, 'processed_occurrences': 6,
        'rank': 20, 'required_kernel_dimension': 1, 'decomposable_points': 6,
        'dispositions': {'intrinsic_survivor': 6}, 'row_gates': 24,
        'projection_ranks': {'1': 24}, 'failed_gates': {}, 'surviving_indices': MANIFEST}
    assert cert['summary'] == expected_summary
    assert digest(path) == before
    assert all(digest(HERE/name) == value for name, value in bound.items())
    summary = {'processed_occurrences': 6, 'required_occurrences': 6,
               'plucker_equations': 210, 'projection_rows': 24, 'original_moment_residuals': 192,
               'original_moment_matrices_rank5': 24, 'intrinsic_survivors': 6,
               'all_nonzero_plucker_pivots': total_plucker_pivots,
               'all_nonzero_projection_pivots': total_projection_pivots}
    classification = [{key: r[key] for key in
                       ['historical_index', 'original_minor_residue', 'u', 'v', 'rows', 'row_reports']}
                      for r in replay]
    out = {'input_sha256': before, 'code_sha256': digest(Path(__file__)),
           'helper_sha256': digest(HERE/'verify_active_rank19_complete_loci.py'),
           'summary': summary, 'classification': classification, 'records': replay, 'failures': []}
    target = HERE/'rank20-selected-gates-replay.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Processed 6/6; rank 20/21; all 24 moment ranks 5/6; failures 0; certificate {target}')


if __name__ == '__main__':
    run()
