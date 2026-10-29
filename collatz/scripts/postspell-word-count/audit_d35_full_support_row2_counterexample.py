#!/usr/bin/env python3
"""Independent exact L106 audit: no construction-code imports or giant powers.

Laurent monomials are represented by (p,q), meaning 3**p / 2**q.
Eta symbols are independent; polynomial endpoint checks are stronger than
needed after substitution. L104's already audited log enclosure is imported.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
base = [(8,40),(15,72),(28,134),(52,249),(98,467),(184,877),
        (347,1650),(653,3106),(1230,5849),(2317,11018),(4365,20756),
        (8224,39104),(15494,73672),(29191,138802),(54998,261511),
        (103621,492705),(195229,928293),(367827,1748976),
        (693015,3295208),(1305695,6208431),(2460032,11697176),
        (4634896,22038409),(8732512,41522114),(16452748,78230965),
        (30998279,32670621)]
old = json.loads((HERE/'d35-full-support-row2-counterexample-certificate.json').read_text())
checks=[]
def ck(name, actual, expected):
    checks.append(dict(name=name, actual=actual, required=expected, passed=actual==expected))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def neg(x): return (-x[0],-x[1])
read = [tuple(map(int,r)) for r in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', (ROOT/'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(),re.M)]
ck('independent literal transcription', read, [(i,j,h) for i,(j,h) in enumerate(base)])
rows=[]
for i,(j,h) in enumerate(base):
    h += -35 if i==0 else 35 if i==24 else 0
    b={0:1,1:1,2:12,24:9250231}.get(i,0)
    a=18*b+2
    row=dict(i=i,J=j,H=h,b=b,a=a,p=3*j+h,q=4*j+h+a,
             eta=f'23/11-(12/11)*(16/27)^{j}-(16/27)^{j}*(2/3)^{h}')
    rows.append(row)
    ck(f'complete original row{i}',old['rows'][i],row)
    ck(f'eta lower hypotheses row{i}',j>=8 and h>0,True)
    ck(f'integer tail domain row{i}',b>=0 and a>=2 and a%18==2,True)
c=[(r['p'],r['q']) for r in rows]
C=[(0,0)]
for x in c: C.append(add(C[-1],x))
K,N=C[-1]
ck('totals', [sum(r['J'] for r in rows),sum(r['H'] for r in rows),sum(r['b'] for r in rows),sum(r['a'] for r in rows),K,N], [66061058,199390205,9250245,166504460,397573379,630138897])
ck('certificate totals',[old['K'],old['N']],[K,N])
ck('literal last tail',rows[24]['a'],166504160)
# Each B[i][j] is the reciprocal-prefix coefficient of eta_j at cut i.
Bs=[]
cut_records=[]
for i in range(25):
    coeff={}
    records=[]
    order=[(i+k)%25 for k in range(25)]
    for k,j in enumerate(order):
        # Direct subset sum rather than the construction's running prefixes.
        pair=(sum(c[t][0] for t in order[:k]),sum(c[t][1] for t in order[:k]))
        rec=dict(input_row=j,p=pair[0],q=pair[1])
        ck(f'original cut{i} prefix{k}',old['exact_tuple'][i]['prefixes'][k],rec)
        coeff[j]=neg(pair)
        original=sub(C[i],C[j])
        if j<i: original=sub(original,(K,N))
        ck(f'one chronological tuple coefficient cut{i} eta{j}',coeff[j],original)
        records.append(rec)
    ck(f'cut{i} empty prefix', coeff[i],(0,0))
    ck(f'cut{i} saved interpretation',
       {key:old['exact_tuple'][i][key] for key in ('start','B','n','s')},
       dict(start=i,B='sum_k eta[input_row[k]]*2^q[k]/3^p[k]',n='B/(2^N/3^K-1)',s='n+23/11'))
    Bs.append(coeff)
    cut_records.append(dict(start=i,prefixes=records))
# Verify B_(i+1) = c_i B_i + c_i eta_i (P^-1-1) as a formal
# Laurent polynomial in independent eta_j, including the closing row.
endpoints=[]
for i in range(25):
    residual=Counter()
    for j,ex in Bs[(i+1)%25].items(): residual[(j,*ex)]+=1
    for j,ex in Bs[i].items(): residual[(j,*add(c[i],ex))]-=1
    residual[(i,*sub(c[i],(K,N)))]-=1
    residual[(i,*c[i])]+=1
    nonzero=[dict(eta=k[0],p=k[1],q=k[2],coefficient=v) for k,v in residual.items() if v]
    ck(f'endpoint row{i} exact residual',nonzero,[])
    endpoints.append(dict(row=i,output=(i+1)%25,residual=nonzero))
# Complete original finite arithmetic: no reliance on saved pass flags.
relations={'=':lambda a,b:a==b,'<':lambda a,b:a<b,'>':lambda a,b:a>b,'>=':lambda a,b:a>=b}
replay=[]
for item in old['checks']:
    a,b=F(item['actual']),F(item['required'])
    passed=relations[item['relation']](a,b)
    ck('replay '+item['name'], passed,True)
    ck('difference '+item['name'], F(item['difference']),a-b)
    replay.append(dict(name=item['name'],actual=a,required=b,relation=item['relation'],difference=a-b,passed=passed))
kap=F(23,11)
lm,lp=F(10584,10**14),F(10585,10**14)
delta=lp/(1-lp)
ck('imported log bounds',[F(old['imported_enclosure']['lower']),F(old['imported_enclosure']['upper'])],[lm,lp])
ck('analytic domain',0<lm<lp<1,True)
ck('eta power bound',2*16**8<27**8,True)
ck('eta lower',kap/2>1,True)
ck('D upper',delta<F(1,100),True)
ck('lower domain',1/delta+kap>100+kap>F(540,11),True)
ck('cut2 k1 exact input/prefix',cut_records[2]['prefixes'][1],dict(input_row=3,p=218,q=464))
ck('power41',3**41<2**65,True)
ck('power13',3**13<2**21,True)
ck('factorization',[41*5+13,65*5+21,464-346],[218,346,118])
ck('direct finite power comparison',3**218<2**346,True)
threshold=F(4,11)*2**112
bounds=dict(D_upper=delta,eta_lower=kap/2,all_n_lower=1/delta,all_s_lower=1/delta+kap,required_s_lower=F(540,11),s2_lower=F(2**118)/delta+kap,coarse_s2_lower=2**118,row2_threshold=threshold,coarse_gap=2**118-threshold)
for key,value in bounds.items(): ck('complete bound '+key,F(old['bounds'][key]),F(value))
ck('threshold strictness',2**118>threshold,True)
failures=[x['name'] for x in checks if not x['passed']]
out=HERE/'d35-full-support-row2-counterexample-audit-certificate.json'
data=dict(scope='L106 independent endpoint-only audit; no J/H verification',rows=rows,totals=dict(K=K,N=N),cuts=cut_records,endpoints=endpoints,bounds=bounds,replayed_checks=replay,checks=checks,summary=dict(verdict='AUDIT_PASSED' if not failures else 'INCOMPLETE',checks=len(checks),failures=failures),limitations='L104 log enclosure imported after exact operand matching. Formal monomial identities and canonical proof establish one rational tuple. No full-guard or actual-word conclusion.')
out.write_text(json.dumps(data,default=str,indent=2)+'\n')
print(f'Verdict={data["summary"]["verdict"]}; checks={len(checks)}; failures={failures}')
print(f'K={K}, N={N}; 625 cyclic coefficients and all25 endpoint identities checked.')
print(f'D < {delta}; all s_i > {bounds["all_s_lower"]}; required >=540/11.')
print(f's2 > {2**118}; threshold={threshold}; gap={2**118-threshold}.')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures: raise SystemExit(1)
