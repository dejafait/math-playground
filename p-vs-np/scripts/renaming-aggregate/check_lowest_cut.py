#!/usr/bin/env python3
"""Exact small checks of the full S_i recurrence in the fixed-length block algebra."""
import json
from pathlib import Path


def add(*polynomials):
    result = set()
    for polynomial in polynomials:
        result.symmetric_difference_update(polynomial)
    return result


def multiply(left, right):
    result = set()
    for u in left:
        for v in right:
            word = u + v
            if word in result:
                result.remove(word)
            else:
                result.add(word)
    return result


def rename(polynomial, bit):
    return {tuple(block ^ bit for block in word) for word in polynomial}


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def run(n):
    # Block mask U denotes the literal n-letter word a_U; equal block
    # length makes concatenation injective in the original free algebra.
    p = {(0,), (0, 0)}
    s = p
    stages = []
    for i in range(1, n + 1):
        bit = 1 << (i - 1)
        rp = rename(p, bit)
        s = add(multiply(rename(s, bit), p), multiply(s, p),
                multiply(multiply(s, rp), p))
        stages.append({"i": i, "support_size": len(s),
                       "minimum_block_degree": min(map(len, s)),
                       "maximum_block_degree": max(map(len, s))})
    low = {word for word in s if len(word) == n + 1}
    expected = {
        tuple(mask & ~((1 << j) - 1) for j in range(n + 1))
        for mask in range(1 << n)
    }
    masks = list(range(0, 1 << n, 2))  # bit 1 (index zero) absent
    suffixes = [tuple(mask & ~((1 << j) - 1)
                      for j in range(1, n + 1)) for mask in masks]
    matrix = [[int((mask,) + suffix in s) for suffix in suffixes]
              for mask in masks]
    row_bits = [sum(value << j for j, value in enumerate(row))
                for row in matrix]
    checks = {
        "no_lower_degree": min(map(len, s)) == n + 1,
        "complete_lowest_support": low == expected,
        "suffixes_distinct": len(set(suffixes)) == len(masks),
        "identity_matrix": all(value == int(i == j)
                               for i, row in enumerate(matrix)
                               for j, value in enumerate(row)),
        "rank_threshold": rank(row_bits) == 2 ** (n - 1),
    }
    return {"n": n, "letter_degree": n * (n + 1), "cut": n,
            "required_rank": 2 ** (n - 1), "actual_rank": rank(row_bits),
            "stages": stages, "checks": checks,
            "row_masks": masks, "column_suffixes": suffixes,
            "complete_selected_matrix": matrix,
            "complete_lowest_support": sorted(low),
            "complete_full_support": sorted(s)}


def main():
    cases = [run(n) for n in range(1, 5)]
    failures = [{"n": case["n"], "check": name}
                for case in cases for name, passed in case["checks"].items()
                if not passed]
    certificate = {
        "encoding": "Each integer block is a subset bitmask for a_U; omitted words have coefficient zero in F2.",
        "scope": "Exact finite checks only; the all-size proof is in L100.",
        "cases": cases, "failures": failures,
    }
    path = Path(__file__).with_name("lowest-cut-certificate.json")
    path.write_text(json.dumps(certificate, separators=(",", ":")) + "\n")
    for case in cases:
        print(f'n={case["n"]}: degree={case["letter_degree"]}, cut={case["cut"]}, '
              f'rank={case["actual_rank"]}, required={case["required_rank"]}, '
              f'full support={len(case["complete_full_support"])}, '
              f'checks={all(case["checks"].values())}')
    print(f"failures={failures}; certificate={path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
