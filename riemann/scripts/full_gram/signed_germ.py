#!/usr/bin/env python3
"""Exact rational six-subset cancellation certificate; no tail truncation.

Run from riemann: python3 scripts/full_gram/signed_germ.py
The arithmetic Taylor coefficients are symbolic inputs, not measured data.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "scripts/full_gram/signed_germ_certificate.json"
ZERO = (0, 0, 0, 0)


def add(poly, key, value):
    poly[key] = poly.get(key, F(0)) + value
    if not poly[key]:
        del poly[key]


def mul(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            add(out, tuple(i+j for i, j in zip(u, v)), x*y)
    return out


def sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p))
                    for j in range(i+1, len(p)))


def alternant(exponents):
    out = {}
    for p in permutations(range(4)):
        add(out, tuple(exponents[p[j]] for j in range(4)), F(sign(p)))
    return out


DELTA = alternant((3, 2, 1, 0))


def divide_exact(numerator, denominator):
    remaining, quotient = dict(numerator), {}
    lead = max(denominator)
    while remaining:
        top = max(remaining)
        power = tuple(a-b for a, b in zip(top, lead))
        assert min(power) >= 0, (top, lead)
        coeff = remaining[top] / denominator[lead]
        add(quotient, power, coeff)
        for u, x in denominator.items():
            add(remaining, tuple(a+b for a, b in zip(u, power)), -coeff*x)
    assert mul(quotient, denominator) == numerator
    return quotient


def partitions(n, limit=None):
    if not n:
        yield ()
        return
    if limit is None:
        limit = n
    for first in range(min(n, limit), 0, -1):
        for rest in partitions(n-first, first):
            if len(rest) < 4:
                yield (first,) + rest


def schur_data(degree):
    out = []
    for part in partitions(degree):
        lam = part + (0,)*(4-len(part))
        exponents = tuple(lam[j]+3-j for j in range(4))
        s = divide_exact(alternant(exponents), DELTA)
        if degree == 2:
            value = 2*s.get((2, 0, 0, 0), 0)-s.get((1, 1, 0, 0), 0)
        elif degree == 3:
            value = 4*s.get((2, 0, 1, 0), 0)-2*s.get((1, 1, 1, 0), 0)
        else:
            value = -2*s.get((2, 0, 1, 1), 0)+s.get((1, 1, 1, 1), 0)
        out.append((exponents, F(value)))
    return out


SCHUR = {degree: schur_data(degree) for degree in (2, 3, 4)}


def pair_orders(a, b):
    return ((a, b),) if a == b else ((a, b), (b, a))


def numerator_coefficient(nu, wanted):
    """Coefficient in Delta times the full six-subset germ.

    B's input is M_ab(q1,q2) M_cd(q3,q4). The exponential is
    exp((sum_I z - sum_Ic z)/2), including the leading Hardy phase.
    """
    result = F(0)
    for I in combinations(range(4), 2):
        J = tuple(j for j in range(4) if j not in I)
        shuffle_sign = sign(I+J)
        exp_sign = tuple(1 if j in I else -1 for j in range(4))
        for left in pair_orders(*nu[:2]):
            for right in pair_orders(*nu[2:]):
                base = [0]*4
                for index, power in zip(I+J, left+right):
                    base[index] = power
                arithmetic_sign = (-1)**sum(right)
                for i, si in ((I[0], 1), (I[1], -1)):
                    for j, sj in ((J[0], 1), (J[1], -1)):
                        power = list(base)
                        power[i] += 1
                        power[j] += 1
                        remainder = [x-y for x, y in zip(wanted, power)]
                        if min(remainder) < 0:
                            continue
                        coefficient = F(shuffle_sign*arithmetic_sign*si*sj)
                        for s, r in zip(exp_sign, remainder):
                            coefficient *= F(s, 2)**r / factorial(r)
                        result += coefficient
    return result


def weights(nu):
    return tuple(sum((v*numerator_coefficient(nu, exponents)
                      for exponents, v in SCHUR[degree]), F(0))
                 if sum(nu) <= degree+4 else F(0)
                 for degree in (2, 3, 4))


def independent_numerator(nu, degree):
    """Full polynomial construction used for selected exact replay cases."""
    needed = degree+4-sum(nu)
    if needed < 0:
        return {}
    out = {}
    for I in combinations(range(4), 2):
        J = tuple(j for j in range(4) if j not in I)
        signs = tuple(1 if j in I else -1 for j in range(4))
        linear = {}
        for j, s in enumerate(signs):
            e = list(ZERO)
            e[j] = 1
            linear[tuple(e)] = F(s, 2)
        exp = {ZERO: F(1)}
        for _ in range(needed):
            exp = mul(exp, linear)
        exp = {k: v/factorial(needed) for k, v in exp.items()}
        seed = {}
        for left in pair_orders(*nu[:2]):
            for right in pair_orders(*nu[2:]):
                e = [0]*4
                for j, r in zip(I+J, left+right):
                    e[j] = r
                seed[tuple(e)] = F((-1)**sum(right)*sign(I+J))
        term = mul(seed, exp)
        for pair in (I, J):
            difference = {}
            for j, s in zip(pair, (1, -1)):
                e = [0]*4
                e[j] = 1
                difference[tuple(e)] = F(s)
            term = mul(term, difference)
        for k, v in term.items():
            add(out, k, v)
    return out


def signed_from_polynomial(poly, degree):
    if degree == 2:
        return 2*poly.get((2, 0, 0, 0), 0)-poly.get((1, 1, 0, 0), 0)
    if degree == 3:
        return 4*poly.get((2, 0, 1, 0), 0)-2*poly.get((1, 1, 1, 0), 0)
    return -2*poly.get((2, 0, 1, 1), 0)+poly.get((1, 1, 1, 1), 0)


def main():
    rows = []
    failures = []
    by_degree = {k: [F(0)]*3 for k in range(9)}
    for a in range(9):
        for b in range(a+1):
            for c in range(9-a-b):
                for d in range(min(c, 8-a-b-c)+1):
                    nu = (a, b, c, d)
                    w = weights(nu)
                    rows.append({"nu": list(nu), "degree": sum(nu),
                                 "weights": [str(v) for v in w]})
                    for j, v in enumerate(w):
                        by_degree[sum(nu)][j] += abs(v)
    lookup = {tuple(row["nu"]): tuple(F(v) for v in row["weights"])
              for row in rows}
    assert lookup[ZERO] == (F(1, 180), F(0), F(1, 5040))
    # Pair interchange conjugates B. Even signed functionals are symmetric;
    # the odd functional is antisymmetric and is multiplied by i.
    for nu, w in lookup.items():
        swapped = lookup[nu[2:]+nu[:2]]
        assert swapped == (w[0], -w[1], w[2]), (nu, w, swapped)
    # B_N(q_I(z))=exp(s*(sum_I z-sum_J z)) rescales the exponent by 1+2s.
    # The degree-two and degree-four outputs scale by powers 6 and 8.
    dilation_checks = []
    for k in range(9):
        actual = tuple(sum((w[j]/(factorial(nu[0])*factorial(nu[1])*
                                  factorial(nu[2])*factorial(nu[3]))
                            for nu, w in lookup.items() if sum(nu) == k), F(0))
                       for j in range(3))
        expected = (F(comb(6, k)*2**k, 180) if k <= 6 else F(0),
                    F(0), F(comb(8, k)*2**k, 5040))
        assert actual == expected, (k, actual, expected)
        dilation_checks.append(k)
    replay_cases = list(lookup)
    for nu in replay_cases:
        for column, degree in enumerate((2, 3, 4)):
            numerator = independent_numerator(nu, degree)
            quotient = divide_exact(numerator, DELTA)
            assert signed_from_polynomial(quotient, degree) == lookup[nu][column]
    certificate = {
        "description": "Exact symbolic arithmetic-jet weights for the full six-subset leading germ",
        "normalization": "Multiply real part by 1/zeta(2)=6/pi^2; columns multiply c0^2, i*c0*c1, c1^2",
        "arithmetic_coefficient": "h_nu=partial^nu B_N(0;a)/(nu!*(log T)^|nu|); pair-symmetric monomial-sum basis",
        "target_relative_defect": "1/2; no arithmetic-jet evaluation or positivity certificate is asserted",
        "rows": rows,
        "absolute_weight_sums_by_degree": {str(k): [str(v) for v in w]
                                           for k, w in by_degree.items()},
        "first_order": {
            "left_nu": [1, 0, 0, 0],
            "left_weights": [str(v) for v in lookup[(1, 0, 0, 0)]],
            "right_nu": [0, 0, 1, 0],
            "right_weights": [str(v) for v in lookup[(0, 0, 1, 0)]],
            "existing_scaled_jet_bound": "4/75+10/log(T), relative to Gamma",
            "c1_squared_first_order_majorant_limit": str(by_degree[1][2]*F(4, 75)/F(1, 5040)),
            "required_total_relative_budget": "1/2",
            "qualification": "64/75 is an upper-bound cost for only degree one, not an attained defect or an obstruction to the actual comparison",
        },
        "checks": {"untwisted": [str(v) for v in lookup[ZERO]],
                   "pair_interchange": "passed for every row",
                   "exact_polynomial_replay_rows": len(replay_cases),
                   "exact_polynomial_replay_degrees": [2, 3, 4],
                   "exponential_dilation_degrees": dilation_checks,
                   "failures": failures},
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"Exact rational coefficient rows: {len(rows)}; failures: {len(failures)}")
    print("Untwisted coefficients: 1/180, 0, 1/5040 (before 1/zeta(2))")
    print("Existing degree-one majorant cost (c1=1): 64/75+O(1/log T); required total <= 1/2")
    print("Actual relative defect: unresolved; required <= 1/2")
    print(f"Certificate: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
