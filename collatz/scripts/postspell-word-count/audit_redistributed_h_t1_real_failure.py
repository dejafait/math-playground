#!/usr/bin/env python3
"""Independent exact reconstruction for the single L082 critical audit.

Does not import or execute the calculation script. Reconstructs every
stored numeric comparison, and uses 120-term analytic bounds independently.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'redistributed-h-t1-real-feasibility-certificate.json'
old = json.loads(SOURCE.read_text())
table = [
    (8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
    (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
    (8224,39104),(15494,73672),(29191,138802),(54998,261511),
    (103621,492705),(195229,928293),(367827,1748976),
    (693015,3295208),(1305695,6208431),(2460032,11697176),
    (4634896,22038409),(8732512,41522114),(16452748,78230965),
    (30998279,32670621)]
evidence = []


def verify(name, condition):
    evidence.append({'name': name, 'passed': bool(condition)})


raw = (ROOT / old['source']['path']).read_bytes()
parsed = [(int(i), int(j), int(h)) for i,j,h in
          re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', raw.decode(), re.M)]
verify('independently transcribed full L055 table',
       parsed == [(i,j,h) for i,(j,h) in enumerate(table)])
verify('source digest', old['source']['sha256'] == hashlib.sha256(raw).hexdigest())
table[0] = (8,39)
table[24] = (30998279,32670622)
tails = [2]*23+[20,166504394]
rows = [dict(i=i,J=j,H=h,a=tails[i]) for i,(j,h) in enumerate(table)]
verify('all changed parameters', old['parameters'] == rows)
sj, sh, sa = sum(j for j,h in table), sum(h for j,h in table), sum(tails)
K, L = 3*sj+sh, sj+sa
N = K+L
verify('all aggregate count fields', old['counts'] == dict(K=K,L=L,N=N,d=1,K0=K,L0=L))
kap, lm, lp = F(23,11), F(10584,10**14), F(10585,10**14)


def series(base, size):
    # Recurrence for odd powers, independently of direct-power generation.
    z = F(base-1, base+1)
    power, terms = z, []
    for k in range(size):
        terms.append(2*power/(2*k+1))
        power *= z*z
    remainder = 2*power/F(2*size+1)/(1-z*z)
    low = sum(terms, F(0))
    return dict(argument=F(base),z=z,terms=terms,remainder_upper=remainder,
                lower=low,upper=low+remainder)


logs = {str(b):series(b,100) for b in (2,3)}
for b, data in logs.items():
    for key, value in data.items():
        got = old['logs'][b][key]
        verify(f'complete log{b} {key}',
               [F(v) for v in got] == value if isinstance(value,list) else F(got) == value)
l2,u2,l3,u3 = (logs[b][k] for b,k in [('2','lower'),('2','upper'),('3','lower'),('3','upper')])
lo,hi = N*l2-K*u3,N*u2-K*l3
verify('both complete amplified Lambda endpoints', list(map(F,old['lambda_interval'])) == [lo,hi])
prefixes, a, d = [],0,0
for i,(j,h) in enumerate(table):
    prefixes.append(dict(i=i,three_exponent=a,two_exponent=d,
                         product_lower=F(1 if i==0 else 10**8*2**(i-1))))
    a += 3*j+h
    d += 4*j+h+tails[i]
verify('all input prefix fields', all(
    all(F(p[k]) == v for k,v in expected.items())
    for p,expected in zip(old['prefixes'],prefixes)) and len(old['prefixes'])==25)
verify('closing exponents independently summed', (a,d)==(K,N))
rp = kap*(1+F(2,10**8))
cap = rp/lm+rp+kap
for key,value in [('lambda_lower',lm),('lambda_upper',lp),('R_upper',rp),
                  ('normalized_shifted_upper',cap)]:
    verify('root '+key,F(old['root'][key])==value)
expterms, term = [], F(1)
for k in range(41):
    expterms.append(term)
    term *= F(24,k+1)
verify('all exp24 terms',list(map(F,old['exp24_terms']))==expterms)
scale=10**12
el,eu,tl,tu = 693147180559,693147180560,1098612288668,1098612288669
A = prefixes[18]['three_exponent']+3*table[18][0]
D = prefixes[18]['two_exponent']+4*table[18][0]+table[18][1]
margin = 24+F(A*tu-D*el,scale)
guard = old['failed_necessary_guard']
for key,val in dict(i=18,J=table[18][0],H=table[18][1],own_input=18,
                    prefix_three=prefixes[18]['three_exponent'],
                    prefix_two=prefixes[18]['two_exponent'],
                    log3_coefficient=A,log2_negative_coefficient=D,
                    margin_strict_upper=margin).items():
    verify('own-input guard '+key,F(guard[key])==val)

# Independently specify the operands of every original comparison.
expected={}
def comparison(name,x,op,y):
    expected[name]=(F(x),op,F(y))

for name,x,y in [('sum J',sj,66061058),('sum H',sh,199390205),
                 ('sum tails',sa,166504460),('K',K,397573379),
                 ('L',L,232565518),('N',N,630138897)]:
    comparison(name,x,'=',y)
for i,(j,h) in enumerate(table):
    for key,x,op,y in [('J domain',j,'>=',2),('H domain',h,'>=',3),
                       ('tail domain',tails[i],'>=',2),('tail congruence',tails[i]%18,'=',2)]:
        comparison(f'row {i} {key}',x,op,y)
for name,x,op,y in [
    ('explicit d=1 odd count threshold',K,'>',225640000),
    ('explicit d=1 even count positive',L,'>',0),
    ('aggregate length inequality',N,'<',F(8,5)*K+F(1725,1034)),
    ('fresh Lambda lower',lm,'<',lo),('fresh Lambda upper',hi,'<',lp),
    ('positive Lambda lower',lm,'>',0),('Lambda upper below one',lp,'<',1),
    ('every eta positive from parameter floors',F(16,27)**2*(F(12,11)+F(2,3)**3),'<',kap),
    ('fresh changed row0 c0',F(3**63,2**73),'>',10**8),
    ('incoming rows 1..22 c_i floor',F(19683,8192),'>',2),
    ('row23 tail20 multiplier floor',F(3**63,2**91),'>',2),
    ('row23 J for tail20 floor',table[23][0],'>=',8),
    ('row23 H for tail20 floor',table[23][1],'>=',39),
    ('closing product odd exponent',a,'=',K),
    ('closing product denominator exponent',d,'=',N),
    ('full inverse prefix bound',kap*sum(1/p['product_lower'] for p in prefixes),'<',rp),
    ('fresh all-input normalized shifted root cap',cap,'<',20*10**9),
    ('exp24 strict partial-sum bound',20*10**9,'<',sum(expterms)),
    ('log2 grid lower',F(el,scale),'<',l2),('log2 grid upper',u2,'<',F(eu,scale)),
    ('log3 grid lower',F(tl,scale),'<',l3),('log3 grid upper',u3,'<',F(tu,scale)),
    ('own-input row18 H margin upper strictly negative',margin,'<',0)]:
    comparison(name,x,op,y)
for i in range(24):
    comparison(f'incoming row {i} exact tail',tails[i],'=',2 if i<23 else 20)
verify('complete comparison name set with no duplicates',
       len(old['checks'])==len(expected)==len({c['name'] for c in old['checks']})
       and {c['name'] for c in old['checks']}==set(expected))
relations={'<':lambda x,y:x<y,'>':lambda x,y:x>y,'=':lambda x,y:x==y,
           '<=':lambda x,y:x<=y,'>=':lambda x,y:x>=y}
reconstructed=[]
for c in old['checks']:
    x,op,y=expected[c['name']]
    passed=relations[op](x,y)
    verify('reconstruct '+c['name'], F(c['actual'])==x and F(c['required'])==y
           and c['relation']==op and F(c['difference'])==x-y and c['passed']==passed and passed)
    reconstructed.append(dict(name=c['name'],actual=x,relation=op,required=y,difference=x-y,passed=passed))

# Separate higher-order evaluation, retaining its full terms and error budgets.
fresh={str(b):series(b,120) for b in (2,3)}
fresh_lo=N*fresh['2']['lower']-K*fresh['3']['upper']
fresh_hi=N*fresh['2']['upper']-K*fresh['3']['lower']
fresh_margin=24+A*fresh['3']['upper']-D*fresh['2']['lower']
verify('independent 120-term Lambda enclosure',lm<fresh_lo<fresh_hi<lp)
verify('independent 120-term strict negative guard cap',fresh_margin<margin<0)
verify('printed root cap equality',cap==F(435606069410390910013,22050000000))
verify('printed row18 margin equality',margin==F(-457745289,50000000000))
verify('printed C18/C24',[(prefixes[i]['three_exponent'],prefixes[i]['two_exponent'])
                         for i in (18,24)]==[(6078923,6862840),(271907920,306970765)])
verify('source failures/summary consistent',old['failures']==[] and old['summary']==dict(
    certification_checks=153,failures=[],guard_index=18,
    margin_strict_upper=str(margin),required_margin_lower=0,all_other_guards_tested=False))
failures=[v['name'] for v in evidence if not v['passed']]
result=dict(source=str(SOURCE.relative_to(ROOT)),source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            verdict='NO_DEFECT_FOUND' if not failures else 'AUDIT_FAILURE',
            rows=rows,counts=dict(K=K,L=L,N=N),prefixes=prefixes,
            reconstructed_comparisons=reconstructed,independent_logs=fresh,
            independent_lambda_interval=[fresh_lo,fresh_hi],independent_margin_upper=fresh_margin,
            amplified_error_widths=dict(Lambda=N*(fresh['2']['upper']-fresh['2']['lower'])+
                                       K*(fresh['3']['upper']-fresh['3']['lower']),
                                       margin=A*(fresh['3']['upper']-fresh['3']['lower'])+
                                       D*(fresh['2']['upper']-fresh['2']['lower'])),
            root_cap=cap,exp24_terms=expterms,evidence=evidence,failures=failures,
            summary=dict(checks=len(evidence),reconstructed_comparisons=len(reconstructed),
                         required_H_margin='>0',certified_strict_upper=margin))
dest=HERE/'redistributed-h-t1-critical-audit-certificate.json'
dest.write_text(json.dumps(result,indent=2,default=str)+'\n')
print(f"Verdict: {result['verdict']}; {len(evidence)} audit checks, {len(reconstructed)} reconstructed comparisons")
print(f'Own-input H margin < {margin}; required > 0')
print(f'Normalized shifted root < {cap} < 20000000000 < exp(24)')
print(f'Lambda: {lm} < independently enclosed value < {lp}; failures: {failures}')
print(f'Certificate: {dest.relative_to(ROOT)}')
assert not failures
