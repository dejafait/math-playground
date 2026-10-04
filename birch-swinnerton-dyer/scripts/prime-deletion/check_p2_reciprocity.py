"""Exact finite localization checks for L016; no arithmetic realization.

Run from the notebook directory:
    python3 scripts/prime-deletion/check_p2_reciprocity.py
The enumeration checks the entire orthogonal complement at p = 5, as
well as coefficient kernels and all two-prime equations used in L015.
It does not construct components at further primes or a full system.
"""

from itertools import product
import json
from pathlib import Path


def check_case(p, tau):
    modulus = p * p

    def add(x, y):
        return tuple((a + b) % modulus for a, b in zip(x, y))

    def scale(a, x):
        return tuple(a * b % modulus for b in x)

    def pair(x, y):
        return (x[0] * y[1] + x[1] * y[0]
                + x[2] * y[3] + x[3] * y[2]) % modulus

    def reduce(x):
        return tuple(a % p for a in x)

    c1 = (1, 0, 0, p * tau % modulus)
    c2 = (0, -p * tau % modulus, 1, 0)
    g1 = scale(p * tau, c2)
    g2 = scale(-p * tau, c1)
    zero = (0, 0, 0, 0)
    graph = {add(scale(a, c1), scale(b, c2))
             for a, b in product(range(modulus), repeat=2)}
    assert len(graph) == modulus**2
    assert pair(c1, c1) == pair(c2, c2) == pair(c1, c2) == 0
    assert all(pair(x, y) == pair(y, x)
               for x in (c1, c2, g1, g2) for y in (c1, c2, g1, g2))

    # Exhaust the ambient module, not just the graph generators.
    orthogonal = {x for x in product(range(modulus), repeat=4)
                  if pair(x, c1) == 0 and pair(x, c2) == 0}
    assert orthogonal == graph

    residual_finite = {(a, 0, b, 0) for a, b in product(range(p), repeat=2)}
    assert {reduce(x) for x in graph} == residual_finite
    socle = {(p * a, 0, p * b, 0)
             for a, b in product(range(p), repeat=2)}
    assert {x for x in graph if reduce(x) == zero} == socle
    assert {scale(p, x) for x in graph} == socle
    assert scale(p, c1) == (p, 0, 0, 0)
    assert scale(p, c2) == (0, 0, p, 0)

    # Finite / transverse modifications and Cartesian residual propagation.
    modified1 = {x for x in graph if x[2] == 0}
    modified2 = {x for x in graph if x[0] == 0}
    assert modified1 == {scale(a, c1) for a in range(modulus)}
    assert modified2 == {scale(a, c2) for a in range(modulus)}
    assert {reduce(x) for x in modified1} == {(a, 0, 0, 0) for a in range(p)}
    assert {reduce(x) for x in modified2} == {(0, 0, b, 0) for b in range(p)}

    # v_i is the singular coordinate and phi_i the finite coordinate.
    assert g1 in socle and g2 in socle
    assert reduce(g1) == reduce(g2) == zero
    assert c1[1] == c2[3] == g1[1] == g2[3] == 0
    assert c1[3] == g1[2] and c2[1] == g2[0]
    assert g1[0] == g2[2] == 0
    assert (pair(c1, c2)) % modulus == 0

    # The obstruction form must have the same radical as the lift image.
    def obstruction(x, y):
        return tau * (x[0] * y[1] - x[1] * y[0]) % p

    residual_coordinates = list(product(range(p), repeat=2))
    radical = {x for x in residual_coordinates
               if all(obstruction(x, y) == 0 for y in residual_coordinates)}
    classical = {x for x in graph if x[1] == x[3] == 0}
    reduction_image = {(x[0] % p, x[2] % p) for x in classical}
    assert radical == reduction_image
    assert len(classical) == (p**4 if tau == 0 else p**2)
    assert len(reduction_image) == (p**2 if tau == 0 else 1)
    assert all(obstruction(x, x) == 0 for x in residual_coordinates)
    assert all((obstruction(x, y) + obstruction(y, x)) % p == 0
               for x in residual_coordinates for y in residual_coordinates)
    return {
        "p": p,
        "tau": tau,
        "ambient_size": modulus**4,
        "relaxed_group_size": len(graph),
        "orthogonal_complement_size": len(orthogonal),
        "classical_group_size": len(classical),
        "classical_reduction_image_size": len(reduction_image),
        "one_prime_scalar_errors_zero": True,
        "two_prime_finite_singular_relations": "PASS",
        "obstruction_radical_equals_reduction_image": True,
    }


def main():
    result = {
        "exact_localization_checks": "PASS",
        "cases": [check_case(5, tau) for tau in (0, 1)],
        "full_kato_system_constructed": False,
        "arithmetic_realization_asserted": False,
        "actual_arithmetic_tau_evaluated": False,
    }
    output = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("p2-reciprocity-result.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
