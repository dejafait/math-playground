"""Exact finite Gilbert certificates; no block enumeration at q=107.

Run from the active notebook: python3 scripts/finite-packing/four_column_gilbert.py
Full exact integers and independent small-case evidence are saved beside this file.
"""
from collections import Counter
from itertools import combinations, product
from math import comb, factorial
from pathlib import Path
import json


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def partitions(n, length, largest=None):
    if n == 0:
        yield ()
    elif length:
        for first in range(min(n, n if largest is None else largest), 0, -1):
            for tail in partitions(n - first, length - 1, first):
                yield (first,) + tail


def placement_count(columns, profile):
    if len(profile) > columns:
        return 0
    denominator = factorial(columns - len(profile))
    for multiplicity in Counter(profile).values():
        denominator *= factorial(multiplicity)
    return factorial(columns) // denominator


def universe_count(columns, q, profile):
    result = placement_count(columns, profile)
    for size in profile:
        result *= choose(q, size)
    return result


def convolution(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return result


def row_counts(columns, q, weight, max_columns, a, profiles):
    """N[a,b,j] for every b and j=0,...,weight, with a fixed A."""
    output = {b: [0] * (weight + 1) for b in profiles}
    s = len(a)
    for u in product(range(min(q, weight) + 1), repeat=s):
        used = sum(u)
        positive = tuple(x for x in u if x)
        if used > weight or len(positive) > max_columns:
            continue
        remaining = weight - used
        for c in partitions(remaining, min(columns - s, max_columns - len(positive)), q):
            b = tuple(sorted(positive + c, reverse=True))
            if b not in output:
                continue
            outside = universe_count(columns - s, q, c)
            coefficients = [1]
            for size_a, size_b in zip(a, u):
                local = [choose(size_a, j) * choose(q - size_a, size_b - j)
                         for j in range(min(size_a, size_b) + 1)]
                coefficients = convolution(coefficients, local)
            for j, count in enumerate(coefficients):
                output[b][j] += outside * count
    return output


def ceil_ratio(numerator, denominator):
    assert denominator > 0
    return (numerator + denominator - 1) // denominator


def calculate(columns, q, weight, max_columns, conflict):
    profiles = list(partitions(weight, min(columns, max_columns), q))
    sizes = {p: universe_count(columns, q, p) for p in profiles}
    rows = {a: row_counts(columns, q, weight, max_columns, a, profiles)
            for a in profiles}
    neighborhoods = {a: {b: sum(rows[a][b][conflict:]) for b in profiles}
                     for a in profiles}
    degrees = {a: sum(neighborhoods[a].values()) for a in profiles}
    total = sum(sizes.values())
    maximum = max(degrees.values())
    return profiles, sizes, rows, neighborhoods, degrees, total, maximum


def direct_small_case(columns, q, weight, max_columns, conflict):
    """Independent actual point sets; check every vertex and every profile."""
    profiles, sizes, rows, neighborhoods, degrees, total, maximum = calculate(
        columns, q, weight, max_columns, conflict)
    actual = []
    for points in combinations(range(columns * q), weight):
        occupancy = Counter(p // q for p in points)
        if len(occupancy) <= max_columns:
            a = tuple(sorted(occupancy.values(), reverse=True))
            mask = sum(1 << p for p in points)
            actual.append((mask, a))
    actual_sizes = Counter(a for _, a in actual)
    failures = []
    full_vertex_evidence = []
    for mask, a in actual:
        direct = {b: [0] * (weight + 1) for b in profiles}
        for other_mask, b in actual:
            direct[b][(mask & other_mask).bit_count()] += 1
        if direct != rows[a]:
            failures.append({"mask": mask, "profile": a, "failure": "intersection histogram"})
        full_vertex_evidence.append({"mask": mask, "profile": list(a),
                                     "histograms": [direct[b] for b in profiles]})
    if dict(actual_sizes) != sizes or len(actual) != total:
        failures.append({"failure": "universe counts"})
    # Independently run an actual finite greedy selection for this small graph.
    remaining = list(actual)
    selected = []
    while remaining:
        mask, a = remaining[0]
        selected.append(mask)
        remaining = [(m, b) for m, b in remaining
                     if (mask & m).bit_count() < conflict]
    if len(selected) < ceil_ratio(total, maximum):
        failures.append({"failure": "greedy size"})
    for left, right in combinations(selected, 2):
        if (left & right).bit_count() >= conflict:
            failures.append({"failure": "selected compatibility", "left": left, "right": right})
    return {"parameters": {"columns": columns, "q": q, "weight": weight,
                           "max_columns": max_columns, "conflict": conflict},
            "profiles": [list(p) for p in profiles], "vertex_count": total,
            "ordered_pairs_checked": total ** 2, "maximum_closed_neighborhood": maximum,
            "gilbert_lower": ceil_ratio(total, maximum), "actual_greedy_size": len(selected),
            "selected_masks": selected, "every_vertex": full_vertex_evidence,
            "failures": failures}


def main():
    columns, q, weight, max_columns, conflict = 9, 107, 9, 4, 5
    baseline, benchmark = 107 ** 5, 19800269675
    profiles, sizes, rows, neighborhoods, degrees, total, maximum = calculate(
        columns, q, weight, max_columns, conflict)
    checks = []

    def check(name, passed):
        checks.append({"name": name, "passed": bool(passed)})

    check("exactly eighteen profiles", len(profiles) == 18)
    for a in profiles:
        for b in profiles:
            check(f"all intersection classes sum to universe {a}/{b}",
                  sum(rows[a][b]) == sizes[b])
            check(f"undirected conflict balance {a}/{b}",
                  sizes[a] * neighborhoods[a][b] == sizes[b] * neighborhoods[b][a])
        check(f"unique self at intersection nine {a}",
              all(rows[a][b][weight] == (1 if a == b else 0) for b in profiles))
        check(f"positive neighborhood {a}", degrees[a] >= neighborhoods[a][a] >= 1)
    union_lower = ceil_ratio(total, maximum)
    records = []
    for a in profiles:
        lower = ceil_ratio(sizes[a], neighborhoods[a][a])
        records.append({"profile": list(a), "size": sizes[a],
                        "intersection_counts_by_target_profile": [
                            {"target_profile": list(b), "by_intersection_0_to_9": rows[a][b],
                             "closed_neighborhood_contribution": neighborhoods[a][b]}
                            for b in profiles],
                        "union_closed_neighborhood": degrees[a],
                        "single_profile_closed_neighborhood": neighborhoods[a][a],
                        "single_profile_lower": lower, "baseline_plus_lower": baseline + lower,
                        "strictly_exceeds_benchmark": baseline + lower > benchmark})
    small_cases = [direct_small_case(*parameters) for parameters in
                   [(4, 2, 4, 3, 3), (4, 3, 5, 3, 3),
                    (3, 3, 4, 2, 2), (3, 2, 3, 2, 1), (3, 2, 3, 2, 3)]]
    for i, case in enumerate(small_cases):
        check(f"complete independent small case {i}", not case["failures"])
    best_added = max([union_lower] + [r["single_profile_lower"] for r in records])
    failures = [c["name"] for c in checks if not c["passed"]]
    certificate = {
        "parameters": {"columns": columns, "q": q, "weight": weight,
                       "max_columns": max_columns, "conflict_intersection": conflict},
        "baseline": baseline, "benchmark": benchmark, "required_added_to_exceed": benchmark - baseline + 1,
        "profiles": records,
        "union": {"size": total, "maximum_closed_neighborhood": maximum,
                  "maximizing_profiles": [list(a) for a in profiles if degrees[a] == maximum],
                  "lower": union_lower, "baseline_plus_lower": baseline + union_lower,
                  "strictly_exceeds_benchmark": baseline + union_lower > benchmark},
        "best_alternative": {"added_lower": best_added, "total_lower": baseline + best_added,
                             "strictly_exceeds_benchmark": baseline + best_added > benchmark,
                             "shortfall_to_strict_target": benchmark + 1 - (baseline + best_added)},
        "checks": checks, "failures": failures,
        "small_cases": small_cases,
    }
    path = Path(__file__).with_name("four-column-gilbert-results.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Profiles: {len(profiles)}; exact checks: {len(checks)}; failures: {failures}")
    print(f"Union: size={total}, maximum closed neighborhood={maximum}, lower={union_lower}")
    print(f"Best alternative: added={best_added}, total={baseline + best_added}")
    print(f"Required: added>={benchmark - baseline + 1}, total>={benchmark + 1}")
    print(f"Small cases: {sum(c['vertex_count'] for c in small_cases)} vertices, "
          f"{sum(c['ordered_pairs_checked'] for c in small_cases)} ordered pairs; "
          f"failures={sum(len(c['failures']) for c in small_cases)}")
    print(f"Full certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
