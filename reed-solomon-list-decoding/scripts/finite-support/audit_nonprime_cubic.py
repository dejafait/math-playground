#!/usr/bin/env python3
"""Independent direct L039 witness audit; no search or producer imports."""
import hashlib
import json
from itertools import combinations
from pathlib import Path

SOURCE = Path(__file__).with_name("nonprime-cubic-results.json")
OUT = Path(__file__).with_name("nonprime-cubic-audit-results.json")
Z, ONE, U = (0, 0), (1, 0), (0, 1)


def scalar(n):
    return n % 11, 0


def add(a, b):
    return (a[0] + b[0]) % 11, (a[1] + b[1]) % 11


def neg(a):
    return (-a[0]) % 11, (-a[1]) % 11


def mul(a, b):
    # Convolve in u, then reduce the u^2 coefficient using u^2=2.
    convolution = [0, 0, 0]
    for i in range(2):
        for j in range(2):
            convolution[i + j] += a[i] * b[j]
    return (convolution[0] + 2 * convolution[2]) % 11, convolution[1] % 11


def encode(a):
    return a[0] + 11 * a[1]


def padd(p, q):
    return [add(p[i] if i < len(p) else Z, q[i] if i < len(q) else Z)
            for i in range(max(len(p), len(q)))]


def pmul(p, q):
    r = [Z] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] = add(r[i + j], mul(a, b))
    return r


def evaluate(p, x):
    # Direct power sum, rather than the producer's Horner method.
    value, power = Z, ONE
    for c in p:
        value = add(value, mul(c, power))
        power = mul(power, x)
    return value


def factors(roots, leading=1):
    p = [scalar(leading)]
    for x in roots:
        p = pmul(p, [neg(x), ONE])
    return p


def points(s):
    return sorted([encode(x), encode(y)] for x, y in s)


source_bytes = SOURCE.read_bytes()
saved = json.loads(source_bytes)
checks = []


def check(name, actual, required):
    checks.append({"name": name, "actual": actual, "required": required,
                   "pass": actual == required})


T = [scalar(i) for i in range(7)] + [U]
deleted = {(Z, scalar(i)) for i in range(4)}
check("positions", [encode(x) for x in T], saved["evaluation_positions"])
check("deleted points", points(deleted), saved["deleted_points"])
check("distinct positions", len(set(T)), 8)
check("squares modulo 11", sorted({i * i % 11 for i in range(11)}), [0, 1, 3, 4, 5, 9])
check("minus u excluded", neg(U) in T, False)
field = [(a, b) for a in range(11) for b in range(11)]
norms = [{"element": encode(x), "norm": (x[0]**2 - 2*x[1]**2) % 11}
         for x in field if x != Z]
check("nonzero norms", sum(row["norm"] != 0 for row in norms), 120)

f = list(map(scalar, [0, -1, 0, 1]))
g = list(map(scalar, [2, 8, -1, 1]))
p = [[scalar(4), Z, Z, Z], padd([scalar(4)], f),
     padd([scalar(4)], g), padd([scalar(4)], padd(f, g))]
polys = {"f": f, "g": g, "f_minus_g": padd(f, [neg(c) for c in g]),
         "f_plus_g": padd(f, g)}
root_lists = {"f": [Z, ONE, scalar(-1)],
              "g": list(map(scalar, [2, 3, 7])),
              "f_minus_g": list(map(scalar, [4, 5])),
              "f_plus_g": [scalar(6), U, neg(U)]}
expanded = {}
for name, roots in root_lists.items():
    product = factors(roots, 2 if name == "f_plus_g" else 1)
    expanded[name] = [encode(c) for c in product]
    check("factorization " + name,
          expanded[name] + [0] * (4 - len(product)), [encode(c) for c in polys[name]])
    check("all field roots " + name,
          sorted(encode(x) for x in field if evaluate(polys[name], x) == Z),
          sorted(encode(x) for x in roots))

values = [[evaluate(poly, x) for x in T] for poly in p]
blocks = [{(x, y) for x, y in zip(T, row)} for row in values]
edges = list(combinations(range(4), 2))
intersections = [blocks[i] & blocks[j] for i, j in edges]
private = [blocks[i] - set().union(*(blocks[j] for j in range(4) if j != i))
           for i in range(4)]
reconstructed = {
    "coefficients": [[encode(c) for c in poly] for poly in p],
    "values": [[encode(y) for y in row] for row in values],
    "blocks": [points(block) for block in blocks],
    "intersections": {f"{i+1}{j+1}": points(s) for (i, j), s in zip(edges, intersections)},
    "private_parts": [points(part) for part in private],
    "pair_sizes": list(map(len, intersections)),
    "pair_sets_mutually_disjoint": all(not (a & b) for a, b in combinations(intersections, 2)),
    "private_sizes": list(map(len, private)),
    "distinct_blocks": len(set(map(frozenset, blocks))) == 4,
    "deleted_points_avoided": all(not (b & deleted) for b in blocks),
    "union_size": len(set().union(*blocks)),
    "common_constant_shift": 4,
    "factorization_coefficients": expanded,
}
check("witness key coverage", sorted(reconstructed), sorted(saved["witness"]))
for name, value in reconstructed.items():
    check("saved witness " + name, value, saved["witness"][name])
for i, row in enumerate(reconstructed["values"]):
    for j, value in enumerate(row):
        check(f"evaluation block {i+1} position {encode(T[j])}", value,
              saved["witness"]["values"][i][j])
degrees = [max(i for i, c in enumerate(poly) if c != Z) for poly in p]
check("degrees", degrees, [0, 3, 3, 3])
check("zero values", [encode(row[0]) for row in values], [4, 4, 6, 6])
check("block sizes", list(map(len, blocks)), [8] * 4)
for name, required in {"pair_sizes": [2]*6, "private_sizes": [2]*4,
                       "pair_sets_mutually_disjoint": True, "distinct_blocks": True,
                       "deleted_points_avoided": True, "union_size": 20}.items():
    check("requirement " + name, reconstructed[name], required)
triple_sizes = [len(set.intersection(*(blocks[i] for i in inds)))
                for inds in combinations(range(4), 3)]
check("all triple intersections empty", triple_sizes, [0] * 4)

failures = [c["name"] for c in checks if not c["pass"]]
out = {"source": SOURCE.name, "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
       "arithmetic": "pairs in F_11[u]/(u^2-2); direct polynomial power sums",
       "scope": "complete L039 witness; no search/reduction audit or actual-label claim",
       "witness": reconstructed, "norms": norms, "degrees": degrees,
       "triple_sizes": triple_sizes, "checks": checks, "failures": failures,
       "summary": {"checks": len(checks), "failures": failures,
                   "evaluations": 32, "pair_sizes": reconstructed["pair_sizes"],
                   "required_pair_sizes": [2]*6, "private_sizes": reconstructed["private_sizes"],
                   "required_private_sizes": [2]*4, "degrees": degrees,
                   "degree_bound": 3, "union_size": reconstructed["union_size"]}}
OUT.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({**out["summary"], "certificate": str(OUT)}))
raise SystemExit(bool(failures))
