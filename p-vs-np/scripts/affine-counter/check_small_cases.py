#!/usr/bin/env python3
"""Finite checks for L004; not a substitute for its all-width proof."""

from math import comb


def gf2_rank(vectors):
    """Rank of binary vectors packed as nonnegative integers."""
    pivots = {}
    for vector in vectors:
        while vector:
            leading = vector.bit_length() - 1
            if leading in pivots:
                vector ^= pivots[leading]
            else:
                pivots[leading] = vector
                break
    return len(pivots)


def check_width(width):
    period = 1 << width
    dimension = period // 2

    # The c-th bit of this integer is the value of the top-bit function at c.
    function = ((1 << dimension) - 1) << dimension
    differences = []
    for _ in range(dimension + 1):
        differences.append(function)
        shift = (function >> 1) | ((function & 1) << (period - 1))
        function ^= shift
    assert differences[-1] == (1 << period) - 1
    assert function == 0
    rank = gf2_rank(differences)
    assert rank == dimension + 1

    # Compute the encoding directly, without using the affine recurrence.
    vectors = [
        sum((comb(counter, k) & 1) << (k - 1)
            for k in range(1, min(counter, dimension) + 1))
        for counter in range(period)
    ]
    coordinate_mask = (1 << dimension) - 1
    for counter, vector in enumerate(vectors):
        affine_next = vector ^ ((vector << 1) & coordinate_mask) ^ 1
        assert affine_next == vectors[(counter + 1) % period]
        for bit in range(width):
            decoded = (vector >> ((1 << bit) - 1)) & 1
            assert decoded == (counter >> bit) & 1

    return period, dimension, rank


def main():
    print("w  states  lift_dimension  difference_rank  result")
    for width in range(1, 9):
        period, dimension, rank = check_width(width)
        print(f"{width}  {period:6}  {dimension:14}  {rank:15}  PASS")
    print("All transitions, cyclic wraps, decoded bits, and difference ranks passed.")
    print("Finite checks only; the all-width dimension bound is proved in L004.")


if __name__ == "__main__":
    main()
