"""Separate L119 proof/certificate audit; exactly the four named supports.

Run from the notebook: python3 scripts/seven-coordinate/audit_first_active_residual.py
The full audit certificate, including replay output and hashes, stays on disk.
"""
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
        ([1, 12], [75, 79]), ([8, 22], [79, 96])]
PAIRS = list(combinations(range(7), 2))
FILES = ['first_active_residual_gates.py', 'verify_first_active_residual_gates.py',
         'zero_anchor_support_filter.py', 'residual_kernel_gates.py',
         'inactive-coordinate-partition-critical-audit.json',
         'first-active-residual-gates.json', 'first-active-residual-gates-replay.json']


def hashes():
    return {name: sha256((HERE/name).read_bytes()).hexdigest() for name in FILES}


def rref(matrix):
    a = [[x % P for x in row] for row in matrix]
    pivots = []
    for col in range(len(a[0])):
        pivot = next((i for i in range(len(pivots), len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        pos = len(pivots)
        a[pos], a[pivot] = a[pivot], a[pos]
        inv = pow(a[pos][col], -1, P)
        a[pos] = [x*inv % P for x in a[pos]]
        for i in range(len(a)):
            if i != pos:
                c = a[i][col]
                a[i] = [(x-c*y) % P for x, y in zip(a[i], a[pos])]
        pivots.append(col)
    return a, pivots


def run():
    before = hashes()
    before_path = HERE/'first-active-residual-critical-audit-before.json'
    before_path.write_text(json.dumps(before, indent=2)+'\n')
    runs = []
    for name in FILES[:2]:
        proc = subprocess.run([sys.executable, str(HERE/name)], capture_output=True, text=True)
        runs.append({'program': name, 'returncode': proc.returncode,
                     'stdout': proc.stdout, 'stderr': proc.stderr})
        if proc.returncode:
            break
    after = hashes()
    checks = []

    def check(name, condition):
        checks.append({'check': name, 'passed': bool(condition)})

    check('both complete programs pass', len(runs) == 2 and all(r['returncode'] == 0 for r in runs))
    check('all seven input/artifact hashes unchanged', before == after)
    cert = json.loads((HERE/'first-active-residual-gates.json').read_text())
    replay = json.loads((HERE/'first-active-residual-gates-replay.json').read_text())
    provenance = json.loads((HERE/'inactive-coordinate-partition-critical-audit.json').read_text())['first_uncovered_record']
    h_labels = [x for x in range(1, P) if pow(x, 16, P) == 1]
    j_labels = sorted(set(h_labels)-set(S))
    check('sixteen distinct nonzero evaluation labels', len(h_labels) == 16 and cert['H'] == h_labels)
    check('exact original supports and historical indices', cert['rows'] == [{'I': i, 'K': k} for i, k in ROWS]
          and provenance['four_rows'] == [[i, k] for i, k in ROWS]
          and cert['source']['historical_indices'] == [0, 320]
          and [provenance['third_index'], provenance['fourth_index']] == [0, 320])
    check('exact support sizes and domain', len(S) == 7 and len(j_labels) == 9
          and all(len(set(i)) == len(set(k)) == 2 and set(i) <= set(S)
                  and set(k) <= set(j_labels) for i, k in ROWS))
    check('source digest binding', cert['source']['sha256'] == before['inactive-coordinate-partition-critical-audit.json'])
    check('replay digest binding', replay['certificate_sha256'] == after['first-active-residual-gates.json'])
    check('column order', cert['column_pairs'] == [[S[a], S[b]] for a, b in PAIRS])

    # Fresh coefficient-polynomial/Horner construction, importing no helpers.
    matrix, polynomials, quotients = [], [], []
    for i, k in ROWS:
        polynomial = [1]
        for root in sorted(set(j_labels)-set(k)):
            nxt = [0]*(len(polynomial)+1)
            for d, value in enumerate(polynomial):
                nxt[d] = (nxt[d]-root*value) % P
                nxt[d+1] = (nxt[d+1]+value) % P
            polynomial = nxt
        values = {}
        for x in h_labels:
            value = 0
            for c in reversed(polynomial):
                value = (value*x+c) % P
            values[x] = value
        observed = sorted(set(S)-set(i))
        z = observed[0]
        q = [[(int(y == x)*values[z]-int(y == z)*values[x]) % P for y in S]
             for x in observed[1:]]
        matrix.extend([[(a[x]*b[y]-a[y]*b[x]) % P for x, y in PAIRS]
                       for a, b in combinations(q, 2)])
        polynomials.append({'I': i, 'K': k, 'coefficients': polynomial,
                            'values_on_H': [values[x] for x in h_labels]})
        quotients.append(q)
    check('all 504 original entries rebuilt', len(matrix) == 24 and all(len(r) == 21 for r in matrix)
          and matrix == cert['original_matrix'] == replay['rebuilt_original_matrix'])
    check('all four quotient matrices rebuilt', quotients == [b['covectors'] for b in cert['blocks']])
    reduced, pivots = rref(matrix)
    free = [c for c in range(21) if c not in pivots]
    fresh_basis = []
    for c in free:
        b = [0]*21
        b[c] = 1
        for n, pivot in enumerate(pivots):
            b[pivot] = -reduced[n][c] % P
        fresh_basis.append(b)
    check('fresh rank and free columns', len(pivots) == 19 and free == [5, 6])
    check('entire kernel matches', fresh_basis == cert['kernel_basis'] == provenance['kernel_basis'])
    check('two-vector independence witness', [[b[c] for c in free] for b in fresh_basis] == [[1, 0], [0, 1]])
    check('all 48 basis residuals', cert['kernel_residuals'] == replay['kernel_residuals'] == [[0]*24, [0]*24])
    check('printed original minor rows', cert['rank_minor_rows'] == list(range(16))+[18, 19, 20])
    check('printed original minor columns', cert['rank_minor_columns'] == [c for c in range(21) if c not in (5, 6)])
    check('printed integer determinant and nonzero residue', cert['rank_minor_integer_determinant']
          == replay['rank_minor_integer_determinant'] == -19413570831084880785282562746937344
          and cert['rank_minor_integer_determinant'] % P == cert['rank_minor_residue'] == 32)
    expected_quadrics = [[0, c, 0] for c in [72, 53, 27, 1]]+[[0, 0, 0] for _ in range(31)]
    check('complete 35 homogeneous coefficient triples', cert['plucker_coefficients_s2_st_t2']
          == replay['plucker_coefficients_s2_st_t2'] == expected_quadrics)
    check('homogeneous quadruple coverage', cert['plucker_quadruples'] == list(map(list, combinations(S, 4))))
    check('both homogeneous endpoints including infinity', cert['complete_projective_parameter_locus'] == [[1, 0], [0, 1]])
    check('exact two-plane and eight-row coverage', len(cert['points_and_all_row_gates']) == 2
          and all(len(p['row_gates']) == 4 for p in cert['points_and_all_row_gates'])
          and [(r['point_index'], r['row_number']) for r in replay['all_row_replay']]
          == [(i, j) for i in range(2) for j in range(1, 5)])
    # Every numeric entry of L119's printed gate table, including successes.
    printed = [([0, 22], [75, 0], 0, [75, 0, 0, 0]),
               ([38, 16], [81, 38], 86, [30, 87, 31, 91]),
               ([0, 69], [28, 0], 0, [28, 0, 0, 0]),
               ([34, 64], [33, 34], 39, [21, 96, 75, 37]),
               ([0, 16], [81, 0], 0, [0, 81, 0, 0]),
               ([72, 0], [0, 72], 0, [72, 0, 0, 0]),
               ([6, 0], [0, 6], 0, [0, 6, 0, 0]),
               ([0, 68], [29, 0], 0, [29, 0, 0, 0])]
    gates = [g for p in cert['points_and_all_row_gates'] for g in p['row_gates']]
    for n, (gate, row, table) in enumerate(zip(gates, replay['all_row_replay'], printed)):
        check(f'printed gate table row {n+1}', ([gate['Q_u'][0], gate['Q_v'][0]],
              gate['direction_coefficients'], gate['lambda_value'], gate['error_weights']) == table)
        check(f'complete independent replay row {n+1}',
              row['Q_u'] == gate['Q_u'] and row['Q_v'] == gate['Q_v']
              and row['h'] == gate['intersection_vector'] and row['lambda'] == gate['lambda_value']
              and [row['error'][str(x)] for x in sum(ROWS[n % 4], [])] == gate['error_weights']
              and row['moments'] == gate['moment_residuals'] == [0]*8
              and row['finite_gate_coefficients_D_C'] == [gate['direction_coefficients'][0],
                                                         -gate['direction_coefficients'][1] % P])
    check('all eight ranks exactly one', all(g['projection_rank'] == 1
          and g['projection_minors'] == [0]*6 and any(g['Q_u']+g['Q_v']) for g in gates))
    check('six failed rows and two retained successes', [g['passes'] for g in gates]
          == [False, True, False, True, False, False, False, False])
    check('128 complete pointwise entries', all(g['h_minus_error_minus_lambda_g_on_H'] == [0]*16 for g in gates))
    check('both first-row intersections have lambda zero', gates[0]['lambda_value'] == gates[4]['lambda_value'] == 0
          and gates[0]['error_weights'].count(0) == gates[4]['error_weights'].count(0) == 3)
    check('no producer or independent replay failure', cert['failures'] == replay['failures'] == [])
    failures = [c['check'] for c in checks if not c['passed']]
    out = {'step_id': '2026-10-19-mca-333-first-active-residual-critical-audit',
           'hashes_before': before, 'hashes_after': after, 'runs': runs,
           'checks': checks, 'polynomials': polynomials, 'original_matrix': matrix,
           'rref': reduced, 'pivot_columns': pivots, 'free_columns': free,
           'complete_kernel_basis': fresh_basis, 'homogeneous_coefficients': expected_quadrics,
           'printed_gate_table': printed, 'all_row_replay': replay['all_row_replay'],
           'chart_review': 'For Delta=AD-BC, alpha0=(D*alpha-C*beta)/Delta and beta0=(-B*alpha+A*beta)/Delta. The two coefficients reconstruct alpha*u+beta*v identically. Finite alpha0!=0 rescales lambda and every weight; alpha0=0 omits the event. This is a symbolic proof, not chart sampling.',
           'summary': {'checks_passed': len(checks)-len(failures), 'checks_required': len(checks),
                       'matrix_entries': 504, 'rank': len(pivots), 'nonzero_minor_residue': 32,
                       'homogeneous_equations': 35, 'complete_points': 2, 'row_gates': len(gates),
                       'failed_rows': 6, 'full_weight_rows': 2, 'pointwise_entries': 128,
                       'shifted_moments': 64, 'unresolved_branches': 0},
           'failures': failures,
           'limitations': 'One L119 necessary-gate exclusion, retaining inherited L109 qualifications. No new exclusions, global improvement or proof-assistant verification. Exact paths share Python and residue arithmetic.'}
    path = HERE/'first-active-residual-critical-audit.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out['summary'], sort_keys=True))
    print(f'Passing planes 0/2; global interval unchanged 11/q–16/q; failures {len(failures)}; certificate: {path}')
    if failures:
        print('Failed checks: '+', '.join(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    run()
