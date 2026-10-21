"""Validate saved selections and independently replay every reported pair-bearing assignment.

The unreported assignments are not independently re-enumerated. No uniform
negative conclusion is supported by this bounded search or this verifier.
"""
import csv
import hashlib
import json
from pathlib import Path
from verify_three_shared_pairs_join import verify

ROOT = Path(__file__).resolve().parent
PREFIX = 'three-shared-pairs-distributed-'


def main():
    summary = json.loads((ROOT/(PREFIX+'prefix.json')).read_text())
    selection_path = ROOT/(PREFIX+'selections.csv')
    H = [x for x in range(1, 97) if pow(x, 16, 97) == 1]
    selections, seen = [], set()
    roles = [[0]*16 for _ in range(3)]
    for ordinal, row in enumerate(csv.reader(selection_path.open()), 1):
        values = list(map(int, row))
        assert len(values) == 10 and values[0] == ordinal
        labels = tuple(values[1:])
        assert len(set(labels)) == 9 and all(x in H for x in labels)
        assert all(labels[i] < labels[i+1] for i in (3, 5, 7))
        assert labels not in seen
        seen.add(labels)
        selections.append(labels)
        for t in range(3):
            roles[t][H.index(labels[t])] += 1
    assert len(selections) == summary['assignments'] == 250000
    assert summary['support_tests'] == 231*len(selections)
    counts = json.loads((ROOT/(PREFIX+'role-counts.json')).read_text())
    assert counts == {'H': H, 'shared_role_counts': roles}
    assert all(all(n > 0 for n in role) for role in roles)
    reports, pair_counts, bearing = [], [0]*3, [0]*3
    reported_ordinals = set()
    for line in (ROOT/(PREFIX+'partials.jsonl')).open():
        saved = json.loads(line)
        ordinal = saved['ordinal']
        assert ordinal not in reported_ordinals
        reported_ordinals.add(ordinal)
        labels = selections[ordinal-1]
        assert labels == tuple([saved[k] for k in ('a', 'b', 'c')]+saved['Y']+saved['Z']+saved['W'])
        replay_input = {**saved, 'rows': saved['gated_rows'], 'pairs': saved['pair_indices']}
        result = verify(Path(f'{PREFIX}partials.jsonl:ordinal-{ordinal}'), replay_input)
        result['ordinal'] = ordinal
        assert result['support_tests'] == 231
        assert [sum(r['tag'] == t for r in result['rows']) for t in range(3)] == saved['rows']
        local_counts = [len(x) for x in result['pairs']]
        assert local_counts == saved['pairs'] and any(local_counts)
        for t, n in enumerate(local_counts):
            pair_counts[t] += n
            bearing[t] += bool(n)
        reports.append(result)
    assert pair_counts == summary['pair_counts']
    assert bearing == summary['pair_bearing_assignments']
    best = json.loads((ROOT/(PREFIX+'best.json')).read_text())
    best_report = verify(ROOT/(PREFIX+'best.json'))
    assert best['ordinal'] in reported_ordinals
    # The present run reaches no common-weight join; check the exact zero
    # fields, not merely the producer's vacuous moment-failure counter.
    for key in ('two_tag_weight_joins', 'three_tag_weight_joins', 'distinct_scalar_joins',
                'linear_joins', 'full_joins', 'moment_failures'):
        assert summary[key] == 0
    assert not summary['candidate_found']
    assert all(not r['three_tag_weight_joins'] and not r['linear_distinct_joins'] for r in reports)
    missing_full_pair_replays = [{'ordinal': r['ordinal'], 'tag': p['tag'], 'rows': p['rows']}
                                 for r in reports for p in r['local_pair_replays'] if p['witness'] is None]
    aggregate = {
        'selections_checked': len(selections), 'unique_actual_assignments': len(seen),
        'selection_sha256': hashlib.sha256(selection_path.read_bytes()).hexdigest(),
        'role_counts': roles,
        'pair_bearing_assignments_replayed': len(reports),
        'support_tests_replayed': sum(r['support_tests'] for r in reports),
        'rows_replayed': sum(len(r['rows']) for r in reports),
        'pair_counts_replayed': pair_counts,
        'pair_bearing_role_counts_replayed': bearing,
        'full_local_pairs_replayed': sum(p['witness'] is not None for r in reports for p in r['local_pair_replays']),
        'missing_full_pair_replays': missing_full_pair_replays,
        'three_tag_weight_joins_replayed': sum(len(r['three_tag_weight_joins']) for r in reports),
        'witness_threshold': 1, 'six_row_moments_checked': 0,
        'failures': [],
    }
    report = {'scope': 'All selections validated; complete row/pair replay only at reported pair-bearing assignments and best. Remaining sampled negatives not independently replayed; no exclusion.',
              'aggregate': aggregate, 'pair_bearing_replays': reports, 'best_replay': best_report}
    output = ROOT/(PREFIX+'verification.json')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(f"Selections {len(selections)}/250000 unique; complete replay {len(reports)} pair-bearing assignments, {aggregate['support_tests_replayed']} support tests, {aggregate['rows_replayed']} rows.")
    print(f"Pairs {pair_counts}; full local pair replays {aggregate['full_local_pairs_replayed']}/{sum(pair_counts)}; missing {len(missing_full_pair_replays)}. Six-row joins 0/required 1; six-row moments checked 0. Failures 0.")
    print(f"Certificate: {output.relative_to(ROOT.parent.parent)}")


if __name__ == '__main__':
    main()
