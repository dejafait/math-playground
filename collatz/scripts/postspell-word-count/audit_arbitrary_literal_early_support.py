#!/usr/bin/env python3
"""Independent exact arithmetic audit of L073, without running its certifier.

The allocation-wide implications are proved in L073. This audits their
finite operands and independently encloses all imported logarithms.
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


def check(name, actual, required, relation="eq"):
    passed = actual == required if relation == "eq" else actual < required
    checks.append(dict(name=name, relation=relation, actual=actual,
                       required=required, passed=passed))


def log_bounds(t):
    # DLMF 4.6.4, positive-real specialization; unrounded finite series.
    x = (t-1)/(t+1)
    assert 0 < x <= Q(1, 2)
    terms = [2*x**(2*m+1)/(2*m+1) for m in range(128)]
    lower = sum(terms, Q(0))
    remainder = 2*x**257/(257*(1-x*x))
    return dict(argument=t, x=x, terms=terms, remainder=remainder,
                lower=lower, upper=lower+remainder)


original_path = HERE / 'arbitrary-literal-early-support-certificate.json'
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
lemma55 = (NOTEBOOK / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
rows = [list(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', lemma55, re.M)]
expected_rows = [[i, J, H] for i, (J, H) in enumerate(PAIRS)]
check('independent table matches L055', rows, expected_rows)
check('original certificate table', original['rows'], expected_rows)
check('sum J', sum(J for J, H in PAIRS), 66061058)
check('sum H', sum(H for J, H in PAIRS), 199390205)
K = sum(3*J+H for J, H in PAIRS)
tail_budget = 25*2+18*9250245
N = sum(4*J+H for J, H in PAIRS)+tail_budget
check('odd count', K, 397573379)
check('total count', N, 630138897)
check('tail sum', tail_budget, 166504460)
check('minimum J after zero', min(J for J, H in PAIRS[1:]), 15)
check('minimum H', min(H for J, H in PAIRS), 40)
check('all J positive', all(J > 0 for J, H in PAIRS), True)

logs = {name: log_bounds(t) for name, t in [('two', Q(2)), ('three', Q(3)), ('shift', Q(11, 4))]}
S = 10**12
EL, EU = 693147180559, 693147180560
TL, TU = 1098612288668, 1098612288669
DL, DU = 1011600911678, 1011600911679
for name, lo, hi in [('two', EL, EU), ('three', TL, TU), ('shift', DL, DU)]:
    check(name+' grid lower', Q(lo, S), logs[name]['lower'], 'lt')
    check(name+' grid upper', logs[name]['upper'], Q(hi, S), 'lt')
lambda_lower = N*logs['two']['lower']-K*logs['three']['upper']
lambda_upper = N*logs['two']['upper']-K*logs['three']['lower']
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
check('Lambda lower', lm, lambda_lower, 'lt')
check('Lambda upper', lambda_upper, lp, 'lt')

denominator = 4*2**60-23
residual = Q(24*23, denominator)
check('positive residual denominator', Q(0), lm-residual, 'lt')
root_upper = Q(23, 11)/(lm-residual)+Q(23, 11)
check('root below 20 billion', root_upper, Q(20*10**9), 'lt')
check('published root fraction', root_upper,
      Q(1325859730438202850942226985830949, 67113790726173775832193))
offset_left = Q(23, 11)*2**20
offset_right = Q(12, 11)*Q(3, 2)**40+1
check('tail20 negative offset', offset_left, offset_right, 'lt')
check('tail2 offset follows', Q(23, 11)*2**2, offset_left, 'lt')
exp_terms = [Q(24**k, factorial(k)) for k in range(41)]
exp_lower = sum(exp_terms, Q(0))
check('exp24 partial sum', Q(20*10**9), exp_lower, 'lt')
check('saved residual', Q(original['other_mass_upper']), residual)
check('saved lambda lower', Q(original['lambda_lower']), lm)
check('saved root upper', Q(original['s0_upper']), root_upper)

# Reconstruct every original rational-check operand, margin and verdict.
original_comparisons = [
    ('other-input mass upper below lambda lower', residual, lm),
    ('guard-conditioned s0 upper below 20 billion', root_upper, Q(20*10**9)),
    ('tail20 negative shifted offset at H40', offset_left, offset_right),
]
margin_records = []
independent_margins = []
for j in range(23):
    prefix_K = sum(3*J+H for J, H in PAIRS[:j+1])
    prefix_N = sum(4*J+H+2 for J, H in PAIRS[:j+1])
    next_J = PAIRS[j+1][0]
    base = 24*S+prefix_K*TU-prefix_N*EL
    u = 24*S+prefix_K*TU-(prefix_N+18+4*next_J)*EL+DU
    independent = (24+prefix_K*logs['three']['upper']
                   -(prefix_N+18+4*next_J)*logs['two']['lower']
                   +logs['shift']['upper'])
    check(f'independent guard upper {j} below -9.32', independent, -Q(233, 25), 'lt')
    check(f'independent bound {j} below grid bound', independent, Q(u, S), 'lt')
    margin_records.append(dict(first_recipient=j, failed_input=j+1,
                               base_prefix_upper_scaled=base,
                               guard_upper_numerator=u, scale=S))
    independent_margins.append(dict(j=j, prefix_K=prefix_K, prefix_N=prefix_N,
                                    next_J=next_J, exact_upper=independent))
    original_comparisons.append((f'first recipient {j} guard margin below -9.32', Q(u, S), -Q(233, 25)))

check('all original margin records', original['margins'], margin_records)
check('original check count', len(original['checks']), len(original_comparisons))
for record, (name, actual, required) in zip(original['checks'], original_comparisons):
    expected = dict(name=name, actual=str(actual), required=str(required),
                    margin=str(required-actual), passed=actual < required)
    check('complete original operands: '+name, record, expected)
    check('recomputed original inequality: '+name, actual, required, 'lt')

expected_integer = dict(
    all_parameters_in_domain=all(J >= 2 and H >= 40 for J, H in PAIRS),
    other_J_at_least_15=all(J >= 15 for J, H in PAIRS[1:]),
    odd_count=K == 397573379, total_count=N == 630138897,
    all_first_recipients_covered=[r['first_recipient'] for r in margin_records] == list(range(23)))
check('all original integer checks reconstructed', original['integer_checks'], expected_integer)
check('integer checks hold', all(expected_integer.values()), True)
lemma64 = (NOTEBOOK / 'lemmas/L064-single-tail-redistribution-j-guard-classification.md').read_text()
published = [list(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(-\d+)\|$', lemma64, re.M)]
check('all L064 published rejecting margins', published,
      [[r['first_recipient'], r['failed_input'], r['guard_upper_numerator']] for r in margin_records])
worst = max(margin_records, key=lambda r: r['guard_upper_numerator'])
check('published weakest recipient', worst['first_recipient'], 4)
check('published weakest margin', worst['guard_upper_numerator'], -9322534135606)
check('no original failures', original['failures'], [])
failures = [c['name'] for c in checks if not c['passed']]

summary = dict(
    checks=len(checks), failures=failures,
    lambda_grid_scale=10**20,
    lambda_lower_floor=(lambda_lower*10**20).__floor__(),
    lambda_upper_ceil=(lambda_upper*10**20).__ceil__(),
    required_lambda_lower=lm, required_lambda_upper=lp,
    residual=residual, positive_denominator=lm-residual,
    root_upper=root_upper, required_root_upper=20*10**9,
    offset_left=offset_left, offset_right=offset_right,
    exp24_partial_sum=exp_lower, required_exp_lower=20*10**9,
    rejecting_numerators=[r['guard_upper_numerator'] for r in margin_records],
    guard_scale=S, weakest_recipient=worst['first_recipient'],
    required_guard_upper=-Q(233, 25))
certificate = dict(purpose='Independent finite-input audit of L073; universal coverage is symbolic',
                   original_sha256=hashlib.sha256(original_bytes).hexdigest(),
                   table=expected_rows, logarithms=logs,
                   lambda_interval=[lambda_lower, lambda_upper], exp24_terms=exp_terms,
                   independent_margins=independent_margins,
                   reconstructed_original_margins=margin_records, checks=checks, summary=summary)
path = HERE / 'arbitrary-literal-early-support-audit-certificate.json'
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Independent exact checks: {len(checks)}; failures: {failures}')
print(f'Root bound: {root_upper} < required {20*10**9}')
print(f'Largest grid guard upper: {worst["guard_upper_numerator"]}/{S} < required -233/25; 23/23 positions')
print(f'Certificate: {path.relative_to(NOTEBOOK)}')
assert not failures
