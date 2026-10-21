"""Independent exact reconstruction of L046; no search completeness claim."""

import json
from itertools import permutations
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def reconstruct(columns):
    points = [[c, x] for c, values in enumerate(columns) for x in values]
    terms = [[x, x**2, x**3, c*x] for c, x in points]
    raw = [sum(row[j] for row in terms) for j in range(4)]
    return {
        "points": sorted(points),
        "column_sizes": [len(values) for values in columns],
        "profile": sorted((len(v) for v in columns if v), reverse=True),
        "terms": terms,
        "raw_totals": raw,
        "syndrome": [n % 107 for n in raw],
        "quotients": [n // 107 for n in raw],
    }


def main():
    source = json.loads((HERE / "mixed-moment-collision-results.json").read_text())
    witness = source["witness"]
    # Reconstruct from the displayed column descriptions, not source functions.
    left = reconstruct([[0, 1, 2], [1, 10], [0, 10], [2, 10]] + [[]]*5)
    right = reconstruct([[0, 1, 2], [0, 10], [2, 10], [1, 10]] + [[]]*5)
    pairs = [set(map(tuple, b["points"])) for b in (left, right)]
    intersection = sorted([list(p) for p in pairs[0] if p in pairs[1]])
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    for name, block, point_set in zip(("left", "right"), (left, right), pairs):
        check(name + "_complete_points", block["points"] == witness[name])
        check(name + "_nine_distinct", len(block["points"]) == len(point_set) == 9)
        check(name + "_ambient", all(0 <= c <= 8 and 0 <= x < 107 for c, x in point_set))
        check(name + "_profile", block["profile"] == [3, 2, 2, 2])
        check(name + "_raw_record", block["raw_totals"] == witness["raw_totals_" + name])
        check(name + "_raw_claim", block["raw_totals"] == [36, 310, 3018, 67])
        check(name + "_syndrome_record", block["syndrome"] == witness["syndrome_" + name])
        check(name + "_syndrome_claim", block["syndrome"] == [36, 96, 22, 67])
        check(name + "_division_identities", all(n == 107*q+r and 0 <= r < 107
              for n, q, r in zip(block["raw_totals"], block["quotients"], block["syndrome"])))
    check("distinct_blocks", pairs[0] != pairs[1])
    check("same_syndrome", left["syndrome"] == right["syndrome"])
    check("complete_intersection", intersection == witness["intersection"])
    check("intersection_claim", len(intersection) == witness["intersection_size"] == 6)
    check("conflict_threshold", witness["required_intersection_size"] == 5 <= len(intersection))
    check("profile_record", witness["profiles"] == [left["profile"], right["profile"]])
    expected_checks = {
        "ambient_points": checks["left_ambient"] and checks["right_ambient"],
        "nine_distinct_points_each": checks["left_nine_distinct"] and checks["right_nine_distinct"],
        "distinct_blocks": checks["distinct_blocks"],
        "required_profiles": checks["left_profile"] and checks["right_profile"],
        "same_syndrome": checks["same_syndrome"],
        "conflict": len(intersection) >= 5,
    }
    check("all_saved_witness_checks", witness["checks"] == expected_checks)
    check("witness_keys", set(witness) == {"left", "right", "profiles", "raw_totals_left",
          "raw_totals_right", "syndrome_left", "syndrome_right", "intersection",
          "intersection_size", "required_intersection_size", "checks"})
    check("source_context", source["field_order"] == 107 and source["columns"] == list(range(9))
          and source["profile"] == [3, 2, 2, 2]
          and source["map"] == ["sum x", "sum x^2", "sum x^3", "sum c*x"]
          and source["universal_search"] is False and source["failures"] == [])
    # Audit the incidental six-trial report independently, without a new search.
    trials = []
    for values in permutations([0, 1, 2]):
        rotated = values[1:] + values[:1]
        blocks = [reconstruct([[0, 1, 2]] + [[v, 10] for v in seq] + [[]]*5)
                  for seq in (values, rotated)]
        common = set(map(tuple, blocks[0]["points"])) & set(map(tuple, blocks[1]["points"]))
        trials.append({"values": list(values), "rotated": list(rotated),
                       "syndrome_left": blocks[0]["syndrome"],
                       "syndrome_right": blocks[1]["syndrome"],
                       "intersection_size": len(common),
                       "is_witness": blocks[0]["syndrome"] == blocks[1]["syndrome"]
                                     and len(common) >= 5})
    check("six_complete_trials", trials == source["trials"] and len(trials) == 6)
    check("two_reported_witnesses", sum(t["is_witness"] for t in trials) == source["witness_count"] == 2)
    dag_rows = [line for line in (ROOT / "DAG.md").read_text().splitlines() if line.startswith("L046:")]
    check("direct_dag_input", dag_rows == ["L046: L045"])
    failures = [name for name, result in checks.items() if not result]
    certificate = {"left": left, "right": right, "intersection": intersection,
                   "left_only": sorted(pairs[0] - pairs[1]),
                   "right_only": sorted(pairs[1] - pairs[0]),
                   "trials": trials, "checks": checks, "failures": failures,
                   "conclusion": "This fixed map has a conflicting fiber; no all-fibers or packing-size conclusion."}
    output = HERE / "mixed-moment-collision-audit-results.json"
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Checks: {len(checks)-len(failures)}/{len(checks)}; failures={failures}")
    print(f"Intersection actual={len(intersection)}, required>=5; both syndromes={left['syndrome']}")
    print(f"Full certificate: {output.relative_to(ROOT)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
