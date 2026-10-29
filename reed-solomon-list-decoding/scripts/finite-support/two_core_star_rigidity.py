#!/usr/bin/env python3
"""Exact, bounded projective test for L030's pointed six-column stars."""
import itertools
import json
from pathlib import Path

Q = 137
T = (16, 64, 70, 102, 112, 118, 121)
LEFT_POINT = 16
DEST = tuple(x for x in T if x != LEFT_POINT)


def normalize(v):
    scale = pow(next(x % Q for x in v if x % Q), -1, Q)
    return tuple(x * scale % Q for x in v)


def multiply(a, b):
    return tuple(sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % Q
                 for i in range(2) for j in range(2))


def inverse_projective(a):
    return (a[3], -a[1], -a[2], a[0])


def triple_to_standard(xs):
    a, b, c = xs
    return (b - c, -a * (b - c), b - a, -c * (b - a))


def by_cross_ratio(xs, ys):
    return normalize(multiply(inverse_projective(triple_to_standard(ys)),
                              triple_to_standard(xs)))


def by_linear_equations(xs, ys):
    rows = [[x % Q, 1, -y * x % Q, -y % Q] for x, y in zip(xs, ys)]
    pivots = []
    rank = 0
    for col in range(4):
        pivot = next((i for i in range(rank, 3) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][col], -1, Q)
        rows[rank] = [v * scale % Q for v in rows[rank]]
        for i in range(3):
            if i != rank:
                factor = rows[i][col]
                rows[i] = [(v - factor * w) % Q
                           for v, w in zip(rows[i], rows[rank])]
        pivots.append(col)
        rank += 1
    if rank != 3:
        raise ArithmeticError("Three-point equations do not have rank three")
    free = next(c for c in range(4) if c not in pivots)
    ans = [0] * 4
    ans[free] = 1
    for i, pivot in enumerate(pivots):
        ans[pivot] = -rows[i][free] % Q
    return normalize(ans)


def evaluate(mat, x):
    a, b, c, d = mat
    denominator = (c * x + d) % Q
    return None if denominator == 0 else (a * x + b) * pow(denominator, -1, Q) % Q


def main():
    records, accepted, failures = [], [], []
    for removed in T:
        source = tuple(x for x in T if x != removed)
        anchors = source[:3]
        for images in itertools.permutations(DEST, 3):
            mat = by_cross_ratio(anchors, images)
            second = by_linear_equations(anchors, images)
            determinant = (mat[0] * mat[3] - mat[1] * mat[2]) % Q
            mapped = [evaluate(mat, x) for x in source]
            checks = {
                "independent_constructions_equal": mat == second,
                "determinant_nonzero": determinant != 0,
                "anchor_images_correct": tuple(mapped[:3]) == images,
            }
            for name, passed in checks.items():
                if not passed:
                    failures.append({"removed": removed, "images": images, "check": name})
            is_accepted = None not in mapped and set(mapped) == set(DEST)
            record = {"removed": removed, "source": source, "anchor_images": images,
                      "matrix": mat, "matrix_by_elimination": second,
                      "determinant": determinant, "all_six_images": mapped,
                      "checks": checks, "accepted": is_accepted}
            records.append(record)
            if is_accepted:
                accepted.append(record)
    required = len(T) * 6 * 5 * 4
    expected = [(LEFT_POINT, (1, 0, 0, 1))]
    actual = [(record["removed"], record["matrix"]) for record in accepted]
    if len(records) != required:
        failures.append("candidate count incomplete")
    if actual != expected:
        failures.append("rigidity criterion fails: further accepted maps exist")
    result = {
        "field": Q, "evaluation_set": T, "left_removed": LEFT_POINT,
        "destination": DEST, "required_candidates": required,
        "actual_candidates": len(records), "accepted": accepted,
        "expected_accepted": [{"removed": LEFT_POINT, "matrix": (1, 0, 0, 1)}],
        "failures": failures, "records": records,
        "qualification": "Finite projective test only; the canonical symbolic proof must justify its implication for arbitrary star isomorphisms and full-law coupling.",
    }
    path = Path(__file__).with_name("two-core-star-rigidity.json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Candidates: {len(records)} / required {required}")
    print(f"Accepted (removed, matrix): {actual}; required {expected}")
    print(f"Failures: {failures}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
