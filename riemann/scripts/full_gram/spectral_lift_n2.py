#!/usr/bin/env python3
"""Exact fixed-N=2 Vandermonde spectral-lift test, with the full tail.

Run from riemann: python3 scripts/full_gram/spectral_lift_n2.py
Uses determinant Taylor expansion, not the six-subset extraction weights.
Geometric moments sum every tail index exactly; no quadrature is used.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import json

from signed_germ import (add, alternant, divide_exact, mul, partitions,
                         signed_from_polynomial, DELTA)
from grassmannian_n2_test import amplitude_coefficient, denominator_inverse

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/full_gram/spectral_lift_n2_certificate.json"
ZERO = (0, 0, 0, 0)
YSTAR = (F(1, 2), F(1, 2), -F(1, 2), -F(1, 2))
SIGNS = (1, 1, -1, -1)
LEFT = ((F(1), (1, 0, 0, 0)), (F(1), (0, 1, 0, 0)),
        (-F(1, 2), (1, 1, 1, 0)), (-F(1, 2), (1, 1, 0, 1)))
EXPECTED = tuple(map(F, ("4/3", "-16/9", "-385/27", "-14/27",
                         "15680/81", "-227269/243", "914228/243",
                         "-7929146/729", "34439992/2187")))


def encode(poly):
    return [{"power": list(power), "coefficient": str(value)}
            for power, value in sorted(poly.items())]


def derivative(poly, orders):
    result = {}
    for power, coefficient in poly.items():
        if any(e < n for e, n in zip(power, orders)):
            continue
        target = tuple(e-n for e, n in zip(power, orders))
        value = coefficient
        for e, n in zip(power, orders):
            value *= factorial(e)//factorial(e-n)
        add(result, target, value)
    return result


def evaluate(poly, point):
    result = F(0)
    for power, coefficient in poly.items():
        value = coefficient
        for y, exponent in zip(point, power):
            value *= y**exponent
        result += value
    return result


def moments(order):
    # M_k=sum_{j>=0} j^k/4^j, with j^0=1 also at j=0.
    result = [F(4, 3)]
    for k in range(1, order+1):
        result.append(sum((comb(k, r)*result[r] for r in range(k)),
                          F(0))/3)
    return result


def shifted_polynomial(poly, b):
    """Return [tau^k j^r] H(y_* - tau*sigma*(b+j*1))."""
    result = {}
    for powers, coefficient in poly.items():
        term = {(0, 0): coefficient}
        for exponent, y, sigma, offset in zip(powers, YSTAR, SIGNS, b):
            factor = {}
            for k in range(exponent+1):
                base = comb(exponent, k)*y**(exponent-k)*(-sigma)**k
                for r in range(k+1):
                    add(factor, (k, r), base*comb(k, r)*offset**(k-r))
            term = mul(term, factor)
        for power, value in term.items():
            add(result, power, value)
    return result


def translation_extraction(poly, terms, moment_values):
    values = [F(0)]*9
    records = []
    for coefficient, b in terms:
        shifted = shifted_polynomial(poly, b)
        contracted = [F(0)]*9
        for (k, r), value in shifted.items():
            contracted[k] += coefficient*value*moment_values[r]
        values = [x+y for x, y in zip(values, contracted)]
        records.append({"numerator_coefficient": str(coefficient),
                        "b": list(b), "tau_j_polynomial": encode(shifted),
                        "contracted_coefficients": [str(x) for x in contracted]})
    return values, records


def main():
    # det(exp(z_i*y_j))/Delta(z) has degree-four z part
    # sum_{lambda |- 4} s_lambda(z)*Alt_(lambda+delta)(y)/prod m_i!.
    kernel = {}
    schur_rows = []
    for partition in partitions(4):
        lam = partition+(0,)*(4-len(partition))
        exponents = tuple(lam[i]+3-i for i in range(4))
        alt = alternant(exponents)
        schur = divide_exact(alt, DELTA)
        signed = signed_from_polynomial(schur, 4)
        denominator = 1
        for e in exponents:
            denominator *= factorial(e)
        coefficient = F(5040)*signed/denominator
        confluent_value = evaluate(derivative(alt, (0, 1, 0, 1)), YSTAR)
        for powers, value in alt.items():
            add(kernel, powers, coefficient*value)
        schur_rows.append({"partition": list(partition),
                           "exponents": list(exponents),
                           "schur_polynomial": encode(schur),
                           "signed_schur_value": str(signed),
                           "factorial_product": denominator,
                           "kernel_coefficient": str(coefficient),
                           "confluent_alternant_value": str(confluent_value),
                           "constant_contribution": str(coefficient*confluent_value)})

    h = derivative(kernel, (0, 1, 0, 1))
    constant = evaluate(h, YSTAR)
    moment_values = moments(8)
    left, left_records = translation_extraction(h, LEFT, moment_values)
    right_terms = tuple((c, b[2:]+b[:2]) for c, b in LEFT)
    right, right_records = translation_extraction(h, right_terms, moment_values)

    # A second evaluation uses the finite Taylor differential operator.
    # It shares only the already recorded exact rational amplitude formula.
    inverse = denominator_inverse(8)
    jet_values = [F(0)]*9
    jet_right = [F(0)]*9
    jet_rows = []
    for nu in product(range(9), repeat=4):
        degree = sum(nu)
        if degree > 8:
            continue
        value = evaluate(derivative(h, nu), YSTAR)
        sign = (-1)**(nu[2]+nu[3])
        amplitude = amplitude_coefficient(nu, inverse)
        swapped = amplitude_coefficient(nu[2:]+nu[:2], inverse)
        contribution = sign*amplitude*value
        contribution_right = sign*swapped*value
        jet_values[degree] += contribution
        jet_right[degree] += contribution_right
        jet_rows.append({"nu": list(nu), "signed_derivative": str(sign*value),
                         "amplitude_coefficient": str(amplitude),
                         "swapped_amplitude_coefficient": str(swapped),
                         "contribution": str(contribution),
                         "swapped_contribution": str(contribution_right)})

    checks = {
        "five_degree_four_partitions": len(schur_rows) == 5,
        "kernel_homogeneous_degree_ten": all(sum(e) == 10 for e in kernel),
        "confluent_kernel_homogeneous_degree_eight": all(sum(e) == 8 for e in h),
        "constant_amplitude_equals_one": constant == 1,
        "full_geometric_translation_matches_all_nine": tuple(left) == EXPECTED,
        "pair_swap_matches_all_nine": right == left,
        "finite_jet_matches_geometric_translation": jet_values == left,
        "swapped_finite_jet_matches_translation": jet_right == right,
        "all_495_multiindices_checked": len(jet_rows) == 495,
    }
    failures = [name for name, passed in checks.items() if not passed]
    certificate = {
        "description": "Full-Vandermonde HCIZ spectral-derivative lift at actual N=2",
        "definition": "(1/12)*d_y2*d_y4*B_2(d_y1/L,d_y2/L,-d_y3/L,-d_y4/L;a)[Delta(y)*I_4(z,y)] at y_*",
        "normalization": {"constant_amplitude_actual": "1",
                          "constant_amplitude_lift": str(constant),
                          "required_difference": "0", "difference": str(constant-1)},
        "diagnostic": [
            {"degree": k, "actual": str(EXPECTED[k]), "lift": str(left[k]),
             "pair_swapped_lift": str(right[k]), "finite_jet": str(jet_values[k]),
             "difference": str(left[k]-EXPECTED[k])} for k in range(9)],
        "geometric_moments": [str(x) for x in moment_values],
        "schur_determinant_rows": schur_rows,
        "kernel_degree_ten": encode(kernel),
        "confluent_kernel_degree_eight": encode(h),
        "left_translation_terms": left_records,
        "right_translation_terms": right_records,
        "finite_jet_rows": jet_rows,
        "verification": {"checks": checks, "failures": failures,
                         "required_all_coefficient_differences": "0"},
        "limits": "Exact N=2 germ identity proved in L632; certificate checks finite algebra only. No all-N domination, lower bound, signed-positive orbit integral, Xi transfer audit or RH conclusion.",
    }
    OUT.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"Constant amplitude: actual=1, lift={constant}; required difference=0")
    print(f"Cross coefficients: {sum(left[k] == EXPECTED[k] for k in range(9))}/9 exact matches; required=9/9")
    print(f"Highest coefficient: lift={left[8]}, required={EXPECTED[8]}")
    print(f"Translation/finite-jet and pair-swap checks: {len(jet_rows)} exact multiindices")
    print(f"Failures: {failures}")
    print("Uniform growing-N target Q>=Gamma/2 with error reserve: unproved")
    print(f"Certificate: {OUT.relative_to(ROOT)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
