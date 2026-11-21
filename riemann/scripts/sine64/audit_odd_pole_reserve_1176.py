"""Independent exact replay of all finite C750p certificate arithmetic.

Analytic compression, coefficient and infinite-tail arguments are audited
in the canonical C750p proof; arithmetic checks alone do not prove them.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parent
source = root / 'odd-pole-reserve-1174.json'
before = source.read_bytes()
data = json.loads(before)
checks = {}
details = {}

def check(name, condition):
    checks[name] = bool(condition)

def exact_list(name, recorded, expected):
    check(name + '_length', len(recorded) == len(expected))
    rows = []
    for j, value in enumerate(expected):
        saved = recorded[j] if j < len(recorded) else None
        ok = saved is not None and F(saved) == value
        check(f'{name}_{j}', ok)
        rows.append({'index': j, 'recorded': saved,
                     'expected': str(value), 'passed': ok})
    details[name] = rows

# Independent recurrence rather than the generator's factorial expression.
exp_terms = [F(1)]
for j in range(1, 9):
    exp_terms.append(exp_terms[-1] * 14 / (3*j))
exact_list('exp_terms', data['exp']['terms'], exp_terms)
exp_sum = sum(exp_terms, F(0))
check('exp_metadata', data['exp']['argument'] == '14/3'
      and data['exp']['degree'] == 8)
check('exp_sum', F(data['exp']['lower_sum']) == exp_sum == F(29874809, 295245))
check('exp_requirement', F(data['exp']['required_lower']) == 101)
check('exp_comparison', exp_sum - 101 == F(55064, 295245) > 0)

atan_terms = [F(1, 2*j+1) if j % 2 == 0 else -F(1, 2*j+1)
              for j in range(64)]
exact_list('atan_terms', data['pi']['terms'], atan_terms)
# Positive consecutive pairs offer an independent sum expression.
pi_sum = sum((F(8, (4*j+1)*(4*j+3)) for j in range(32)), F(0))
check('pi_sum', F(data['pi']['strict_lower']) == pi_sum == 4*sum(atan_terms, F(0)))
check('pi_requirement', F(data['pi']['required_lower']) == F(25, 8))
check('pi_comparison', pi_sum > F(25, 8))
check('pi_next_term', F(data['pi']['error_upper']) == F(4, 129))
check('sqrt_comparison', 10*10 < 101)
check('sinh_upper_algebra', (F(102, 10)-2)/4 == F(41, 20))
check('parameter_bounds', data['parameter_bounds'] == {
    'b_strict_upper': '7/3',
    'sinh_b_over_2_squared_strict_upper': '41/20'})
tail = data['complete_tail']
check('tail_indices', tail['first_k'] == 33 and tail['last_removed_k'] == 32)
check('tail_bound', F(tail['strict_upper']) == F(1, 32))
# Exact algebraic output of the analytically justified coarse bounds.
norm = (F(7, 3)*F(41, 20)) / (4*F(25, 8)**2)
margin = F(1, 8)-norm
check('norm_all_fields', {k: F(v) for k, v in data['norm'].items()} == {
    'lower': F(0), 'strict_upper': norm,
    'required_strict_upper': F(1, 8), 'strict_margin': margin})
check('final_constant', norm == F(1148, 9375))
check('final_margin', margin == F(191, 75000) > 0)
expected_checks = {
    'positive_exp_sum_exceeds_101': exp_sum > 101,
    'atan_lower_exceeds_25_over_8': pi_sum > F(25, 8),
    'sqrt101_exceeds_10': 101 > 100,
    'sinh_square_algebra': (F(102, 10)-2)/4 == F(41, 20),
    'strict_norm_upper_below_threshold': norm < F(1, 8)}
check('original_checks_complete', data['checks'] == expected_checks)
check('original_failures_complete', data['failures'] == [
    key for key, value in expected_checks.items() if not value])

# Run the saved generator and verify byte-for-byte reproducibility.
replay = subprocess.run([sys.executable, str(root / 'odd_pole_reserve_1174.py')],
                        capture_output=True, text=True)
check('generator_exit', replay.returncode == 0)
check('generator_identical', source.read_bytes() == before)
failures = [name for name, value in checks.items() if not value]
output = root / 'odd-pole-audit-1176.json'
report = {
    'source': str(source.relative_to(root.parent.parent)),
    'source_sha256': hashlib.sha256(before).hexdigest(),
    'term_evidence': details,
    'exact_comparisons': {'exp_excess': str(exp_sum-101),
        'pi_lower_excess': str(pi_sum-F(25, 8)),
        'norm_upper': str(norm), 'required': '1/8', 'margin': str(margin)},
    'checks': checks, 'failures': failures,
    'generator_stdout': replay.stdout, 'generator_stderr': replay.stderr,
    'scope': 'Finite exact arithmetic replay; analytic audit is in C750p.'}
output.write_text(json.dumps(report, indent=2)+'\n')
print('C750p independent arithmetic audit:', 'PASS' if not failures else 'FAIL')
print('Checks:', len(checks), '; failures:', failures)
print('Actual strict upper:', norm, '; required:', F(1, 8), '; margin:', margin)
print('Complete-tail start: k=33; analytic infinite-tail proof audited in C750p')
print('Full certificate:', output)
if failures:
    raise SystemExit(1)
