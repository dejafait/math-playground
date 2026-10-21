#!/usr/bin/env python3
"""Independent exact audit of L069; no construction-program imports."""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ORIGINAL = HERE / 'permuted-last-pair-certificate.json'
raw = ORIGINAL.read_bytes()
stored = json.loads(raw)
# Separately transcribed from the canonical L055 table.
J = [8, 15, 28, 52, 98, 184, 347, 653, 1230, 2317, 4365, 8224,
     15494, 29191, 54998, 103621, 195229, 367827, 693015, 1305695,
     2460032, 4634896, 8732512, 16452748, 30998279]
H = [40, 72, 134, 249, 467, 877, 1650, 3106, 5849, 11018, 20756,
     39104, 73672, 138802, 261511, 492705, 928293, 1748976, 3295208,
     6208431, 11697176, 22038409, 41522114, 78230965, 32670621]
S, ell, u = 10**12, 693147180559, 1098612288669
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
checks = []


def check(name, actual, required, relation='='):
    passed = actual == required if relation == '=' else actual < required
    checks.append(dict(name=name, actual=actual, required=required,
                       relation=relation, passed=passed))


def log_interval(z):
    # DLMF 4.6.4 / the already assessed integrated geometric remainder.
    # For these z, 0<x<=1/2. No term rounding or binary reduction.
    x = (z-1)/(z+1)
    terms = [2*x**(2*k+1)/(2*k+1) for k in range(160)]
    lower = sum(terms, Q(0))
    error = 2*x**321/(321*(1-x*x))
    return dict(argument=z, x=x, terms=terms, error=error,
                lower=lower, upper=lower+error)


rows = [dict(i=i, J=j, H=h) for i, (j, h) in enumerate(zip(J, H))]
text55 = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
canonical = [tuple(map(int, r)) for r in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', text55, re.M)]
check('canonical complete table', canonical, list(zip(range(25), J, H)))
check('stored complete table', stored['rows'], rows)
check('sum J', sum(J), 66061058)
check('sum H', sum(H), 199390205)
K = sum(3*j+h for j, h in zip(J, H))
N = sum(4*j+h for j, h in zip(J, H)) + 166504460
check('odd count', K, 397573379)
check('total length', N, 630138897)
boundary_tails = []
for t in (2, 9250245):
    tails = [2]*23 + [2+18*t, 166504412-18*t]
    boundary_tails.append(dict(t=t, tails=tails))
    check(f't={t} sum tails', sum(tails), 166504460)
    check(f't={t} tail domain and congruence',
          all(a>=2 and a % 18 == 2 for a in tails), True)

logs = {str(z): log_interval(z) for z in (Q(2), Q(3))}
l2, l3 = logs['2'], logs['3']
check('strict log2 lower', Q(ell, S), l2['lower'], '<')
check('strict log3 upper', l3['upper'], Q(u, S), '<')
lambda_interval = [N*l2['lower']-K*l3['upper'],
                   N*l2['upper']-K*l3['lower']]
check('strict Lambda lower', lm, lambda_interval[0], '<')
check('strict Lambda upper', lambda_interval[1], lp, '<')
check('saved import operands', stored['imported_bounds'], dict(
    source='L055 audited (2),(6)', lambda_lower=str(lm),
    log2_lower_scaled=ell, log3_upper_scaled=u, scale=S))

minimum_upper = Q(575, 11)/lm+Q(23, 11)
terms = [Q(27)**q/factorial(q) for q in range(41)]
exp_sum = sum(terms, Q(0))
check('written minimum upper', minimum_upper, Q(7187500000030429, 14553))
check('saved minimum upper', Q(stored['minimum_shifted_upper']), minimum_upper)
check('minimum upper threshold', minimum_upper, 500000000000, '<')
check('all saved exp27 terms', list(map(Q, stored['exp27_terms'])), terms)
check('written exp27 sum', exp_sum, Q(
    1112436109266660239093546627471481746956608769015849,
    2106019961293006716393905717248000000000))
check('exp27 sum threshold', Q(500000000000), exp_sum, '<')
# Every eta is positive: both positive powers are <1 and 12/11+1=23/11.
check('all parameters for eta positivity', all(j>0 and h>0 for j,h in zip(J,H)), True)
check('negative prefix offset', Q(81,44), Q(3,11)*Q(3,2)**5, '<')
check('all prefix H >=5', all(h>=5 for h in H[:23]), True)
check('log(11/4)<2 positive exp2 sum', Q(11,4), Q(5), '<')
expected_rational = [
    ('positive imported Lambda lower', Q(0), lm),
    ('minimum shifted junction upper', minimum_upper, Q(500000000000)),
    ('exp27 partial sum exceeds 500 billion', Q(500000000000), exp_sum),
    ('log 11/4 below two via exp2 partial sum', Q(11,4), Q(5)),
    ('tail2 shifted offset negative at H>=5', Q(81,44), Q(3,11)*Q(3,2)**5)]
expected_rational_records = [dict(name=name, actual=str(a), required=str(b),
    relation='<', margin=str(b-a), passed=a<b) for name,a,b in expected_rational]
check('all saved rational checks including operands', stored['checks'], expected_rational_records)

prefixes = [dict(position=k, A=sum(3*J[i]+H[i] for i in range(k)),
                 D=sum(4*J[i]+H[i]+2 for i in range(k))) for k in range(24)]
check('all saved prefixes', stored['prefixes'], prefixes)
check('new final prefix', prefixes[23], dict(position=23, A=144318712, D=162928789))
pairs = []
for k in range(24):
    A, D = prefixes[k]['A'], prefixes[k]['D']
    for j in range(k+1, 25):
        lhs, rhs = 4*J[j]*ell, 29*S+A*u-D*ell
        record = dict(position=k, row=j, J=J[j], A=A, D=D,
                      lhs_lower_scaled=lhs, rhs_upper_scaled=rhs,
                      margin_scaled=lhs-rhs, passed=lhs>rhs)
        pairs.append(record)
        check(f'strict pair {k},{j}', 0, lhs-rhs, '<')
check('all 300 saved pair operands and margins', stored['pairs'], pairs)
weakest = [p for p in pairs if p['row']==p['position']+1]
check('all saved weakest operands', stored['weakest'], weakest)
text69 = (ROOT / 'lemmas/L069-permuted-last-pair-j-infeasibility.md').read_text()
written69 = [tuple(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|$', text69, re.M)]
check('all 24 written weakest margins', written69,
      [(p['position'], p['margin_scaled']) for p in weakest])
text63 = (ROOT / 'lemmas/L063-fixed-allocation-j-guard-order-rigidity.md').read_text()
written63 = [tuple(map(int, r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|$', text63, re.M)]
check('all 23 L063 finite margins minus 3S', written63,
      [(p['position'], p['margin_scaled']+3*S) for p in weakest[:23]])
for k in range(24):
    differences = [4*(J[j]-J[k+1])*ell for j in range(k+1,25)]
    check(f'weakest at {k},{k+1}',
          [p['margin_scaled']-weakest[k]['margin_scaled'] for p in pairs if p['position']==k],
          differences)
    check(f'monotone row {k}', min(differences), 0)
table_checks = dict(
    indexed_rows=[r['i'] for r in rows] == list(range(25)),
    increasing_J=all(a<b for a,b in zip(J,J[1:])),
    parameter_lower_bounds=min(J)>=8 and min(H)>=40,
    odd_count=K == 397573379,
    total_tail_budget=23*2+2+166504412 == 166504460,
    total_length=N == 630138897,
    max_parameter_tails=2+18*9250245 == 166504412 and 166504412-18*9250245 == 2,
    first_displacement_coverage=len(pairs)==300 and len(weakest)==24 and
        {(p['position'],p['row']) for p in pairs} ==
        {(k,j) for k in range(24) for j in range(k+1,25)})
check('all eight saved table checks', stored['table_checks'], table_checks)
check('all eight independent table checks true', all(table_checks.values()), True)
smallest = min(pairs, key=lambda p:p['margin_scaled'])
check('written minimum margin', Q(smallest['margin_scaled'], S), Q(629441541677, 50000000000))
check('required minimum margin', Q(1258,100), Q(smallest['margin_scaled'],S), '<')
check('stored summary recomputed', stored['summary'], dict(pair_count=300, minimum=smallest, failures=[]))
# This boundary computation cross-checks the imported audited L068 margin;
# its full-interval monotonicity remains an explicit cited input.
boundary_upper = Q(24)+Q(271907921*u-430963900*ell+1011600911679,S)
check('L068 imported boundary arithmetic', boundary_upper, -Q(474883782659,125000000000))
check('L068 strict rejection threshold', boundary_upper, -Q(379,100), '<')
failures = [c['name'] for c in checks if not c['passed']]
summary = dict(check_count=len(checks), failures=failures, pair_count=len(pairs),
    weakest_count=len(weakest), minimum_scaled_margin=smallest['margin_scaled'],
    minimum_required=0, minimum_shifted_upper=str(minimum_upper),
    shifted_threshold=500000000000, exp_sum_exceeds_threshold=exp_sum>500000000000,
    last_pair=weakest[-1], L068_boundary_upper=str(boundary_upper),
    classification='independent audit; symbolic order/interval proof remains canonical')
out = dict(summary=summary, original_sha256=sha256(raw).hexdigest(),
    checks=checks, rows=rows, boundary_tails=boundary_tails, logarithms=logs,
    lambda_interval=lambda_interval, prefixes=prefixes, pairs=pairs,
    weakest=weakest, exp27_terms=terms, exp27_sum=exp_sum)
path = HERE / 'permuted-last-pair-audit-certificate.json'
path.write_text(json.dumps(out, default=str, indent=2)+'\n')
print(f'{len(checks)} exact checks; failures: {failures}')
print(f'{len(pairs)} margins required >0; minimum {Q(smallest["margin_scaled"],S)} >12.58')
print(f'Minimum upper {minimum_upper} <500000000000; exp27 partial sum >500000000000: {exp_sum>500000000000}')
print(f'L068 boundary upper {boundary_upper} <-3.79')
print(f'Certificate: {path}')
assert not failures
