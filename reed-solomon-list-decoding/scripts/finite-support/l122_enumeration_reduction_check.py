"""Exact small-field checks of L122; deliberately does not count full H.

Run from the active notebook. The certificate retains every small-field
line occupancy and the independent brute-force disjoint-triple line counts.
Only a bounded summary is printed. No external packages or network access.
"""

from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
import json


def fall3(n):
    return n * (n - 1) * (n - 2)


def subgroup(p, n):
    for h in range(1, p):
        values = [pow(h, j, p) for j in range(n)]
        if pow(h, n, p) == 1 and len(set(values)) == n:
            return h, sorted(values)
    raise ValueError((p, n))


def cosets(p, H):
    unseen = set(range(1, p))
    parts = []
    while unseen:
        u = min(unseen)
        part = sorted(u * h % p for h in H)
        assert len(set(part)) == len(H)
        assert set(part) <= unseen
        parts.append((u, part))
        unseen.difference_update(part)
    return parts


def check_case(p, n):
    h, H = subgroup(p, n)
    pairs = list(combinations(H, 2))
    points = [((a + b) % p, a * b % p) for a, b in pairs]
    assert len(set(points)) == len(pairs)
    parts = cosets(p, H)
    vertical = [0] * p
    hist = [[0] * p for _ in range(p)]
    endpoints = [[[] for _ in range(p)] for _ in range(p)]
    for pair, (s, t) in zip(pairs, points):
        vertical[s] += 1
        for u in range(p):
            v = (t - u * s) % p
            hist[u][v] += 1
            endpoints[u][v].extend(pair)

    # Test the matching/star cases on every affine line, not just rich ones.
    for u in range(p):
        for v in range(p):
            if v == -u * u % p:
                assert hist[u][v] == (n - 1 if u in H else 0)
                for a, b in pairs:
                    if (a * b - u * (a + b)) % p == v:
                        assert u in (a, b)
            else:
                assert len(set(endpoints[u][v])) == len(endpoints[u][v])
    for s in range(p):
        line_pairs = [pair for pair, point in zip(pairs, points) if point[0] == s]
        flat = [x for pair in line_pairs for x in pair]
        assert len(set(flat)) == len(flat)

    # Independently enumerate pair triples, with integer cross-products and
    # a six-endpoint set test. Multiply unordered triples by 6 at the end.
    brute_lines = Counter()
    collinear = 0
    for i, j, k in combinations(range(len(pairs)), 3):
        s1, t1 = points[i]
        s2, t2 = points[j]
        s3, t3 = points[k]
        if ((s2 - s1) * (t3 - t1) - (s3 - s1) * (t2 - t1)) % p:
            continue
        collinear += 6
        if len(set(pairs[i] + pairs[j] + pairs[k])) != 6:
            continue
        if s1 == s2:
            key = ("vertical", s1)
        else:
            u = (t2 - t1) * pow(s2 - s1, -1, p) % p
            key = ("nonvertical", u, (t1 - u * s1) % p)
        brute_lines[key] += 6

    # Check complete per-line multiplicities against brute force.
    expected_lines = {}
    for s, r in enumerate(vertical):
        key = ("vertical", s)
        expected_lines[key] = fall3(r)
    for u in range(p):
        for v, r in enumerate(hist[u]):
            key = ("nonvertical", u, v)
            expected_lines[key] = 0 if v == -u * u % p else fall3(r)
    assert all(brute_lines[key] == count for key, count in expected_lines.items())
    assert set(brute_lines) <= set(expected_lines)

    # Test the actual orbit transport for every h, intercept and slope rep.
    for u, _ in parts:
        for scale in H:
            for v in range(p):
                assert hist[u][v] == hist[scale * u % p][scale * scale * v % p]
    vertical_count = sum(map(fall3, vertical))
    horizontal_count = sum(map(fall3, hist[0]))
    rep_count = sum(
        fall3(hist[u][v])
        for u, _ in parts
        for v in range(p)
        if v != -u * u % p
    )
    reduced = vertical_count + horizontal_count + n * rep_count
    brute = sum(brute_lines.values())
    assert reduced == brute
    assert vertical[0] == n // 2
    assert horizontal_count == n // 2 * (fall3(n // 2 - 1) + fall3(n // 2))
    assert collinear - brute == n * fall3(n - 1)
    N = len(pairs)
    first = sum(vertical) + sum(map(sum, hist))
    second = sum(r * r for r in vertical) + sum(r * r for row in hist for r in row)
    assert first == (p + 1) * N
    assert second == N * N + p * N
    return {
        "p": p, "n": n, "generator": h, "H": H,
        "pairs": pairs, "points": points, "cosets": parts,
        "vertical_occupancies": vertical, "nonvertical_occupancies": hist,
        "brute_ordered_disjoint_triples_by_nonzero_line": [
            [list(key), value] for key, value in sorted(brute_lines.items())
        ],
        "vertical_ordered": vertical_count, "horizontal_ordered": horizontal_count,
        "representative_ordered": rep_count, "orbit_weight": n,
        "formula_ordered": reduced, "brute_ordered": brute,
        "all_collinear_ordered": collinear,
        "excluded_shared_endpoint_ordered": collinear - brute,
        "first_moment_actual": first, "first_moment_required": (p + 1) * N,
        "second_moment_actual": second, "second_moment_required": N * N + p * N,
        "unordered_triples_examined": comb(N, 3), "failures": [],
    }


def full_instance_resources():
    p, n = 65537, 1024
    h = pow(3, 64, p)
    H = sorted(pow(h, i, p) for i in range(n))
    assert pow(h, n, p) == 1 and pow(h, n // 2, p) == p - 1
    assert len(set(H)) == n
    parts = cosets(p, H)
    assert len(parts) == 64 and parts[0][0] == 1
    N = comb(n, 2)
    return {
        "p": p, "n": n, "generator": h, "H": H, "cosets": parts,
        "pair_count": N, "slope_representatives": len(parts),
        "pair_bin_updates_actual": (len(parts) + 2) * N,
        "pair_bin_updates_required_upper": 35_000_000,
        "histogram_bins_scanned": (len(parts) + 2) * p,
        "packed_arrays_bytes": {
            "two_pair_coordinate_uint32_arrays": 8 * N,
            "one_uint32_histogram": 4 * p,
            "one_byte_coset_marks": p,
            "H_and_representatives_uint32": 4 * (n + len(parts)),
        },
        "vertical_antipodal_ordered": fall3(n // 2),
        "horizontal_ordered": n // 2 * (fall3(n // 2 - 1) + fall3(n // 2)),
        "maximum_target_ordered_strict_upper": 2 ** 57,
        "all_distinct_pair_ordered_upper": fall3(N),
        "full_count_run": False, "failures": [],
    }


def main():
    cases = [check_case(p, n) for p, n in [(17, 8), (17, 16), (41, 8), (97, 16)]]
    resources = full_instance_resources()
    assert resources["pair_bin_updates_actual"] < resources["pair_bin_updates_required_upper"]
    assert resources["all_distinct_pair_ordered_upper"] < resources["maximum_target_ordered_strict_upper"]
    assert sum(resources["packed_arrays_bytes"].values()) < 5_000_000
    result = {"lemma": "L122", "cases": cases, "full_instance_resources": resources,
              "failures": [], "scope": "reduction checks only; no full-H count or RS safety test"}
    path = Path(__file__).with_name("l122-enumeration-reduction-check.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "cases": [{"p": c["p"], "n": c["n"], "formula": c["formula_ordered"],
                   "brute": c["brute_ordered"], "failures": c["failures"]} for c in cases],
        "pair_bin_updates": resources["pair_bin_updates_actual"],
        "required_upper": resources["pair_bin_updates_required_upper"],
        "packed_arrays_bytes": sum(resources["packed_arrays_bytes"].values()),
        "failures": [], "certificate": str(path), "full_count_run": False,
    }))


if __name__ == "__main__":
    main()
