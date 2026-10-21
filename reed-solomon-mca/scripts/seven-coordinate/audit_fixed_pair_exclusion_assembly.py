"""Separate L124 provenance/coverage audit; reuse scoped mathematical audits.

Does not rerun historical rank/locus computations or enlarge the target.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent
TARGET = BASE / 'fixed-pair-assembly-critical-audit.json'


def digest(path):
    h = sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def read(name):
    return json.loads((BASE / name).read_bytes())


def run():
    out = {'scope': 'Separate bounded L124 proof/program audit',
           'checks': [], 'audit_schemas': [], 'executions': [],
           'plane_bindings': [], 'failures': []}

    def require(name, condition):
        out['checks'].append({'check': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)

    def wedge(u, v):
        w = [(u[i]*v[j]-u[j]*v[i]) % 97 for i, j in combinations(range(7), 2)]
        pivot = next(x for x in w if x)
        return [x*pow(pivot, -1, 97) % 97 for x in w]

    try:
        master = read('fixed-pair-exclusion-assembly.json')
        require('successful existing master', master['failures'] == master['uncovered'] == [])
        expected = master['source_hashes']
        require('all 643 frozen sources match', len(expected) == 643 and
                all(digest(ROOT / p) == h for p, h in expected.items()))
        require('ten distinct canonical audits', len(master['audit_bindings']) == 10 and
                len({a['path'] for a in master['audit_bindings']}) == 10)
        for binding in master['audit_bindings']:
            name = binding['path']
            a = read(name)
            require(name + ' exact binding and no failures',
                    binding['sha256'] == digest(BASE / name) ==
                    expected['scripts/seven-coordinate/' + name] and a['failures'] == [])
            # Explicitly validate each present schema, rather than treating an
            # absent optional field as a successful execution.
            success_fields = []
            if 'checks' in a:
                require(name + ' complete checks', bool(a['checks']) and all(x['passed'] for x in a['checks']))
                success_fields.append('checks')
            if 'replay_returncode' in a:
                require(name + ' replay exit', a['replay_returncode'] == 0)
                success_fields.append('replay_returncode')
            for field in ['runs', 'executions', 'program_replays']:
                if field in a:
                    require(name + ' ' + field, bool(a[field]) and all(x['returncode'] == 0 for x in a[field]))
                    for x in a[field]:
                        if 'byte_identical' in x:
                            require(name + ' replay byte identity', x['byte_identical'])
                    success_fields.append(field)
            for field in ['artifact_hashes', 'hashes', 'code_hashes']:
                before, after = field + '_before', field + '_after'
                if before in a:
                    require(name + ' ' + field + ' unchanged', a[before] == a[after])
                    for p, h in a[after].items():
                        require(name + ' manifested ' + p,
                                digest(BASE / p) == h == expected[str((BASE / p).resolve().relative_to(ROOT))])
            for field, root in [('code_hashes', BASE), ('unchanged_hashes', ROOT)]:
                for p, h in a.get(field, {}).items():
                    require(name + ' bound ' + p,
                            digest(root / p) == h == expected[str((root / p).resolve().relative_to(ROOT))])
            if name == 'nondisjoint-third-critical-audit.json':
                require('L113 explicit supplement success schema', a['summary']['failures'] == 0
                        and a['summary']['source_and_replay_unchanged'] is True
                        and len(a['unchanged_hashes']) == 4)
                replay = read('nondisjoint-third-diagnostic-replay.json')
                require('L113 complete saved replay successful', replay['failures'] == [] and len(replay['cases']) == 756)
                success_fields.append('summary and complete saved replay')
            require(name + ' declares success evidence', bool(success_fields))
            out['audit_schemas'].append({'path': name, 'success_fields': success_fields})

        failure_name = 'fixed-pair-exclusion-assembly-first-schema-failure.json'
        first = read(failure_name)
        require('initial schema failure preserved before coverage',
                first['failures'] == [{'type': 'KeyError', 'message': "'unresolved'"}]
                and first['thirds'] == first['uncovered'] == []
                and first['source_hashes'] == expected and all(c['passed'] for c in first['checks']))
        out['initial_failure_sha256'] = digest(BASE / failure_name)
        out['initial_program_sha256'] = first['program_sha256']
        require('repaired source declares optional unresolved schema exactly',
                'unresolved' not in read('rank20-selected-gates.json') and
                all(read(n)['unresolved'] == [] for n in ['active-rank19-complete-loci.json',
                    'intrinsic-survivor-full-rows.json', 'rank20-survivor-full-rows.json']))

        # Bind every completed plane to all indexed source loci, not just to
        # a union of historical indices or a shortfall disposition string.
        loci = {tuple(r['historical_index']): r for r in read('active-rank19-complete-loci.json')['records']}
        rank20 = {tuple(r['historical_index']): r for r in read('rank20-selected-gates.json')['records']}
        for source, records, required in [('intrinsic-survivor-full-rows.json', loci, 4),
                                          ('rank20-survivor-full-rows.json', rank20, 6)]:
            seen = []
            for plane in read(source)['planes']:
                w = wedge(plane['u'], plane['v'])
                summary = plane['summary']
                require(source + ' full pre-chart shortfall', summary['covered_rows'] == summary['required_rows'] == 756
                        and summary['distinct_directions_before_chart'] == 4
                        and summary['required_distinct_directions'] == 12 and summary['shortfall'] == 8
                        and plane['duplicate_direction_groups'] == [])
                for idx in map(tuple, plane['historical_indices']):
                    r = records[idx]
                    points = (r['points_and_all_row_gates'] if source.startswith('intrinsic')
                              else [r['plane_and_all_row_gates']])
                    passing = [p for p in points if p['passes_intrinsic_gates']]
                    require(source + ' exact forced plane ' + str(idx), len(passing) == 1 and
                            wedge(passing[0]['u'], passing[0]['v']) == w)
                    seen.append(idx)
                    out['plane_bindings'].append({'source': source, 'index': idx, 'normalized_wedge': w})
            require(source + ' complete distinct indexed completions', len(seen) == len(set(seen)) == required)
            selected = ({i for i, r in loci.items() if r['disposition'] == 'intrinsic_survivor'}
                        if source.startswith('intrinsic') else set(rank20))
            require(source + ' exact source selector', set(seen) == selected)

        artifacts = ['fixed-pair-exclusion-assembly.json', 'fixed-pair-exclusion-assembly-replay.json', failure_name]
        artifacts += [r['certificate'] for r in master['thirds']]
        require('382 distinct output shards', len(master['thirds']) == 382 and len(set(artifacts)) == 385)
        out['artifact_hashes_before'] = {p: digest(BASE / p) for p in artifacts}
        out['code_hashes_before'] = {p: digest(BASE / p) for p in
                ['fixed_pair_exclusion_assembly.py', 'verify_fixed_pair_exclusion_assembly.py']}
        log = BASE / 'fixed-pair-assembly-critical-audit.log'
        with log.open('w') as stream:
            for program in out['code_hashes_before']:
                result = subprocess.run([sys.executable, str(BASE / program)], cwd=ROOT,
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                stream.write(program + '\n' + result.stdout + '\n')
                out['executions'].append({'program': program, 'returncode': result.returncode})
                require(program + ' complete execution', result.returncode == 0)
        out['artifact_hashes_after'] = {p: digest(BASE / p) for p in artifacts}
        out['code_hashes_after'] = {p: digest(BASE / p) for p in out['code_hashes_before']}
        require('all 385 output/failure artifacts byte identical', out['artifact_hashes_before'] == out['artifact_hashes_after'])
        require('both inspected programs unchanged', out['code_hashes_before'] == out['code_hashes_after'])
        replay = read('fixed-pair-exclusion-assembly-replay.json')
        require('full replay success and all checks', replay['failures'] == [] and
                all(c['passed'] for c in replay['checks']) and len(replay['thirds']) == 382)
        counts = Counter()
        overlaps = []
        fixed_union = {x for row in master['first_two'] for pair in row for x in pair}
        for meta, verified in zip(master['thirds'], replay['thirds']):
            shard = read(meta['certificate'])
            require('each complete output shard bound', digest(BASE / meta['certificate']) == meta['sha256'] and
                    shard['failures'] == [] and shard['third'] == verified['third'])
            require('every occurrence independently scope checked',
                    [r['fourth_index'] for r in shard['cases']] == verified['eligible_fourths'] and
                    len(shard['cases']) == len(verified['complete_scoped_checks']) and
                    all(v['scope_matches'] and v['fourth_index'] == r['fourth_index'] and
                        v['disposition'] == r['disposition']
                        for r, v in zip(shard['cases'], verified['complete_scoped_checks'])))
            n = verified['historical_third_index']
            for r in shard['cases']:
                idx = [n, r['fourth_index']] if n is not None else None
                require('exact historical occurrence identity', r['historical_index'] == idx)
                earlier = []
                if n is not None:
                    fourth_set = {x for pair in r['fourth'] for x in pair}
                    if not fourth_set & fixed_union:
                        earlier = ['L112_exchanged_rows']
                    elif fourth_set == {1, 22, 75, 79}:
                        earlier = ['L113_exchanged_rows']
                require('exact preserved earlier-scope overlap', r['earlier_scope_overlaps'] == earlier)
                if earlier:
                    overlaps.append({'historical_index': idx, 'exclusions': earlier,
                                     'selected_disposition': r['disposition'],
                                     'rows': master['first_two'] + [shard['third'], r['fourth']]})
            counts.update(r['disposition'] for r in shard['cases'])
        require('complete ordered overlap manifest preserved', overlaps == master['overlaps'])
        require('complete 100764 dispositions and no omissions', sum(counts.values()) == 100764 and
                dict(counts) == master['summary']['dispositions'] == replay['summary']['dispositions'])
        require('all imported sources unchanged at finish', all(digest(ROOT / p) == h for p, h in expected.items()))
        out['summary'] = {'actual_thirds': len(master['thirds']), 'required_thirds': 382,
                          'actual_occurrences': sum(counts.values()), 'required_occurrences': 100764,
                          'actual_audits': len(out['audit_schemas']), 'required_audits': 10,
                          'frozen_inputs_checked': len(expected), 'artifacts_byte_identical': len(artifacts),
                          'plane_index_bindings': len(out['plane_bindings']), 'dispositions': dict(counts),
                          'preserved_overlap_records': len(overlaps), 'uncovered': 0}
    except Exception as exc:
        out['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
    out['audit_program_sha256'] = digest(Path(__file__))
    TARGET.write_text(json.dumps(out, separators=(',', ':')) + '\n')
    print(json.dumps(out.get('summary', {}), sort_keys=True))
    print('Failures:', len(out['failures']), '; full certificate:', TARGET)
    if out['failures']:
        print(out['failures'][0])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
