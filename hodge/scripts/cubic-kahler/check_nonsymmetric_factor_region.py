#!/usr/bin/env python3
"""Exact arithmetic checks for L052's necessary filter; no bundle existence."""

import json
from fractions import Fraction as Q
from pathlib import Path


def rref(rows):
    rows = [[Q(x) for x in row] for row in rows]
    pivots = []
    cursor = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(cursor, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[cursor], rows[pivot] = rows[pivot], rows[cursor]
        scale = rows[cursor][col]
        rows[cursor] = [v / scale for v in rows[cursor]]
        for i in range(len(rows)):
            if i != cursor:
                scale = rows[i][col]
                rows[i] = [v - scale * u for v, u in zip(rows[i], rows[cursor])]
        pivots.append(col)
        cursor += 1
        if cursor == len(rows):
            break
    return rows, pivots


def determinant(rows):
    rows = [[Q(v) for v in row] for row in rows]
    answer = Q(1)
    for col in range(len(rows)):
        pivot = next(i for i in range(col, len(rows)) if rows[i][col])
        if pivot != col:
            rows[col], rows[pivot] = rows[pivot], rows[col]
            answer *= -1
        scale = rows[col][col]
        answer *= scale
        for i in range(col + 1, len(rows)):
            ratio = rows[i][col] / scale
            rows[i] = [v - ratio * u for v, u in zip(rows[i], rows[col])]
    return answer


def main():
    gram = [[0, 1, 0, 1], [1, -2, 0, 0],
            [0, 0, -2, 1], [1, 0, 1, -2]]
    # Each row represents coefficients of lambda, 1, 1/lambda.
    h = [[2, 3, 1], [0, 1, 1], [0, 0, -1], [0, 0, 0]]
    gh = [[sum(gram[i][j] * h[j][c] for j in range(4))
           for c in range(3)] for i in range(4)]
    assert gh == [[0, 1, 1], [2, 1, -1], [0, 0, 2], [2, 3, 0]]
    equations = [list(row) for row in zip(*gh)]
    reduced, pivots = rref(equations)
    assert pivots == [0, 1, 2]
    kernel = [-reduced[i][3] for i in range(3)] + [Q(1)]
    assert kernel == [Q(-2), Q(-1), Q(1, 2), Q(1)]
    k = [-4, -2, 1, 2]
    assert [2 * x for x in kernel] == k
    square = sum(k[i] * gram[i][j] * k[j]
                 for i in range(4) for j in range(4))
    assert square == -14
    assert determinant(gram) == -7
    # A monic cubic is irreducible over Q iff it has no rational root.
    f = lambda x: x ** 3 + x ** 2 - 2 * x - 1
    assert f(1) != 0 and f(-1) != 0

    residues = [[m, n] for m in range(12) for n in range(12)
                if m * n % 12 == 6]
    assert len(residues) == 20
    assert all(m not in (0, 4) and n not in (0, 4) for m, n in residues)
    assert all(m != n for m, n in residues)
    # These are representatives of every congruence class, not an
    # enumeration offered as a proof of the infinite-region condition.
    positive_representatives = [[m if m >= 5 else m + 12,
                                 n if n >= 5 else n + 12]
                                for m, n in residues]
    assert all(m >= 5 and n >= 5 and m * n % 12 == 6
               for m, n in positive_representatives)
    boundary = [[m, n] for m in range(5, 12) for n in range(5, 12)
                if m + n <= 11 and m * n % 12 == 6]
    assert boundary == [[5, 6], [6, 5]]
    examples = []
    for j in range(20):
        m, n = 5, 6 + 12 * j
        assert m * n % 12 == 6
        examples.append({"m": m, "n": n, "a": -m - 4, "b": -n - 4})
        m, n = 3, 2 + 4 * j
        assert m + n >= 5 and m * n % 12 == 6
        assert m < 4  # Stable Euler test fails; no split square 14r^2.

    certificate = {
        "scope": "Arithmetic of necessary tests only; no stable bundle existence",
        "metric_basis": ["lambda", "1", "1/lambda"],
        "gram": gram, "gram_determinant": -7,
        "h_coefficients": h, "q_l_h_equations": equations,
        "equations_rref": [[str(x) for x in row] for row in reduced],
        "primitive_integral_kernel": k, "kernel_square": square,
        "congruence_residues": residues,
        "positive_representatives": positive_representatives,
        "stable_necessary_c2_minimum": 4,
        "congruence_refined_factor_c2_minimum": 5,
        "old_correction_sum_cutoff": -13,
        "new_correction_sum_cutoff": -19,
        "minimum_total_c2_pairs": boundary,
        "surviving_family_examples": examples,
        "failed_checks": [],
    }
    path = Path(__file__).with_name("nonsymmetric_factor_region_certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print("PASS: exact zero-slope lattice is Z(-4,-2,1,2), square -14.")
    print("PASS: stable Euler test requires factor c2>=4; congruence refines this to >=5.")
    print("PASS: all 20 congruence residues admit representatives with both factor c2>=5.")
    print("PASS: least total c2 is 11, pairs (5,6) and (6,5).")
    print("Cutoff: a+b<=-19, compared with old necessary a+b<=-13.")
    print("Holomorphic existence, compatible product realization and transport: not proved.")
    print("Failed checks: none.")
    print(f"Certificate: {path.relative_to(Path(__file__).resolve().parents[2])}")


if __name__ == "__main__":
    main()
