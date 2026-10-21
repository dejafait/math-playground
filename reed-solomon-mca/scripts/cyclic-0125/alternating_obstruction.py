"""Exact extension-stable necessary-condition certificate; no weight sampling."""

import itertools
import json
from pathlib import Path

P = 97
PAIRS = list(itertools.combinations(range(8), 2))
ROW_PAIRS = list(itertools.combinations(range(4), 2))
GENERATORS = [w for w in range(1, P)
              if pow(w, 16, P) == 1 and pow(w, 8, P) != 1]


def polynomial(w):
    c = [1]
    for a in (0, 1, 2, 5):
        x = pow(w, a, P)
        d = [0] * (len(c) + 1)
        for j, v in enumerate(c):
            d[j] = (d[j] - x * v) % P
            d[j + 1] = (d[j + 1] + v) % P
        c = d
    return c


def determinant(A):
    """Leibniz formula, independent of the rank routine below."""
    total = 0
    for perm in itertools.permutations(range(len(A))):
        inversions = sum(perm[i] > perm[j]
                         for i in range(len(A)) for j in range(i + 1, len(A)))
        term = (-1) ** inversions
        for i, j in enumerate(perm):
            term *= A[i][j]
        total += term
    return total % P


def rank(A):
    A = [row[:] for row in A]
    k = 0
    for j in range(len(A[0])):
        pivot = next((i for i in range(k, len(A)) if A[i][j]), None)
        if pivot is None:
            continue
        A[k], A[pivot] = A[pivot], A[k]
        inverse = pow(A[k][j], -1, P)
        A[k] = [v * inverse % P for v in A[k]]
        for i in range(k + 1, len(A)):
            multiple = A[i][j]
            A[i] = [(x - multiple * y) % P for x, y in zip(A[i], A[k])]
        k += 1
    return k


def block(c, h):
    def coefficient(i):
        return c[i] if 0 <= i <= 4 else 0
    columns = [(j, k) for j, k in PAIRS if j + k == h]
    matrix = [[(coefficient(j - r) * coefficient(k - s)
                - coefficient(k - r) * coefficient(j - s)) % P
               for j, k in columns] for r, s in ROW_PAIRS]
    return columns, matrix


def main():
    coefficients = {w: polynomial(w) for w in GENERATORS}
    failures = []
    blocks = []
    for h in range(1, 14):
        matrices = {w: block(coefficients[w], h)[1] for w in GENERATORS}
        columns = block(coefficients[GENERATORS[0]], h)[0]
        size = len(columns)
        selected = next((rows for rows in itertools.combinations(range(6), size)
                         if all(determinant([matrices[w][i] for i in rows])
                                for w in GENERATORS)), None)
        if selected is None:
            failures.append(f"No common nonsingular row selection for h={h}")
            continue
        blocks.append({"h": h, "columns": columns, "selected_rows": selected,
                       "by_generator": {
                           w: {"matrix": matrices[w],
                               "minor": [matrices[w][i] for i in selected],
                               "determinant": determinant([matrices[w][i] for i in selected])}
                           for w in GENERATORS}})

    direct = {}
    for w in GENERATORS:
        M = []
        scaling_verified = True
        for t in range(16):
            # Rebuild P_t independently by multiplication at its actual roots.
            c = [1]
            for a in (0, 1, 2, 5):
                x = pow(w, (a + t) % 16, P)
                d = [0] * (len(c) + 1)
                for j, v in enumerate(c):
                    d[j] = (d[j] - x * v) % P
                    d[j + 1] = (d[j + 1] + v) % P
                c = d
            R = [[0] * r + c + [0] * (3 - r) for r in range(4)]
            for index, (r, s) in enumerate(ROW_PAIRS):
                row = [(R[r][j] * R[s][k] - R[r][k] * R[s][j]) % P
                       for j, k in PAIRS]
                M.append(row)
                for col, (j, k) in enumerate(PAIRS):
                    columns, B = block(coefficients[w], j + k)
                    expected = B[index][columns.index((j, k))] * pow(w, ((8 + r + s - j - k) * t) % 16, P) % P
                    scaling_verified &= row[col] == expected
        actual_rank = rank(M)
        direct[w] = {"matrix": M, "rank": actual_rank,
                     "required_rank": 28, "scaling_verified": scaling_verified}
        if actual_rank != 28 or not scaling_verified:
            failures.append(f"Direct verification failed for generator {w}")

    report = {"modulus": P, "generators": GENERATORS,
              "coefficients_ascending": coefficients, "row_pairs": ROW_PAIRS,
              "blocks": blocks, "direct_checks": direct,
              "proof_certificate": {
                  "generators": GENERATORS, "coefficients": coefficients,
                  "row_pairs": ROW_PAIRS,
                  "minors": [{"h": b["h"], "columns": b["columns"],
                              "rows": b["selected_rows"],
                              "determinants": [b["by_generator"][w]["determinant"]
                                               for w in GENERATORS]}
                             for b in blocks]},
              "failures": failures,
              "conclusion": "Full rank 28 for all eight generators" if not failures else "FAILED"}
    path = Path(__file__).with_name("alternating-obstruction-result.json")
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Result: {report['conclusion']}; required rank 28; failures: {failures}")
    print(f"Full certificate: {path}")
    print("Coefficients:", coefficients)
    print("h | selected row indices | determinants in generator order")
    for entry in blocks:
        print(entry["h"], entry["selected_rows"],
              [entry["by_generator"][w]["determinant"] for w in GENERATORS])
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
