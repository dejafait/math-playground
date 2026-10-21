"""Complete finite incidence check for L077; no RS-label sampling."""
import json
from itertools import combinations, product
from pathlib import Path


def mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        b >>= 1
        if a & 4:
            a ^= 7
    return result


labels = [
    ["a", "b", "y_1", "y_2"],
    ["c", "d_1", "d_2", "d_3"],
    ["z_1", "d_4", "d_5", "w_1"],
    ["z_2", "d_6", "w_2", "d_7"],
]
blocks = {f"V{i}": {(i, y) for y in range(4)} for i in range(4)}
blocks.update({f"M{m}D{e}": {(x, mul(m, x) ^ e) for x in range(4)}
               for m in (0, 1, 2) for e in range(4)})
classes = [[f"V{i}" for i in range(4)]] + [
    [f"M{m}D{e}" for e in range(4)] for m in (0, 1, 2)]
failures = []
cases, quads = [], []
for ids in product(*classes):
    triples = [{"blocks": list(t), "points": sorted(set.intersection(
        *(blocks[b] for b in t)))} for t in combinations(ids, 3)]
    valid = not any(t["points"] for t in triples)
    cases.append({"blocks": list(ids), "triple_intersections": triples,
                  "valid": valid})
    if not valid:
        continue
    union = set.union(*(blocks[b] for b in ids))
    singles = [blocks[b] - set.union(*(blocks[c] for c in ids if c != b))
               for b in ids]
    if len(union) != 10 or any(len(s) != 1 for s in singles):
        failures.append("union/singleton condition " + str(ids))
        continue
    points = [next(iter(s)) for s in singles]
    quads.append({"blocks": list(ids), "singleton_points": points,
                  "singleton_labels": [labels[x][y] for x, y in points],
                  "union_points": sorted(union)})

formula = {(f"V{i}", f"M0D{j}", f"M1D{k}",
            f"M2D{i ^ mul(3, k) ^ mul(2, j)}")
           for i, j, k in product(range(4), repeat=3) if k != (i ^ j)}
if formula != {tuple(q["blocks"]) for q in quads}:
    failures.append("complete formula/case-set disagreement")

seed = ["V0", "V1", "V2", "M0D0", "M1D0"]
known = set(seed)
chain = []
while True:
    for q in quads:
        missing = set(q["blocks"]) - known
        if len(missing) == 1:
            new = next(iter(missing))
            chain.append({"quadrilateral": q["blocks"],
                          "singleton_labels": q["singleton_labels"],
                          "known_inputs": [b for b in q["blocks"] if b != new],
                          "recovered": new})
            known.add(new)
            break
    else:
        break
if known != set(blocks) or len(chain) != 11:
    failures.append("five-seed closure")

certificate = {
    "scope": "Complete auxiliary-F4 incidence only; not fixed-H rank or realization",
    "candidate_cases": cases, "quadrilaterals": quads,
    "formula_quadrilaterals": sorted(formula),
    "reconstruction": {"seed": seed, "chain": chain, "covered": sorted(known)},
    "actual": {"cases": len(cases), "valid_quadrilaterals": len(quads),
               "formula_quadrilaterals": len(formula), "seed_size": len(seed),
               "reconstruction_steps": len(chain), "covered_blocks": len(known)},
    "required": {"cases": 256, "valid_quadrilaterals": 48,
                 "formula_quadrilaterals": 48, "seed_size": 5,
                 "reconstruction_steps": 11, "covered_blocks": 16},
    "failures": failures,
}
if certificate["actual"] != certificate["required"]:
    failures.append("actual/required bounds")
output = Path(__file__).with_name("affine-plane-quadrilaterals.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{'FAIL' if failures else 'PASS'}: cases {len(cases)}/256; quadrilaterals "
      f"{len(quads)}/48; five-seed reconstruction {len(chain)}/11; "
      f"coverage {len(known)}/16. No H-labeling tested.")
print(f"Failures: {failures}; certificate: {output}")
raise SystemExit(bool(failures))
