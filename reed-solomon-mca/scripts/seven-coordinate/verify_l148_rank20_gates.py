"""Independent polynomial/Horner, row-kernel, all-pivot and moment replay.

No producer imports or historical main routines execute. Full evidence stays
on disk; only the eight approved occurrences are tested.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

from verify_active_rank19_complete_loci import (P, S, H, J, PAIRS, QUADS,
    digest, dot, rank, determinant, block, plane)
from verify_rank20_selected_gates import independent_nullspace, proportional

HERE = Path(__file__).resolve().parent
MANIFEST = [[467, 750], [499, 668], [608, 695], [668, 499],
            [678, 749], [695, 608], [749, 678], [750, 467]]


def read(name):
    return json.loads((HERE/name).read_bytes())


def run():
    assert __debug__
    path = HERE/'l148-rank20-gates.json'
    before = digest(path)
    cert = read(path.name)
    assert cert['modulus'] == P and cert['S'] == S and cert['H'] == H and cert['J'] == J
    assert cert['selected_manifest'] == MANIFEST and not cert['failures']
    assert digest(HERE/'l148_rank20_gates.py') == cert['code_sha256']
    bound = cert['input_sha256']
    assert all(digest(HERE/name) == value for name, value in bound.items())
    audit = read('l148-critical-audit.json')
    assert not audit['failures'] and audit['original_artifacts_byte_unchanged']
    assert all(c['passes'] for c in audit['checks'])
    assert all(bound[name] == value for name, value in audit['input_sha256'].items())
    oa = read('l125-critical-audit.json')
    assert not oa['failures'] and oa['original_artifacts_byte_unchanged']
    assert oa['full_saved_replay_identical']
    assert oa['summary']['actual_cases'] == oa['summary']['required_cases'] == 100764
    source = read('l147-literal-reuse.json')
    source_replay = read('l147-literal-reuse-replay.json')
    assert source_replay['certificate_sha256'] == bound['l147-literal-reuse.json']
    assert source['unmatched_indices'] == source_replay['unmatched_indices'] == MANIFEST
    assert not source['failures'] and not source_replay['failures']
    master = read('new-pair-filter.json')
    assert bound['new-pair-filter.json'] == oa['audited_input_hashes']['new-pair-filter.json']
    assert master['residual_occurrences'] == source['historical_residual_occurrences']
    assert len(master['residual_occurrences']) == 154
    universe = [[list(i), list(k)] for i in combinations(S, 2) for k in combinations(J, 2)]
    assert master['universe'] == universe and len(universe) == 756
    first = [[[1, 8], [47, 50]], [[12, 18], [64, 75]]]
    assert master['first_two'] == first
    fi = [universe.index(row) for row in first]
    assert fi == master['first_indices']
    assert len(cert['records']) == 8
    reports, classifications = [], []
    total_ext = total_proj = 0
    for index, rec in zip(MANIFEST, cert['records']):
        n, f = index
        assert rec['indices'] == index
        old = next(r for r in source['overlay'] if r['indices'] == index)
        assert old['disposition'] == 'unmatched'
        shard_name = rec['shard']
        assert bound[shard_name] == oa['audited_input_hashes'][shard_name]
        shard = read(shard_name)
        assert shard['third_index'] == n and rec['shard'] == old['shard']
        assert rec['case_pointer'] == old['case_pointer']
        position = int(rec['case_pointer'].split('/')[-1])
        case = shard['cases'][position]
        assert [r for r in shard['cases'] if r['fourth_index'] == f] == [case]
        assert case == rec['complete_original_record'] == old['complete_original_record']
        assert case['status'] == 'residual' and case['rank'] == 20
        rows = [dict(I=universe[t][0], K=universe[t][1]) for t in fi+index]
        assert rows == rec['rows'] == old['rows']
        supports = [set(r['I']+r['K']) for r in rows]
        assert len(set(map(tuple, map(sorted, supports)))) == 4
        assert all(len(a & b) <= 1 for a, b in combinations(supports, 2))
        blocks = [block(r['I'], r['K']) for r in rows]
        matrix = [r for q, g, z, ext in blocks for r in ext]
        assert matrix == rec['original_matrix'] == old['original_matrix']
        for row, (q, g, z, ext), inp, t in zip(rows, blocks, rec['row_inputs'], fi+index):
            assert inp['original_block'] == master['blocks'][t]
            assert inp['I'] == row['I'] and inp['K'] == row['K'] and inp['z'] == z
            assert inp['g_roots'] == [x for x in J if x not in row['K']]
            assert q == inp['original_block']['covectors'] and ext == inp['original_block']['matrix']
            assert {str(x): g[x] for x in S+row['K']} == inp['g_values_on_S_union_K']
            # Every coefficient independently follows from elementary symmetric sums.
            roots = inp['g_roots']
            coeff = []
            for d in range(8):
                terms = []
                for subset in combinations(roots, 7-d):
                    value = 1
                    for x in subset:
                        value *= x
                    terms.append(value)
                coeff.append((-1)**(7-d)*sum(terms) % P)
            assert coeff == inp['g_coefficients_ascending']
        assert rec['row_inputs'] == old['row_inputs']
        assert rank(matrix) == 20
        fresh_rank, fresh_basis = independent_nullspace(matrix)
        assert fresh_rank == 20 and len(fresh_basis) == 1
        [p] = rec['kernel_basis']
        assert rec['kernel_basis'] == case['kernel_basis'] == old['kernel_basis']
        proportional(fresh_basis[0], p)
        assert rec['free_columns'] == old['free_columns'] and len(rec['free_columns']) == 1
        assert p[rec['free_columns'][0]] == 1
        assert [[dot(r, p) for r in matrix]] == rec['kernel_residuals'] == case['kernel_residuals'] == [[0]*24]
        assert rec['rank_minor_rows'] == case['minor_rows'] and rec['rank_minor_columns'] == case['pivot_columns']
        assert len(rec['rank_minor_rows']) == len(set(rec['rank_minor_rows'])) == 20
        assert len(rec['rank_minor_columns']) == len(set(rec['rank_minor_columns'])) == 20
        minor = [[matrix[r][c] for c in rec['rank_minor_columns']] for r in rec['rank_minor_rows']]
        assert determinant(minor) == rec['rank_minor_residue'] == case['minor_residue'] != 0
        skew = [[0]*7 for _ in S]
        for (a, b), value in zip(PAIRS, p):
            skew[a][b], skew[b][a] = value, -value % P
        plucker = [(skew[a][b]*skew[c][d]-skew[a][c]*skew[b][d]+skew[a][d]*skew[b][c]) % P
                   for a, b, c, d in QUADS]
        assert plucker == rec['plucker_values'] == [0]*35 and rec['decomposable']
        point = rec['plane_and_all_row_gates']
        pivots = [pair for pair, value in zip(PAIRS, p) if value]
        u, v = plane(p, pivots[0])
        assert point['pivot_indices'] == list(pivots[0])
        assert point['u'] == u and point['v'] == v and point['bivector'] == p
        assert len(point['row_gates']) == 4
        row_reports, lines = [], []
        for row, (q, g, z, ext), gate in zip(rows, blocks, point['row_gates']):
            qu, qv = [dot(c, u) for c in q], [dot(c, v) for c in q]
            assert qu == gate['Q_u'] and qv == gate['Q_v']
            assert [(qu[a]*qv[b]-qu[b]*qv[a]) % P for a, b in combinations(range(4), 2)] == gate['projection_minors'] == [0]*6
            assert any(qu+qv) and gate['projection_rank'] == 1
            m = next(m for m in range(4) if qu[m] or qv[m])
            alpha, beta = -qv[m] % P, qu[m]
            h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
            assert any(h) and [alpha, beta] == gate['direction_coefficients']
            assert h == gate['intersection_vector'] and all(dot(c, h) == 0 for c in q)
            lam = h[S.index(z)]*pow(g[z], -1, P) % P
            weights = [(h[S.index(x)]-lam*g[x]) % P for x in row['I']] + [-lam*g[x] % P for x in row['K']]
            assert lam == gate['lambda_value'] and weights == gate['error_weights']
            assert weights[:2] == gate['overlap_weights']
            failed = (['lambda_zero'] if lam == 0 else []) + [f'overlap_weight_zero_at_{x}' for x, e in zip(row['I'], weights) if not e]
            assert failed == gate['failed_gates'] and gate['passes'] == (not failed)
            error = dict(zip(row['I']+row['K'], weights))
            identity = [((h[S.index(x)] if x in S else 0)-error.get(x, 0)-lam*g[x]) % P for x in H]
            moments = [sum(((h[S.index(x)] if x in S else 0)-error.get(x, 0))*pow(x, d, P) for x in H) % P for d in range(1, 9)]
            assert identity == gate['h_minus_error_minus_lambda_g_on_H'] == [0]*16
            assert moments == gate['moment_residuals'] == [0]*8
            assert gate['prescribed_finite_gate'] == {'D_coefficient': alpha, 'C_coefficient': -beta % P}
            mm = [[sum(u[S.index(x)]*pow(x, d, P) for x in S) % P,
                   sum(v[S.index(x)]*pow(x, d, P) for x in S) % P]
                  +[-pow(x, d, P) % P for x in row['I']+row['K']] for d in range(1, 9)]
            mrank, mbasis = independent_nullspace(mm)
            assert mrank == rank(mm) == 5 and len(mbasis) == 1
            proportional(mbasis[0], [alpha, beta]+weights)
            row_reports.append(dict(direction=[alpha, beta], lambda_value=lam, weights=weights,
                                    failed_gates=failed, moment_matrix=mm, moment_rank=mrank, moment_kernel=mbasis[0]))
            lines.append(h)
        passes = all(not r['failed_gates'] for r in row_reports)
        assert point['passes_intrinsic_gates'] == passes
        disposition = 'intrinsic_survivor' if passes else 'excluded_necessary_gates'
        assert rec['disposition'] == disposition
        alternatives = []
        for pivot in pivots:
            uu, vv = plane(p, pivot)
            for row_number, (row, (q, g, z, ext)) in enumerate(zip(rows, blocks)):
                aa, bb = [dot(c, uu) for c in q], [dot(c, vv) for c in q]
                assert rank([[a, b] for a, b in zip(aa, bb)]) == 1
                for m in range(4):
                    if not (aa[m] or bb[m]):
                        continue
                    hh = [(-bb[m]*x+aa[m]*y) % P for x, y in zip(uu, vv)]
                    ratio = proportional(hh, lines[row_number])
                    lam = hh[S.index(z)]*pow(g[z], -1, P) % P
                    weights = [(hh[S.index(x)]-lam*g[x]) % P for x in row['I']] + [-lam*g[x] % P for x in row['K']]
                    assert lam == ratio*row_reports[row_number]['lambda_value'] % P
                    assert weights == [ratio*x % P for x in row_reports[row_number]['weights']]
                    alternatives.append(dict(pivot=list(pivot), row=row_number+1, component=m,
                                             scale=ratio, lambda_value=lam, error_weights=weights))
        total_ext += len(pivots)
        total_proj += len(alternatives)
        directions = [r['direction'] for r in row_reports]
        determinants = [(a*d-b*c) % P for (a, b), (c, d) in combinations(directions, 2)]
        if passes:
            assert all(determinants)
        classifications.append(dict(indices=index, minor=rec['rank_minor_residue'], u=u, v=v,
                                    rows=rows, row_gates=[{k: r[k] for k in ('direction','lambda_value','weights','failed_gates')} for r in row_reports],
                                    disposition=disposition))
        reports.append(dict(indices=index, independent_kernel=fresh_basis, row_replay=row_reports,
                            all_pivot_replay=alternatives, direction_determinants=determinants))
    expected = dict(actual_records=8, required_records=8, rank=20, kernel_dimension=1,
                    nonzero_original_minors=8, original_entries=4032, plucker_values=280,
                    decomposable_points=8, dispositions=dict(Counter(r['disposition'] for r in classifications)),
                    projection_ranks={'1': 32}, failed_gates=dict(Counter(f for r in classifications for g in r['row_gates'] for f in g['failed_gates'])))
    assert cert['summary'] == expected
    groups = []
    for rec in classifications:
        group = next((g for g in groups if g['u'] == rec['u']), None)
        if group is None:
            group = dict(u=rec['u'], v=rec['v'], indices=[], disposition=rec['disposition'])
            groups.append(group)
        assert group['v'] == rec['v'] and group['disposition'] == rec['disposition']
        group['indices'].append(rec['indices'])
    assert len(groups) == 4 and all(len(g['indices']) == 2 for g in groups)
    assert all(g['indices'][0] == list(reversed(g['indices'][1])) for g in groups)
    assert all(r['u'][:2] == [1, 0] and r['v'][0] == 0 and r['v'][1] for r in classifications)
    assert sum(g['disposition'] == 'intrinsic_survivor' for g in groups) == 2
    assert digest(path) == before and all(digest(HERE/name) == value for name, value in bound.items())
    summary = dict(expected, all_nonzero_exterior_pivots=total_ext, all_nonzero_projection_pivots=total_proj,
                   original_moment_matrices_rank5=32, original_moment_residuals=256,
                   pointwise_entries=512, distinct_planes=4, surviving_planes=2,
                   source_files_unchanged=len(bound))
    out = dict(certificate_sha256=before, code_sha256=digest(Path(__file__)),
               helper_sha256={name: digest(HERE/name) for name in
                              ('verify_active_rank19_complete_loci.py','verify_rank20_selected_gates.py')},
               summary=summary, classification=classifications, plane_groups=groups, records=reports, failures=[])
    target = HERE/'l148-rank20-gates-replay.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Records 8/8; all moment ranks 5/6; failures 0; {target}')


if __name__ == '__main__':
    run()
