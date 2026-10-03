"""Exact support checks for L011 over F_97, not a maximum over all pencils."""

import importlib.util
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path

sys.dont_write_bytecode = True
SOURCE = Path(__file__).resolve().parents[1] / "locator-incidence" / "check.py"
SPEC = importlib.util.spec_from_file_location("locator_check", SOURCE)
BASE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BASE)
P, H = BASE.P, BASE.H


def constraints(points, radius):
    """Interpolation constraints on every allowed original or punctured support."""
    result = []
    for omitted_size in range(radius + 1):
        for omitted in combinations(range(len(points)), omitted_size):
            support = tuple(i for i in range(len(points)) if i not in omitted)
            anchor = support[:8]
            basis = []
            for i in anchor:
                numerator = BASE.root_polynomial(points[j] for j in anchor if j != i)
                basis.append(BASE.scale(numerator, pow(BASE.evaluate(numerator, points[i]), -1, P)))
            equations = tuple(
                (i, tuple(BASE.evaluate(polynomial, points[i]) for polynomial in basis))
                for i in support[8:]
            )
            result.append((anchor, equations, support))
    return result


def event(a, b, support_constraints):
    """Directly test combination membership and input failure on the same support."""
    bad, weights = set(), {}
    for anchor, equations, support in support_constraints:
        def residual(word):
            return tuple(
                (word[i] - sum(c * word[j] for c, j in zip(coefficients, anchor))) % P
                for i, coefficients in equations
            )

        ra, rb = residual(a), residual(b)
        if any(rb):
            first = next(i for i, value in enumerate(rb) if value)
            parameter = -ra[first] * pow(rb[first], -1, P) % P
            matches = [parameter] if all(
                (u + parameter * v) % P == 0 for u, v in zip(ra, rb)
            ) else []
            bad.update(matches)
        elif not any(ra):
            matches = range(P)
        else:
            matches = []
        for parameter in matches:
            weight = len(a) - len(support)
            weights[parameter] = min(weights.get(parameter, len(a)), weight)
    return bad, weights


def check_case(name, a, b, removed, full_constraints, expected_bad,
               expected_missing, expected_weight=None):
    d, _, locators = BASE.locator(a, b)
    assert d != (0,) and locators[removed] == (0,), name
    persistent = tuple(x for x in H if locators[x] == (0,))
    original_bad, original_weights = event(a, b, full_constraints)
    remaining = tuple(i for i, x in enumerate(H) if x != removed)
    punctured_points = tuple(H[i] for i in remaining)
    punctured_bad, punctured_weights = event(
        tuple(a[i] for i in remaining), tuple(b[i] for i in remaining),
        constraints(punctured_points, 3)
    )
    assert original_bad == expected_bad, (name, original_bad)
    assert original_bad - punctured_bad == expected_missing, name
    assert len(original_bad) <= 12 and len(punctured_bad) <= 12, name
    assert set(original_weights) <= set(punctured_weights), name
    for t, weight in original_weights.items():
        assert punctured_weights[t] <= 3
        if weight == 4:
            assert BASE.evaluate(d, t) != 0
        if BASE.evaluate(d, t) == 0:
            assert weight <= 3
    if expected_weight is not None:
        assert original_weights[0] == expected_weight
        assert BASE.evaluate(d, 0) == 0
    print(
        f"PASS: {name}: persistent={persistent}; original bad={sorted(original_bad)}; "
        f"punctured bad={sorted(punctured_bad)}; lost={sorted(expected_missing)}; "
        f"original/punctured close counts={len(original_weights)}/{len(punctured_weights)}."
    )


def main():
    full_constraints = constraints(H, 4)
    assert len(full_constraints) == 2517
    x, y, z = H[:3]

    fixed_a = (1,) * 4 + (0,) * 12
    fixed_b = (1, 2, 3, 4) + (0,) * 12
    roots = {-pow(i, -1, P) % P for i in range(1, 5)}
    check_case("fixed-four-support regression", fixed_a, fixed_b, x,
               full_constraints, roots, {P - 1})

    # The derivative moment j*z^(j-1) gives a repeated locator at z.
    # The generic original rank is four: x, y, and the double node z.
    a = tuple(int(point == y) for point in H)
    b = BASE.word_with_syndrome(tuple(
        (pow(x, j, P) + j * pow(z, j - 1, P)) % P for j in range(1, 9)
    ))
    assert a[H.index(x)] == 0
    check_case("singular error omits persistent coordinate", a, b, x,
               full_constraints, {0}, set(), expected_weight=1)

    code_a = tuple(BASE.evaluate((3, 1, 4, 1, 5, 9, 2, 6), point) for point in H)
    code_b = tuple(BASE.evaluate((2, 7, 1, 8, 2, 8, 1), point) for point in H)
    check_case("translated singular pencil",
               tuple((u + c) % P for u, c in zip(a, code_a)),
               tuple((v + c) % P for v, c in zip(b, code_b)), x,
               full_constraints, {0}, set(), expected_weight=1)

    delta, eta = Fraction(8, 15), Fraction(3, 15)
    threshold = (delta - eta) / (eta * (delta - 2 * eta))
    assert delta / 3 <= eta <= delta / 2 - Fraction(1, 15)
    assert threshold == Fraction(25, 2) < 13
    assert Fraction(13 * 3, 12) == Fraction(13, 4) < 4
    assert 15 * 2**128 <= 97**20 < 16 * 2**128
    print("PASS: BCHKS range, threshold 25/2, integral support bound three, and allowable budget fifteen.")
    print("All checks are auxiliary prime-field examples; the proof covers arbitrary F_(97^20) inputs.")


if __name__ == "__main__":
    main()
