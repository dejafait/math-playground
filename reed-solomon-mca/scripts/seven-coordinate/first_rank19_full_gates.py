"""One approved rank-19 occurrence; exact whole-projective-line certificate.

Run: python3 scripts/seven-coordinate/first_rank19_full_gates.py
No census, four-row converse, or arbitrary-chart replacement is used.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import residual_kernel_gates as gates

HERE = Path(__file__).resolve().parent
P = 97
ROWS = [{'I': i, 'K': k} for i, k in [
    ([1, 8], [47, 50]), ([12, 18], [64, 70]),
    ([1, 12], [75, 79]), ([8, 18], [75, 85])]]


def run():
    source_path = HERE/'residual-coordinate-factors/third-000.json'
    raw = source_path.read_bytes()
    source = json.loads(raw)['cases'][3]
    assert (source['third_index'], source['fourth_index']) == (0, 279)
    assert source['four_rows'] == [[row['I'], row['K']] for row in ROWS]
    assert source['status'] == 'unresolved' and source['rank'] == 19
    blocks = [direct.block(row['I'], row['K']) for row in ROWS]
    matrix = [r for block in blocks for r in block['matrix']]
    basis = [[int(c == n) for c in range(21)] for n in (2, 6)]
    assert basis == source['kernel_basis'] and source['free_columns'] == [2, 6]
    residuals = [[sum(a*b for a, b in zip(v, r)) % P for r in matrix] for v in basis]
    assert residuals == source['original_stack_residuals'] and not any(map(any, residuals))
    rank, selected_rows = direct.rank_and_rows(matrix)
    selected_columns = [c for c in range(21) if c not in (2, 6)]
    minor = [[matrix[r][c] for c in selected_columns] for r in selected_rows]
    assert rank == 19 and len(minor) == 19
    residue = direct.determinant(minor)
    integer_det = direct.integer_determinant(minor)
    assert residue != 0 and integer_det % P == residue
    quadrics = gates.plucker_polynomials(basis)
    assert len(quadrics) == 35
    assert all(q in ([0, 0, 0], [0, 1, 0]) for q in quadrics)
    nonzero = [n for n, q in enumerate(quadrics) if any(q)]
    assert len(nonzero) == 1
    quads = [[direct.S[a] for a in q] for q in combinations(range(7), 4)]
    assert quads[nonzero[0]] == [1, 8, 12, 18]
    # This coefficient identity proves the entire locus is st=0 over
    # every extension, not just over the 98 base-field projective points.
    points = [gates.plane_gates(b, ROWS) for b in basis]
    for point in points:
        assert not point['passes_intrinsic_gates']
        for row, block, gate in zip(ROWS, blocks, point['row_gates']):
            assert gate['projection_rank'] == 1 and gate['lambda_value'] == 0
            assert gate['error_weights'].count(0) == 3
            assert not any(gate['moment_residuals'])
            # Check the stronger pointwise polynomial identity h-e=0:
            # all field-scalar multiples and every original chart follow.
            error = dict(zip(row['I']+row['K'], gate['error_weights']))
            identity = [((gate['intersection_vector'][direct.S.index(x)]
                          if x in direct.S else 0)-error.get(x, 0)) % P for x in direct.H]
            assert not any(identity)
            gate['h_minus_error_values_on_H'] = identity
            gate['g_values_on_S_union_K'] = {
                str(x): direct.g(row['K'], x) for x in direct.S+row['K']}
            gate['original_basis_convention'] = 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0'
            gate['original_first_coefficient'] = '(D*alpha-C*beta)/(AD-BC)'
    out = {
        'modulus': P, 'H': direct.H, 'S': direct.S, 'J': direct.J, 'rows': ROWS,
        'source': {'path': str(source_path.relative_to(HERE)), 'sha256': sha256(raw).hexdigest(),
                   'pointer': '/cases/3', 'historical_indices': [0, 279]},
        'column_pairs': [[direct.S[a], direct.S[b]] for a, b in direct.PAIRS],
        'blocks': blocks, 'original_matrix': matrix, 'kernel_basis': basis,
        'free_columns': [2, 6], 'kernel_residuals': residuals,
        'rank_minor_rows': selected_rows, 'rank_minor_columns': selected_columns,
        'rank_minor': minor, 'rank_minor_residue': residue,
        'rank_minor_integer_determinant': integer_det,
        'plucker_quadruples': quads, 'plucker_coefficients_s2_st_t2': quadrics,
        'nonzero_plucker_indices': nonzero,
        'complete_projective_parameter_locus': [[1, 0], [0, 1]],
        'points_and_all_row_gates': points,
        'summary': {'actual_loci': 1, 'required_loci': 1, 'rank': rank,
                    'kernel_dimension': 2, 'basis_residuals': 48,
                    'plucker_equations': 35, 'complete_projective_points': 2,
                    'row_tests': 8, 'rank_one_rows': 8, 'lambda_zero_rows': 8,
                    'shifted_moment_residuals': 64, 'pointwise_identity_entries': 128,
                    'unresolved_branches': 0},
        'scope': 'One intrinsic four-row exclusion over every extension, all prescribed charts; separate audit pending.',
        'failures': []}
    path = HERE/'first-rank19-full-gates.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print(f'Rank {rank}/21; minor {residue}!=0; Plucker locus exactly st=0; '
          f'lambda zero 8/8, required nonzero; failures 0; certificate: {path}')


if __name__ == '__main__':
    run()
