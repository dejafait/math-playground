"""Exact nonprime determinant-root branch for the saved disjoint triple.

Only nonzero fourth determinants and one-dimensional full-weight kernels
at roots in F_(97^20) are exhausted. Zero determinants, larger kernels
and arbitrary triples remain outside this finite generator. Conjugate
occurrences are counted, without asserting distinct projective pencils.
"""

from collections import Counter
from itertools import permutations
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("three_support", HERE / "three_support.py")
three = importlib.util.module_from_spec(spec)
spec.loader.exec_module(three)
alg, base = three.alg, three.base
P, H = base.P, base.H
SUPPORTS = ((1, 8, 12, 18), (22, 27, 33, 47), (50, 64, 70, 75))


def irreducible(f):
    n = alg.degree(f)
    assert n in (2, 3, 4) and f == alg.monic(f)
    if alg.field_root_part(f, n) != f:
        return False
    divisors = (1, 2) if n == 4 else (1,)
    return all(alg.field_root_part(f, d) == alg.ONE for d in divisors)


def small_factors(f):
    """Deterministic factorization of a squarefree degree-at-most-four f."""
    f = alg.monic(f)
    factors = []
    for t in range(P):
        if alg.degree(f) > 0 and not base.evaluate(f, t):
            factor = (-t % P, 1)
            factors.append(factor)
            f = alg.quotient(f, factor)
    n = alg.degree(f)
    if n in (2, 3):
        assert irreducible(f)
        factors.append(f)
    elif n == 4:
        quadratic_part = alg.field_root_part(f, 2)
        if quadratic_part == alg.ONE:
            assert irreducible(f)
            factors.append(f)
        else:
            assert quadratic_part == f
            # Split two irreducible quadratics by their quadratic characters.
            split = None
            for power in (1, 2, 3):
                for c in range(P):
                    trial = (c,) + (0,) * (power - 1) + (1,)
                    half = alg.powmod(trial, (P * P - 1) // 2, f)
                    g = alg.gcd(f, base.add(half, (-1,)))
                    if alg.degree(g) == 2:
                        split = g
                        break
                if split is not None:
                    break
            assert split is not None
            other = alg.quotient(f, split)
            assert irreducible(split) and irreducible(other)
            factors.extend((split, other))
    else:
        assert n == 0
    reconstructed = alg.ONE
    for factor in factors:
        reconstructed = base.multiply(reconstructed, factor)
    return factors, reconstructed


class Field:
    """F_97[alpha]/f, with exact coefficient tuples of fixed length."""

    def __init__(self, modulus):
        assert irreducible(modulus)
        self.modulus = modulus
        self.n = len(modulus) - 1
        self.zero = (0,) * self.n
        self.one = (1,) + (0,) * (self.n - 1)
        self.alpha = (0, 1) + (0,) * (self.n - 2)
        self.inverses = {self.one: self.one}

    def c(self, value):
        return (value % P,) + (0,) * (self.n - 1)

    def add(self, a, b):
        return tuple((x + y) % P for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x % P for x in a)

    def sub(self, a, b):
        return tuple((x - y) % P for x, y in zip(a, b))

    def scale(self, a, value):
        return tuple(x * value % P for x in a)

    def mul(self, a, b):
        if a == self.zero or b == self.zero:
            return self.zero
        if not any(a[1:]):
            return self.scale(b, a[0])
        if not any(b[1:]):
            return self.scale(a, b[0])
        r = [0] * (2 * self.n - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                r[i + j] += x * y
        for k in range(len(r) - 1, self.n - 1, -1):
            value = r[k] % P
            for j in range(self.n):
                r[k - self.n + j] -= value * self.modulus[j]
        return tuple(x % P for x in r[:self.n])

    def inv(self, a):
        assert a != self.zero
        if a not in self.inverses:
            r0, r1 = self.modulus, base.trim(a)
            t0, t1 = alg.ZERO, alg.ONE
            while r1 != alg.ZERO:
                q, r = alg.divmod_poly(r0, r1)
                r0, r1 = r1, r
                t0, t1 = t1, base.add(t0, base.scale(base.multiply(q, t1), -1))
            assert alg.degree(r0) == 0
            value = alg.divmod_poly(base.scale(t0, pow(r0[0], -1, P)), self.modulus)[1]
            result = value + (0,) * (self.n - len(value))
            assert self.mul(a, result) == self.one
            self.inverses[a] = result
        return self.inverses[a]

    def div(self, a, b):
        return self.mul(a, self.inv(b))

    def pow(self, a, exponent):
        r = self.one
        while exponent:
            if exponent & 1:
                r = self.mul(r, a)
            exponent >>= 1
            if exponent:
                a = self.mul(a, a)
        return r

    def eval_prime(self, polynomial, a):
        r = self.zero
        for c in reversed(polynomial):
            r = self.add(self.mul(r, a), self.c(c))
        return r


class Polynomials:
    def __init__(self, field):
        self.F = field
        self.zero = (field.zero,)
        self.one = (field.one,)
        self.t = (field.zero, field.one)

    def trim(self, f):
        f = list(f)
        while len(f) > 1 and f[-1] == self.F.zero:
            f.pop()
        return tuple(f)

    def prime(self, f):
        return self.trim([self.F.c(x) for x in f])

    def degree(self, f):
        return len(f) - 1 if f != self.zero else -1

    def add(self, f, g):
        return self.trim([self.F.add(f[i] if i < len(f) else self.F.zero,
                                    g[i] if i < len(g) else self.F.zero)
                          for i in range(max(len(f), len(g)))])

    def scale(self, f, value):
        return self.trim([self.F.mul(x, value) for x in f])

    def mul(self, f, g):
        if f == self.zero or g == self.zero:
            return self.zero
        r = [self.F.zero] * (len(f) + len(g) - 1)
        for i, x in enumerate(f):
            if x != self.F.zero:
                for j, y in enumerate(g):
                    if y != self.F.zero:
                        r[i + j] = self.F.add(r[i + j], self.F.mul(x, y))
        return self.trim(r)

    def power(self, f, exponent):
        r = self.one
        while exponent:
            if exponent & 1:
                r = self.mul(r, f)
            exponent >>= 1
            if exponent:
                f = self.mul(f, f)
        return r

    def divmod(self, f, g):
        assert g != self.zero
        r = list(f)
        q = [self.F.zero] * max(1, len(f) - len(g) + 1)
        inverse = self.F.inv(g[-1])
        while self.trim(r) != self.zero and len(r) >= len(g):
            k = len(r) - len(g)
            c = self.F.mul(r[-1], inverse)
            q[k] = c
            for j, value in enumerate(g):
                r[k + j] = self.F.sub(r[k + j], self.F.mul(c, value))
            r = list(self.trim(r))
        return self.trim(q), self.trim(r)

    def quotient(self, f, g):
        q, r = self.divmod(f, g)
        assert r == self.zero
        return q

    def monic(self, f):
        return self.scale(f, self.F.inv(f[-1])) if f != self.zero else f

    def gcd(self, f, g):
        while g != self.zero:
            f, g = g, self.divmod(f, g)[1]
        return self.monic(f)

    def derivative(self, f):
        return self.trim([self.F.scale(x, i) for i, x in enumerate(f)][1:]
                         or [self.F.zero])

    def evaluate(self, f, a):
        r = self.F.zero
        for c in reversed(f):
            r = self.F.add(self.F.mul(r, a), c)
        return r

    def powmod(self, f, exponent, modulus):
        r = self.one
        f = self.divmod(f, modulus)[1]
        while exponent:
            if exponent & 1:
                r = self.divmod(self.mul(r, f), modulus)[1]
            exponent >>= 1
            if exponent:
                f = self.divmod(self.mul(f, f), modulus)[1]
        return r

    def field_roots(self, f, extension_degree=20):
        if self.degree(f) == 0:
            return self.one
        assert self.gcd(f, self.derivative(f)) == self.one
        frobenius = self.divmod(self.t, f)[1]
        for _ in range(extension_degree):
            frobenius = self.powmod(frobenius, P, f)
        return self.gcd(f, self.add(frobenius, self.scale(self.t, self.F.c(-1))))

    def squarefree(self, f):
        assert 0 <= self.degree(f) < P
        original = self.monic(f)
        repeated = self.gcd(original, self.derivative(original))
        remaining = self.quotient(original, repeated)
        result, m = {}, 1
        while remaining != self.one:
            common = self.gcd(remaining, repeated)
            factor = self.quotient(remaining, common)
            if factor != self.one:
                result[m] = factor
                assert self.gcd(factor, self.derivative(factor)) == self.one
            remaining = common
            repeated = self.quotient(repeated, common)
            m += 1
        assert repeated == self.one
        reconstructed = self.one
        for m, factor in result.items():
            reconstructed = self.mul(reconstructed, self.power(factor, m))
        assert reconstructed == original
        return result

    def determinant(self, matrix):
        result = self.zero
        for perm in permutations(range(len(matrix))):
            sign = (-1) ** sum(perm[i] > perm[j]
                               for i in range(len(perm)) for j in range(i + 1, len(perm)))
            term = self.one
            for i, j in enumerate(perm):
                term = self.mul(term, matrix[i][j])
            result = self.add(result, self.scale(term, self.F.c(sign)))
        return result


def rref(F, matrix):
    rows = [list(row) for row in matrix]
    width, pivots = len(rows[0]), []
    for column in range(width):
        pivot = next((i for i in range(len(pivots), len(rows))
                      if rows[i][column] != F.zero), None)
        if pivot is None:
            continue
        k = len(pivots)
        rows[k], rows[pivot] = rows[pivot], rows[k]
        inverse = F.inv(rows[k][column])
        rows[k] = [F.mul(x, inverse) for x in rows[k]]
        for i in range(len(rows)):
            if i != k:
                factor = rows[i][column]
                if factor != F.zero:
                    rows[i] = [F.sub(x, F.mul(factor, y)) for x, y in zip(rows[i], rows[k])]
        pivots.append(column)
    return rows, pivots


def kernel(F, matrix):
    rows, pivots = rref(F, matrix)
    result = []
    for free in range(len(rows[0])):
        if free in pivots:
            continue
        vector = [F.zero] * len(rows[0])
        vector[free] = F.one
        for i, pivot in enumerate(pivots):
            vector[pivot] = F.neg(rows[i][free])
        assert all(dot(F, row, vector) == F.zero for row in matrix)
        result.append(tuple(vector))
    return len(pivots), result


def dot(F, a, b):
    result = F.zero
    for x, y in zip(a, b):
        result = F.add(result, F.mul(x, y))
    return result


def syndrome(F, word):
    return tuple(dot(F, word, [F.c(pow(x, j, P)) for x in H]) for j in range(1, 9))


def word_on(F, support, weights):
    return tuple(weights[support.index(x)] if x in support else F.zero for x in H)


def actual_locator(R, u, v):
    s = [R.trim((x, y)) for x, y in zip(u, v)]
    rows = [[s[i + j] for j in range(5)] for i in range(4)]
    coefficients = tuple(R.scale(R.determinant([[row[j] for j in range(5) if j != k]
                                                for row in rows]), R.F.c((-1) ** k))
                         for k in range(5))
    locators = {x: R.zero for x in H}
    for x in H:
        for j, f in enumerate(coefficients):
            locators[x] = R.add(locators[x], R.scale(f, R.F.c(pow(x, j, P))))
    # The four recurrence identities are checked as polynomial identities.
    for i in range(4):
        residual = R.zero
        for j, f in enumerate(coefficients):
            residual = R.add(residual, R.mul(f, s[i + j]))
        assert residual == R.zero
    return coefficients[-1], coefficients, locators


def scalar_det(F, matrix):
    """Independent scalar elimination, rather than signed minor expansion."""
    rows = [list(row) for row in matrix]
    answer = F.one
    for j in range(len(rows)):
        pivot = next((i for i in range(j, len(rows)) if rows[i][j] != F.zero), None)
        if pivot is None:
            return F.zero
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            answer = F.neg(answer)
        value = rows[j][j]
        answer = F.mul(answer, value)
        inverse = F.inv(value)
        for i in range(j + 1, len(rows)):
            factor = F.mul(rows[i][j], inverse)
            for k in range(j + 1, len(rows)):
                rows[i][k] = F.sub(rows[i][k], F.mul(factor, rows[j][k]))
    return answer


def coefficient_power(R, product):
    if R.degree(product) != 64:
        return None, {"degree_gate": False}
    normalized = R.monic(product)
    reverse = [R.F.one]
    for j in range(1, 17):
        earlier = R.power(R.trim(reverse), 4)
        known = earlier[j] if j < len(earlier) else R.F.zero
        reverse.append(R.F.scale(R.F.sub(normalized[64 - j], known), pow(4, -1, P)))
    candidate = R.trim(list(reversed(reverse)))
    fourth = R.power(candidate, 4)
    assert all(fourth[64 - j] == normalized[64 - j] for j in range(17))
    failed = [j for j in range(17, 65) if fourth[64 - j] != normalized[64 - j]]
    return candidate, {"degree_gate": True, "failed_residuals": failed,
                       "power_identity": not failed}


def chart(R, u, v, coefficients, locators):
    F = R.F
    tau = next(t for t in range(P) if R.evaluate(coefficients[4], F.c(t)) != F.zero
               and all(R.evaluate(f, F.c(t)) != F.zero for f in locators.values()))

    def transform(f):
        result = R.zero
        for h, value in enumerate(f):
            monomial = (F.zero,) * h + (F.scale(value, pow(tau, h, P)),)
            result = R.add(result, R.mul(monomial, R.power(R.prime((1, 1)), 4 - h)))
        return result

    coefficients = tuple(transform(f) for f in coefficients)
    locators = {x: transform(f) for x, f in locators.items()}
    new_v = tuple(F.add(x, F.scale(y, tau)) for x, y in zip(u, v))
    assert R.degree(coefficients[4]) == 4
    assert all(R.degree(f) == 4 for f in locators.values())
    return new_v, tau, coefficients, locators


def audit(F, a, b, fourth, alpha):
    R = Polynomials(F)
    u, v = syndrome(F, a), syndrome(F, b)
    d, coefficients, locators = actual_locator(R, u, v)
    assert d != R.zero and all(f != R.zero for f in locators.values())
    for t, support in zip((F.c(0), F.c(1), F.c(2), alpha), SUPPORTS + (fourth,)):
        assert R.evaluate(d, t) != F.zero
        assert tuple(x for x in H if R.evaluate(locators[x], t) == F.zero) == support
    # Independent determinants at five points check all signed-minor coefficients.
    for t in range(5):
        moments = [F.add(x, F.scale(y, t)) for x, y in zip(u, v)]
        rows = [[moments[i + j] for j in range(5)] for i in range(4)]
        for k, f in enumerate(coefficients):
            expected = F.scale(scalar_det(F, [[row[j] for j in range(5) if j != k]
                                              for row in rows]), (-1) ** k)
            assert expected == R.evaluate(f, F.c(t))
    v, tau, coefficients, locators = chart(R, u, v, coefficients, locators)
    d = coefficients[4]
    product = R.one
    radicals, common = R.one, R.zero
    coordinate_squarefree = True
    for f in locators.values():
        product = R.mul(product, f)
        repeated = R.gcd(f, R.derivative(f))
        coordinate_squarefree &= repeated == R.one
        radicals = R.mul(radicals, R.monic(R.quotient(f, repeated)))
        common = R.gcd(common, f)
    candidate, power_check = coefficient_power(R, product)
    decomposition = R.squarefree(product)
    power_by_multiplicity = (set(decomposition) == {4}
                             and R.degree(decomposition[4]) == 16)
    assert power_check["power_identity"] == power_by_multiplicity
    if power_by_multiplicity:
        assert candidate == decomposition[4]
    candidate_squarefree = R.gcd(candidate, R.derivative(candidate)) == R.one
    candidate_field_part = R.field_roots(R.quotient(candidate, R.gcd(candidate, R.derivative(candidate))))
    candidate_split = candidate_squarefree and candidate_field_part == candidate
    candidate_regular = R.gcd(candidate, d) == R.one
    equality = (power_by_multiplicity and coordinate_squarefree and candidate_squarefree
                and candidate_split and candidate_regular)
    # Distinct coordinate incidences, even when an unrelated root repeats.
    regular_four = R.squarefree(radicals).get(4, R.one)
    regular_four = R.quotient(regular_four, R.gcd(regular_four, d))
    in_target = R.field_roots(regular_four)
    in_coefficient = R.field_roots(regular_four, F.n)
    no_lower = common == R.one
    # These four known points give an independent polynomial comparison
    # whenever the exhaustive incidence calculation finds degree four.
    if R.degree(regular_four) == 4:
        prescribed = R.one
        for t in (F.c(0), F.c(1), F.c(2), alpha):
            new_t = F.div(t, F.sub(F.c(tau), t))
            prescribed = R.mul(prescribed, (F.neg(new_t), F.one))
        assert regular_four == prescribed
    return {"modulus": F.modulus, "fourth_support": fourth,
            "alpha": alpha, "a_original_chart": a, "b_original_chart": b,
            "new_infinity_old_parameter": tau, "moments_u": u, "moments_v": v,
            "D": d, "locator_coefficients": coefficients,
            "resultant": product, "coefficient_power_audit": power_check,
            "coordinate_squarefree": coordinate_squarefree,
            "candidate_squarefree": candidate_squarefree,
            "candidate_split_in_target_field": candidate_split,
            "candidate_D_coprime": candidate_regular,
            "full_L010_equality": equality,
            "multiplicity_four_polynomial": regular_four,
            "target_field_weight_four_polynomial": in_target,
            "weight_four_count_algebraic_closure": R.degree(regular_four),
            "weight_four_count_target_field": R.degree(in_target),
            "weight_four_count_coefficient_field": R.degree(in_coefficient),
            "lower_weights_excluded": no_lower,
            "exact_total_count_target_field": R.degree(in_target) if no_lower else None,
            "actual_minors_independently_checked": True,
            "affine_recurrences_checked": True}


def independent_event(record):
    """Original same-support event over its exact coefficient field."""
    F = Field(tuple(record["modulus"]))
    a = tuple(tuple(x) for x in record["a_original_chart"])
    old_b = tuple(tuple(x) for x in record["b_original_chart"])
    tau = record["new_infinity_old_parameter"]
    b = tuple(F.add(x, F.scale(y, tau)) for x, y in zip(a, old_b))
    bad, weights = set(), {}
    constraints = base.interpolation_constraints()
    for anchor, equations, support in constraints:
        def residual(word):
            return tuple(F.sub(word[i], dot(F, [F.c(c) for c in cs], [word[j] for j in anchor]))
                         for i, cs in equations)
        ra, rb = residual(a), residual(b)
        if any(x != F.zero for x in rb):
            first = next(i for i, x in enumerate(rb) if x != F.zero)
            t = F.neg(F.div(ra[first], rb[first]))
            if all(F.add(x, F.mul(t, y)) == F.zero for x, y in zip(ra, rb)):
                bad.add(t)
                weights[t] = min(weights.get(t, 16), 16 - len(support))
        elif all(x == F.zero for x in ra):
            raise AssertionError("Whole pencil agrees on an admissible support")
    R = Polynomials(F)
    polynomial = tuple(tuple(x) for x in record["target_field_weight_four_polynomial"])
    assert record["lower_weights_excluded"]
    for t in bad:
        assert weights[t] == 4
        assert R.evaluate(polynomial, t) == F.zero
    assert len(bad) == record["weight_four_count_coefficient_field"]
    record["independent_original_event_parameters_new_chart"] = sorted(bad)
    old_parameters = [F.div(F.scale(t, tau), F.add(F.one, t))
                      for t in bad if t != F.c(-1)]
    record["independent_original_event_parameters_original_chart"] = sorted(old_parameters)
    record["original_infinity_is_bad"] = F.c(-1) in bad
    record["independent_original_event_supports_checked"] = len(constraints)
    record["target_parameters_outside_coefficient_field"] = (
        record["weight_four_count_target_field"] - len(bad))


def controls():
    alg.algebra_controls()
    for modulus in ((-5 % P, 0, 1), (-5 % P, 0, 0, 0, 1)):
        F, R = Field(modulus), None
        R = Polynomials(F)
        assert F.eval_prime(modulus, F.alpha) == F.zero
        assert F.pow(F.alpha, P ** F.n) == F.alpha
        assert F.pow(F.alpha, P ** 20) == F.alpha
        assert F.pow(F.alpha, P ** (F.n // 2)) != F.alpha
        for a in (F.alpha, F.add(F.alpha, F.one), F.pow(F.alpha, 3)):
            assert F.inv(a) == F.pow(a, P ** F.n - 2)
        # Separate prime-polynomial multiplication/reduction checks the
        # custom field reduction on nonconstant element pairs.
        elements = [F.pow(F.add(F.alpha, F.c(i)), i + 1) for i in range(6)]
        for a in elements:
            for b in elements:
                reference = alg.divmod_poly(base.multiply(a, b), modulus)[1]
                reference += (0,) * (F.n - len(reference))
                assert F.mul(a, b) == reference
        # Cross-check the new ring on embedded prime-field polynomials.
        f, g = (2, 4, 6, 8), (9, 3, 7)
        assert R.mul(R.prime(f), R.prime(g)) == R.prime(base.multiply(f, g))
        assert R.gcd(R.prime(f), R.prime(g)) == R.prime(alg.gcd(f, g))
        synthetic = R.power(R.trim((F.neg(F.alpha), F.one)), 4)
        sf = R.squarefree(synthetic)
        assert sf == {4: R.trim((F.neg(F.alpha), F.one))}
        assert R.field_roots(sf[4]) == sf[4]
    for f in ((-5 % P, 0, 0, 0, 1), (1, 0, 1), (0, -1 % P, 0, 0, 1)):
        radical = alg.monic(alg.quotient(f, alg.gcd(f, alg.derivative(f))))
        factors, rebuilt = small_factors(radical)
        assert rebuilt == radical and factors


def main():
    controls()
    basis, initial, direction = three.triple_space(SUPPORTS)
    stats = Counter()
    degree_stats = {2: Counter(), 4: Counter()}
    records, root_certificate, zero_systems = [], [], []
    best = None
    for index, fourth in enumerate(three.SUPPORTS):
        if fourth in SUPPORTS:
            continue
        stats["fourth_supports"] += 1
        matrix = three.fourth_matrix(fourth, initial, direction)
        determinant = base.determinant(matrix)
        for t in range(5):
            assert three.scalar_determinant([[base.evaluate(f, t) for f in row] for row in matrix]) == base.evaluate(determinant, t)
        if determinant == alg.ZERO:
            zero_systems.append(fourth)
            continue
        radical = alg.monic(alg.quotient(determinant, alg.gcd(determinant, alg.derivative(determinant))))
        factors, rebuilt = small_factors(radical)
        assert rebuilt == radical
        expected_nonprime = alg.degree(alg.field_root_part(radical, 20)) - alg.degree(alg.field_root_part(radical, 1))
        selected = [f for f in factors if alg.degree(f) in (2, 4)]
        assert sum(alg.degree(f) for f in selected) == expected_nonprime
        stats["target_field_nonprime_root_occurrences"] += expected_nonprime
        for factor in selected:
            n = alg.degree(factor)
            ds = degree_stats[n]
            ds["irreducible_factor_occurrences"] += 1
            ds["conjugate_root_occurrences"] += n
            F = Field(factor)
            alpha = F.alpha
            assert F.eval_prime(factor, alpha) == F.zero
            assert F.pow(alpha, P ** 20) == alpha
            numerical = [[F.eval_prime(f, alpha) for f in row] for row in matrix]
            rank, kernels = kernel(F, numerical)
            assert rank < 4 and kernels
            certificate = {"fourth_support": fourth, "determinant": determinant,
                           "irreducible_factor": factor, "rank": rank}
            root_certificate.append(certificate)
            if len(kernels) != 1:
                ds["larger_kernels_unsearched"] += 1
                certificate["gate"] = "larger_kernel_unsearched"
                continue
            weights = tuple(dot(F, kernels[0], [F.c(z[j]) for z in basis]) for j in range(12))
            certificate["triple_weights"] = weights
            if any(x == F.zero for x in weights):
                ds["zero_triple_weight"] += 1
                certificate["gate"] = "zero_triple_weight"
                continue
            e0 = word_on(F, SUPPORTS[0], weights[:4])
            e1 = word_on(F, SUPPORTS[1], weights[4:8])
            e2 = word_on(F, SUPPORTS[2], weights[8:])
            a, b = e0, tuple(F.sub(y, x) for x, y in zip(e0, e1))
            u, v = syndrome(F, a), syndrome(F, b)
            assert tuple(F.add(x, F.scale(y, 2)) for x, y in zip(u, v)) == syndrome(F, e2)
            target = tuple(F.add(x, F.mul(alpha, y)) for x, y in zip(u, v))
            rows, pivots = rref(F, [[F.c(pow(x, j, P)) for x in fourth] + [target[j - 1]]
                                   for j in range(1, 5)])
            assert pivots == [0, 1, 2, 3]
            fourth_weights = tuple(row[-1] for row in rows)
            certificate["fourth_weights"] = fourth_weights
            assert syndrome(F, word_on(F, fourth, fourth_weights)) == target
            if any(x == F.zero for x in fourth_weights):
                ds["zero_fourth_weight"] += 1
                certificate["gate"] = "zero_fourth_weight"
                continue
            certificate["gate"] = "full_weight_actual_pencil"
            ds["full_weight_actual_pencils"] += 1
            record = audit(F, a, b, fourth, alpha)
            record["triple_weights"] = weights
            record["fourth_weights"] = fourth_weights
            records.append(record)
            ds["power_identity"] += int(record["coefficient_power_audit"]["power_identity"])
            ds["full_equality"] += int(record["full_L010_equality"])
            count = record["exact_total_count_target_field"]
            ds[f"exact_total_count_{count}"] += 1
            if count is not None and (best is None or count > best["exact_total_count_target_field"]):
                best = record
        if (index + 1) % 128 == 0:
            print(f"fourth supports {index + 1}/1820; nonprime occurrences {stats['target_field_nonprime_root_occurrences']}; "
                  f"actual representatives {len(records)}; best exact count "
                  f"{None if best is None else best['exact_total_count_target_field']}", flush=True)
            write_report(stats, degree_stats, records, root_certificate, zero_systems, best, False)
    assert stats["fourth_supports"] == 1817
    assert stats["target_field_nonprime_root_occurrences"] == 402
    assert len(zero_systems) == 4
    # These are the exact finite conclusions used in the fixed-branch
    # restriction, rather than an assumption in candidate generation.
    assert len(root_certificate) == len(records) == 201
    assert not degree_stats[4]
    assert all(c["rank"] == 3 and c["gate"] == "full_weight_actual_pencil"
               and alg.degree(c["irreducible_factor"]) == 2 for c in root_certificate)
    assert all(r["weight_four_count_algebraic_closure"] == 4
               and r["exact_total_count_target_field"] == 4
               and r["lower_weights_excluded"] and not r["full_L010_equality"]
               for r in records)
    if best is not None:
        independent_event(best)
    write_report(stats, degree_stats, records, root_certificate, zero_systems, best, True)
    print(f"PASS: all 402 nonprime root occurrences; {len(records)} full-weight factor representatives.")
    print(f"PASS: actual minors, recurrence identities, complete power/equality and exact F_(97^20) gates.")
    print(f"degree statistics: {json.dumps(degree_stats, sort_keys=True)}")
    print(f"Best exact count: {None if best is None else best['exact_total_count_target_field']}.")
    print("Four zero-determinant systems and arbitrary triples remain unsearched; no global count improvement.")


def write_report(stats, degree_stats, records, certificate, zero_systems, best, completed):
    result = {"scope": "Saved disjoint triple: nonprime roots of nonzero fourth determinants, one representative per irreducible factor; no distinct-line claim.",
              "completed": completed, "supports": SUPPORTS, "target_extension_degree": 20,
              "counts": stats, "degree_statistics": degree_stats,
              "zero_determinant_supports_unsearched": zero_systems,
              "root_certificate": certificate, "actual_pencil_audits": records,
              "best_exact_pencil": best}
    (HERE / "extension-root-result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
