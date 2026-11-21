"""Exact fixed-support determinant certificate; uses Python integer/Fraction arithmetic."""

from fractions import Fraction
from itertools import permutations
from math import factorial
from pathlib import Path
import json


ZERO = (0, 0, 0)


def constant(value):
    return {ZERO: Fraction(value)} if value else {}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            result[powers] = result.get(powers, Fraction(0)) + coefficient
    return {powers: c for powers, c in result.items() if c}


def scale(polynomial, scalar):
    return {powers: c * scalar for powers, c in polynomial.items() if c * scalar}


def multiply(*polynomials):
    result = constant(1)
    for polynomial in polynomials:
        product = {}
        for powers, c in result.items():
            for other_powers, d in polynomial.items():
                key = tuple(v + w for v, w in zip(powers, other_powers))
                product[key] = product.get(key, Fraction(0)) + c * d
        result = {powers: c for powers, c in product.items() if c}
    return result


def determinant(matrix):
    n = len(matrix)
    terms = []
    for permutation in permutations(range(n)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(n) for j in range(i + 1, n))
        terms.append(scale(multiply(*(matrix[i][permutation[i]] for i in range(n))),
                           (-1) ** inversions))
    return add(*terms)


def time_derivative(polynomial):
    # a(t)=a, b(t)=b exp(t), c(t)=c exp(4t).
    return {powers: coefficient * (powers[1] + 4 * powers[2])
            for powers, coefficient in polynomial.items()
            if powers[1] + 4 * powers[2]}


def serial(polynomial):
    return [{"a_b_c_powers": list(powers), "coefficient": str(c)}
            for powers, c in sorted(polynomial.items())]


def main():
    a, b, c = ({powers: Fraction(1)} for powers in
               [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    q = [add(a, b, c)] + [scale(add(b, scale(c, 4 ** n)), Fraction(1, factorial(2 * n)))
                              for n in range(1, 6)]
    q_dot = [scale(add(b, scale(c, 4 ** (n + 1))), Fraction(1, factorial(2 * n)))
             for n in range(6)]
    matrix = [[q[2 + i - j] for j in range(3)] for i in range(3)]
    matrix_dot = [[q_dot[2 + i - j] for j in range(3)] for i in range(3)]
    boundary = determinant(matrix)
    derivative_rows = [determinant([matrix_dot[i] if i == row else matrix[i]
                                   for i in range(3)]) for row in range(3)]
    derivative = add(*derivative_rows)
    denominator = 14515200
    C_numerator = add(scale(multiply(b, b), 13),
                      scale(multiply(b, c), -496), scale(multiply(c, c), 53248))
    F_numerator = add(scale(multiply(b, b, b), 313),
                      scale(multiply(b, b, c), 3117),
                      scale(multiply(b, c, c), -84048),
                      scale(multiply(c, c, c), 1282048))
    expected = scale(add(multiply(a, C_numerator), F_numerator),
                     Fraction(1, denominator))
    C_positive_terms = [scale(multiply(add(b, scale(c, -20)),
                                      add(b, scale(c, -20))), 13),
                        scale(multiply(b, c), 24),
                        scale(multiply(c, c), 48048)]
    F_positive_terms = [scale(multiply(b, b, b), 313),
                        scale(multiply(c, add(b, scale(c, -14)),
                                       add(b, scale(c, -14))), 3117),
                        scale(multiply(b, c, c), 3228),
                        scale(multiply(c, c, c), 671116)]
    checks = {
        "determinant_expansion_exact": boundary == expected,
        "C_positive_decomposition_exact": C_numerator == add(*C_positive_terms),
        "F_positive_decomposition_exact": F_numerator == add(*F_positive_terms),
        "coefficient_time_derivatives_exact": all(time_derivative(q[n]) == q_dot[n]
                                                    for n in range(6)),
        "coefficient_shift_q0_through_q4_exact": all(q_dot[n] == scale(q[n + 1],
                                                        (2 * n + 2) * (2 * n + 1))
                                                     for n in range(5)),
        "all_three_row_derivatives_exact": derivative == time_derivative(boundary),
        "q5_used_in_last_row_derivative": matrix_dot[2][0] == scale(q[5], 90),
    }
    failures = [name for name, passed in checks.items() if not passed]
    output = Path(__file__).with_name("three-atom-boundary-flux-20261106.json")
    certificate = {
        "status": "FIXED_SUPPORT_NO_BOUNDARY" if not failures else "FAILED",
        "variables": "unnormalized positive masses a,b,c at 0,1,4; no time renormalization",
        "coefficient_order": "powers in a,b,c; exact Fraction coefficients",
        "q0_through_q5": [serial(v) for v in q],
        "q_dot_0_through_5": [serial(v) for v in q_dot],
        "B": serial(boundary),
        "integer_denominator": denominator,
        "C_numerator": serial(C_numerator),
        "F_numerator": serial(F_numerator),
        "C_positive_terms": [serial(v) for v in C_positive_terms],
        "F_positive_terms": [serial(v) for v in F_positive_terms],
        "row_derivative_terms": [serial(v) for v in derivative_rows],
        "B_prime": serial(derivative),
        "checks": checks,
        "bounds": {
            "actual": "B >= 671116*c^3/14515200 > 0 for a,b,c>0",
            "required": "B=0, rank=2, every proper minor>0, B_prime>0",
            "consequence": "B=0 is impossible, so minor/rank/flux filtering is unnecessary",
        },
        "failures": failures,
        "limits": "Only support {0,1,4}; neither general cone invariance nor actual Xi signs.",
    }
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(certificate["status"])
    print("Actual bound:", certificate["bounds"]["actual"])
    print("Required boundary:", certificate["bounds"]["required"])
    print("Exact checks:", len(checks), "; failures:", failures)
    print("Full certificate:", output)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
