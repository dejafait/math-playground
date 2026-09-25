#!/usr/bin/env python3
"""Exact controls for L008; no search for complete Beal solutions."""
import json
from math import comb, gcd, isqrt
from pathlib import Path

P = 31
Q = 373
T_BASE = 3 ** (P - 2)


def coefficient(r, t, modulus):
    return sum(
        comb(P, 2 * j + 1)
        * pow(r, P - 2 * j - 1, modulus)
        * pow(-3 * t * t, j, modulus)
        for j in range((P + 1) // 2)
    ) % modulus


def derivative(r, t, modulus):
    return sum(
        (P - 2 * j - 1)
        * comb(P, 2 * j + 1)
        * pow(r, P - 2 * j - 2, modulus)
        * pow(-3 * t * t, j, modulus)
        for j in range((P - 1) // 2)
    ) % modulus


def lucas(r, v, modulus=None):
    us, ts = [0, 1], [2, r]
    for _ in range(2, P + 1):
        u = r * us[-1] - v * us[-2]
        trace = r * ts[-1] - v * ts[-2]
        us.append(u if modulus is None else u % modulus)
        ts.append(trace if modulus is None else trace % modulus)
    return us, ts


def exact_valuation_residue(m):
    """A root to precision m, followed by a deliberately non-root digit."""
    root = 4
    precision = Q
    deriv = derivative(root, T_BASE, Q)
    assert deriv == 90
    for _ in range(1, m):
        residue = coefficient(root, T_BASE, precision * Q)
        assert residue % precision == 0
        digit = -(residue // precision) * pow(deriv, -1, Q) % Q
        root += digit * precision
        precision *= Q
        assert coefficient(root, T_BASE, precision) == 0
    residue = coefficient(root, T_BASE, precision * Q)
    unique_lift = -(residue // precision) * pow(deriv, -1, Q) % Q
    other_digit = (unique_lift + 1) % Q
    chosen = root + other_digit * precision
    assert coefficient(chosen, T_BASE, precision * Q) % precision == 0
    assert coefficient(chosen, T_BASE, precision * Q) != 0
    return chosen, precision * Q


def make_control(m):
    chosen, modulus = exact_valuation_residue(m)
    d = (chosen - 33 * T_BASE) % modulus
    d += modulus * ((5 - 33 * T_BASE - d) * pow(modulus, -1, 24) % 24)
    if d == 0:
        d = 24 * modulus
    h = 1 + 24 * P * modulus * d
    t = T_BASE * h ** P
    r = 33 * t + d
    assert t > d > 0
    assert r % 24 == 5 and t % 24 == T_BASE % 24
    assert gcd(r, t) == 1 and h % P == 1
    assert r % modulus == chosen and t % modulus == T_BASE % modulus
    assert (r * r + 3 * t * t) % 4 == 0
    v = (r * r + 3 * t * t) // 4
    assert v % 12 == 1 and gcd(r, v) == gcd(t, v) == 1
    us, ts = lucas(r, v)
    u, trace = us[P], ts[P]
    w = t * u
    assert u > 0 and abs(trace) < 3 * w
    assert trace * trace + 3 * w * w == 4 * v ** P
    assert u % (Q ** m) == 0 and u % modulus != 0
    assert coefficient(r, t, modulus) == (2 ** (P - 1) * u) % modulus
    assert gcd(Q, 3 * t * v) == 1
    assert all(value % Q for value in us[1:P])
    # This extra control checks whether the complete power condition is false
    # modulo 311; failure to obstruct would not make the construction a solution.
    test_prime = 311
    power_residues = sorted({pow(a, P, test_prime) for a in range(test_prime)})
    u_residue = u % test_prime
    return {
        "multiplicity": m,
        "lifted_r_residue": chosen,
        "lift_modulus": modulus,
        "D": d,
        "N": 1,
        "h_bit_length": h.bit_length(),
        "U_bit_length": u.bit_length(),
        "primitive_divisor": Q,
        "exact_valuation": m,
        "earlier_terms_nonzero_mod_373": P - 1,
        "norm_coprimality_and_trace_checks": "PASS",
        "power_test_prime": test_prime,
        "U_mod_311": u_residue,
        "31st_power_residues_mod_311": power_residues,
        "complete_power_condition_excluded_mod_311": u_residue not in power_residues,
    }


def main():
    assert all(Q % d for d in range(2, isqrt(Q) + 1))
    assert all(311 % d for d in range(2, isqrt(311) + 1))
    assert 177 * 177 % Q == Q - 3
    a, b = (4 + 177 * T_BASE) % Q, (4 - 177 * T_BASE) % Q
    ratio = a * pow(b, -1, Q) % Q
    assert (a, b, ratio) == (138, 243, 217)
    assert ratio != 1 and pow(ratio, P, Q) == 1
    assert coefficient(4, T_BASE, Q) == 0
    assert derivative(4, T_BASE, Q) == 90
    controls = [make_control(m) for m in (1, 2, 31)]
    result = {
        "status": "PASS",
        "scope": "Exact controls for primitive-divisor multiplicity; no general emptiness claim.",
        "p": P,
        "q": Q,
        "base_t": T_BASE,
        "root_mod_q": 4,
        "ratio_mod_q": ratio,
        "derivative_mod_q": 90,
        "controls": controls,
    }
    Path(__file__).with_name("results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "multiplicities": [x["multiplicity"] for x in controls],
                      "power_condition_excluded_mod_311": [x["complete_power_condition_excluded_mod_311"] for x in controls]}))


if __name__ == "__main__":
    main()
