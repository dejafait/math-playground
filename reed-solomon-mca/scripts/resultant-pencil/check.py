"""Bounded exact tests of supplied F_97 moment pencils; no exhaustive bound.

All polynomials have increasing coefficients. Splitting is checked in
F_(97^20) by modular Frobenius, without enumerating that field.
"""

import importlib.util
import json
from collections import Counter
from pathlib import Path
import random
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "locator_check", ROOT / "scripts/locator-incidence/check.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
P, H = base.P, base.H
trim, add, scale = base.trim, base.add, base.scale
multiply, evaluate = base.multiply, base.evaluate
ZERO, ONE, T = (0,), (1,), (0, 1)
SEED = 2026100421


def degree(f):
    return len(f) - 1 if f != ZERO else -1


def monic(f):
    return scale(f, pow(f[-1], -1, P)) if f != ZERO else ZERO


def divmod_poly(f, g):
    assert g != ZERO
    remainder = list(f)
    quotient = [0] * max(1, len(f) - len(g) + 1)
    inverse = pow(g[-1], -1, P)
    while trim(remainder) != ZERO and len(remainder) >= len(g):
        k = len(remainder) - len(g)
        coefficient = remainder[-1] * inverse % P
        quotient[k] = coefficient
        for j, value in enumerate(g):
            remainder[k + j] = (remainder[k + j] - coefficient * value) % P
        remainder = list(trim(remainder))
    return trim(quotient), trim(remainder)


def quotient(f, g):
    answer, remainder = divmod_poly(f, g)
    assert remainder == ZERO
    return answer


def gcd(f, g):
    while g != ZERO:
        f, g = g, divmod_poly(f, g)[1]
    return monic(f)


def derivative(f):
    return trim([i * value for i, value in enumerate(f)][1:] or [0])


def power(f, exponent):
    answer = ONE
    for _ in range(exponent):
        answer = multiply(answer, f)
    return answer


def powmod(f, exponent, modulus):
    answer = ONE
    f = divmod_poly(f, modulus)[1]
    while exponent:
        if exponent & 1:
            answer = divmod_poly(multiply(answer, f), modulus)[1]
        exponent >>= 1
        if exponent:
            f = divmod_poly(multiply(f, f), modulus)[1]
    return answer


def field_root_part(f, extension_degree):
    """For squarefree f, return its factor whose roots lie in F_(97^s)."""
    if degree(f) == 0:
        return ONE
    assert gcd(f, derivative(f)) == ONE
    frobenius = divmod_poly(T, f)[1]
    for _ in range(extension_degree):
        frobenius = powmod(frobenius, P, f)
    return gcd(f, add(frobenius, scale(T, -1)))


def squarefree_factors(f):
    """Return multiplicity -> monic factor, using deg(f)<char(F)."""
    assert 0 <= degree(f) < P
    f = monic(f)
    repeated = gcd(f, derivative(f))
    remaining = quotient(f, repeated)
    factors, multiplicity = {}, 1
    while remaining != ONE:
        common = gcd(remaining, repeated)
        factor = quotient(remaining, common)
        if factor != ONE:
            factors[multiplicity] = factor
            assert gcd(factor, derivative(factor)) == ONE
        remaining = common
        repeated = quotient(repeated, common)
        multiplicity += 1
    assert repeated == ONE  # No inseparable residual: degree is below 97.
    reconstructed = ONE
    for multiplicity, factor in factors.items():
        reconstructed = multiply(reconstructed, power(factor, multiplicity))
    assert reconstructed == f
    return factors


def resultant_product(coordinate_locators):
    result = ONE
    for x in H:
        result = multiply(result, coordinate_locators[x])
    return result


def target_power_root(r):
    """Return P if r=c*P^4 with monic squarefree P of degree sixteen."""
    if degree(r) != 64:
        return None
    repeated = gcd(r, derivative(r))
    if degree(repeated) != 48:
        return None
    candidate = monic(quotient(r, repeated))
    if degree(candidate) != 16 or gcd(candidate, derivative(candidate)) != ONE:
        return None
    return candidate if power(candidate, 4) == monic(r) else None


def equality_check(d, coordinate_locators, r):
    """This is L010's full criterion only for an actual moment pencil."""
    candidate = target_power_root(r)
    if candidate is None:
        return False
    if field_root_part(candidate, 20) != candidate:
        return False
    if gcd(candidate, d) != ONE:
        return False
    return all(degree(f) == 4 and gcd(f, derivative(f)) == ONE
               for f in coordinate_locators.values())


def two_block(first, second):
    remaining = tuple(x for x in H if x not in first + second)
    q = base.root_polynomial(remaining)
    a = tuple(x * evaluate(q, x) % P if x in first else 0 for x in H)
    b = tuple(-evaluate(q, x) % P if x in first else 0 for x in H)
    return a, b


def audit_two_block(a, b, forced, d, coefficients, locators):
    first = tuple(x for x, value in zip(H, b) if value)
    second = tuple(x for x in forced if x not in first)
    remaining = tuple(x for x in H if x not in first + second)
    assert (len(first), len(second), len(remaining)) == (5, 5, 6)
    u, v = base.root_polynomial(first), base.root_polynomial(second)
    # Divide U(T)V(X)-V(T)U(X) by X-T over F_97[T].
    numerator = [add(scale(u, v[j]), scale(v, -u[j])) for j in range(6)]
    kernel = [ZERO] * 5
    kernel[4] = numerator[5]
    for j in range(3, -1, -1):
        kernel[j] = add(numerator[j + 1], multiply(T, kernel[j + 1]))
    assert add(numerator[0], multiply(T, kernel[0])) == ZERO
    alpha = first[0]
    scalar = -evaluate(d, alpha) * pow(evaluate(v, alpha), -1, P) % P
    assert scalar
    assert coefficients == tuple(scale(f, scalar) for f in kernel)
    assert d == scale(add(u, scale(v, -1)), scalar)

    fibers = {}
    for x in remaining:
        ratio = evaluate(u, x) * pow(evaluate(v, x), -1, P) % P
        fibers.setdefault(ratio, []).append(x)
    large = [(ratio, roots) for ratio, roots in fibers.items()
             if ratio != 1 and len(roots) >= 4]
    assert len(large) <= 1
    predicted = set(first + second)
    for ratio, roots in large:
        assert len(roots) <= 5
        fiber_polynomial = monic(add(u, scale(v, -ratio)))
        root_polynomial = base.root_polynomial(roots)
        if len(roots) == 4:
            residual = quotient(fiber_polynomial, root_polynomial)
            assert degree(residual) == 1 and residual[-1] == 1
            predicted.add(-residual[0] % P)
        else:
            assert fiber_polynomial == root_polynomial
            predicted.update(roots)
    decoded = {gamma for gamma in range(P) if evaluate(d, gamma) and
               sum(evaluate(f, gamma) == 0 for f in locators.values()) == 4}
    assert decoded == predicted
    assert len(predicted) in (10, 11, 15)
    return len(predicted), max(map(len, fibers.values()))


def supplied_pencils():
    rng = random.Random(SEED)
    partitions = set()
    for i in range(256):
        while True:
            permuted = rng.sample(H, 16)
            first, second = sorted((tuple(sorted(permuted[:5])),
                                    tuple(sorted(permuted[5:10]))))
            if (first, second) not in partitions:
                partitions.add((first, second))
                break
        a, b = two_block(first, second)
        yield "two_block", i, a, b, first + second
    for i in range(128):
        permuted = rng.sample(H, 16)
        e0 = tuple(rng.randrange(1, P) if x in permuted[:4] else 0 for x in H)
        e1 = tuple(rng.randrange(1, P) if x in permuted[4:8] else 0 for x in H)
        yield "two_four_error_points", i, e0, tuple((v - u) % P
                                                    for u, v in zip(e0, e1)), (0, 1)
    for i in range(128):
        ma = tuple(rng.randrange(P) for _ in range(8))
        mb = tuple(rng.randrange(P) for _ in range(8))
        yield "independent_moments", i, base.word_with_syndrome(ma), \
            base.word_with_syndrome(mb), ()


def algebra_controls():
    roots = tuple(range(16))
    candidate = base.root_polynomial(roots)
    synthetic = {x: base.root_polynomial(roots[(i + j) % 16] for j in range(4))
                 for i, x in enumerate(H)}
    r = resultant_product(synthetic)
    assert r == power(candidate, 4)
    assert target_power_root(r) == candidate
    assert equality_check(ONE, synthetic, r)
    repeated = {x: power((-i % P, 1), 4) for i, x in enumerate(H)}
    assert resultant_product(repeated) == r
    assert not equality_check(ONE, repeated, r)
    assert not equality_check((-3, 1), synthetic, r)
    # X^4-5 is irreducible: its second Frobenius gcd is 1, its fourth is all.
    quartic = (-5 % P, 0, 0, 0, 1)
    assert field_root_part(quartic, 2) == ONE
    assert field_root_part(quartic, 4) == quartic
    assert field_root_part(quartic, 20) == quartic
    assert field_root_part(quartic, 1) == ONE
    assert target_power_root(power(candidate, 3)) is None
    factors = squarefree_factors(multiply(power(candidate, 4), quartic))
    assert factors == {1: quartic, 4: candidate}
    # These manufactured quartics validate algebra only; no affine moments
    # producing them are asserted.


def main():
    algebra_controls()
    report = {"seed": SEED, "coefficient_field": 97, "target_extension_degree": 20,
              "scope": "512 supplied prime-subfield pencils; not exhaustive over inputs",
              "families": {}, "full_equality_candidates": []}
    best, score_best = None, -1
    for family, index, a, b, forced in supplied_pencils():
        stats = report["families"].setdefault(family, {
            "tested": 0, "zero_D": 0, "persistent_locator": 0,
            "resultant_degrees": Counter(), "derivative_gcd_degrees": Counter(),
            "squarefree_power_candidates": 0, "full_equality": 0,
            "multiplicity_four_degrees": Counter(), "regular_exact_count_cases": 0,
            "exact_counts_in_target_field": Counter()})
        stats["tested"] += 1
        d, coefficients, locators = base.locator(a, b)
        assert coefficients[-1] == d
        if family == "two_block":
            count, largest = audit_two_block(a, b, forced, d, coefficients, locators)
            stats.setdefault("fiber_prediction_counts", Counter())[count] += 1
            stats.setdefault("largest_ratio_fibers", Counter())[largest] += 1
            stats["divided_difference_identities_checked"] = \
                stats.get("divided_difference_identities_checked", 0) + 1
        if d == ZERO:
            stats["zero_D"] += 1
            continue
        if any(f == ZERO for f in locators.values()):
            stats["persistent_locator"] += 1
            continue
        for gamma in forced:
            assert evaluate(d, gamma)
            assert sum(evaluate(f, gamma) == 0 for f in locators.values()) == 4
        r = resultant_product(locators)
        stats["resultant_degrees"][degree(r)] += 1
        stats["derivative_gcd_degrees"][degree(gcd(r, derivative(r)))] += 1
        factors = squarefree_factors(r)
        four = factors.get(4, ONE)
        stats["multiplicity_four_degrees"][degree(four)] += 1
        radical = ONE
        for factor in factors.values():
            radical = multiply(radical, factor)
        regular = (gcd(radical, d) == ONE and
                   all(gcd(f, derivative(f)) == ONE for f in locators.values()))
        exact_count = None
        if regular:
            # With simple coordinate roots and D nonzero at every root,
            # product multiplicity four is exactly four distinct incidences.
            assert all(m <= 4 for m in factors)
            exact_count = degree(field_root_part(four, 20))
            stats["regular_exact_count_cases"] += 1
            stats["exact_counts_in_target_field"][exact_count] += 1
        candidate = target_power_root(r)
        if candidate is not None:
            stats["squarefree_power_candidates"] += 1
            if equality_check(d, locators, r):
                stats["full_equality"] += 1
                report["full_equality_candidates"].append({
                    "family": family, "index": index, "a": a, "b": b,
                    "P": candidate, "D": d, "locator_coefficients": coefficients})
        score = exact_count if exact_count is not None else -1
        if score > score_best:
            score_best = score
            best = {"family": family, "index": index, "a": a, "b": b,
                    "D": d, "locator_coefficients": coefficients,
                    "R": r, "squarefree_factors": factors,
                    "exact_bad_count_F_97_20": exact_count}
    assert sum(stats["tested"] for stats in report["families"].values()) == 512
    report["best_regular_pencil"] = best
    if best is not None:
        constraints = base.interpolation_constraints()
        bad, weights = base.original_event(best["a"], best["b"], constraints)
        locators = {x: add(add(add(add(best["locator_coefficients"][0],
                                      scale(best["locator_coefficients"][1], x)),
                                  scale(best["locator_coefficients"][2], x*x)),
                              scale(best["locator_coefficients"][3], x**3)),
                          scale(best["locator_coefficients"][4], x**4)) for x in H}
        decoded = {gamma for gamma in range(P) if evaluate(best["D"], gamma) and
                   sum(evaluate(f, gamma) == 0 for f in locators.values()) == 4}
        assert bad == decoded
        assert all(weights[gamma] == 4 for gamma in bad)
        four = best["squarefree_factors"].get(4, ONE)
        assert len(bad) == degree(field_root_part(four, 1))
        best["independent_original_event_F_97"] = sorted(bad)
        best["admissible_supports_checked"] = len(constraints)
    assert 97**20 // 2**128 == 15
    destination = Path(__file__).with_name("result.json")
    destination.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    for family, stats in report["families"].items():
        print(f"{family}: {json.dumps(stats, sort_keys=True)}")
    print(f"Full equality candidates: {len(report['full_equality_candidates'])}")
    print(f"Best regular pencil: {None if best is None else best['exact_bad_count_F_97_20']} "
          "bad parameters in F_(97^20).")
    print("PASS: power recognition, simple-root exclusions and exact extension splitting controls.")
    print("PASS: independent original-event audit of the best regular pencil.")
    print("No exhaustive search, global upper bound, or originality claim is inferred.")


if __name__ == "__main__":
    main()
