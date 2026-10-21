"""Audit full saved verification records and replay identity for L049.

Run after disjoint_d_pair.py and verify_disjoint_d_pair.py. The latter
checks every membership and pair; this checks all emitted per-case records,
metadata and totals against the complete grouping certificate.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib
import json
import math


def main():
    base = Path(__file__).resolve().parent
    root = base.parent.parent
    source = base / 'disjoint-d-pair-result.json'
    verification = base / 'disjoint-d-pair-verification.json'
    data = json.loads(source.read_text())
    checked = json.loads(verification.read_text())
    before = json.loads((root / 'drafts/2026-10-09-disjoint-d-audit-before.json').read_text())
    hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in (source, verification)}
    assert hashes == before, 'Replay changed a saved certificate'
    assert __debug__, 'Assertions must be enabled'
    h = data['scope']['H']
    assert len(h) == len(set(h)) == 16
    assert all(0 < x < 97 and pow(x, 16, 97) == 1 for x in h)
    # Sixteen distinct roots exhaust X^16-1; explicit cyclic generator check.
    generator = next(x for x in h if pow(x, 8, 97) != 1)
    assert {pow(generator, j, 97) for j in range(16)} == set(h)
    assert data['scope'] == dict(prime=97, H=h, h=1,
        d_ignored_overapproximation=True, cubics_per_pair_choice=165,
        required_distinct_cubics=3)
    expected = {(y,z) for y in combinations(sorted(set(h)-{1}),2)
                for z in combinations(sorted(set(h)-{1}-set(y)),2)}
    assert len(expected) == math.comb(15,2)*math.comb(13,2) == 8190
    records = checked['complete_case_checks']
    assert len(records) == len(data['complete_groups']) == len(expected)
    histogram = Counter()
    memberships = pairs = large = 0
    seen = set()
    for case, record in zip(data['complete_groups'], records):
        y,z = case['Y'],case['Z']
        choice = (tuple(y),tuple(z))
        assert choice in expected and choice not in seen
        seen.add(choice)
        sizes = [len(triples) for key,triples in case['groups']]
        assert all(n > 0 for n in sizes)
        n = sum(sizes)
        assert n == math.comb(11,3) == 165
        count = sum(s >= 3 for s in sizes)
        pc = sum(math.comb(s,2) for s in sizes if s >= 3)
        assert record == dict(Y=y,Z=z,cubics_verified=n,
            groups_at_least_three=count,pairs_checked_in_large_groups=pc)
        histogram.update(sizes)
        memberships += n
        large += count
        pairs += pc
    assert seen == expected
    assert dict(histogram) == {1:1314906,2:4992,3:1680,4:4830,5:420}
    assert data['group_size_histogram'] == checked['group_size_histogram'] == {
        str(k):v for k,v in sorted(histogram.items())}
    assert data['statistics'] == dict(y_z_pair_choices=8190,
        split_cubics_grouped=memberships,disjoint_pairs_tested=0,
        groups_at_least_three=large)
    assert checked['source'] == source.name
    assert checked['summary'] == dict(normalized_label_choices=8190,
        required_label_choices=8190,cubic_memberships_verified=memberships,
        required_cubic_memberships=1351350,pairs_checked_in_large_groups=pairs,
        actual_disjoint_pairs=0,required_for_pair=1,failures=[],
        all_partition_and_ratio_checks_passed=True,proves_eleven=False)
    assert (memberships,large,pairs) == (1351350,6930,38220)
    out = base / 'disjoint-d-critical-audit.json'
    result = dict(certificate_sha256=hashes, replay_matches_initial_bytes=True,
        producer_sha256=hashlib.sha256((base/'disjoint_d_pair.py').read_bytes()).hexdigest(),
        verifier_sha256=hashlib.sha256((base/'verify_disjoint_d_pair.py').read_bytes()).hexdigest(),
        H=h, generator=generator,
        summary=dict(complete_records_checked=len(records),required_records=8190,
            cubic_memberships=memberships,large_groups=large,checked_pairs=pairs,
            actual_disjoint_pairs=0,required_for_pair=1,failures=[],
            record_consistency_passed=True,proves_eleven=False))
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],sort_keys=True))
    print(f'Full certificate: {out}')


if __name__ == '__main__':
    main()
