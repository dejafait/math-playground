#!/usr/bin/env python3
"""Specialize L072's four affine classes; save a complete incidence witness."""

from collections import Counter
from itertools import combinations
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
S = (1, 8, 12, 18, 22, 27, 33)
J = (47, 50, 64, 70, 75, 79, 85, 89, 96)
GRID = (
    (1, 47, 50, 64),
    (70, 75, 8, 12),
    (18, 22, 79, 85),
    (89, 96, 27, 33),
)
# 0, 1, u, u+1 in F_2[u]/(u^2+u+1); addition is bitwise xor.
MUL = ((0, 0, 0, 0), (0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2))


def main():
    rows = []
    for direction in ("vertical", 0, 1, 2):
        for intercept in range(4):
            points = ([(intercept, y) for y in range(4)]
                      if direction == "vertical" else
                      [(x, MUL[direction][x] ^ intercept) for x in range(4)])
            labels = sorted(GRID[x][y] for x, y in points)
            s_labels = sorted(set(labels) & set(S))
            rows.append({
                "id": len(rows) + 1, "class": str(direction),
                "intercept": intercept, "points": points, "labels": labels,
                "S_labels": s_labels, "J_labels": sorted(set(labels) & set(J)),
                "in_E2": len(s_labels) == 2,
            })
    edges = {row["id"]: set(row["labels"]) for row in rows}
    e2 = [row["id"] for row in rows if row["in_E2"]]
    completing = [row["id"] for row in rows if not row["in_E2"]]
    degrees = [{"label": x, "rows": [i for i in edges if x in edges[i]],
                "degree": sum(x in edge for edge in edges.values())} for x in S + J]
    pairs = [{"rows": [a, b], "intersection": sorted(edges[a] & edges[b])}
             for a, b in combinations(edges, 2)]
    quadruples = []
    for ids in combinations(e2, 4):
        incidences = Counter(x for i in ids for x in edges[i])
        pair_intersections = [{"rows": [a, b],
                               "intersection": sorted(edges[a] & edges[b])}
                              for a, b in combinations(ids, 2)]
        nonempty = [p for p in pair_intersections if p["intersection"]]
        target = (len(nonempty) == 1 and len(nonempty[0]["intersection"]) == 1
                  and nonempty[0]["intersection"][0] in S)
        quadruples.append({
            "rows": list(ids), "pair_intersections": pair_intersections,
            "nonempty_pairs": len(nonempty),
            "S_pair_multiplicity": sum(incidences[x] * (incidences[x] - 1) // 2 for x in S),
            "J_pair_multiplicity": sum(incidences[x] * (incidences[x] - 1) // 2 for x in J),
            "target": target,
        })
    omitted = [[(x, MUL[3][x] ^ e) for x in range(4)] for e in (0, 1)]
    selected_points = set(omitted[0] + omitted[1]) - {(0, 1)}
    failures = []

    def check(name, condition):
        if not condition:
            failures.append(name)

    check("sixteen distinct labels", set(x for line in GRID for x in line) == set(S + J))
    check("S equals two omitted lines minus one point",
          {GRID[x][y] for x, y in selected_points} == set(S))
    check("sixteen distinct four-sets",
          len(rows) == len({tuple(row["labels"]) for row in rows}) == 16
          and all(len(edge) == 4 for edge in edges.values()))
    check("all degrees exactly four", all(d["degree"] == 4 for d in degrees))
    check("all 120 pair intersections at most one",
          len(pairs) == 120 and all(len(p["intersection"]) <= 1 for p in pairs))
    check("complete E2 has twelve rows", len(e2) == 12)
    check("four completing rows have S overlap one",
          len(completing) == 4 and all(len(edges[i] & set(S)) == 1 for i in completing))
    check("all 495 E2 quadruples fail the marked pattern",
          len(quadruples) == 495 and not any(q["target"] for q in quadruples))
    check("E2 quadruples have at least three intersecting pairs",
          min(q["nonempty_pairs"] for q in quadruples) == 3)
    summary = {
        "row_count": len(rows), "required_row_count": 16,
        "E2_count": len(e2), "required_E2_interval": [12, 14],
        "degree_values": sorted({d["degree"] for d in degrees}), "required_degree": 4,
        "maximum_pair_intersection": max(len(p["intersection"]) for p in pairs),
        "required_maximum_pair_intersection": 1,
        "checked_pairs": len(pairs), "required_pairs": 120,
        "checked_E2_quadruples": len(quadruples), "required_E2_quadruples": 495,
        "minimum_intersecting_pairs_in_E2_quadruple": min(q["nonempty_pairs"] for q in quadruples),
        "required_intersecting_pairs_for_target": 1,
        "intersecting_pair_histogram": dict(sorted(Counter(q["nonempty_pairs"] for q in quadruples).items())),
        "marked_pattern_count": sum(q["target"] for q in quadruples),
        "required_pattern_count_for_counterexample": 0,
        "failures": failures,
    }
    certificate = {
        "scope": "One explicit abstract full-family counterexample; no census or coding realization.",
        "S": S, "J": J, "label_grid": GRID, "rows": rows,
        "E2_rows": e2, "completing_rows": completing, "degrees": degrees,
        "pair_intersections": pairs, "E2_quadruples": quadruples, "summary": summary,
    }
    path = HERE / "counterexample.json"
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Rows 16/16; E2 12 in [12,14]; all degrees 4/4; max pair intersection 1/1.")
    print("Checked pairs 120/120, E2 quadruples 495/495; minimum intersecting pairs 3 > target 1.")
    print(f"Marked patterns {summary['marked_pattern_count']}/0; failures: {failures}")
    print(f"Certificate: {path.relative_to(HERE.parent.parent)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
