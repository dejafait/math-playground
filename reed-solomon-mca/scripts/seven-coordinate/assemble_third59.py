"""Compare only the audited third-59 domain and two residual exclusions.

No matrix search, new locus calculation, census enlargement or input writes.
The mathematical actual-row selection argument is in canonical L131.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
OUT = HERE / 'third59-assembly.json'


def run():
    evidence = dict(checks=[], failures=[], input_sha256={})

    def check(name, condition):
        evidence['checks'].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    def digest(name):
        value = sha256((HERE / name).read_bytes()).hexdigest()
        evidence['input_sha256'][name] = value
        return value

    def read(name):
        digest(name)
        return json.loads((HERE / name).read_bytes())

    try:
        master = read('new-pair-filter.json')
        replay = read('new-pair-filter-replay.json')
        shard_name = 'new-pair-filter/third-059.json'
        shard = read(shard_name)
        audit = read('l125-critical-audit.json')
        # Only the active shard and eight common audit inputs are touched.
        selected_hashes = {k: v for k, v in audit['audited_input_hashes'].items()
                           if '/' not in k or k == shard_name}
        check('nine scoped L125 audit bindings', len(selected_hashes) == 9)
        for name, expected in selected_hashes.items():
            check('L125 hash ' + name, digest(name) == expected)
        check('L125 fresh audit replay/log binding',
              digest('audit_l125_partition.py') == audit['audit_code_sha256']
              and digest('l125-critical-audit-replay.log') == audit['complete_replay_log_sha256'])
        check('L125 complete successful audit', audit['failures'] == []
              and audit['original_artifacts_byte_unchanged'] is True
              and audit['full_saved_replay_identical'] is True)
        check('L125 master/replay/audit summary agreement',
              master['summary'] == replay['summary'] == audit['summary']
              and master['failures'] == replay['failures'] == [])
        check('L125 replay binds master', replay['source_sha256'] == digest('new-pair-filter.json'))

        h = [x for x in range(1, 97) if pow(x, 16, 97) == 1]
        s = [1, 8, 12, 18, 22, 27, 33]
        j = sorted(set(h) - set(s))
        # Generate rows without importing any historical domain helper.
        universe = [[list(i), list(k)] for i in combinations(s, 2) for k in combinations(j, 2)]
        supports = [frozenset(i + k) for i, k in universe]
        seed_indices = [0, 412, 59]
        expected_seed = [[[1, 8], [47, 50]], [[12, 18], [64, 75]], [[1, 12], [70, 85]]]
        check('frozen field and full lexicographic universe',
              master['modulus'] == 97 and master['H'] == h and master['S'] == s
              and master['J'] == j and master['universe'] == universe
              and len(universe) == len(set(supports)) == 756)
        check('exact actual three-support seed',
              [universe[i] for i in seed_indices] == expected_seed
              and master['first_indices'] == seed_indices[:2]
              and master['first_two'] == expected_seed[:2] and shard['third_index'] == 59)
        check('third-59 eligibility and membership',
              master['third_screen'][59] == dict(index=59, intersections=[1, 1], distinct=True, eligible=True)
              and master['third_indices'].count(59) == 1
              and all(len(supports[a] & supports[b]) <= 1 for a, b in combinations(seed_indices, 2)))
        meta = [x for x in master['thirds'] if x['third_index'] == 59]
        rmeta = [x for x in replay['thirds'] if x['third_index'] == 59]
        check('unique audited shard manifest', len(meta) == 1 and meta == rmeta
              and meta[0]['certificate'] == shard_name and meta[0]['sha256'] == digest(shard_name))

        screen = []
        for index, support in enumerate(supports):
            intersections = [len(support & supports[k]) for k in seed_indices]
            distinct = index not in seed_indices
            screen.append(dict(index=index, intersections=intersections, distinct=distinct,
                               eligible=distinct and all(x <= 1 for x in intersections)))
        eligible = [x['index'] for x in screen if x['eligible']]
        check('complete 756 fourth-screen entries', screen == shard['fourth_screen'])
        check('complete ordered eligible fourth cases',
              [x['fourth_index'] for x in shard['cases']] == eligible
              and len(eligible) == len(set(eligible)) == meta[0]['cases'] == 282 and shard['failures'] == [])
        pairs = list(combinations(s, 2))
        check('exterior column order', master['column_pairs'] == [list(p) for p in pairs])
        coverage = []
        for offset, record in enumerate(shard['cases']):
            index, rank = record['fourth_index'], record['rank']
            basis = record['kernel_basis']
            check(f'{index}: complete saved basis dimensions and minor',
                  0 <= rank <= 21 and len(basis) == 21 - rank
                  and all(len(v) == 21 for v in basis) and record['minor_residue'] % 97 != 0)
            if rank == 21:
                status = 'rank'
                check(f'{index}: full-rank disposition', record['factor_tests'] == record['omission_tests'] == [])
            else:
                factors, omissions = [], []
                for row, key in enumerate(expected_seed + [universe[index]]):
                    for c in key[0]:
                        columns = [a for a, pair in enumerate(pairs) if c not in pair]
                        witness = next(([b, a, v[a]] for b, v in enumerate(basis)
                                        for a in columns if v[a]), None)
                        factors.append(dict(row=row, coordinate=c, passes=witness is None, failure_witness=witness))
                for c in s:
                    columns = [a for a, pair in enumerate(pairs) if c in pair]
                    witness = next(([b, a, v[a]] for b, v in enumerate(basis)
                                    for a in columns if v[a]), None)
                    omissions.append(dict(coordinate=c, passes=witness is None, failure_witness=witness))
                check(f'{index}: all complete factor/omission predicates and witnesses',
                      factors == record['factor_tests'] and omissions == record['omission_tests'])
                status = ('factor' if any(x['passes'] for x in factors) else
                          'omission' if any(x['passes'] for x in omissions) else 'residual')
            check(f'{index}: audited priority disposition', status == record['status'])
            coverage.append(dict(fourth_index=index, support=universe[index], status=status,
                                 source_pointer=f'/cases/{offset}'))
        statuses = dict(sorted(Counter(x['status'] for x in coverage).items()))
        residuals = [x['fourth_index'] for x in coverage if x['status'] == 'residual']
        check('complete status counts and exactly two residuals',
              statuses == meta[0]['statuses'] and residuals == shard['residual_indices'] == [355, 647])
        check('preserved historical residual membership',
              [x for x in master['residual_occurrences'] if x[0] == 59] == [[59, 355], [59, 647]])

        residual_bindings = []
        for index, word, audit_name, fourth in [
            (355, 'first', 'l129-critical-audit.json', [[8, 27], [79, 89]]),
            (647, 'second', 'l130-critical-audit.json', [[18, 33], [89, 96]])
        ]:
            exact_audit = read(audit_name)
            for name, expected in exact_audit['input_sha256'].items():
                check(f'{index}: audit hash {name}', digest(name) == expected)
            checks = exact_audit['checks']
            success = all(checks.values()) if isinstance(checks, dict) else all(x['passes'] for x in checks)
            runs = exact_audit.get('runs', exact_audit.get('isolated_runs'))
            check(f'{index}: complete successful separate audit', success and exact_audit['failures'] == []
                  and len(runs) == 2 and all(x['returncode'] == 0 for x in runs))
            check(f'{index}: audit scope',
                  exact_audit.get('target') == [59, index] if index == 355 else
                  exact_audit['scope'] == 'L130 only: full-universe occurrence (59,647); no new census or assembly')
            name = f'third59-{word}-residual-gates.json'
            cert = read(name)
            exact_replay = read(f'third59-{word}-residual-gates-replay.json')
            rows = expected_seed + [fourth]
            selected = next(x for x in shard['cases'] if x['fourth_index'] == index)
            source = cert['source']
            check(f'{index}: exact labels, indices and audited source binding',
                  universe[index] == fourth and cert['rows'] == [dict(I=i, K=k) for i, k in rows]
                  and cert['H'] == h and cert['S'] == s and cert['J'] == j
                  and source['full_universe_indices'] == [59, index]
                  and source['shard_path'] == shard_name and source['shard_sha256'] == digest(shard_name)
                  and source['sha256'] == digest(source['path']))
            pointed = json.loads((HERE / source['path']).read_bytes())
            for part in source['pointer'].strip('/').split('/'):
                pointed = pointed[int(part)] if isinstance(pointed, list) else pointed[part]
            check(f'{index}: exact source pointer record',
                  pointed == selected['kernel_basis'] == cert['kernel_basis'])
            check(f'{index}: complete residual basis and audit certificate match',
                  selected['status'] == 'residual' and selected['rank'] == 19
                  and selected['kernel_basis'] == cert['kernel_basis']
                  and selected['minor_rows'] == cert['rank_minor_rows']
                  and selected['pivot_columns'] == cert['rank_minor_columns']
                  and selected['minor_residue'] == cert['rank_minor_residue']
                  and selected['kernel_residuals'] == cert['kernel_residuals']
                  and cert['column_pairs'] == master['column_pairs']
                  and cert['import_binding'] == dict(locus='L126' if index == 355 else 'L127',
                                                    identical_rows=[1, 2, 4], changed_row=3)
                  and cert['summary']['intrinsically_passing_points'] == 0
                  and cert['summary']['unresolved_branches'] == 0
                  and cert['summary']['complete_projective_points'] == 2
                  and exact_replay['certificate_sha256'] == digest(name)
                  and cert['failures'] == exact_replay['failures'] == [])
            residual_bindings.append(dict(fourth_index=index, support=fourth,
                                          lemma='L129' if index == 355 else 'L130',
                                          audit=audit_name, source=source,
                                          shard_case_pointer=f'/cases/{eligible.index(index)}',
                                          complete_kernel_basis=selected['kernel_basis'],
                                          minor_rows=selected['minor_rows'],
                                          minor_columns=selected['pivot_columns'],
                                          minor_residue=selected['minor_residue'],
                                          complete_points=2, passing_points=0))

        evidence.update(third_index=59, seed_indices=seed_indices, seed=expected_seed,
                        full_fourth_screen=screen, eligible_fourth_indices=eligible, coverage=coverage,
                        statuses=statuses, residual_bindings=residual_bindings,
                        summary=dict(actual_screen=756, required_screen=756, actual_eligible=len(eligible),
                                     required_eligible=282, covered=len(coverage), uncovered=0,
                                     residuals_bound=2, residuals_required=2),
                        qualification='Restricted indexed assembly comparison; audited exclusions reused, no new loci or global bound.')
        check('all original inputs byte unchanged', all(sha256((HERE / n).read_bytes()).hexdigest() == v
                                                      for n, v in evidence['input_sha256'].items()))
    except Exception as error:
        evidence['failures'].append(f'{type(error).__name__}: {error}')
    OUT.write_text(json.dumps(evidence, indent=2) + '\n')
    print('Summary:', json.dumps(evidence.get('summary', {}), sort_keys=True))
    print('Statuses:', json.dumps(evidence.get('statuses', {}), sort_keys=True))
    print(f'Checks passed/required: {sum(x["passes"] for x in evidence["checks"])}/{len(evidence["checks"])}; '
          f'failures: {len(evidence["failures"])}; certificate: {OUT}')
    if evidence['failures']:
        print('Failures:', evidence['failures'])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
