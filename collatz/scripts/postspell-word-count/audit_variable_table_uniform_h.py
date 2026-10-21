#!/usr/bin/env python3
"""Independent complete finite-operand audit of L083 (not its universal proof).

Read the constructor's certificate without importing or executing its code.
Reconstruct all mathematical fields, including every stored comparison.
The quantified argument and analytic remainder justification are in L083.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'variable-table-uniform-h-certificate.json'
raw = SOURCE.read_bytes()
old = json.loads(raw)
pairs = [
    (8,40), (15,72), (28,134), (52,249), (98,467), (184,877),
    (347,1650), (653,3106), (1230,5849), (2317,11018),
    (4365,20756), (8224,39104), (15494,73672), (29191,138802),
    (54998,261511), (103621,492705), (195229,928293),
    (367827,1748976), (693015,3295208), (1305695,6208431),
    (2460032,11697176), (4634896,22038409), (8732512,41522114),
    (16452748,78230965), (30998279,32670621),
]
checks, comparisons = [], []


def verify(name, passed, **evidence):
    checks.append(dict(name=name, passed=bool(passed), **evidence))


def normalized(value):
    return json.loads(json.dumps(value, default=str))


def match(path, actual, required):
    """Traverse every leaf, including all long analytic evidence arrays."""
    required = normalized(required)
    if isinstance(required, dict) and isinstance(actual, dict):
        verify(path+' keys', set(actual) == set(required),
               actual=sorted(actual), required=sorted(required))
        for k, v in required.items():
            match(path+'/'+k, actual.get(k), v)
    elif isinstance(required, list) and isinstance(actual, list):
        verify(path+' length', len(actual) == len(required),
               actual=len(actual), required=len(required))
        for i, v in enumerate(required):
            match(path+'/'+str(i), actual[i] if i < len(actual) else None, v)
    else:
        verify(path, actual == required, actual=actual, required=required)


def compare(name, actual, relation, required):
    a, b = F(actual), F(required)
    ok = {'<': a < b, '>': a > b, '=': a == b,
          '<=': a <= b, '>=': a >= b}[relation]
    item = dict(name=name, actual=a, relation=relation, required=b,
                difference=a-b, passed=ok)
    comparisons.append(item)
    verify('fresh '+name, ok, actual=a, relation=relation, required=b,
           difference=a-b)


def logarithm(x, count):
    z = (x-1)/(x+1)
    verify('analytic domain '+str(x), 0 < z < 1, actual=z, required='0<z<1')
    power = z
    terms = []
    for k in range(count):
        terms.append(2*power/(2*k+1))
        power *= z*z
    rem = 2*power/((2*count+1)*(1-z*z))
    low = sum(terms, F(0))
    return dict(argument=x, z=z, terms=terms, remainder_upper=rem,
                lower=low, upper=low+rem)


source_path = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
source_raw = source_path.read_bytes()
source_rows = [tuple(map(int, r)) for r in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', source_raw.decode(), re.M)]
match('independently transcribed table', normalized(source_rows),
      [(i,j,h) for i,(j,h) in enumerate(pairs)])
match('source', old['source'], dict(path=str(source_path.relative_to(ROOT)),
      sha256=hashlib.sha256(source_raw).hexdigest()))
match('parameters', old['parameters'], dict(r=25,B=9250245,tau=2,m=1,survivors=[0,1]))
logs = {str(x): logarithm(F(x),100) for x in (2,3)}
match('logs', old['logs'], logs)
lm, lp = F(10584,10**14), F(10585,10**14)
ell, u, kap = F(693147180559,10**12), F(1098612288669,10**12), F(23,11)
compare('log2 lower grid', ell, '<', logs['2']['lower'])
compare('log3 upper grid', logs['3']['upper'], '<', u)
exp_terms = [F(1)]
for k in range(1,41):
    exp_terms.append(exp_terms[-1]*24/k)
exp_low = sum(exp_terms,F(0))
match('exp24_terms',old['exp24_terms'],exp_terms)
match('exp24_partial_sum',old['exp24_partial_sum'],exp_low)
compare('exp24 partial sum exceeds U',20*10**9,'<',exp_low)
lowers = [F(1)] + [F(10**8*2**k) for k in range(24)]
reciprocal = 1+F(2,10**8)*(1-F(1,2**24))
verify('complete geometric sum',reciprocal==sum(1/x for x in lowers),
       actual=reciprocal,required=sum(1/x for x in lowers))
qcap, wcap = kap*(1+F(2,10**8)), kap
cap = qcap/lm+qcap+wcap
match('certificate_constants',old['certificate_constants'],dict(
    lambda_lower=lm,lambda_upper=lp,ell=ell,u=u,T=24,U=20*10**9,
    incoming_L=lowers,Q=qcap,W=wcap))
match('full_reciprocal_sum',old['full_reciprocal_sum'],reciprocal)
match('normalized_cap',old['normalized_cap'],cap)
compare('full incoming reciprocal cap',kap*reciprocal,'<',qcap)
compare('normalized cap below U',cap,'<',20*10**9)
floors = dict(tail2=F(3**9,2**13),tail20=F(3**63,2**91))
match('multiplier_floor',old['multiplier_floor'],floors)
compare('tail2 multiplier floor',floors['tail2'],'>',2)
compare('tail20 multiplier floor',floors['tail20'],'>',2)
tables = {}
for name in ('changed','original'):
    table = [(j,h-(i==0)+(i==24)) if name=='changed' else (j,h)
             for i,(j,h) in enumerate(pairs)]
    verify(name+' table domain',all(j>=2 and h>=3 for j,h in table)
           and all(table[i][0]<table[i+1][0] for i in range(24)),rows=table)
    tails0 = [2]*24+[2+18*9250245]
    tails1 = [2]*23+[20,2+18*(9250245-1)]
    odd = [3*j+h for j,h in table]
    ds = [[4*j+h+a for (j,h),a in zip(table,t)] for t in (tails0,tails1)]
    K,N = sum(odd),sum(ds[0])
    compare(name+' K',K,'=',397573379)
    compare(name+' N',N,'=',630138897)
    lo = N*logs['2']['lower']-K*logs['3']['upper']
    hi = N*logs['2']['upper']-K*logs['3']['lower']
    compare(name+' Lambda lower',lm,'<',lo)
    compare(name+' Lambda upper',hi,'<',lp)
    compare(name+' positive lower',lm,'>',0)
    compare(name+' upper below one',lp,'<',1)
    c0 = F(3**odd[0],2**ds[0][0])
    compare(name+' row0 c0',c0,'>',10**8)
    for i,(j,h) in enumerate(table[1:23],1):
        compare(f'{name} row{i} J tail2 floor',j,'>=',2)
        compare(f'{name} row{i} H tail2 floor',h,'>=',3)
    compare(name+' row23 J tail20 floor',table[23][0],'>=',8)
    compare(name+' row23 H tail20 floor',table[23][1],'>=',39)
    prefixes = []
    for i,(j,h) in enumerate(table):
        A,D0,D1 = sum(odd[:i]),sum(ds[0][:i]),sum(ds[1][:i])
        pos,neg = A+3*j,D0+4*j+h
        margin = 24+pos*u-neg*ell
        prefixes.append(dict(i=i,A=A,D_at_0=D0,D_at_m=D1,L=lowers[i],
            H_log3_coefficient=pos,H_negative_log2_coefficient=neg,
            uniform_H_margin_strict_upper=margin))
        verify(f'{name} incoming direction {i}',D1-D0==(18 if i==24 else 0),
               actual=D1-D0,required=18 if i==24 else 0)
        verify(f'{name} positive margin coefficients {i}',pos>0 and neg>0,
               actual=[pos,neg],required='both positive')
        if name=='original':
            compare(f'original row{i} sufficient rejection test fails',margin,'>',0)
    compare(name+' complete closing odd exponent',sum(odd),'=',K)
    compare(name+' closing exponent at t0',sum(ds[0]),'=',N)
    compare(name+' closing exponent at t1',sum(ds[1]),'=',N)
    if name=='changed':
        compare('changed row18 uniform rejection',prefixes[18]['uniform_H_margin_strict_upper'],'<',0)
        compare('changed row18 bound matches C082a',prefixes[18]['uniform_H_margin_strict_upper'],
                '=',-F(457745289,50000000000))
    tables[name] = dict(rows=[dict(i=i,J=j,H=h) for i,(j,h) in enumerate(table)],
        counts=dict(K=K,N=N),Lambda_interval=[lo,hi],row0_multiplier=c0,
        incoming_prefixes=prefixes,row18=prefixes[18],
        rejected_rows=[x['i'] for x in prefixes if x['uniform_H_margin_strict_upper']<=0])
match('tables',old['tables'],tables)
match('checks',old['checks'],comparisons)
match('failures',old['failures'],[])
match('summary',old['summary'],dict(checks=len(comparisons),failures=[],
    changed_row18_upper=tables['changed']['row18']['uniform_H_margin_strict_upper'],
    required_rejection_upper=0,original_rejected_rows=tables['original']['rejected_rows']))

# Independent smaller-z evaluation of Lambda via log3=log2+log(3/2).
alt2,alt32 = logarithm(F(2),120),logarithm(F(3,2),120)
alt_lo = (630138897-397573379)*alt2['lower']-397573379*alt32['upper']
alt_hi = (630138897-397573379)*alt2['upper']-397573379*alt32['lower']
verify('alternative Lambda enclosed',lm<alt_lo<alt_hi<lp,
       actual=[alt_lo,alt_hi],required=[lm,lp])
verify('alternative Lambda refines construction',
       tables['changed']['Lambda_interval'][0]<alt_lo<alt_hi<tables['changed']['Lambda_interval'][1],
       actual=[alt_lo,alt_hi],required=tables['changed']['Lambda_interval'])
failures = [x['name'] for x in checks if not x['passed']]
out = HERE / 'variable-table-uniform-h-audit-certificate.json'
out.write_text(json.dumps(dict(source_sha256=hashlib.sha256(raw).hexdigest(),
    source=str(SOURCE.relative_to(ROOT)),checks=checks,
    reconstructed=dict(logs=logs,exp_terms=exp_terms,tables=tables,comparisons=comparisons),
    alternative_analytic=dict(log2=alt2,log3over2=alt32,Lambda=[alt_lo,alt_hi]),
    summary=dict(checks=len(checks),constructor_comparisons=len(comparisons),failures=failures,
        normalized_cap=cap,required_cap=20*10**9,
        changed_row18=tables['changed']['row18']['uniform_H_margin_strict_upper'],
        required_H_margin='>0',original_rejected_rows=tables['original']['rejected_rows']),
    limitations='Universal proof and both cyclic cuts audited in L083; O/S/C imported from audited L079. No new table or realization.'),
    indent=2,default=str)+'\n')
print(f'Audit: {len(checks)} checks; {len(comparisons)} reconstructed comparisons; failures={failures}')
print(f'Normalized cap {cap} < required 20000000000 < exp(24).')
print('Changed row18 H margin < -457745289/50000000000; required >0.')
print(f"Original rejection rows: {tables['original']['rejected_rows']}; certificate: {out.relative_to(ROOT)}")
assert not failures
