#!/usr/bin/env python3
"""Exact arithmetic for L071; theorem hypotheses are justified in its proof."""
import json
from fractions import Fraction as Q
from pathlib import Path


def main():
    f = lambda z: z**3 + z**2 - 2*z - 1
    root_endpoints = [Q(1), Q(5, 4)]
    assert [f(z) for z in root_endpoints] == [Q(-1), Q(1, 64)]
    # The cited full mixed square is input, not recomputed geometry.
    mixed_square = 156
    residues = []
    for p in range(12):
        for t in range(12):
            u_square = 2*p*t + mixed_square
            j = Q(48*(p+t) + 2*u_square, 4)
            chi = 8 + 2*(p+t) + Q(u_square, 12)
            assert j == 12*(p+t) + p*t + 78
            assert j.denominator == 1
            assert (j % 12 == 0) == (p*t % 12 == 6)
            assert (chi.denominator == 1) == (p*t % 6 == 0)
            if j % 12 == 0:
                residues.append([p, t])
    assert len(residues) == 20
    assert all(p != t for p, t in residues)
    checked = 0
    for m in range(-10, 31):
        for n in range(-10, 31):
            factor_pass = lambda c: c == 0 or c >= 4
            top = m*n % 12 == 6
            # Exact integer Bogomolov condition p+t<=4, with p=-m,t=-n.
            all_pass = top and -m-n <= 4 and factor_pass(m) and factor_pass(n)
            region = m >= 5 and n >= 5 and top
            assert all_pass == region
            checked += 1
    boundary = [[m, n] for m in range(5, 12) for n in range(5, 12)
                if m+n <= 11 and m*n % 12 == 6]
    assert boundary == [[5, 6], [6, 5]]
    examples = []
    for m, n in boundary:
        p, t = -m, -n
        examples.append({"a": p-4, "b": t-4,
                         "J": 12*(p+t)+p*t+78,
                         "ch4": str(Q(p*t+78, 6)),
                         "chi": str(8+2*(p+t)+Q(p*t+78, 6))})
    cert = {
        "scope": "Bounded exact arithmetic only; infinite domain and theorem use proved in L071",
        "inputs": {"full_mixed_square": mixed_square, "source": "L048"},
        "root_interval": [str(z) for z in root_endpoints],
        "root_endpoint_values": [str(f(z)) for z in root_endpoints],
        "bogomolov": {"required": "p+t <= 4lambda", "integer_equivalent": "a+b <= -4"},
        "characteristic_number": "12(p+t)+pt+78",
        "required_residue": "J=0 mod 12; equivalently pt=6 mod 12",
        "passing_residues": residues,
        "finite_intersection_check": {"charges": [-10, 30], "pairs": checked},
        "boundary": {"required_minimum_charge_sum": 11, "pairs": boundary,
                     "maximal_a_plus_b": -19, "examples": examples},
        "failures": [],
    }
    path = Path(__file__).with_name("sign_reversed_necessity_certificate.json")
    path.write_text(json.dumps(cert, indent=2) + "\n")
    print(f"PASS: 144 residues, 20 topological survivors; {checked} bounded intersection checks.")
    print("Bounds: Bogomolov integer total a+b<=-4; final actual maximum=-19.")
    print("Minimum charge sum actual/required=11/11 at (5,6),(6,5); failures=0.")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    print("Holomorphic realization and transport remain unproved.")


if __name__ == "__main__":
    main()
