#!/usr/bin/env python3
"""Check the finite certificate and regress the quantitative specialization.

Run from the Collatz notebook: python3 scripts/mod27-hitting/check_hitting.py.
The universal proof is in L013. Finite orbit checks do not prove its bound.
Only Python's standard library is used; no external source code is run.
"""

import json
import math
from fractions import Fraction
from pathlib import Path


LEVELS = (
    (4, 8, 17, 22),
    (2, 5, 11, 14, 23),
    (1, 7, 10, 16, 19, 25),
)
HEIGHT = {r: h for h, residues in enumerate(LEVELS) for r in residues}
WEIGHT = (16, 28, 49)
CONTRACTION = Fraction(20, 21)


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def stopped(n):
    return n <= 2 or n % 27 == 20


def valuation_two(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def rank(n):
    assert n > 0
    if stopped(n):
        return (0, 0)
    if n % 3 == 0:
        return (3, n)
    if n % 27 == 26:
        return (1, valuation_two(n + 1) + 2)
    if n % 27 == 13:
        return (1, 1)
    return (2, WEIGHT[HEIGHT[n % 27]] * n)


def check_edges():
    expected = {r for r in range(27) if r % 3 and r not in (13, 20, 26)}
    assert set(HEIGHT) == expected
    rows = []
    internal = []
    exits = []
    for residue in sorted(HEIGHT):
        destinations = []
        for parity in (0, 1):
            image = (14 * ((3 * residue + 1) if parity else residue)) % 27
            destinations.append(image)
            # Representative modulo 54 checks actual integer parity independently.
            representative = residue + (27 if residue % 2 != parity else 0)
            assert shortcut(representative) % 27 == image
            assert image % 3 != 0
            edge = [residue, image, parity]
            if image not in HEIGHT:
                assert image in (13, 20, 26)
                exits.append(edge)
                continue
            assert 2 * parity - 1 <= HEIGHT[residue] - HEIGHT[image]
            before, after = WEIGHT[HEIGHT[residue]], WEIGHT[HEIGHT[image]]
            if parity:
                # Clearing 42n preserves the actual +1 term.
                coefficient = 40 * before - 63 * after
                value_at_three = 3 * coefficient - 21 * after
                assert coefficient >= 0 and value_at_three >= 0
            else:
                assert 40 * before - 21 * after >= 0
            internal.append(edge)
        rows.append([residue, HEIGHT[residue], *destinations])
    assert len(internal) == 25 and len(exits) == 5
    assert Fraction(7, 8) < CONTRACTION
    assert 14 * 26 % 27 == 13
    assert 14 * (3 * 26 + 1) % 27 == 26
    assert 14 * 13 % 27 == 20
    assert 14 * (3 * 13 + 1) % 27 == 20
    # Exact rational bounds used after the phase estimates in L013.
    assert Fraction(1225, 144) < 9
    assert 3 + Fraction(41, 2) < 24
    assert 8 + Fraction(53, 192) * Fraction(41, 2) < 14
    return rows, internal, exits


def check_regressions(limit=20000):
    largest_time = (0, 1)
    maximum_core_ratio = Fraction(0)
    for start in range(1, limit + 1):
        n = start
        steps = 0
        prefix = 0
        entry = None
        tail_entry = None
        core_edges = 0
        while not stopped(n):
            before = rank(n)
            after_n = shortcut(n)
            after = rank(after_n)
            assert after < before
            if before[0] == 3:
                prefix += 1
                if after[0] != 3:
                    entry = after_n
            elif entry is None:
                entry = n
            if before[0] == 2 and after[0] == 2:
                core_edges += 1
                ratio = Fraction(after[1], before[1])
                assert ratio <= CONTRACTION
                maximum_core_ratio = max(maximum_core_ratio, ratio)
            if after[0] == 1 and tail_entry is None:
                tail_entry = after_n
            if before[0] == 1 and tail_entry is None:
                tail_entry = n
            n = after_n
            steps += 1
            assert steps <= math.ceil(24 * math.log(start) + 14)
        if start >= 3:
            assert prefix <= math.log(start) / math.log(2) + 1
            if entry is not None:
                assert 3 * entry <= 5 * start
            if tail_entry is not None:
                assert tail_entry <= 9 * start
            assert core_edges <= math.log(Fraction(245, 192) * start) / math.log(Fraction(21, 20))
        largest_time = max(largest_time, (steps, start))
    return {
        "starts_checked": limit,
        "largest_hitting_time": largest_time[0],
        "a_start_attaining_it": largest_time[1],
        "largest_observed_internal_core_ratio": str(maximum_core_ratio),
    }


def check_arithmetic_loops():
    exponents = (0, 1, 2, 3, 20, 100, 1024)
    for exponent in exponents:
        start = 27 * (1 << exponent) - 1
        n = start
        for index in range(exponent):
            assert n % 27 == 26 and n % 2 == 1
            assert valuation_two(n + 1) == exponent - index
            assert n + 1 == 27 * 3**index * 2 ** (exponent - index)
            n = shortcut(n)
        assert n % 27 == 26 and n % 2 == 0
        assert valuation_two(n + 1) == 0
        n = shortcut(n)
        assert n % 27 == 13
        assert shortcut(n) % 27 == 20
        assert exponent + 2 <= math.ceil(24 * math.log(start) + 14)
    return list(exponents)


def main():
    rows, internal, exits = check_edges()
    result = {
        "scope": "finite exact coefficient checks and regressions, not the universal proof",
        "constants": {"A": 24, "B": 14, "M": 2, "logarithm": "natural"},
        "table_columns": ["residue", "h", "even_image", "odd_image"],
        "modular_table": rows,
        "internal_core_edges": len(internal),
        "core_exit_edges": exits,
        "all_integer_inequalities": "PASS: every internal edge, with the positive additive term",
        "phase_regressions": check_regressions(),
        "residue_26_loop_exponents": check_arithmetic_loops(),
    }
    Path(__file__).with_name("result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "modular_table"}, indent=2))


if __name__ == "__main__":
    main()
