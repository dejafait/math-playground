"""Separate L122 audit; reproduce only the six approved selected-row records.

Existing producer and verifier are inspected inputs. Extra checks bind the
printed tables, certify minors by integer Bareiss elimination, and compare
the three planes and exchanged rows. No additional support rows are tested.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = 97


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def integer_det(matrix):
    """Fraction-free row elimination over Z, checking each exact division."""
    a = [row[:] for row in matrix]
    previous, sign = 1, 1
    for k in range(len(a)-1):
        pivot = next((r for r in range(k, len(a)) if a[r][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        value = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = value*a[i][j]-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = value
    return sign*a[-1][-1]


def integers(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def run():
    output = HERE/'rank20-classification-critical-audit.json'
    log_path = HERE/'rank20-classification-critical-audit.log'
    result = {'scope': 'L122 six records and their four selected rows only',
              'checks': [], 'failures': [], 'record_checks': []}

    def check(name, condition):
        result['checks'].append({'check': name, 'passed': bool(condition)})
        if not condition:
            result['failures'].append(name)
            raise AssertionError(name)

    try:
        prior_path = HERE/'inactive-coordinate-partition-critical-audit.json'
        prior = json.loads(prior_path.read_bytes())
        bindings = {**prior['artifact_hashes_after'], **prior['code_hashes']}
        check('prior audit successful and immutable', not prior['failures']
              and prior['replay_returncode'] == 0
              and all(c['passed'] for c in prior['checks'])
              and prior['artifact_hashes_before'] == prior['artifact_hashes_after'])
        check('all prior bound artifacts and programs unchanged',
              all(digest(HERE/name) == value for name, value in bindings.items()))
        names = sorted(set(bindings) | {prior_path.name,
                       'rank20-selected-gates.json', 'rank20-selected-gates-replay.json'})
        result['artifact_hashes_before'] = {name: digest(HERE/name) for name in names}
        code_names = ['rank20_selected_gates.py', 'verify_rank20_selected_gates.py',
                      'zero_anchor_support_filter.py', 'residual_kernel_gates.py',
                      'verify_fixed_three_row_extensions.py', 'verify_inactive_coordinate_screen.py',
                      'verify_active_rank19_complete_loci.py', Path(__file__).name]
        result['code_hashes'] = {name: digest(HERE/name) for name in code_names}
        before_replay = json.loads((HERE/'rank20-selected-gates-replay.json').read_bytes())
        check('saved replay program and helper binding',
              before_replay['code_sha256'] == result['code_hashes']['verify_rank20_selected_gates.py']
              and before_replay['helper_sha256'] == result['code_hashes']['verify_active_rank19_complete_loci.py']
              and before_replay['input_sha256'] == digest(HERE/'rank20-selected-gates.json')
              and not before_replay['failures'])
        commands = []
        with log_path.open('w') as log:
            for name in ['rank20_selected_gates.py', 'verify_rank20_selected_gates.py']:
                proc = subprocess.run([sys.executable, str(HERE/name)],
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                log.write(name+'\n'+proc.stdout+'\n')
                commands.append({'program': name, 'returncode': proc.returncode})
                check('complete execution '+name, proc.returncode == 0)
        result['executions'] = commands
        cert = json.loads((HERE/'rank20-selected-gates.json').read_bytes())
        replay = json.loads((HERE/'rank20-selected-gates-replay.json').read_bytes())
        check('complete replay agrees byte for byte', replay == before_replay)
        lemma = HERE.parent.parent/'lemmas/L122-rank20-selected-row-survivor-classification.md'
        lines = lemma.read_text().splitlines()
        basis_lines = [line for line in lines if line.startswith('| (')]
        row_lines = [line for line in lines if re.match(r'^\| [PQR] \|', line)]
        check('exact printed table sizes', len(basis_lines) == 3 and len(row_lines) == 12)
        records = cert['records']
        check('six complete records', len(records) == len(replay['records']) == 6)
        for index, rec in enumerate(records):
            matrix, basis = rec['original_matrix'], rec['kernel_basis']
            check(f'{index}: dimensions and distinct minor indices', len(matrix) == 24
                  and all(len(row) == 21 for row in matrix) and len(basis) == 1
                  and len(basis[0]) == 21
                  and len(set(rec['rank_minor_rows'])) == len(set(rec['rank_minor_columns'])) == 20)
            minor = [[matrix[r][c] for c in rec['rank_minor_columns']] for r in rec['rank_minor_rows']]
            exact_det = integer_det(minor)
            p = basis[0]
            check(f'{index}: complete rank20 kernel via integer minor and null vector',
                  exact_det % P == rec['rank_minor_residue'] != 0 and any(p)
                  and all(sum(a*b for a, b in zip(row, p)) % P == 0 for row in matrix))
            point = rec['plane_and_all_row_gates']
            u, v = point['u'], point['v']
            check(f'{index}: exact wedge', [(u[a]*v[b]-u[b]*v[a]) % P
                  for a, b in combinations(range(7), 2)] == p)
            check(f'{index}: complete saved pivot reports', len(replay['records'][index]['all_pivot_reports'])
                  == sum(x != 0 for x in p))
            result['record_checks'].append({'historical_index': rec['historical_index'],
                'integer_minor_determinant': exact_det, 'minor_residue': exact_det % P,
                'null_vector': p, 'u': u, 'v': v})
        for n in range(3):
            first, second = records[n], records[n+3]
            a, b = first['plane_and_all_row_gates'], second['plane_and_all_row_gates']
            fields = [field.strip() for field in basis_lines[n].split('|')[1:-1]]
            check(f'{n}: printed plane table', integers(fields[0]) == first['historical_index']+second['historical_index']
                  and integers(fields[1]) == a['u'] and integers(fields[2]) == a['v'])
            check(f'{n}: exchanged-row plane identification', a['u'] == b['u'] and a['v'] == b['v']
                  and first['kernel_basis'] == second['kernel_basis']
                  and first['rows'] == [second['rows'][i] for i in [0, 1, 3, 2]]
                  and a['row_gates'] == [b['row_gates'][i] for i in [0, 1, 3, 2]])
            for j in range(4):
                fields = [field.strip() for field in row_lines[4*n+j].split('|')[1:-1]]
                row, gate = first['rows'][j], a['row_gates'][j]
                check(f'{n},{j}: printed gate table', fields[0] == 'PQR'[n]
                      and integers(fields[1]) == row['I']+row['K']
                      and integers(fields[2]) == gate['direction_coefficients']
                      and integers(fields[3]) == [gate['lambda_value']]
                      and integers(fields[4]) == gate['error_weights'])
        ratios = [r['plane_and_all_row_gates']['v'][2]
                  * pow(r['plane_and_all_row_gates']['v'][1], -1, P) % P for r in records[:3]]
        check('three distinct projective planes', ratios == [5, 76, 50] and len(set(ratios)) == 3)
        check('all displayed directions finite', all(g['direction_coefficients'][0] != 0
              for r in records for g in r['plane_and_all_row_gates']['row_gates']))
        result['three_plane_ratios'] = ratios
        result['replay_summary'] = replay['summary']
        result['artifact_hashes_after'] = {name: digest(HERE/name) for name in names}
        check('all source and regenerated artifacts byte-identical',
              result['artifact_hashes_before'] == result['artifact_hashes_after'])
        check('all called code unchanged', all(digest(HERE/name) == value
              for name, value in result['code_hashes'].items()))
    except Exception as exc:
        result['failures'].append(type(exc).__name__+': '+str(exc))
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(f"Records {len(result['record_checks'])}/6; rank target 20/21; kernels 1/1; "
          f"checks {sum(c['passed'] for c in result['checks'])}/{len(result['checks'])}; "
          f"failures {len(result['failures'])}")
    print(f'Certificate: {output}\nComplete execution log: {log_path}')
    if result['failures']:
        print(result['failures'])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
