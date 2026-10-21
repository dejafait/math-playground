"""Independent set/predicate replay of the new assembly, without producer imports.

Imports already audited rank/locus/row-count results, not their algorithms.
Writes the full occurrence checks and source bindings to disk.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent


def run():
    output = {'scope': 'Independent complete indexed assembly replay only',
              'thirds': [], 'checks': [], 'failures': []}

    def require(name, condition):
        output['checks'].append({'check': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)

    def digest(path):
        with path.open('rb') as stream:
            h = sha256()
            for part in iter(lambda: stream.read(1024 * 1024), b''):
                h.update(part)
        return h.hexdigest()

    def read(name):
        return json.loads((BASE / name).read_bytes())

    def pair(row):
        return (tuple(row['I']), tuple(row['K'])) if isinstance(row, dict) else tuple(map(tuple, row))

    def rows(record):
        return [pair(r) for r in record['rows']]

    try:
        cert = read('fixed-pair-exclusion-assembly.json')
        require('producer has no failures or uncovered records', cert['failures'] == cert['uncovered'] == [])
        require('producer code binding', cert['program_sha256'] == digest(BASE / 'fixed_pair_exclusion_assembly.py'))
        require('all frozen inputs bind', all(digest(ROOT / p) == h for p, h in cert['source_hashes'].items()))
        h = sorted({pow(8, i, 97) for i in range(16)})
        s = {1, 8, 12, 18, 22, 27, 33}
        require('independent subgroup and metadata', len(h) == 16 and cert['H'] == h and set(cert['S']) == s
                and all(pow(x, 16, 97) == 1 for x in h))
        # Generate four-sets first, rather than the producer's product of pairs.
        u = sorted((tuple(x for x in a if x in s), tuple(x for x in a if x not in s))
                   for a in combinations(h, 4) if len(set(a) & s) == 2)
        masks = [sum(1 << h.index(x) for x in i + k) for i, k in u]
        first = [((1, 8), (47, 50)), ((12, 18), (64, 70))]
        fm = [masks[u.index(a)] for a in first]
        valid = [i for i, m in enumerate(masks) if all((m & f).bit_count() <= 1 for f in fm)]
        disjoint = {i for i in valid if not masks[i] & (fm[0] | fm[1])}
        named = u.index(((1, 22), (75, 79)))
        t = [i for i in valid if i not in disjoint and i != named]
        require('independent exact support domains', len(u) == len(set(u)) == 756 and len(valid) == 382
                and len(disjoint) == 30 and len(t) == 351)
        require('complete ordered third output', [pair(r['third']) for r in cert['thirds']] == [u[i] for i in valid])
        historical = read('remaining-third-factor-filter.json')
        factors = read('residual-coordinate-factors.json')
        factor_meta = {r['third_index']: r for r in factors['thirds']}
        screen = read('inactive-coordinate-screen.json')
        screen_map = {(r['third_index'], r['fourth_index']): r for r in screen['records']}
        loci = read('active-rank19-complete-loci.json')
        lm = {tuple(r['historical_index']): r for r in loci['records']}
        r20 = read('rank20-selected-gates.json')
        rm = {tuple(r['historical_index']): r for r in r20['records']}
        completions = {}
        for label, source in [('L121_shortfall', 'intrinsic-survivor-full-rows.json'),
                              ('L123_shortfall', 'rank20-survivor-full-rows.json')]:
            completions[label] = {tuple(i) for p in read(source)['planes'] for i in p['historical_indices']}
        disposition_counts = Counter()
        total = 0
        for ei, (ui, meta) in enumerate(zip(valid, cert['thirds'])):
            n = t.index(ui) if ui in t else None
            path = BASE / meta['certificate']
            require('output shard hash', digest(path) == meta['sha256'])
            shard = read(meta['certificate'])
            require('shard third identity', shard['eligible_third_index'] == ei
                    and shard['historical_third_index'] == n and pair(shard['third']) == u[ui])
            expected_fourths = [j for j, m in enumerate(masks) if
                                all((m & old).bit_count() <= 1 for old in fm + [masks[ui]])]
            require('all and only eligible fourths, no duplicate',
                    [r['fourth_index'] for r in shard['cases']] == expected_fourths
                    and len(expected_fourths) == meta['eligible_fourths'])
            old = read(historical['thirds'][n]['certificate'])['cases'] if n is not None else None
            factor = ({r['fourth_index']: r for r in read(factor_meta[n]['certificate'])['cases']}
                      if n in factor_meta else {})
            evidence = []
            for r in shard['cases']:
                j = r['fourth_index']
                idx = (n, j)
                actual_rows = first + [u[ui], u[j]]
                reason = r['disposition']
                require('exact saved fourth labels', pair(r['fourth']) == u[j])
                require('exact all three intersections', r['intersections'] ==
                        [(masks[j] & a).bit_count() for a in fm + [masks[ui]]])
                valid_reason = False
                if reason == 'L112_third':
                    valid_reason = ui in disjoint
                elif reason == 'L113_third':
                    valid_reason = ui == named
                elif reason in ['L114_rank', 'L114_factor']:
                    valid_reason = old[j]['status'] == {'L114_rank': 'excluded_rank',
                                                        'L114_factor': 'excluded_label_1_factor'}[reason]
                else:
                    require('later inputs restricted to historical unresolved', old[j]['status'] == 'unresolved')
                    if reason == 'L116_factor':
                        valid_reason = factor[j]['status'] == 'excluded_coordinate_factor'
                    else:
                        require('later inputs restricted to factor failures', factor[j]['status'] == 'unresolved')
                        sr = screen_map[idx]
                        require('exact screen support binding', [pair(a) for a in sr['four_rows']] == actual_rows)
                        if reason == 'L118_activity':
                            valid_reason = sr['status'] == 'excluded_inactive_coordinate'
                        else:
                            require('later inputs restricted to activity failures', sr['status'] == 'screen_failure')
                            if reason == 'L112_exchanged_rows':
                                valid_reason = j in disjoint and 'L112_exchanged_rows' in sr['prior_exclusions']
                            elif reason == 'L119_named':
                                valid_reason = idx == (0, 320) and actual_rows == rows(read('first-active-residual-gates.json'))
                            elif reason in ['L120_locus', 'L121_shortfall']:
                                lr = lm[idx]
                                valid_reason = (sr['rank'] == 19 and rows(lr) == actual_rows
                                                and 'L112_exchanged_rows' not in sr['prior_exclusions']
                                                and idx != (0, 320))
                                valid_reason &= (lr['disposition'] == 'excluded_necessary_gates' if reason == 'L120_locus'
                                                 else lr['disposition'] == 'intrinsic_survivor' and idx in completions[reason])
                            elif reason == 'L123_shortfall':
                                valid_reason = (sr['rank'] == 20 and rows(rm[idx]) == actual_rows
                                                and idx in completions[reason])
                require('scoped exclusion at ' + str((ei, j)), valid_reason)
                evidence.append({'fourth_index': j, 'disposition': reason, 'scope_matches': valid_reason})
                disposition_counts[reason] += 1
            output['thirds'].append({'eligible_third_index': ei, 'historical_third_index': n,
                                     'third': u[ui], 'eligible_fourths': expected_fourths,
                                     'complete_scoped_checks': evidence})
            total += len(expected_fourths)
        require('exact complete dispositions', dict(disposition_counts) == cert['summary']['dispositions'])
        require('no gaps in independent domain count', total == cert['summary']['eligible_occurrences'] == 100764)
        require('all input hashes still unchanged', all(digest(ROOT / p) == h for p, h in cert['source_hashes'].items()))
        output['summary'] = {'actual_thirds': len(output['thirds']), 'required_thirds': 382,
                             'actual_eligible_occurrences': total, 'required_eligible_occurrences': 100764,
                             'dispositions': dict(disposition_counts), 'uncovered': 0}
    except Exception as exc:
        output['failures'].append({'type': type(exc).__name__, 'message': str(exc)})
    output['verifier_sha256'] = digest(Path(__file__))
    output['producer_certificate_sha256'] = digest(BASE / 'fixed-pair-exclusion-assembly.json')
    target = BASE / 'fixed-pair-exclusion-assembly-replay.json'
    target.write_text(json.dumps(output, separators=(',', ':')) + '\n')
    print(json.dumps(output.get('summary', {}), sort_keys=True))
    print(f"Failures: {len(output['failures'])}; full certificate: {target}")
    if output['failures']:
        print(output['failures'][0])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
