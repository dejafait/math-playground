"""Exactly eight approved L148 rank-20 kernels; necessary L109 tests only."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import l139_literal_reuse as original
import residual_kernel_gates as gates
import zero_anchor_support_filter as direct

HERE = Path(__file__).resolve().parent
MANIFEST = [[467, 750], [499, 668], [608, 695], [668, 499],
            [678, 749], [695, 608], [749, 678], [750, 467]]
CHART = ('u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0; '
         'require D*alpha-C*beta!=0 for each rank-one direction; '
         'divide h,lambda,error by (D*alpha-C*beta)/(AD-BC) if finite.')


def run():
    assert __debug__
    audit = original.read('l148-critical-audit.json')
    assert not audit['failures'] and audit['original_artifacts_byte_unchanged']
    assert all(c['passes'] for c in audit['checks'])
    for name, value in audit['input_sha256'].items():
        assert sha256(original.raw(name)).hexdigest() == value, name
    source = original.bound('l147-literal-reuse.json', audit['input_sha256']['l147-literal-reuse.json'])
    replay = original.bound('l147-literal-reuse-replay.json', audit['input_sha256']['l147-literal-reuse-replay.json'])
    assert not source['failures'] and not replay['failures']
    assert source['unmatched_indices'] == replay['unmatched_indices'] == MANIFEST
    oa = original.read('l125-critical-audit.json')
    assert not oa['failures'] and oa['original_artifacts_byte_unchanged']
    assert oa['full_saved_replay_identical']
    assert oa['summary']['actual_cases'] == oa['summary']['required_cases'] == 100764
    master = original.bound('new-pair-filter.json', oa['audited_input_hashes']['new-pair-filter.json'])
    assert not master['failures'] and len(master['residual_occurrences']) == 154
    assert source['historical_residual_occurrences'] == master['residual_occurrences']
    universe = [[list(i), list(k)] for i in combinations(original.S, 2) for k in combinations(original.J, 2)]
    assert universe == master['universe'] and len(universe) == 756
    assert master['first_two'] == [[[1, 8], [47, 50]], [[12, 18], [64, 75]]]
    assert master['column_pairs'] == [[original.S[a], original.S[b]] for a, b in original.PAIRS]
    for name in ('l139_literal_reuse.py', 'verify_new_pair_filter.py',
                 'verify_fixed_three_row_extensions.py', 'residual_kernel_gates.py',
                 'zero_anchor_support_filter.py'):
        original.raw(name)
    records = []
    for index in MANIFEST:
        old = next(r for r in source['overlay'] if r['indices'] == index)
        assert old['disposition'] == 'unmatched' and old['mismatch']['kind'] == 'basis_length'
        shard_name = old['shard']
        shard = original.bound(shard_name, oa['audited_input_hashes'][shard_name])
        assert original.HASHES[shard_name] == audit['input_sha256'][shard_name]
        position = int(old['case_pointer'].split('/')[-1])
        case = shard['cases'][position]
        n, f = index
        assert shard['third_index'] == n and case['fourth_index'] == f
        assert [r for r in shard['cases'] if r['fourth_index'] == f] == [case]
        assert case == old['complete_original_record'] and case['status'] == 'residual'
        row_indices = master['first_indices'] + index
        rows = [dict(I=universe[t][0], K=universe[t][1]) for t in row_indices]
        assert rows == old['rows']
        supports = [set(r['I']+r['K']) for r in rows]
        assert len(set(map(tuple, map(sorted, supports)))) == 4
        assert all(len(a & b) <= 1 for a, b in combinations(supports, 2))
        inputs = [original.inputs(row) for row in rows]
        assert inputs == old['row_inputs']
        assert [r['original_block'] for r in inputs] == [master['blocks'][t] for t in row_indices]
        matrix = [r for inp in inputs for r in inp['original_block']['matrix']]
        columns, basis = original.column_kernel(matrix)
        assert matrix == old['original_matrix']
        assert columns == case['pivot_columns'] and basis == case['kernel_basis'] == old['kernel_basis']
        assert len(columns) == case['rank'] == old['rank'] == 20 and len(basis) == 1
        free = sorted(set(range(21))-set(columns))
        assert free == old['free_columns'] and basis[0][free[0]] == 1
        residuals = [[sum(a*b for a, b in zip(r, v)) % 97 for r in matrix] for v in basis]
        assert residuals == case['kernel_residuals'] and not any(map(any, residuals))
        minor = [[matrix[r][c] for c in columns] for r in case['minor_rows']]
        det = original.determinant(minor)
        assert det == case['minor_residue'] == old['rank_minor_residue'] != 0
        quadrics = gates.plucker_polynomials(basis)
        assert len(quadrics) == 35 and all(q[1:] == [0, 0] for q in quadrics)
        values = [q[0] for q in quadrics]
        rec = dict(indices=index, shard=shard_name, case_pointer=old['case_pointer'],
                   complete_original_record=case, rows=rows, row_inputs=inputs,
                   original_matrix=matrix, kernel_basis=basis, free_columns=free,
                   kernel_residuals=residuals, rank_minor_rows=case['minor_rows'],
                   rank_minor_columns=columns, rank_minor_residue=det,
                   plucker_values=values, decomposable=not any(values))
        if any(values):
            t = next(t for t, value in enumerate(values) if value)
            rec['nonzero_plucker_witness'] = dict(indices=list(gates.QUADS[t]), value=values[t])
            rec['disposition'] = 'excluded_nondecomposable'
        else:
            point = gates.plane_gates(basis[0], rows)
            for row, gate in zip(rows, point['row_gates']):
                if gate['projection_rank'] == 0:
                    continue
                error = dict(zip(row['I']+row['K'], gate['error_weights']))
                identity = [((gate['intersection_vector'][original.S.index(x)] if x in original.S else 0)
                             -error.get(x, 0)-gate['lambda_value']*direct.g(row['K'], x)) % 97
                            for x in original.H]
                assert not any(identity) and not any(gate['moment_residuals'])
                gate['h_minus_error_minus_lambda_g_on_H'] = identity
            rec['plane_and_all_row_gates'] = point
            rec['disposition'] = ('intrinsic_survivor' if point['passes_intrinsic_gates']
                                  else 'excluded_necessary_gates')
        records.append(rec)
    points = [r['plane_and_all_row_gates'] for r in records if r['decomposable']]
    row_gates = [g for p in points for g in p['row_gates']]
    summary = dict(actual_records=len(records), required_records=8, rank=20, kernel_dimension=1,
                   nonzero_original_minors=len(records), original_entries=504*len(records),
                   plucker_values=35*len(records), decomposable_points=len(points),
                   dispositions=dict(Counter(r['disposition'] for r in records)),
                   projection_ranks=dict(Counter(g['projection_rank'] for g in row_gates)),
                   failed_gates=dict(Counter(f for g in row_gates for f in g['failed_gates'])))
    assert [r['indices'] for r in records] == MANIFEST
    for name, value in original.HASHES.items():
        assert sha256((HERE/name).read_bytes()).hexdigest() == value, name
    out = dict(step_id='2026-10-24-mca-453-l148-rank20-gates', modulus=97,
               S=original.S, H=original.H, J=original.J, selected_manifest=MANIFEST,
               input_sha256=original.HASHES, code_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               original_chart_condition=CHART, summary=summary, records=records,
               original_inputs_unchanged=True, failures=[],
               qualification='Necessary selected-row classification only; separate critical audit pending.')
    target = HERE/'l148-rank20-gates.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Records {len(records)}/8; rank 20/21; kernel dimension 1/1; failures 0; {target}')


if __name__ == '__main__':
    run()
