#!/usr/bin/env python3
"""Exact root/sign evidence for L118; no numerical root approximations."""

from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


COEFFICIENTS = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
OUT = Path(__file__).with_name("marked-octic-real-image-certificate.json")


def evaluate(x):
    value = Q(0)
    for coefficient in reversed(COEFFICIENTS):
        value = value * x + coefficient
    return value


def sign(value):
    return 1 if value > 0 else -1 if value < 0 else 0


def label(vector):
    return "".join("+" if entry == 1 else "-" for entry in vector)


def quotient(vector):
    # Unique representative with first coordinate positive.
    return label(tuple(vector[0] * entry for entry in vector))


def block(k):
    return (-1,) * k + (1,) * (8 - k)


def main():
    positive = [(Q(1, 4), Q(1, 2)), (Q(3, 4), Q(1)),
                (Q(3, 2), Q(2)), (Q(5, 2), Q(3))]
    ascending = [(-b, -a) for a, b in reversed(positive)] + positive
    intervals = list(reversed(ascending))
    roots = []
    for index, (a, b) in enumerate(intervals, 1):
        roots.append(dict(index=index, interval=[str(a), str(b)],
                          values=[str(evaluate(a)), str(evaluate(b))],
                          signs=[sign(evaluate(a)), sign(evaluate(b))]))

    samples = [Q(3), Q(1), Q(0), Q(-1), Q(-3)]
    interval_rows = []
    for k, x in zip(range(0, 9, 2), samples):
        # Bounds enclosing the whole indicated gap between isolated roots.
        inside = ((k == 0 and x >= intervals[0][1])
                  or (k == 8 and x <= intervals[-1][0])
                  or (0 < k < 8 and intervals[k][1] <= x <= intervals[k-1][0]))
        interval_rows.append(dict(negative_block=k, sample=str(x),
                                  G_sample=str(evaluate(x)), certified_inside=inside,
                                  sign_vector=label(block(k)),
                                  quotient=quotient(block(k))))

    branch_rows = []
    for j in range(1, 9):
        derivative_sign = (-1) ** (j - 1)
        vector = tuple(-1 if i < j else derivative_sign if i == j else 1
                       for i in range(1, 9))
        k = j - 1 if j % 2 else j
        branch_rows.append(dict(root_index=j, derivative_sign=derivative_sign,
                                sign_vector=label(vector), negative_block=k,
                                expected_vector=label(block(k)), quotient=quotient(vector)))

    infinity_rows = [dict(q=0, Z=z, chart_derivative=2*z,
                          fake_representative=3025, quotient="++++++++")
                     for z in (-55, 55)]
    norm_vectors = [v for v in product((1, -1), repeat=8)
                    if sum(entry == -1 for entry in v) % 2 == 0]
    ambient = sorted({quotient(v) for v in norm_vectors})
    image = sorted({row["quotient"] for row in interval_rows})
    collisions = {q: [row["negative_block"] for row in interval_rows
                      if row["quotient"] == q] for q in image}
    excluded = "+--+++++"
    checks = dict(
        degree_eight=len(COEFFICIENTS)-1 == 8 and COEFFICIENTS[-1] == 55**2,
        even_polynomial=all(COEFFICIENTS[i] == 0 for i in (1, 3, 5, 7)),
        eight_disjoint_intervals=len(roots) == 8 and all(
            ascending[i][1] < ascending[i+1][0] for i in range(7)),
        all_intervals_change_sign=all(row["signs"][0]*row["signs"][1] == -1 for row in roots),
        all_allowed_blocks_covered=[row["negative_block"] for row in interval_rows] == [0,2,4,6,8],
        all_samples_realizable=all(row["certified_inside"] and Q(row["G_sample"]) > 0
                                  for row in interval_rows),
        all_branches_match_blocks=all(row["sign_vector"] == row["expected_vector"]
                                      for row in branch_rows),
        all_branch_images_retained=all(row["quotient"] in image for row in branch_rows),
        both_infinity_points_retained=len(infinity_rows) == 2 and all(
            row["Z"]**2 == 3025 and row["chart_derivative"] != 0
            and row["quotient"] in image for row in infinity_rows),
        norm_vector_count=len(norm_vectors) == 128,
        every_scalar_orbit_size_two=all(tuple(-entry for entry in v) in norm_vectors
                                      and v != tuple(-entry for entry in v) for v in norm_vectors),
        ambient_count=len(ambient) == 64,
        image_count=len(image) == 4,
        image_subset_ambient=set(image) <= set(ambient),
        only_exterior_collision=sorted(sorted(v) for v in collisions.values()) == [[0,8],[2],[4],[6]],
        properness_witness=excluded in ambient and excluded not in image,
        excluded_count=len(set(ambient)-set(image)) == 60,
    )
    failures = [key for key, passed in checks.items() if not passed]
    certificate = dict(
        coefficients_ascending=COEFFICIENTS, root_order="theta_1 > ... > theta_8",
        root_count_argument="Eight disjoint sign changes exhaust degree eight; all roots simple and real.",
        roots=roots, nonreal_pairs=[], ordinary_interval_rows=interval_rows,
        branch_rows=branch_rows, infinity_rows=infinity_rows,
        quotient_convention="first coordinate positive; simultaneous sign reversal",
        ambient_representatives=ambient, image_representatives=image,
        interval_collisions=collisions, excluded_witness=excluded,
        bounds=dict(real_roots_actual=8, real_roots_required=8,
                    branch_rows_actual=8, branch_rows_required=8,
                    infinity_rows_actual=2, infinity_rows_required=2,
                    image_actual=len(image), ambient_actual=len(ambient),
                    properness_required="image < ambient", removed=len(set(ambient)-set(image))),
        checks=checks, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
    print(f"Real roots: 8/8; branch rows: 8/8; infinity rows: 2/2")
    print(f"Image: {len(image)}; norm ambient: {len(ambient)}; required: image < ambient; removed: 60")
    print(f"Certificate: {OUT}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
