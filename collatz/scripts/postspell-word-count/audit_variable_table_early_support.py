#!/usr/bin/env python3
"""Independent finite-input audit of L076, not its universal implication.

No construction certifier is imported or executed. All original arithmetic
records are rebuilt, and analytic inputs are enclosed by exact series.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import factorial
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
PAIRS = [
    (8, 40), (15, 72), (28, 134), (52, 249), (98, 467),
    (184, 877), (347, 1650), (653, 3106), (1230, 5849),
    (2317, 11018), (4365, 20756), (8224, 39104), (15494, 73672),
    (29191, 138802), (54998, 261511), (103621, 492705),
    (195229, 928293), (367827, 1748976), (693015, 3295208),
    (1305695, 6208431), (2460032, 11697176), (4634896, 22038409),
    (8732512, 41522114), (16452748, 78230965), (30998279, 32670621),
]
checks = []


def check(name, actual, required, relation='='):
    passed = actual == required if relation == '=' else actual < required
    checks.append(dict(name=name, actual=actual, required=required,
                       relation=relation, passed=passed))


def log_interval(t):
    # Assessed DLMF 4.6.4 positive-real expansion and geometric remainder.
    x = (t-1)/(t+1)
    assert 0 < x <= Q(1, 2)
    terms = [2*x**(2*m+1)/(2*m+1) for m in range(128)]
    lo = sum(terms, Q(0))
    rem = 2*x**257/(257*(1-x*x))
    return dict(argument=t, x=x, terms=terms, remainder=rem,
                lower=lo, upper=lo+rem)


source_path = HERE / 'variable-table-early-support-certificate.json'
source_bytes = source_path.read_bytes()
source = json.loads(source_bytes)
rows = [[i, J, H] for i, (J, H) in enumerate(PAIRS)]
lemma55 = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
published_rows = [list(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', lemma55, re.M)]
check('independent transcription matches L055', rows, published_rows)
check('original table', source['rows'], rows)
r, budget, S = 25, 9250245, 10**12
K = 3*sum(J for J, H in PAIRS)+sum(H for J, H in PAIRS)
N = 4*sum(J for J, H in PAIRS)+sum(H for J, H in PAIRS)+2*r+18*budget
for name, value, expected in [('sum J', sum(J for J, H in PAIRS), 66061058),
                              ('sum H', sum(H for J, H in PAIRS), 199390205),
                              ('K', K, 397573379), ('N', N, 630138897)]:
    check(name, value, expected)
for key, expected in [('budget', budget), ('K', K), ('N', N)]:
    check('original '+key, source[key], expected)

logs = {name: log_interval(t) for name, t in
        [('two', Q(2)), ('three', Q(3)), ('shift', Q(11, 4))]}
EL, EU, TL, TU, VL, VU = (693147180559, 693147180560, 1098612288668,
                          1098612288669, 1011600911678, 1011600911679)
for name, lo, hi in [('two', EL, EU), ('three', TL, TU), ('shift', VL, VU)]:
    check(name+' grid lower', Q(lo, S), logs[name]['lower'], '<')
    check(name+' grid upper', logs[name]['upper'], Q(hi, S), '<')
lambda_lo = N*logs['two']['lower']-K*logs['three']['upper']
lambda_hi = N*logs['two']['upper']-K*logs['three']['lower']
lam, cap, T = Q(10584, 10**14), Q(20*10**9), Q(24)
check('Lambda strict lower', lam, lambda_lo, '<')
check('Lambda strict upper', lambda_hi, Q(10585, 10**14), '<')
ell, u, v = Q(EL, S), Q(TU, S), Q(VU, S)
E = Q(23*(r-1), 4*2**(4*PAIRS[1][0])-23)
residual = lam-E
R = Q(23, 11)/residual+Q(23, 11)
exp_terms = [Q(24**k, factorial(k)) for k in range(41)]
exp_lower = sum(exp_terms, Q(0))
min_H = min(H for J, H in PAIRS[:r-2])
offset_lower = Q(12, 11)*Q(3, 2)**min_H+1
offset_threshold = Q(23, 11)*2**20
constants = dict(lambda_lower=str(lam), E=str(E), residual=str(residual),
                 R=str(R), U=str(cap), T=str(T), ell=str(ell), u=str(u), v=str(v))
check('all original constants', source['constants'], constants)
check('all original exponential terms', source['exponential_terms'], list(map(str, exp_terms)))
check('original offset operands', source['offset'],
      dict(minimum_early_H=min_H, Q_lower=str(offset_lower)))
check('published residual fraction', residual,
      Q(6101253702379434166563, 57646075230342348512500000000000))
check('published root fraction', R,
      Q(1325859730438202850942226985830949, 67113790726173775832193))
check('published exponential fraction', exp_lower,
      Q(202750314819830504045671593478515759301, 7661655986496068058455078125))
check('published offset fraction', offset_lower,
      Q(36472999400827762787, 3023656976384))
check('tail2 threshold below tail20', Q(23, 11)*4, offset_threshold, '<')

# Rebuild every original rational operand, difference, relation and verdict.
reconstructed = []


def original_check(name, actual, required, relation):
    actual, required = Q(actual), Q(required)
    passed = {'<': actual < required, '>': actual > required,
              '=': actual == required}[relation]
    reconstructed.append(dict(name=name, actual=str(actual), required=str(required),
                              relation=relation, difference=str(actual-required), passed=passed))
    check('independent original test: '+name, passed, True)


original_check('positive residual', residual, 0, '>')
original_check('root cap', R, cap, '<')
original_check('positive exponential partial sum', exp_lower, cap, '>')
original_check('smallest early H tail20 offset test', offset_lower, offset_threshold, '>')
original_check('odd count', K, 397573379, '=')
original_check('total count', N, 630138897, '=')
lemma64 = (NOTEBOOK / 'lemmas/L064-single-tail-redistribution-j-guard-classification.md').read_text()
old_margins = [list(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(-\d+)\|$', lemma64, re.M)]
check('complete L064 table length', len(old_margins), 23)
margins, direct_intervals = [], []
for j in range(r-2):
    # Direct finite sums; no dependence on the construction recurrence.
    A = sum(3*J+H for J, H in PAIRS[:j+1])
    D = sum(4*J+H+2 for J, H in PAIRS[:j+1])
    next_J = PAIRS[j+1][0]
    coefficient = D+18+4*next_J
    M = Q(coefficient*EL-24*S-VU-A*TU, S)
    check(f'L064 index pair {j}', old_margins[j][:2], [j, j+1])
    old_upper = old_margins[j][2]
    original_check(f'recipient {j} strict rejection', M, Q(233, 25), '>')
    original_check(f'recipient {j} exact L064 margin match', M, Q(-old_upper, S), '=')
    margins.append(dict(first_recipient=j, next_input=j+1, A=A, D=D,
                        next_J=next_J, margin=str(M), scaled_margin=int(M*S),
                        published_upper=old_upper))
    direct_lower = coefficient*logs['two']['lower']-24-logs['shift']['upper']-A*logs['three']['upper']
    check(f'unrounded rejection {j} stronger than grid', M, direct_lower, '<')
    direct_intervals.append(dict(j=j, A=A, D=D, coefficient=coefficient,
                                 lower=direct_lower, grid_lower=M))
check('all original rational records and verdicts', source['checks'], reconstructed)
check('all original prefix and margin records', source['margins'], margins)
integer_checks = dict(
    r_at_least_three=r >= 3,
    integer_domain=all(J >= 2 and H >= 3 for J, H in PAIRS),
    increasing_J=all(PAIRS[i][0] < PAIRS[i+1][0] for i in range(r-1)),
    budget_positive=budget > 0,
    nonzero_index_floor=all(J >= PAIRS[1][0] for J, H in PAIRS[1:]),
    offset_floor_all_early=all(H >= min_H for J, H in PAIRS[:r-2]),
    all_recipient_indices=[m['first_recipient'] for m in margins] == list(range(r-2)),
    both_boundaries=(margins[0]['first_recipient'], margins[-1]['first_recipient']) == (0, r-3))
check('all original integer checks', source['integer_checks'], integer_checks)
check('integer checks hold', all(integer_checks.values()), True)
minimum = min(Q(m['margin']) for m in margins)
source_summary = dict(rational_checks=52, integer_checks=8, recipients=23,
                      minimum_margin=str(minimum), required_margin='233/25',
                      first_margin=margins[0]['margin'], final_margin=margins[-1]['margin'], failures=[])
check('original summary', source['summary'], source_summary)
check('minimum margin at recipient 4', margins[4]['margin'], str(minimum))
failures = [c['name'] for c in checks if not c['passed']]
summary = dict(checks=len(checks), failures=failures, original_records=52,
               original_integer_checks=8, recipients=23, residual=residual,
               root_cap=R, required_cap=cap, exponential_lower=exp_lower,
               offset_lower=offset_lower, required_offset=offset_threshold,
               minimum_margin=minimum, required_margin=Q(233, 25),
               first_margin=margins[0]['margin'], final_margin=margins[-1]['margin'])
certificate = dict(purpose='L076 finite benchmark audit; universal proof is symbolic',
                   source_sha256=hashlib.sha256(source_bytes).hexdigest(), rows=rows,
                   logarithms=logs, lambda_interval=[lambda_lo, lambda_hi],
                   exponential_terms=exp_terms, constants=constants,
                   reconstructed_original_checks=reconstructed, margins=margins,
                   direct_margin_bounds=direct_intervals, integer_checks=integer_checks,
                   checks=checks, summary=summary)
path = HERE / 'variable-table-early-support-audit-certificate.json'
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Independent exact checks: {len(checks)}; failures: {failures}')
print(f'Root cap {R} < required {cap}; residual {residual} > required 0')
print(f'23/23 margins; minimum {minimum} > required 233/25; all original records match')
print(f'Certificate: {path.relative_to(NOTEBOOK)}')
assert not failures
