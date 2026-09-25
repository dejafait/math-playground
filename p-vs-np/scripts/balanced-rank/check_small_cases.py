"""Exact finite sanity checks for L001; not a substitute for its general proof.

Run from the notebook root:
    python3 scripts/balanced-rank/check_small_cases.py
Only Python's standard library is required.
"""

from fractions import Fraction
from itertools import product


def binary_rank(rows):
    basis = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in basis:
                row ^= basis[pivot]
            else:
                basis[pivot] = row
                break
    return len(basis)


def rational_rank(matrix):
    rows = [[Fraction(entry) for entry in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        pivot = next(
            (i for i in range(rank, len(rows)) if rows[i][column]), None
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        leading = rows[rank][column]
        rows[rank] = [entry / leading for entry in rows[rank]]
        for i in range(rank + 1, len(rows)):
            factor = rows[i][column]
            if factor:
                rows[i] = [
                    entry - factor * base
                    for entry, base in zip(rows[i], rows[rank])
                ]
        rank += 1
        if rank == len(rows):
            break
    return rank


def internal_quadratic(value, width):
    return sum(
        ((value >> i) & 1) * ((value >> j) & 1)
        for i in range(width)
        for j in range(i + 1, width)
    ) % 2


def check_rank_conversion():
    checked = 0
    for width in range(1, 4):
        mask = (1 << width) - 1
        for encoding in range(1 << (width * width)):
            rows = [
                (encoding >> (i * width)) & mask for i in range(width)
            ]
            binary = binary_rank(rows)
            signs = []
            booleans = []
            for a in range(1 << width):
                sign_row = []
                boolean_row = []
                for b in range(1 << width):
                    cross = sum(
                        ((a >> i) & 1) * (rows[i] & b).bit_count()
                        for i in range(width)
                    ) % 2
                    sign = (-1) ** cross
                    sign_row.append(sign)
                    scaled = sign * (-1) ** (
                        internal_quadratic(a, width)
                        + internal_quadratic(b, width)
                    )
                    boolean_row.append((1 - scaled) // 2)
                signs.append(sign_row)
                booleans.append(boolean_row)
            assert rational_rank(signs) == 2 ** binary
            assert rational_rank(booleans) >= 2 ** binary - 1
            checked += 1
    print(f"PASS: exact sign-rank and 0/1-rank checks for {checked} binary matrices (widths 1–3).")


def check_gate_encodings():
    checked = 0
    for u, v, z in product((False, True), repeat=3):
        and_cnf = ((not z) or u) and ((not z) or v) and (
            z or (not u) or (not v)
        )
        or_cnf = (z or (not u)) and (z or (not v)) and (
            (not z) or u or v
        )
        assert and_cnf == (z == (u and v))
        assert or_cnf == (z == (u or v))
        checked += 2
    for u, z in product((False, True), repeat=2):
        not_cnf = ((not z) or (not u)) and (z or u)
        assert not_cnf == (z == (not u))
        checked += 1
    for u, v in product((False, True), repeat=2):
        assert ((u or v) and not (u and v)) == (u != v)
    print(f"PASS: all {checked} gate-equivalence valuations and all 4 XOR input pairs.")


if __name__ == "__main__":
    check_rank_conversion()
    check_gate_encodings()
