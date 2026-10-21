"""Exact approved fixed-pair assembly; imports audited exclusions read-only.

No rank/locus calculation, new feasibility solver or four-row converse.
Run from the notebook: python3 scripts/seven-coordinate/fixed_pair_exclusion_assembly.py
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'fixed-pair-exclusion-assembly'
TARGET = HERE / 'fixed-pair-exclusion-assembly.json'
S = [1, 8, 12, 18, 22, 27, 33]
H = [x for x in range(1, 97) if pow(x, 16, 97) == 1]
J = [x for x in H if x not in S]
FIRST = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
NAMED = ((1, 22), (75, 79))


def key(row):
    if isinstance(row, dict):
        return tuple(row['I']), tuple(row['K'])
    return tuple(row[0]), tuple(row[1])


def save(path, value):
    path.write_text(json.dumps(value, separators=(',', ':')) + '\n')


def run():
    OUT.mkdir(exist_ok=True)
    out = {'scope': 'Approved fixed-pair exact indexed assembly only',
           'modulus': 97, 'H': H, 'S': S, 'first_two': FIRST,
           'source_hashes': {}, 'audit_bindings': [], 'thirds': [],
           'overlaps': [], 'uncovered': [], 'checks': [], 'failures': []}
    frozen = out['source_hashes']

    def check(name, condition):
        out['checks'].append({'check': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)

    def digest(path):
        with path.open('rb') as stream:
            h = sha256()
            for data in iter(lambda: stream.read(1024 * 1024), b''):
                h.update(data)
        return h.hexdigest()

    def bind(path, expected=None):
        path = path.resolve()
        check('input in active notebook ' + str(path), path.is_relative_to(ROOT))
        name = str(path.relative_to(ROOT))
        value = digest(path)
        if expected is not None:
            check('exact audited digest ' + name, value == expected)
        if name in frozen:
            check('consistent input digest ' + name, frozen[name] == value)
        frozen[name] = value
        return value

    def load(name, expected=None):
        path = HERE / name
        bind(path, expected)
        value = json.loads(path.read_bytes())
        if 'failures' in value:
            check('no recorded failures ' + name, value['failures'] == [])
        return value

    def audited(name):
        value = load(name)
        if 'checks' in value:
            check('all complete audit checks ' + name,
                  bool(value['checks']) and all(c['passed'] for c in value['checks']))
        if 'replay_returncode' in value:
            check('audit replay exit ' + name, value['replay_returncode'] == 0)
        for runs in ['runs', 'executions', 'program_replays']:
            if runs in value:
                check('all audit executions ' + name, bool(value[runs]) and
                      all(r['returncode'] == 0 for r in value[runs]))
        for before, after in [('artifact_hashes_before', 'artifact_hashes_after'),
                              ('hashes_before', 'hashes_after'),
                              ('code_hashes_before', 'code_hashes_after')]:
            if before in value:
                check('immutable audit manifest ' + name, value[before] == value[after])
                for path, h in value[after].items():
                    bind(HERE / path, h)
        for path, h in value.get('code_hashes', {}).items():
            bind(HERE / path, h)
        # L113's saved paths are notebook-relative, unlike the other audits.
        for path, h in value.get('unchanged_hashes', {}).items():
            bind(ROOT / path, h)
        out['audit_bindings'].append({'path': name, 'sha256': digest(HERE / name)})
        return value

    try:
        for name in ['remaining-third-partition-critical-audit.json',
                     'residual-coordinate-partition-critical-audit.json',
                     'inactive-coordinate-partition-critical-audit.json',
                     'first-active-residual-critical-audit.json',
                     'active-rank19-critical-audit.json',
                     'intrinsic-survivor-critical-audit.json',
                     'rank20-classification-critical-audit.json',
                     'rank20-full-rows-critical-audit.json',
                     'nondisjoint-third-critical-audit.json']:
            audited(name)
        l112 = audited('residual-kernel-critical-audit.json')
        bind(HERE / 'third-row-variation.json', l112['source_sha256'])
        bind(HERE / 'third-row-critical-audit.json', l112['prior_L111_audit_sha256'])
        bind(HERE / 'residual-kernel-gates.json', l112['gate_certificate_sha256'])
        bind(HERE / 'residual-kernel-gates-replay.json', l112['replay_certificate_sha256'])

        universe = list(product(combinations(S, 2), combinations(J, 2)))
        supports = {a: set(a[0] + a[1]) for a in universe}
        initial = supports[FIRST[0]] | supports[FIRST[1]]
        eligible = [a for a in universe if all(len(supports[a] & supports[f]) <= 1 for f in FIRST)]
        disjoint = [a for a in eligible if not supports[a] & initial]
        thirds = [a for a in eligible if a not in disjoint and a != NAMED]
        check('complete distinct ordered domains', len(universe) == len(set(universe)) == 756
              and len(eligible) == 382 and len(disjoint) == 30 and len(thirds) == 351
              and NAMED in eligible and NAMED not in disjoint)
        old = load('remaining-third-factor-filter.json')
        factors = load('residual-coordinate-factors.json')
        screen = load('inactive-coordinate-screen.json')
        loci = load('active-rank19-complete-loci.json')
        intrinsic = load('intrinsic-survivor-full-rows.json')
        rank20 = load('rank20-selected-gates.json')
        extra20 = load('rank20-survivor-full-rows.json')
        named = load('first-active-residual-gates.json')
        check('frozen historical screen', digest(HERE / 'inactive-coordinate-screen.json') ==
              '90b6f145c7993d33a834f3498fb3bee60f08ca328bd8e710af216a70df6172c1')
        check('exact removed thirds', [key(r) for r in old['removed_disjoint_thirds']] == disjoint
              and key(old['removed_named_third']) == NAMED)
        for source in [old, factors, screen, loci, intrinsic, rank20, extra20, named]:
            check('same field and seven-set', source['S'] == S and source['H'] == H
                  and source['modulus'] == 97)
        for source in [loci, intrinsic, extra20]:
            check('no unresolved source branch', source['unresolved'] == [])
        check('fixed first rows and full third manifest',
              [key(r) for r in old['first_two']] == FIRST and len(old['thirds']) == 351)
        screen_map = {(r['third_index'], r['fourth_index']): r for r in screen['records']}
        locus_map = {tuple(r['historical_index']): r for r in loci['records']}
        rank20_map = {tuple(r['historical_index']): r for r in rank20['records']}
        check('unique later indexed domains', len(screen_map) == len(screen['records']) == 599
              and len(locus_map) == len(loci['records']) == 223
              and len(rank20_map) == len(rank20['records']) == 6)
        selected19 = [idx for idx, r in screen_map.items() if r['status'] == 'screen_failure'
                      and r['rank'] == 19 and 'L112_exchanged_rows' not in r['prior_exclusions']
                      and idx != (0, 320)]
        selected20 = [idx for idx, r in screen_map.items() if r['status'] == 'screen_failure'
                      and r['rank'] == 20]
        check('exact later selectors, including source order', list(locus_map) == selected19
              and list(rank20_map) == selected20)
        completed19, completed20 = set(), set()
        for source, target, required in [(intrinsic, completed19, 2), (extra20, completed20, 3)]:
            check('complete survivor plane count', len(source['planes']) == required)
            for plane in source['planes']:
                check('complete-row necessary shortfall', plane['disposition'] == 'excluded_necessary_shortfall'
                      and len(plane['rows']) == 756
                      and [key(r) for r in plane['rows']] == universe)
                target.update(tuple(i) for i in plane['historical_indices'])
        check('exact four rank19 completions', completed19 ==
              {idx for idx, r in locus_map.items() if r['disposition'] == 'intrinsic_survivor'})
        check('exact six rank20 completions', completed20 == set(rank20_map))
        check('L119 exact support/index identification',
              [key(r) for r in named['rows']] == FIRST + [thirds[0], universe[320]]
              and named['source']['historical_indices'] == [0, 320])

        factor_meta = {r['third_index']: r for r in factors['thirds']}
        residuals_seen, screen_seen = set(), set()
        counts, old_statuses, screen_partition = Counter(), Counter(), Counter()
        for e, third in enumerate(eligible):
            n = thirds.index(third) if third in thirds else None
            old_cases, factor_map = None, {}
            if n is not None:
                meta = old['thirds'][n]
                check('ordered historical third', meta['third_index'] == n
                      and key([meta['third_I'], meta['third_K']]) == third)
                shard = load(meta['certificate'], meta['sha256'])
                old_cases = shard['cases']
                check('complete ordered historical fourths', len(old_cases) == 756
                      and [key(c) for c in old_cases] == universe)
                if n in factor_meta:
                    fm = factor_meta[n]
                    fs = load(fm['certificate'], fm['sha256'])
                    factor_map = {r['fourth_index']: r for r in fs['cases']}
                    check('exact historical factor selector', len(factor_map) == len(fs['cases'])
                          and list(factor_map) == shard['residual_case_indices'])
                else:
                    check('no omitted historical residuals', not shard['residual_case_indices'])
            rows3 = FIRST + [third]
            records = []
            for u, fourth in enumerate(universe):
                intersections = [len(supports[fourth] & supports[a]) for a in rows3]
                is_eligible = fourth not in rows3 and max(intersections) <= 1
                if old_cases is not None:
                    check('exact independent fourth eligibility', old_cases[u]['eligible'] == is_eligible)
                if not is_eligible:
                    continue
                rows = rows3 + [fourth]
                idx = (n, u)
                reason = None
                overlaps = []
                if third in disjoint:
                    reason = 'L112_third'
                elif third == NAMED:
                    reason = 'L113_third'
                else:
                    status = old_cases[u]['status']
                    old_statuses[status] += 1
                    if status == 'excluded_rank':
                        reason = 'L114_rank'
                    elif status == 'excluded_label_1_factor':
                        reason = 'L114_factor'
                    else:
                        check('only frozen unresolved status', status == 'unresolved' and u in factor_map)
                        residuals_seen.add(idx)
                        r = factor_map[u]
                        check('factor index/support binding', r['third_index'] == n
                              and r['fourth_index'] == u and [key(a) for a in r['four_rows']] == rows)
                        if r['status'] == 'excluded_coordinate_factor':
                            reason = 'L116_factor'
                        else:
                            check('only frozen factor failure', r['status'] == 'unresolved' and idx in screen_map)
                            screen_seen.add(idx)
                            s = screen_map[idx]
                            check('screen index/support binding', [key(a) for a in s['four_rows']] == rows)
                            screen_partition[s['status']] += 1
                            if s['status'] == 'excluded_inactive_coordinate':
                                reason = 'L118_activity'
                            elif 'L112_exchanged_rows' in s['prior_exclusions']:
                                check('exact exchanged L112 scope', fourth in disjoint and
                                      third in universe and max(intersections) <= 1)
                                reason = 'L112_exchanged_rows'
                            elif idx == (0, 320):
                                reason = 'L119_named'
                            elif idx in locus_map:
                                r = locus_map[idx]
                                check('rank19 support binding', [key(a) for a in r['rows']] == rows)
                                if r['disposition'] == 'excluded_necessary_gates':
                                    reason = 'L120_locus'
                                elif idx in completed19:
                                    reason = 'L121_shortfall'
                            elif idx in completed20:
                                r = rank20_map[idx]
                                check('rank20 support binding', [key(a) for a in r['rows']] == rows)
                                reason = 'L123_shortfall'
                    # Preserve earlier scope overlaps independently of disposition precedence.
                    if fourth in disjoint:
                        overlaps.append('L112_exchanged_rows')
                    elif fourth == NAMED:
                        overlaps.append('L113_exchanged_rows')
                if overlaps:
                    out['overlaps'].append({'historical_index': idx, 'exclusions': overlaps,
                                            'selected_disposition': reason, 'rows': rows})
                if reason is None:
                    out['uncovered'].append({'historical_index': idx, 'rows': rows})
                    reason = 'UNCOVERED'
                counts[reason] += 1
                records.append({'fourth_index': u, 'fourth': fourth,
                                'intersections': intersections, 'disposition': reason,
                                'historical_index': idx if n is not None else None,
                                'earlier_scope_overlaps': overlaps})
            path = OUT / f'third-{e:03d}.json'
            save(path, {'eligible_third_index': e, 'historical_third_index': n,
                        'third': third, 'cases': records, 'failures': []})
            out['thirds'].append({'eligible_third_index': e, 'historical_third_index': n,
                                  'third': third, 'eligible_fourths': len(records),
                                  'certificate': str(path.relative_to(HERE)),
                                  'sha256': digest(path)})
        check('every historical residual visited once', len(residuals_seen) == 24866)
        check('exact screen domain consumed', screen_seen == set(screen_map))
        check('historical partition unchanged', old_statuses == Counter({
            'excluded_rank': 50042, 'excluded_label_1_factor': 18942, 'unresolved': 24866}))
        check('activity partition unchanged', screen_partition == Counter({
            'excluded_inactive_coordinate': 360, 'screen_failure': 239}))
        check('no eligible occurrence uncovered', not out['uncovered'])
        check('all inputs unchanged at completion', all(digest(ROOT / name) == h for name, h in frozen.items()))
        out['summary'] = {'actual_thirds': len(out['thirds']), 'required_thirds': 382,
                          'universe_fourths_per_third': 756,
                          'eligible_occurrences': sum(counts.values()),
                          'dispositions': dict(counts), 'uncovered_occurrences': len(out['uncovered']),
                          'historical_residual_occurrences': len(residuals_seen),
                          'screen_occurrences': len(screen_seen),
                          'all_thirds_fully_covered': all(r['eligible_fourths'] > 0 for r in out['thirds']),
                          'audits_bound': len(out['audit_bindings']), 'inputs_bound': len(frozen)}
    except Exception as exc:
        out['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
    out['program_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    save(TARGET, out)
    print(json.dumps(out.get('summary', {}), sort_keys=True))
    print(f"Failures: {len(out['failures'])}; uncovered: {len(out['uncovered'])}; full certificate: {TARGET}")
    if out['failures']:
        print(out['failures'][0])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
