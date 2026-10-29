"""Bounded exact construction search; write complete witness/check evidence."""
import itertools
import json
from pathlib import Path

S = (1, 8, 12, 18, 22, 27, 33)
J = (47, 50, 64, 70, 75, 79, 85, 89, 96)
PAIRS = tuple(p for p in itertools.combinations(S[:6], 2)
              if p not in ((1, 8), (12, 18), (22, 27)))
JPAIRS = tuple(itertools.combinations(J, 2))
LIMIT = 1_000_000
nodes = 0
assigned = {}
degree = dict.fromkeys(J, 0)


def options(i):
    return [p for p in JPAIRS
            if all(degree[x] < 4 for x in p)
            and all(len(set(PAIRS[i]) & set(PAIRS[k]))
                    + len(set(p) & set(q)) <= 1
                    for k, q in assigned.items())]


def search():
    global nodes
    nodes += 1
    if nodes > LIMIT:
        return False
    if len(assigned) == len(PAIRS):
        return True
    domains = [(options(i), i) for i in range(len(PAIRS))
               if i not in assigned]
    choices, i = min(domains, key=lambda t: (len(t[0]), t[1]))
    for p in choices:
        assigned[i] = p
        for x in p:
            degree[x] += 1
        if search():
            return True
        for x in p:
            degree[x] -= 1
        del assigned[i]
    return False


found = search()
out = {"scope": "abstract incidence only; no coding realization",
       "S": S, "J": J, "nodes": nodes, "node_limit": LIMIT,
       "found": found}
if found:
    edges = [list(PAIRS[i] + assigned[i]) for i in range(len(PAIRS))]
    sets = list(map(set, edges))
    pair_checks = [{"indices": [i, j],
                    "intersection": sorted(sets[i] & sets[j])}
                   for i, j in itertools.combinations(range(12), 2)]
    quadruples = []
    for indices in itertools.combinations(range(12), 4):
        intersections = [sets[i] & sets[j]
                         for i, j in itertools.combinations(indices, 2)]
        nonempty = [sorted(t) for t in intersections if t]
        pattern = (len(nonempty) == 1 and len(nonempty[0]) == 1
                   and nonempty[0][0] in S)
        quadruples.append({"indices": indices,
                           "S_union": sorted(set().union(
                               *(sets[i] & set(S) for i in indices))),
                           "pair_intersections": [sorted(t) for t in intersections],
                           "target_pattern": pattern})
    degrees = {str(x): sum(x in e for e in sets) for x in S + J}
    failures = []
    if len({tuple(sorted(e)) for e in sets}) != 12:
        failures.append("distinctness")
    if not all(len(e) == 4 and len(e & set(S)) == 2
               and len(e & set(J)) == 2 for e in sets):
        failures.append("two-plus-two")
    if not all(len(p["intersection"]) <= 1 for p in pair_checks):
        failures.append("linearity")
    if max(degrees.values()) > 4:
        failures.append("degree")
    if any(q["target_pattern"] for q in quadruples):
        failures.append("target pattern found")
    out.update(edges=edges, degrees=degrees, pair_checks=pair_checks,
               quadruple_checks=quadruples, failures=failures,
               summary={"edges": 12, "required_edges": [12, 14],
                        "pair_checks": len(pair_checks),
                        "quadruple_checks": len(quadruples),
                        "target_patterns": sum(q["target_pattern"] for q in quadruples),
                        "max_degree": max(degrees.values()),
                        "required_max_degree": 4,
                        "max_S_union_four_edges": max(len(q["S_union"]) for q in quadruples),
                        "required_S_union_for_target": 7})
path = Path(__file__).with_name("counterexample.json")
path.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"found": found, "nodes": nodes,
                  "summary": out.get("summary"),
                  "failures": out.get("failures"), "certificate": str(path)}))
if not found or out["failures"]:
    raise SystemExit(1)
