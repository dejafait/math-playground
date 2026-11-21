"""Replay all C681c scalar evidence and independently check every sum term.

Analytic saddle and norm arguments remain in C681c; these checks certify
only the finite scalar evidence. The original certificate is preserved.
"""
from fractions import Fraction as Q
from pathlib import Path
import contextlib
import hashlib
import io
import json

HERE = Path(__file__).resolve().parent
generator = HERE / 'positive-blend-saddle-certificate.py'
original_path = HERE / 'positive-blend-saddle-certificate.json'
replay_path = HERE / 'positive-blend-saddle-audit-replay.json'
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
code = generator.read_text()
old = "output = HERE / 'positive-blend-saddle-certificate.json'"
new = "output = HERE / 'positive-blend-saddle-audit-replay.json'"
assert code.count(old) == 1
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(code.replace(old, new), str(generator), 'exec'),
         {'__file__': str(generator), '__name__': '__main__'})
replay = json.loads(replay_path.read_text())
checks, failures, sum_rows, scalar_rows = [], [], [], []


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})
    if not passed:
        failures.append(name)


check('entire_original_certificate_matches_replay', original == replay)
check('original_bytes_preserved', original_path.read_bytes() == original_bytes)
check('22_scalar_rows_and_four_integral_rows',
      len(original['checks']) == 22 and len(original['riemann_sums']) == 4)
check('original_and_replay_no_failures',
      original['passed'] and replay['passed']
      and original['failures'] == replay['failures'] == [])

for row in original['checks']:
    lo, hi = map(Q, row['actual'])
    lower = None if row['required_lower'] is None else Q(row['required_lower'])
    upper = None if row['required_upper'] is None else Q(row['required_upper'])
    passed = (lo <= hi and (lower is None or lo > lower)
              and (upper is None or hi < upper))
    check('scalar_' + row['name'], passed and row['passed'] and row['strict'])
    scalar_rows.append(dict(name=row['name'], actual=[str(lo), str(hi)],
                            required_lower=row['required_lower'],
                            required_upper=row['required_upper'], passed=passed))

expected_specs = [
    ('broad_denominator_integral', Q(11, 8), 'denominator'),
    ('broad_numerator_integral', Q(11, 8), 'numerator'),
    ('right_denominator_integral', Q(6, 5), 'denominator'),
    ('right_numerator_integral', Q(5, 4), 'numerator'),
]
for row, (name, A, kind) in zip(original['riemann_sums'], expected_specs):
    check(name + '_specification',
          (row['name'], Q(row['A']), row['kind'], row['partition_count'], row['scale'])
          == (name, A, kind, 256, 10**15))
    vals = []
    for j in range(257):
        t = Q(j, 256)
        vals.append(1 / ((A-t)**2+Q(1, 4)) if kind == 'denominator'
                    else (t / (Q(121, 64)-A*t))**2)
    lower_terms, upper_terms = [], []
    for lo_value, hi_value in zip(vals[:-1], vals[1:]):
        scaled_lo, scaled_hi = lo_value * 10**15 / 256, hi_value * 10**15 / 256
        lo_int, _ = divmod(scaled_lo.numerator, scaled_lo.denominator)
        hi_int, rem = divmod(scaled_hi.numerator, scaled_hi.denominator)
        lower_terms.append(lo_int)
        upper_terms.append(hi_int + (rem != 0))
    check(name + '_all_512_outward_terms',
          lower_terms == row['lower_term_numerators']
          and upper_terms == row['upper_term_numerators'])
    bounds = [str(Q(sum(lower_terms), 10**15)), str(Q(sum(upper_terms), 10**15))]
    check(name + '_complete_sum', bounds == row['integral_bounds'])
    check(name + '_grid_monotonicity', all(a < b for a, b in zip(vals, vals[1:])))
    sum_rows.append(dict(name=name, integral_bounds=bounds,
                         lower_term_numerators=lower_terms,
                         upper_term_numerators=upper_terms))

barrier, eventual, required = Q(121, 13000), Q(19, 2000), Q(1, 100)
check('strict_rate_gaps', barrier < eventual < required)
result = dict(scope='Complete scalar replay and all 2048 outward sum contributions; '
                    'no numerical certification of the analytic saddle limit',
              original_sha256=hashlib.sha256(original_bytes).hexdigest(),
              generator_sha256=hashlib.sha256(generator.read_bytes()).hexdigest(),
              replay_path=replay_path.name, checks=checks,
              scalar_checks=scalar_rows, riemann_sums=sum_rows,
              rates=dict(barrier=str(barrier), eventual=str(eventual), required=str(required),
                         polynomial_absorption_gap=str(eventual-barrier)),
              failures=failures, passed=not failures)
output = HERE / 'positive-blend-saddle-audit.json'
output.write_text(json.dumps(result, indent=2)+'\n')
print(f'Audit checks: {len(checks)}; scalar rows: {len(scalar_rows)}; '
      f'outward contributions: 2048; failures: {len(failures)}')
for row in scalar_rows:
    print(row['name'], row['actual'], 'required:', row['required_lower'],
          '< value <', row['required_upper'], 'PASS' if row['passed'] else 'FAIL')
print('Rate barrier:', barrier, '; eventual lower-bound rate:', eventual,
      '; target upper-bound rate >', required)
print('Failures:', failures)
print('Audit:', output)
print('Replay:', replay_path)
if failures:
    raise SystemExit(1)
