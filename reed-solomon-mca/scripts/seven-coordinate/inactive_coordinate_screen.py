"""Approved complete-kernel omission screen on exactly L116's 599 failures.

Full certificates, including every failed coordinate, are saved to disk.
No field-point sampling, general Plucker solver or recursive exclusion.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import verify_fixed_three_row_extensions as independent

HERE = Path(__file__).resolve().parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
NAMED = ((1, 22), (75, 79))


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    checks, failures = [], []

    def check(name, valid):
        checks.append({'check': name, 'passed': bool(valid)})
        if not valid:
            failures.append(name)

    audit_path = HERE/'residual-coordinate-partition-critical-audit.json'
    audit = json.loads(audit_path.read_bytes())
    check('L116 audit succeeded', audit['failures'] == [] and audit['replay_returncode'] == 0
          and all(c['passed'] for c in audit['checks']))
    check('audit before/after identical', audit['artifact_hashes_before'] == audit['artifact_hashes_after'])
    # Full audited provenance is verified without reexecuting the older census.
    for name, value in audit['artifact_hashes_after'].items():
        check('audited artifact '+name, digest(HERE/name) == value)
    for name, value in audit['code_hashes'].items():
        check('audited helper '+name, digest(HERE/name) == value)
    master_path = HERE/'residual-coordinate-factors.json'
    source = json.loads(master_path.read_bytes())
    historical_path = HERE/source['source']
    historical = json.loads(historical_path.read_bytes())
    check('historical master hash', digest(historical_path) == source['source_sha256'])
    h = [x for x in range(1, P) if pow(x, 16, P) == 1]
    j = [x for x in h if x not in S]
    pairs = list(combinations(range(7), 2))
    check('field and column metadata', direct.S == independent.S == source['S'] == S
          and direct.H == independent.H == source['H'] == h
          and direct.J == independent.J == j and direct.PAIRS == independent.PAIRS == pairs
          and source['modulus'] == historical['modulus'] == P
          and historical['column_pairs'] == [[S[a], S[b]] for a, b in pairs]
          and source['first_two'] == [[list(a), list(b)] for a, b in FIRST])
    universe = list(product(combinations(S, 2), combinations(j, 2)))
    support = {key: set(key[0]+key[1]) for key in universe}
    initial = set.union(*(support[key] for key in FIRST))
    eligible = [key for key in universe if all(len(support[key]&support[f]) <= 1 for f in FIRST)]
    disjoint = [key for key in eligible if not support[key]&initial]
    thirds = [key for key in eligible if key not in disjoint and key != NAMED]
    check('exact ordered universes', len(universe) == 756 and len(disjoint) == 30
          and len(thirds) == len(historical['thirds']) == 351)
    check('source has no failures', source['failures'] == historical['failures'] == [])
    block_cache = {}

    def block(key):
        if key not in block_cache:
            original = direct.block(*key)['matrix']
            alternate = independent.block(*key)
            check('entrywise independent block '+str(key), original == alternate)
            block_cache[key] = original
        return block_cache[key]

    records, manifest, partition, overlap = [], [], [], Counter()
    ranks, coordinate_counts = Counter(), Counter()
    vector_count = 0
    for meta in source['thirds']:
        if not meta['remaining']:
            continue
        n = meta['third_index']
        path = HERE/meta['certificate']
        shard = json.loads(path.read_bytes())
        hist_path = HERE/shard['source_shard']
        hist = json.loads(hist_path.read_bytes())
        check(f'{n}: shard provenance', digest(path) == meta['sha256']
              == audit['artifact_hashes_after'][meta['certificate']]
              and digest(hist_path) == shard['source_sha256']
              and hist_path == HERE/historical['thirds'][n]['certificate'])
        check(f'{n}: ordered third and complete fourth list',
              historical['thirds'][n]['third_index'] == n
              and (tuple(historical['thirds'][n]['third_I']), tuple(historical['thirds'][n]['third_K'])) == thirds[n]
              and [(tuple(c['I']), tuple(c['K'])) for c in hist['cases']] == universe)
        selected = [c for c in shard['cases'] if c['status'] == 'unresolved']
        indices = [c['fourth_index'] for c in selected]
        check(f'{n}: exact retained indices', indices == shard['remaining_indices']
              and len(indices) == meta['remaining'] and len(set(indices)) == len(indices))
        manifest.append({'third_index': n, 'path': meta['certificate'], 'sha256': digest(path),
                         'historical_path': shard['source_shard'], 'historical_sha256': digest(hist_path),
                         'selected_fourth_indices': indices})
        for case in selected:
            u = case['fourth_index']
            prefix = f'({n},{u})'
            rows = FIRST+[thirds[n], universe[u]]
            check(prefix+' support indices/linearity',
                  case['four_rows'] == [[list(a), list(b)] for a, b in rows]
                  and all(len(support[a]&support[b]) <= 1 for a, b in combinations(rows, 2)))
            matrix = [r for key in rows for r in block(key)]
            rank, original_rows = direct.rank_and_rows(matrix)
            rank2, pivots = independent.column_rank(matrix)
            basis, free = case['kernel_basis'], case['free_columns']
            check(prefix+' two exact ranks', rank == rank2 == case['rank'] == hist['cases'][u]['rank'])
            check(prefix+' complete original basis', basis == hist['cases'][u]['kernel_basis']
                  and len(basis) == 21-rank and all(len(v) == 21 for v in basis)
                  and all(type(x) is int and 0 <= x < P for v in basis for x in v)
                  and free == sorted(set(range(21))-set(pivots))
                  and [[v[c] for c in free] for v in basis] ==
                  [[int(a == b) for b in range(len(basis))] for a in range(len(basis))])
            residuals = [[sum(a*b for a, b in zip(row, v)) % P for row in matrix] for v in basis]
            check(prefix+' all original stack residuals', not any(map(any, residuals))
                  and residuals == case['original_stack_residuals'])
            check(prefix+' original-row rank witness',
                  independent.column_rank([matrix[r] for r in original_rows])[0] == rank)
            tests = []
            for x in range(7):
                columns = [c for c, pair in enumerate(pairs) if x in pair]
                entries = [[v[c] for c in columns] for v in basis]
                nonzero = [(b, c, basis[b][c]) for b in range(len(basis))
                           for c in columns if basis[b][c]]
                omitted = not nonzero
                check(prefix+f' coordinate {S[x]} six-entry test', len(columns) == 6
                      and omitted == (not any(map(any, entries))))
                tests.append({'coordinate': S[x], 'incident_columns': columns,
                              'complete_incident_coefficients': entries, 'omitted': omitted,
                              'nonzero_witness': list(nonzero[0]) if nonzero else None})
                if omitted:
                    coordinate_counts[S[x]] += 1
            omitted_labels = [test['coordinate'] for test in tests if test['omitted']]
            prior = []
            if universe[u] in disjoint:
                prior.append('L112_exchanged_rows')
            if (n, u) == (0, 279):
                prior.append('L117')
            status = 'excluded_inactive_coordinate' if omitted_labels else 'screen_failure'
            overlap['+'.join(prior or ['none'])+':'+status] += 1
            partition.append({'third_index': n, 'fourth_index': u, 'status': status,
                              'omitted_coordinates': omitted_labels, 'prior_exclusions': prior})
            ranks[rank] += 1
            vector_count += len(basis)
            records.append({'third_index': n, 'fourth_index': u, 'four_rows': case['four_rows'],
                            'rank': rank, 'independent_original_rows': original_rows,
                            'independent_pivot_columns': pivots, 'free_columns': free,
                            'kernel_basis': basis, 'original_stack_residuals': residuals,
                            'coordinate_tests': tests, 'status': status,
                            'prior_exclusions': prior})
    passing = [r for r in partition if r['status'] == 'excluded_inactive_coordinate']
    new = [r for r in passing if not r['prior_exclusions']]
    check('exact domain sizes', len(records) == 599 and len(manifest) == 56
          and [m['third_index'] for m in manifest] == source['remaining_third_indices'])
    check('all 599 indexed occurrences unique', len({(r['third_index'], r['fourth_index']) for r in records}) == 599)
    check('prior-exclusion controls', sum('L112_exchanged_rows' in r['prior_exclusions'] for r in records) == 9
          and sum('L117' in r['prior_exclusions'] for r in records) == 1)
    # Every source artifact is read-only during this calculation.
    check('audited inputs still unchanged', all(digest(HERE/name) == value
          for name, value in audit['artifact_hashes_after'].items()))
    summary = {'actual_occurrences': len(records), 'required_occurrences': 599,
               'actual_thirds': len(manifest), 'required_thirds': 56,
               'basis_vectors': vector_count, 'original_residual_entries': 24*vector_count,
               'coordinate_tests': 7*len(records), 'passing_occurrences': len(passing),
               'failing_occurrences': len(records)-len(passing), 'new_relative_to_L112_L117': len(new),
               'rank_histogram': dict(sorted(ranks.items())),
               'omitted_coordinate_histogram': dict(sorted(coordinate_counts.items())),
               'overlap_histogram': dict(sorted(overlap.items()))}
    output = {'scope': 'exact L116 retained domain; whole-kernel omission only',
              'modulus': P, 'H': h, 'S': S, 'column_pairs': [[S[a], S[b]] for a, b in pairs],
              'audit_path': audit_path.name, 'audit_sha256': digest(audit_path),
              'source_path': master_path.name, 'source_sha256': digest(master_path),
              'code_sha256': digest(Path(__file__)), 'summary': summary, 'manifest': manifest,
              'partition': partition, 'records': records, 'checks': checks, 'failures': failures}
    path = HERE/'inactive-coordinate-screen.json'
    path.write_text(json.dumps(output, separators=(',', ':'))+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: {len(failures)}; certificate: {path}')
    if failures:
        print('First failures:', failures[:8])
    assert not failures


if __name__ == '__main__':
    run()
