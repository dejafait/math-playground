#!/usr/bin/env python3
"""Independent L064 audit; does not execute/import the original certifier.

Use unrounded 128-term rational logarithms and direct prefix exponent sums.
Also check every original rounded term, stored operand and guard record.
The symbolic fixed-point/domain proof is audited in canonical L064.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'single-tail-redistribution-certificate.json'
old = json.loads(SOURCE.read_text())
checks = []


def check(name, actual, required, relation='=='):
    ok = actual == required if relation == '==' else actual < required
    checks.append(dict(name=name, actual=str(actual), required=str(required),
                       relation=relation, passed=ok))


# Independently transcribed literal rows, compared with the canonical table.
J = [8,15,28,52,98,184,347,653,1230,2317,4365,8224,15494,29191,
     54998,103621,195229,367827,693015,1305695,2460032,4634896,
     8732512,16452748,30998279]
H = [40,72,134,249,467,877,1650,3106,5849,11018,20756,39104,73672,
     138802,261511,492705,928293,1748976,3295208,6208431,11697176,
     22038409,41522114,78230965,32670621]
literal = [(i, J[i], H[i]) for i in range(25)]
table = [tuple(map(int, r)) for r in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(), re.M)]
check('literal table independently transcribed', literal, table)
K, N, L, S = 397573379, 630138897, 232565518, 10**12
check('sum J', sum(J), 66061058)
check('sum H', sum(H), 199390205)
check('original counts', old['counts'], dict(K=K, L=L, N=N))


def series(t):
    """128 unrounded terms; argument-specific geometric tail bound."""
    x = (t-1)/(t+1)
    assert 0 <= x <= F(1, 2)
    terms, power = [], x
    for m in range(128):
        terms.append(2*power/(2*m+1))
        power *= x*x
    tail = 2*power/(257*(1-x*x))
    lo = sum(terms, F(0))
    return lo, lo+tail, dict(argument=str(t), x=str(x),
        terms=[str(v) for v in terms], tail_upper=str(tail))


logs = {}
for name, value in [('2',F(2)), ('3',F(3)), ('11/4',F(11,4))]:
    lo, hi, detail = series(value)
    logs[name] = dict(lower=str(lo), upper=str(hi), detail=detail)
e0, e1 = (F(logs['2'][k]) for k in ('lower','upper'))
t0, t1 = (F(logs['3'][k]) for k in ('lower','upper'))
d0, d1 = (F(logs['11/4'][k]) for k in ('lower','upper'))
lo, hi, detail = series(F(18*10**9, 2**34))
logs['18000000000'] = dict(lower=str(lo+34*e0), upper=str(hi+34*e1),
    binary_exponent=34, detail=detail)
check('independent log18e9 lower', F(2361,100), lo+34*e0, '<')
check('independent Lambda lower', F(10584,10**14), N*e0-K*t1, '<')
check('independent Lambda upper', N*e1-K*t0, F(10585,10**14), '<')
constants = dict(S=S, EL=693147180559, EU=693147180560,
    TL=1098612288668, TU=1098612288669, CL=1011600911678, CU=1011600911679,
    AL=523248143764, AU=523248143771, BL=405465108108, BU=405465108110)
check('all published constants', old['constants'], constants)
for name, low, high, lkey, ukey in [('log2',e0,e1,'EL','EU'),
        ('log3',t0,t1,'TL','TU'), ('log11/4',d0,d1,'CL','CU')]:
    check(name+' independent lower', F(constants[lkey],S), low, '<')
    check(name+' independent upper', high, F(constants[ukey],S), '<')

# Authenticate original error budgets and every stored term, not just their sums.
rounded_audits = []


def verify_rounded(name, t, record):
    x = (t-1)/(t+1)
    check(name+' reduced domain lower', True, 0 <= x <= F(1,3))
    check(name+' x', F(record['x']), x)
    terms = [2*x**(2*m+1)/(2*m+1) for m in range(96)]
    check(name+' summand count', len(record['rounded_summands']), 96)
    for m, term in enumerate(terms):
        rounded = F(record['rounded_summands'][m], 2**192)
        check(f'{name} term {m} floor', True, rounded <= term < rounded+F(1,2**192))
    budget, remainder = F(96,2**192), F(9,4*193*3**193)
    check(name+' rounding budget', F(record['rounding_budget']), budget)
    check(name+' remainder budget', F(record['remainder_upper']), remainder)
    exact_tail_bound = 2*x**193/(193*(1-x*x))
    check(name+' geometric tail envelope', True, exact_tail_bound <= remainder)
    lower = F(sum(record['rounded_summands']),2**192)
    rounded_audits.append(dict(name=name, exact_terms=[str(t) for t in terms],
        lower=str(lower), upper=str(lower+budget+remainder),
        actual_tail_upper=str(exact_tail_bound), required_tail_upper=str(remainder)))
    return lower, lower+budget+remainder


oe0, oe1 = verify_rounded('original log2 base', F(2), old['log2_detail'])
check('original log keys', set(old['logs']), {'2','3','11/4','18000000000'})
for key, rec in old['logs'].items():
    k, u = rec['binary_exponent'], F(rec['reduced_argument'])
    check(key+' reduction', F(key), 2**k*u)
    check(key+' normalized domain', True, k >= 0 and 1 <= u < 2)
    a, b = verify_rounded('original '+key, u, rec['detail'])
    check(key+' full lower', F(rec['lower']), a+k*oe0)
    check(key+' full upper', F(rec['upper']), b+k*oe1)

# Root/domain operands independently reconstructed from exact small powers.
lm, lp = F(10584,10**14), F(10585,10**14)
eta = F(23,11)-F(12*16**8,11*27**8)-F(16**8*2**40,27**8*3**40)
bmax = F(23,11)*(1+F(2**19,10**8))
root_lo, root_hi = 2/lp-2, bmax/lm
shift_hi = root_hi+bmax+F(23,11)
for key, value in dict(lambda_lower=lm,lambda_upper=lp,eta0=eta,B_lower=F(2),
        B_upper=bmax,n0_lower=root_lo,n0_upper=root_hi,
        normalized_shifted_upper=shift_hi).items():
    check('root operand '+key, F(old['bounds'][key]), value)
check('finite B upper strictly below Bmax',
    F(23,11)*(1+F(2**18,10**8)*sum((F(1,2**i) for i in range(24)), F(0))), bmax, '<')
exp_terms = [F(24**k,factorial(k)) for k in range(41)]
check('all original exponential terms', [F(v) for v in old['exp24_terms']], exp_terms)

# Reconstruct the complete original rational-check operands and signs.
ol = lambda key: F(old['logs'][key]['lower'])
ou = lambda key: F(old['logs'][key]['upper'])
expected = []
for name,key,lkey,ukey in [('log2','2','EL','EU'),('log3','3','TL','TU'),
        ('log(11/4)','11/4','CL','CU')]:
    expected += [(name+' lower',F(constants[lkey],S),ol(key)),
                 (name+' upper',ou(key),F(constants[ukey],S))]
expected += [
    ('alpha lower positive',F(0),F(constants['AL'])),
    ('beta lower positive',F(0),F(constants['BL'])),
    ('Lambda lower independently reproduced',lm,N*ol('2')-K*ou('3')),
    ('Lambda upper independently reproduced',N*ou('2')-K*ol('3'),lp),
    ('Lambda upper below one',lp,F(1)), ('eta0 above two',F(2),eta),
    ('row0 tail20 multiplier above 1e8/2^18',F(10**8,2**18),F(3**64,2**92)),
    ('row0 uniform multiplier above two',F(2),F(10**8,2**18)),
    ('rows1..23 tail20 baseline above two',F(2),F(3**117,2**152)),
    ('n0 lower above 18 billion',F(18*10**9),root_lo),
    ('prefix normalized shifted upper below 20 billion',shift_hi,F(20*10**9)),
    ('domain follows from lower root',F(540,11),F(18*10**9)),
    ('lower normalized log above 23.61',F(2361,100),ol('18000000000')),
    ('exp24 finite lower sum above 20 billion',F(20*10**9),sum(exp_terms))]
check('original rational check count', len(old['checks']), len(expected))
for (name,a,b), rec in zip(expected,old['checks']):
    check(name+' full record',rec,dict(name=name,actual=str(a),required=str(b),
                                     margin=str(b-a),passed=a<b))
    check(name+' verified inequality',a,b,'<')

# Direct prefix sums, not the original v/w recurrence; a second computation
# uses tighter independent logarithms with the total exponents directly.
allocations, decisive = [], []
EL, EU, TL, TU, CL, CU = (constants[k] for k in ('EL','EU','TL','TU','CL','CU'))
check('allocation count',len(old['allocations']),24)
for moved, saved in enumerate(old['allocations']):
    tails = [20 if i==moved else 166504394 if i==24 else 2 for i in range(25)]
    rows = [dict(i=i,J=J[i],H=H[i],a=tails[i]) for i in range(25)]
    check(f'{moved} literal parameters', saved['rows'], rows)
    check(f'{moved} moved index', saved['moved_tail_row'], moved)
    check(f'{moved} total tails',sum(tails),166504460)
    truths = dict(literal_order=True,
        parameter_domain=all(J[i]>=2 and H[i]>=3 and tails[i]>=2 and tails[i]%18==2 for i in range(25)),
        odd_total=sum(3*J[i]+H[i] for i in range(25))==K,
        even_total=sum(J)+sum(tails)==L,
        total_exponent=4*sum(J)+sum(H)+sum(tails)==N,
        growing_prefix_baselines=all(J[i]>=15 and H[i]>=72 and tails[i]<=20 for i in range(1,24)),
        closing_product=(3*sum(J)+sum(H),4*sum(J)+sum(H)+sum(tails))==(K,N))
    check(f'{moved} all seven integer-check meanings',saved['integer_checks'],truths)
    check(f'{moved} integer checks true',all(truths.values()),True)
    check(f'{moved} closing exponents', saved['closing_prefix'],dict(three_exponent=K,two_exponent=N))
    guards, prefixes, independent = [], [], []
    for i in range(25):
        pk = 3*sum(J[:i])+sum(H[:i])
        pn = 4*sum(J[:i])+sum(H[:i])+sum(tails[:i])
        prefixes.append(dict(i=i,three_exponent=pk,two_exponent=pn))
        v, w = 2361*S//100+pk*TL-pn*EU, 24*S+pk*TU-pn*EL
        low, high = v+CL-4*J[i]*EU, w+CU-4*J[i]*EL
        verdict = 'PASS_STRICT' if low>0 else 'FAIL_STRICT' if high<0 else 'UNRESOLVED'
        guards.append(dict(i=i,J=J[i],log_s_lower_scaled=v,log_s_upper_scaled=w,
            margin_lower_scaled=low,margin_upper_scaled=high,verdict=verdict))
        ilow = F(2361,100)+pk*t0-(pn+4*J[i])*e1+d0
        ihigh = F(24)+pk*t1-(pn+4*J[i])*e0+d1
        iv = 'PASS_STRICT' if ilow>0 else 'FAIL_STRICT' if ihigh<0 else 'UNRESOLVED'
        check(f'{moved}:{i} independent verdict',iv,verdict)
        independent.append(dict(i=i,three_exponent=pk,two_exponent=pn,
            lower=str(ilow),upper=str(ihigh),verdict=iv))
        if (moved<23 and i==moved+1) or moved==23:
            decisive.append(dict(moved=moved,i=i,lower_scaled=low,upper_scaled=high,
                independent_lower=str(ilow),independent_upper=str(ihigh)))
    check(f'{moved} all 25 original guards', saved['guards'], guards)
    check(f'{moved} all 25 original prefixes',saved['prefixes'],prefixes)
    failed = [g['i'] for g in guards if g['verdict']=='FAIL_STRICT']
    unresolved = [g['i'] for g in guards if g['verdict']=='UNRESOLVED']
    verdict = 'REJECTED_BY_J_GUARD' if failed else 'UNRESOLVED' if unresolved else 'ALL_J_GUARDS_PASS'
    check(f'{moved} allocation verdict',saved['verdict'],verdict)
    check(f'{moved} first failed guard',saved['first_failed_guard'],failed[0] if failed else None)
    check(f'{moved} unresolved guards',saved['unresolved_guard_indices'],unresolved)
    check(f'{moved} no unresolved guards',unresolved,[])
    check(f'{moved} domain label',saved['domain'],'ALL_s_i_ABOVE_18_BILLION')
    if moved<23:
        check(f'{moved} decisive rejection threshold',guards[moved+1]['margin_upper_scaled'],-932*S//100,'<')
    else:
        check('survivor all guards',all(g['margin_lower_scaled']>0 for g in guards),True)
        check('survivor minimum',(min(g['margin_lower_scaled'] for g in guards),
             min(range(25),key=lambda i: guards[i]['margin_lower_scaled'])),(402427610954,19))
    allocations.append(dict(moved=moved,tails=tails,prefixes=prefixes,
        guards=guards,independent_guards=independent,verdict=verdict))

# Compare the complete published decisive tables with independently computed values.
lemma = (ROOT/'lemmas/L064-single-tail-redistribution-j-guard-classification.md').read_text()
published_fail = [tuple(map(int,r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(-\d+)\|$',lemma,re.M)]
check('all 23 published failure margins',published_fail,
      [(v['moved'],v['i'],v['upper_scaled']) for v in decisive if v['moved']<23])
published_pass = list(map(int,re.search(r'```text\n([\d\s]+)\n```',lemma).group(1).split()))
check('all 25 published survivor margins',published_pass,
      [v['lower_scaled'] for v in decisive if v['moved']==23])
check('decisive comparison count',len(decisive),48)
check('original survivors',old['survivors'],[23])
check('original failures',old['failures'],[])
failures = [c['name'] for c in checks if not c['passed']]
summary = dict(check_count=len(checks),failures=failures,allocations=24,
    original_guard_records=600,independent_guard_verdicts=600,rounded_terms=5*96,
    decisive_comparisons=48,survivors=[a['moved'] for a in allocations if a['verdict']=='ALL_J_GUARDS_PASS'],
    least_failure_margin_lower_scaled=min(-d['upper_scaled'] for d in decisive if d['moved']<23),
    required_failure_margin_scaled=932*S//100,
    survivor_minimum_lower_scaled=402427610954,required_survivor_lower_scaled=0,
    scale=S,root_lower=str(root_lo),required_root_lower=18*10**9,
    normalized_upper=str(shift_hi),required_normalized_upper=20*10**9)
summary['decisive_failure_upper_scaled'] = [d['upper_scaled'] for d in decisive if d['moved']<23]
summary['survivor_lower_scaled'] = [d['lower_scaled'] for d in decisive if d['moved']==23]
out = HERE/'single-tail-redistribution-audit-certificate.json'
out.write_text(json.dumps(dict(summary=summary,original_certificate_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    checks=checks,independent_logs=logs,original_log_audits=rounded_audits,
    allocations=allocations,decisive=decisive),indent=2)+'\n')
print(f'Checks: {len(checks)}; failures: {failures}; 600 independent guard verdicts; 48 decisive comparisons')
print(f'Failure margin > {summary["least_failure_margin_lower_scaled"]}/{S} > 9.32; survivor margin > 402427610954/{S} > 0')
print(f'Root > {root_lo} > 18000000000; normalized shifted height < {shift_hi} < 20000000000')
print(f'Certificate: {out.relative_to(ROOT)}')
assert not failures
