#!/usr/bin/env python3
"""Replay the full certificate from an independently transcribed row table."""

from collections import Counter
from itertools import combinations
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
S = {1, 8, 12, 18, 22, 27, 33}
J = {47, 50, 64, 70, 75, 79, 85, 89, 96}
# Four successive groups are the four parallel classes in the proof.
TABLE = (
    (1, 47, 50, 64), (8, 12, 70, 75), (18, 22, 79, 85), (27, 33, 89, 96),
    (1, 18, 70, 89), (22, 47, 75, 96), (8, 27, 50, 79), (12, 33, 64, 85),
    (1, 33, 75, 79), (27, 47, 70, 85), (12, 18, 50, 96), (8, 22, 64, 89),
    (1, 8, 85, 96), (12, 47, 79, 89), (22, 33, 50, 70), (18, 27, 64, 75),
)


def main():
    data = json.loads((HERE / "counterexample.json").read_text())
    checks = []

    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})

    edges = {i + 1: set(row) for i, row in enumerate(TABLE)}
    # Column incidence is the independent reconstruction of every intersection.
    columns = {x: {i for i, edge in edges.items() if x in edge} for x in sorted(S | J)}
    e2 = [i for i, edge in edges.items() if len(edge & S) == 2]
    completion = [i for i in edges if i not in e2]
    check("exact fixed partition", set(data["S"]) == S and set(data["J"]) == J
          and len(data["S"]) == 7 and len(data["J"]) == 9 and not (S & J))
    check("sixteen distinct four-sets on S union J",
          len(edges) == len({tuple(sorted(edge)) for edge in edges.values()}) == 16
          and all(len(edge) == 4 and edge <= S | J for edge in edges.values()))
    check("complete row list", [row["id"] for row in data["rows"]] == list(edges))
    for row in data["rows"]:
        i = row["id"]
        check(f"complete row {i}", row["labels"] == sorted(edges[i])
              and row["S_labels"] == sorted(edges[i] & S)
              and row["J_labels"] == sorted(edges[i] & J)
              and row["in_E2"] == (i in e2))
    check("every degree is exactly four", all(len(v) == 4 for v in columns.values()))
    saved_degrees = {d["label"]: d for d in data["degrees"]}
    check("all sixteen degree records", len(data["degrees"]) == 16 and set(saved_degrees) == S | J)
    for x, ids in columns.items():
        check(f"degree and incidence column {x}", saved_degrees[x]["rows"] == sorted(ids)
              and saved_degrees[x]["degree"] == len(ids) == 4)
    check("complete E2 and remaining rows", data["E2_rows"] == e2 and len(e2) == 12
          and data["completing_rows"] == completion == [1, 6, 10, 14]
          and all(len(edges[i] & S) == 1 for i in completion))
    pairs = []
    for a, b in combinations(edges, 2):
        intersection = sorted(x for x, ids in columns.items() if a in ids and b in ids)
        same_class = (a - 1) // 4 == (b - 1) // 4
        check(f"pair {a},{b} exact parallel-class rule", len(intersection) == (0 if same_class else 1))
        pairs.append({"rows": [a, b], "intersection": intersection})
    check("all 120 saved pair records", data["pair_intersections"] == pairs and len(pairs) == 120)
    quadruples = []
    multiplicities = []
    for ids in combinations(e2, 4):
        selected = set(ids)
        counts = {x: len(column & selected) for x, column in columns.items()}
        s_total = sum(counts[x] * (counts[x] - 1) // 2 for x in S)
        j_total = sum(counts[x] * (counts[x] - 1) // 2 for x in J)
        target = s_total == 1 and j_total == 0
        p_records = [{"rows": [a, b], "intersection": sorted(
            x for x, column in columns.items() if {a, b} <= column)}
            for a, b in combinations(ids, 2)]
        nonempty_count = sum(bool(p["intersection"]) for p in p_records)
        class_counts = [sum((i - 1) // 4 == c for i in ids) for c in range(4)]
        class_formula = 6 - sum(n * (n - 1) // 2 for n in class_counts)
        check(f"quadruple {ids} independent predicates",
              s_total + j_total == nonempty_count == class_formula >= 3
              and max(class_counts) <= 3 and not target)
        quadruples.append({
            "rows": list(ids), "pair_intersections": p_records,
            "nonempty_pairs": nonempty_count, "S_pair_multiplicity": s_total,
            "J_pair_multiplicity": j_total, "target": target,
        })
        multiplicities.append({"rows": list(ids), "coordinate_multiplicities": counts,
                               "parallel_class_counts": class_counts,
                               "intersecting_pairs_from_classes": class_formula})
    check("all 495 saved quadruple records", data["E2_quadruples"] == quadruples
          and len(quadruples) == 495)
    histogram = dict(sorted(Counter(q["nonempty_pairs"] for q in quadruples).items()))
    check("full quadruple histogram", histogram == {3: 36, 4: 54, 5: 324, 6: 81})
    summary = {
        "row_count": len(edges), "required_row_count": 16,
        "E2_count": len(e2), "required_E2_interval": [12, 14],
        "degree_values": sorted({len(v) for v in columns.values()}), "required_degree": 4,
        "maximum_pair_intersection": max(len(p["intersection"]) for p in pairs),
        "required_maximum_pair_intersection": 1,
        "checked_pairs": len(pairs), "required_pairs": 120,
        "checked_E2_quadruples": len(quadruples), "required_E2_quadruples": 495,
        "minimum_intersecting_pairs_in_E2_quadruple": min(q["nonempty_pairs"] for q in quadruples),
        "required_intersecting_pairs_for_target": 1,
        "intersecting_pair_histogram": {str(k): v for k, v in histogram.items()},
        "marked_pattern_count": sum(q["target"] for q in quadruples),
        "required_pattern_count_for_counterexample": 0,
        "failures": [],
    }
    check("entire saved summary", data["summary"] == summary)
    failures = [c["name"] for c in checks if not c["passed"]]
    path = HERE / "verification.json"
    path.write_text(json.dumps({
        "scope": "Same-step independent table/column replay; separate critical audit pending.",
        "table": TABLE, "columns": {str(x): sorted(v) for x, v in columns.items()},
        "E2_rows": e2, "completing_rows": completion, "pair_intersections": pairs,
        "E2_quadruples": quadruples, "quadruple_multiplicities": multiplicities,
        "checks": checks, "summary": summary, "failures": failures,
    }, indent=2) + "\n")
    print(f"Independent table replay: {len(checks)} checks; failures: {failures}")
    print("Rows 16/16; E2 12 in [12,14]; degrees 4/4; pairs 120/120; quadruples 495/495.")
    print(f"Intersecting-pair histogram: {histogram}; minimum 3 > target 1; marked patterns 0/0.")
    print(f"Verification: {path.relative_to(HERE.parent.parent)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
