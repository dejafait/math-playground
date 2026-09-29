#!/usr/bin/env python3
"""Exact checks for L031's spin-block certificate; not a cycle test.

The six-dimensional split Clifford model checks the nonzero vector
block and its inverse-pairing contraction. The sign table checks the
three-factor rescaling. L031 proves the assertions for the full even
Clifford algebra, its actual polarization, and arbitrary auxiliary v_0.
No large Kuga--Satake matrices or numerical Hodge computations are used.
"""

from fractions import Fraction
from itertools import product


def multiply(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b)))
         for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][c]
        a[r] = [x / divisor for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def exterior_operator(k, contraction=False):
    a = [[0] * 8 for _ in range(8)]
    for mask in range(8):
        occupied = bool(mask & (1 << k))
        if occupied != contraction:
            continue
        target = mask ^ (1 << k)
        a[target][mask] = (-1) ** (mask & ((1 << k) - 1)).bit_count()
    return a


def main():
    identity = [[int(i == j) for j in range(8)] for i in range(8)]
    wedge = [exterior_operator(k) for k in range(3)]
    contraction = [exterior_operator(k, True) for k in range(3)]
    gamma = [
        [[wedge[k][i][j] + s * contraction[k][i][j]
          for j in range(8)] for i in range(8)]
        for s in (1, -1) for k in range(3)
    ]
    signs = [1] * 3 + [-1] * 3
    for a in range(6):
        for b in range(6):
            ab, ba = multiply(gamma[a], gamma[b]), multiply(gamma[b], gamma[a])
            assert all(
                ab[i][j] + ba[i][j]
                == 2 * int(a == b) * signs[a] * identity[i][j]
                for i in range(8) for j in range(8)
            )

    # The last three generators square to -1. Multiplying them by i
    # normalizes all six squares to +1; the normalized volume is -i Q.
    volume = identity
    for matrix in gamma:
        volume = multiply(volume, matrix)
    assert multiply(volume, volume) == identity
    for matrix in gamma:
        ab, ba = multiply(volume, matrix), multiply(matrix, volume)
        assert all(ab[i][j] == -ba[i][j] for i in range(8) for j in range(8))
    assert sum(volume[i][i] for i in range(8)) == 0

    even = [m for m in range(8) if m.bit_count() % 2 == 0]
    odd = [m for m in range(8) if m.bit_count() % 2 == 1]
    block = [[matrix[i][j] for i in even for j in odd] for matrix in gamma]
    assert rank(block) == 6
    tensor = [
        [sum(signs[k] * block[k][i] * block[k][j] for k in range(6))
         for j in range(16)]
        for i in range(16)
    ]
    assert tensor[0][5] == 2
    assert sum(bool(x) for row in tensor for x in row) == 24

    triples = list(product((1, -1), repeat=3))
    alpha = (1, 1, 1)
    opposite = lambda e: tuple(-x for x in e)
    weight = {e: Fraction(1) for e in triples}
    weight[alpha] = Fraction(2)
    weight[opposite(alpha)] = Fraction(1, 2)
    assert all(weight[e] * weight[opposite(e)] == 1 for e in triples)
    delta = (-1, 1, 1)
    eta = opposite(delta)
    destinations = [
        tuple(-x if i == k else x for i, x in enumerate(delta))
        for k in range(3)
    ]
    assert [k for k, e in enumerate(destinations) if e == alpha] == [0]
    assert (weight[alpha] * weight[eta]) ** 2 == 4

    print("PASS: exact six-generator Clifford relations and normalized volume signs")
    print("PASS: vector block rank 6; inverse-pairing tensor has 24 nonzero entries")
    print("PASS: four dual sign pairs preserved; only T_1 reaches the selected block")
    print("PASS: projected tensor weight 4 under g_2, versus invariant weight 1")
    print("Scope: split-model checks; full tensor and choice independence are proved in L031")


if __name__ == "__main__":
    main()
