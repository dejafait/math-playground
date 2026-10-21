"""L125 occurrence (59,355): bind the new kernel and specialize audited L126."""
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
    ([1, 12], [70, 85]), ([8, 27], [79, 89])]]


def run():
    source_path = HERE/'new-pair-first-residual-gates.json'
    raw = source_path.read_bytes()
    source = json.loads(raw)
    assert source['source']['full_universe_indices'] == [58, 355]
    basis = source['kernel_basis']
    assert source['column_pairs'] == [[direct.S[a], direct.S[b]] for a,b in direct.PAIRS]
    assert basis == [[67, 68, 2, 44, 54, 1]+[0]*15, [0]*6+[1]+[0]*14]
    shard_path = HERE/'new-pair-filter/third-059.json'
    shard_raw = shard_path.read_bytes()
    shard = json.loads(shard_raw)
    assert shard['third_index'] == 59 and shard['residual_indices'] == [355, 647]
    records = [r for r in shard['cases'] if r['fourth_index'] == 355]
    assert len(records) == 1
    record = records[0]
    assert record['status'] == 'residual' and record['rank'] == 19
    assert record['kernel_basis'] == basis and record['pivot_columns'] == [c for c in range(21) if c not in (5, 6)]
    universe = [(list(i), list(k)) for i in combinations(direct.S, 2)
                for k in combinations(direct.J, 2)]
    assert universe[59] == (ROWS[2]['I'], ROWS[2]['K'])
    assert universe[355] == (ROWS[3]['I'], ROWS[3]['K'])
    blocks = [direct.block(r['I'], r['K']) for r in ROWS]
    matrix = [r for block in blocks for r in block['matrix']]
    residuals = [[sum(a*b for a, b in zip(v, r)) % P for r in matrix] for v in basis]
    assert residuals == record['kernel_residuals'] and not any(map(any, residuals))
    rank, selected = direct.rank_and_rows(matrix)
    columns = [c for c in range(21) if c not in (5, 6)]
    minor = [[matrix[r][c] for c in columns] for r in selected]
    residue = direct.determinant(minor)
    integer_det = direct.integer_determinant(minor)
    assert rank == record['rank'] == 19 and len(minor) == 19
    assert selected == record['minor_rows'] and columns == record['pivot_columns']
    assert residue == record['minor_residue'] == 54 and integer_det % P == residue
    for j in (0, 1, 3):
        assert ROWS[j] == source['rows'][j] and blocks[j] == source['blocks'][j]
    quadrics = gates.plucker_polynomials(basis)
    assert len(quadrics) == 35 and all(q[0] == q[2] == 0 for q in quadrics)
    nonzero = [n for n, q in enumerate(quadrics) if q[1]]
    assert nonzero
    affine = [gates.trim(q) for q in quadrics]
    gcd, bezout = gates.gcd_certificate(affine)
    quotients = [gates.divrem(q, gcd)[0] for q in affine]
    assert gcd == [0, 1]
    assert quadrics == source['plucker_coefficients_s2_st_t2']
    assert source['complete_projective_parameter_locus'] == [[1, 0], [0, 1]]
    # Import L126's complete extension-field locus after literal basis binding.
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
    for point, old in zip(points, source['points_and_all_row_gates']):
        for key in ('u', 'v', 'bivector', 'pivot_indices'):
            assert point[key] == old[key]
        for j in (0, 1, 3):
            assert point['row_gates'][j] == old['row_gates'][j]
    row_gates = [g for p in points for g in p['row_gates']]
    out = {
        'modulus': P, 'H': direct.H, 'S': direct.S, 'J': direct.J, 'rows': ROWS,
        'source': {'path': source_path.name, 'sha256': sha256(raw).hexdigest(),
                   'pointer': '/kernel_basis', 'full_universe_indices': [59, 355],
                   'shard_path': 'new-pair-filter/third-059.json',
                   'shard_sha256': sha256(shard_raw).hexdigest()},
        'column_pairs': [[direct.S[a], direct.S[b]] for a, b in direct.PAIRS],
        'blocks': blocks, 'original_matrix': matrix, 'kernel_basis': basis,
        'free_columns': [5, 6], 'kernel_residuals': residuals,
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
                    'intrinsically_passing_points': sum(p['passes_intrinsic_gates'] for p in points),
                    'unresolved_branches': 0},
        'import_binding': {'locus': 'L126', 'identical_rows': [1, 2, 4], 'changed_row': 3},
        'scope': 'One four-row necessary-gate exclusion over every extension and prescribed chart; separate audit pending.',
        'failures': []}
    path = HERE/'third59-first-residual-gates.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print(f'Rank {rank}/21; minor {residue}!=0; complete locus st=0; '
          f'passing planes 0/2; failures 0; certificate: {path}')


if __name__ == '__main__':
    run()
