#!/usr/bin/env python3
"""Exact diagonal certificate for L969's one fixed profile.

Reuse L967's finite polynomial utilities and complete tensor coefficients.
This is a construction self-check, not an independent proof audit.
Convergence and the actual positive normalization are proved in L969.
"""

from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
source = Path(__file__).with_name('tensor-boundary-check-168.py')
spec = importlib.util.spec_from_file_location('tensor168', source)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def check(n):
    h, delta, _, d, expected_d = base.coefficients(n)
    q = F(8 * 3**n)
    # The third exponent denotes gamma, not L967's old kappa.
    z = base.mul(base.ep(kappa=1), base.add(base.H(q, 0), base.H(q, 1)))
    b = [z] + [base.scale(base.H(F(1, 2), r - 1), 2*r)
               for r in range(1, n + 1)]
    c = [base.add(z, base.scale(base.H(q, 0), 2*delta)),
         base.add(base.scale(base.H(q, 0), 2),
                  base.scale(base.H(q, 1), 2*delta))]
    total, theta_part, distant_part = {}, {}, {}
    terms = []
    for coefficient, factors in base.stated_tensor(n, d):
        # On the diagonal all (n+1)! permutations coincide, so their
        # normalized average is exactly this product, with no factorial.
        value = base.ep(coefficient=coefficient)
        for tag, r in factors:
            value = base.mul(value, b[r] if tag == 'b' else c[r])
        is_distant = factors[-1] == ('h', 1)
        if is_distant:
            distant_part = base.add(distant_part, value)
        else:
            theta_part = base.add(theta_part, value)
        total = base.add(total, value)
        terms.append({
            'coefficient': str(coefficient),
            'factors': [[tag, r] for tag, r in factors],
            'is_distant': is_distant,
            'maximum_exponential_rate': str(max(k[0] for k in value)),
            'complete_diagonal_polynomial': base.serialize(value),
        })

    rate = (n + 1)*q
    required_coefficient = -d[1]*delta/(2*q*(4*q)**n)
    expected_leading = base.ep(rate, n + 1, n, required_coefficient)
    leading = {k: v for k, v in total.items()
               if k[0] == rate and k[1] == n + 1}
    residual = base.add(leading, base.scale(expected_leading, -1))
    failures = []
    if d != expected_d:
        failures.append('L966 and L967 coefficients disagree')
    if residual:
        failures.append('diagonal limit coefficient mismatch')
    if max(k[0] for k in theta_part) > n*q + F(1, 2):
        failures.append('theta remainder exceeds proved exponential bound')
    if any(k[0] > rate or (k[0] == rate and k[1] > n + 1)
           for k in total):
        failures.append('unaccounted faster diagonal term')
    if required_coefficient >= 0:
        failures.append('limit coefficient is not strictly negative')
    return {
        'n': n, 'h': str(h), 'q': str(q), 'delta': str(delta),
        'd': [str(v) for v in d[1:]],
        'basis': 'coefficient * exp(rate*t) * t^degree * gamma^power',
        'terms': terms,
        'complete_diagonal_polynomial': base.serialize(total),
        'checks': {
            'actual_theta_maximum_rate': str(max(k[0] for k in theta_part)),
            'required_theta_rate_upper_bound': str(n*q + F(1, 2)),
            'dominant_rate': str(rate), 'dominant_degree': n + 1,
            'limit_coefficient_without_gamma_power': str(required_coefficient),
            'gamma_power': n,
            'complete_leading_term': base.serialize(leading),
            'exact_leading_residual': base.serialize(residual),
            'failures': failures,
        },
    }


def main():
    cases = [check(n) for n in (2, 3)]
    failures = [f"n={case['n']}: {failure}" for case in cases
                for failure in case['checks']['failures']]
    summary = {
        'actual': 'strictly negative diagonal limit at both orders for every gamma>0',
        'required': 'nonnegative kernel throughout the positive orthant',
        'limits_without_gamma_power': [case['checks']['limit_coefficient_without_gamma_power']
                                       for case in cases],
        'theta_rate_bounds': [case['checks']['actual_theta_maximum_rate'] for case in cases],
        'dominant_negative_rates': [case['checks']['dominant_rate'] for case in cases],
        'failures': failures,
        'scope': 'This fixed profile fails; no sign of the integrated numerator is asserted.',
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps({'summary': summary, 'cases': cases}, indent=2) + '\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Full certificate: {output.relative_to(Path.cwd())}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
