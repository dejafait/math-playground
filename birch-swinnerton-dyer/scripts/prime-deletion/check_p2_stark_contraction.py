"""Exact divisor-subsystem checks for L017; no full arithmetic family.

Run from the notebook directory:
    python3 scripts/prime-deletion/check_p2_stark_contraction.py
The exterior coordinates below represent the free summands used by the
specified bidual elements. No identification of whole nonfree exterior
powers with exterior biduals is made.
"""

from itertools import combinations, product
import json
from pathlib import Path


def check_case(p, tau):
    modulus = p * p
    dimension = 3  # x_1, x_2, w

    def exterior(degree, values=None):
        values = values or {}
        return {indices: values.get(indices, 0) % modulus
                for indices in combinations(range(dimension), degree)}

    def scale(a, element):
        return {indices: a * value % modulus
                for indices, value in element.items()}

    def contract(form, element):
        degree = len(next(iter(element)))
        assert degree >= 1
        result = exterior(degree - 1)
        for indices, value in element.items():
            for position, index in enumerate(indices):
                target = indices[:position] + indices[position + 1:]
                result[target] += (-1)**position * form[index] * value
                result[target] %= modulus
        return result

    def scalar(element):
        assert set(element) == {()}
        return element[()]

    phi = (0, 0, 1)
    s1 = (0, -p * tau % modulus, 0)
    s2 = (p * tau % modulus, 0, 0)
    f1 = (1, 0, 0)
    f2 = (0, 1, 0)
    eta0 = {"N": exterior(2, {(0, 1): 1})}
    eta1 = {"N": exterior(3, {(0, 1, 2): 1})}

    # Determinant orientations make the divisor paths agree. Rank one
    # has the opposite edge signs because phi anticommutes with s_i.
    edges = (
        ("N", "ell1", s2, 1),
        ("N", "ell2", s1, -1),
        ("ell1", "1", s1, 1),
        ("ell2", "1", s2, 1),
    )
    for source, target, form, sign in edges:
        next0 = scale(sign, contract(form, eta0[source]))
        next1 = scale(-sign, contract(form, eta1[source]))
        if target in eta0:
            assert eta0[target] == next0
            assert eta1[target] == next1
        else:
            eta0[target] = next0
            eta1[target] = next1
        assert contract(phi, next1) == next0

    for divisor in eta0:
        assert contract(phi, eta1[divisor]) == eta0[divisor]
    assert eta0["ell1"] == exterior(1, {(1,): p * tau})
    assert eta0["ell2"] == exterior(1, {(0,): -p * tau})
    assert eta1["ell1"] == exterior(2, {(1, 2): -p * tau})
    assert eta1["ell2"] == exterior(2, {(0, 2): p * tau})
    assert eta0["1"] == exterior(0)
    assert eta1["1"] == exterior(1)
    assert all(scale(p, eta0[d]) == exterior(1)
               for d in ("ell1", "ell2"))
    assert any(eta0["ell1"].values()) == (tau != 0)
    assert any(eta0["ell2"].values()) == (tau != 0)

    # Contraction at the top index is an isomorphism of determinant lines.
    images = {tuple(contract(phi, scale(a, eta1["N"])).values())
              for a in range(modulus)}
    assert len(images) == modulus
    assert images == {tuple(scale(a, eta0["N"]).values())
                      for a in range(modulus)}

    # Scalar-regulator diagrams at all four divisors.
    delta = {
        "N": -scalar(contract(f2, contract(f1, eta0["N"]))) % modulus,
        "ell1": scalar(contract(f1, eta0["ell1"])),
        "ell2": scalar(contract(f2, eta0["ell2"])),
        "1": scalar(eta0["1"]),
    }
    rank_one = {
        "N": scale(-1, contract(f2, contract(f1, eta1["N"]))),
        "ell1": scale(-1, contract(f1, eta1["ell1"])),
        "ell2": scale(-1, contract(f2, eta1["ell2"])),
        "1": eta1["1"],
    }
    assert delta == {"N": modulus - 1, "ell1": 0, "ell2": 0, "1": 0}
    assert all(scalar(contract(phi, rank_one[d])) == delta[d]
               for d in delta)
    assert all(rank_one[d] == exterior(1) for d in ("ell1", "ell2", "1"))

    c1 = scale(-1, contract(f2, eta0["N"]))
    c2 = contract(f1, eta0["N"])
    assert c1 == exterior(1, {(0,): 1})
    assert c2 == exterior(1, {(1,): 1})
    g1, g2 = eta0["ell1"], eta0["ell2"]
    assert scalar(contract(s2, c1)) == scalar(contract(f2, g1))
    assert scalar(contract(s1, c2)) == scalar(contract(f1, g2))
    assert scalar(contract(f1, g1)) == scalar(contract(f2, g2)) == 0
    assert scalar(contract(s1, c1)) == scalar(contract(s2, c2)) == 0

    # Exact module counts for the canonical p-local sequence and modified
    # groups. The six-coordinate ambient orthogonal complement is given
    # by three linear equations, rather than enumerating 25^6 points.
    canonical = list(product(range(modulus), repeat=3))
    relaxed = {(a, b, 0) for a, b in product(range(modulus), repeat=2)}
    assert {x for x in canonical if x[2] == 0} == relaxed
    assert {x[2] for x in canonical} == set(range(modulus))

    def localize(x):
        a, b, z = x
        return (a, -p * tau * b % modulus, b, p * tau * a % modulus, 0, z)

    def pair(x, y):
        return sum(x[i] * y[i + 1] + x[i + 1] * y[i]
                   for i in (0, 2, 4)) % modulus

    generators = [localize(x) for x in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    assert all(pair(x, y) == 0 for x in generators for y in generators)
    for x in canonical:
        local = localize(x)
        assert local[1] == -p * tau * local[2] % modulus
        assert local[3] == p * tau * local[0] % modulus
        assert local[4] == 0

    modified1 = {x for x in relaxed if localize(x)[3] == 0}
    modified2 = {x for x in relaxed if localize(x)[1] == 0}
    classical = modified1 & modified2
    assert tuple(g1[(i,)] for i in range(3)) in modified1
    assert tuple(g2[(i,)] for i in range(3)) in modified2
    assert len(modified1) == len(modified2) == (p**4 if tau == 0 else p**3)
    assert len(classical) == (p**4 if tau == 0 else p**2)
    reduction_image = {tuple(a % p for a in x) for x in classical}
    assert len(reduction_image) == (p**2 if tau == 0 else 1)

    # The residual determinant diagram and local lines do not depend on
    # tau; one-prime vectors reduce to zero for every case.
    assert all(all(value % p == 0 for value in eta0[d].values())
               for d in ("ell1", "ell2", "1"))
    assert all(all(value % p == 0 for value in eta1[d].values())
               for d in ("ell1", "ell2", "1"))
    assert {tuple(a % p for a in x) for x in relaxed} == {
        (a, b, 0) for a, b in product(range(p), repeat=2)
    }

    return {
        "p": p,
        "tau": tau,
        "canonical_group_size": len(canonical),
        "p_local_kernel_size": len(relaxed),
        "classical_group_size": len(classical),
        "classical_reduction_image_size": len(reduction_image),
        "one_prime_stark_vectors_nonzero": tau != 0,
        "proper_divisor_scalars_zero": True,
        "top_scalar_unit": True,
        "determinant_transfer_isomorphism": True,
        "both_divisor_paths_and_phi_diagrams": "PASS",
    }


def main():
    result = {
        "exact_stark_divisor_checks": "PASS",
        "cases": [check_case(5, tau) for tau in range(5)],
        "full_stark_or_kato_family_constructed": False,
        "arithmetic_realization_asserted": False,
        "actual_arithmetic_tau_evaluated": False,
    }
    output = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("p2-stark-contraction-result.json").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
