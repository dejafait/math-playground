#!/usr/bin/env python3
"""Exact finite observer contraction using L634's proved analytic row bound.

Run from riemann with PYTHONDONTWRITEBYTECODE=1. This checks all three
L629 channels by full polynomial division and writes the full certificate.
It does not audit the infinite-row proof or the analytic transfer.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

from signed_germ import (DELTA, ZERO, weights, independent_numerator,
                         divide_exact, signed_from_polynomial)

OUT = Path(__file__).resolve().parent / 'full_observer_row_budget_certificate.json'


def main():
    rows, replay, lookup = [], [], {}
    maxima = [F(0)] * 9
    maximizers = [None] * 9
    for a in range(9):
        for b in range(a+1):
            for c in range(9-a-b):
                for d in range(min(c, 8-a-b-c)+1):
                    nu = (a, b, c, d)
                    k = sum(nu)
                    w = weights(nu)
                    lookup[nu] = w
                    orbit = (1 if a == b else 2)*(1 if c == d else 2)
                    # Normalize by B(c). In x=sqrt(28)c0, y=c1,
                    # sqrt(28)>5 bounds the imaginary cross coefficient.
                    aa, dd = 180*abs(w[0])/orbit, 5040*abs(w[2])/orbit
                    cross = 1008*abs(w[1])/orbit
                    bound = max(aa, dd)+cross/2
                    if bound > maxima[k]:
                        maxima[k], maximizers[k] = bound, nu
                    rows.append({'nu': list(nu), 'degree': k, 'orbit_size': orbit,
                                 'weights': list(map(str, w)),
                                 'normalized_abs_c0_diagonal': str(aa),
                                 'normalized_abs_c1_diagonal': str(dd),
                                 'imaginary_cross_upper_bound': str(cross),
                                 'uniform_observer_bound': str(bound)})
                    for column, degree in enumerate((2, 3, 4)):
                        numerator = independent_numerator(nu, degree)
                        quotient = divide_exact(numerator, DELTA)
                        actual = signed_from_polynomial(quotient, degree)
                        replay.append({'nu': list(nu), 'output_degree': degree,
                                       'quotient': [{'nu': list(power), 'value': str(value)}
                                                    for power, value in sorted(quotient.items())],
                                       'weight': str(actual), 'difference': str(actual-w[column])})

    exponent = [F(0)]+[F(4, factorial(k))+(2 if k == 1 else 0) for k in range(1, 9)]
    majorant = [F(1)]
    for k in range(1, 9):
        majorant.append(sum((j*exponent[j]*majorant[k-j]
                             for j in range(1, k+1)), F(0))/k)
    # Replay the finite exponential by a different computation.
    power, replay_majorant = [F(1)]+[F(0)]*8, [F(1)]+[F(0)]*8
    for j in range(1, 9):
        power = [sum((power[i]*exponent[k-i] for i in range(k+1)), F(0)) for k in range(9)]
        replay_majorant = [a+b/factorial(j) for a, b in zip(replay_majorant, power)]
    costs = [maxima[k]*majorant[k]/100**k for k in range(1, 9)]
    total = sum(costs, F(0))
    expected = list(map(F, ('1', '27/5', '301/10', '105', '420',
                            '840', '2520', '2520', '5040')))
    checks = {
        'all_175_orbits': len(rows) == 175,
        'all_495_multiindices_accounted_for': sum(r['orbit_size'] for r in rows) == 495,
        'all_525_polynomial_divisions': len(replay) == 525,
        'all_polynomial_weights_match': all(F(r['difference']) == 0 for r in replay),
        'zero_shift_reference_normalization': lookup[ZERO] == (F(1, 180), F(0), F(1, 5040)),
        'pair_exchange_Hermitian_symmetry': all(lookup[nu[2:]+nu[:2]] == (w[0], -w[1], w[2])
                                                for nu, w in lookup.items()),
        'degreewise_maxima': maxima == expected,
        'majorant_replay': majorant == replay_majorant,
        'exact_total': total == F(7794564687024429, 20000000000000000),
        'strict_below_two_fifths': total < F(2, 5),
        'strict_below_required_half': total < F(1, 2),
        'transfer_reserve': F(2, 5)+F(1, 20) == F(9, 20) < F(1, 2),
    }
    failures = [name for name, value in checks.items() if not value]
    certificate = {
        'description': 'Full real-observer normalized-row sufficient budget, exact finite algebra',
        'qualification': 'L634 (20) supplies the uniform infinite-row majorant; L629 (1) supplies the qualified relative transfer. Neither is independently audited by this calculation. No pointwise Xi sign or RH claim.',
        'rows': rows, 'full_polynomial_replay': replay,
        'degreewise_maxima': list(map(str, maxima)),
        'maximizers': [list(nu) if nu is not None else None for nu in maximizers],
        'majorant_coefficients': list(map(str, majorant)),
        'contraction': {'theta_upper_bound': '1/100', 'degree_costs': list(map(str, costs)),
                        'total_exact': str(total), 'total_decimal_preview': float(total),
                        'eventual_arithmetic_bound': '2/5', 'transfer_allowance': '1/20',
                        'eventual_full_bound': '9/20', 'required_bound': '1/2',
                        'arithmetic_slack': str(F(2, 5)-total)},
        'checks': checks, 'failures': failures,
    }
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f'Observer orbits: {len(rows)}; complete polynomial divisions: {len(replay)}')
    print(f'Actual sufficient limsup cost: {total} = {float(total):.17g}')
    print('Eventual arithmetic bound: 2/5; full bound with transfer: 9/20; required: 1/2')
    print(f'Failures: {failures}')
    print(f'Certificate: {OUT.relative_to(OUT.parents[2])}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
