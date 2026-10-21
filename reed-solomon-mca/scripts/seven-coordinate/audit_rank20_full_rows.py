"""Separate L123 audit: full replay and independent saved-witness checks."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, P) if pow(x, 16, P) == 1]
J = [x for x in H if x not in S]
PAIRS = [[[60, 666], [295, 197]], [[65, 671], [300, 202]],
         [[145, 696], [314, 382]]]
OUT = HERE / 'rank20-full-rows-critical-audit.json'
LOG = HERE / 'rank20-full-rows-critical-audit.log'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def load(name):
    return json.loads((HERE / name).read_bytes())


def determinant(matrix):
    """Integer Bareiss determinant; check every exact division."""
    a = [r[:] for r in matrix]
    n = len(a)
    assert all(len(r) == n for r in a)
    sign, denominator = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                assert numerator % denominator == 0
                a[i][j] = numerator // denominator
            a[i][k] = 0
        denominator = pivot
    return sign * a[-1][-1]


def normalize(v):
    inverse = pow(next(x for x in v if x), -1, P)
    return [inverse * x % P for x in v]


def numbers(s):
    return [int(x) for x in re.findall(r'\d+', s)]


def run():
    out = {'scope': 'Separate bounded L123 proof/program audit; no enlarged census',
           'checks': [], 'planes': [], 'executions': [], 'failures': []}
    originals = {}
    def check(name, condition):
        out['checks'].append({'name': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)
    try:
        prior = load('rank20-classification-critical-audit.json')
        code_names = list(prior['code_hashes']) + [
            'rank20_survivor_full_rows.py', 'verify_rank20_survivor_full_rows.py',
            Path(__file__).name]
        out['code_hashes_before'] = {n: digest(HERE / n) for n in code_names}
        check('L122 audited code hashes', all(digest(HERE / n) == h
                                               for n, h in prior['code_hashes'].items()))
        artifact_names = list(prior['artifact_hashes_after']) + [
            'rank20-classification-critical-audit.json',
            'rank20-survivor-full-rows-first-schema-failure.json',
            'rank20-survivor-full-rows.json', 'rank20-survivor-full-rows-replay.json']
        originals = {n: (HERE / n).read_bytes() for n in artifact_names}
        out['artifact_hashes_before'] = {n: sha256(b).hexdigest() for n, b in originals.items()}
        check('L122 complete successful audit', not prior['failures'] and
              len(prior['executions']) == 2 and
              {x['program'] for x in prior['executions']} ==
              {'rank20_selected_gates.py', 'verify_rank20_selected_gates.py'} and
              all(x['returncode'] == 0 for x in prior['executions']) and
              len(prior['checks']) == 54 and all(c['passed'] for c in prior['checks']))
        check('L122 unchanged manifest', prior['artifact_hashes_before'] == prior['artifact_hashes_after']
              and all(digest(HERE / n) == h for n, h in prior['artifact_hashes_after'].items()))
        failed = load('rank20-survivor-full-rows-first-schema-failure.json')
        check('Preserved failure before plane processing', failed == {
            'scope': 'Exactly three L122 planes, all 756 two-overlap rows each; necessary test only',
            'modulus': P, 'H': H, 'S': S, 'planes': [],
            'failures': [{'type': 'KeyError', 'message': "'replay_returncode'"}], 'unresolved': []})
        with LOG.open('w') as log:
            for program in ['rank20_survivor_full_rows.py', 'verify_rank20_survivor_full_rows.py']:
                result = subprocess.run([sys.executable, str(HERE / program)], cwd=ROOT,
                                        stdout=log, stderr=subprocess.STDOUT, check=False)
                out['executions'].append({'program': program, 'returncode': result.returncode})
                check('Execution ' + program, result.returncode == 0)
        cert = load('rank20-survivor-full-rows.json')
        replay = load('rank20-survivor-full-rows-replay.json')
        source = load('rank20-selected-gates.json')
        check('Both complete runs have no failures or unresolved branches',
              not any(x['failures'] or x['unresolved'] for x in [cert, replay]))
        check('Certificate program and input bindings',
              cert['producer_sha256'] == digest(HERE / 'rank20_survivor_full_rows.py') and
              replay['verifier_sha256'] == digest(HERE / 'verify_rank20_survivor_full_rows.py') and
              replay['producer_certificate_sha256'] == digest(HERE / 'rank20-survivor-full-rows.json') and
              cert['input_hashes_before'] == cert['input_hashes_after'] == replay['input_hashes'] and
              all(digest(HERE / n) == h for n, h in cert['input_hashes_before'].items()))
        check('All six indices and three planes', len(source['records']) == 6 and
              [p['historical_indices'] for p in cert['planes']] == PAIRS and
              [p['historical_indices'] for p in replay['planes']] == PAIRS)
        rows = [(list(i), list(k)) for i in combinations(S, 2) for k in combinations(J, 2)]
        check('Complete independent row universe', len(rows) == 756 and len(set(tuple(i+k) for i,k in rows)) == 756)
        text = (ROOT / 'lemmas/L123-rank20-survivor-complete-row-exclusion.md').read_text()
        printed = [[c.strip() for c in line.split('|')[1:-1]] for line in text.splitlines()
                   if re.match(r'^\| [PQR] \|', line)]
        printed_bases = [r for r in printed if len(r) == 4]
        printed_recoveries = [r for r in printed if len(r) == 3]
        check('Printed table sizes', len(printed_bases) == 3 and len(printed_recoveries) == 12)
        for pi, (plane, verified) in enumerate(zip(cert['planes'], replay['planes'])):
            label = 'PQR'[pi]
            u, v = plane['u'], plane['v']
            table = printed_bases[pi]
            check(label + ' printed basis and indices', table[0] == label and
                  numbers(table[1]) == sum(PAIRS[pi], []) and numbers(table[2]) == u and numbers(table[3]) == v)
            old = [next(r for r in source['records'] if r['historical_index'] == index) for index in PAIRS[pi]]
            check(label + ' six-index basis binding and row exchange', all(
                r['plane_and_all_row_gates']['u'] == u and r['plane_and_all_row_gates']['v'] == v for r in old)
                and old[1]['rows'] == [old[0]['rows'][i] for i in [0, 1, 3, 2]]
                and old[1]['plane_and_all_row_gates']['row_gates'] ==
                [old[0]['plane_and_all_row_gates']['row_gates'][i] for i in [0, 1, 3, 2]])
            check(label + ' complete stored rows', len(plane['rows']) == len(verified['rows']) == 756)
            details = {'plane': label, 'rows': [], 'printed_recoveries': [], 'directions': []}
            out['planes'].append(details)
            ranks = Counter()
            for ri, (i, k) in enumerate(rows):
                qrow, witness = plane['rows'][ri], verified['rows'][ri]
                assert qrow['row_index'] == witness['row_index'] == ri
                assert qrow['I'] == witness['I'] == i and qrow['K'] == witness['K'] == k
                matrix = [[sum(u[j]*x**d for j,x in enumerate(S)) % P,
                           sum(v[j]*x**d for j,x in enumerate(S)) % P] +
                          [-x**d % P for x in i+k] for d in range(1,9)]
                assert matrix == witness['moment_matrix']
                e, reduced = witness['left_multiplier'], witness['moment_rref']
                assert len(e) == len(reduced) == 8 and all(len(r) == 8 for r in e)
                assert all(len(r) == 6 for r in reduced)
                det_e = determinant(e)
                assert det_e % P
                assert [[sum(e[a][b]*matrix[b][c] for b in range(8)) % P
                         for c in range(6)] for a in range(8)] == reduced
                pivots, kernel = witness['pivot_columns'], witness['complete_null_basis']
                rank = witness['moment_rank']
                assert len(pivots) == len(set(pivots)) == rank
                assert rank in [5,6] and len(witness['nonzero_pivot_values']) == rank
                assert all(x % P for x in witness['nonzero_pivot_values'])
                assert [[reduced[a][c] for c in pivots] for a in range(rank)] == [
                    [int(a == b) for b in range(rank)] for a in range(rank)]
                assert all(not any(r) for r in reduced[rank:])
                free = [c for c in range(6) if c not in pivots]
                assert len(kernel) == 6-rank and all(len(b) == 6 for b in kernel)
                assert [[b[c] for c in free] for b in kernel] == [
                    [int(a == b) for b in range(len(free))] for a in range(len(free))]
                assert all(not any(sum(a*b for a,b in zip(r,w)) % P for r in matrix) for w in kernel)
                error_minor = determinant([r[2:] for r in matrix[:4]])
                assert error_minor % P
                assert qrow['projection_rank'] == rank-4
                ranks[rank] += 1
                details['rows'].append({'row_index': ri, 'I': i, 'K': k, 'moment_rank': rank,
                                       'left_multiplier_integer_determinant': det_e,
                                       'error_minor_integer_determinant': error_minor,
                                       'complete_kernel_checked': True})
                if rank == 6:
                    assert qrow['status'] == 'rank_two_no_intersection' and not kernel
                    continue
                gate = qrow['recovery']
                direction = normalize(kernel[0][:2])
                assert direction == gate['normalized_direction']
                assert normalize(kernel[0]) == normalize(gate['direction_coefficients'] + gate['error_weights'])
                assert qrow['status'] == 'intrinsic_success' and gate['passes_intrinsic']
                assert gate['lambda_value'] and all(gate['error_weights']) and not gate['failed_gates']
                assert len(gate['identity_residuals']) == 16 and not any(gate['identity_residuals'])
                assert len(gate['shifted_moment_residuals']) == 8 and not any(gate['shifted_moment_residuals'])
                assert gate['prescribed_finite_gate'] == {'D_coefficient': gate['direction_coefficients'][0],
                                                        'C_coefficient': -gate['direction_coefficients'][1] % P}
                matching = [r for r in printed_recoveries if r[0] == label and numbers(r[1]) == i+k]
                assert len(matching) == 1 and numbers(matching[0][2]) == direction
                oldpos = next(j for j,r in enumerate(old[0]['rows']) if r['I'] == i and r['K'] == k)
                oldgate = old[0]['plane_and_all_row_gates']['row_gates'][oldpos]
                assert all(gate[key] == oldgate[key] for key in
                           ['direction_coefficients', 'lambda_value', 'error_weights', 'prescribed_finite_gate'])
                details['printed_recoveries'].append({'I': i, 'K': k, 'direction': direction,
                                                     'lambda': gate['lambda_value'], 'weights': gate['error_weights']})
                details['directions'].append(direction)
            check(label + ' all original kernels and printed recoveries',
                  ranks == {5:4, 6:752} and len(details['printed_recoveries']) == 4)
            check(label + ' distinct pre-chart directions and necessary shortfall',
                  len({tuple(d) for d in details['directions']}) == 4 and
                  plane['summary']['distinct_directions_before_chart'] == 4 and
                  plane['summary']['required_distinct_directions'] == 12 and plane['summary']['shortfall'] == 8)
            details['summary'] = {'complete_rows_checked': 756, 'moment_rank_counts': dict(ranks),
                                  'actual_directions': 4, 'required_directions': 12, 'shortfall': 8}
        out['artifact_hashes_after'] = {n: digest(HERE/n) for n in originals}
        check('Every bound artifact reproduced unchanged', out['artifact_hashes_before'] == out['artifact_hashes_after'])
        out['code_hashes_after'] = {n: digest(HERE/n) for n in code_names}
        check('Every bound program unchanged', out['code_hashes_before'] == out['code_hashes_after'])
    except Exception as exc:
        out['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
        raise
    finally:
        for name, data in originals.items():
            if (HERE/name).read_bytes() != data:
                saved = HERE/('rank20-full-row-audit-before-' + name)
                saved.write_bytes(data)
                out.setdefault('preserved_changed_inputs', []).append(str(saved.relative_to(ROOT)))
        OUT.write_text(json.dumps(out, separators=(',', ':'))+'\n')
        for plane in out['planes']:
            print(plane['plane'], plane.get('summary', 'INCOMPLETE'))
        print(f"Checks {sum(c['passed'] for c in out['checks'])}/{len(out['checks'])}; failures {len(out['failures'])}")
        print('Full audit:', OUT.relative_to(ROOT), '; replay log:', LOG.relative_to(ROOT))


if __name__ == '__main__':
    run()
