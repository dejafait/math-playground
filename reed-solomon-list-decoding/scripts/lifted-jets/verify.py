#!/usr/bin/env python3
"""Exact small-chart checks for L003; no third-party packages required.

Sparse polynomials over Q check the recurrence and degrees symbolically.
Reduction at nonsingular base points checks every residual equation over
small prime fields. This is a regression check, not the general proof.
"""

from fractions import Fraction
from math import comb
from pathlib import Path
import json
import random


def constant(n, value=1):
    return {(0,) * n: Fraction(value)} if value else {}


def variable(n, index):
    mon = [0] * n
    mon[index] = 1
    return {tuple(mon): Fraction(1)}


def add(left, right):
    result = dict(left)
    for mon, coeff in right.items():
        result[mon] = result.get(mon, 0) + coeff
        if not result[mon]:
            del result[mon]
    return result


def scale(poly, scalar):
    return {mon: coeff * scalar for mon, coeff in poly.items() if coeff * scalar}


def multiply(left, right):
    result = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            mon = tuple(a + b for a, b in zip(ml, mr))
            result[mon] = result.get(mon, 0) + cl * cr
    return {mon: coeff for mon, coeff in result.items() if coeff}


def power(poly, exponent, n):
    assert exponent >= 0
    result = constant(n)
    for _ in range(exponent):
        result = multiply(result, poly)
    return result


def degree(poly):
    return max((sum(mon) for mon in poly), default=-1)


def evaluate_mod(poly, values, prime):
    total = 0
    for mon, coeff in poly.items():
        term = coeff.numerator * pow(coeff.denominator, -1, prime) % prime
        for value, exponent in zip(values, mon):
            term = term * pow(value, exponent, prime) % prime
        total = (total + term) % prime
    return total


def check_chart(name, d, s, alpha, q_terms):
    # Each Q term is (coefficient, Z exponent, X exponent, Y exponents).
    D = max(max(z, x) for _, z, x, _ in q_terms)
    B = max(sum(ys) for _, _, _, ys in q_terms)
    A, a = D + B, d - s
    length = max(0, 2 * a - 1)
    n, base_n = d + 3, s + 2
    z_var, u_var = variable(n, 0), variable(n, 1)
    x_poly = add(constant(n, alpha), u_var)
    series = []
    for i in range(s + 1):
        poly = {}
        for j in range(i, d + 1):
            term = multiply(variable(n, 2 + j), power(u_var, j - i, n))
            poly = add(poly, scale(term, comb(j, i)))
        series.append(poly)

    expanded, H = {}, {}
    for coeff, z, x, ys in q_terms:
        term = scale(multiply(power(z_var, z, n), power(x_poly, x, n)), coeff)
        for i, exponent in enumerate(ys):
            term = multiply(term, power(series[i], exponent, n))
        expanded = add(expanded, term)
        if ys[s]:
            hs = list(ys)
            hs[s] -= 1
            H = add(H, {(z, *hs): Fraction(coeff * alpha**x * ys[s])})
    assert H and degree(H) <= A - 1

    coefficients = [{} for _ in range(D + B * d + 1)]
    for mon, coeff in expanded.items():
        order = mon[1]
        key = (mon[0], *mon[2:])  # Variables Z,c_0,...,c_d.
        coefficients[order] = add(coefficients[order], {key: coeff})

    numerators = {}

    def clear(poly, budget):
        result = {}
        for mon, coeff in poly.items():
            term = {mon[:base_n]: coeff}
            used = 0
            for h, exponent in enumerate(mon[base_n:], 1):
                if exponent:
                    assert h in numerators
                    used += (2 * h - 1) * exponent
                    term = multiply(term, power(numerators[h], exponent, base_n))
            assert used <= budget
            term = multiply(term, power(H, budget - used, base_n))
            result = add(result, term)
        return result

    for t in range(1, a + 1):
        current_index = 1 + s + t
        linear, remainder = {}, {}
        for mon, coeff in coefficients[t].items():
            if mon[current_index]:
                expected_high = tuple(1 if h == t else 0 for h in range(1, a + 1))
                assert mon[base_n:] == expected_high
                linear = add(linear, {mon[:base_n]: coeff})
            else:
                assert all(exponent == 0 for exponent in mon[current_index:])
                remainder = add(remainder, {mon: coeff})
        binomial = comb(s + t, s)
        assert linear == scale(H, binomial)
        numerators[t] = scale(clear(remainder, 2 * t - 2), Fraction(-1, binomial))
        assert degree(numerators[t]) <= A * (2 * t - 1)

    residuals = [clear(poly, B * length) for poly in coefficients]
    assert all(not residuals[t] for t in range(1, a + 1))
    assert all(degree(poly) <= A * (1 + B * length) for poly in residuals)

    rng = random.Random(20260925)
    samples = 0
    for prime in (5, 7, 11):
        assert prime > d
        accepted = 0
        while accepted < 8:
            base = tuple(rng.randrange(prime) for _ in range(base_n))
            h_value = evaluate_mod(H, base, prime)
            if not h_value:
                continue
            all_values = list(base)
            for t in range(1, a + 1):
                value = evaluate_mod(numerators[t], base, prime)
                value = value * pow(pow(h_value, 2 * t - 1, prime), -1, prime) % prime
                all_values.append(value)
            for order, original in enumerate(coefficients):
                direct = evaluate_mod(original, all_values, prime)
                cleared = evaluate_mod(residuals[order], base, prime)
                assert cleared == direct * pow(h_value, B * length, prime) % prime
                if 1 <= order <= a:
                    assert direct == 0
            accepted += 1
            samples += 1

    return {
        "case": name,
        "d": d,
        "s": s,
        "D": D,
        "B": B,
        "L": length,
        "numerator_degrees": [degree(numerators[t]) for t in range(1, a + 1)],
        "numerator_bounds": [A * (2 * t - 1) for t in range(1, a + 1)],
        "max_residual_degree": max(map(degree, residuals)),
        "residual_bound": A * (1 + B * length),
        "finite_field_samples": samples,
        "all_checks_passed": True,
    }


def main():
    cases = [
        ("square_root", 4, 0, 0, [(1, 0, 0, (2,)), (-1, 1, 0, (0,)), (-1, 0, 1, (0,))]),
        ("nonlinear_first_order", 4, 1, 1, [
            (1, 1, 0, (0, 2)), (1, 0, 1, (0, 2)), (1, 0, 0, (3, 0)),
            (1, 2, 1, (0, 0)), (1, 0, 0, (0, 0)),
        ]),
        ("second_order", 4, 2, 2, [
            (1, 2, 0, (0, 0, 1)), (1, 0, 1, (0, 0, 1)),
            (1, 0, 0, (0, 2, 0)), (1, 0, 2, (2, 0, 0)), (1, 1, 0, (0, 0, 0)),
        ]),
        ("no_lift_needed", 1, 1, 0, [
            (1, 0, 0, (0, 2)), (1, 0, 0, (1, 0)), (1, 1, 1, (0, 0)),
        ]),
        ("linear_differential_equation", 4, 1, 1, [
            (1, 1, 0, (0, 1)), (1, 0, 2, (0, 1)), (1, 2, 0, (1, 0)),
            (1, 0, 0, (1, 0)), (1, 0, 1, (0, 0)),
        ]),
    ]
    results = [check_chart(*case) for case in cases]
    output = Path(__file__).with_name("results.json")
    output.write_text(json.dumps(results, indent=2) + "\n")
    print(f"PASS: {len(results)} exact symbolic charts; "
          f"{sum(row['finite_field_samples'] for row in results)} finite-field samples.")
    print(f"Results: {output.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
