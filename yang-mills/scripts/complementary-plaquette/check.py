#!/usr/bin/env python3
"""Finite-matrix checks for L005; the mesh-limit proof is in the lemma."""

from itertools import combinations, product
import math


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def multiply(left, right):
    columns = transpose(right)
    return [[sum(a * b for a, b in zip(row, col)) for col in columns]
            for row in left]


def inverse(matrix):
    n = len(matrix)
    rows = [list(row) + [float(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = max(range(j, n), key=lambda i: abs(rows[i][j]))
        rows[j], rows[pivot] = rows[pivot], rows[j]
        scale = rows[j][j]
        assert abs(scale) > 1e-14
        rows[j] = [value / scale for value in rows[j]]
        for i in range(n):
            if i == j:
                continue
            scale = rows[i][j]
            if scale:
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def shifted_inverse(matrix, shift):
    return inverse([[entry + shift * (i == j) for j, entry in enumerate(row)]
                    for i, row in enumerate(matrix)])


def omega(k, n):
    return n / 4 * math.sin(k * math.pi / (2 * n))


def neumann_kernel(t, s, frequency, a):
    lo, hi = sorted((t, s))
    gamma = 2 / a * math.asinh(a * frequency / 2)
    return (a * math.cosh(gamma * (lo + 4))
            * math.cosh(gamma * (4 - hi))
            / (math.sinh(a * gamma) * math.sinh(8 * gamma)))


def check_time_resolvents():
    worst = 0.0
    for n in (4, 8, 16):
        a = 8 / n
        derivative = [[((i + 1 == j + 1) - (i == j + 1)) / a
                       for j in range(n - 1)] for i in range(n)]
        adjoint = transpose(derivative)
        lv = multiply(adjoint, derivative)
        le = multiply(derivative, adjoint)
        times = [-4 + (i + 0.5) * a for i in range(n)]
        for k in ((1, 1, 0), (1, 2, 1)):
            beta = omega(k[0], n) ** 2 + omega(k[1], n) ** 2
            w3 = omega(k[2], n) ** 2
            frequency = math.sqrt(beta + w3)
            gv = shifted_inverse(lv, frequency ** 2)
            ge = shifted_inverse(le, frequency ** 2)
            differentiated = multiply(multiply(derivative, gv), adjoint)
            for i, t in enumerate(times):
                for j, s in enumerate(times):
                    electric = w3 * ge[i][j] + differentiated[i][j]
                    reduced = float(i == j) - beta * ge[i][j]
                    kernel = neumann_kernel(t, s, frequency, a)
                    worst = max(worst, abs(electric - reduced),
                                abs(ge[i][j] / a - kernel))
                    if t < 0 < s:
                        assert electric < 0
                        worst = max(worst, abs(electric / a + beta * kernel))
    assert worst < 1e-11, worst
    return worst


def cells(degree, n):
    result = []
    for directions in combinations(range(4), degree):
        ranges = [range(n) if j in directions else range(1, n)
                  for j in range(4)]
        result.extend((directions, position) for position in product(*ranges))
    return result


def incidence(source, target):
    lookup = {cell: index for index, cell in enumerate(source)}
    rows = []
    for directions, position in target:
        row = {}
        for j, coordinate in enumerate(directions):
            remaining = directions[:j] + directions[j + 1:]
            upper = list(position)
            upper[coordinate] += 1
            sign = (-1) ** j
            for point, value in ((tuple(upper), sign), (position, -sign)):
                index = lookup.get((remaining, point))
                if index is not None:
                    row[index] = row.get(index, 0) + value
        rows.append(row)
    return rows


def spatial_wave(k, position, n):
    a = 8 / n
    x1, x2 = (-4 + a * position[j] for j in (0, 1))
    x3 = -4 + a * (position[2] + 0.5)
    vertex = lambda mode, x: 0.5 * math.sin(mode * math.pi * (x + 4) / 8)
    edge = (1 / math.sqrt(8) if k[2] == 0 else
            0.5 * math.cos(k[2] * math.pi * (x3 + 4) / 8))
    return vertex(k[0], x1) * vertex(k[1], x2) * edge


def check_full_cochain_covariance():
    n = 3
    a = 8 / n
    vertices, edges, faces = (cells(degree, n) for degree in range(3))
    d0, d1 = incidence(vertices, edges), incidence(edges, faces)
    columns = [{} for _ in vertices]
    for edge, row in enumerate(d0):
        for vertex, value in row.items():
            columns[vertex][edge] = value
    laplacian = [[0.0] * len(edges) for _ in edges]
    for row in columns + d1:
        for i, left in row.items():
            for j, right in row.items():
                laplacian[i][j] += left * right
    # This is the unscaled relative Hodge Laplacian, built from incidence.
    for i, (orientation, _) in enumerate(edges):
        for j, (other, _) in enumerate(edges):
            if orientation != other:
                assert laplacian[i][j] == 0
    covariance = inverse(laplacian)

    def curvature(left, right):
        return sum(x * covariance[i][j] * y
                   for i, x in left.items() for j, y in right.items()) / a ** 4

    magnetic = [i for i, (directions, _) in enumerate(faces)
                if directions == (0, 1)]
    electric = [i for i, (directions, _) in enumerate(faces)
                if directions == (2, 3)]
    mixed = max(abs(curvature(d1[i], d1[j])) for i in magnetic for j in electric)
    assert mixed == 0
    negative = [i for i in electric if faces[i][1][3] == 0]
    positive = [i for i in electric if faces[i][1][3] == n - 1]
    worst = 0.0
    for i in negative:
        left = faces[i][1]
        t = -4 + a * (left[3] + 0.5)
        for j in positive:
            right = faces[j][1]
            s = -4 + a * (right[3] + 0.5)
            spectral = 0.0
            for k in product(range(1, n), range(1, n), range(n)):
                beta = omega(k[0], n) ** 2 + omega(k[1], n) ** 2
                frequency = math.sqrt(beta + omega(k[2], n) ** 2)
                spectral -= (beta * spatial_wave(k, left, n)
                             * spatial_wave(k, right, n)
                             * neumann_kernel(t, s, frequency, a))
            worst = max(worst, abs(spectral - curvature(d1[i], d1[j])))
    assert worst < 1e-12, worst
    return mixed, worst


if __name__ == '__main__':
    time_error = check_time_resolvents()
    mixed, cochain_error = check_full_cochain_covariance()
    print(f'PASS: direct time-resolvent and edge-kernel error {time_error:.3g}')
    print(f'PASS: full relative cochain mixed covariance {mixed:g}; '
          f'electric spectral error {cochain_error:.3g}')
    print('Finite checks only; separated mesh convergence and the lower bound '
          'are proved in L005.')
