"""Exact rational subchecks for L906; analytic bounds are proved in L906."""
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path


def delta_polynomial(p):
    """P -> (1/2-2x)P+2xP', coefficients in increasing order."""
    q = [F(0)] * (len(p) + 1)
    for k, c in enumerate(p):
        q[k] += (F(1, 2) + 2 * k) * c
        q[k + 1] -= 2 * c
    return q


p0 = [F(0), F(-3), F(2)]
p1 = delta_polynomial(p0)
p2 = delta_polynomial(p1)
expected = [F(0), F(-75, 4), F(165, 2), F(-56), F(8)]
q_upper = 8 * F(22, 7)**3 - 56 * 9 + F(165, 2) * F(22, 7) - F(75, 4)
exp3_lower = sum((F(3)**k / factorial(k) for k in range(9)), F(0))
ratio = F(3, 2)**8 / 20**5
tail = F(900 * 256, 20**4) / (1 - F(1, 100000))
bounds = {
    'first_term_bracket_upper': [q_upper, F(-15), q_upper < -15],
    'e_upper': [F(8, 3) + F(5, 96), F(11, 4), F(8, 3) + F(5, 96) < F(11, 4)],
    'exp_pi_upper': [F(11, 4)**3 * F(7, 6), F(27), F(11, 4)**3 * F(7, 6) < 27],
    'exp3_lower': [exp3_lower, F(20), exp3_lower > 20],
    'positive_tail_polynomial_factor': [8 + F(165, 2) / 12**2, F(9), 8 + F(165, 2) / 12**2 < 9],
    'pi_fourth_upper': [F(22, 7)**4, F(100), F(22, 7)**4 < 100],
    'series_ratio_upper': [ratio, F(1, 100000), ratio < F(1, 100000)],
    'tail_upper': [tail, F(3, 2), tail < F(3, 2)],
    'delta2_w_upper': [F(-5, 3) + tail, F(-1, 6), F(-5, 3) + tail < F(-1, 6)],
}
failures = [name for name, (_, _, passed) in bounds.items() if not passed]
if p2 != expected:
    failures.append('second_derivative_polynomial')
certificate = {
    'scope': 'Exact rational subchecks only; series, inversion and operator reasoning are in L906.',
    'polynomials': {'P0': list(map(str, p0)), 'P1': list(map(str, p1)), 'P2': list(map(str, p2))},
    'bounds': {name: {'actual': str(a), 'required_threshold': str(b), 'passed': ok}
               for name, (a, b, ok) in bounds.items()},
    'all_passed': not failures,
    'failures': failures,
}
path = Path(__file__).with_name('finite-domain-kernel-143.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
for name, (actual, required, passed) in bounds.items():
    print(f'{name}: actual={actual}; threshold={required}; passed={passed}')
print(f'polynomial_match={p2 == expected}; failures={failures}; certificate={path}')
if failures:
    raise SystemExit(1)
