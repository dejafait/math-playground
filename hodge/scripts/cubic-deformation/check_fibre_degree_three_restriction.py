#!/usr/bin/env python3
"""Check L021's actual restriction ranks in a few finite-field cases.

The geometric proof is over C and treats all r. This arithmetic check
retains the lower terms of y^2 and x*z^2, but proves no geometric claim.
"""

from functools import lru_cache

from check_positive_ideal_restriction import PRIME, ZETA, rectangle


X0, Y0 = 2, 1
DICKSON = {7: 1, -7: 1}
A_COEFF = {**DICKSON, 0: 3}
B_COEFF = {7: -X0, -7: -X0, 0: Y0**2 - X0**3 - 3 * X0}


def add_term(result, key, value):
    value = (result.get(key, 0) + value) % PRIME
    if value:
        result[key] = value
    else:
        result.pop(key, None)


@lru_cache(None)
def reduce_monomial(form, i, j):
    """Return normal-form x^i*y^j or x^i*z^j with Laurent coefficients."""
    if form == "A":
        if j < 2:
            return {(i, j, 0): 1}
        assert j == 2
        result = {(i + 3, 0, 0): 1}
        for k, value in A_COEFF.items():
            add_term(result, (i + 1, 0, k), value)
        for k, value in B_COEFF.items():
            add_term(result, (i, 0, k), value)
        return result
    if i == 0 or j < 2:
        return {(i, j, 0): 1}
    # x*z^2 = x^2 + X0*x + X0^2 + A(v) + X0*z^2 + 2*Y0*z.
    terms = [
        (i + 1, j - 2, {0: 1}),
        (i, j - 2, {0: X0}),
        (i - 1, j - 2, {**DICKSON, 0: X0**2 + 3}),
        (i - 1, j, {0: X0}),
        (i - 1, j - 1, {0: 2 * Y0}),
    ]
    result = {}
    for new_i, new_j, coefficient in terms:
        for (out_i, out_j, k), value in reduce_monomial(form, new_i, new_j).items():
            for shift, scale in coefficient.items():
                add_term(result, (out_i, out_j, k + shift), value * scale)
    return result


def basis_bounds(form, b, r):
    if form == "A":
        result = {
            (i, 0): r * b - 4 * i - max(0, r - i)
            for i in range(3 * r // 2 + 1)
        }
        result.update({
            (j, 1): r * b - 6 - 4 * j - max(0, r - 1 - j)
            for j in range((3 * r - 3) // 2 + 1)
        })
        return result
    result = {(i, 0): r * b - 4 * i for i in range(r + 1)}
    result.update({(i, 1): r * b - 4 * i - 2 for i in range(r)})
    result.update({(0, j): r * b - 2 * j for j in range(2, r + 1)})
    return result


def sparse_rank(rows):
    pivots = {}
    for row in rows:
        row = dict(row)
        while row:
            key = min(row)
            value = row[key]
            if key not in pivots:
                inverse = pow(value, -1, PRIME)
                pivots[key] = {k: v * inverse % PRIME for k, v in row.items()}
                break
            for k, v in pivots[key].items():
                add_term(row, k, -value * v)
    return len(pivots)


def restriction_rows(form, b, r):
    source = basis_bounds(form, b, r)
    target = basis_bounds(form, b, 2 * r)
    for (i, j), a in source.items():
        for (k, ell), c in source.items():
            normal = reduce_monomial(form, i + k, j + ell)
            for coefficient in rectangle(a, c):
                row = {}
                for (out_i, out_j, shift), value in normal.items():
                    bound = target[out_i, out_j]
                    for degree, scale in coefficient.items():
                        assert abs(degree + shift) <= bound
                        add_term(row, (out_i, out_j, degree + shift), value * scale)
                yield row


def main():
    assert (Y0**2 - X0**3 - 3 * X0 - B_COEFF[0]) % PRIME == 0
    cases = [("A", 7, 1), ("B", 5, 1), ("A", 7, 2), ("B", 5, 2), ("A", 7, 3)]
    for form, b, r in cases:
        square = 6 * b - (20 if form == "A" else 10)
        source = basis_bounds(form, b, r)
        target = basis_bounds(form, b, 2 * r)
        assert min(source.values()) >= r
        assert sum(v + 1 for v in source.values()) == 2 + r * r * square // 2
        normalization = sum(2 * v + 1 for v in target.values())
        assert normalization == 4 + 4 * r * r * square - 6 * r
        actual = sparse_rank(restriction_rows(form, b, r))
        assert actual == normalization - 3, (form, b, r, actual, normalization)
        print(f"form={form}, b={b}, r={r}: normalization={normalization}, image={actual}, descent target={normalization - 3}")
    print(f"PASS: actual product ranks over F_{PRIME}, zeta={ZETA}; geometry and all-degree validity require L021's proof.")


if __name__ == "__main__":
    main()
