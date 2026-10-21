"""Separate L118 audit of saved evidence, without enlarging/rerunning the screen."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import subprocess
import sys

import zero_anchor_support_filter as direct
import verify_fixed_three_row_extensions as independent

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def run():
    checks, failures = [], []

    def check(name, value):
        checks.append({'check': name, 'passed': bool(value)})
        if not value:
            failures.append(name)

    audit_path = HERE/'residual-coordinate-partition-critical-audit.json'
    audit = json.loads(audit_path.read_bytes())
    screen_path = HERE/'inactive-coordinate-screen.json'
    screen = json.loads(screen_path.read_bytes())
    master_path = HERE/'residual-coordinate-factors.json'
    master = json.loads(master_path.read_bytes())
    historical = json.loads((HERE/master['source']).read_bytes())
    names = set(audit['artifact_hashes_after']) | {
        audit_path.name, screen_path.name, 'inactive-coordinate-screen-replay.json'}
    before = {name: digest(HERE/name) for name in sorted(names)}
    code_names = ['inactive_coordinate_screen.py', 'verify_inactive_coordinate_screen.py',
                  'zero_anchor_support_filter.py', 'verify_fixed_three_row_extensions.py',
                  'audit_inactive_coordinate_partition.py']
    code_hashes = {name: digest(HERE/name) for name in code_names}
    check('successful step-321 audit', not audit['failures'] and audit['replay_returncode'] == 0
          and all(c['passed'] for c in audit['checks']))
    check('step-321 immutable manifest', audit['artifact_hashes_before'] == audit['artifact_hashes_after'])
    for name, value in audit['artifact_hashes_after'].items():
        check('audited artifact '+name, before[name] == value)
    for name, value in audit['code_hashes'].items():
        check('audited code '+name, digest(HERE/name) == value)
    check('screen source and code binding', screen['source_path'] == master_path.name
          and screen['source_sha256'] == digest(master_path)
          and screen['audit_path'] == audit_path.name and screen['audit_sha256'] == digest(audit_path)
          and screen['code_sha256'] == code_hashes['inactive_coordinate_screen.py']
          and not screen['failures'] and all(c['passed'] for c in screen['checks']))
    s, j = direct.S, direct.J
    universe = list(product(combinations(s, 2), combinations(j, 2)))
    support = {k: set(k[0]+k[1]) for k in universe}
    first = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
    union = support[first[0]] | support[first[1]]
    eligible = [k for k in universe if all(len(support[k]&support[f]) <= 1 for f in first)]
    removed = [k for k in eligible if not support[k]&union]
    thirds = [k for k in eligible if k not in removed and k != ((1, 22), (75, 79))]
    check('ordered universes', (len(universe), len(eligible), len(removed), len(thirds)) == (756, 382, 30, 351)
          and thirds == [(tuple(m['third_I']), tuple(m['third_K'])) for m in historical['thirds']])
    check('exact L112 overlap domain', removed == list(product(
        combinations([22, 27, 33], 2), combinations([75, 79, 85, 89, 96], 2))))
    expected, originals, manifest = [], {}, []
    for meta in master['thirds']:
        if not meta['remaining']:
            continue
        n = meta['third_index']
        path = HERE/meta['certificate']
        shard = json.loads(path.read_bytes())
        hist_path = HERE/shard['source_shard']
        hist = json.loads(hist_path.read_bytes())
        check(f'{n}: provenance', digest(path) == meta['sha256']
              and digest(hist_path) == shard['source_sha256']
              and shard['source_shard'] == historical['thirds'][n]['certificate'])
        selected = [c for c in shard['cases'] if c['status'] == 'unresolved']
        indices = [c['fourth_index'] for c in selected]
        check(f'{n}: complete retained indices', indices == shard['remaining_indices']
              and len(indices) == meta['remaining'])
        manifest.append({'third_index': n, 'path': meta['certificate'], 'sha256': digest(path),
                         'historical_path': shard['source_shard'], 'historical_sha256': digest(hist_path),
                         'selected_fourth_indices': indices})
        for c in selected:
            index = (n, c['fourth_index'])
            expected.append(index)
            originals[index] = (c, hist['cases'][index[1]])
    check('exact manifest and ordered domain', screen['manifest'] == manifest
          and expected == [(r['third_index'], r['fourth_index']) for r in screen['records']]
          and len(expected) == len(set(expected)) == 599 and len(manifest) == 56
          and [m['third_index'] for m in manifest] == master['remaining_third_indices'])
    blocks, ranks, omissions, overlap = {}, Counter(), Counter(), Counter()
    vectors = residual_entries = 0
    partition = []
    for record in screen['records']:
        n, u = record['third_index'], record['fourth_index']
        rows = first+[thirds[n], universe[u]]
        case, old = originals[(n, u)]
        check(f'{n},{u}: support family', record['four_rows'] == case['four_rows']
              == [[list(a), list(b)] for a, b in rows]
              and all(len(support[a]&support[b]) <= 1 for a, b in combinations(rows, 2)))
        for key in rows:
            if key not in blocks:
                blocks[key] = direct.block(*key)['matrix']
                check('original/derivative block '+str(key), blocks[key] == independent.block(*key))
        matrix = [r for key in rows for r in blocks[key]]
        rank, chosen = direct.rank_and_rows(matrix)
        rank2, pivots = independent.column_rank(matrix)
        basis, free = record['kernel_basis'], record['free_columns']
        check(f'{n},{u}: ranks and witnesses', rank == rank2 == record['rank'] == case['rank'] == old['rank']
              and chosen == record['independent_original_rows']
              and pivots == record['independent_pivot_columns']
              and independent.column_rank([matrix[r] for r in chosen])[0] == rank)
        residuals = [[sum(a*b for a, b in zip(row, v)) % 97 for row in matrix] for v in basis]
        check(f'{n},{u}: complete original kernel', basis == case['kernel_basis'] == old['kernel_basis']
              and len(basis) == 21-rank and all(len(v) == 21 for v in basis)
              and all(type(x) is int and 0 <= x < 97 for v in basis for x in v)
              and free == sorted(set(range(21))-set(pivots))
              and [[v[c] for c in free] for v in basis] ==
                  [[int(a == b) for b in range(len(basis))] for a in range(len(basis))]
              and not any(map(any, residuals))
              and residuals == record['original_stack_residuals'] == case['original_stack_residuals'])
        missing = [x for i, x in enumerate(s) if all(
            not v[c] for v in basis for c, pair in enumerate(direct.PAIRS) if i in pair)]
        check(f'{n},{u}: omitted set exactly as stated', not missing or missing == [22, 27, 33])
        prior = ['L112_exchanged_rows'] if universe[u] in removed else []
        if (n, u) == (0, 279):
            prior.append('L117')
            check('L117 exact support identity', rows[2:] == [((1, 12), (75, 79)), ((8, 18), (75, 85))])
        status = 'excluded_inactive_coordinate' if missing else 'screen_failure'
        check(f'{n},{u}: disposition', record['status'] == status and record['prior_exclusions'] == prior)
        partition.append({'third_index': n, 'fourth_index': u, 'status': status,
                          'omitted_coordinates': missing, 'prior_exclusions': prior})
        ranks[rank] += 1
        omissions.update(missing)
        overlap['+'.join(prior or ['none'])+':'+status] += 1
        vectors += len(basis)
        residual_entries += sum(map(len, residuals))
    check('complete partition', partition == screen['partition'])
    check('written exact counts', dict(ranks) == {19: 593, 20: 6}
          and dict(omissions) == {22: 360, 27: 360, 33: 360}
          and vectors == 1192 and residual_entries == 28608
          and dict(overlap) == {'L117:excluded_inactive_coordinate': 1,
              'none:excluded_inactive_coordinate': 359, 'L112_exchanged_rows:screen_failure': 9,
              'none:screen_failure': 230})
    log_path = HERE/'inactive-coordinate-partition-critical-audit.log'
    with log_path.open('w') as log:
        replay = subprocess.run([sys.executable, str(HERE/'verify_inactive_coordinate_screen.py')],
                                stdout=log, stderr=subprocess.STDOUT)
    verified = json.loads((HERE/'inactive-coordinate-screen-replay.json').read_bytes())
    check('complete independent replay succeeds', replay.returncode == 0 and not verified['failures']
          and all(c['passed'] for c in verified['checks'])
          and verified['partition'] == partition and verified['summary'] == screen['summary'])
    after = {name: digest(HERE/name) for name in sorted(names)}
    check('all source/target artifacts unchanged', before == after)
    check('all called code unchanged', code_hashes == {name: digest(HERE/name) for name in code_names})
    remaining = [r for r in screen['records'] if r['status'] == 'screen_failure' and not r['prior_exclusions']]
    output = {'scope': 'separate critical audit of exact L118 partition only',
              'summary': screen['summary'], 'checks': checks, 'failures': failures,
              'artifact_hashes_before': before, 'artifact_hashes_after': after,
              'code_hashes': code_hashes, 'replay_returncode': replay.returncode,
              'overlap_histogram': dict(overlap), 'partition': partition,
              'first_uncovered_record': remaining[0]}
    path = HERE/'inactive-coordinate-partition-critical-audit.json'
    path.write_text(json.dumps(output, separators=(',', ':'))+'\n')
    print('Occurrences: 599 / required 599; coordinate tests: 4193 / required 4193')
    print('Passes 360; failures 239; additional indexed exclusions 359; no global bound change')
    print(f'Audit failures: {len(failures)}; replay exit: {replay.returncode}; artifacts: {len(before)} unchanged')
    print(f'Certificate: {path}; log: {log_path}')
    if failures:
        print('Failed checks:', failures)
    assert not failures


if __name__ == '__main__':
    run()
