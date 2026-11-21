#!/usr/bin/env python3
"""Independent finite audit of C998u's chosen majorant rule, not its energy."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'remote-image-measure-audit-726.json'
SOURCE = BASE / 'remote-image-measure-preflight-724.json'
SCRIPT = BASE / 'remote-image-measure-preflight-724.py'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
PIN = '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a'
paths = [SOURCE, SCRIPT, WITNESS]
before = {p.name: sha256(p.read_bytes()).hexdigest() for p in paths}
old = json.loads(SOURCE.read_text())
checks = []


def check(name, condition):
    checks.append({'name': name, 'passed': bool(condition)})


# Work with the integer inequality 4*N-3 >= 2*A*denominator,
# independently of the original Fraction/ceiling cutoff routine.
M, B = 1 << 20, 1 << 23
A, cap = M*B, 100_000_000
check('witness pin', before[WITNESS.name] == PIN)
check('original witness fields', old['witness']['actual_sha256'] == PIN
      and old['witness']['expected_sha256'] == PIN)
check('A and B', old['bounds']['A'] == A and old['bounds']['B'] == B)
check('translation majorant beats uniform-TV majorant', 2*A < B*B)
cases = {}
for label, denominator, expected_n in [
        ('reserved', 10_000_000, 43_980_465_111_040_000_001),
        ('whole', 1_000_000, 4_398_046_511_104_000_001)]:
    numerator = 2*A*denominator
    q, remainder = divmod(numerator, 4)
    check(f'{label}: numerator divisible by four', remainder == 0)
    n = q+1
    margin = 4*n-3-numerator
    previous_margin = 4*(n-1)-3-numerator
    check(f'{label}: integer minimality margins', margin == 1 and previous_margin == -3)
    check(f'{label}: printed cutoff', n == expected_n)
    bound = Fraction(2*A, 4*n-3)
    previous = Fraction(2*A, 4*(n-1)-3)
    budget = Fraction(1, denominator)
    check(f'{label}: exact budget bracket', bound <= budget < previous)
    check(f'{label}: fixed-loop work exceeds total cap', n > cap)
    cases[label] = {'N': n, 'budget': str(budget), 'tail_majorant': str(bound),
                    'previous_majorant': str(previous), 'integer_margin': margin,
                    'previous_integer_margin': previous_margin,
                    'loop_accumulations': n, 'required_total_cap': cap}

r, w = cases['reserved'], cases['whole']
expected_cutoff = {
    'N': r['N'], 'tail_majorant': r['tail_majorant'],
    'previous_tail_majorant': r['previous_majorant'],
    'whole_budget_N': w['N'], 'whole_budget_tail_majorant': w['tail_majorant'],
    'whole_budget_previous_tail_majorant': w['previous_majorant']}
expected_work = {
    'required_total_cap': cap, 'selected_loop_accumulations_only': r['N'],
    'whole_budget_loop_accumulations_only': w['N'],
    'selected_cap_ratio': str(Fraction(r['N'], cap)),
    'all_other_costs_assigned_favorable_zero': True, 'cap_met': False}
check('all original cutoff fields independently match', old['cutoff'] == expected_cutoff)
check('all original work fields independently match', old['work'] == expected_work)
check('tail and remaining budgets add to total',
      Fraction(old['bounds']['reserved_tail_budget']) == Fraction(1, 10_000_000)
      and Fraction(old['bounds']['remaining_error_allowance']) == Fraction(9, 10_000_000)
      and Fraction(old['bounds']['total_error_goal']) == Fraction(1, 1_000_000))
check('original eleven checks report success', len(old['checks']) == 11
      and all(c['passed'] for c in old['checks']) and old['failed_checks'] == [])
check('original certificate disclaims proof and scalar evaluation',
      old['analytic_proof_verified_by_script'] is False
      and old['scalar_sweep_or_gram_evaluated'] is False)
check('original artifacts unchanged',
      before == {p.name: sha256(p.read_bytes()).hexdigest() for p in paths})
certificate = {
    'scope': 'Independent rational/hash audit of C998u Section3; analytic audit is canonical Section4.',
    'source_hashes': before, 'cases': cases, 'checks': checks,
    'failed_checks': [c['name'] for c in checks if not c['passed']],
    'unpaid': old['unpaid'], 'target_failures': old['target_failures'],
    'analytic_proof_verified_by_script': False,
    'scalar_sweep_or_gram_evaluated': False,
    'actual_small_N_error_lower_bound': False,
    'general_complexity_lower_bound': False}
OUT.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Independent finite checks: {sum(c["passed"] for c in checks)}/{len(checks)}; failures: {certificate["failed_checks"]}')
for label, row in cases.items():
    print(f'{label}: tail bound {row["tail_majorant"]} <= {row["budget"]}; N={row["N"]}; allowed total work={cap}')
print('Selected prescription STOP; other errors unpaid; no scalar, sweep or Gram evaluated.')
print(f'Certificate: {OUT.relative_to(BASE.parent.parent)}')
if certificate['failed_checks']:
    raise SystemExit(1)
