#!/usr/bin/env python3
"""Exact finite contraction for L634; no numerical or asymptotic simulation.

The analytic local-row estimates are proved in L634, not certified by this
script. All arithmetic below is rational. Run from the active notebook:
PYTHONDONTWRITEBYTECODE=1 python3 scripts/full_gram/normalized_row_margin.py
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import json

from signed_germ import add, alternant, weights
from spectral_lift_n2 import derivative, evaluate, YSTAR

OUT = Path(__file__).resolve().parent / 'normalized_row_margin_certificate.json'


def main():
    kernel = {}
    for powers, coefficient in [((7, 2, 1, 0), -F(1, 2)),
                                ((6, 3, 1, 0), -F(7, 6)),
                                ((5, 3, 2, 0), F(7, 2)),
                                ((4, 3, 2, 1), F(35, 2))]:
        for nu, value in alternant(powers).items():
            add(kernel, nu, coefficient * value)
    h = derivative(kernel, (0, 1, 0, 1))
    rows, comparison = [], []
    maxima = [F(0)] * 9
    for nu in product(range(9), repeat=4):
        k = sum(nu)
        if k > 8:
            continue
        orbit = sorted({nu, (nu[1], nu[0], nu[2], nu[3]),
                        (nu[0], nu[1], nu[3], nu[2]),
                        (nu[1], nu[0], nu[3], nu[2])})
        values = [(-1)**(w[2]+w[3]) * evaluate(derivative(h, w), YSTAR)
                  for w in orbit]
        average = sum(values, F(0)) / len(orbit)
        maxima[k] = max(maxima[k], abs(average))
        rows.append({'nu': list(nu), 'degree': k,
                     'orbit': [list(w) for w in orbit],
                     'signed_derivatives': [str(v) for v in values],
                     'average': str(average)})
        if nu[0] >= nu[1] and nu[2] >= nu[3]:
            source = 5040 * weights(nu)[2]
            actual = average * len(orbit)
            comparison.append({'nu': list(nu), 'orbit_sum': str(actual),
                               'six_subset_weight': str(source),
                               'difference': str(actual-source)})

    expected = list(map(F, ('1', '4', '35/2', '84', '420', '840',
                            '2520', '2520', '5040')))
    # exp(2u + 4(exp(u)-1)), using k a_k=sum_(j=1)^k j b_j a_(k-j).
    exponent = [F(0)] + [F(4, factorial(k)) + (2 if k == 1 else 0)
                           for k in range(1, 9)]
    majorant = [F(1)]
    for k in range(1, 9):
        majorant.append(sum((j*exponent[j]*majorant[k-j]
                              for j in range(1, k+1)), F(0))/k)
    costs = [maxima[k]*majorant[k]/100**k for k in range(1, 9)]
    total = sum(costs, F(0))

    # Finite exact diagnostics of the universal U_d identity used in the
    # proof. The proof itself covers every d, not just these test indices.
    local_checks = []
    for d in range(1, 13):
        for k in range(9):
            direct = F((d+1)*d**k - 2*d*(d-1)**k
                       + ((d-1)*(d-2)**k if d >= 2 else 0), factorial(k))
            # Positive-factor decomposition: two single factors and a
            # convolution of two differences of exponentials.
            positive = 2*F(d**k-(d-1)**k, factorial(k))
            if d >= 2:
                positive += sum((F(comb(k, j), factorial(k)) *
                                 ((r+1)**j-r**j) *
                                 ((d-1-r)**(k-j)-(d-2-r)**(k-j))
                                 for r in range(d-1) for j in range(k+1)), F(0))
            local_checks.append({'d': d, 'degree': k, 'coefficient': str(direct),
                                 'positive_decomposition': str(positive),
                                 'difference': str(direct-positive)})

    checks = {
        'homogeneous_degree_eight': all(sum(nu) == 8 for nu in h),
        'constant_normalization': evaluate(h, YSTAR) == 1,
        'all_495_derivatives': len(rows) == 495,
        'all_175_pair_symmetric_comparisons': len(comparison) == 175,
        'six_subset_agreement': all(F(r['difference']) == 0 for r in comparison),
        'degreewise_maxima': maxima == expected,
        'U_positive_decomposition': all(F(r['difference']) == 0 for r in local_checks),
        'U_nonnegative': all(F(r['coefficient']) >= 0 for r in local_checks),
        'strict_reserve_below_three_tenths': total < F(3, 10),
        'strict_reserve_below_one_half': total < F(1, 2),
    }
    failures = [name for name, value in checks.items() if not value]
    result = {
        'description': 'Exact L634 spectral contraction and local polynomial diagnostics',
        'qualification': 'Analytic uniformity, tensor-row bounds and input identities require the written proof; this is not an RH or independent audit certificate.',
        'spectral_polynomial': [{'nu': list(nu), 'coefficient': str(c)}
                                for nu, c in sorted(h.items())],
        'all_signed_derivative_orbits': rows,
        'six_subset_comparison': comparison,
        'local_U_diagnostics': local_checks,
        'degreewise_maxima': [str(c) for c in maxima],
        'majorant': {'expression': 'exp(2u+4(exp(u)-1))',
                     'exponent_coefficients': [str(c) for c in exponent],
                     'coefficients': [str(c) for c in majorant]},
        'contraction': {'theta_upper_bound': '1/100',
                        'degree_costs': [str(c) for c in costs],
                        'total_exact': str(total), 'total_decimal_preview': float(total),
                        'eventual_row_bound': '3/10', 'required_threshold': '1/2',
                        'eventual_Q_over_Gamma': '7/10', 'epsilon': '1/5'},
        'checks': checks, 'failures': failures,
    }
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Exact derivative rows: {len(rows)}; independent six-subset comparisons: {len(comparison)}')
    print(f'Row limsup bound: {total} = {float(total):.17g}; eventual bound 3/10; required < 1/2')
    print(f'Failures: {failures}')
    print(f'Certificate: {OUT.relative_to(OUT.parents[2])}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
