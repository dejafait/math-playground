#!/usr/bin/env python3
"""Exact finite-complex check for L013; the all-mesh proof is in the lemma."""

from fractions import Fraction as Q
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def matmul(left, right):
    columns = transpose(right)
    return [
        [sum(x * y for x, y in zip(row, column)) for column in columns]
        for row in left
    ]


def inverse(matrix):
    size = len(matrix)
    augmented = [
        list(row) + [Q(i == j) for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for k in range(size):
        pivot = next(i for i in range(k, size) if augmented[i][k])
        augmented[k], augmented[pivot] = augmented[pivot], augmented[k]
        scale = augmented[k][k]
        augmented[k] = [x / scale for x in augmented[k]]
        for i in range(size):
            if i != k:
                multiplier = augmented[i][k]
                augmented[i] = [
                    x - multiplier * y
                    for x, y in zip(augmented[i], augmented[k])
                ]
    return [row[size:] for row in augmented]


def incidence_matrix(rows, size, spacing):
    return [[Q(row.get(j, 0)) / spacing for j in range(size)] for row in rows]


def check():
    # Reuse the existing cell enumeration; its own checks are not rerun here.
    spec = spec_from_file_location(
        "fixed_box", Path("scripts/fixed-box-gaussian/check.py")
    )
    fixed_box = module_from_spec(spec)
    spec.loader.exec_module(fixed_box)

    n = 2
    spacing = Q(8, n)
    vertices, edges, faces = [fixed_box.cells(k, n) for k in range(3)]
    d = incidence_matrix(fixed_box.incidence(vertices, edges), len(vertices), spacing)
    e = incidence_matrix(fixed_box.incidence(edges, faces), len(edges), spacing)
    assert (len(vertices), len(edges), len(faces)) == (1, 8, 24)
    assert all(x == 0 for row in matmul(e, d) for x in row)
    scalar_lap = matmul(transpose(d), d)
    assert scalar_lap == [[Q(1, 2)]]
    maxwell = matmul(transpose(e), e)
    gauge_fix = matmul(d, transpose(d))
    hodge = [
        [x + y for x, y in zip(row, gauge)]
        for row, gauge in zip(maxwell, gauge_fix)
    ]
    hodge_inverse = inverse(hodge)
    # Point covariance has the a^-4 factor from the cochain inner product.
    cov_hodge = [
        [x / spacing**4 for x in row]
        for row in matmul(matmul(e, hodge_inverse), transpose(e))
    ]
    pinned_edge = edges.index(((0,), (0, 1, 1, 1)))
    assert d[pinned_edge][0] != 0
    slice_e = [
        [x for j, x in enumerate(row) if j != pinned_edge] for row in e
    ]
    slice_hessian = matmul(transpose(slice_e), slice_e)
    cov_forest = [
        [x / spacing**4 for x in row]
        for row in matmul(matmul(slice_e, inverse(slice_hessian)), transpose(slice_e))
    ]
    assert cov_hodge == cov_forest
    longitudinal = matmul(
        matmul(d, inverse(matmul(scalar_lap, scalar_lap))), transpose(d)
    )
    assert all(
        x == 0 for row in matmul(matmul(e, longitudinal), transpose(e)) for x in row
    )
    print("PASS exact N=2 relative complex: 1 interior vertex, 8 links, 24 faces; det L0=1/2.")
    print("PASS all 576 raw curvature covariance entries: auxiliary/Hodge form equals forest-gauge form, including a^-4 normalization.")
    print("PASS longitudinal covariance contributes zero to every curvature pair.")


if __name__ == "__main__":
    check()
