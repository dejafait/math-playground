"""Exact rational replay only; analytic hypotheses/proof are in L751."""
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

output = Path(__file__).with_name('exact-bounds-320.json')
integral_u2 = factorial(2) * 2**3
integral_u1 = factorial(1) * 2**2
coefficient = F(2 * integral_u2 + integral_u1, 2)
continuous_upper = F(32, 9) + F(40, 81)
residual_upper = -F(9, 2) + continuous_upper
checks = {
    'gamma_integrals': integral_u2 == 16 and integral_u1 == 4,
    'quadratic_coefficient': coefficient == 18,
    'window_prime_cutoff': 3**9 == 19683,
    'midpoint_prime_cutoff_squared': 81**2 * 3 == 3**9,
    'continuous_increment': continuous_upper == F(328, 81),
    'residual_arithmetic': residual_upper == -F(73, 162),
    'strict_negative_threshold': residual_upper < 0,
}
certificate = {
    'scope': 'Exact arithmetic replay, not verification of analytic hypotheses',
    'canonical_proof': 'lemmas/L751-fixed-sine-complete-neutral-supersolution-obstruction.md',
    'analytic_requirements': [
        'L751 equations (11)-(15), including full zero-extension residual',
        'all surviving von Mangoldt weights/cosines nonnegative',
        'pi in (3,4), e<3, gamma>=0, log2>2/3',
    ],
    'values': {
        'integral_u2_exp_minus_u_over_2': integral_u2,
        'integral_u_exp_minus_u_over_2': integral_u1,
        'quadratic_coefficient': str(coefficient),
        'continuous_increment_strict_upper': str(continuous_upper),
        'scalar_strict_upper': '-9/2',
        'full_residual_strict_upper': str(residual_upper),
        'required_pointwise_lower_threshold': '0',
    },
    'checks': checks,
    'failures': [name for name, passed in checks.items() if not passed],
}
output.write_text(json.dumps(certificate, indent=2) + '\n')
print(f"Exact arithmetic: {sum(checks.values())}/{len(checks)} pass; "
      f"residual upper {residual_upper}; required lower threshold 0; "
      f"failures {certificate['failures']}; certificate {output}")
raise SystemExit(bool(certificate['failures']))
