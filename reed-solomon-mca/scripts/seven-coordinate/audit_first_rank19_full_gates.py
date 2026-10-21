"""Step-325 separate audit: replay the exact approved occurrence, never a census."""
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent


def run():
    before = json.loads((HERE/'first-rank19-critical-audit-before.json').read_text())
    runs = []
    for name in ['first_rank19_full_gates.py', 'verify_first_rank19_full_gates.py']:
        result = subprocess.run([sys.executable, str(HERE/name)],
                                capture_output=True, text=True, check=True)
        runs.append({'program': name, 'returncode': result.returncode,
                     'stdout': result.stdout, 'stderr': result.stderr})
    after = {name: sha256((HERE/name).read_bytes()).hexdigest() for name in before}
    assert after == before, 'A source, program or complete certificate changed on replay'
    cert = json.loads((HERE/'first-rank19-full-gates.json').read_text())
    replay = json.loads((HERE/'first-rank19-full-gates-replay.json').read_text())
    source = json.loads((HERE/'residual-coordinate-factors/third-000.json').read_text())['cases'][3]
    checks = []

    def check(name, condition):
        checks.append({'check': name, 'passed': bool(condition)})
        assert condition, name

    check('H has sixteen distinct nonzero roots of X^16-1',
          len(cert['H']) == len(set(cert['H'])) == 16 and
          all(x != 0 and pow(x, 16, 97) == 1 for x in cert['H']))
    check('four complete blocks and exact original matrix shape',
          len(cert['blocks']) == 4 and len(cert['original_matrix']) == 24 and
          all(len(b['covectors']) == 4 and all(len(c) == 7 for c in b['covectors'])
              and len(b['matrix']) == 6 and all(len(r) == 21 for r in b['matrix'])
              for b in cert['blocks']) and
          all(len(row) == 21 for row in cert['original_matrix']))
    check('written minor rows and columns match complete certificate',
          cert['rank_minor_rows'] == list(range(16))+[18, 19, 20] and
          cert['rank_minor_columns'] == [c for c in range(21) if c not in [2, 6]])
    check('written exact determinant and nonzero residue',
          cert['rank_minor_integer_determinant'] == -1442234786736581438195068452790272 and
          cert['rank_minor_residue'] == 27)
    check('two complete independent null vectors and all 48 original residuals',
          cert['kernel_basis'] == [[int(c == n) for c in range(21)] for n in [2, 6]] and
          cert['kernel_residuals'] == [[0]*24, [0]*24])
    check('complete 35 homogeneous restrictions, unique st equation',
          cert['plucker_coefficients_s2_st_t2'] == [[0, 1, 0]]+[[0, 0, 0]]*34 and
          len(cert['plucker_quadruples']) == 35 and
          cert['plucker_quadruples'][0] == [1, 8, 12, 18])
    points = cert['points_and_all_row_gates']
    check('both projective endpoints and all eight row records retained',
          cert['complete_projective_parameter_locus'] == [[1, 0], [0, 1]] and
          len(points) == 2 and all(len(p['row_gates']) == 4 for p in points) and
          len(replay['all_row_replay']) == 8)
    table = [[(1, 53), (18, 38), (1, 4), (18, 89)],
             [(8, 81), (12, 72), (12, 6), (8, 65)]]
    for n, point in enumerate(points):
        for j, gate in enumerate(point['row_gates']):
            c, a = table[n][j]
            check(f'point {n}, row {j+1}: exact written representative and rank-one failure',
                  gate['intersection_vector'] == [a if x == c else 0 for x in cert['S']] and
                  gate['projection_rank'] == 1 and gate['lambda_value'] == 0 and
                  len(gate['error_weights']) == 4 and gate['error_weights'].count(0) == 3 and
                  not gate['passes'])
            check(f'point {n}, row {j+1}: all shifted moments and pointwise entries',
                  gate['moment_residuals'] == [0]*8 and
                  gate['h_minus_error_values_on_H'] == [0]*16)
            check(f'point {n}, row {j+1}: prescribed chart convention',
                  gate['original_basis_convention'] ==
                  'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0' and
                  gate['original_first_coefficient'] == '(D*alpha-C*beta)/(AD-BC)')
    check('historical record identity, complete basis and preserved filter failures',
          source['third_index'] == 0 and source['fourth_index'] == 279 and
          source['rank'] == 19 and source['status'] == 'unresolved' and
          source['kernel_basis'] == cert['kernel_basis'] and
          source['original_stack_residuals'] == cert['kernel_residuals'] and
          len(source['factor_tests']) == 8 and all(not t['contained'] for t in source['factor_tests']))
    check('complete independent matrix and homogeneous evidence agree',
          replay['rebuilt_original_matrix'] == cert['original_matrix'] and
          replay['kernel_residuals'] == cert['kernel_residuals'] and
          replay['plucker_coefficients_s2_st_t2'] == cert['plucker_coefficients_s2_st_t2'] and
          replay['certificate_sha256'] == after['first-rank19-full-gates.json'])
    check('both complete programs report no failures', cert['failures'] == replay['failures'] == [])
    out = {'step_id': '2026-10-18-mca-325-first-rank19-critical-audit',
           'scope': 'Only L117 occurrence (0,279); analytical audit is canonical in L117.',
           'before_sha256': before, 'after_sha256': after, 'complete_artifacts_unchanged': True,
           'runs': runs, 'checks': checks, 'checked_representatives': table,
           'summary': {'passed_checks': len(checks), 'failed_checks': 0,
                       'actual_occurrences': 1, 'required_occurrences': 1,
                       'rank': 19, 'minor_residue': 27, 'kernel_dimension': 2,
                       'complete_projective_points': 2, 'row_gates': 8,
                       'lambda_zero': 8, 'required_lambda_nonzero': 8},
           'failures': [], 'limitations': 'Shared Python/residue arithmetic; no formal verification or broader census.'}
    target = HERE/'first-rank19-critical-audit.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Checks {len(checks)}/{len(checks)}; occurrences 1/1; rank 19, minor 27 != 0; '
          'full locus 2 points; lambda zero 8/8 against required nonzero; failures 0.')
    print(f'All seven scoped hashes unchanged; complete audit evidence: {target}')


if __name__ == '__main__':
    run()
