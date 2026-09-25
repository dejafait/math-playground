#!/usr/bin/env python3
"""Exact finite checks for L009; neither these tests nor raw solution counts
determine an agreement-filtered Reed--Solomon list boundary.
"""

from itertools import product
import json
from pathlib import Path


class Field:
    def __init__(self, p, modulus):
        self.p, self.r = p, len(modulus) - 1
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


def sub(f, u, v):
    return add(f, u, scale(f, f.neg[1], v))


def mul(f, u, v):
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


def monic(f, u):
    return scale(f, f.inv[u[-1]], u) if u else ()


def divide(f, u, v):
    assert v
    remainder = trim(u)
    quotient = [0] * max(0, len(u) - len(v) + 1)
    while remainder and len(remainder) >= len(v):
        shift = len(remainder) - len(v)
        coefficient = f.mul[remainder[-1]][f.inv[v[-1]]]
        quotient[shift] = coefficient
        remainder = sub(f, remainder, (0,) * shift + scale(f, coefficient, v))
    return trim(quotient), remainder


def exact(f, u, v):
    quotient, remainder = divide(f, u, v)
    assert not remainder
    return quotient


def gcd(f, u, v):
    while v:
        u, v = v, divide(f, u, v)[1]
    return monic(f, u)


def kernel(f, a, c0):
    # L008 bounds the minimal generator by (p-1) deg(a). Nullspace
    # computation here is independent of the divisor reconstruction.
    width = (f.p - 1) * (len(a) - 1) + 1
    columns = [sub(f, mul(f, a, derivative(f, (0,) * j + (1,))),
                   mul(f, c0, (0,) * j + (1,))) for j in range(width)]
    height = max(map(len, columns), default=0)
    matrix = [[col[i] if i < len(col) else 0 for col in columns]
              for i in range(height)]
    pivots = []
    for col in range(width):
        pivot = next((i for i in range(len(pivots), height) if matrix[i][col]), None)
        if pivot is None:
            continue
        row = len(pivots)
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        inverse = f.inv[matrix[row][col]]
        matrix[row] = [f.mul[inverse][x] for x in matrix[row]]
        for i in range(height):
            if i != row and matrix[i][col]:
                scalar = f.neg[matrix[i][col]]
                matrix[i] = [f.add[x][f.mul[scalar][y]]
                             for x, y in zip(matrix[i], matrix[row])]
        pivots.append(col)
    basis = []
    for col in range(width):
        if col not in pivots:
            vector = [0] * width
            vector[col] = 1
            for row, pivot in enumerate(pivots):
                vector[pivot] = f.neg[matrix[row][col]]
            basis.append(trim(vector))
    return monic(f, min(basis, key=len)) if basis else ()


def divisors(f, polynomial):
    remaining = monic(f, polynomial)
    factors = []
    degree = 1
    while 2 * degree <= len(remaining) - 1:
        for coefficients in product(range(f.q), repeat=degree):
            candidate = coefficients + (1,)
            exponent = 0
            while len(remaining) >= len(candidate):
                quotient, remainder = divide(f, remaining, candidate)
                if remainder:
                    break
                exponent += 1
                remaining = quotient
            if exponent:
                factors.append((candidate, exponent))
        degree += 1
    if len(remaining) > 1:
        factors.append((remaining, 1))
    out = [(1,)]
    for factor, exponent in factors:
        previous, power = out, (1,)
        out = []
        for _ in range(exponent + 1):
            out.extend(mul(f, term, power) for term in previous)
            power = mul(f, power, factor)
    assert len(out) == len(set(out))
    assert all(not divide(f, polynomial, t)[1] for t in out)
    return out


def residual(f, a, b, c, d, polynomial):
    return add(f, add(f, mul(f, a, derivative(f, polynomial)),
                      mul(f, b, mul(f, polynomial, polynomial))),
               add(f, mul(f, c, polynomial), d))


cases = []
for p in (3, 5):
    f = Field(p, (0, 1))
    aa = (0, p - 1) + (0,) * (p - 2) + (1,)
    cases.extend([
        (f, p, (1,), (1,), (), (), "singleton"),
        (f, p, (1,), (1,), (), (p - 1,), "two_without_homogeneous"),
        (f, p, (0, 0, 1), (1,), (), (), "two_with_homogeneous"),
        (f, p, aa, (1,), (1,), (), "split_additive"),
    ])
f = Field(3, (0, 1))
aa = (0, 2, 0, 1)
cases.append((f, 4, (1,), (1,), (), (1,), "empty"))
for shift in ((1, 1), (2, 1, 0, 1), (0, 0, 0, 0, 1)):
    cc = sub(f, (1,), scale(f, 2, shift))
    dd = sub(f, sub(f, mul(f, shift, shift), shift),
             mul(f, aa, derivative(f, shift)))
    cases.append((f, 5, aa, (1,), cc, dd, "translated"))
for zz in ((0, 1), (1, 0, 1)):
    cases.append((f, 6, mul(f, aa, zz), (1,),
                  sub(f, zz, mul(f, aa, derivative(f, zz))), (), "rescaled_unknown"))
cases.append((f, 5, mul(f, aa, (1, 1)), (1, 1), (1, 1), (), "common_factor"))
cases.append((f, 9, (0, 2) + (0,) * 7 + (1,), (1,), (1,), (), "degree_nine"))
f9 = Field(3, (1, 0, 1))
cases.append((f9, 3, aa, (1,), (1,), (), "extension_field"))

records = []
tested_polynomials = tested_divisors = recovered_parameters = 0
for f, k, a, b, c, d, label in cases:
    actual = {trim(poly) for poly in product(range(f.q), repeat=k)
              if not residual(f, a, b, c, d, trim(poly))}
    tested_polynomials += f.q ** k
    record = {"case": label, "q": f.q, "k": k, "solutions": len(actual)}
    if len(actual) < 2:
        records.append(record)
        continue
    p0, p1 = sorted(actual, key=lambda poly: (len(poly), poly))[:2]
    c0 = add(f, scale(f, 2, mul(f, b, p0)), c)
    gg = kernel(f, a, c0)
    if not gg:
        assert len(actual) == 2
        record["homogeneous_kernel"] = "zero"
        records.append(record)
        continue
    delta = sub(f, p1, p0)
    phi = mul(f, delta, gg)
    ww = mul(f, delta, phi)
    rr = derivative(f, phi)
    assert rr and not add(f, mul(f, a, rr), mul(f, b, ww))
    predicted = {p0}
    all_divisors = divisors(f, ww)
    tested_divisors += len(all_divisors)
    for tt in all_divisors:
        mm, remainder = divide(f, derivative(f, tt), rr)
        if remainder or derivative(f, mm):
            continue
        nn = sub(f, tt, mul(f, phi, mm))
        assert not derivative(f, nn)
        if not nn or gcd(f, mm, nn) != (1,):
            continue
        uu = sub(f, delta, mul(f, exact(f, ww, tt), mm))
        assert uu and mul(f, uu, tt) == mul(f, delta, nn)
        polynomial = add(f, p0, uu)
        if len(polynomial) > k:
            continue
        assert not residual(f, a, b, c, d, polynomial)
        predicted.add(polynomial)
    assert predicted == actual
    for polynomial in actual - {p0}:
        uu = sub(f, polynomial, p0)
        mm, nn = sub(f, delta, uu), mul(f, uu, phi)
        common = gcd(f, mm, nn)
        mm, nn = exact(f, mm, common), exact(f, nn, common)
        assert not derivative(f, mm) and not derivative(f, nn)
        tt = add(f, nn, mul(f, phi, mm))
        inverse = f.inv[tt[-1]]
        mm, nn, tt = (scale(f, inverse, poly) for poly in (mm, nn, tt))
        assert not divide(f, ww, tt)[1]
        assert derivative(f, tt) == mul(f, rr, mm)
        assert nn == sub(f, tt, mul(f, phi, mm))
        recovered_parameters += 1
    record.update({"g_degree": len(gg) - 1, "W_degree": len(ww) - 1,
                   "monic_divisors": len(all_divisors)})
    records.append(record)


subspace_records = []
for f in (f9, Field(3, (2, 1, 0, 0, 1))):
    t = f.r // 2
    aa = (0, f.neg[1]) + (0,) * (f.q - 2) + (1,)
    polynomials = set()
    for entries in product(range(f.p), repeat=t * (f.r - t)):
        roots = []
        for coordinates in product(range(f.p), repeat=t):
            tail = [sum(entries[i * t + j] * coordinates[j] for j in range(t)) % f.p
                    for i in range(f.r - t)]
            digits = list(coordinates) + tail
            roots.append(sum(value * f.p**i for i, value in enumerate(digits)))
        assert len(set(roots)) == f.p ** t
        hh = (1,)
        for root in roots:
            hh = mul(f, hh, (f.neg[root], 1))
        hd = derivative(f, hh)
        assert len(hd) == 1 and hd[0] != 0 and not derivative(f, hd)
        pp = scale(f, hd[0], exact(f, aa, hh))
        assert len(pp) - 1 == f.q - f.p ** t
        assert not residual(f, aa, (1,), (1,), (), pp)
        assert all(evaluate(f, pp, x) == (f.neg[1] if x in roots else 0)
                   for x in range(f.q))
        polynomials.add(pp)
    assert len(polynomials) == f.p ** (t * (f.r - t))
    subspace_records.append({"p": f.p, "s": f.r, "N": f.q, "dimension": t,
                             "distinct_graph_subspace_solutions": len(polynomials),
                             "solution_degree": f.q - f.p ** t})


result = {
    "scope": "Finite polynomial identities and exhaustive small solution sets; no list boundary claim.",
    "exhaustive_cases": len(cases),
    "polynomials_enumerated": tested_polynomials,
    "monic_divisors_tested": tested_divisors,
    "rational_parameters_recovered": recovered_parameters,
    "cases": records,
    "subspace_examples": subspace_records,
}
Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"Passed {len(cases)} exhaustive cases ({tested_polynomials} polynomials), "
      f"{tested_divisors} divisor tests, and {recovered_parameters} parameter recoveries; "
      f"checked {sum(r['distinct_graph_subspace_solutions'] for r in subspace_records)} "
      "distinct subspace solutions.")
