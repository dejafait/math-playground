"""Exact small-instance checks of L001's abstract groups, not elliptic curves."""

import json
from itertools import product


def check_case(p, depth):
    exponent = 2 * depth
    modulus = p**exponent
    ambient = list(product(range(modulus), repeat=2))

    def pairing_numerator(x, y):
        return (x[0] * y[1] - x[1] * y[0]) % modulus

    # Pairing values are numerator/modulus in Q/Z. Testing against the
    # two generators suffices to find the radical by bilinearity.
    radical = [
        x for x in ambient
        if pairing_numerator(x, (1, 0)) == 0
        and pairing_numerator(x, (0, 1)) == 0
    ]
    assert radical == [(0, 0)]
    assert all(pairing_numerator(x, x) == 0 for x in ambient)

    def phi(n, x):
        scale = p ** (exponent - n)
        return tuple(scale * t % modulus for t in x)

    orders = []
    pairing_checks = 0
    downward_checks = 0
    upward_checks = 0
    for n in range(1, depth + 1):
        level_modulus = p**n
        free_level = list(product(range(level_modulus), repeat=2))
        torsion_level = {
            x for x in ambient
            if all(level_modulus * t % modulus == 0 for t in x)
        }
        images = {phi(n, x) for x in free_level}
        assert len(images) == len(free_level) == p ** (2 * n)
        assert images == torsion_level
        orders.append(len(images))

        for x, y in product(free_level, repeat=2):
            summed = tuple((a + b) % level_modulus for a, b in zip(x, y))
            image_sum = tuple(
                (a + b) % modulus for a, b in zip(phi(n, x), phi(n, y))
            )
            assert phi(n, summed) == image_sum
            assert pairing_numerator(phi(n, x), phi(n, y)) == 0
            pairing_checks += 1

        if n < depth:
            for x in product(range(p ** (n + 1)), repeat=2):
                reduced = tuple(t % level_modulus for t in x)
                multiplied = tuple(p * t % modulus for t in phi(n + 1, x))
                assert multiplied == phi(n, reduced)
                downward_checks += 1
            for x in free_level:
                raised = tuple(p * t % (p ** (n + 1)) for t in x)
                assert phi(n + 1, raised) == phi(n, x)
                upward_checks += 1

    return {
        "p": p,
        "observation_depth": depth,
        "sha_model_exponent": exponent,
        "sha_model_order": len(ambient),
        "common_observed_orders": orders,
        "rank_parameters": [2, 0],
        "restricted_pairing_and_addition_checks": pairing_checks,
        "downward_transition_checks": downward_checks,
        "upward_transition_checks": upward_checks,
    }


def main():
    cases = [check_case(p, depth) for p in (2, 3) for depth in (1, 2)]
    print(json.dumps({
        "scope": "Abstract finite groups only; no elliptic-curve realization asserted",
        "result": "PASS",
        "cases": cases,
    }, indent=2))


if __name__ == "__main__":
    main()
