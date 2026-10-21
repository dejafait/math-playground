#!/usr/bin/env python3
"""Independent exact arithmetic for the approved L071 critical audit.

No construction/audit program is imported or executed. Universal order and
parameter coverage is justified in L071's written audit, not sampled here.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
original_path = HERE / 'permuted-two-recipient-certificate.json'
original_bytes = original_path.read_bytes()
original = json.loads(original_bytes)
J = [8, 15, 28, 52, 98, 184, 347, 653, 1230, 2317, 4365, 8224,
     15494, 29191, 54998, 103621, 195229, 367827, 693015, 1305695,
     2460032, 4634896, 8732512, 16452748, 30998279]
H = [40, 72, 134, 249, 467, 877, 1650, 3106, 5849, 11018, 20756,
     39104, 73672, 138802, 261511, 492705, 928293, 1748976, 3295208,
     6208431, 11697176, 22038409, 41522114, 78230965, 32670621]
S, ell, upper3 = 10**12, 693147180559, 1098612288669
lower_lambda, upper_lambda = F(10584, 10**14), F(10585, 10**14)
checks = []


def check(name, actual, required, relation='=='):
    passed = actual == required if relation == '==' else actual < required
    checks.append(dict(name=name, actual=actual, required=required,
                       relation=relation, passed=passed))


rows = [dict(i=i, J=J[i], H=H[i]) for i in range(25)]
source_table = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(),
    re.M)]
check('independent transcription against L055',
      list(zip(range(25), J, H)), source_table)
check('construction rows', original['rows'], rows)
check('sum J', sum(J), 66061058)
check('sum H', sum(H), 199390205)
K = sum(3*j+h for j, h in zip(J, H))
N = sum(4*j+h for j, h in zip(J, H)) + 166504460
check('K', K, 397573379)
check('N', N, 630138897)


def log_interval(z):
    # Assessed DLMF expansion, with exact positive geometric remainder.
    x = (z-1)/(z+1)
    terms = [2*x**(2*k+1)/F(2*k+1) for k in range(160)]
    lo = sum(terms)
    remainder = 2*x**321/(321*(1-x*x))
    return dict(argument=z, x=x, terms=terms, remainder=remainder,
                lower=lo, upper=lo+remainder)


logs = {str(z): log_interval(z) for z in (F(2), F(3), F(11, 4))}
l2, l3, l11 = logs['2'], logs['3'], logs['11/4']
check('strict log2 grid lower', F(ell, S), l2['lower'], '<')
check('strict log3 grid upper', l3['upper'], F(upper3, S), '<')
check('L070 log11/4 grid upper', l11['upper'], F(1011600911679, S), '<')
lam_lo = N*l2['lower']-K*l3['upper']
lam_hi = N*l2['upper']-K*l3['lower']
check('Lambda lower', lower_lambda, lam_lo, '<')
check('Lambda upper', lam_hi, upper_lambda, '<')

minimum = F(575, 11)/lower_lambda+F(23, 11)
exp_terms = [F(27**k, factorial(k)) for k in range(41)]
exp_sum = sum(exp_terms)
offset = F(12, 11)*F(3, 2)**40/2**20
offset_difference = offset-F(23, 11)
check('written minimum fraction', minimum, F(7187500000030429, 14553))
check('written exp27 fraction', exp_sum, F(
    1112436109266660239093546627471481746956608769015849,
    2106019961293006716393905717248000000000))
check('written offset fraction', offset,
      F(36472996377170786403, 3170534137668829184))
check('written offset difference', offset_difference,
      F(2713063429607401481, 288230376151711744))
check('construction minimum', original['minimum_shifted_upper'], str(minimum))
check('construction offset', original['offset_subtraction_lower'], str(offset))
check('all exp27 terms', original['exp27_terms'], list(map(str, exp_terms)))
check('construction exp27 sum', original['exp27_sum'], str(exp_sum))

comparisons = [
    ('positive imported Lambda lower', F(0), lower_lambda),
    ('minimum shifted junction upper', minimum, F(500_000_000_000)),
    ('exp27 positive partial sum exceeds threshold', F(500_000_000_000), exp_sum),
    ('log 11/4 below two via exp2 partial sum', F(11, 4), F(5)),
    ('negative shifted offset for a<=20 H>=40', F(23, 11), offset),
    ('L070 literal guard upper is negative', F(-474883782659, 125000000000), F(0)),
]
expected_checks = []
for name, actual, required in comparisons:
    check(name, actual, required, '<')
    expected_checks.append(dict(name=name, actual=str(actual), required=str(required),
        relation='<', margin=str(required-actual), passed=actual < required))
check('complete original rational comparison records', original['checks'], expected_checks)

boundaries = [dict(t=t, tails=[2]*22+[20, 2+18*t, 166504394-18*t])
              for t in (1, 9250244)]
check('complete original boundary tails', original['boundaries'], boundaries)
check('last tail at maximum t', boundaries[1]['tails'][-1], 2)
prefixes, pairs, weakest = [], [], []
for k in range(24):
    A = sum(3*J[i]+H[i] for i in range(k))
    D = sum(4*J[i]+H[i]+(20 if i == 22 else 2) for i in range(k))
    prefixes.append(dict(position=k, A=A, D=D))
    for j in range(k+1, 25):
        lhs = 4*J[j]*ell
        rhs = 29*S+A*upper3-D*ell
        record = dict(position=k, row=j, J=J[j], A=A, D=D,
            lhs_lower_scaled=lhs, rhs_upper_scaled=rhs,
            margin_scaled=lhs-rhs, passed=lhs > rhs)
        pairs.append(record)
        check(f'pair {k},{j} strict rejection', rhs, lhs, '<')
        if j == k+1:
            weakest.append(record)
check('complete original prefixes', original['prefixes'], prefixes)
check('complete original 300 operands and margins', original['pairs'], pairs)
check('complete original weakest records', original['weakest'], weakest)
written = [tuple(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|$',
    (ROOT / 'lemmas/L071-permuted-two-recipient-j-infeasibility.md').read_text(), re.M)]
check('all 24 written weakest margins', written,
      [(r['position'], r['margin_scaled']) for r in weakest])
check('written final lower operand', weakest[-1]['lhs_lower_scaled'], 85945478764125031844)
check('written final upper operand', weakest[-1]['rhs_upper_scaled'], 45616696284190811215)
check('changed final prefix', prefixes[-1], dict(position=23, A=144318712, D=162928807))
check('strict increasing J', all(J[i] < J[i+1] for i in range(24)), True)
check('smallest pair', min(pairs, key=lambda p:p['margin_scaled']), pairs[0])
check('minimum margin fraction', F(pairs[0]['margin_scaled'], S),
      F(629441541677, 50000000000))
check('minimum margin threshold', F(1258, 100), F(pairs[0]['margin_scaled'], S), '<')

# Verify the literal cited bound's arithmetic; its whole-interval theorem
# and exact hypothesis match are reviewed in the canonical written audit.
boundary_tails = boundaries[0]['tails']
p24 = sum(3*J[i]+H[i] for i in range(24))
q24 = sum(4*J[i]+H[i]+boundary_tails[i] for i in range(24))
literal_guard = F(24*S+p24*upper3-(q24+4*J[24])*ell+1011600911679, S)
check('L070 boundary p,q', [p24, q24], [271907921, 306970784])
check('L070 cited margin', literal_guard, F(-474883782659, 125000000000))

table_checks = dict(
    indexed_rows=[r['i'] for r in rows] == list(range(25)),
    increasing_J=all(J[i] < J[i+1] for i in range(24)),
    parameter_bounds=all(j >= 8 and h >= 40 for j, h in zip(J, H)),
    sum_J=sum(J) == 66061058, sum_H=sum(H) == 199390205,
    odd_count=K == 397573379, total_length=N == 630138897,
    constant_tail_budget=44+20+2+166504394 == 166504460,
    boundary_tail_sums=all(sum(b['tails']) == 166504460 for b in boundaries),
    boundary_tail_domain=all(a >= 2 and a % 18 == 2 for b in boundaries for a in b['tails']),
    changed_final_prefix=prefixes[-1] == dict(position=23, A=144318712, D=162928807),
    full_pair_coverage=len(pairs) == 300 and len(weakest) == 24 and
        {(p['position'], p['row']) for p in pairs} ==
        {(k, j) for k in range(24) for j in range(k+1, 25)})
check('complete original table checks', original['table_checks'], table_checks)
for name, passed in table_checks.items():
    check('independent table '+name, passed, True)
check('original imported constants', original['imports'], dict(
    source='L055 audited (2),(6); L070 audited literal exclusion',
    lambda_lower=str(lower_lambda), log2_lower_scaled=ell,
    log3_upper_scaled=upper3, scale=S))

failures = [c['name'] for c in checks if not c['passed']]
result = dict(
    scope='Independent L071 arithmetic audit; endpoint/domain/J only, t=1..9250244',
    original_sha256=sha256(original_bytes).hexdigest(), rows=rows, boundaries=boundaries,
    logarithms=logs, lambda_interval=dict(lower=lam_lo, upper=lam_hi),
    prefixes=prefixes, pairs=pairs, weakest=weakest,
    exp27_terms=exp_terms, exp27_sum=exp_sum,
    minimum_upper=minimum, offset_lower=offset, offset_difference=offset_difference,
    literal_guard_upper=literal_guard, checks=checks,
    summary=dict(checks=len(checks), failures=failures, pair_count=len(pairs),
        weakest_count=len(weakest), minimum_margin=F(pairs[0]['margin_scaled'], S),
        final_prefix=prefixes[-1], final_pair=weakest[-1],
        required_pair_margin='>0', required_minimum_upper='<500000000000',
        required_exp27_sum='>500000000000', required_offset_lower='>23/11'))
out = HERE / 'permuted-two-recipient-audit-certificate.json'
out.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'{len(checks)} exact checks; failures: {failures}')
print(f'300 pair margins required >0; minimum {F(pairs[0]["margin_scaled"], S)} > 12.58')
print(f'Minimum upper {minimum} < 500000000000; exp27 partial sum > 500000000000: {exp_sum > 500000000000}')
print(f'Offset lower {offset} > 23/11; D_23={prefixes[-1]["D"]}')
print(f'L070 boundary guard {literal_guard} < -3.79')
print(f'Full certificate: {out.relative_to(ROOT)}')
assert not failures
