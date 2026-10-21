"""Independently replay complete three-same-tag rejection evidence.

Checks the complete cubic partition, triple and recovery-case coverage.
Verifies recovery equations by cross multiplication, not producer inverses.
"""
from itertools import combinations, permutations
from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).parent
P = 97
H = tuple(x for x in range(1, P) if pow(x, 16, P) == 1)


def value(s, x):
    a, b, c = s
    return (x-a)*(x-b)*(x-c) % P


def key(z, ss, y, d, w):
    return z, tuple(tuple(s) for s in ss), y, d, tuple(w)


def main():
    data = json.loads((ROOT/'three-singleton-result.json').read_text())
    assert data['complete'] and data['witness'] is None and not data['failures']
    tests = {}
    rejection_counts = Counter()
    for row in data['recovery_tests']:
        k = key(row['z'], row['S'], row['y'], row['d'], row['W'])
        assert k not in tests
        tests[k] = row
        rejection_counts[row['rejection']] += 1
    expected_tests, expected_triples = set(), set()
    cubics_checked = 0
    assert [row['z'] for row in data['cubic_groups']] == list(H[1:])
    for case in data['cubic_groups']:
        z = case['z']
        available = [x for x in H if x not in (1, z)]
        expected_cubics = set(combinations(available, 3))
        seen, ratios = set(), set()
        for group in case['groups']:
            ratio = group['ratio']
            assert ratio not in ratios and 0 < ratio < P
            ratios.add(ratio)
            members = [tuple(s) for s in group['cubics']]
            for s in members:
                assert s in expected_cubics and s not in seen
                assert (value(s, z)-ratio*value(s, 1)) % P == 0
                seen.add(s)
            for ss in combinations(members, 3):
                union = set().union(*map(set, ss))
                if len(union) != 9 or len(members) < 4:
                    continue
                expected_triples.add((z, ratio, ss))
                complement = [x for x in available if x not in union]
                for w in members:
                    if w in ss:
                        continue  # W=S forces mu=-1, excluded independently.
                    for y, d in permutations(complement, 2):
                        if y in w or d in w:
                            continue
                        k = key(z, ss, y, d, w)
                        assert k not in expected_tests
                        expected_tests.add(k)
                        row = tests[k]
                        assert row['ratio'] == ratio
                        us, mus = row['u'], row['mu']
                        assert len(us) == len(mus) == 3
                        for s, u, mu in zip(ss, us, mus):
                            assert 0 < u < P and 0 < mu < P
                            assert (u*value(w, 1)-value(s, 1)) % P == 0
                            assert (mu*value(s, y)+u*value(w, y)) % P == 0
                        if 96 in mus or len(set(mus)) != 3:
                            assert row['rejection'] == 'excluded_or_colliding_scalar'
                            assert 'r' not in row
                            continue
                        rs = row['r']
                        assert len(rs) == 3 and all(0 <= r < P for r in rs)
                        for s, u, mu, r in zip(ss, us, mus, rs):
                            assert ((1-(1+mu)*r)*value(s, d)-u*value(w, d)) % P == 0
                        assert len(set(rs)) != 1 or rs[0] in (0, 1)
                        assert row['rejection'] == 'inconsistent_or_ungated_r'
        assert seen == expected_cubics and len(seen) == 364
        cubics_checked += len(seen)
    actual_triples = {(row['z'], row['ratio'], tuple(tuple(s) for s in row['S']))
                      for row in data['disjoint_triples']}
    assert len(actual_triples) == len(data['disjoint_triples'])
    assert actual_triples == expected_triples
    assert set(tests) == expected_tests
    assert data['statistics']['cubics'] == cubics_checked == 5460
    assert data['statistics']['disjoint_triples'] == len(expected_triples) == 704
    assert data['statistics']['scalar_tests'] == len(expected_tests) == 28688
    out = ROOT/'three-singleton-verification.json'
    result = dict(complete=True, cubics_checked=cubics_checked, required_cubics=5460,
                  disjoint_triples_checked=len(expected_triples), required_triples=704,
                  recovery_tests_checked=len(expected_tests), required_recovery_tests=28688,
                  rejection_counts=dict(rejection_counts), actual_common_gated_r=0,
                  required_common_gated_r_for_witness=1, failures=[])
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(f'cubics {cubics_checked}/5460; disjoint triples {len(expected_triples)}/704; recovery tests {len(expected_tests)}/28688')
    print(f'common gated r 0; required 1; failures 0; certificate {out}')


if __name__ == '__main__':
    main()
