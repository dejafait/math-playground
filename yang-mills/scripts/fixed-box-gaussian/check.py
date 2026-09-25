#!/usr/bin/env python3
"""Sanity checks for L003; numerical checks are not proof of its limits."""

from itertools import combinations, product
import math


def cells(degree, n):
    result = []
    for directions in combinations(range(4), degree):
        ranges = [
            range(n) if coordinate in directions else range(1, n)
            for coordinate in range(4)
        ]
        result.extend((directions, position) for position in product(*ranges))
    return result


def incidence(source, target):
    lookup = {cell: index for index, cell in enumerate(source)}
    rows = []
    for directions, position in target:
        row = {}
        for index, coordinate in enumerate(directions):
            remaining = directions[:index] + directions[index + 1 :]
            upper = list(position)
            upper[coordinate] += 1
            sign = (-1) ** index
            for point, coefficient in ((tuple(upper), sign), (position, -sign)):
                source_index = lookup.get((remaining, point))
                if source_index is not None:
                    row[source_index] = row.get(source_index, 0) + coefficient
        rows.append(row)
    return rows


def add_outer(matrix, row):
    for i, left in row.items():
        for j, right in row.items():
            matrix[i][j] = matrix[i].get(j, 0) + left * right


def check_relative_complex():
    n = 3
    vertices, edges, faces = (cells(degree, n) for degree in range(3))
    d0 = incidence(vertices, edges)
    d1 = incidence(edges, faces)
    for row in d1:
        composition = {}
        for edge, first in row.items():
            for vertex, second in d0[edge].items():
                composition[vertex] = composition.get(vertex, 0) + first * second
        assert all(value == 0 for value in composition.values())

    laplacian = [{} for _ in edges]
    columns = [{} for _ in vertices]
    for edge, row in enumerate(d0):
        for vertex, coefficient in row.items():
            columns[vertex][edge] = coefficient
    for row in columns + d1:
        add_outer(laplacian, row)

    lookup = {cell: index for index, cell in enumerate(edges)}
    for i, (directions, position) in enumerate(edges):
        expected = {}
        diagonal = 0
        for coordinate in range(4):
            is_edge_coordinate = coordinate in directions
            allowed = range(n) if is_edge_coordinate else range(1, n)
            diagonal += (
                1
                if is_edge_coordinate and position[coordinate] in (0, n - 1)
                else 2
            )
            for sign in (-1, 1):
                neighbor = list(position)
                neighbor[coordinate] += sign
                if neighbor[coordinate] in allowed:
                    expected[lookup[(directions, tuple(neighbor))]] = -1
        expected[i] = diagonal
        actual = {j: value for j, value in laplacian[i].items() if value}
        assert actual == expected, (i, actual, expected)
    print(
        "PASS exact relative cochain identities:",
        len(vertices),
        "vertices,",
        len(edges),
        "edges,",
        len(faces),
        "faces; d1 d0 = 0 and componentwise Hodge Laplacian.",
    )


def frequency(k, n):
    return (n / 4) * math.sin(k * math.pi / (2 * n))


def green(i, j, n, omega):
    if i in (0, n) or j in (0, n):
        return 0.0
    i, j = sorted((i, j))
    a = 8 / n
    eta = 2 * math.asinh(a * omega / 2)
    return (
        a
        * math.sinh(i * eta)
        * math.sinh((n - j) * eta)
        / (math.sinh(eta) * math.sinh(n * eta))
    )


def check_green():
    maximum_recurrence_error = 0.0
    maximum_spectral_error = 0.0
    maximum_mode_error = 0.0
    for n in (8, 16, 32):
        a = 8 / n
        omega = math.hypot(frequency(2, n), frequency(1, n))
        for k in range(1, n):
            for j in range(n):
                difference = (
                    0.5 * math.sin(k * math.pi * (j + 1) / n)
                    - 0.5 * math.sin(k * math.pi * j / n)
                ) / a
                expected = frequency(k, n) * 0.5 * math.cos(
                    k * math.pi * (j + 0.5) / n
                )
                maximum_mode_error = max(
                    maximum_mode_error, abs(difference - expected)
                )
        for i in range(1, n):
            for j in range(1, n):
                value = green(i, j, n, omega)
                recurrence = (
                    (2 + a * a * omega * omega) * value
                    - green(i - 1, j, n, omega)
                    - green(i + 1, j, n, omega)
                ) / (a * a)
                maximum_recurrence_error = max(
                    maximum_recurrence_error,
                    abs(recurrence - (1 / a if i == j else 0)),
                )
                spectral = sum(
                    0.25
                    * math.sin(k * math.pi * i / n)
                    * math.sin(k * math.pi * j / n)
                    / (frequency(k, n) ** 2 + omega**2)
                    for k in range(1, n)
                )
                maximum_spectral_error = max(
                    maximum_spectral_error, abs(value - spectral)
                )
    assert maximum_mode_error < 1e-11
    assert maximum_recurrence_error < 1e-11
    assert maximum_spectral_error < 1e-11
    print(
        "PASS interval modes and Green kernel:",
        f"mode error {maximum_mode_error:.3g},",
        f"resolvent error {maximum_recurrence_error:.3g},",
        f"spectral error {maximum_spectral_error:.3g}.",
    )


def bump(s):
    return math.exp(-1 / (1 - s * s)) if abs(s) < 1 else 0.0


def check_selected_mode():
    omega = math.pi * math.sqrt(5) / 8
    alpha = math.pi**2 / 16
    m_phi = math.cos(math.pi / 16) ** 2 * math.cos(math.pi / 32) ** 2 / 128
    d_box = m_phi * alpha * math.sinh(2 * omega) ** 2 / (
        omega * math.sinh(8 * omega)
    )
    print(f"d_box = {d_box:.12g}; eventual bound c_box = {0.75*d_box**2:.12g}.")

    # Only a numerical normalization check; the proof uses integral f = 1.
    steps = 16384
    h = 2 / steps
    integral = h / 3 * sum(
        (1 if j in (0, steps) else 4 if j % 2 else 2) * bump(-1 + j * h)
        for j in range(steps + 1)
    )
    for n in (64, 128, 256, 512):
        a = 8 / n
        edge_points = [-4 + (j + 0.5) * a for j in range(n)]
        vertex_points = [-4 + j * a for j in range(1, n)]
        omega_a = math.hypot(frequency(2, n), frequency(1, n))
        alpha_a = frequency(2, n) ** 2
        gamma = 2 / a * math.asinh(a * omega_a / 2)
        r = a / (math.sinh(a * gamma) * math.sinh(8 * gamma))
        factors = [
            a * sum(bump(4 * x) / 8 for x in edge_points),
            a
            * sum(
                bump(4 * x) * 0.25 * math.cos(math.pi * x / 4) ** 2
                for x in edge_points
            ),
            a
            * sum(
                bump(4 * x) * 0.25 * math.cos(math.pi * x / 8) ** 2
                for x in vertex_points
            ),
            a
            * sum(
                bump(2 * t - 3) * math.sinh(gamma * (4 - t)) ** 2
                for t in vertex_points
            ),
        ]
        weighted_sum = 128 / integral**4 * math.prod(factors)
        normalization = (
            128
            / integral**4
            * (a * sum(bump(4 * x) for x in edge_points)) ** 2
            * (a * sum(bump(4 * x) for x in vertex_points))
            * (a * sum(bump(2 * t - 3) for t in vertex_points))
        )
        lower_sum = m_phi * math.sinh(2 * gamma) ** 2 * normalization
        assert weighted_sum >= lower_sum - 1e-14
        diagonal_contribution = 1.5 * (alpha_a * r * weighted_sum) ** 2
        print(
            f"N={n}: sampled integral f={normalization:.9f}; "
            f"retained diagonal contribution={diagonal_contribution:.12g}."
        )


if __name__ == "__main__":
    check_relative_complex()
    check_green()
    check_selected_mode()
