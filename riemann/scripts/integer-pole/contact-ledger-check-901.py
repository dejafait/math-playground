#!/usr/bin/env python3
"""Read EVERY compact enclosure and verify its interval coverage and signs.

This checks the saved ledger, not the analytic enclosure formulas or sources.
"""
import json
from fractions import Fraction as R
from pathlib import Path

SOURCE=Path(__file__).with_name('contact-certificate-901.json')
OUT=Path(__file__).with_suffix('.json')
d=json.loads(SOURCE.read_text())
S=2**d['bits']
fail=[]
def check(ok,msg):
    if not ok:
        fail.append(msg)
def bounds(row,key):
    a,b=map(int,row[key])
    check(a<=b,'reversed interval '+key)
    return R(a,S),R(b,S)

check((d['bits'],d['N'],d['K'])==(512,128,12),'parameters')
domains=[('prefix',R(1,4),R(177,32)),('contact',R(177,32),R(89,16)),
         ('lower',R(89,16),R(179,32))]
check(len(d['cells'])==189,'unexpected cell count')
counts={}
for mode,left,right in domains:
    rows=[r for r in d['cells'] if r['mode']==mode]
    counts[mode]=len(rows)
    cursor=left
    for i,row in enumerate(rows):
        a,b=R(row['left']),R(row['right'])
        check(a==cursor and a<b<=right,f'{mode} coverage cell{i}')
        cursor=b
        p=bounds(row,'Q')
        d2=bounds(row,'D2_Q')
        d3=bounds(row,'D3_Q')
        dp=bounds(row,'D3_Q_prime')
        check(p[0]>0,f'{mode} Q cell{i}')
        check(d2[0]>R(1,50000),f'{mode} D2 cell{i}')
        if mode=='prefix':
            check(d3[0]>R(1,50000),f'prefix D3 cell{i}')
        if mode=='contact':
            check(dp[1]<-R(1,200),f'contact derivative cell{i}')
    check(cursor==right,mode+' final endpoint')
check(sum(counts.values())==len(d['cells']),'unrecognized cell modes')
for row,x,sign in zip(d['endpoints'],[R(177,32),R(89,16)],[1,-1]):
    check(R(row['x'])==x,'endpoint x')
    a,b=bounds(row,'D3_Q')
    check(a>0 if sign==1 else b<0,'endpoint sign')
maxerror=max(R(int(v[1]),S) for v in d['true_law_error'])
maxtail=max(R(int(v[1]),S) for v in d['omitted_finite_modes'])
check(maxerror<R(1,10**20),'true law error exceeds reported coarse bound')
check(maxtail<R(1,10**100),'finite-mode error exceeds reported coarse bound')
check(len(d['true_law_error'])==8 and len(d['omitted_finite_modes'])==8,'jet count')
report=dict(status='PASS' if not fail else 'FAIL',source=str(SOURCE),
    checked_all_cells=len(d['cells']),counts=counts,failures=fail,
    required=dict(D2_Q_lower='>1/50000',prefix_D3_Q_lower='>1/50000',
                  contact_D3_Q_prime_upper='<-1/200',
                  max_true_law_error='<1e-20',max_omitted_mode_error='<1e-100'),
    maximum_true_law_error=str(maxerror),maximum_omitted_mode_error=str(maxtail),
    qualification='Ledger validation only; independent conceptual and arithmetic audit pending.')
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(report['status'],'all',len(d['cells']),'cells;',counts,'failures:',fail)
print('Actual errors below required 1e-20 and 1e-100:',maxerror<R(1,10**20),maxtail<R(1,10**100))
print('Full ledger check:',OUT)
