"""Exact rational replay of L559 audit1275; no numerical theta sampling."""
from fractions import Fraction as F
import json
from pathlib import Path


def deriv_exp_polynomial(p):
    # d/du [exp(u/2) p(t) exp(-t)], where dt/du = 2t.
    out = [F(0)] * (len(p) + 1)
    for j, coefficient in enumerate(p):
        out[j] += (F(1, 2) + 2*j) * coefficient
        out[j + 1] -= 2 * coefficient
    return out


p1 = deriv_exp_polynomial([F(0), F(-3), F(2)])
p2 = deriv_exp_polynomial(p1)
q = F(22, 7)
checks = []


def record(name, actual, required, relation, passed):
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation=relation, passed=bool(passed)))


expected = [F(0), F(-75, 4), F(330, 4), F(-224, 4), F(32, 4)]
record('second derivative coefficients, ascending powers', p2, expected,
       'equals', p2 == expected)
value = 96*q*q - 448*q + 330
record('P_prime_at_22_over_7', value, F(-6358, 49), 'equals', value == F(-6358, 49))
record('P_prime_negative', value, 0, 'less_than', value < 0)
record('pi_fourth_rational_majorant', q**4, 100, 'less_than', q**4 < 100)
record('e_cubed_rational_minorant', F(8, 3)**3, 18, 'greater_than', F(8, 3)**3 > 18)
record('ratio_polynomial_factor', F(3, 2)**8, 26, 'less_than', F(3, 2)**8 < 26)
record('tail_ratio_majorant', F(26, 18**5), F(1, 100), 'less_than', F(26, 18**5) < F(1, 100))
tail = F(8*100*256*100, 18**4*99)
record('tail_upper_bound', tail, 2, 'less_than', tail < 2)
record('coarse_curvature_upper_bound', -F(79, 36)+2, -F(7, 36),
       'equals', -F(79, 36)+2 == -F(7, 36))
failures = [item['name'] for item in checks if not item['passed']]
result = dict(scope='Finite rational arithmetic only; see L559 for analytic proof.',
              checks=checks, failures=failures, passed=not failures)
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(result, indent=2) + '\n')
print(f"PASS={not failures}; {len(checks)} exact checks; failures={failures}")
print(f"Tail majorant={tail} < required 2; curvature upper bound=-7/36 < required 0")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
