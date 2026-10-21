"""Check every saved cubic group by Horner evaluation and cross products.

No inverse-table grouping or candidate-recovery code from the search is used.
Checks all labels and all cubic memberships, not a sample or summary preview.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json


def main():
    source = Path(__file__).with_name("disjoint-d-pair-result.json")
    out = Path(__file__).with_name("disjoint-d-pair-verification.json")
    data = json.loads(source.read_text())
    p = 97
    hset = {x for x in range(1, p) if x**16 % p == 1}
    expected_choices = {(y, z) for y in combinations(sorted(hset - {1}), 2)
                        for z in combinations(sorted(hset - {1} - set(y)), 2)}
    seen_choices = set()
    histogram = Counter()
    case_records = []
    failures = []
    cubic_count = pair_count = 0
    example = None
    for case in data["complete_groups"]:
        ys, zs = tuple(case["Y"]), tuple(case["Z"])
        choice = (ys, zs)
        assert choice in expected_choices and choice not in seen_choices
        seen_choices.add(choice)
        outside = hset - {1} - set(ys) - set(zs)
        expected_cubics = set(combinations(sorted(outside), 3))
        seen_cubics, seen_keys = set(), set()
        large_count, checked_pairs = 0, 0
        for key, triples in case["groups"]:
            key = tuple(key)
            assert key not in seen_keys and all(0 < v < p for v in key)
            seen_keys.add(key)
            histogram[len(triples)] += 1
            for s in triples:
                s = tuple(s)
                assert s in expected_cubics and s not in seen_cubics
                seen_cubics.add(s)
                a, b, c = s
                coefficients = (1, -(a+b+c), a*b+a*c+b*c, -a*b*c)
                values = []
                for x in (*ys, *zs):
                    value = 0
                    for coefficient in coefficients:
                        value = (value*x + coefficient) % p
                    assert value != 0
                    values.append(value)
                assert (values[0] - key[0]*values[1]) % p == 0
                assert (values[2] - key[1]*values[3]) % p == 0
            if len(triples) >= 3:
                large_count += 1
                if example is None:
                    example = {"Y": ys, "Z": zs, "key": key, "triples": triples}
                for s, ss in combinations(triples, 2):
                    checked_pairs += 1
                    if not set(s) & set(ss):
                        failures.append({"Y": ys, "Z": zs, "key": key,
                                         "disjoint_pair": [s, ss]})
        assert seen_cubics == expected_cubics
        cubic_count += len(seen_cubics)
        pair_count += checked_pairs
        case_records.append({"Y": ys, "Z": zs, "cubics_verified": len(seen_cubics),
                             "groups_at_least_three": large_count,
                             "pairs_checked_in_large_groups": checked_pairs})
    assert seen_choices == expected_choices
    assert cubic_count == 1351350
    assert dict(sorted(histogram.items())) == {
        int(k): v for k, v in data["group_size_histogram"].items()}
    result = {"source": source.name, "complete_case_checks": case_records,
              "group_size_histogram": dict(sorted(histogram.items())),
              "first_large_group": example,
              "summary": {"normalized_label_choices": len(seen_choices),
                          "required_label_choices": 8190,
                          "cubic_memberships_verified": cubic_count,
                          "required_cubic_memberships": 1351350,
                          "pairs_checked_in_large_groups": pair_count,
                          "actual_disjoint_pairs": len(failures),
                          "required_for_pair": 1, "failures": failures,
                          "all_partition_and_ratio_checks_passed": True,
                          "proves_eleven": False}}
    out.write_text(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))
    print(f"actual disjoint pairs {len(failures)}; required for pair 1; certificate {out}")
    assert not failures


if __name__ == "__main__":
    main()
