"""Separate L121 audit: full replay, row-operation witnesses, frozen failure."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
P = 97


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) % P
             for col in zip(*b)] for row in a]


def reduce_with_witness(matrix):
    """Forward-column elimination; record the full invertible left multiplier."""
    m, n = len(matrix), len(matrix[0])
    a = [row[:] for row in matrix]
    transform = [[int(i == j) for j in range(m)] for i in range(m)]
    pivots, factors = [], []
    for c in range(n):
        r = len(pivots)
        pivot = next((j for j in range(r, m) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        transform[r], transform[pivot] = transform[pivot], transform[r]
        factor = a[r][c]
        assert 0 < factor < P
        factors.append(factor)
        inverse = pow(factor, -1, P)
        a[r] = [v*inverse % P for v in a[r]]
        transform[r] = [v*inverse % P for v in transform[r]]
        for j in range(m):
            if j != r:
                scale = a[j][c]
                a[j] = [(v-scale*w) % P for v, w in zip(a[j], a[r])]
                transform[j] = [(v-scale*w) % P for v, w in zip(transform[j], transform[r])]
        pivots.append(c)
    assert multiply(transform, matrix) == a
    assert all(not any(row) for row in a[len(pivots):])
    assert [[a[r][c] for c in pivots] for r in range(len(pivots))] == [
        [int(i == j) for j in range(len(pivots))] for i in range(len(pivots))]
    return a, transform, pivots, factors


def run():
    target = HERE/'intrinsic-survivor-critical-audit.json'
    log = HERE/'intrinsic-survivor-critical-audit.log'
    names = ['intrinsic-survivor-full-rows.json', 'intrinsic-survivor-full-rows-replay.json',
             'intrinsic-survivor-full-rows-replay-first-encoding-failure.json',
             'active-rank19-critical-audit.json', 'active-rank19-complete-loci.json',
             'active-rank19-complete-loci-replay.json']
    code = ['intrinsic_survivor_full_rows.py', 'verify_intrinsic_survivor_full_rows.py']
    out = {'scope': 'Separate audit of L121, exactly two planes and 1512 rows',
           'failures': [], 'checks': [], 'planes': []}

    def check(label, condition):
        out['checks'].append({'check': label, 'passed': bool(condition)})
        assert condition, label

    try:
        out['artifact_hashes_before'] = {name: digest(HERE/name) for name in names}
        out['code_hashes'] = {name: digest(HERE/name) for name in code}
        with log.open('w') as stream:
            for name in code:
                result = subprocess.run([sys.executable, str(HERE/name)], stdout=stream,
                                        stderr=subprocess.STDOUT, check=False)
                check(name+' complete reproduction', result.returncode == 0)
        cert = json.loads((HERE/names[0]).read_bytes())
        replay = json.loads((HERE/names[1]).read_bytes())
        failed = json.loads((HERE/names[2]).read_bytes())
        source = json.loads((HERE/'active-rank19-complete-loci.json').read_bytes())
        check('both full certificates have no failures or unresolved branches',
              all(not a['failures'] and not a['unresolved'] for a in [cert, replay]))
        # Reconstruct the old program byte-for-byte: the single key-type repair.
        current_code = (HERE/code[1]).read_text()
        old_fragment = "Counter(r['projection_rank'] for r in rec['rows'])"
        new_fragment = "Counter(str(r['projection_rank']) for r in rec['rows'])"
        check('exactly one changed histogram expression', current_code.count(new_fragment) == 1)
        old_code = current_code.replace(new_fragment, old_fragment)
        check('old verifier hash matches one-expression serialization repair',
              sha256(old_code.encode()).hexdigest() == failed['verifier_sha256'])
        check('preserved failure is exactly one first-plane summary assertion',
              failed['failures'] == [{'type': 'AssertionError', 'message': ''}]
              and failed['unresolved'] == [] and len(failed['planes']) == 1
              and set(failed['planes'][0]) == {'historical_indices', 'rows'})
        check('every previously completed row is unchanged',
              failed['planes'][0]['rows'] == replay['planes'][0]['rows']
              and failed['planes'][0]['historical_indices'] == replay['planes'][0]['historical_indices']
              and failed['producer_certificate_sha256'] == replay['producer_certificate_sha256']
              and failed['input_hashes'] == replay['input_hashes'])
        h, s = cert['H'], cert['S']
        j = sorted(set(h)-set(s))
        universe = [(list(i), list(k)) for i, k in product(combinations(s, 2), combinations(j, 2))]
        expected_directions = [[[1, 36], [1, 37], [1, 79], [1, 90]],
                               [[1, 15], [1, 20], [1, 50], [1, 91]]]
        check('exact plane and row counts', len(cert['planes']) == len(replay['planes']) == 2
              and len(universe) == 756)
        for plane_index, (plane, rep) in enumerate(zip(cert['planes'], replay['planes'])):
            check(f'plane {plane_index} complete row arrays', len(plane['rows']) == len(rep['rows']) == 756)
            audited = {'historical_indices': plane['historical_indices'], 'row_witnesses': []}
            out['planes'].append(audited)
            ranks = Counter()
            for index, ((i, k), row, evidence) in enumerate(zip(universe, plane['rows'], rep['rows'])):
                assert row['I'] == evidence['I'] == i and row['K'] == evidence['K'] == k
                assert row['row_index'] == evidence['row_index'] == index
                matrix = [[sum(w*pow(x, d, P) for w, x in zip(vec, s)) % P
                           for vec in [plane['u'], plane['v']]]
                          + [(-pow(x, d, P)) % P for x in i+k] for d in range(1, 9)]
                assert matrix == evidence['moment_matrix']
                reduced, transform, pivots, factors = reduce_with_witness(matrix)
                rank = len(pivots)
                assert rank == evidence['moment_rank'] in [5, 6]
                ranks[rank] += 1
                # Check the saved reverse-pivot basis in full, including free coordinates.
                saved_pivots = evidence['pivot_columns']
                free = [c for c in range(6) if c not in saved_pivots]
                kernel = evidence['complete_null_basis']
                assert len(saved_pivots) == len(set(saved_pivots)) == rank
                assert all(0 <= c < 6 for c in saved_pivots)
                assert len(kernel) == 6-rank and all(len(v) == 6 for v in kernel)
                assert [[v[c] for c in free] for v in kernel] == [
                    [int(a == b) for b in range(len(free))] for a in range(len(free))]
                assert all(sum(a*b for a, b in zip(m, v)) % P == 0 for m in matrix for v in kernel)
                assert len(evidence['moment_rref']) == 8 and all(len(r) == 6 for r in evidence['moment_rref'])
                if rank == 5:
                    gate = row['recovery']
                    assert row['status'] == 'intrinsic_success' and gate['lambda_value']
                    assert len(gate['error_weights']) == 4 and all(gate['error_weights'])
                    assert len(gate['h']) == 7 and len(gate['direction_coefficients']) == 2
                    assert len(gate['identity_residuals']) == 16 and len(gate['shifted_moment_residuals']) == 8
                audited['row_witnesses'].append({'row_index': index, 'moment_matrix': matrix,
                    'forward_reduction': reduced, 'invertible_left_multiplier': transform,
                    'nonzero_pivot_values': factors, 'pivot_columns': pivots})
            check(f'plane {plane_index} ranks five/four versus six/752', dict(ranks) == {5: 4, 6: 752})
            check(f'plane {plane_index} exact four directions',
                  [g['direction'] for g in plane['direction_groups']] == expected_directions[plane_index]
                  and all(len(g['row_indices']) == 1 for g in plane['direction_groups']))
            selected_rows = [r for r in plane['rows'] if r['status'] == 'intrinsic_success']
            for historical_index in plane['historical_indices']:
                old = next(r for r in source['survivor_details'] if r['historical_index'] == historical_index)
                assert len(old['rows']) == len(old['row_gates']) == 4
                assert {(tuple(r['I']), tuple(r['K'])) for r in old['rows']} == {
                    (tuple(r['I']), tuple(r['K'])) for r in selected_rows}
            audited['actual_directions'] = 4
            audited['required_directions'] = 12
            audited['shortfall'] = 8
        out['artifact_hashes_after'] = {name: digest(HERE/name) for name in names}
        check('all six artifacts remain byte-identical', out['artifact_hashes_before'] == out['artifact_hashes_after'])
        check('both inspected programs unchanged', out['code_hashes'] == {name: digest(HERE/name) for name in code})
        out['audit_program_sha256'] = digest(Path(__file__))
    except Exception as exc:
        out['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
        raise
    finally:
        target.write_text(json.dumps(out, separators=(',', ':'))+'\n')
        print(f"Checked {sum(len(p['row_witnesses']) for p in out['planes'])}/1512 complete row witnesses; "
              f"failures {len(out['failures'])}; actual/required directions 4/12 per plane.")
        print(f"Full audit certificate: {target}; full reproduction log: {log}")


if __name__ == '__main__':
    run()
