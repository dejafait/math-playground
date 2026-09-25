"""Exact checks for the L007 witness; the uniform upper bound is a proof."""

from itertools import combinations
from math import comb


P = 17
DOMAIN = tuple(range(1, P))
FIBERS = {
    0: (7, 13, 14),
    3: (4, 5, 11),
    6: (3, 8, 12),
    10: (2, 9, 16),
    14: (6, 10, 15),
}


def evaluate(coefficients, x):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % P
    return value


def multiply(first, second):
    result = [0] * (len(first) + len(second) - 1)
    for i, a in enumerate(first):
        for j, b in enumerate(second):
            result[i + j] = (result[i + j] + a * b) % P
    return tuple(result)


def root_polynomial(roots):
    result = (1,)
    for x in roots:
        result = multiply(result, (-x % P, 1))
    return result


def interpolation_coefficients(word, points):
    result = [0] * len(points)
    for x in points:
        others = tuple(y for y in points if y != x)
        numerator = root_polynomial(others)
        scale = word[x - 1] * pow(evaluate(numerator, x), -1, P) % P
        for j, value in enumerate(numerator):
            result[j] = (result[j] + scale * value) % P
    return tuple(result)


def restriction_test(support):
    """Linear membership test from interpolation on eight coordinates."""
    anchor = support[:8]
    basis = []
    for x in anchor:
        numerator = root_polynomial(tuple(y for y in anchor if y != x))
        scale = pow(evaluate(numerator, x), -1, P)
        basis.append(tuple(value * scale % P for value in numerator))
    constraints = tuple(
        (x, tuple(evaluate(polynomial, x) for polynomial in basis))
        for x in support[8:]
    )

    def member(word):
        return all(
            (word[x - 1] - sum(weight * word[y - 1] for weight, y in zip(weights, anchor)))
            % P == 0
            for x, weights in constraints
        )

    return member


def main():
    assert sorted(x for roots in FIBERS.values() for x in roots) == list(range(2, 17))
    errors = {}
    for t, roots in FIBERS.items():
        assert root_polynomial(roots) == (1, (t - 3) % P, -t % P, 1)
        errors[t] = tuple(
            16 * pow(x, 15, P)
            * pow(((3 * x * x - 2 * t * x + t - 3) * (x * x - x) ** 2) % P, -1, P)
            % P if x in roots else 0
            for x in DOMAIN
        )
        assert sum(value != 0 for value in errors[t]) == 3

    a = errors[0]
    b = tuple((v - u) * pow(3, -1, P) % P for u, v in zip(errors[0], errors[3]))
    assert a == (0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 7, 8, 0, 0)
    assert b == (0, 0, 0, 15, 14, 0, 15, 0, 0, 0, 9, 0, 9, 3, 0, 0)

    for t, roots in FIBERS.items():
        codeword = tuple((u + t * v - e) % P for u, v, e in zip(a, b, errors[t]))
        coefficients = interpolation_coefficients(codeword, DOMAIN[:8])
        assert tuple(evaluate(coefficients, x) for x in DOMAIN) == codeword
        if t not in (0, 3):
            outside = tuple(x for x in DOMAIN if x not in FIBERS[0] + FIBERS[3] + roots)
            expected = tuple(-t * (t - 3) * value % P for value in root_polynomial(outside))
            assert coefficients == expected
        support = tuple(x for x in DOMAIN if x not in roots)
        member = restriction_test(support)
        assert member(tuple((u + t * v) % P for u, v in zip(a, b)))
        assert not member(b)
    print("PASS: five cubic factorizations, error weights, degree-seven codewords, and same-support failure.")

    supports = tuple(
        tuple(x for x in DOMAIN if x not in omitted)
        for size in range(4)
        for omitted in combinations(DOMAIN, size)
    )
    bad = set()
    witnesses = {t: set() for t in range(P)}
    for support in supports:
        member = restriction_test(support)
        failure = not member(a) or not member(b)
        for gamma in range(P):
            word = tuple((u + gamma * v) % P for u, v in zip(a, b))
            if member(word) and failure:
                bad.add(gamma)
                witnesses[gamma].add(support)
    assert bad == set(FIBERS)
    for t in FIBERS:
        assert witnesses[t] == {tuple(x for x in DOMAIN if x not in FIBERS[t])}
    assert len(supports) == 697
    print(f"PASS: original event for all 17 parameters and {len(supports)} admissible supports; bad = {sorted(bad)}.")

    assert comb(16, 9) // comb(12, 8) == 23
    assert 17**31 < 5 * 2**128 <= 17**32 < 7 * 2**128
    assert 6 * 2**128 <= 17**32
    assert 256 - 128 + 1 == 3 * 43 and 256 // 43 < 44
    assert 44 * 2**128 <= 257**32
    print("PASS: earlier sufficient count 23; sharp count 5; security threshold first met at q=17^32 in this tower.")
    print("PASS: q=17^32 permits at most six bad parameters; seven would exceed the budget.")
    print("This checks the explicit pair, not an exhaustive maximization over all input words.")


if __name__ == "__main__":
    main()
