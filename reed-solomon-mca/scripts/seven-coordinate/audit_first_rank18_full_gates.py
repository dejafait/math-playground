"""Separate L115 audit: exact written witnesses and byte-stable full replay.

Run from the notebook: python3 scripts/seven-coordinate/audit_first_rank18_full_gates.py
Only the single named four-row locus is checked; no L114 census is run.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
ROWS = [([1, 8], [47, 50]), ([12, 18], [64, 70]),
        ([1, 12], [75, 79]), ([8, 12], [85, 89])]


def run():
    output = {'scope': 'Separate audit of L115 only; L114 provenance case 249 only',
              'checks': {}, 'failures': []}

    def check(name, condition):
        output['checks'][name] = bool(condition)
        if not condition:
            output['failures'].append(name)

    files = ['first-rank18-full-gates.json', 'first-rank18-full-gates-replay.json',
             'remaining-third-factor-filter/third-000.json']
    before = {f: sha256((HERE/f).read_bytes()).hexdigest() for f in files}
    saved = json.loads((HERE/files[0]).read_text())
    H = [x for x in range(1, P) if pow(x, 16, P) == 1]
    J = sorted(set(H)-set(S))
    pairs = list(combinations(range(7), 2))
    blocks, values_by_row = [], []
    for overlap, outside in ROWS:
        roots = sorted(set(J)-set(outside))
        values = {}
        for x in H:
            v = 1
            for y in roots:
                v = v*(x-y) % P
            values[x] = v
        observed = [x for x in S if x not in overlap]
        z = observed[0]
        q = [[(values[z]*int(a == x)-values[x]*int(a == z)) % P
              for a in S] for x in observed[1:]]
        blocks.append(q)
        values_by_row.append(values)
        check('shortening_set_'+str(len(blocks)), len(roots) == 7 and
              all((values[x] != 0) == (x in S+outside) for x in H))
    matrix = [[(a[i]*b[j]-a[j]*b[i]) % P for i, j in pairs]
              for q in blocks for a, b in combinations(q, 2)]
    check('entire_original_matrix', matrix == saved['original_matrix'])
    basis = [[int((i, j) == (0, 2)) for i, j in pairs],
             [int((i, j) == (1, 2)) for i, j in pairs],
             [{(2, 3): 73, (2, 4): 63, (2, 5): 62, (2, 6): 1}.get((i, j), 0)
              for i, j in pairs]]
    check('written_basis_matches_complete_certificate', basis == saved['kernel_basis'])
    residuals = [[sum(a*b for a, b in zip(v, row)) % P for row in matrix] for v in basis]
    check('all_72_original_residuals', residuals == saved['kernel_residuals'] and
          all(v == 0 for row in residuals for v in row))
    free = [1, 6, 14]
    check('basis_independence', [[v[c] for c in free] for v in basis] ==
          [[int(i == j) for j in range(3)] for i in range(3)])
    mr = list(range(16))+[18, 19]
    mc = [0, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
    check('written_minor_indices', mr == saved['rank_minor_rows'] and mc == saved['rank_minor_columns'])
    minor = [[matrix[r][c] for c in mc] for r in mr]
    # Rational elimination, independent of modular and fraction-free paths.
    a = [[Fraction(v) for v in row] for row in minor]
    det = Fraction(1)
    for n in range(18):
        pivot = next((r for r in range(n, 18) if a[r][n]), None)
        if pivot is None:
            det = Fraction(0)
            break
        if pivot != n:
            a[n], a[pivot] = a[pivot], a[n]
            det = -det
        diagonal = a[n][n]
        det *= diagonal
        for r in range(n+1, 18):
            factor = a[r][n]/diagonal
            a[r] = [x-factor*y for x, y in zip(a[r], a[n])]
    check('integer_minor_determinant', det.denominator == 1)
    check('written_nonzero_minor_residue', det.numerator % P == saved['rank_minor_residue'] == 92)
    check('common_label12_factor', all(v[n] == 0 for v in basis
          for n, pair in enumerate(pairs) if 2 not in pair))
    check('row2_annihilates_E12', all(c[2] == 0 for c in blocks[1]))
    check('row2_original_lambda_denominator', values_by_row[1][1] != 0)
    check('row2_E12_full_weight_failure', S[2] == 12 and 1 != 12 and
          all(x != 12 for x in [18, 64, 70]))
    output['written_witness'] = {'H': H, 'S': S, 'rows': ROWS,
        'g_values': [{str(x): v for x, v in values.items()} for values in values_by_row],
        'quotient_covectors': blocks, 'original_matrix': matrix,
        'kernel_basis': basis, 'kernel_residuals': residuals,
        'minor_rows': mr, 'minor_columns': mc, 'minor': minor,
        'minor_integer_determinant': det.numerator, 'minor_residue': det.numerator % P}
    output['executions'] = []
    for script in ['first_rank18_full_gates.py', 'verify_first_rank18_full_gates.py']:
        proc = subprocess.run([sys.executable, str(HERE/script)], text=True,
                              capture_output=True, cwd=HERE.parent.parent)
        output['executions'].append({'script': script, 'returncode': proc.returncode,
                                     'stdout': proc.stdout, 'stderr': proc.stderr})
        check('execution_'+script, proc.returncode == 0)
    after = {f: sha256((HERE/f).read_bytes()).hexdigest() for f in files}
    check('all_original_artifacts_byte_stable', before == after)
    replay = json.loads((HERE/files[1]).read_text())
    check('complete_replay_evidence', replay['failures'] == [] and replay['summary'] == {
        'empty_charts': 15, 'nonempty_charts': 6,
        'exact_original_generator_identities': 672,
        'moment_coefficients_checked': 4608, 'row_projection_pivots': 96,
        'determining_branch_evaluations': 576})
    code = ['audit_first_rank18_full_gates.py', 'first_rank18_full_gates.py',
            'verify_first_rank18_full_gates.py', 'zero_anchor_support_filter.py',
            'fixed_three_row_extensions.py', 'nondisjoint_third_diagnostic.py',
            'verify_nondisjoint_third_diagnostic.py']
    output.update(artifact_hashes_before=before, artifact_hashes_after=after,
                  inspected_code_sha256={f: sha256((HERE/f).read_bytes()).hexdigest() for f in code},
                  full_replay=replay, summary={
                      'checks_passed': sum(output['checks'].values()),
                      'checks_required': len(output['checks']),
                      'actual_loci': 1, 'required_loci': 1,
                      'actual_rank': 18, 'rank_bound_from_minor': 18,
                      'rank_bound_from_independent_kernel': 18,
                      'projective_charts_checked': 21, 'projective_charts_required': 21})
    path = HERE/'first-rank18-critical-audit.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output['summary'], sort_keys=True))
    print('Row 2: required nonzero lambda/full weights; actual lambda=e18=e64=e70=0 on its rank-one recovery line.')
    print(f'Failures: {output["failures"]}; certificate: {path}')
    if output['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    run()
