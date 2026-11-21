"""Exact scalar and unit checks for C919g; no component certificate replay."""
from fractions import Fraction as Q
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/h2-head/assembly_audit_2173.json'
B = Q(9038116652331572962135737621217329139050385873,
      13463243595254160685006848000000000000)
eps = Q(133662268399, 267363281250000000000)
head_threshold = Q(1, 700000000)
tail_threshold = Q(1, 2000000000)
reserve = Q(13, 14000000000)
mu = 1 / B - eps
checks = []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})


check('B_positive', B > 0)
check('inverse_B_strictly_above_head_threshold', 1 / B > head_threshold)
check('epsilon_nonnegative', eps >= 0)
check('epsilon_strictly_below_tail_threshold', eps < tail_threshold)
check('threshold_difference_is_claimed_reserve',
      head_threshold - tail_threshold == reserve)
check('reserve_positive', reserve > 0)
check('mu_strictly_above_reserve', mu > reserve)
check('strict_margin_decomposition', mu - reserve ==
      (1 / B - head_threshold) + (tail_threshold - eps))
boxes = [(Q(14), Q(29, 2)), (Q(41, 2), Q(43, 2)),
         (Q(49, 2), Q(51, 2))]
check('positive_nonempty_boxes_inside_rectangle',
      all(0 < a < b < 100 for a, b in boxes))
check('distinct_positive_opposite_classes',
      boxes[0][1] < boxes[1][0] and boxes[1][1] < boxes[2][0])
d = [1, 200, 40000]
check('D_real_invertible', all(isinstance(x, int) and x != 0 for x in d))
check('weights_match_H2_indices',
      all(2 * (i + 1) + 2 * (j + 1) == 2 * (i + j + 2)
          for i in range(3) for j in range(3)))

scalars = {
    'B': B, 'inverse_B': 1 / B, 'epsilon_star': eps,
    'head_required_strict_lower': head_threshold,
    'tail_required_strict_upper': tail_threshold,
    'head_surplus': 1 / B - head_threshold,
    'tail_surplus': tail_threshold - eps,
    'mu': mu, 'required_strict_reserve': reserve,
    'surplus_over_reserve': mu - reserve,
}
failures = [item['name'] for item in checks if not item['passed']]
payload = {
    'step': 2173, 'scope': 'C919g exact assembly scalars and fixed units only',
    'scalars': {key: str(value) for key, value in scalars.items()},
    'D_inverse_squared': [str(Q(1, x*x)) for x in d],
    'boxes': [[str(a), str(b)] for a, b in boxes],
    'checks': checks, 'failures': failures,
    'qualification': 'No verification or replay of component analytic proofs, '
                     'numerical certificates, or arithmetic backends.',
}
OUT.write_text(json.dumps(payload, indent=2) + '\n')
print(f'{len(checks)} exact assembly checks; failures={failures}')
print(f'actual mu={mu}; required mu>{reserve}')
print(f'actual epsilon={eps}; required epsilon<{tail_threshold}')
print(f'certificate: {OUT.relative_to(ROOT)}')
raise SystemExit(1 if failures else 0)
