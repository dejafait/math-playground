"""Separate L166 audit from literal proof tables, without constructor imports."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
S = (1, 8, 12, 18, 22, 27, 33)
J = (47, 50, 64, 70, 75, 79, 85, 89, 96)
# Transcribed from both complete tables of L166, with one-based row labels.
ROWS = (
    ((1, 12), (47, 50)),
    ((1, 18), (64, 70)),
    ((1, 22), (75, 79)),
    ((1, 27), (85, 89)),
    ((8, 12), (79, 89)),
    ((8, 18), (75, 85)),
    ((8, 22), (47, 70)),
    ((8, 27), (50, 64)),
    ((12, 22), (64, 85)),
    ((12, 27), (70, 75)),
    ((18, 22), (50, 89)),
    ((18, 27), (47, 79)),
)
J_TABLE = {
    47: (1, 7, 12), 50: (1, 8, 11), 64: (2, 8, 9),
    70: (2, 7, 10), 75: (3, 6, 10), 79: (3, 5, 12),
    85: (4, 6, 9), 89: (4, 5, 11), 96: (),
}
checks = []
failures = []


def check(name, condition):
    passed = bool(condition)
    checks.append({"name": name, "passed": passed})
    if not passed:
        failures.append(name)


source_path = HERE / "counterexample.json"
source_bytes = source_path.read_bytes()
data = json.loads(source_bytes)
saved_verification = json.loads((HERE / "verification.json").read_text())
edges = [frozenset(s + j) for s, j in ROWS]
active_s = frozenset(S[:-1])
check("disjoint ambient parts", set(S).isdisjoint(J))
check("exact twelve distinct four-sets", len(edges) == len(set(edges)) == 12
      and all(len(e) == 4 for e in edges))
check("m within original interval", 12 <= len(edges) <= 14)
check("two-plus-two and no outside labels", all(
    len(e & set(S)) == len(e & set(J)) == 2
    and e <= set(S + J) for e in edges))
check("certificate ambient sets", data["S"] == list(S) and data["J"] == list(J))
check("every certificate row equals literal first table",
      data["edges"] == [list(s + j) for s, j in ROWS])
check("S pairs are K6 minus the stated matching",
      {frozenset(s) for s, _ in ROWS} ==
      {frozenset(p) for p in combinations(active_s, 2)} -
      {frozenset((1, 8)), frozenset((12, 18)), frozenset((22, 27))})
check("J pairs distinct", len({j for _, j in ROWS}) == 12)

degrees = {str(x): sum(x in e for e in edges) for x in S + J}
expected_degrees = {str(x): (0 if x in (33, 96) else 4 if x in S else 3)
                    for x in S + J}
check("all sixteen degrees match the proof", degrees == expected_degrees)
check("all sixteen degrees match the certificate", degrees == data["degrees"])
check("maximum integer degree at most four", max(degrees.values()) <= 4)
j_records = []
for x in J:
    indices = tuple(i + 1 for i, e in enumerate(edges) if x in e)
    check(f"literal J table row {x}", indices == J_TABLE[x])
    multiplicities = Counter(y for i in indices for y in ROWS[i - 1][0])
    partitions = multiplicities == Counter(active_s) if indices else None
    if indices:
        check(f"J incidence triple {x} partitions all active S", partitions)
    j_records.append({"label": x, "one_based_indices": indices,
                      "S_multiplicities": dict(sorted(multiplicities.items())),
                      "partitions_active_S": partitions})

# Reconstruct all entries directly by set intersections, not saved columns.
pair_records = []
for i, j in combinations(range(12), 2):
    intersection = sorted(edges[i] & edges[j])
    check(f"linearity of rows {i + 1},{j + 1}", len(intersection) <= 1)
    pair_records.append({"indices": [i, j], "intersection": intersection})
check("all 66 pair records equal certificate", pair_records == data["pair_checks"])

quad_records = []
multiplicity_records = []
for indices in combinations(range(12), 4):
    s_counts = Counter(x for i in indices for x in edges[i] & set(S))
    j_counts = Counter(x for i in indices for x in edges[i] & set(J))
    # Sum binomial multiplicities counts pair intersections with repetitions;
    # it explicitly detects triple/fourfold coincidences as well.
    s_pair_total = sum(comb(d, 2) for d in s_counts.values())
    j_pair_total = sum(comb(d, 2) for d in j_counts.values())
    target = s_pair_total == 1 and j_pair_total == 0
    intersections = [sorted(edges[i] & edges[j])
                     for i, j in combinations(indices, 2)]
    direct_target = (sum(bool(t) for t in intersections) == 1
                     and sum(len(t) == 1 and t[0] in S
                             for t in intersections) == 1)
    check(f"independent target predicates agree for {indices}", target == direct_target)
    # Verify the counting consequence, without taking absence as a premise.
    if target:
        check(f"seven-label necessity for {indices}", len(s_counts) == 7)
    check(f"six-label bound for {indices}", set(s_counts) <= active_s)
    quad_records.append({"indices": list(indices), "S_union": sorted(s_counts),
                         "pair_intersections": intersections,
                         "target_pattern": target})
    multiplicity_records.append({"indices": list(indices),
                                 "S_multiplicities": dict(sorted(s_counts.items())),
                                 "J_multiplicities": dict(sorted(j_counts.items())),
                                 "S_pair_total": s_pair_total,
                                 "J_pair_total": j_pair_total})
check("all 495 four-subset records equal certificate",
      quad_records == data["quadruple_checks"])
check("no target pattern", not any(r["target_pattern"] for r in quad_records))
check("pair and four-subset coverage", len(pair_records) == comb(12, 2) == 66
      and len(quad_records) == comb(12, 4) == 495)
summary = {
    "edges": 12, "required_edges": [12, 14],
    "pair_checks": len(pair_records), "quadruple_checks": len(quad_records),
    "target_patterns": sum(r["target_pattern"] for r in quad_records),
    "max_degree": max(degrees.values()), "required_max_degree": 4,
    "max_S_union_four_edges": max(len(r["S_union"]) for r in quad_records),
    "required_S_union_for_target": 7,
}
check("entire certificate summary", summary == data["summary"])
check("certificate records success without failures", data["found"] is True
      and data["failures"] == [])
check("prior verification agrees after complete reconstruction",
      saved_verification["verified"] is True
      and saved_verification["failures"] == []
      and saved_verification["summary"] == summary)

outpath = HERE / "l166-critical-audit.json"
out = {
    "verified": not failures,
    "scope": "L166 abstract incidence only; no coding or completion claim",
    "certificate": str(source_path.relative_to(ROOT)),
    "certificate_sha256": sha256(source_bytes).hexdigest(),
    "method": "literal proof tables; independent multiplicity target predicate",
    "summary": summary, "degrees": degrees, "J_table_checks": j_records,
    "pair_checks": pair_records, "quadruple_checks": quad_records,
    "quadruple_multiplicities": multiplicity_records,
    "checks": checks, "failures": failures,
}
outpath.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"verified": out["verified"], "summary": summary,
                  "failures": failures, "checks_performed": len(checks),
                  "input": out["certificate"],
                  "audit": str(outpath.relative_to(ROOT))}))
raise SystemExit(bool(failures))
