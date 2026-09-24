"""Exact rational certificate for L262; no numerical sign decisions."""
from fractions import Fraction as F
from math import factorial as fac


def mul(p, q):
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] += a * b
    return result


b, epsilon = F(1, 4), F(1, 40)
c = [F(1)]
for r in [10 - 2 * epsilon, 10 - epsilon, F(10), 10 + epsilon, 10 + 2 * epsilon]:
    c = mul(c, [r * r, F(1)])
c = mul(c, [(100 + b * b)**2, 200 - 2 * b * b, F(1)])
h = [sum(c[k] * (-1)**(k-l) * F(fac(2*k), fac(k-l)*fac(2*l)*4**(k-l))
         for k in range(l, 8)) for l in range(8)]
expected = [966, 915, 883, 869, 872, 893, 934, 1000]
for l, m in enumerate(expected):
    assert c[l] > 0
    assert m * c[l] <= 1000 * h[l] < (m + 1) * c[l]
    assert h[l] > 0
print('PASS: exact coefficient ratio floors:', expected)
