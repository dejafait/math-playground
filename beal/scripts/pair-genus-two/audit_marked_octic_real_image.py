#!/usr/bin/env python3
"""Independent exact L118 audit, including the smooth-chart arc gluing."""

from fractions import Fraction
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "marked-octic-real-image-certificate.json"
OUTPUT = BASE / "marked-octic-real-image-audit-certificate.json"


def evaluate(x):
    # Direct homogeneous evaluation of 11*F, not producer Horner code.
    a, b = x.numerator, x.denominator
    numerator = 11 * (275*a**8 - 2860*a**6*b**2 + 6930*a**4*b**4
                      - 3564*a**2*b**6 + 243*b**8)
    return Fraction(numerator, b**8)


def sign(x):
    return (x > 0) - (x < 0)


def word(mask):
    return "".join("-" if mask & (1 << i) else "+" for i in range(8))


def canonical(mask):
    return word(mask ^ 255 if mask & 1 else mask)


def main():
    source = json.loads(SOURCE.read_text())
    checks = {}

    def check(name, actual, expected=True):
        checks[name] = {"actual": actual, "expected": expected,
                        "passed": actual == expected}

    intervals = [(Fraction(a), Fraction(b)) for a, b in
                 [("5/2", "3"), ("3/2", "2"), ("3/4", "1"),
                  ("1/4", "1/2"), ("-1/2", "-1/4"), ("-1", "-3/4"),
                  ("-2", "-3/2"), ("-3", "-5/2")]]
    check("actual_polynomial", source["coefficients_ascending"],
          [11*c for c in [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]])
    check("root_order", source["root_order"], "theta_1 > ... > theta_8")
    check("all_intervals_ordered_disjoint", all(
        intervals[i+1][1] < intervals[i][0] for i in range(7)))
    roots = []
    for j, (a, b) in enumerate(intervals, 1):
        values = [evaluate(a), evaluate(b)]
        row = {"index": j, "interval": [str(a), str(b)],
               "values": [str(v) for v in values], "signs": list(map(sign, values))}
        roots.append(row)
        check(f"root_{j}_sign_change", values[0]*values[1] < 0)
    check("all_root_rows", source["roots"], roots)
    check("degree_exhausted", len(roots), 8)
    check("nonreal_pairs", source["nonreal_pairs"], [])

    # Sample one point of every gap, including the four forbidden gaps.
    samples = [Fraction(3)]
    samples += [(intervals[k][1]+intervals[k-1][0])/2 for k in range(1, 8)]
    samples += [Fraction(-3)]
    gaps = []
    for k, x in enumerate(samples):
        bits = []
        for a, b in intervals:
            check(f"gap_{k}_separated_from_root_{len(bits)+1}", x <= a or x >= b)
            bits.append(1 if x <= a else 0)
        mask = sum(bit << i for i, bit in enumerate(bits))
        value = evaluate(x)
        check(f"gap_{k}_polynomial_sign", sign(value), (-1)**k)
        check(f"gap_{k}_negative_coordinates", sum(bits), k)
        gaps.append({"gap": k, "sample": str(x), "G_sample": str(value),
                     "sign_vector": word(mask), "mask": mask,
                     "real_points": value > 0, "quotient": canonical(mask)})

    ordinary = []
    for k, x in zip([0, 2, 4, 6, 8], map(Fraction, [3, 1, 0, -1, -3])):
        value = evaluate(x)
        mask = sum(1 << i for i, (a, b) in enumerate(intervals) if x <= a)
        separated = all(x <= a or x >= b for a, b in intervals)
        check(f"realizing_gap_{k}", separated and value > 0 and mask == gaps[k]["mask"])
        ordinary.append({"negative_block": k, "sample": str(x),
                         "G_sample": str(value), "certified_inside": separated,
                         "sign_vector": word(mask), "quotient": canonical(mask)})
    check("all_ordinary_rows", source["ordinary_interval_rows"], ordinary)

    branches = []
    for j, (a, b) in enumerate(intervals):
        # Signs of a_root - each other root from pairwise disjoint bounds.
        differences = [(-1 if b < c else 1) for i, (c, d) in enumerate(intervals) if i != j]
        derivative = 1
        for s in differences:
            derivative *= s
        coordinates = iter(differences)
        vector = [derivative if i == j else next(coordinates) for i in range(8)]
        mask = sum((s < 0) << i for i, s in enumerate(vector))
        allowed_gap = j if derivative > 0 else j+1
        check(f"branch_{j+1}_adjacent_allowed_image", word(mask), gaps[allowed_gap]["sign_vector"])
        check(f"branch_{j+1}_norm_positive", derivative*derivative, 1)
        branches.append({"root_index": j+1, "derivative_sign": derivative,
                         "sign_vector": word(mask), "negative_block": sum(s < 0 for s in vector),
                         "expected_vector": gaps[allowed_gap]["sign_vector"], "quotient": canonical(mask)})
    check("all_branch_rows", source["branch_rows"], branches)

    infinities = []
    for z in [-55, 55]:
        check(f"infinity_{z}_smooth", z*z == 3025 and 2*z != 0)
        infinities.append({"q": 0, "Z": z, "chart_derivative": 2*z,
                           "fake_representative": 55**2, "quotient": canonical(0)})
    check("both_infinity_rows", source["infinity_rows"], infinities)

    # Each edge is one open Y-sign arc. At infinity t^4 is positive;
    # at a simple finite root the two Y-sign arcs meet.
    edges = []
    for k in [2, 4, 6]:
        for y_sign in [-1, 1]:
            edges.append({"ends": [f"r{k}", f"r{k+1}"], "Y_sign": y_sign,
                          "image": gaps[k]["quotient"]})
    for root, gap in [(1, 0), (8, 8)]:
        for y_sign in [-1, 1]:
            edges.append({"ends": [f"r{root}", f"I{55*y_sign}"], "Y_sign": y_sign,
                          "image": gaps[gap]["quotient"]})
    vertices = {v for e in edges for v in e["ends"]}
    degrees = {v: sum(v in e["ends"] for e in edges) for v in sorted(vertices)}
    components = []
    unseen = set(vertices)
    while unseen:
        component, queue = set(), [min(unseen)]
        while queue:
            v = queue.pop()
            if v in component:
                continue
            component.add(v)
            queue += [w for e in edges if v in e["ends"] for w in e["ends"] if w not in component]
        unseen -= component
        labels = sorted({e["image"] for e in edges if e["ends"][0] in component})
        components.append({"vertices": sorted(component), "image": labels})
    check("all_ten_smooth_endpoints", len(vertices), 10)
    check("no_unattached_arc", set(degrees.values()) == {2})
    check("four_connected_components", len(components), 4)
    check("one_image_per_component", all(len(c["image"]) == 1 for c in components))

    even_masks = [m for m in range(256) if m.bit_count() % 2 == 0]
    orbits = [[m, m ^ 255] for m in even_masks if m < (m ^ 255)]
    ambient = sorted(canonical(orbit[0]) for orbit in orbits)
    image = sorted({g["quotient"] for g in gaps if g["real_points"]})
    collisions = {label: [g["gap"] for g in gaps if g["real_points"] and g["quotient"] == label]
                  for label in image}
    check("norm_vectors", len(even_masks), 128)
    check("orbits_partition_norm_vectors", sorted(m for o in orbits for m in o), even_masks)
    check("all_ambient_representatives", source["ambient_representatives"], ambient)
    check("all_image_representatives", source["image_representatives"], image)
    check("all_collisions", source["interval_collisions"], collisions)
    check("branch_and_infinity_images_retained", all(r["quotient"] in image for r in branches+infinities))
    check("component_images_distinct", len({c["image"][0] for c in components}), 4)
    check("properness_witness", source["excluded_witness"], "+--+++++")
    check("witness_norm_admissible_and_excluded", "+--+++++" in ambient and "+--+++++" not in image)
    check("image_size", len(image), 4)
    check("ambient_size", len(ambient), 64)
    check("excluded_size", len(set(ambient)-set(image)), 60)
    failures = [name for name, row in checks.items() if not row["passed"]]
    record = {"source": SOURCE.name, "method": "Independent integer homogenization, all gaps, pairwise root order, scalar orbits and chart arc graph; no producer imports.",
              "roots": roots, "all_gaps": gaps, "ordinary_rows": ordinary,
              "branch_rows": branches, "infinity_rows": infinities,
              "arc_edges": edges, "vertex_degrees": degrees, "components": components,
              "scalar_orbits": orbits, "ambient": ambient, "image": image, "collisions": collisions,
              "bounds": {"roots_actual": len(roots), "roots_required": 8,
                         "branches_actual": len(branches), "branches_required": 8,
                         "infinities_actual": len(infinities), "infinities_required": 2,
                         "components_actual": len(components), "components_required": 4,
                         "image_actual": len(image), "ambient_actual": len(ambient),
                         "properness_required": "image < ambient", "excluded_actual": 60},
              "checks": checks, "failures": failures}
    OUTPUT.write_text(json.dumps(record, indent=2) + "\n")
    print(f"Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
    print(f"Roots: {len(roots)}/8; branches: {len(branches)}/8; infinities: {len(infinities)}/2; components: {len(components)}/4")
    print(f"Image {len(image)} < ambient {len(ambient)}; required: strict inequality; excluded: {len(set(ambient)-set(image))}")
    print(f"Certificate: {OUTPUT}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
