#!/usr/bin/env python3
"""Exact N=2 full-tail signed form and a bounded orbit-insertion test.

Run from riemann: python3 scripts/full_gram/grassmannian_n2_test.py
The geometric sums are closed before differentiation. No tail cutoff,
floating-point calculation, or Haar quadrature is used.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import json

from signed_germ import (weights, independent_numerator, add, divide_exact,
                         signed_from_polynomial, DELTA)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/full_gram/grassmannian_n2_certificate.json"


def denominator_inverse(order):
    # 1 / (1 - exp(-s)/4), in ordinary power-series coefficients.
    den = [F(3, 4)] + [-F((-1)**j, 4*factorial(j))
                      for j in range(1, order+1)]
    inv = [1/den[0]]
    for k in range(1, order+1):
        inv.append(-sum((den[j]*inv[k-j] for j in range(1, k+1)),
                        F(0))/den[0])
    for k in range(order+1):
        assert sum((den[j]*inv[k-j] for j in range(k+1)), F(0)) == (k == 0)
    return inv


LEFT_TERMS = ((F(1), (1, 0, 0, 0)), (F(1), (0, 1, 0, 0)),
              (-F(1, 2), (1, 1, 1, 0)),
              (-F(1, 2), (1, 1, 0, 1)))


def amplitude_coefficient(nu, inverse):
    # [w^nu] (exp(-w1)+exp(-w2)
    #         -(exp(-w1-w2-w3)+exp(-w1-w2-w4))/2)
    #        / (1-exp(-sum(w))/4).
    result = F(0)
    for coeff, linear in LEFT_TERMS:
        for mu in product(*(range(n+1) for n in nu)):
            value = coeff
            for v, exponent in zip(linear, mu):
                value *= F((-v)**exponent, factorial(exponent))
            if not value:
                continue
            remainder = tuple(n-m for n, m in zip(nu, mu))
            k = sum(remainder)
            value *= inverse[k]*factorial(k)
            for exponent in remainder:
                value /= factorial(exponent)
            result += value
    return result


def main():
    inverse = denominator_inverse(8)
    actual = [F(0) for _ in range(9)]
    swapped = [F(0) for _ in range(9)]
    numerators = [{} for _ in range(9)]
    rows = []
    for a in range(9):
        for b in range(a+1):
            for c in range(9-a-b):
                for d in range(min(c, 8-a-b-c)+1):
                    nu = (a, b, c, d)
                    weight = weights(nu)[2]
                    value = amplitude_coefficient(nu, inverse)
                    paired = amplitude_coefficient(nu[2:]+nu[:2], inverse)
                    contribution = 5040*weight*value
                    actual[sum(nu)] += contribution
                    swapped[sum(nu)] += 5040*weight*paired
                    if value:
                        for power, coeff in independent_numerator(nu, 4).items():
                            add(numerators[sum(nu)], power, value*coeff)
                    rows.append({"nu": list(nu), "weight": str(weight),
                                 "amplitude_coefficient": str(value),
                                 "pair_swapped_coefficient": str(paired),
                                 "contribution": str(contribution)})
    assert actual == swapped
    quotients = [divide_exact(numerator, DELTA) for numerator in numerators]
    replay = [5040*signed_from_polynomial(quotient, 4) for quotient in quotients]
    assert replay == actual
    assert actual[0] == F(4, 3)
    assert actual[1] == -F(16, 9)
    derivatives = [amplitude_coefficient(tuple(int(i == j) for i in range(4)),
                                        inverse) for j in range(4)]
    assert derivatives == [-F(4, 9), -F(4, 9), F(2, 9), F(2, 9)]
    # Independent first-coefficient argument: the symmetrized amplitude
    # is 4/3 - tau*(sum_I z-sum_J z)/9 + O(tau^2).
    # Full subset extraction scales as lambda^8; a multiplicative
    # orbit integral scales as lambda^4 (both normalized to 1).
    direct_first = -F(2, 9)*8
    orbit_first = -F(2, 9)*4
    assert actual[1] == direct_first
    certificate = {
        "description": "Actual N=2 full-tail arithmetic form versus multiplicative compressed-spectrum orbit insertion",
        "parameter": "tau=log(2)/L; q is scaled before differentiation",
        "actual_form": "Q=|a1|^2+|a2|^2+sqrt(2)*Re(a1*conj(a2))*P(tau)",
        "actual_polynomial_coefficients_ascending": [str(v) for v in actual],
        "normalization": "P(0)=4/3; Gamma=|a1|^2+|a2|^2+(4*sqrt(2)/3)*Re(a1*conj(a2))",
        "tail_method": "Exact recurrence for the full infinite geometric sums, including analytic D_2(q)^(-1); no tail truncation",
        "denominator_inverse_coefficients": [str(v) for v in inverse],
        "rows": rows,
        "degree_eight_nonzero_contributions": [row for row in rows
                                               if sum(row["nu"]) == 8
                                               and F(row["contribution"])],
        "direct_quotient_polynomials": [
            [{"power": list(power), "coefficient": str(coeff)}
             for power, coeff in sorted(quotient.items())] for quotient in quotients],
        "direct_signed_extraction": [
            {"degree": k, "coefficient_2011": str(quotient.get((2, 0, 1, 1), F(0))),
             "coefficient_1111": str(quotient.get((1, 1, 1, 1), F(0))),
             "signed_times_5040": str(replay[k])}
            for k, quotient in enumerate(quotients)],
        "identity_test": {
            "constant_amplitude_actual": "1",
            "constant_amplitude_candidate": "1",
            "actual_cross_first_coefficient": str(actual[1]),
            "candidate_cross_first_coefficient": str(orbit_first),
            "first_coefficient_difference": str(actual[1]-orbit_first),
            "required_difference": "0",
            "verdict": "FAIL: multiplicative compressed-spectrum insertion is not the signed functional",
            "actual_cross_degree_eight": str(actual[8]),
            "analytic_scaled_multiplicative_insertion_maximum_degree": 4,
        },
        "verification": {
            "exact_rational_rows": len(rows),
            "denominator_inverse_convolution": "passed at every degree 0..8",
            "left_right_equality": "passed at every degree 0..8",
            "independent_first_coefficient": "passed",
            "independent_full_six_subset_polynomial_division": "passed at every degree 0..8, with exact multiply-back",
            "left_amplitude_gradient": [str(v) for v in derivatives],
            "unexpected_failures": [],
        },
        "limits": "No all-N bound, half-margin proof or refutation, positive Haar insertion, numerical onset, Xi transfer audit, or RH claim. The orbit first coefficient is proved in L631; no higher orbit coefficient is claimed computed.",
    }
    OUT.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"Exact N=2 rows: {len(rows)}; verification failures: 0")
    print(f"Constant-amplitude normalization: actual=1, candidate=1")
    print(f"First cross coefficient: actual={actual[1]}, candidate={orbit_first}")
    print(f"Identity difference={actual[1]-orbit_first}; required=0; candidate FAIL")
    print(f"Actual degree-eight cross coefficient={actual[8]}; scaled multiplicative insertion requires 0")
    print("Uniform half-margin: unresolved (required Q>=Gamma/2)")
    print(f"Certificate: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
