#!/usr/bin/env python3
"""Separate L167 audit: parse canonical tables, reconstruct all finite evidence.

Does not import or run either original certificate producer. F_4 multiplication
uses polynomial reduction rather than their hard-coded multiplication table.
Original certificates are read-only; the full audit is saved separately.
"""

from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
S = {1, 8, 12, 18, 22, 27, 33}
J = {47, 50, 64, 70, 75, 79, 85, 89, 96}
L167 = ROOT / "lemmas/L167-completed-family-marked-extraction-counterexample.md"
L072 = ROOT / "lemmas/L072-triangle-balanced-linear-support-witness.md"


def mul(a, b):
    """Multiply binary polynomials, then reduce by u^2+u+1 (binary 111)."""
    product = 0
    for power in range(2):
        if b & (1 << power):
            product ^= a << power
    for power in range(product.bit_length() - 1, 1, -1):
        if product & (1 << power):
            product ^= 0b111 << (power - 2)
    return product


def table(text, first_header):
    lines = text.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(first_header))
    result = []
    for line in lines[start + 2:]:
        if not line.startswith("|"):
            break
        result.append([cell.strip() for cell in line.strip("|").split("|")])
    return result


def main():
    inputs = [L167, L072, HERE / "counterexample.json", HERE / "verification.json"]
    texts = {p: p.read_text() for p in inputs}
    data = json.loads(texts[inputs[2]])
    replay = json.loads(texts[inputs[3]])
    checks = []

    def equal(name, actual, expected):
        record = {"name": name, "passed": actual == expected}
        if actual != expected:
            record.update(actual=actual, expected=expected)
        checks.append(record)

    points = list((x, y) for x in range(4) for y in range(4))
    directions = ("vertical", 0, 1, 2)
    coordinate_lines = []
    for direction in directions:
        for e in range(4):
            coordinate_lines.append([p for p in points if
                (p[0] if direction == "vertical" else p[1] ^ mul(direction, p[0])) == e])

    # Check L072's complete table, including its prescribed triangle.
    abstract_grid = [row[1:] for row in table(texts[L072], "| X ")]
    abstract_rows = table(texts[L072], "| Coordinate/intercept")
    equal("L072 grid dimensions", [len(r) for r in abstract_grid], [4] * 4)
    abstract_labels = [x for row in abstract_grid for x in row]
    equal("L072 sixteen distinct abstract labels", len(set(abstract_labels)), 16)
    for c in range(4):
        for e in range(4):
            expected = sorted(abstract_grid[x][y] for x, y in coordinate_lines[4 * c + e])
            actual = sorted(abstract_rows[e][c + 1].strip("{}").split(","))
            equal(f"L072 coordinate block {c},{e}", actual, expected)
    equal("L072 prescribed triangle", [sorted(abstract_grid[x][y] for x, y in
          coordinate_lines[i]) for i in (0, 4, 9)],
          [sorted(v) for v in (("a", "b", "y_1", "y_2"),
                              ("a", "c", "z_1", "z_2"),
                              ("b", "c", "w_1", "w_2"))])

    grid = [[int(v) for v in row[1:]] for row in table(texts[L167], "| X ")]
    equal("L167 grid dimensions", [len(r) for r in grid], [4] * 4)
    equal("fixed label bijection", sorted(v for row in grid for v in row), sorted(S | J))
    proof_rows = table(texts[L167], "| Row | Class")
    equal("complete proof table size", len(proof_rows), 16)
    rows = []
    for i, line in enumerate(coordinate_lines):
        labels = sorted(grid[x][y] for x, y in line)
        row = {"id": i + 1, "class": str(directions[i // 4]), "intercept": i % 4,
               "points": [list(p) for p in line], "labels": labels,
               "S_labels": sorted(set(labels) & S), "J_labels": sorted(set(labels) & J),
               "in_E2": len(set(labels) & S) == 2}
        rows.append(row)
        p = proof_rows[i]
        equal(f"L167 displayed row {i + 1}",
              [int(p[0]), p[1], sorted(map(int, p[2].split(","))),
               sorted(map(int, p[3].split(",")))],
              [i + 1, ("vertical", "slope 0", "slope 1", "slope u")[i // 4],
               row["S_labels"], row["J_labels"]])
    equal("all saved coordinate and label row records", data["rows"], rows)
    equal("saved fixed partition", [data["S"], data["J"]], [sorted(S), sorted(J)])
    equal("saved label grid", data["label_grid"], grid)
    omitted = [{(x, mul(3, x) ^ e) for x in range(4)} for e in (0, 1)]
    equal("two omitted lines are disjoint", sorted(omitted[0] & omitted[1]), [])
    equal("omitted-line labels", [sorted(grid[x][y] for x, y in line) for line in omitted],
          [[1, 12, 22, 27], [8, 18, 33, 47]])
    equal("removed point label", grid[0][1], 47)
    equal("S equals omitted union minus P",
          sorted(grid[x][y] for x, y in (omitted[0] | omitted[1]) - {(0, 1)}), sorted(S))

    edges = {r["id"]: set(r["labels"]) for r in rows}
    columns = {v: sorted(i for i, edge in edges.items() if v in edge) for v in sorted(S | J)}
    degrees = [{"label": v, "rows": columns[v], "degree": len(columns[v])} for v in sorted(S | J)]
    equal("sixteen distinct four-sets", [len(set(tuple(r["labels"]) for r in rows)),
          sorted(set(map(len, edges.values())))], [16, [4]])
    equal("all sixteen full-family degrees", [len(columns[v]) for v in sorted(S | J)], [4] * 16)
    equal("all saved degree records", data["degrees"], degrees)
    e2 = [i for i, edge in edges.items() if len(edge & S) == 2]
    completion = [i for i in edges if i not in e2]
    equal("complete E2", e2, [2, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 16])
    equal("complete omitted rows", completion, [1, 6, 10, 14])
    equal("omitted row S-overlaps", [len(edges[i] & S) for i in completion], [1] * 4)
    equal("E2 S-degrees", [sum(v in edges[i] for i in e2) for v in sorted(S)],
          [3, 4, 3, 4, 3, 3, 4])
    pairs = []
    for a, b in combinations(edges, 2):
        intersection = sorted(edges[a] & edges[b])
        equal(f"exact class incidence {a},{b}", len(intersection), int((a - 1) // 4 != (b - 1) // 4))
        pairs.append({"rows": [a, b], "intersection": intersection})
    quadruples, multiplicities = [], []
    occupancies = Counter()
    for ids in combinations(e2, 4):
        counts = {v: sum(v in edges[i] for i in ids) for v in sorted(S | J)}
        s = sum(n * (n - 1) // 2 for v, n in counts.items() if v in S)
        j = sum(n * (n - 1) // 2 for v, n in counts.items() if v in J)
        pr = [{"rows": [a, b], "intersection": sorted(edges[a] & edges[b])}
              for a, b in combinations(ids, 2)]
        t = sum(bool(p["intersection"]) for p in pr)
        marked = [p for p in pr if p["intersection"]]
        direct_target = len(marked) == 1 and marked[0]["intersection"][0] in S
        cc = [sum((i - 1) // 4 == c for i in ids) for c in range(4)]
        formula = 6 - sum(n * (n - 1) // 2 for n in cc)
        equal(f"quadruple {ids} counts and predicates", [t, t, direct_target, t >= 3],
              [s + j, formula, s == 1 and j == 0, True])
        quadruples.append({"rows": list(ids), "pair_intersections": pr, "nonempty_pairs": t,
                           "S_pair_multiplicity": s, "J_pair_multiplicity": j,
                           "target": direct_target})
        multiplicities.append({"rows": list(ids), "coordinate_multiplicities":
                               {str(v): n for v, n in counts.items()}, "parallel_class_counts": cc,
                               "intersecting_pairs_from_classes": formula})
        occupancies[tuple(sorted((n for n in cc if n), reverse=True))] += 1
    equal("all occupancy cases with multiplicities", {str(k): v for k, v in occupancies.items()},
          {str((3, 1)): 36, str((2, 2)): 54, str((2, 1, 1)): 324, str((1, 1, 1, 1)): 81})
    histogram = {str(k): v for k, v in sorted(Counter(q["nonempty_pairs"] for q in quadruples).items())}
    summary = {"row_count": 16, "required_row_count": 16, "E2_count": len(e2),
               "required_E2_interval": [12, 14], "degree_values": sorted({len(c) for c in columns.values()}),
               "required_degree": 4, "maximum_pair_intersection": max(len(p["intersection"]) for p in pairs),
               "required_maximum_pair_intersection": 1, "checked_pairs": len(pairs), "required_pairs": 120,
               "checked_E2_quadruples": len(quadruples), "required_E2_quadruples": 495,
               "minimum_intersecting_pairs_in_E2_quadruple": min(q["nonempty_pairs"] for q in quadruples),
               "required_intersecting_pairs_for_target": 1, "intersecting_pair_histogram": histogram,
               "marked_pattern_count": sum(q["target"] for q in quadruples),
               "required_pattern_count_for_counterexample": 0, "failures": []}
    for name, expected in (("E2_rows", e2), ("completing_rows", completion),
                           ("pair_intersections", pairs), ("E2_quadruples", quadruples),
                           ("summary", summary)):
        equal("constructor full field " + name, data[name], expected)
        equal("prior replay full field " + name, replay[name], expected)
    equal("prior replay table", replay["table"], [r["labels"] for r in rows])
    equal("prior replay columns", replay["columns"], {str(v): c for v, c in columns.items()})
    equal("all prior replay coordinate multiplicities", replay["quadruple_multiplicities"], multiplicities)
    equal("prior replay check count", len(replay["checks"]), 657)
    equal("prior replay check results", [c["passed"] for c in replay["checks"]], [True] * 657)
    equal("prior replay failures", replay["failures"], [])
    failures = [c for c in checks if not c["passed"]]
    path = HERE / "l167-critical-audit.json"
    path.write_text(json.dumps({
        "scope": "Separate finite L167 incidence audit only; no coding realization or challenge conclusion.",
        "input_sha256": {str(p.relative_to(ROOT)): sha256(texts[p].encode()).hexdigest() for p in inputs},
        "checks": checks, "rows": rows, "columns": {str(v): c for v, c in columns.items()},
        "pair_intersections": pairs, "E2_quadruples": quadruples,
        "quadruple_multiplicities": multiplicities, "summary": summary,
        "audit_check_count": len(checks), "failures": failures}, indent=2) + "\n")
    print(f"Separate L167 audit: {len(checks)} checks; failures: {len(failures)}")
    print("Rows 16/16; E2 12 in [12,14]; all degrees 4/4; maximum intersection 1/1.")
    print(f"Full records: pairs {len(pairs)}/120; quadruples {len(quadruples)}/495; histogram {histogram}.")
    print("Minimum intersecting pairs 3 > required target 1; marked patterns 0/0.")
    print(f"Certificate: {path.relative_to(ROOT)}")
    if failures:
        print("Failed checks:", [c["name"] for c in failures])
        raise SystemExit(1)


if __name__ == "__main__":
    main()
