"""Replay the original full census and independently count all anchor directions.

Preserves the original certificates. Saves all per-anchor histograms, point/support
data, complete producer replay and a summary with actual/required bounds/failures.
Only the approved five-coordinate finite configuration is enumerated.
"""
from collections import Counter
from itertools import combinations
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
P = 97
REPORT = HERE / "five-coordinate-complete-census-audit.json"
REPLAY = HERE / "five-coordinate-census-replay.jsonl"
ANCHORS = HERE / "five-coordinate-anchor-census.jsonl"
POINTS = HERE / "five-coordinate-audit-points.jsonl"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def product(values):
    answer = 1
    for value in values:
        answer = answer * value % P
    return answer


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_records(path):
    return [json.loads(line) for line in path.read_text().splitlines()]


def run(report):
    saved = read_records(HERE / "five-coordinate-orbits.jsonl")
    require(len(saved) == 273, "saved orbit record count")
    # Enumerate roots directly, independently of the producer's cyclic recurrence.
    roots = tuple(x for x in range(1, P) if pow(x, 16, P) == 1)
    cyclic = tuple(pow(8, i, P) for i in range(16))
    require(len(roots) == 16 and set(roots) == set(cyclic), "domain mismatch")
    expected_sets = {frozenset(a) for a in combinations(roots, 5)}
    covered = set()
    inputs = ["273"]
    configurations = []
    masks = set()
    for record in saved:
        mask = record["mask"]
        a = tuple(record["A"])
        require(mask not in masks, "duplicate representative")
        masks.add(mask)
        require(mask.bit_count() == 5, "mask cardinality")
        require(a == tuple(cyclic[i] for i in range(16) if mask & (1 << i)), "mask/labels")
        orbit = {frozenset(h * x % P for x in a) for h in roots}
        require(len(orbit) == 16 and not covered.intersection(orbit), "orbit overlap")
        covered.update(orbit)
        complement = tuple(x for x in roots if x not in a)
        all_roots_at_a = tuple(product(x - y for y in complement) for x in a)
        points = []
        supports = list(combinations(complement, 4))
        for support in supports:
            # Product of eleven roots divided by the selected four factors.
            values = tuple(numerator * pow(product(x - k for k in support), -1, P) % P
                           for x, numerator in zip(a, all_roots_at_a))
            direct = tuple(product(x - y for y in complement if y not in support) for x in a)
            require(values == direct and all(values), "point formula discrepancy")
            points.append(tuple(x * pow(values[0], -1, P) % P for x in values))
        require(len(points) == 330 and len(set(points)) == 330, "point distinctness")
        configurations.append({"mask": mask, "A": a, "supports": supports, "points": points})
        inputs.append(f"{mask} 330")
        inputs.extend(" ".join(map(str, point)) for point in points)
    require(covered == expected_sets and len(covered) == 4368, "incomplete five-set coverage")
    POINTS.write_text("".join(json.dumps(row, separators=(",", ":")) + "\n" for row in configurations))
    with tempfile.TemporaryDirectory(prefix="five-census-audit-") as build:
        original = Path(build) / "original"
        independent = Path(build) / "anchor"
        for source, executable in (("five_coordinate_lines.cpp", original),
                                   ("five_coordinate_anchor_census.cpp", independent)):
            subprocess.run(["c++", "-O3", "-std=c++17", str(HERE / source), "-o", str(executable)], check=True)
        with REPLAY.open("w") as output:
            subprocess.run([str(original)], stdout=output, check=True)
        with ANCHORS.open("w") as output:
            subprocess.run([str(independent)], input="\n".join(inputs) + "\n", text=True,
                           stdout=output, check=True)
    replay = read_records(REPLAY)
    anchors = read_records(ANCHORS)
    require(replay == saved, "complete producer replay differs from saved records")
    require(len(anchors) == 273, "anchor configuration count")
    orbit_results = []
    for old, independent, configuration in zip(replay, anchors, configurations):
        mask = old["mask"]
        require(independent["mask"] == configuration["mask"] == mask, "configuration order")
        require(len(independent["anchors"]) == 330, "anchor coverage")
        total = Counter()
        for local in independent["anchors"]:
            local = {int(m): count for m, count in local.items()}
            require(all(m >= 2 and count > 0 for m, count in local.items()), "local sizes")
            require(sum((m - 1) * count for m, count in local.items()) == 329, "anchor neighbors")
            total.update(local)
        require(all(count % m == 0 for m, count in total.items()), "line anchor multiplicity")
        histogram = {str(m): count // m for m, count in sorted(total.items())}
        require(histogram == independent["line_size_histogram"] == old["line_size_histogram"],
                f"complete histogram mismatch for mask {mask}")
        require(sum(histogram.values()) == old["lines"], "line total")
        require(sum(int(m) * (int(m) - 1) // 2 * count for m, count in histogram.items()) == 54285,
                "pair total")
        maximum = max(map(int, histogram))
        require(maximum == independent["maximum_external_points"] == old["maximum_external_points"],
                "maximum mismatch")
        require(independent["directed_differences"] == 108570, "directed census total")
        # Membership check is supplementary, not the source of the upper bound.
        by_support = dict(zip(configuration["supports"], configuration["points"]))
        listed = {tuple(sorted(s)) for s in old["maximum_line_supports"]}
        require(len(listed) == maximum, "stored line repeated supports")
        p, q = [by_support[s] for s in sorted(listed)[:2]]
        pivot = next(i for i in range(1, 5) if p[i] != q[i])
        inverse = pow((q[pivot] - p[pivot]) % P, -1, P)
        actual = set()
        for support, point in by_support.items():
            t = (point[pivot] - p[pivot]) * inverse % P
            if all((point[i] - p[i] - t * (q[i] - p[i])) % P == 0 for i in range(5)):
                actual.add(support)
        require(actual == listed, "stored line membership mismatch")
        orbit_results.append({"mask": mask, "maximum": maximum, "histogram": histogram,
                              "full_anchor_census_match": True, "maximal_line_membership_match": True})
    maximum = max(row["maximum"] for row in orbit_results)
    report.update({"status": "PASS", "five_sets": len(covered), "orbits": len(anchors),
                   "points_per_configuration": 330, "anchors_checked": 273 * 330,
                   "point_pairs_replayed": 273 * 54285,
                   "directed_differences_independently_counted": 273 * 108570,
                   "actual_maximum": maximum,
                   "orbit_maximum_histogram": dict(sorted(Counter(row["maximum"] for row in orbit_results).items())),
                   "required_maximum_for_twelve_additional": 10,
                   "implied_total_bad_bound": 5 + maximum,
                   "implied_additional_bound_after_three_base_parameters": 2 + maximum,
                   "required_additional_bound": 12, "orbit_results": orbit_results,
                   "complete_original_replay_identical": True,
                   "complete_histograms_match_all_orbits": True,
                   "all_nonzero_point_coordinates_and_distinctness_checked": True,
                   "complete_disjoint_multiplicative_orbit_coverage": True,
                   "artifacts": {path.name: digest(path) for path in (REPLAY, ANCHORS, POINTS)},
                   "sources": {name: digest(HERE / name) for name in
                               ("five_coordinate_lines.cpp", "five_coordinate_anchor_census.cpp",
                                "verify_five_coordinate_census.py", "five-coordinate-orbits.jsonl")}})
    require(maximum <= 10, "required upper-bound threshold failed")


def main():
    report = {"status": "INCOMPLETE", "failures": [],
              "scope": "Complete fixed-H five-coordinate configuration bound, not arbitrary triangle extraction."}
    try:
        run(report)
    except Exception as error:
        report["status"] = "FAIL"
        report["failures"].append(f"{type(error).__name__}: {error}")
        REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        print(f"FAIL: {report['failures']}; certificate: {REPORT.relative_to(HERE.parent.parent)}")
        raise
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"PASS: {report['orbits']} orbits cover {report['five_sets']} five-sets; "
          f"{report['point_pairs_replayed']} producer pairs and "
          f"{report['directed_differences_independently_counted']} independent directed differences.")
    print(f"Actual/required M upper bound: {report['actual_maximum']}/10; "
          f"total bad bound {report['implied_total_bad_bound']}; additional bound "
          f"{report['implied_additional_bound_after_three_base_parameters']}/12; failures: 0.")
    print("Full evidence: " + ", ".join(str(path.relative_to(HERE.parent.parent))
                                       for path in (REPORT, REPLAY, ANCHORS, POINTS)))


if __name__ == "__main__":
    main()
