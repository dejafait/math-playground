"""Independent complete-nullspace/contraction replay of the approved screen."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import verify_fixed_three_row_extensions as derivative

HERE = Path(__file__).resolve().parent
P = 97


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def nullspace(matrix):
    """Gauss-Jordan with reverse original-row order, all-row elimination."""
    reduced = [r[:] for r in reversed(matrix)]
    pivots = []
    for c in range(len(matrix[0])):
        pivot = next((r for r in range(len(pivots), len(reduced)) if reduced[r][c]), None)
        if pivot is None:
            continue
        r = len(pivots)
        reduced[r], reduced[pivot] = reduced[pivot], reduced[r]
        inverse = pow(reduced[r][c], -1, P)
        reduced[r] = [inverse*x % P for x in reduced[r]]
        for k in range(len(reduced)):
            if k != r:
                multiple = reduced[k][c]
                reduced[k] = [(a-multiple*b) % P for a, b in zip(reduced[k], reduced[r])]
        pivots.append(c)
    free = sorted(set(range(len(matrix[0])))-set(pivots))
    basis = []
    for c in free:
        v = [0]*len(matrix[0])
        v[c] = 1
        for r, pivot in enumerate(pivots):
            v[pivot] = -reduced[r][c] % P
        basis.append(v)
    return pivots, basis


def run():
    path = HERE/'inactive-coordinate-screen.json'
    before = digest(path)
    source = json.loads(path.read_bytes())
    master_path = HERE/source['source_path']
    master = json.loads(master_path.read_bytes())
    checks, failures, records = [], [], []

    def check(name, valid):
        checks.append({'check': name, 'passed': bool(valid)})
        if not valid:
            failures.append(name)

    check('screen input and program hashes', source['failures'] == []
          and all(c['passed'] for c in source['checks'])
          and digest(master_path) == source['source_sha256']
          and digest(HERE/source['audit_path']) == source['audit_sha256']
          and digest(HERE/'inactive_coordinate_screen.py') == source['code_sha256'])
    s = [1, 8, 12, 18, 22, 27, 33]
    h = sorted({pow(8, e, P) for e in range(16)})
    j = sorted(set(h)-set(s))
    pairs = list(combinations(range(7), 2))
    universe = list(product(combinations(s, 2), combinations(j, 2)))
    first = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
    initial = set(x for key in first for half in key for x in half)
    eligible = [key for key in universe if all(len(set(key[0]+key[1])&set(a+b)) <= 1 for a, b in first)]
    disjoint = [key for key in eligible if not set(key[0]+key[1])&initial]
    thirds = [key for key in eligible if key not in disjoint and key != ((1, 22), (75, 79))]
    check('ordered universe sizes', len(universe) == 756 and len(eligible) == 382
          and len(disjoint) == 30 and len(thirds) == 351)
    check('reconstructed metadata', source['S'] == s and source['H'] == h
          and source['modulus'] == P and source['column_pairs'] == [[s[a], s[b]] for a, b in pairs])
    expected_indices, original_cases = [], {}
    for meta in master['thirds']:
        if not meta['remaining']:
            continue
        shard_path = HERE/meta['certificate']
        shard = json.loads(shard_path.read_bytes())
        check('master shard '+str(meta['third_index']), digest(shard_path) == meta['sha256'])
        retained = [c['fourth_index'] for c in shard['cases'] if c['status'] == 'unresolved']
        check('saved remaining indices '+str(meta['third_index']), retained == shard['remaining_indices']
              and len(retained) == meta['remaining'])
        for case in shard['cases']:
            if case['status'] == 'unresolved':
                index = (meta['third_index'], case['fourth_index'])
                expected_indices.append(index)
                original_cases[index] = case
    actual_indices = [(r['third_index'], r['fourth_index']) for r in source['records']]
    check('exact ordered 599-record domain', actual_indices == expected_indices
          and len(actual_indices) == len(set(actual_indices)) == 599)
    blocks = {}
    counts, overlap, coordinates, ranks = Counter(), Counter(), Counter(), Counter()
    vector_count = 0
    replay_partition = []
    for record in source['records']:
        n, u = record['third_index'], record['fourth_index']
        index = (n, u)
        rows = first+[thirds[n], universe[u]]
        for key in rows:
            if key not in blocks:
                blocks[key] = derivative.block(*key)
        matrix = [r for key in rows for r in blocks[key]]
        pivots, basis = nullspace(matrix)
        label = str(index)
        check(label+' rebuilt nullspace and original basis', len(pivots) == record['rank']
              and basis == record['kernel_basis'] == original_cases[index]['kernel_basis']
              and len(basis) == 21-len(pivots)
              and all(not any(sum(a*b for a, b in zip(v, row)) % P for row in matrix) for v in basis))
        skew = []
        for v in basis:
            tensor = [[0]*7 for _ in s]
            for c, (a, b) in enumerate(pairs):
                tensor[a][b] = v[c]
                tensor[b][a] = -v[c] % P
            skew.append(tensor)
        omitted = [s[x] for x in range(7) if all(not any(tensor[x]) for tensor in skew)]
        check(label+' all seven contractions', [t['coordinate'] for t in record['coordinate_tests']] == s)
        for x, test in enumerate(record['coordinate_tests']):
            cols = [c for c, (a, b) in enumerate(pairs) if x == a or x == b]
            entries = [[v[c] for c in cols] for v in basis]
            check(label+f' complete entries at {s[x]}', test['incident_columns'] == cols
                  and test['complete_incident_coefficients'] == entries
                  and test['omitted'] == (s[x] in omitted))
            witness = test['nonzero_witness']
            check(label+f' failure witness at {s[x]}',
                  witness is None if s[x] in omitted else witness is not None
                  and 0 <= witness[0] < len(basis) and witness[1] in cols
                  and basis[witness[0]][witness[1]] == witness[2] != 0)
        prior = (['L112_exchanged_rows'] if universe[u] in disjoint else [])
        if index == (0, 279):
            prior.append('L117')
        status = 'excluded_inactive_coordinate' if omitted else 'screen_failure'
        check(label+' disposition and overlap', record['status'] == status and record['prior_exclusions'] == prior)
        counts[status] += 1
        if omitted and not prior:
            counts['new'] += 1
        overlap['+'.join(prior or ['none'])+':'+status] += 1
        coordinates.update(omitted)
        ranks[len(pivots)] += 1
        vector_count += len(basis)
        replay_partition.append({'third_index': n, 'fourth_index': u, 'status': status,
                                 'omitted_coordinates': omitted, 'prior_exclusions': prior})
        records.append({'third_index': n, 'fourth_index': u, 'rank': len(pivots),
                        'recomputed_kernel_basis': basis, 'complete_skew_matrices': skew,
                        'omitted_coordinates': omitted, 'prior_exclusions': prior})
    summary = {'actual_occurrences': len(records), 'required_occurrences': 599,
               'actual_thirds': len({r['third_index'] for r in records}), 'required_thirds': 56,
               'basis_vectors': vector_count, 'original_residual_entries': 24*vector_count,
               'coordinate_tests': 7*len(records), 'passing_occurrences': counts['excluded_inactive_coordinate'],
               'failing_occurrences': counts['screen_failure'], 'new_relative_to_L112_L117': counts['new'],
               'rank_histogram': {str(k): v for k, v in sorted(ranks.items())},
               'omitted_coordinate_histogram': {str(k): v for k, v in sorted(coordinates.items())},
               'overlap_histogram': dict(sorted(overlap.items()))}
    check('complete summary/partition agreement', source['summary'] == summary and source['partition'] == replay_partition)
    check('source remains unchanged', digest(path) == before)
    output = {'source_sha256': digest(path), 'summary': summary, 'partition': replay_partition,
              'records': records, 'checks': checks, 'failures': failures,
              'scope': 'same-step replay; shared Python, prime arithmetic and audited derivative helper'}
    out = HERE/'inactive-coordinate-screen-replay.json'
    out.write_text(json.dumps(output, separators=(',', ':'))+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: {len(failures)}; complete replay: {out}')
    if failures:
        print('First failures:', failures[:8])
    assert not failures


if __name__ == '__main__':
    run()
