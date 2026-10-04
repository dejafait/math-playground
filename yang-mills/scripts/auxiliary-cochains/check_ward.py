#!/usr/bin/env python3
"""Exact Ward signs and breaking terms on the complete N=2 relative complex.

Use beta = -i b as an algebraic coordinate for rational Wick contractions;
this is not an integration-contour change. The all-mesh proof is in L014.
"""

from fractions import Fraction as Q
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations_with_replacement
from pathlib import Path


def load_module(name, path):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def monomials(size, max_degree):
    for degree in range(max_degree + 1):
        for indices in combinations_with_replacement(range(size), degree):
            powers = [0] * size
            for j in indices:
                powers[j] += 1
            yield tuple(powers)


def check():
    algebra = load_module("auxiliary_covariance", "scripts/auxiliary-cochains/check.py")
    cells = load_module("relative_cells", "scripts/fixed-box-gaussian/check.py")
    spacing = Q(4)
    vertices, edges, faces = [cells.cells(k, 2) for k in range(3)]
    assert (len(vertices), len(edges), len(faces)) == (1, 8, 24)
    d_matrix = algebra.incidence_matrix(
        cells.incidence(vertices, edges), len(vertices), spacing
    )
    e_matrix = algebra.incidence_matrix(
        cells.incidence(edges, faces), len(edges), spacing
    )
    d = tuple(row[0] for row in d_matrix)
    scalar_lap = sum(x * x for x in d)
    assert scalar_lap == Q(1, 2)
    maxwell = algebra.matmul(algebra.transpose(e_matrix), e_matrix)
    hodge = [
        [value + d[i] * d[j] for j, value in enumerate(row)]
        for i, row in enumerate(maxwell)
    ]
    n = len(edges)
    beta_index = n
    count_total = 0

    for epsilon in (Q(0), Q(1, 3), Q(2)):
        hessian = [
            [value + epsilon * Q(i == j) for j, value in enumerate(row)]
            for i, row in enumerate(hodge)
        ]
        cov_a = algebra.inverse(hessian)
        cov_a_beta = [sum(row[j] * d[j] for j in range(n)) for row in cov_a]
        assert cov_a_beta == [x / (scalar_lap + epsilon) for x in d]
        cov_beta_beta = -epsilon / (scalar_lap + epsilon)
        covariance = [
            list(row) + [cov_a_beta[i]] for i, row in enumerate(cov_a)
        ] + [cov_a_beta + [cov_beta_beta]]

        @lru_cache(maxsize=None)
        def wick(powers):
            if sum(powers) == 0:
                return Q(1)
            if sum(powers) % 2:
                return Q(0)
            i = next(j for j, power in enumerate(powers) if power)
            reduced = list(powers)
            reduced[i] -= 1
            value = Q(0)
            for j, multiplicity in enumerate(reduced):
                if multiplicity:
                    paired = list(reduced)
                    paired[j] -= 1
                    value += multiplicity * covariance[i][j] * wick(tuple(paired))
            return value

        def expectation(powers, mask):
            # Ordered exterior generators are c, bar c. The orientation
            # B[c bar c] = 1 gives Z_ghost = L0 and <c bar c> = 1/L0.
            if mask == 0:
                return wick(powers)
            if mask == 3:
                return wick(powers) / scalar_lap
            return Q(0)

        def ward_left(powers, mask):
            value = Q(0)
            # sA_j = d_j c, with c multiplying the exterior monomial on its left.
            if not mask & 1:
                for j, multiplicity in enumerate(powers[:n]):
                    if multiplicity:
                        reduced = list(powers)
                        reduced[j] -= 1
                        value += multiplicity * d[j] * expectation(tuple(reduced), mask | 1)
            # s bar c = -beta. Left differentiation of c bar c contributes -c.
            if mask & 2:
                increased = list(powers)
                increased[beta_index] += 1
                derivative_sign = -1 if mask & 1 else 1
                value -= derivative_sign * expectation(tuple(increased), mask ^ 2)
            return value

        def ward_right(powers, mask):
            if mask & 1:
                return Q(0)
            parity_sign = -1 if mask.bit_count() % 2 else 1
            # P (delta A,c) multiplies c on the right; bar c c = -c bar c.
            product_sign = -1 if mask & 2 else 1
            value = Q(0)
            for j, entry in enumerate(d):
                increased = list(powers)
                increased[j] += 1
                value += entry * expectation(tuple(increased), mask | 1)
            return parity_sign * epsilon * product_sign * value

        checked = 0
        for powers in monomials(n + 1, 4):
            for mask in range(4):
                left = ward_left(powers, mask)
                right = ward_right(powers, mask)
                assert left == right, (epsilon, powers, mask, left, right)
                checked += 1
        assert checked == 2860
        count_total += checked

        connection_powers = [0] * (n + 1)
        connection_powers[0] = 1
        connection_defect = ward_left(tuple(connection_powers), 2)
        expected_connection_defect = (
            epsilon * d[0] / (scalar_lap * (scalar_lap + epsilon))
        )
        assert connection_defect == expected_connection_defect
        auxiliary_powers = [0] * (n + 1)
        auxiliary_powers[beta_index] = 1
        auxiliary_defect = ward_left(tuple(auxiliary_powers), 2)
        assert auxiliary_defect == epsilon / (scalar_lap + epsilon)
        if epsilon:
            assert connection_defect and auxiliary_defect
        else:
            assert connection_defect == auxiliary_defect == 0
        print(
            f"PASS epsilon={epsilon}: {checked} polynomial Ward checks; "
            f"antighost/connection defect={connection_defect}, "
            f"antighost/beta defect={auxiliary_defect}."
        )

    print(
        f"PASS {count_total} exact rational checks with all 8 relative links and "
        "all four exterior monomials; regulated breaking is nonzero and removal gives zero."
    )


if __name__ == "__main__":
    check()
