#!/usr/bin/env python3
"""Exact algebra supporting L008; not a computation of its global obstruction."""


def add(left, right):
    result = dict(left)
    for exponent, value in right.items():
        result[exponent] = result.get(exponent, 0) + value
    return {exponent: value for exponent, value in result.items() if value}


def scale(poly, scalar):
    return {exponent: scalar * value for exponent, value in poly.items() if scalar * value}


def multiply(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            exponent = tuple(i + j for i, j in zip(a, b))
            result[exponent] = result.get(exponent, 0) + x * y
    return {exponent: value for exponent, value in result.items() if value}


def invariant_basis(degree, weight):
    """Rotation eigenmonomials, then inversion e <-> degree-e."""
    support = tuple(e for e in range(degree + 1) if e % 7 == weight % 7)
    assert all(degree - e in support for e in support)
    orbits = sorted({tuple(sorted({e, degree - e})) for e in support})
    for orbit in orbits:
        # Laurent form of A(1/v) = v^-degree A(v), coefficient by coefficient.
        assert {-e: 1 for e in orbit} == {e - degree: 1 for e in orbit}
    return support, orbits


def main():
    weights = [(6, 2), (3, 5), (6, 2)]
    for pair in weights:
        # A factor zeta^e-zeta^-e is zero exactly when 2e=0 modulo 7.
        assert all(2 * e % 7 != 0 for e in pair)
        assert sum(pair) % 7 == 1
    assert (1 - 3) % 7 == 5  # Y/X in the X blowup chart
    assert (1 - 6) % 7 == 2  # Y/q in the q blowup chart

    support_a, basis_a = invariant_basis(16, 8)
    support_b, basis_b = invariant_basis(24, 12)
    assert support_a == (1, 8, 15) and basis_a == [(1, 15), (8,)]
    assert support_b == (5, 12, 19) and basis_b == [(5, 19), (12,)]
    assert len(basis_a) + len(basis_b) == 4
    # Dividing by v^8 and v^12 recovers the same invariant Laurent polynomial.
    assert {e - 8 for e in basis_a[0]} == {-7, 7}
    assert {e - 12 for e in basis_b[0]} == {-7, 7}

    # P_n(v+v^-1)=v^n+v^-n from the exact Dickson recurrence for a=1.
    t = {(1,): 1, (-1,): 1}
    previous, current = {(0,): 2}, t
    for n in range(2, 8):
        previous, current = current, add(multiply(t, current), scale(previous, -1))
        assert current == {(n,): 1, (-n,): 1}

    # A_1 resolution chart: z=xr+lambda, y=xr^2+2lambda r.
    x = {(1, 0, 0): 1}
    r = {(0, 1, 0): 1}
    lam = {(0, 0, 1): 1}
    z = add(multiply(x, r), lam)
    y = add(multiply(multiply(x, r), r), scale(multiply(lam, r), 2))
    assert add(multiply(x, y), scale(multiply(z, z), -1)) == scale(multiply(lam, lam), -1)

    print("PASS: all three fixed-point tangent pairs give transverse graph branches.")
    print("PASS: full coefficient bounds give A exponents", support_a, "and B exponents", support_b)
    print("PASS: inversion leaves four coefficient parameters; Dickson descent is exact.")
    print("PASS: A_1 resolution chart satisfies xy = z^2 - lambda^2.")
    print("The global kernel and deformation arguments require the proof in L008.")


if __name__ == "__main__":
    main()
