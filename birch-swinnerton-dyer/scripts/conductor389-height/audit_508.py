#!/usr/bin/env python3
"""Replay all step-506 witnesses, then check fixed-input audit anchors.

No producer import or numerical height library. The existing sparse checker
verifies all reduction/group/series identities; this audit additionally binds
its evidence to the exact requested inputs, precision metadata and saved data.
Infinite bounds are proved in L121, never inferred from this finite replay.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import subprocess
import sys

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'step-508'
OUT.mkdir(exist_ok=True)
CP = ROOT / 'step-506/certificate.json'
VP = ROOT / 'step-506/verification.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


before = {str(p.relative_to(ROOT)): digest(p) for p in (CP, VP)}
replay = subprocess.run([sys.executable, str(ROOT / 'check_certificate.py')],
                        capture_output=True, text=True)
(OUT / 'finite-replay.txt').write_text(replay.stdout + replay.stderr)
C = json.loads(CP.read_text())
V = json.loads(VP.read_text())
checks = {}
failures = []


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        failures.append(name)


def val(x):
    x = F(x)
    if not x:
        return 10**9
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % 5 == 0:
        n //= 5
        v += 1
    while d % 5 == 0:
        d //= 5
        v -= 1
    return v


def residue(x, n):
    x = F(x)
    return x.numerator * pow(x.denominator, -1, 5**n) % 5**n


check('complete_sparse_replay', replay.returncode == 0 and
      V['check_count'] == len(V['checks']) and all(V['checks'].values()) and
      not V['failures'])
check('original_evidence_preserved', all(digest(ROOT / p) == h
      for p, h in before.items()))
check('exact_curve_prime_precision_multipliers',
      C['curve'] == [0, 1, 1, -2, 0] and C['p'] == 5 and
      C['output_absolute_exponent'] == 6 and
      (C['n1'], C['n2'], C['n']) == (9, 1, 9))
expected = {'P': ['0', '0'], 'Q': ['1', '0'], 'P+Q': ['-2', '-1']}
check('exact_point_labels', C['points'] == expected and
      set(C['height_details']) == set(expected))
FR = C['frobenius']
pairs = [(t['j'], t['basis_index']) for t in FR['terms']]
check('every_frobenius_term_once', len(pairs) == 16 and
      set(pairs) == {(j, i) for j in range(8) for i in range(2)})
check('actual_delta_degree', len(FR['delta']) == 14 and
      F(FR['delta'][-1]) != 0)
check('polynomial_horizontal_primitives', all(s['degree'] >= 2
      for term in FR['terms'] for s in term['horizontal']))
fm = FR['F_mod_5^7']
fp = [[1, 0], [0, 1]]
for _ in range(6):
    fp = [[sum(fp[r][k] * fm[k][c] for k in range(2)) % 5**7
           for c in range(2)] for r in range(2)]
check('saved_frobenius_power', fp == FR['F_power_6_mod_5^7'])
check('first_column_and_unit_denominator',
      fm[0][0] % 5 == fm[1][0] % 5 == 0 and fp[1][1] % 5 != 0)
check('E2_value', FR['E2_mod_5^6'] == V['E2_mod_5^6'] == 10008 and
      residue(F(-12 * fp[0][1], fp[1][1]), 6) == 10008)
check('saved_frobenius_tail_contract', FR['tail']['first_omitted_j'] == 8 and
      FR['tail']['absolute_F_exponent'] == 7)

S = C['sigma']
check('formal_series_lengths_and_initial_terms',
      len(S['w']) == 12 and list(map(F, S['w'][:4])) == [0, 0, 0, 1] and
      len(S['t_squared_x']) == 9 and F(S['t_squared_x'][0]) == 1 and
      len(S['omega']) == 8 and F(S['omega'][0]) == 1)
check('sigma_constant_and_h_centers', S['c'] == ['-2501/3', 6] and
      [F(a[0]) for a in S['h']] ==
      list(map(F, ['0', '2504/3', '3/2', '9983/9', '12535/6'])))
check('sigma_evidence_lengths', len(S['theta_balls']) ==
      len(S['sigma_profile']) == len(V['symbolic_sigma']) == 6)
for k in range(6):
    center, exponent = S['theta_balls'][k]
    row, sym = S['sigma_profile'][k], V['symbolic_sigma'][k]
    coeff = {int(j): F(x) for j, x in sym['polynomial_in_z'].items()}
    nonconstant = [x for j, x in coeff.items() if j > 0 and x]
    check(f'sigma_profile_{k+1}', row['sigma_degree'] == sym['degree'] == k+1 and
          F(row['center']) == F(center) == coeff.get(0, F(0)) and
          row['absolute_exponent'] == exponent and
          row['required'] == sym['required'] == 6-k and
          (not nonconstant or min(map(val, nonconstant)) >= exponent) and
          (exponent != 10**9 or not nonconstant) and exponent >= 6-k)
check('sigma_integral_tail_contract', S['sigma_tail_degree'] == 7 and
      S['imported_sigma_integrality'] is True)

point_evidence = {}
for label, D in C['height_details'].items():
    base = tuple(map(F, D['point']))
    previous = None
    for k, entry in enumerate(D['multiplication_chain'], 1):
        branch_valid = previous is None or previous[0] != base[0] or (
            previous == base and 2 * base[1] + 1 != 0)
        check(f'group_law_branch_{label}_{k}', branch_valid)
        previous = tuple(map(F, entry['point']))
    alpha, beta, t = map(F, (D['alpha'], D['beta'], D['t']))
    check('exact_formal_valuation_' + label,
          val(D['d']) == val(t) == D['v_t'] == 1 and
          val(alpha) == val(beta) == 0)
    tv = sum(F(a[0]) * t**k for k, a in enumerate(S['theta_balls']))
    unit = (-alpha / beta) * tv
    check('saved_theta_ball_' + label,
          F(D['theta_value'][0]) == tv and D['theta_value'][1] == 6)
    check('saved_unit_ball_' + label,
          F(D['sigma_over_d_unit'][0]) == unit and
          D['sigma_over_d_unit'][1] == 6 and val(unit) == 0)
    z = unit**4 - 1
    exact_log = sum(F((-1)**(k+1), k) * z**k for k in range(1, 8)) / 4
    height = residue(2 * exact_log / 81, 6)
    check('exact_saved_log_and_final_precision_' + label,
          F(D['log_power_minus_one']) == z and F(D['log_partial']) == exact_log and
          D['log_tail_first_k'] == 8 and D['log_tail_exponent_lower_bound'] == 6 and
          val(z) >= 1 and D['absolute_exponent'] == 6 and
          D['q_H_center_mod_5^6'] == V['points'][label]['q_H_mod_5^6'] == height)
    point_evidence[label] = {'v_t': val(t), 'unit_residue': residue(unit, 6),
                             'height_center': height, 'absolute_exponent': 6}
L = C['L119']
check('full_L119_metadata', L['height_centers'] ==
      {label: D['height_center'] for label, D in point_evidence.items()} and
      (L['b'], L['t'], L['k'], L['a'], L['N'], L['B0']) == (2, 0, 2, 0, 6, 6) and
      F(L['D0']) == -22126600 and L['v_D0'] == 2 and L['strict_test_pass'] is True)
report = {
    'status': 'FINITE_AUDIT_PASS' if not failures else 'FINITE_AUDIT_FAIL',
    'checks': checks, 'failures': failures, 'sparse_replay_check_count': V['check_count'],
    'points': point_evidence,
    'actual_determinant_valuation': val(L['D0']), 'required_strict_bound': 6,
    'original_evidence_hashes': before,
    'script_hashes': {n: digest(ROOT / n) for n in
                      ('produce.py', 'check_certificate.py', 'audit_508.py')},
    'limitations': ['Infinite bounds and cited theorem applicability are checked in L121 prose.',
                    'Published L120 arithmetic executions remain unreplayed.']}
path = OUT / 'audit.json'
path.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: report[k] for k in ('status', 'sparse_replay_check_count',
      'actual_determinant_valuation', 'required_strict_bound', 'failures')}, indent=2))
print('Full audit certificate: ' + str(path))
sys.exit(bool(failures))
