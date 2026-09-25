"""Exact interpolation checks; the proof supplies extension-field persistence."""

from itertools import combinations
from math import comb


P = 17
DOMAIN = tuple(range(1, P))
DIMENSION = 8


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


def restriction_matrix(support):
    """Equations for interpolation of degree less than eight on this support."""
    anchor = support[:DIMENSION]
    basis = []
    for x in anchor:
        numerator = root_polynomial(tuple(y for y in anchor if y != x))
        scale = pow(evaluate(numerator, x), -1, P)
        basis.append(tuple(value * scale % P for value in numerator))
    constraints = tuple(
        (x, tuple(evaluate(polynomial, x) for polynomial in basis))
        for x in support[DIMENSION:]
    )

    def residual(word):
        return tuple(
            (word[x - 1] - sum(weight * word[y - 1] for weight, y in zip(weights, anchor))) % P
            for x, weights in constraints
        )

    return residual


def combination(a, b, gamma):
    return tuple((u + gamma * v) % P for u, v in zip(a, b))


def check_witness(a, b, errors):
    for gamma, omitted in errors.items():
        support = tuple(x for x in DOMAIN if x not in omitted)
        assert len(support) == 12
        residual = restriction_matrix(support)
        assert not any(residual(combination(a, b, gamma)))
        assert any(residual(b))


def all_bad_parameters(a, b):
    """Check the same-support event on every admissible support, not decoding."""
    bad = set()
    supports_tested = 0
    for size in range(5):
        for omitted in combinations(DOMAIN, size):
            support = tuple(x for x in DOMAIN if x not in omitted)
            residual = restriction_matrix(support)
            ra, rb = residual(a), residual(b)
            supports_tested += 1
            for gamma in range(P):
                agrees = all((u + gamma * v) % P == 0 for u, v in zip(ra, rb))
                if agrees and (any(ra) or any(rb)):
                    bad.add(gamma)
    assert supports_tested == sum(comb(16, size) for size in range(5)) == 2517
    return bad, supports_tested


def main():
    search_a = (0, 0, 0, 0, 15, 13, 0, 0, 0, 13, 0, 0, 0, 0, 3, 0)
    search_b = (0, 0, 0, 0, 2, 4, 0, 15, 3, 4, 0, 6, 0, 0, 14, 14)
    search_errors = {
        0: (5, 6, 10, 15),
        1: (8, 9, 12, 16),
        3: (8, 9, 12, 14),
        8: (9, 12, 14, 16),
        9: (8, 9, 14, 16),
        10: (1, 2, 4, 6),
        11: (8, 12, 14, 16),
    }
    check_witness(search_a, search_b, search_errors)
    print("PASS: the seven search parameters satisfy the original event on their claimed supports.")

    first, second = DOMAIN[:5], DOMAIN[5:10]
    q_polynomial = root_polynomial(DOMAIN[10:])
    assert len(q_polynomial) - 1 == 6
    a = tuple(x * evaluate(q_polynomial, x) % P if x in first else 0 for x in DOMAIN)
    b = tuple(-evaluate(q_polynomial, x) % P if x in first else 0 for x in DOMAIN)
    errors = {
        gamma: tuple(x for x in (first if gamma in first else second) if x != gamma)
        for gamma in first + second
    }
    check_witness(a, b, errors)
    for gamma in first + second:
        polynomial = (0,) if gamma in first else multiply(q_polynomial, (-gamma % P, 1))
        assert len(polynomial) - 1 < DIMENSION
        word = combination(a, b, gamma)
        actual_errors = tuple(x for x in DOMAIN if word[x - 1] != evaluate(polynomial, x))
        assert actual_errors == errors[gamma]
    print(f"PASS: ten explicit challenges, degree bounds, four errors, and same-support failure; Q = {q_polynomial}.")
    print(f"a = {a}")
    print(f"b = {b}")

    bad, supports_tested = all_bad_parameters(a, b)
    assert set(first + second).issubset(bad)
    print(f"PASS: original event on all 17 parameters and {supports_tested} admissible supports; bad = {sorted(bad)}.")
    assert 5 * 2**128 <= 17**32 < 7 * 2**128 < 10 * 2**128
    assert 17**32 // 2**128 == 6
    assert comb(16, 9) // comb(11, 8) == 69
    assert 130 * 2**128 < 257**32
    assert (97 - 1) % 16 == 0 and 97**20 // 2**128 == 15
    print("PASS: q=17^32 allows six bad parameters; ten exceed the budget; L004 gives only the upper count 69.")
    print("PASS: the general count 130 at n=256,k=128,r=64 is insufficient to exceed the q=257^32 budget.")
    print("PASS: the proposed F_(97^20) test has allowable count fifteen and a smooth length-16 domain.")
    print("These checks do not maximize over pairs or certify all extension-field parameters.")


if __name__ == "__main__":
    main()
