"""Exact finite permutation certificate for the approved two-auxiliary test.

The field-to-group proof is in L055; this script certifies its finite groups,
all orbital maps, full compositum degrees, and exact rational image rank.
No numerical roots, class groups, external backend or GRH are used.
"""
from fractions import Fraction
from itertools import permutations, product
from math import isqrt
from pathlib import Path
import json

P = 11
INF = 11
IDENTITY = tuple(range(12))
failures = []


def require(label, condition):
    if not condition:
        failures.append(label)


def action(m):
    a, b, c, d = m
    out = []
    for x in range(12):
        num, den = (a, c) if x == INF else ((a*x+b) % P, (c*x+d) % P)
        out.append(INF if den == 0 else num*pow(den, -1, P) % P)
    return tuple(out)


def parity(s):
    return sum(s[i] > s[j] for i in range(len(s)) for j in range(i+1, len(s))) % 2


def compose(s, t):
    return tuple(s[t[i]] for i in range(len(s)))


def generated(gens):
    seen, queue = {IDENTITY}, [IDENTITY]
    for s in queue:
        for t in gens:
            z = compose(t, s)
            if z not in seen:
                seen.add(z)
                queue.append(z)
    return seen


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    r, pivots = 0, []
    for c in range(len(a[0])):
        i = next((i for i in range(r, len(a)) if a[i][c]), None)
        if i is None:
            continue
        a[r], a[i] = a[i], a[r]
        p = a[r][c]
        a[r] = [x/p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x-q*y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
    return r, pivots, [[str(x) for x in row] for row in a]


rows = []
for m in product(range(P), repeat=4):
    first = next((x for x in m if x), None)
    det = (m[0]*m[3]-m[1]*m[2]) % P
    if first != 1 or det == 0:
        continue
    s = action(m)
    det_parity = 0 if pow(det, 5, P) == 1 else 1
    require("determinant/sign agreement", parity(s) == det_parity)
    rows.append({"matrix": list(m), "permutation": list(s), "parity": det_parity})
rows.sort(key=lambda row: row["permutation"])
all_pgl = {tuple(row["permutation"]) for row in rows}
psl = {tuple(row["permutation"]) for row in rows if row["parity"] == 0}
u, v = action((1, 1, 0, 1)), action((1, 0, 1, 1))
require("PGL order and faithfulness", len(rows) == len(all_pgl) == 1320)
require("PSL order", len(psl) == 660)
require("upper/lower elementary generation", generated([u, v]) == psl)
# D=diag(2,6) in SL2(F11): [D,u(1)]=u(3), [D,v(1)]=v(2).
comm_u, comm_v = action((1, 3, 0, 1)), action((1, 0, 2, 1))
require("perfectness generators", generated([comm_u, comm_v]) == psl)
d = action((2, 0, 0, 6))
dinv = action((6, 0, 0, 2))
require("upper commutator formula", compose(compose(compose(d, u), dinv), action((1, 10, 0, 1))) == comm_u)
require("lower commutator formula", compose(compose(compose(d, v), dinv), action((1, 0, 10, 1))) == comm_v)

s3 = list(permutations(range(3)))
joint = [(i, j) for i, row in enumerate(rows) for j, t in enumerate(s3)
         if row["parity"] == parity(t)]
require("joint fiber-product order", len(joint) == 3960)

X = list(product(range(12), range(3)))


def all_orbits(aux):
    n = 12 if aux == "K96" else 3
    unseen = set(product(range(36), range(n)))
    orbits = []
    while unseen:
        x, y = min(unseen)
        a, b = X[x]
        orbit = set()
        for i, j in joint:
            s, t = rows[i]["permutation"], s3[j]
            xx = 3*s[a]+t[b]
            yy = s[y] if aux == "K96" else t[y]
            orbit.add((xx, yy))
        require("orbital disjointness", orbit <= unseen)
        unseen -= orbit
        matrix = [[int((xx, yy) in orbit) for yy in range(n)] for xx in range(36)]
        orbits.append({"representative": [x, y], "size": len(orbit),
                       "pairs": [list(z) for z in sorted(orbit)], "map_matrix": matrix})
    return orbits


ok, of = all_orbits("K96"), all_orbits("F")
require("all K96 compositum orbits", [z["size"] for z in ok] == [36, 396])
require("all F compositum orbits", [z["size"] for z in of] == [36, 72])
for aux, orbits, n, coordinate in [("K96", ok, 12, 0), ("F", of, 3, 1)]:
    for k, orbital in enumerate(orbits):
        expected = [[int((X[x][coordinate] == y) == (k == 0))
                     for y in range(n)] for x in range(36)]
        require(f"full {aux} orbital {k} is coordinate incidence", orbital["map_matrix"] == expected)
all_maps = ok+of
matrix = [sum((z["map_matrix"][i] for z in all_maps), []) for i in range(36)]
actual, pivots, rref = rank(matrix)
require("complete-map rank", actual == 14)
require("required target dimension", len(X) == 36)
witness = [0]*36
witness[0], witness[1], witness[3], witness[4] = 1, -1, -1, 1
require("nonzero annihilator", any(witness))
require("annihilator of every column", all(sum(witness[i]*matrix[i][j] for i in range(36)) == 0 for j in range(len(matrix[0]))))
require("annihilator separates target basis vector", witness[0] == 1)

dm = -307926804295486824275116956724109113198514489839954427904
dh = -41229056
square_roots = [isqrt(-z//11) for z in [dm, dh]]
require("both square classes are -11", all(z == -11*r*r for z, r in zip([dm, dh], square_roots)))
certificate = {
    "field_inputs": {"canonical_line_action": "L050", "models_degrees_discriminants": "L051",
                     "ramification_index_eleven": "L052", "cubic_degree": "L054",
                     "field_to_joint_group_proof": "lemmas/L055-ninety-six-two-auxiliary-relation-obstruction.md"},
    "discriminants": {"m": dm, "h": dh, "square_class": -11, "square_roots": square_roots},
    "projective_group": {"all_normalized_matrices_and_permutations": rows, "PGL_order": len(rows),
                         "PSL_order": len(psl), "elementary_generated_order": len(generated([u, v])),
                         "commutator_generated_order": len(generated([comm_u, comm_v]))},
    "joint_group": {"S3_permutations": [list(t) for t in s3], "all_index_pairs": [list(z) for z in joint],
                    "order": len(joint), "target_points": [list(z) for z in X]},
    "all_composita": {"K96": ok, "F": of,
                      "factor_degrees_over_L96": {"K96": [1, 11], "F": [1, 2]},
                      "factor_degrees_over_Q": {"K96": [36, 396], "F": [36, 72]},
                      "qualification": "Degrees and embedding maps certified by exact Galois-set orbits, not polynomial factor guesses."},
    "coverage": {"complete_map_matrix": matrix, "actual_rank": actual, "required_rank": 36,
                 "missing_dimension": 36-actual, "pivot_columns": pivots, "exact_rref": rref,
                 "annihilator": witness, "basis_vector_separated": 0,
                 "decision": "NO generalized norm relation for this auxiliary pair"},
    "failures": failures,
}
path = Path(__file__).with_name("coverage-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"PGL/PSL/joint orders: {len(rows)}/{len(psl)}/{len(joint)}")
print(f"All compositum degrees over L96: K96 [1,11]; F [1,2]")
print(f"Complete-map rank: actual {actual}, required 36; missing {36-actual}")
print(f"Failures: {failures}; full certificate: {path.relative_to(Path.cwd())}")
if failures:
    raise SystemExit(1)
