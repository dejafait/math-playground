#!/usr/bin/env python3
"""Exact finite checks for L010, not a full Reed--Solomon list boundary."""

from fractions import Fraction
from itertools import combinations, product
import json
from math import gcd, prod
from pathlib import Path


# F_9 = F_3[i]/(i^2+1); an integer u+3v represents u+vi.
def fadd(a, b):
    return (a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3)


def fneg(a):
    return (-a % 3) % 3 + 3 * ((-(a // 3)) % 3)


def fmul(a, b):
    u, v, x, y = a % 3, a // 3, b % 3, b // 3
    return (u * x - v * y) % 3 + 3 * ((u * y + v * x) % 3)


def trim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return tuple(poly)


def add(u, v):
    return trim(fadd(u[i] if i < len(u) else 0,
                     v[i] if i < len(v) else 0)
                for i in range(max(len(u), len(v))))


def sub(u, v):
    return add(u, tuple(fneg(x) for x in v))


def mul(u, v):
    if not u or not v:
        return ()
    out = [0] * (len(u) + len(v) - 1)
    for i, a in enumerate(u):
        for j, b in enumerate(v):
            out[i + j] = fadd(out[i + j], fmul(a, b))
    return trim(out)


def derivative(u):
    return trim(fmul(i % 3, u[i]) for i in range(1, len(u)))


def evaluate(poly, x):
    out = 0
    for coefficient in reversed(poly):
        out = fadd(fmul(out, x), coefficient)
    return out


def root_order(poly, x):
    assert poly
    order = 0
    while poly and evaluate(poly, x) == 0:
        # Synthetic division by X-x, with coefficients in ascending order.
        quotient = [0] * (len(poly) - 1)
        quotient[-1] = poly[-1]
        for j in range(len(quotient) - 2, -1, -1):
            quotient[j] = fadd(poly[j + 1], fmul(x, quotient[j + 1]))
        assert fadd(poly[0], fmul(x, quotient[0])) == 0
        poly = trim(quotient)
        order += 1
    return order


def solutions(k, a, b, c, d):
    out = []
    for coefficients in product(range(9), repeat=k):
        polynomial = trim(coefficients)
        residual = add(add(mul(a, derivative(polynomial)),
                           mul(b, mul(polynomial, polynomial))),
                       add(mul(c, polynomial), d))
        if not residual:
            out.append(polynomial)
    return out


def bound(p, n, k, e, agreement):
    degree = k - 1
    v = n + (p - 1) * e
    diagonal = p * agreement - (p - 1) * max(0, agreement - (n - e))
    denominator = p * agreement**2 - v * degree
    if denominator <= 0:
        return None
    return (v * (diagonal - degree)) // denominator


assert all(fmul(x, y) == fmul(y, x) for x in range(9) for y in range(9))
assert all(any(fmul(x, y) == 1 for y in range(1, 9)) for x in range(1, 9))
aa = (0, 2, 0, 1)
split_solutions = solutions(3, aa, (1,), (1,), ())
triple_solutions = solutions(4, (1,), (1,), (0, 0, 0, 2), ())
assert () in triple_solutions and (0, 0, 0, 1) in triple_solutions

cases = [
    ("one_exception_scalar", 3, aa, split_solutions, (0, 3, 4, 5, 6), 1),
    ("two_exceptions_interleaved", 3, aa, split_solutions, (0, 1, 3, 4), 2),
    ("regular_triple_root", 4, (1,), triple_solutions, (0, 1, 3, 4, 5), 1),
    ("all_exceptional", 3, aa, split_solutions, (0, 1, 2), 1),
]
records = []
pair_checks = regular_roots = centers_checked = list_checks = 0
for label, k, a, scalar, points, m in cases:
    n = len(points)
    assert k <= n and len(set(points)) == n
    weights = [1 if evaluate(a, x) == 0 else 3 for x in points]
    e = weights.count(1)
    for u, v in combinations(scalar, 2):
        difference = sub(u, v)
        for x in range(9):
            order = root_order(difference, x)
            if order and evaluate(a, x):
                assert order % 3 == 0
                regular_roots += 1
    tuples = list(product(scalar, repeat=m))
    words = [tuple(tuple(evaluate(row, x) for row in candidate) for x in points)
             for candidate in tuples]
    assert len(set(words)) == len(words)
    for u, v in combinations(words, 2):
        assert sum(w for w, x, y in zip(weights, u, v) if x == y) <= k - 1
        pair_checks += 1

    # A received column has one agreement mask for each value attained by
    # a candidate, plus the zero mask if unused alphabet values exist.
    # This exhausts all centers up to identical agreement behavior.
    options = []
    for i in range(n):
        masks = {}
        for j, word in enumerate(words):
            masks[word[i]] = masks.get(word[i], 0) | (1 << j)
        column_options = list(masks.values())
        if len(masks) < 9**m:
            column_options.append(0)
        options.append(column_options)
    predictions = {a0: bound(3, n, k, e, a0) for a0 in range(k, n + 1)}
    maxima = {a0: 0 for a0 in range(k, n + 1)}
    for center_masks in product(*options):
        counts = [0] * len(words)
        for mask in center_masks:
            while mask:
                bit = mask & -mask
                counts[bit.bit_length() - 1] += 1
                mask ^= bit
        for a0, prediction in predictions.items():
            size = sum(c >= a0 for c in counts)
            maxima[a0] = max(maxima[a0], size)
            if prediction is not None:
                assert size <= prediction
                list_checks += 1
            if e == 0:
                h = (k - 1) // 3
                if a0 * a0 > n * h:
                    assert size <= n * (a0 - h) // (a0 * a0 - n * h)
        centers_checked += 1
    records.append({
        "case": label, "q": 9, "n": n, "k": k, "m": m, "e": e,
        "all_scalar_solutions": len(scalar), "all_solution_tuples": len(words),
        "center_agreement_patterns": prod(map(len, options)),
        "maximum_list_by_agreement": maxima,
        "weighted_bound_by_agreement": predictions,
    })
assert regular_roots > 0

arithmetic_checks = 0
for p in (3, 5, 7, 11, 17):
    for n in range(1, 41):
        for k in range(1, n + 1):
            for agreement in range(k, n + 1):
                if agreement**2 > n * (k - 1):
                    ordinary = n * (agreement - k + 1) // (agreement**2 - n * (k - 1))
                    assert bound(p, n, k, n, agreement) == ordinary
                    arithmetic_checks += 1

thresholds = []
for rate_denominator, p, expected in (
        (2, 3, Fraction(1, 4)), (4, 5, Fraction(1, 16)),
        (8, 11, Fraction(3, 80)), (16, 17, Fraction(1, 256))):
    rho = (Fraction(p, rate_denominator) - 1) / (p - 1)
    assert rho == expected
    for exponent in range(4, 15):
        n = 2**exponent
        k = n // rate_denominator
        e = n * rho.numerator // rho.denominator
        value = bound(p, n, k, e, k)
        assert value is not None and value <= p * n
    thresholds.append({"rate": f"1/{rate_denominator}", "p": p,
                       "sufficient_exception_fraction": str(rho)})

subspace_records = []
for s in range(3, 22, 2):
    q0 = 3**s
    k = 1 << (q0 - 1).bit_length()
    n = 2 * k
    e = gcd(n, q0 - 1)
    assert e == 2
    value = bound(3, n, k, e, k)
    assert value is not None and value <= 4
    subspace_records.append({"s": s, "Q": q0, "k": k, "n": n, "e": e,
                             "raw_solution_lower_bound": 3**((s*s - 1) // 4),
                             "filtered_upper_bound": value})

result = {
    "scope": "Exact finite multiplicity and center-pattern checks; no full-code boundary claim.",
    "polynomials_enumerated": 9**3 + 9**4,
    "tuple_pairs_checked": pair_checks,
    "nonexceptional_pair_roots_checked": regular_roots,
    "center_agreement_patterns_checked": centers_checked,
    "positive_denominator_list_checks": list_checks,
    "ordinary_bound_specializations_checked": arithmetic_checks,
    "cases": records, "zero_slack_thresholds": thresholds,
    "smooth_subspace_parameter_checks": subspace_records,
}
Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"Passed {pair_checks} tuple-pair checks, {centers_checked} exhaustive center patterns, "
      f"{list_checks} list inequalities, and {arithmetic_checks} ordinary-bound checks; "
      f"tested {len(subspace_records)} smooth subspace parameter instances.")
