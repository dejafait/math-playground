"""Exactly the six approved L118 rank-20 screen failures; necessary gates only."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import residual_kernel_gates as gates
import verify_fixed_three_row_extensions as derivative
from verify_inactive_coordinate_screen import nullspace

HERE = Path(__file__).resolve().parent
P = 97
MANIFEST = [[60, 666], [65, 671], [145, 696], [295, 197], [300, 202], [314, 382]]
CHART = ('u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0; '
         'require D*alpha-C*beta!=0 for each rank-one direction. '
         'Divide h,lambda,error by (D*alpha-C*beta)/(AD-BC) if finite.')


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    audit_path = HERE/'inactive-coordinate-partition-critical-audit.json'
    audit = json.loads(audit_path.read_bytes())
    assert not audit['failures'] and audit['replay_returncode'] == 0
    assert all(c['passed'] for c in audit['checks'])
    assert audit['artifact_hashes_before'] == audit['artifact_hashes_after']
    bound_hashes = {**audit['artifact_hashes_after'], **audit['code_hashes']}
    assert all(digest(HERE/name) == value for name, value in bound_hashes.items())
    source_path = HERE/'inactive-coordinate-screen.json'
    source = json.loads(source_path.read_bytes())
    assert digest(source_path) == '90b6f145c7993d33a834f3498fb3bee60f08ca328bd8e710af216a70df6172c1'
    assert digest(source_path) == audit['artifact_hashes_after'][source_path.name]
    assert not source['failures'] and all(c['passed'] for c in source['checks'])
    assert len(source['records']) == 599
    assert sum(r['status'] == 'screen_failure' for r in source['records']) == 239
    selected = [(i, r) for i, r in enumerate(source['records'])
                if r['status'] == 'screen_failure' and r['rank'] == 20]
    assert [[r['third_index'], r['fourth_index']] for i, r in selected] == MANIFEST
    assert [i for i, r in selected] == [264, 265, 538, 596, 597, 598]
    records = []
    for position, old in selected:
        rows = [{'I': i, 'K': k} for i, k in old['four_rows']]
        blocks = [direct.block(r['I'], r['K']) for r in rows]
        matrix = [r for b in blocks for r in b['matrix']]
        assert matrix == [r for row in rows for r in derivative.block(row['I'], row['K'])]
        pivots, basis = nullspace(matrix)
        assert len(pivots) == 20 and len(basis) == 1
        assert basis == old['kernel_basis']
        free = sorted(set(range(21))-set(pivots))
        assert free == old['free_columns'] and basis[0][free[0]] == 1
        residuals = [sum(x*y for x, y in zip(row, basis[0])) % P for row in matrix]
        assert not any(residuals)
        rank, minor_rows = direct.rank_and_rows(matrix)
        det = direct.determinant([[matrix[r][c] for c in pivots] for r in minor_rows])
        assert rank == 20 and det
        quadrics = gates.plucker_polynomials(basis)
        assert len(quadrics) == 35 and all(q[1:] == [0, 0] for q in quadrics)
        values = [q[0] for q in quadrics]
        rec = {'historical_index': [old['third_index'], old['fourth_index']],
               'source_record_position': position, 'rows': rows, 'original_matrix': matrix,
               'kernel_basis': basis, 'free_columns': free, 'kernel_residuals': residuals,
               'rank_minor_rows': minor_rows, 'rank_minor_columns': pivots,
               'rank_minor_residue': det, 'plucker_values': values,
               'decomposable': not any(values)}
        if any(values):
            n = next(n for n, value in enumerate(values) if value)
            rec['nonzero_plucker_witness'] = {'quad_indices': list(gates.QUADS[n]),
                                               'value': values[n]}
            rec['disposition'] = 'excluded_nondecomposable'
        else:
            point = gates.plane_gates(basis[0], rows)
            for row, gate in zip(rows, point['row_gates']):
                if gate['projection_rank'] == 0:
                    continue
                error = dict(zip(row['I']+row['K'], gate['error_weights']))
                identity = [((gate['intersection_vector'][direct.S.index(x)] if x in direct.S else 0)
                             -error.get(x, 0)-gate['lambda_value']*direct.g(row['K'], x)) % P
                            for x in direct.H]
                assert not any(identity) and not any(gate['moment_residuals'])
                gate['h_minus_error_minus_lambda_g_on_H'] = identity
            rec['plane_and_all_row_gates'] = point
            rec['disposition'] = ('intrinsic_survivor' if point['passes_intrinsic_gates']
                                  else 'excluded_necessary_gates')
        records.append(rec)
    points = [r['plane_and_all_row_gates'] for r in records if r['decomposable']]
    row_gates = [g for p in points for g in p['row_gates']]
    summary = {'required_occurrences': 6, 'processed_occurrences': len(records),
               'rank': 20, 'required_kernel_dimension': 1,
               'decomposable_points': len(points),
               'dispositions': dict(Counter(r['disposition'] for r in records)),
               'row_gates': len(row_gates),
               'projection_ranks': dict(Counter(g['projection_rank'] for g in row_gates)),
               'failed_gates': dict(Counter(f for g in row_gates for f in g['failed_gates'])),
               'surviving_indices': [r['historical_index'] for r in records
                                     if r['disposition'] == 'intrinsic_survivor']}
    assert all(digest(HERE/name) == value for name, value in bound_hashes.items())
    helpers = ['zero_anchor_support_filter.py', 'residual_kernel_gates.py',
               'verify_fixed_three_row_extensions.py', 'verify_inactive_coordinate_screen.py']
    out = {'scope': 'Exactly six L118 rank-20 screen failures; necessary L109 gates only',
           'modulus': P, 'H': direct.H, 'S': direct.S,
           'source_path': source_path.name, 'source_sha256': digest(source_path),
           'audit_path': audit_path.name, 'audit_sha256': digest(audit_path),
           'audited_hashes_checked_unchanged': len(bound_hashes),
           'code_sha256': digest(Path(__file__)),
           'helper_sha256': {name: digest(HERE/name) for name in helpers},
           'original_chart_condition': CHART, 'selected_manifest': MANIFEST,
           'summary': summary, 'records': records, 'failures': []}
    target = HERE/'rank20-selected-gates.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Processed {len(records)}/6; rank 20/21; kernel dimension 1/1; failures 0; certificate {target}')


if __name__ == '__main__':
    run()
