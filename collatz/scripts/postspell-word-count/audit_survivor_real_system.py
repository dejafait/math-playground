#!/usr/bin/env python3
"""Independent, exact audit of L065 only; never run/import its generator."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'survivor-remaining-real-guards-certificate.json'
raw = SOURCE.read_bytes()
old = json.loads(raw)
checks, log_evidence, margins = [], {}, []


def check(name, passed, **evidence):
    checks.append(dict(name=name, passed=bool(passed), **evidence))


def lt(name, a, b):
    a, b = Q(a), Q(b)
    check(name, a < b, actual=str(a), required=str(b),
          relation='<', margin=str(b-a))


def independent_log(t):
    """128 exact terms, direct arguments through 3, no dyadic rounding."""
    t = Q(t)
    if str(t) in log_evidence:
        r = log_evidence[str(t)]
        return Q(r['lower']), Q(r['upper'])
    u, k = t, 0
    while u > 3:
        u /= 2
        k += 1
    assert 1 <= u <= 3
    x = (u-1)/(u+1)
    p = sum((2*x**(2*m+1)/(2*m+1) for m in range(128)), Q(0))
    error = 2*x**257/(257*(1-x*x))
    lo, hi = p, p+error
    if k:
        el, eu = independent_log(2)
        lo, hi = lo+k*el, hi+k*eu
    log_evidence[str(t)] = dict(reduced_argument=str(u), binary_exponent=k,
        x=str(x), terms=128, exact_partial_sum=str(p), remainder_upper=str(error),
        lower=str(lo), upper=str(hi))
    return lo, hi


TABLE = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
    (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
    (8224,39104),(15494,73672),(29191,138802),(54998,261511),
    (103621,492705),(195229,928293),(367827,1748976),(693015,3295208),
    (1305695,6208431),(2460032,11697176),(4634896,22038409),
    (8732512,41522114),(16452748,78230965),(30998279,32670621)]
canonical = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
parsed = [tuple(map(int, x)) for x in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', canonical, re.M)]
check('independent table matches canonical', parsed == [(i,*r) for i,r in enumerate(TABLE)])
rows = [dict(i=i,J=j,H=h,a=20 if i == 23 else 166504394 if i == 24 else 2)
        for i,(j,h) in enumerate(TABLE)]
check('complete saved tuple', old['parameters'] == rows)
K = sum(3*j+h for j,h in TABLE)
N = sum(4*r['J']+r['H']+r['a'] for r in rows)
L = N-K
check('counts', (K,L,N) == (397573379,232565518,630138897))
check('saved counts and explicit scaling', old['counts'] == dict(K=K,L=L,N=N,d=1,K0=K,L0=L))
check('all parameter and congruence guards', all(r['J'] >= 2 and r['H'] >= 3 and r['a'] >= 2 and r['a'] % 18 == 2 for r in rows))
lt('primitive parameter threshold',225640000,K)
lt('positive L0',0,L)
length_margin = Q(8,5)*K+Q(69*25,1034)-N
lt('aggregate length margin',0,length_margin)
check('published length margin',length_margin == Q(30908902223,5170))

el,eu = independent_log(2)
tl,tu = independent_log(3)
dl,du = independent_log(Q(11,4))
lambda_lo,lambda_hi = N*el-K*tu,N*eu-K*tl
lm,lp = Q(10584,10**14),Q(10585,10**14)
lt('independent Lambda lower',lm,lambda_lo)
lt('independent Lambda upper',lambda_hi,lp)
lt('amplified Lambda interval width',lambda_hi-lambda_lo,Q(1,10**60))
lt('Lambda cap below one',lp,1)

# Verify precisely the inherited changed-tail bounds needed here.
eta0 = Q(23,11)-Q(12,11)*Q(16,27)**8-Q(16,27)**8*Q(2,3)**40
lt('eta0 lower',2,eta0)
lt('row zero worst tail growth',Q(10**8,2**18),Q(3**64,2**92))
lt('row zero growth baseline',2,Q(10**8,2**18))
lt('remaining growing edges baseline',2,Q(3**117,2**152))
check('all first 24 edges meet inherited growth hypotheses',
      all(r['J']>=15 and r['H']>=72 and r['a']<=20 for r in rows[1:24]) and rows[0]['a']<=20)
bmax = Q(23,11)*(1+Q(2*2**18,10**8))
lt('finite B envelope',Q(23,11)*(1+Q(2**18,10**8)*sum((Q(1,2**i) for i in range(24)),Q(0))),bmax)
root_lower = 2*(1-lp)/lp
norm_upper = bmax/lm+bmax+Q(23,11)
lt('root domain',18*10**9,root_lower)
lt('normalized upper',norm_upper,20*10**9)
lt('L051 domain',Q(540,11),18*10**9)
lo18,hi18 = independent_log(18*10**9)
lo20,hi20 = independent_log(20*10**9)
lt('normalized log lower',Q(2361,100),lo18)
lt('normalized log upper',hi20,24)
logN = independent_log(N)
log25 = independent_log(25)
seed_lo,seed_hi = [Q(133,10)*logN[i]+8+log25[i] for i in (0,1)]
lt('seed positive height',0,Q(2361,100))
lt('seed upper guard',24,seed_lo)
lt('seed cap above 280',280,seed_lo)

S=10**12
EL,EU,TL,TU=693147180559,693147180560,1098612288668,1098612288669
AL,AU,BL,BU=3*TL-4*EU,3*TU-4*EL,TL-EU,TU-EL
for name,a,b in [('ell grid lower',Q(EL,S),el),('ell grid upper',eu,Q(EU,S)),
                 ('tau grid lower',Q(TL,S),tl),('tau grid upper',tu,Q(TU,S))]:
    lt(name,a,b)
check('saved constants',old['constants']==dict(S=S,EL=EL,EU=EU,TL=TL,TU=TU,AL=AL,AU=AU,BL=BL,BU=BU))
expected_int = dict(exactly_approved_literal_tuple=len(rows)==25,
    moved_tail_only_at_23=all(r['a']==(20 if i==23 else 166504394 if i==24 else 2) for i,r in enumerate(rows)),
    parameter_domain=all(r['J']>=2 and r['H']>=3 and r['a']>=2 for r in rows),
    tail_congruences=all(r['a']%18==2 for r in rows),
    sum_J=sum(j for j,h in TABLE)==66061058,sum_H=sum(h for j,h in TABLE)==199390205,
    sum_a=sum(r['a'] for r in rows)==166504460,K_total=K==397573379,L_total=L==232565518,
    N_total=N==630138897,K_plus_L=K+L==N,explicit_scaling_d1=K>225640000 and L>0)
prefixes=[]
expected_guards=[]
for i,(j,h) in enumerate(TABLE):
    # Direct finite sums: no recurrence and no values read from the certificate.
    p=sum(3*r['J']+r['H'] for r in rows[:i])
    q=sum(4*r['J']+r['H']+r['a'] for r in rows[:i])
    prefixes.append(dict(i=i,three_exponent=p,two_exponent=q))
    v=2361*S//100+p*TL-q*EU
    w=24*S+p*TU-q*EL
    low,high=v+j*AL-h*EU,w+j*AU-h*EL
    expected_guards.append(dict(i=i,J=j,H=h,own_input=i,
        log_s_lower_scaled=v,log_s_upper_scaled=w,J_alpha_lower_scaled=j*AL,
        H_log2_upper_scaled=h*EU,margin_lower_scaled=low,margin_upper_scaled=high,verdict='PASS_STRICT'))
    Hlo=Q(2361,100)+(p+3*j)*tl-(q+4*j+h)*eu
    Hhi=24+(p+3*j)*tu-(q+4*j+h)*el
    Jlo=Q(2361,100)+p*tl-(q+4*j)*eu+dl
    Jhi=24+p*tu-(q+4*j)*el+du
    lt(f'independent H {i}',0,Hlo)
    lt(f'independent J {i}',0,Jlo)
    lt(f'published H lower {i}',0,Q(low,S))
    lt(f'independent H refines published lower {i}',Q(low,S),Hlo)
    lt(f'independent H error budget {i}',
       (p+3*j)*(tu-tl)+(q+4*j+h)*(eu-el),Q(1,10**60))
    margins.append(dict(i=i,p=p,q=q,H_lower=str(Hlo),H_upper=str(Hhi),
        J_lower=str(Jlo),J_upper=str(Jhi),published_H_lower_scaled=low))
    expected_int[f'prefix_lower_identity_{i}']=v==2361*S//100+p*TL-q*EU
    expected_int[f'prefix_upper_identity_{i}']=w==24*S+p*TU-q*EL
expected_int['closing_exponents']=(K,N)==(397573379,630138897)
check('all 25 complete H records',old['H_guards']==expected_guards)
check('all prefix records',old['prefixes']==prefixes)
check('closing exponents',old['closing_exponents']==dict(three=K,two=N))
check('all 63 integer checks reconstructed',old['integer_checks']==expected_int and all(expected_int.values()))
published = [70097927712,570420269452,53436522780,496444359460,243194644024,
    296420192316,267360955140,357237954752,638069930720,305365679840,
    444535689244,220290618028,636585593476,136430507056,322103147984,
    548337798856,465906922552,188606219424,6289114252,664232490696,
    480571431372,56750531324,64953570744,399111636848,79519729152858484664]
check('all 25 published numerators',published==[g['margin_lower_scaled'] for g in expected_guards])

# Full reconstruction of the ORIGINAL rounded certificates and their errors.
def original_base(t,record,label):
    t=Q(t)
    x=(t-1)/(t+1)
    check(label+' domain and argument',0<=x<=Q(1,3) and record['argument']==str(t) and record['x']==str(x))
    check(label+' term count',len(record['rounded_summands'])==96)
    for m,z in enumerate(record['rounded_summands']):
        exact=2*x**(2*m+1)/(2*m+1)*2**192
        check(f'{label} floor {m}',Q(z)<=exact<Q(z+1),rounded=z)
    budget=Q(96,2**192)
    remainder=Q(9,4*193*3**193)
    check(label+' exact budgets',Q(record['rounding_budget'])==budget and Q(record['remainder_upper'])==remainder)
    check(label+' valid integrated remainder envelope',2*x**193/(193*(1-x*x))<=remainder)
    a=Q(sum(record['rounded_summands']),2**192)
    return a,a+budget+remainder

oe=original_base(2,old['log2_detail'],'original log2 base')
original_logs={}
expected_args=[2,3,18*10**9,20*10**9,N,25]
check('complete original log arguments',set(old['logs'])==set(map(str,expected_args)))
for t in expected_args:
    r=old['logs'][str(t)]
    u,k=Q(t),0
    while u>=2:
        u/=2
        k+=1
    check(f'original reduction {t}',r['binary_exponent']==k and r['reduced_argument']==str(u))
    base=original_base(u,r['detail'],f'original log {t}')
    lo,hi=base[0]+k*oe[0],base[1]+k*oe[1]
    check(f'original final interval {t}',(Q(r['lower']),Q(r['upper']))==(lo,hi))
    il,iu=independent_log(t)
    check(f'independent interval refines original {t}',lo<il and iu<hi)
    original_logs[t]=(lo,hi)

l2,u2=original_logs[2]
l3,u3=original_logs[3]
oseed=[Q(133,10)*original_logs[N][i]+8+original_logs[25][i] for i in (0,1)]
expected_checks=[('log2 grid lower',Q(EL,S),l2),('log2 grid upper',u2,Q(EU,S)),
    ('log3 grid lower',Q(TL,S),l3),('log3 grid upper',u3,Q(TU,S)),
    ('positive alpha grid lower',0,AL),('positive beta grid lower',0,BL),
    ('Lambda lower',lm,N*l2-K*u3),('Lambda upper',N*u2-K*l3,lp),
    ('Lambda upper below one',lp,1),('aggregate length inequality',N,Q(8,5)*K+Q(1725,1034)),
    ('L064 root lower exceeds 18 billion',18*10**9,root_lower),
    ('L064 normalized shifted upper below 20 billion',norm_upper,20*10**9),
    ('domain from root lower',Q(540,11),18*10**9),
    ('height lower exceeds 23.61',Q(2361,100),original_logs[18*10**9][0]),
    ('initial height upper below 24',original_logs[20*10**9][1],24),
    ('seed upper cap strictly exceeds 24',24,oseed[0]),
    ('seed positivity from L064 height lower',0,Q(2361,100))]
expected_checks += [(f'own-input strict H guard {g["i"]}',g['H_log2_upper_scaled'],
    g['log_s_lower_scaled']+g['J_alpha_lower_scaled']) for g in expected_guards]
check('original rational check count',len(old['checks'])==len(expected_checks)==42)
for r,(name,a,b) in zip(old['checks'],expected_checks):
    a,b=Q(a),Q(b)
    check('original comparison '+name,r==dict(name=name,actual=str(a),required=str(b),
        relation='<',margin=str(b-a),passed=a<b) and a<b)
check('original seed record',old['seed']==dict(height_lower='23.61',height_upper='24',
    cap_lower=str(oseed[0]),cap_upper=str(oseed[1])))
check('original imported bounds',old['imported_bounds']==dict(B_upper=str(bmax),root_lower=str(root_lower),
    normalized_shifted_upper=str(norm_upper),lambda_lower=str(lm),lambda_upper=str(lp),
    height='23.61+log C_i < log s_i < 24+log C_i'))
weak=min(expected_guards,key=lambda r:r['margin_lower_scaled'])
check('claimed smallest margin',weak['i']==18 and weak['margin_lower_scaled']==6289114252)
check('original summary',old['summary']==dict(H_guards_pass=25,required_H_guards=25,
    weakest_H_index=18,weakest_H_margin_lower=str(Q(6289114252,S)),seed_height_lower='23.61',
    seed_height_upper='24',seed_cap_lower=str(oseed[0]),seed_cap_lower_floor=oseed[0].__floor__(),
    seed_margin_lower=str(oseed[0]-24),rational_checks=42,integer_checks=63,failures=[],unresolved_H_indices=[]))
check('original overall verdict',old['failures']==[] and old['verdict']=='ALL_REMAINING_REAL_GUARDS_PASS')
failures=[c['name'] for c in checks if not c['passed']]
summary=dict(check_count=len(checks),failures=failures,H_pass=25,J_pass=25,
    published_H_lower_numerators=published,scale=S,weakest_H_index=18,
    weakest_H_margin_lower=str(Q(6289114252,S)),seed_cap_lower_floor=seed_lo.__floor__(),
    seed_required_height_upper=24,root_lower=str(root_lower),normalized_upper=str(norm_upper),
    lambda_lower_guard=str(lm),lambda_upper_guard=str(lp),length_margin=str(length_margin),
    complete_original_rational_checks=42,complete_original_integer_checks=63,
    original_rounded_terms_checked=7*96,independent_log_error_after_amplification_below='1/10^60',
    symbolic_assembly='L064 coordinate substitution, finite affine composition and closing product checked in L065 audit text')
result=dict(target='Independent L065 fixed j=23 full real-system audit',
    original_sha256=hashlib.sha256(raw).hexdigest(),rows=rows,counts=dict(K=K,L=L,N=N),
    independent_logs=log_evidence,margins=margins,checks=checks,
    independent_lambda=dict(lower=str(lambda_lo),upper=str(lambda_hi)),
    independent_seed=dict(lower=str(seed_lo),upper=str(seed_hi)),summary=summary,
    limitations='No integer/parity/residue/exact-valuation or primitive realization; no additional tuple or modulus tested.')
out=HERE/'survivor-real-system-audit-certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(f'Checks: {len(checks)}; failures={failures}; H=25/25; J=25/25')
print('Smallest published H lower margin: 6289114252/10^12 > required 0 at i=18')
print(f'Seed: h0 < 24 < {seed_lo.__floor__()} < required cap; amplified log errors < 10^-60')
print(f'Full certificate: {out}')
assert not failures
