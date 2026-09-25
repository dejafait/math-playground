"""Exact auxiliary checks for L010 over F_97; not a search over all pencils."""

from itertools import combinations, permutations
from math import comb


P = 97
H = tuple(sorted(pow(8, i, P) for i in range(16)))


def trim(coefficients):
    coefficients = [value % P for value in coefficients]
    while len(coefficients) > 1 and not coefficients[-1]:
        coefficients.pop()
    return tuple(coefficients)


def add(first, second):
    result = [0] * max(len(first), len(second))
    for i, value in enumerate(first):
        result[i] += value
    for i, value in enumerate(second):
        result[i] += value
    return trim(result)


def scale(polynomial, scalar):
    return trim([value * scalar for value in polynomial])


def multiply(first, second):
    result = [0] * (len(first) + len(second) - 1)
    for i, a in enumerate(first):
        for j, b in enumerate(second):
            result[i + j] += a * b
    return trim(result)


def evaluate(coefficients, x):
    value = 0
    for coefficient in reversed(coefficients):
        value = (value * x + coefficient) % P
    return value


def root_polynomial(roots):
    result = (1,)
    for x in roots:
        result = multiply(result, (-x, 1))
    return result


def determinant(matrix):
    """Determinant over F_97[T], by signed permutation expansion."""
    size = len(matrix)
    result = (0,)
    for permutation in permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size) for j in range(i + 1, size)
        )
        term = (1,)
        for i, j in enumerate(permutation):
            term = multiply(term, matrix[i][j])
        result = add(result, scale(term, (-1) ** inversions))
    return result


def locator(a, b):
    moments_a, moments_b = syndrome(a), syndrome(b)
    moments = [trim((u, v)) for u, v in zip(moments_a, moments_b)]
    rows = [[moments[i + j] for j in range(5)] for i in range(4)]
    coefficients = tuple(
        scale(determinant([[row[j] for j in range(5) if j != column]
                           for row in rows]), (-1) ** column)
        for column in range(5)
    )
    by_coordinate = {}
    for x in H:
        result = (0,)
        for j, coefficient in enumerate(coefficients):
            result = add(result, scale(coefficient, pow(x, j, P)))
        by_coordinate[x] = result
    return coefficients[-1], coefficients, by_coordinate


def syndrome(word):
    return tuple(sum(value * pow(x, j, P) for x, value in zip(H, word)) % P
                 for j in range(1, 9))


def solve_square(matrix, target):
    size = len(matrix)
    rows = [list(row) + [value] for row, value in zip(matrix, target)]
    for column in range(size):
        pivot = next(i for i in range(column, size) if rows[i][column] % P)
        rows[column], rows[pivot] = rows[pivot], rows[column]
        inverse = pow(rows[column][column] % P, -1, P)
        rows[column] = [value * inverse % P for value in rows[column]]
        for i in range(size):
            if i != column:
                factor = rows[i][column]
                rows[i] = [(a - factor * b) % P
                           for a, b in zip(rows[i], rows[column])]
    return tuple(row[-1] for row in rows)


def word_with_syndrome(moments):
    weights = solve_square([[pow(x, j, P) for x in H[:8]]
                            for j in range(1, 9)], moments)
    result = weights + (0,) * 8
    assert syndrome(result) == moments
    return result


def interpolation_constraints():
    """All supports of size at least twelve, independently of the locator."""
    constraints = []
    for omitted_size in range(5):
        for omitted in combinations(range(16), omitted_size):
            support = tuple(i for i in range(16) if i not in omitted)
            anchor = support[:8]
            basis = []
            for i in anchor:
                numerator = root_polynomial(H[j] for j in anchor if j != i)
                basis.append(scale(numerator, pow(evaluate(numerator, H[i]), -1, P)))
            equations = tuple(
                (i, tuple(evaluate(polynomial, H[i]) for polynomial in basis))
                for i in support[8:]
            )
            constraints.append((anchor, equations, support))
    assert len(constraints) == sum(comb(16, w) for w in range(5)) == 2517
    return constraints


def original_event(a, b, constraints):
    bad = set()
    decoded_weights = {}
    for anchor, equations, support in constraints:
        def residual(word):
            return tuple((word[i] - sum(c * word[j] for c, j in zip(weights, anchor))) % P
                         for i, weights in equations)

        ra, rb = residual(a), residual(b)
        if any(rb):
            first = next(i for i, value in enumerate(rb) if value)
            gamma = -ra[first] * pow(rb[first], -1, P) % P
            parameters = [gamma] if all((u + gamma * v) % P == 0
                                       for u, v in zip(ra, rb)) else []
            bad.update(parameters)
        elif not any(ra):
            parameters = range(P)
        else:
            parameters = []
        for gamma in parameters:
            omitted = 16 - len(support)
            decoded_weights[gamma] = min(decoded_weights.get(gamma, 16), omitted)
    return bad, decoded_weights


def multiplicity(polynomial, root):
    assert polynomial != (0,)
    result = 0
    while len(polynomial) > 1 and evaluate(polynomial, root) == 0:
        quotient = [0] * (len(polynomial) - 1)
        quotient[-1] = polynomial[-1]
        for i in range(len(quotient) - 2, -1, -1):
            quotient[i] = (polynomial[i + 1] + root * quotient[i + 1]) % P
        assert (polynomial[0] + root * quotient[0]) % P == 0
        polynomial = trim(quotient)
        result += 1
    return result


def check_regular_case(name, a, b, constraints, forced_weight=None):
    d, locator_coefficients, coordinate_locators = locator(a, b)
    assert d != (0,), name
    assert all(polynomial != (0,) for polynomial in coordinate_locators.values()), name
    bad, weights = original_event(a, b, constraints)
    assert bad == set(weights), (name, bad, weights)
    if forced_weight is not None:
        assert weights[0] == forced_weight
    counts = [sum(w == j for w in weights.values()) for j in range(5)]
    weighted = 4 * counts[4] + 16 * sum((4 - w) * counts[w] for w in range(4))
    degrees = sum(len(polynomial) - 1 for polynomial in coordinate_locators.values())
    assert weighted <= degrees <= 64
    assert len(bad) <= 16 - 3 * counts[3] - 7 * counts[2] - 11 * counts[1] - 15 * counts[0]

    for gamma in range(P):
        roots = [x for x in H if evaluate(coordinate_locators[x], gamma) == 0]
        d_value = evaluate(d, gamma)
        if d_value:
            assert len(roots) <= 4
            assert (len(roots) == 4) == (weights.get(gamma) == 4)
            if len(roots) == 4:
                actual = tuple(evaluate(coefficient, gamma) for coefficient in locator_coefficients)
                assert actual == scale(root_polynomial(roots), d_value)
                values = solve_square([[pow(x, j, P) for x in roots]
                                       for j in range(1, 5)],
                                      syndrome(tuple((u + gamma * v) % P for u, v in zip(a, b)))[:4])
                assert all(values)
                recovered = tuple(values[roots.index(x)] if x in roots else 0 for x in H)
                assert syndrome(recovered) == syndrome(tuple((u + gamma * v) % P for u, v in zip(a, b)))
        if gamma in weights and weights[gamma] <= 3:
            assert not d_value and len(roots) == 16
            assert all(multiplicity(polynomial, gamma) >= 4 - weights[gamma]
                       for polynomial in coordinate_locators.values())

    print(f"PASS: {name}: bad={sorted(bad)}, counts N_0..N_4={counts}; incidence {weighted} <= {degrees} <= 64.")
    return bad


def main():
    assert len(set(H)) == 16 and all(pow(x, 16, P) == 1 for x in H)
    constraints = interpolation_constraints()

    first, second, remainder = H[:5], H[5:10], H[10:]
    q_polynomial = root_polynomial(remainder)
    a = tuple(x * evaluate(q_polynomial, x) % P if x in first else 0 for x in H)
    b = tuple(-evaluate(q_polynomial, x) % P if x in first else 0 for x in H)
    assert check_regular_case("two-block witness", a, b, constraints) == set(first + second)

    direction = word_with_syndrome((1, 2, 3, 5, 7, 11, 13, 17))
    for weight in range(4):
        initial = tuple(i + 1 if i < weight else 0 for i in range(16))
        check_regular_case(f"weight-{weight} at zero", initial, direction, constraints, weight)

    fixed_a = (1,) * 4 + (0,) * 12
    fixed_b = (1, 2, 3, 4) + (0,) * 12
    d, _, coordinate_locators = locator(fixed_a, fixed_b)
    assert d != (0,)
    assert all(coordinate_locators[x] == (0,) for x in H[:4])
    bad, decoded = original_event(fixed_a, fixed_b, constraints)
    assert len(decoded) == P and len(bad) == 4
    print("PASS: fixed-support pencil has 97 decodable values but only four bad values; persistent roots exclude it.")

    assert 15 * 2**128 <= 97**20 < 16 * 2**128
    print("PASS: the proved count sixteen is one above the actual allowable count fifteen.")
    print("All event checks use 2517 supports; no global maximum or extension-field enumeration is inferred.")


if __name__ == "__main__":
    main()
