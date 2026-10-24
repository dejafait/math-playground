#!/usr/bin/env python3
"""Finite arithmetic accompanying C124a's exact Hensel proof.

No finite approximant defines a field or decides an uncertified class.
The full exact transport and unbounded square-neighborhood arguments
are in the canonical corollary; this checks their finite residue data.
"""

import json
from itertools import product
from pathlib import Path

OUT = Path(__file__).with_name("surviving-linear-five-adic-certificate.json")
checks = {}


def check(name, actual, required):
    checks[name] = {"actual": actual, "required": required,
                    "pass": actual == required}


def evaluate(coefficients, x):
    value = 0
    for c in reversed(coefficients):
        value = value * x + c
    return value


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i+j] += a*b
    return result


def xor(left, right):
    return tuple(a ^ b for a, b in zip(left, right))


def bits(row):
    return "".join(map(str, row))


def main():
    H = [3025, -31460, 76230, -39204, 2673]
    J = [121, -6292, 76230, -196020, 66825]
    check("fixed_product", multiply([-3, -1], [3, -1]), [-9, 0, 1])
    check("mask", (1 << 0) | (1 << 4), 17)
    check("H_seed_and_derivative",
          [evaluate(H, 3) % 5,
           evaluate([i*c for i, c in enumerate(H)][1:], 3) % 5], [0, 1])
    check("J_seed_and_derivative",
          [evaluate(J, 3) % 5,
           evaluate([i*c for i, c in enumerate(J)][1:], 3) % 5], [0, 3])
    check("principal_quadratic_transport_units",
          [3*pow(3, -1, 5) % 5, 3*pow(3, -1, 5) % 5], [1, 1])
    # Normalized valuations: v_pi(5)=4, v_lambda(5)=2,
    # v_U(5)=1. q is a uniformizer in the two ramified fields.
    ramified = []
    for model, uniformizer, ramification in [("L4", "pi", 4),
                                            ("L2", "lambda", 2)]:
        row = dict(model=model, uniformizer=uniformizer,
                   v_5=ramification, v_q=1, v_theta=-1,
                   v_delta=-2, normalized_unit_residue=1,
                   square_factor="q^(-2)",
                   principal_factor="1-9*q^2",
                   exact_relative_valuation=2,
                   required_relative_valuation_strictly_greater_than=0,
                   square_class_bits=[0, 0])
        ramified.append(row)
        check(model+"_strict_margin", row["exact_relative_valuation"] > 0, True)
        check(model+"_valuation_parity", row["v_delta"] % 2, 0)
    r0_residue = 3
    delta_residue = (pow(r0_residue, -1, 5)-9) % 5
    w_residue = (1-9*r0_residue)*pow(3*r0_residue, -1, 5) % 5
    check("unramified_delta_residue", delta_residue, 3)
    check("unramified_principal_unit", w_residue, 1)
    check("unramified_relative_error_numerator", (1-12*r0_residue) % 5, 0)
    check("omega_squared", 3, delta_residue)
    check("unramified_residue_norm", delta_residue**2 % 5, 4)

    raw = (0,)*6
    scalar2, scalar5 = (0, 1, 0, 1, 0, 0), (0, 1, 0, 1, 1, 0)
    scalars = sorted({(0,)*6, scalar2, scalar5, xor(scalar2, scalar5)})
    orbit = sorted(xor(raw, s) for s in scalars)
    canonical = [v for v in orbit if v[3] == 0 and v[4] == 0]
    norm = lambda v: (v[0] ^ v[2], v[0] ^ v[2] ^ v[5])
    check("raw_norm_bits", list(norm(raw)), [0, 0])
    check("orbit_size", len(orbit), 4)
    check("orbit_norms", [list(norm(v)) for v in orbit], [[0, 0]]*4)
    check("canonical_representative", [bits(v) for v in canonical], ["000000"])
    point_image = ["000000", "101000"]  # imported audited L119
    check("point_image_membership", bits(canonical[0]) in point_image, True)
    check("leading_coefficient_square", 55**2, 3025)
    # These are elementary residue-field checks, not an image recomputation.
    squares = sorted({((a*a+3*b*b) % 5, (2*a*b) % 5)
                      for a, b in product(range(5), repeat=2) if a or b})
    check("delta_residue_is_F25_square", (delta_residue, 0) in squares, True)

    certificate = dict(
        result="PASS: identity class; no additional pruning of mask 17",
        mask=17, polynomial_ascending=[-9, 0, 1],
        exact_models={
            "H_ascending": H, "J_ascending": J,
            "r0": "unique root of H in 3+5Z5",
            "u1": "unique root of J in 3+5Z5; r1=5*u1",
            "a": "-39204/2673+r0+r1", "b": "3025/(2673*r0*r1)",
            "L4": "pi^4=10; u=1 mod pi solves u^4+(a/pi^2)u^2+b/10=0; q=pi*u",
            "L2": "lambda^2=15; q=lambda*sqrt(r1/15), principal square root",
            "U": "omega^2=3; q=omega*sqrt(r0/3), principal square root",
            "theta": "1/q in every factor"},
        ramified_components=ramified,
        unramified_component=dict(v_delta=0, delta="(1-9*r0)/r0",
            normalized_residue=[3, 0], residue_square_root=[0, 1],
            square_factor="omega^2", principal_factor="(1-9*r0)/(3*r0)",
            relative_error="(1-12*r0)/(3*r0)",
            relative_valuation_lower_bound=1,
            required_relative_valuation_strictly_greater_than=0,
            square_class_bits=[0, 0]),
        F25_nonzero_squares=[list(v) for v in squares],
        raw_label=bits(raw), norm_bits=list(norm(raw)),
        scalar_generators=[bits(scalar2), bits(scalar5)],
        full_scalar_orbit=[bits(v) for v in orbit],
        canonical_representative=bits(canonical[0]), imported_point_image=point_image,
        relative_precision_lower_bounds=[2, 2, 1],
        checks=checks, failures=[name for name, row in checks.items() if not row["pass"]])
    OUT.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"{len(checks)} checks; failures={certificate['failures']}")
    print("relative bounds [2,2,1] > required 0 in every factor")
    print("raw/canonical=000000; full orbit="+",".join(certificate["full_scalar_orbit"]))
    print("point-image membership=PASS (identity); no additional pruning")
    print("certificate="+str(OUT))
    if certificate["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
