"""One approved rank-18 locus, with complete extension-field gate forms.

Reuses the established chart encoder, but not its named-third conclusions.
Run from the notebook: python3 scripts/seven-coordinate/first_rank18_full_gates.py
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import fixed_three_row_extensions as elimination
import nondisjoint_third_diagnostic as encoder

P = 97
HERE = Path(__file__).resolve().parent
S, H, J = direct.S, direct.H, direct.J
ROWS = [{'I': i, 'K': k} for i, k in [
    ([1, 8], [47, 50]), ([12, 18], [64, 70]),
    ([1, 12], [75, 79]), ([8, 12], [85, 89])]]
PAIRS = list(combinations(range(7), 2))


def run():
    shard_path = HERE/'remaining-third-factor-filter/third-000.json'
    raw = shard_path.read_bytes()
    shard = json.loads(raw)
    old = shard['cases'][249]
    assert old['I'] == ROWS[3]['I'] and old['K'] == ROWS[3]['K']
    matrix = [r for row in ROWS for r in direct.block(row['I'], row['K'])['matrix']]
    pivots, basis = elimination.rref_kernel(matrix)
    assert len(pivots) == old['rank'] == 18
    assert pivots == old['pivot_columns'] and basis == old['kernel_basis']
    residuals = [[sum(a*b for a, b in zip(v, row)) % P for row in matrix] for v in basis]
    assert residuals == old['kernel_residuals'] and not any(map(any, residuals))
    rank, minor_rows = direct.rank_and_rows(matrix)
    minor_residue = direct.determinant([[matrix[r][c] for c in pivots] for r in minor_rows])
    assert rank == 18 and minor_residue != 0
    factor = S.index(12)
    assert all(v[n] == 0 for v in basis for n, pair in enumerate(PAIRS) if factor not in pair)
    plucker = encoder.homogeneous_plucker(basis)
    assert len(plucker['coefficients']) == 35 and not any(map(any, plucker['coefficients']))
    gates = encoder.algebraic_charts(basis, ROWS, plucker)
    moment_checks = branches = nonempty = 0
    for chart in gates['charts']:
        if chart['status'] == 'empty_pivot_chart':
            continue
        nonempty += 1
        assert chart['rows'][1]['row_all_branches_excluded']
        for row, record in zip(ROWS, chart['rows']):
            i, k = row['I'], row['K']
            z = min(set(S)-set(i))
            gz = direct.g(k, z)
            record['rank_zero_branch'] = {
                'all_zero_linear_forms': record['Q_U_linear_forms']+record['Q_V_linear_forms'],
                'status': 'rejected_by_actual_nonpersistence_L109'}
            for branch in record['branches']:
                h = branch['intersection_vector_quadrics']
                lam = [v*pow(gz, -1, P) % P for v in h[S.index(z)]]
                error = {x: [(a-direct.g(k, x)*b) % P for a, b in zip(h[S.index(x)], lam)] for x in i}
                error.update({x: [-direct.g(k, x)*b % P for b in lam] for x in k})
                residual = [[sum((((h[S.index(x)][m] if x in S else 0)-error.get(x, [0]*6)[m])
                                  *pow(x, d, P)) for x in H) % P for m in range(6)] for d in range(1, 9)]
                assert not any(map(any, residual))
                branch.update(lambda_quadratic=lam,
                              error_label_order=i+k,
                              error_weight_quadrics=[error[x] for x in i+k],
                              original_shifted_moment_residual_quadrics=residual)
                moment_checks += 8*6
                branches += 1
        # The intrinsic second-row obstruction must hold independently of
        # whichever first excluded row the general encoder chose.
        for branch in chart['rows'][1]['branches']:
            assert not any(branch['weight_numerator_quadrics'][0])
            assert not any(branch['weight_numerator_quadrics'][2])
    assert gates['status'] == 'excluded_all_charts' and nonempty == 6
    result = {
        'modulus': P, 'H': H, 'S': S, 'J': J, 'rows': ROWS,
        'source': {'path': str(shard_path.relative_to(HERE)), 'sha256': sha256(raw).hexdigest(),
                   'pointer': '/cases/249'},
        'column_pairs': [[S[a], S[b]] for a, b in PAIRS],
        'original_matrix': matrix, 'pivot_columns': pivots, 'kernel_basis': basis,
        'rank_minor_rows': minor_rows, 'rank_minor_columns': pivots,
        'rank_minor_residue': minor_residue,
        'kernel_residuals': residuals, 'common_coordinate_factor': 12,
        'plucker_system': plucker, 'algebraic_gate_system': gates,
        'summary': {'actual_loci': 1, 'required_loci': 1, 'rank': 18,
                    'kernel_dimension': 3, 'basis_residuals': 72,
                    'plucker_equations': 35, 'projective_charts': 21,
                    'empty_charts': 15, 'nonempty_charts': nonempty,
                    'row_projection_pivots': branches, 'nonzero_alternatives': 2*branches,
                    'moment_coefficients': moment_checks, 'unresolved_charts': 0,
                    'excluded_row_number': 2},
        'scope': 'One four-row intrinsic exclusion over every extension; no four-row converse, census or separate audit.',
        'failures': []}
    path = HERE/'first-rank18-full-gates.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['summary'], sort_keys=True))
    print('Row 2 gates: required lambda!=0 and e18!=0; actual both identically zero on every rank-one branch.')
    print(f'Coverage: 1/1 loci, 35/35 Plucker equations, 21/21 charts; failures: 0; certificate: {path}')


if __name__ == '__main__':
    run()
