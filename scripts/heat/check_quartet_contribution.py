#!/usr/bin/env python3
"""Exact finite polynomial checks for Lemma 65; no zeta zero computations."""
from fractions import Fraction as F
from itertools import product


def mul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, u in enumerate(p):
        for j, v in enumerate(q):
            r[i + j] += u * v
    return r


def derivative(p):
    return [i * p[i] for i in range(1, len(p))]


def evaluate(p, x):
    r = F(0)
    for c in reversed(p):
        r = r * x + c
    return r


def contribution(x, a, b, m):
    d = x*x - a*a + b*b
    return 8*m*x*d / (d*d + 4*a*a*b*b)


def main():
    count = 0
    for x, a, b, m in product(
        map(F, [-5, -4, -3, -1, 1, 3, 4, 5]),
        [F(1, 2), F(3), F(5)],
        [F(1, 3), F(3), F(5)], [1, 2, 3]
    ):
        q = [(a*a + b*b)**2, F(0), -2*(a*a - b*b), F(0), F(1)]
        p = [-x*x, F(0), F(1)]
        for _ in range(m):
            p = mul(p, q)
        dp = derivative(p)
        assert evaluate(p, x) == 0
        assert evaluate(dp, x) != 0
        actual = evaluate(derivative(dp), x) / evaluate(dp, x) - 1/x
        expected = contribution(x, a, b, m)
        assert actual == expected
        sign = lambda t: (t > 0) - (t < 0)
        assert sign(actual) == sign(x) * sign(x*x - a*a + b*b)
        count += 1
    assert [contribution(F(x), F(5), F(3), 1) for x in [3, 4, 5]] == [F(-168, 949), F(0), F(40, 109)]
    print(f'Passed {count} exact polynomial and sign checks, plus three stated examples.')


if __name__ == '__main__':
    main()
