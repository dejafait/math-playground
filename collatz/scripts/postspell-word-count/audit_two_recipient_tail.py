#!/usr/bin/env python3
"""Independent finite audit of L070; interval algebra is in the lemma.

Does not import or execute the original certifier. Full operands go to disk.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
original_path = HERE / 'two-recipient-tail-certificate.json'
raw = original_path.read_bytes()
original = json.loads(raw)
pairs = [
    (8,40), (15,72), (28,134), (52,249), (98,467),
    (184,877), (347,1650), (653,3106), (1230,5849), (2317,11018),
    (4365,20756), (8224,39104), (15494,73672), (29191,138802),
    (54998,261511), (103621,492705), (195229,928293),
    (367827,1748976), (693015,3295208), (1305695,6208431),
    (2460032,11697176), (4634896,22038409), (8732512,41522114),
    (16452748,78230965), (30998279,32670621),
]
checks = []


def eq(name, actual, required):
    checks.append(dict(name=name, relation='=', actual=actual,
                       required=required, passed=actual == required))


def lt(name, actual, required):
    checks.append(dict(name=name, relation='<', actual=actual,
                       required=required, margin=required-actual,
                       passed=actual < required))


text = (ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
source_rows = [tuple(map(int, row)) for row in
               re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', text, re.M)]
eq('independent table matches all source rows', source_rows,
   [(i,j,h) for i,(j,h) in enumerate(pairs)])

# Coefficients of a_i(t), so the entire interval is retained symbolically.
tails = [(2,0)]*22+[(20,0),(2,18),(166504394,-18)]
prefixes = []
for i in range(26):
    prefixes.append(dict(i=i,
        three=sum(3*j+h for j,h in pairs[:i]),
        two_constant=sum(4*pairs[k][0]+pairs[k][1]+tails[k][0] for k in range(i)),
        two_t_coefficient=sum(tails[k][1] for k in range(i))))
eq('all-prefix t coefficients', [p['two_t_coefficient'] for p in prefixes],
   [0]*24+[18,0])
eq('full closing exponents', prefixes[25],
   dict(i=25,three=397573379,two_constant=630138897,two_t_coefficient=0))
eq('sum J', sum(j for j,h in pairs), 66061058)
eq('sum H', sum(h for j,h in pairs), 199390205)
eq('total tail constant', sum(a for a,b in tails), 166504460)
for i, ((j,h),(a,b)) in enumerate(zip(pairs,tails)):
    eq(f'boundary row {i}', original['t1']['rows'][i], dict(i=i,J=j,H=h,a=a+b))
    p = prefixes[i]
    eq(f'boundary prefix {i}', original['t1']['prefixes'][i],
       dict(i=i,three_exponent=p['three'],two_exponent=p['two_constant']+p['two_t_coefficient']))
    eq(f'eta monotone hypotheses {i}', j >= 8 and h >= 40, True)
    for t in (1,9250244):
        eq(f'tail endpoint domain {i} at {t}', a+b*t >= 2 and (a+b*t)%18 == 2, True)
    if 1 <= i <= 23:
        eq(f'boundary growth hypotheses {i}', j >= 15 and h >= 72 and a+b <= 20, True)
    if i <= 22:
        eq(f'uniform fixed prefix tail {i}', b, 0)
eq('original closure', original['t1']['closing_exponents'], dict(three=397573379,two=630138897))
eq('upper-end changed tails', [a+b*9250244 for a,b in tails[-3:]], [20,166504394,2])

# Independent exact logarithms: geometric remainder, no rounded terms.
series = {}
def log_interval(argument):
    x = (argument-1)/(argument+1)
    terms = [2*x**(2*k+1)/(2*k+1) for k in range(128)]
    lower = sum(terms)
    remainder = 2*x**257/(257*(1-x*x))
    series[str(argument)] = dict(argument=argument,x=x,terms=terms,
                                lower=lower,remainder=remainder,upper=lower+remainder)
    return lower, lower+remainder

ell = log_interval(Q(2))
tau = log_interval(Q(3))
delta = log_interval(Q(11,4))
scale = 10**12
for name, bounds, lo, hi in [
    ('log2',ell,693147180559,693147180560),
    ('log3',tau,1098612288668,1098612288669),
    ('log(11/4)',delta,1011600911678,1011600911679),
]:
    lt(name+' lower grid', Q(lo,scale), bounds[0])
    lt(name+' upper grid', bounds[1], Q(hi,scale))
lmin,lmax = Q(10584,10**14),Q(10585,10**14)
lambda_bounds = (630138897*ell[0]-397573379*tau[1],
                 630138897*ell[1]-397573379*tau[0])
lt('Lambda lower independently checked', lmin, lambda_bounds[0])
lt('Lambda upper independently checked', lambda_bounds[1], lmax)

eta0 = Q(23,11)-Q(16,27)**8*(Q(12,11)+Q(2,3)**40)
n_lower = 2*(1-lmax)/lmax
bmax = Q(23,11)*(1+Q(2,10**8))
normalized = bmax/lmin+bmax+Q(23,11)
exp_terms = [Q(1)]
for k in range(1,41):
    exp_terms.append(exp_terms[-1]*24/k)
eq('all 41 exponential terms', list(map(Q,original['exp24_terms'])), exp_terms)
p = prefixes[24]['three']
q = prefixes[24]['two_constant']+prefixes[24]['two_t_coefficient']
gq = q+4*pairs[24][0]
operands = [24*scale,p*1098612288669,-gq*693147180559,1011600911679]
margin = Q(sum(operands),scale)
eq('all original guard operands', original['t1']['row24_guard']['operands'], operands)
eq('original guard complete record', original['t1']['row24_guard'],
   dict(index=24,three_exponent=p,combined_two_exponent=gq,operands=operands,
        margin_upper_scaled=sum(operands),margin_upper=str(margin),required_margin='>=0'))
eq('boundary B upper', Q(original['t1']['B_upper']), bmax)
eq('boundary normalized bound', Q(original['t1']['normalized_shifted_upper']), normalized)
expected = [(Q(2),eta0),(Q(0),lmin),(lmax,Q(1)),(Q(18*10**9),n_lower),
            (Q(540,11),n_lower+Q(23,11)),(Q(10**8),Q(3**64,2**74)),
            (Q(2),Q(3**117,2**152)),(normalized,Q(20*10**9)),
            (Q(20*10**9),sum(exp_terms)),(margin,Q(0)),(margin,Q(-379,100))]
eq('original rational check count', len(original['checks']),len(expected))
for i,(actual,required) in enumerate(expected):
    rec = original['checks'][i]
    eq(f'original check {i} operands', (Q(rec['actual']),Q(rec['required']),Q(rec['difference'])),
       (actual,required,required-actual))
    lt(f'independent rational check {i}',actual,required)

independent_margin = 24+p*tau[1]-gq*ell[0]+delta[1]
lt('independent boundary margin below grid bound', independent_margin,margin)
lt('required rejection', margin,Q(-379,100))
summary = dict(check_count=len(checks), failures=[c['name'] for c in checks if not c['passed']],
    verdict='No defect found in audited endpoint/domain/J scope',
    unshifted_lower=str(n_lower), required_shifted_domain='540/11',
    boundary_normalized_upper=str(normalized), required_normalized_upper='20000000000',
    boundary_prefix=[p,q,gq], guard_operands=operands,
    boundary_margin_upper=str(margin),required_guard_margin='>=0',
    checked_rejection_threshold='-379/100',
    lambda_enclosure=[str(lmin),str(lmax)], interval=[1,9250244])
result = dict(summary=summary,original_sha256=hashlib.sha256(raw).hexdigest(),
    checks=checks, affine_tail_coefficients=tails, all_prefix_exponents=prefixes,
    logarithm_series=series,lambda_bounds=lambda_bounds,
    independent_margin_upper=independent_margin,exp24_terms=exp_terms,
    scope='Finite operands checked independently; closure, positivity and uniform monotonicity are proved in L070 audit text.')
path = HERE/'two-recipient-tail-audit-certificate.json'
path.write_text(json.dumps(result,default=lambda x:str(x) if isinstance(x,Q) else x,indent=2)+'\n')
print(f"Checks: {len(checks)}; failures: {summary['failures']}")
print(f'All t: n_i > {n_lower} > 18000000000; required s_i >= 540/11')
print(f't=1 normalized shifted bound: {normalized} < 20000000000')
print(f'Row24 margin < {margin} < -379/100; required >=0')
print(f'Certificate: {path}')
assert not summary['failures']
