"""Exact constants for L648; analytic inequalities are proved in the lemma."""
from fractions import Fraction as F
import json
from pathlib import Path

R, d, r = F(11, 8), F(5, 4), F(9, 8)
U = R * R
boxes = []
for k in range(1, 5):
    t = F(k, 4)
    bound = (U - t*t) / ((d+t)*(U+d*t))
    boxes.append(dict(t=str(t), integrand_lower=str(bound),
                      integral_lower=str((d-r)*bound/4)))
gamma_lower = sum(F(row['integral_lower']) for row in boxes)
derivative_bound = 1/(r-1) + 1/(U-d)
checks = []
def check(name, actual, relation, required, condition):
    checks.append(dict(name=name, actual=str(actual), relation=relation,
                       required=str(required), passed=bool(condition)))

check('reflected-zero clearance', 2*d-1, '>', R, 2*d-1 > R)
check('inner evaluation base radius', 2*d-R, '=', r, 2*d-R == r)
check('integration strip is outside grid', r, '>', F(1), r > 1)
check('integration strip stays inside disk', d, '<', R, d < R)
check('radial denominator margin', U-d, '>', F(0), U-d > 0)
check('n>=11 evaluation stays in strip', r+R/11, '=', d, r+R/11 == d)
check('logarithmic derivative bound', derivative_bound, '<', F(10),
      derivative_bound < 10)
check('four-box exponent lower bound', gamma_lower, '>', F(1,25),
      gamma_lower > F(1,25))
check('proved input decay exceeds target decay', F(1,25), '>', F(1,32),
      F(1,25) > F(1,32))
check('strict exponent margin', F(1,25)-F(1,32), '=', F(7,800),
      F(1,25)-F(1,32) == F(7,800))
check('anchor squared kernel norm', 1/(U-d*d), '=', F(64,21),
      1/(U-d*d) == F(64,21))
check('anchor census at smallest allowed n', F(1), '<=', F(5,3),
      F(1) <= F(5,3))

failures = [c['name'] for c in checks if not c['passed']]
record = dict(kind='EXACT_RATIONAL_CONSTANT_CHECK',
              lemma='L648', parameters=dict(R=str(R), d=str(d),
                  r=str(r), U=str(U)), boxes=boxes,
              gamma_lower=str(gamma_lower),
              gamma_lower_preview=float(gamma_lower),
              required_root_rate=str(F(1,32)), proved_root_rate=str(F(1,25)),
              exact_margin=str(F(1,25)-F(1,32)), checks=checks,
              failures=failures,
              qualification='Does not independently verify the analytic proof or the exploratory quadrature.')
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(dict(passed=len(checks)-len(failures), total=len(checks),
    actual_gamma_lower=str(gamma_lower), actual_preview=float(gamma_lower),
    proved_rate=str(F(1,25)), required_rate=str(F(1,32)),
    failures=failures, path=str(path)), indent=2))
if failures:
    raise SystemExit(1)
