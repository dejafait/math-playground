"""Independent defining-product and exact-minor audit of L162.

No imports from construction/census scripts or their certificates.
The all-parameter argument is in L162, not inferred from samples here.
"""

import itertools
import json
from pathlib import Path


P = 97
S = (1, 8, 12, 18, 22, 27, 33)
J = (47, 50, 64, 70, 75, 79, 85, 89, 96)
ROWS = {
    "a": ((1, 8), (89, 96), 35),
    "b": ((12, 33), (64, 85), 522),
    "c": ((12, 27), (50, 70), 477),
    "d": ((18, 22), (75, 79), 566),
}
DISPLAYED = {
    "a": [[0, 0, 87, 46, 0, 0, 0], [0, 0, 8, 0, 46, 0, 0],
          [0, 0, 71, 0, 0, 46, 0], [0, 0, 89, 0, 0, 0, 46]],
    "b": [[18, 73, 0, 0, 0, 0, 0], [57, 0, 0, 73, 0, 0, 0],
          [32, 0, 0, 0, 73, 0, 0], [43, 0, 0, 0, 0, 73, 0]],
    "c": [[83, 51, 0, 0, 0, 0, 0], [91, 0, 0, 51, 0, 0, 0],
          [63, 0, 0, 0, 51, 0, 0], [95, 0, 0, 0, 0, 0, 51]],
    "d": [[4, 27, 0, 0, 0, 0, 0], [13, 0, 27, 0, 0, 0, 0],
          [10, 0, 0, 0, 0, 27, 0], [36, 0, 0, 0, 0, 0, 27]],
}
X = [[2, 50, 5, 77, 16, 45, 81], [58, 92, 4, 81, 71, 36, 26]]
Y = [[75, 32, 0, 69, 3, 1, 0], [0, 0, 30, 0, 0, 0, 1]]
failures = []


def require(condition, name):
    if not condition:
        failures.append(name)


def evaluate_product(roots, t):
    value = 1
    for root in roots:
        value = value * (t - root) % P
    return value


def determinant(matrix):
    # Leibniz formula over the integers, independent of row reduction.
    total = 0
    n = len(matrix)
    for perm in itertools.permutations(range(n)):
        term = 1
        for i in range(n):
            term *= matrix[i][perm[i]]
        inversions = sum(perm[i] > perm[j]
                         for i in range(n) for j in range(i + 1, n))
        total += (-1 if inversions % 2 else 1) * term
    return total


all_labels = list(itertools.product(itertools.combinations(S, 2),
                                   itertools.combinations(J, 2)))
maps = {}
labels = {}
supports = {}
for name, (inside, outside, expected_label) in ROWS.items():
    actual_label = all_labels.index((inside, outside))
    require(actual_label == expected_label, f"label {name}")
    roots = sorted(set(J) - set(outside))
    values = [evaluate_product(roots, t) for t in S]
    retained = sorted(set(S) - set(inside))
    anchor = retained[0]
    matrix = []
    for t in retained[1:]:
        row = [0] * len(S)
        row[S.index(t)] = values[S.index(anchor)]
        row[S.index(anchor)] = -values[S.index(t)] % P
        matrix.append(row)
    maps[name] = matrix
    supports[name] = set(inside) | set(outside)
    labels[name] = dict(I=inside, K=outside, actual_label=actual_label,
                        required_label=expected_label, roots=roots,
                        values_on_S=values, anchor=anchor,
                        target_order=retained[1:])
    require(matrix == DISPLAYED[name], f"displayed Q_{name}")
    require(all(values), f"nonzero g_{name} on S")

intersections = {}
for a, b in itertools.combinations(ROWS, 2):
    actual = sorted(supports[a] & supports[b])
    expected = [12] if (a, b) == ("b", "c") else []
    intersections[a + b] = actual
    require(actual == expected, f"support intersection {a}{b}")

identities = []
for i in range(2):
    inputs = {"a": X[i], "b": Y[i],
              "c": [(x + y) % P for x, y in zip(X[i], Y[i])],
              "d": [(x + 26 * y) % P for x, y in zip(X[i], Y[i])]}
    for name, vector in inputs.items():
        residual = [sum(a * b for a, b in zip(row, vector)) % P
                    for row in maps[name]]
        identities.append(dict(index=i, row=name, vector=vector,
                               residual=residual))
        require(residual == [0] * 4, f"identity {name}, index {i}")

minors = []
for a, b, selection, expected in [
    ("a", "b", [0, 1, 2, 3, 4, 5, 7], 158723284464),
    ("c", "d", [0, 1, 2, 3, 5, 6, 7], -70496180091),
]:
    stack = maps[a] + maps[b]
    minor = [stack[i] for i in selection]
    det = determinant(minor)
    require(det == expected, f"integer determinant {a}{b}")
    require(det % P != 0, f"nonzero minor {a}{b}")
    minors.append(dict(pair=a + b, selected_rows=selection, matrix=minor,
                       integer_determinant=det, residue=det % P,
                       certified_rank=7 if det % P else None,
                       required_rank=7))

recovery = [[Y[i][S.index(t)] for i in range(2)] for t in (27, 33)]
require(recovery == [[1, 0], [0, 1]], "Y parameter recovery")
require(26 % P != 0 and 25 % P != 0, "cross-ratio nondegeneracy")
require(len(all_labels) == 756, "original label count")
require(len(set(S + J)) == 16 and all(pow(t, 16, P) == 1 for t in S + J),
        "original order-sixteen subgroup")

certificate = dict(
    method="Independent defining products and integer Leibniz determinants",
    modulus=P, coordinates=S, complement=J, labels=labels,
    support_intersections=intersections, maps=maps, x_vectors=X, y_vectors=Y,
    identities=identities, minors=minors, Y_parameter_recovery=recovery,
    vector_identities_actual=len(identities), vector_identities_required=8,
    scalar_residuals_actual=sum(len(item["residual"]) for item in identities),
    scalar_residuals_required=32, failures=failures,
    scope="Arithmetic only; all-parameter proof is audited in canonical L162.")
path = Path(__file__).with_name("l162-critical-audit.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print("Labels:", [labels[name]["actual_label"] for name in ROWS],
      "; required: [35, 522, 477, 566]")
print("Vector identities:", len(identities), "; required: 8 (32 scalar zeros)")
print("Pair ranks:", [m["certified_rank"] for m in minors], "; required: [7, 7]")
print("Minor residues:", [m["residue"] for m in minors], "; required: nonzero")
print("Failures:", failures)
print("Certificate:", path.relative_to(Path.cwd()))
raise SystemExit(bool(failures))
