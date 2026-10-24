"""Exactly the approved first L138 mismatch (175,274), including its entire homogeneous locus."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import residual_kernel_gates as gates

HERE = Path(__file__).resolve().parent
P = 97
ROWS = [{'I': i, 'K': k} for i, k in [
    ([1, 8], [47, 50]), ([12, 18], [64, 75]),
    ([1, 27], [79, 89]), ([8, 18], [70, 79])]]


def run():
    source_path = HERE/'new-pair-filter/third-175.json'
    raw = source_path.read_bytes()
    shard = json.loads(raw)
    assert shard['third_index'] == 175
    records = [r for r in shard['cases'] if r['fourth_index'] == 274]
    assert len(records) == 1 and shard['cases'][33] == records[0]
    record = records[0]
    basis = record['kernel_basis']
    assert len(basis) == 2 and all(len(b) == 21 for b in basis)
    overlay_path = HERE/'l137-literal-reuse.json'
    overlay_raw = overlay_path.read_bytes()
    overlay = json.loads(overlay_raw)['overlay'][8]
    assert overlay['indices'] == [175, 274]
    assert overlay['case_pointer'] == '/cases/33'
    assert overlay['shard'] == 'new-pair-filter/third-175.json'
    assert overlay['complete_original_record'] == record
    assert overlay['rows'] == ROWS and overlay['disposition'] == 'unmatched'
    assert all(not c['covered'] and not c['point_row_bindings'] for c in overlay['comparisons'])
    audit_raw = (HERE/'l138-critical-audit.json').read_bytes()
    audit = json.loads(audit_raw)
    assert audit['failures'] == [] and all(c['passes'] for c in audit['checks'])
    assert audit['input_sha256']['l137-literal-reuse.json'] == sha256(overlay_raw).hexdigest()
    assert audit['input_sha256']['new-pair-filter/third-175.json'] == sha256(raw).hexdigest()
    assert record['status'] == 'residual' and record['rank'] == 19
    assert record['kernel_basis'] == basis
    assert record['pivot_columns'] == [c for c in range(21) if c not in (2, 10)]
    supports = [set(r['I']+r['K']) for r in ROWS]
    assert len({tuple(sorted(r)) for r in supports}) == 4
    assert all(len(a & b) <= 1 for a,b in combinations(supports, 2))
    universe = [(list(i), list(k)) for i in combinations(direct.S, 2)
                for k in combinations(direct.J, 2)]
    assert universe[175] == (ROWS[2]['I'], ROWS[2]['K'])
    assert universe[274] == (ROWS[3]['I'], ROWS[3]['K'])
    blocks = [direct.block(r['I'], r['K']) for r in ROWS]
    matrix = [r for block in blocks for r in block['matrix']]
    residuals = [[sum(a*b for a, b in zip(v, r)) % P for r in matrix] for v in basis]
    assert residuals == record['kernel_residuals'] and not any(map(any, residuals))
    rank, selected = direct.rank_and_rows(matrix)
    columns = [c for c in range(21) if c not in (2, 10)]
    minor = [[matrix[r][c] for c in columns] for r in selected]
    residue = direct.determinant(minor)
    integer_det = direct.integer_determinant(minor)
    assert rank == record['rank'] == 19 and len(minor) == 19
    assert residue and integer_det % P == residue
    assert selected == record['minor_rows'] and residue == record['minor_residue']
    quadrics = gates.plucker_polynomials(basis)
    assert len(quadrics) == 35 and all(q[0] == q[2] == 0 for q in quadrics)
    nonzero = [n for n, q in enumerate(quadrics) if q[1]]
    assert nonzero
    affine = [gates.trim(q) for q in quadrics]
    gcd, bezout = gates.gcd_certificate(affine)
    quotients = [gates.divrem(q, gcd)[0] for q in affine]
    assert gcd == [0, 1]
    # Thus every extension-field solution has st=0. Both endpoints
    # are explicit wedges, verified again by pivot reconstruction.
    points = [gates.plane_gates(b, ROWS) for b in basis]
    for point in points:
        assert not point['passes_intrinsic_gates']
        for row, block, gate in zip(ROWS, blocks, point['row_gates']):
            gate['g_values_on_S_union_K'] = {
                str(x): direct.g(row['K'], x) for x in direct.S+row['K']}
            if gate['projection_rank'] == 0:
                # Rejected by L109 nonpersistence, before finite/weight
                # gates: there is no unique projective intersection.
                continue
            error = dict(zip(row['I']+row['K'], gate['error_weights']))
            identity = [((gate['intersection_vector'][direct.S.index(x)]
                          if x in direct.S else 0)-error.get(x, 0)
                         -gate['lambda_value']*direct.g(row['K'], x)) % P for x in direct.H]
            assert not any(identity) and not any(gate['moment_residuals'])
            gate['h_minus_error_minus_lambda_g_on_H'] = identity
            gate['original_basis_convention'] = 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0'
            gate['original_first_coefficient'] = '(D*alpha-C*beta)/(AD-BC)'
    row_gates = [g for p in points for g in p['row_gates']]
    out = {
        'modulus': P, 'H': direct.H, 'S': direct.S, 'J': direct.J, 'rows': ROWS,
        'source': {'path': str(source_path.relative_to(HERE)), 'sha256': sha256(raw).hexdigest(),
                   'pointer': '/cases/33', 'full_universe_indices': [175, 274]},
        'audited_mismatch_binding': {'path': 'l137-literal-reuse.json', 'pointer': '/overlay/8',
                                      'sha256': sha256(overlay_raw).hexdigest(), 'complete_overlay': overlay},
        'mismatch_audit_binding': {'path': 'l138-critical-audit.json', 'sha256': sha256(audit_raw).hexdigest(),
                                   'checks_passed': len(audit['checks'])},
        'column_pairs': [[direct.S[a], direct.S[b]] for a, b in direct.PAIRS],
        'blocks': blocks, 'original_matrix': matrix, 'kernel_basis': basis,
        'free_columns': [2, 10], 'kernel_residuals': residuals,
        'rank_minor_rows': selected, 'rank_minor_columns': columns,
        'rank_minor': minor, 'rank_minor_residue': residue,
        'rank_minor_integer_determinant': integer_det,
        'plucker_quadruples': [[direct.S[a] for a in q] for q in combinations(range(7), 4)],
        'plucker_coefficients_s2_st_t2': quadrics, 'nonzero_plucker_indices': nonzero,
        'affine_gcd': gcd, 'bezout_coefficients': bezout,
        'affine_quotients': quotients,
        'complete_projective_parameter_locus': [[1, 0], [0, 1]],
        'points_and_all_row_gates': points,
        'summary': {'actual_loci': 1, 'required_loci': 1, 'rank': rank,
                    'kernel_dimension': 2, 'basis_residuals': 48,
                    'plucker_equations': 35, 'nonzero_plucker_equations': len(nonzero),
                    'complete_projective_points': 2, 'row_tests': 8,
                    'rank_zero_rows': sum(g['projection_rank'] == 0 for g in row_gates),
                    'rank_one_rows': sum(g['projection_rank'] == 1 for g in row_gates),
                    'lambda_zero_rows': sum(g.get('lambda_value') == 0 for g in row_gates),
                    'full_weight_rows': sum(g['passes'] for g in row_gates),
                    'intrinsically_passing_points': sum(p['passes_intrinsic_gates'] for p in points),
                    'unresolved_branches': 0},
        'scope': 'One four-row necessary-gate exclusion over every extension and prescribed chart; separate audit pending.',
        'failures': []}
    path = HERE/'first-l138-mismatch-locus-gates.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print(f'Rank {rank}/21; minor {residue}!=0; complete locus st=0; '
          f'passing planes 0/2; failures 0; certificate: {path}')


if __name__ == '__main__':
    run()
