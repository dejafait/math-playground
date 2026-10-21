"""Read every W-intersection record; validate stored scope and moment evidence.

This supplements, rather than replaces, the producer's exhaustive independent
all-mu/all-support maximizer checks. It does not validate every RREF rejection.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).parent
v = json.loads((ROOT / 'w-intersection-count-result.json').read_text())
assert len(v['cases']) == 240 and len(v['bases']) == 192
assert len(v['verifications']) == 240
hist, outside_hist, full_hist = Counter(), Counter(), Counter()
checked = 0
supports = set(combinations(v['scope']['H'], 4))
for base in v['bases']:
    records = base['support_classification']
    assert len(records) == 1820 and {tuple(x['K']) for x in records} == supports


def moments(word):
    return [sum(int(x)**j*w for x, w in word.items()) % 97 for j in range(1, 9)]


for i, case in enumerate(v['cases']):
    count = case['count']
    assert [c['r'] for c in count['rational_r_cases']] == list(range(2, 97))
    assert max(len(c['mus']) for c in count['rational_r_cases']) == count['maximum'] == 3
    assert len(count['nonprime_r_mus']) <= 3
    outside_hist[len(count['nonprime_r_mus'])] += 1
    for row in count['rational_r_cases']:
        assert row['mus'] == sorted(set(row['mus']))
        assert set(count['nonprime_r_mus']) <= set(row['mus'])
        hist[len(row['mus'])] += 1
    check = v['verifications'][i]
    assert check['case_index'] == i
    a = check['verification']
    assert a['exact_set_match'] and a['all_eight_pencil_moments']
    for t, word in zip(a['gamma'], a['original_errors']):
        assert all(word.values())
        assert moments(word) == [(x+t*y) % 97 for x, y in zip(a['intercept'], a['slope'])]
    for row in a['complete_admitted_records']:
        assert moments(row['actual_error']) == [(x+row['T']*y) % 97
                                               for x, y in zip(a['intercept'], a['slope'])]
        assert row['T'] not in a['gamma'] and row['E'] != 0
        assert row['full_weight'] == all(row['omega'])
        full_hist[str(row['full_weight'])] += 1
        checked += 1
    assert sorted({row['mu'] for row in a['complete_admitted_records']}) == count['first_maximizer']['mus']

result = {'complete_support_partitions_checked': 192,
          'complete_r_count_sets_checked': 22800,
          'complete_verification_records_checked': 240,
          'admitted_moment_records_checked': checked,
          'rational_count_histogram': dict(hist),
          'nonprime_count_histogram': dict(outside_hist),
          'full_weight_record_histogram': dict(full_hist), 'failures': []}
out = ROOT / 'w-intersection-count-integrity.json'
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, sort_keys=True))
print(f'actual maximum {max(hist)}; required refutation count 12; certificate {out}')
