#!/usr/bin/env python3
"""Exact arithmetic for L025; cone entry uses the cited approximation theorem."""

from fractions import Fraction as Q


def matrix(rows):
    return [[Q(x) for x in row] for row in rows]


def transpose(a):
    return list(map(list, zip(*a)))


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def linear_combination(*terms):
    n = len(terms[0][1])
    return [[sum(c * a[i][j] for c, a in terms) for j in range(n)] for i in range(n)]


def identity(n):
    return matrix([[i == j for j in range(n)] for i in range(n)])


def f_matrix(a):
    a2 = multiply(a, a)
    return linear_combination((1, multiply(a2, a)), (1, a2), (-2, a), (-1, identity(len(a))))


def polynomial_multiply(a, b):
    result = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def f(x):
    return x**3 + x**2 - 2 * x - 1


def main():
    # Columns of R are E, 2F, -O-2F, P-O-2F+E/2.
    g = matrix([[0, 1, 0, 1], [1, -2, 0, 0], [0, 0, -2, 1], [1, 0, 1, -2]])
    r = matrix([[0, 2, -2, -2], [0, 0, -1, -1], [1, 0, 0, Q(1, 2)], [0, 0, 0, 1]])
    gram = matrix([[-2, 0, 0, 0], [0, 0, -2, 0], [0, -2, 2, 0], [0, 0, 0, Q(-7, 2)]])
    assert multiply(multiply(transpose(r), g), r) == gram

    # Multiplication by a, then by a^2-2, in Q[a]/(f).
    m = matrix([[0, 0, 1], [1, 0, 2], [0, 1, -1]])
    p = linear_combination((1, multiply(m, m)), (-2, identity(3)))
    assert p == matrix([[-2, 1, -1], [0, 0, -1], [1, -1, 1]])
    zero3 = matrix([[0] * 3 for _ in range(3)])
    assert f_matrix(m) == f_matrix(p) == zero3
    b = [row[:3] for row in gram[:3]]
    assert multiply(transpose(p), b) == multiply(b, p)

    d = [row + [Q(0)] for row in p] + [[Q(0)] * 4]
    a = matrix([[1, 2, -2, 5], [Q(1, 2), 0, -1, Q(3, 2)], [Q(1, 2), 0, -2, 2], [0, 0, 0, 0]])
    assert multiply(a, r) == multiply(r, d)
    assert multiply(transpose(a), g) == multiply(g, a)
    assert multiply(a, f_matrix(a)) == matrix([[0] * 4 for _ in range(4)])

    # f(z^2-2)=z^6-5z^4+6z^2-1=f(z)(z^3-z^2-2z+1).
    assert polynomial_multiply([-1, -2, 1, 1], [1, -2, -1, 1]) == [-1, 0, 6, 0, -5, 0, 1]
    assert f(-1) != 0 and f(1) != 0  # The only possible rational roots.
    intervals = [(Q(-2), Q(-3, 2)), (Q(-1, 2), Q(0)), (Q(1), Q(3, 2))]
    assert all(f(lo) * f(hi) < 0 for lo, hi in intervals)
    assert intervals[0][1] ** 2 - 2 == Q(1, 4) > 0

    print("PASS: exact divisor-form isometry; self-adjoint matrix; cubic block and zero complement.")
    print("PASS: irreducible cubic, disjoint root intervals, and positive-eigenvalue permutation.")
    print("Kahler-cone entry is justified by the cited theorem in L025, not by this computation.")


if __name__ == "__main__":
    main()
