"""Independent incidence replay of the entire saved finite certificate."""
import itertools
import json
from pathlib import Path

path = Path(__file__).with_name("counterexample.json")
data = json.loads(path.read_text())
S = (1, 8, 12, 18, 22, 27, 33)
J = (47, 50, 64, 70, 75, 79, 85, 89, 96)
edges = data["edges"]
assert data["S"] == list(S) and data["J"] == list(J)
assert 12 <= len(edges) <= 14
assert len({tuple(sorted(e)) for e in edges}) == len(edges)
assert all(len(e) == len(set(e)) == 4 for e in edges)
assert all(sum(x in S for x in e) == sum(x in J for x in e) == 2
           for e in edges)
columns = {x: [i for i, e in enumerate(edges) if x in e] for x in S + J}
degrees = {str(x): len(col) for x, col in columns.items()}
assert degrees == data["degrees"]
assert max(degrees.values()) <= 4
intersections = {}
for i, j in itertools.combinations(range(len(edges)), 2):
    intersections[i, j] = [x for x, col in columns.items()
                            if i in col and j in col]
assert all(len(t) <= 1 for t in intersections.values())
assert data["pair_checks"] == [
    {"indices": list(pair), "intersection": sorted(t)}
    for pair, t in intersections.items()]
replay = []
for quad in itertools.combinations(range(len(edges)), 4):
    six = [intersections[pair] for pair in itertools.combinations(quad, 2)]
    pattern = (sum(bool(t) for t in six) == 1
               and sum(len(t) == 1 and t[0] in S for t in six) == 1)
    union = [x for x in S if any(i in columns[x] for i in quad)]
    replay.append({"indices": list(quad), "S_union": sorted(union),
                   "pair_intersections": [sorted(t) for t in six],
                   "target_pattern": pattern})
assert replay == data["quadruple_checks"]
assert not any(q["target_pattern"] for q in replay)
assert not data["failures"]
summary = {"edges": len(edges), "required_edges": [12, 14],
           "pair_checks": len(intersections), "quadruple_checks": len(replay),
           "target_patterns": sum(q["target_pattern"] for q in replay),
           "max_degree": max(degrees.values()), "required_max_degree": 4,
           "max_S_union_four_edges": max(len(q["S_union"]) for q in replay),
           "required_S_union_for_target": 7}
assert summary == data["summary"]
out = {"verified": True, "summary": summary, "failures": [],
       "certificate": str(path.relative_to(path.parents[2])),
       "method": "rebuild columns and all 66 pair/495 quadruple records"}
outpath = path.with_name("verification.json")
outpath.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(dict(out, verification=str(outpath))))
