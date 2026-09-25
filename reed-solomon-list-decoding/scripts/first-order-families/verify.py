#!/usr/bin/env python3
"""Finite algebra/counting checks for L008; the general proof is in the lemma."""

from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
from random import Random


class Field:
    """Small finite fields, with low-to-high coefficients for a monic modulus."""

    def __init__(self, p, modulus):
        self.p, self.modulus = p, modulus
        self.r = len(modulus) - 1
        self.q = p ** self.r
        digits = [tuple((a // p**i) % p for i in range(self.r))
                  for a in range(self.q)]
        self.add = [[sum(((x + y) % p) * p**i
                         for i, (x, y) in enumerate(zip(aa, bb)))
                     for bb in digits] for aa in digits]
        self.neg = [sum((-x % p) * p**i for i, x in enumerate(aa))
                    for aa in digits]
        self.mul = []
        for aa in digits:
            row = []
            for bb in digits:
                raw = [0] * (2 * self.r - 1)
                for i, x in enumerate(aa):
                    for j, y in enumerate(bb):
                        raw[i + j] = (raw[i + j] + x * y) % p
                for t in range(len(raw) - 1, self.r - 1, -1):
                    factor = raw[t]
                    for j in range(self.r + 1):
                        raw[t - self.r + j] = (
                            raw[t - self.r + j] - factor * modulus[j]) % p
                row.append(sum(raw[i] * p**i for i in range(self.r)))
            self.mul.append(row)
        self.inv = [0] + [self.power(a, self.q - 2) for a in range(1, self.q)]
        # This also checks that the chosen quotient rings are fields.
        assert all(self.mul[a][self.inv[a]] == 1 for a in range(1, self.q))

    def power(self, a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul[result][a]
            a = self.mul[a][a]
            exponent //= 2
        return result


def trim(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def add(f, u, v):
    return trim(f.add[u[i] if i < len(u) else 0][v[i] if i < len(v) else 0]
                for i in range(max(len(u), len(v))))


def scale(f, scalar, u):
    return trim(f.mul[scalar][x] for x in u)


def multiply(f, u, v):
    if not u or not v:
        return ()
    out = [0] * (len(u) + len(v) - 1)
    for i, x in enumerate(u):
        for j, y in enumerate(v):
            out[i + j] = f.add[out[i + j]][f.mul[x][y]]
    return trim(out)


def derivative(f, u):
    return trim(f.mul[i % f.p][u[i]] for i in range(1, len(u)))


def evaluate(f, poly, x):
    out = 0
    for coefficient in reversed(poly):
        out = f.add[f.mul[out][x]][coefficient]
    return out


def operator(f, a, b, u):
    return add(f, multiply(f, a, derivative(f, u)), multiply(f, b, u))


def frobenius_poly(f, u):
    out = [0] * (f.p * max(0, len(u) - 1) + 1)
    for i, coefficient in enumerate(u):
        out[f.p * i] = coefficient
    return trim(out)


def kernel(f, a, b, k):
    columns = [operator(f, a, b, (0,) * j + (1,)) for j in range(k)]
    height = max(map(len, columns), default=0)
    matrix = [[col[i] if i < len(col) else 0 for col in columns]
              for i in range(height)]
    pivots = []
    for col in range(k):
        pivot = next((i for i in range(len(pivots), height) if matrix[i][col]), None)
        if pivot is None:
            continue
        row = len(pivots)
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        inverse = f.inv[matrix[row][col]]
        matrix[row] = [f.mul[inverse][x] for x in matrix[row]]
        for i in range(height):
            if i != row and matrix[i][col]:
                multiple = f.neg[matrix[i][col]]
                matrix[i] = [f.add[x][f.mul[multiple][y]]
                             for x, y in zip(matrix[i], matrix[row])]
        pivots.append(col)
    basis = []
    for col in range(k):
        if col not in pivots:
            vector = [0] * k
            vector[col] = 1
            for row, pivot in enumerate(pivots):
                vector[pivot] = f.neg[matrix[row][col]]
            basis.append(trim(vector))
    return basis


kernel_checks = 0
nontrivial_kernels = 0
for p, coefficient_count in ((2, 3), (3, 3), (5, 2)):
    f = Field(p, (0, 1))
    coefficients = [trim(u) for u in product(range(p), repeat=coefficient_count)]
    for a in coefficients:
        if not a:
            continue
        for b in coefficients:
            for k in (1, p, p + 1, 2 * p + 1):
                basis = kernel(f, a, b, k)
                kernel_checks += 1
                if not basis:
                    continue
                nontrivial_kernels += 1
                g = min(basis, key=len)
                g = scale(f, f.inv[g[-1]], g)
                d = len(g) - 1
                h = (k - 1 - d) // p
                # Independent nullspace dimension versus the proposed module.
                assert len(basis) == h + 1
                assert d <= (p - 1) * (len(a) - 1)
                for j in range(h + 1):
                    assert not operator(f, a, b, (0,) * (p * j) + g)
                for x in range(p):
                    if evaluate(f, g, x) == 0:
                        assert evaluate(f, a, x) == 0


affine_checks = 0
f = Field(3, (0, 1))
k = 7
for a, b in (((1,), ()), ((0, 1), (2,)), ((1,), (1,)),
             ((2, 1, 1), (2, 1))):
    p0 = (1, 2, 0, 1, 1)
    right = operator(f, a, b, p0)
    actual = {trim(u) for u in product(range(f.q), repeat=k)
              if operator(f, a, b, trim(u)) == right}
    basis = kernel(f, a, b, k)
    if basis:
        g = min(basis, key=len)
        h = (k - len(g)) // f.p
        predicted = {add(f, p0, multiply(f, g, frobenius_poly(f, trim(u))))
                     for u in product(range(f.q), repeat=h + 1)}
    else:
        predicted = {p0}
    assert actual == predicted
    affine_checks += 1
# The coefficient of X^(p-1) in a derivative is always zero.
assert not any(operator(f, (1,), (), trim(u)) == (0, 0, 1)
               for u in product(range(f.q), repeat=k))
affine_checks += 1


f = Field(3, (1, 0, 1))  # F_9, with T^2+1=0.
domain = tuple(range(1, f.q))
n, k = len(domain), 5
g = (2, 1)  # X-1: one evaluation zero, two residual H coefficients.
g_values = [evaluate(f, g, x) for x in domain]
zeros = [i for i, value in enumerate(g_values) if value == 0]
remaining = [i for i, value in enumerate(g_values) if value]
hs = [trim(u) for u in product(range(f.q), repeat=2)]
h_values = [[evaluate(f, h, f.power(x, f.p)) for x in domain] for h in hs]
count_checks = 0
random = Random(20260925)
for m in (1, 2):
    p0 = [(j + 1, 0, 1) for j in range(m)]
    base = [[evaluate(f, p0[j], x) for j in range(m)] for x in domain]
    candidates = []
    for indices in product(range(len(hs)), repeat=m):
        polynomials = [add(f, p0[j], multiply(f, g, frobenius_poly(f, hs[index])))
                       for j, index in enumerate(indices)]
        raw = [tuple(evaluate(f, poly, x) for poly in polynomials) for x in domain]
        shortened = [tuple(h_values[index][i] for index in indices) for i in remaining]
        candidates.append((raw, shortened))
    centers = [list(candidates[t][0]) for t in (0, 1, len(candidates) - 1)]
    for _ in range(12):
        center = list(candidates[random.randrange(len(candidates))][0])
        for i in random.sample(range(n), random.randrange(1, n + 1)):
            center[i] = tuple(random.randrange(f.q) for _ in range(m))
        centers.append(center)
    for center in centers:
        z = sum(center[i] == tuple(base[i]) for i in zeros)
        transformed = [tuple(f.mul[f.inv[g_values[i]]][f.add[center[i][j]][f.neg[base[i][j]]]]
                             for j in range(m)) for i in remaining]
        full_histogram = Counter()
        short_histogram = Counter()
        for raw, shortened in candidates:
            full_histogram[sum(x == y for x, y in zip(raw, center))] += 1
            short_histogram[z + sum(x == y for x, y in zip(shortened, transformed))] += 1
        assert full_histogram == short_histogram
        for agreement in range(k, n + 1):
            size = sum(value for key, value in full_histogram.items() if key >= agreement)
            a0, length, h = agreement - z, len(remaining), 1
            if a0 > length:
                assert size == 0
            elif a0 * a0 > length * h:
                assert size <= (length * (a0 - h)) // (a0 * a0 - length * h)
            count_checks += 1


slack_checks = 0
for n in (16, 32, 64, 128, 256, 512, 1024):
    for rate_denominator in (2, 4, 8, 16):
        k = n // rate_denominator
        c, gamma = Fraction(n - k, n), Fraction(1, 10)
        agreement = k + (n + 9) // 10
        for p in (3, 5, 7, 11, 13, 17):
            # A negative discriminant proves gamma lies above the lower
            # sufficient-slack root, without approximating a square root.
            assert 4 * p * gamma**2 - 4 * p * c * gamma + c**2 < 0
            for e in range(k):
                h, length = (k - 1 - e) // p, n - e
                denominator = (agreement - e)**2 - length * h
                assert 3 * denominator >= length
                bound = Fraction(length * (agreement - e - h), denominator)
                assert bound <= 3 * n
                slack_checks += 1
negative_example = {"n": 32, "k": 16, "p": 3, "d": 12, "e": 12}
assert (16 - 12)**2 - (32 - 12) * ((16 - 1 - 12) // 3) == -4
negative_example["denominator_at_A_k"] = -4


f = Field(3, (2, 1, 0, 0, 1))  # F_81, T^4+T+2.
primitive = next(a for a in range(1, f.q)
                 if f.power(a, 40) != 1 and f.power(a, 16) != 1)
root = f.power(primitive, 5)
domain = [f.power(root, i) for i in range(16)]
assert len(set(domain)) == 16 and f.power(root, 16) == 1
g = (1,)
for x in domain[:7]:
    g = multiply(f, g, (f.neg[x], 1))
b = scale(f, f.neg[1], derivative(f, g))
assert not operator(f, g, b, g)
values = [evaluate(f, g, x) for x in domain]
center = [0] * 7 + [f.mul[values[i]][i - 7] for i in range(7, 16)]
agreements = [sum(f.mul[scalar][value] == y for value, y in zip(values, center))
              for scalar in range(f.q)]
assert sum(a >= 8 for a in agreements) == 9
attained_example = {"p": 3, "q": 81, "n": 16, "k": 8,
                    "e": 7, "h": 0, "family_size": 81,
                    "list_size_at_A_k": 9, "bound": 9,
                    "domain": domain, "g_coefficients": list(g),
                    "received_word": center}


result = {
    "scope": "Finite algebra/counting checks only; the general informal proof is L008.",
    "kernel_checks": kernel_checks,
    "nontrivial_kernels": nontrivial_kernels,
    "exhaustive_affine_fiber_checks": affine_checks,
    "shortened_list_checks": count_checks,
    "shortened_list_scope": "F_9, n=8, k=5, m=1,2; all family codewords, 15 centers per m.",
    "rational_slack_checks": slack_checks,
    "rational_slack": "1/10",
    "negative_denominator_example": negative_example,
    "attained_smooth_example": attained_example,
}
Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"Passed {kernel_checks} kernel, {affine_checks} affine, {count_checks} shortened-list, "
      f"and {slack_checks} slack checks; the smooth example attains list size 9.")
