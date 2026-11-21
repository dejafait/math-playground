#!/usr/bin/env python3
"""Full independent arithmetic check of fixed compact allowance94.

Does not import/run the producer. Exact Pascal transform checks every
global coefficient; Euclidean replay checks every subdivision operation.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE/'l938-compact-negative-mass-check-94.json'
EXACT = BASE/'l938-compact-global-exact-94.json'
N,G = 3089,10**120
report = dict(status='IN_PROGRESS',stage='input',checks=[],failures=[],inputs_sha256={},
              python=sys.version,subdivision_row_checks=0,midpoint_updates=0)


def save():
    OUT.write_text(json.dumps(report,indent=2)+'\n')


def check(name,ok):
    report['checks'].append(dict(name=name,passed=bool(ok)))
    if not ok:
        report['failures'].append(name)
        report['status']='FAILED'
        save()
        raise AssertionError(name)


def read(name):
    raw=(BASE/name).read_bytes()
    report['inputs_sha256'][name]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


save()
claim=read('l938-compact-negative-mass-94.json')
saved=read('l938-compact-bernstein-enclosures-94.json')
poly=read('actual-h2-energy-cell-polynomial-48.json')
kernel=read('actual-h2-energy-cell-48.json')
audit50=read('actual-h2-energy-cell-audit-50.json')
audit92=read('c948a-complete-budget-audit-92.json')
old=read('l938-negative-tail-allowance-87.json')
for name in ('actual-h2-energy-cell-polynomial-48.json','actual-h2-energy-cell-48.json'):
    check('unchanged full audited input '+name,report['inputs_sha256'][name]
          ==claim['inputs_sha256'][name]==audit50['inputs_sha256'][name])
check('complete saved coefficient identity',report['inputs_sha256']['l938-compact-bernstein-enclosures-94.json']
      ==claim['coefficient_sha256'])
for label,obj in [('producer',claim),('audit50',audit50),('audit92',audit92)]:
    check(label+' complete flags',not obj['failures'] and all(x['passed'] is True for x in obj['checks']))
ap=kernel['approximation']
R=list(map(int,poly['numerators']))
den=int(poly['denominator'])
C=2*factorial(12)*G*4**518
check('normalization degree and fixed kernel',len(R)==3073 and R[-1]!=0 and den==C**12
      and (ap['degree'],ap['nodes'],ap['theta_terms'],ap['precision'])==(256,257,8,200)
      and int(ap['chebyshev_denominator'])==G and int(ap['power_denominator'])==G*4**256
      and saved['degree']==N and int(saved['grid'])==G)
fac=[factorial(s) for s in range(N+1)]
check('full global arrays',len(saved['power'])==len(saved['global_bernstein'])==N+1)
for s,(lo,hi) in enumerate(saved['power']):
    lo,hi=int(lo),int(hi)
    exact=F(0) if s<17 else F(R[s-17]*8**s,den*fac[s])
    check('independent full scalar '+str(s),F(lo,G)<=exact<=F(hi,G) and 0<=hi-lo<=1)

# Exact binomial transform, without the producer's interval Horner formula.
# b_j= sum_s binom(j,s) z_s/H, z_s=R_(s-17)8^s(N-s)!, H=den*N!.
H=den*fac[N]
t=[0 if s<17 else R[s-17]*8**s*fac[N-s] for s in range(N+1)]
report['stage']='exact complete Pascal transform'
save()
pascal_updates=0
for r in range(N):
    for j in range(N,r,-1):
        t[j]+=t[j-1]
        pascal_updates+=1
    if r%512==0:
        print('Independent exact Pascal stage',r,'/',N,flush=True)
for j,(lo,hi) in enumerate(saved['global_bernstein']):
    lo,hi=int(lo),int(hi)
    check('exact global inclusion '+str(j),lo*H<=t[j]*G<=hi*H)
EXACT.write_text(json.dumps(dict(degree=N,normalization='v_p(8x)/pi^6',
    denominator=str(H),bernstein_numerators=list(map(str,t))),indent=2)+'\n')
report['exact_global_artifact']=EXACT.name
report['exact_global_sha256']=hashlib.sha256(EXACT.read_bytes()).hexdigest()
report['pascal_updates']=pascal_updates
report['stage']='full independent subdivision replay'
save()

records=saved['subdivisions']
cursor=0


def split(bounds,a,b):
    global cursor
    rec=records[cursor]
    check('prescribed subdivision interval '+str(cursor),rec['interval']==[str(a),str(b)]
          and len(rec['left'])==len(rec['right'])==N+1)
    low=[int(x) for x,y in bounds]
    high=[int(y) for x,y in bounds]
    left=[(low[0],high[0])]
    right=[(low[-1],high[-1])]
    for depth in range(1,N+1):
        new_low=[]
        new_high=[]
        valid=True
        for i in range(len(low)-1):
            x=low[i]+low[i+1]
            y=high[i]+high[i+1]
            q,r=divmod(x,2)
            s,t=divmod(y,2)
            valid=valid and x==2*q+r and y==2*s+t and r in (0,1) and t in (0,1)
            u=s+int(t!=0)
            valid=valid and q<=u and 2*q<=x and y<=2*u
            new_low.append(q)
            new_high.append(u)
        check('all midpoint inclusions '+str(cursor)+','+str(depth),valid)
        report['midpoint_updates']+=len(new_low)
        report['subdivision_row_checks']+=1
        low,high=new_low,new_high
        left.append((low[0],high[0]))
        right.append((low[-1],high[-1]))
    right.reverse()
    check('all left coefficients '+str(cursor),left==[tuple(map(int,v)) for v in rec['left']])
    check('all right coefficients '+str(cursor),right==[tuple(map(int,v)) for v in rec['right']])
    cursor+=1
    print('Independent full restriction',cursor,'/16:',a,b,flush=True)
    save()
    return left,right


global_bounds=[tuple(map(int,v)) for v in saved['global_bernstein']]
_,right=split(global_bounds,F(0),F(8))
leaves=[(F(4),F(8),right)]
for depth in range(4):
    result=[]
    for a,b,bounds in leaves:
        left,right=split(bounds,a,b)
        result.extend([(a,(a+b)/2,left),((a+b)/2,b,right)])
    leaves=result
check('all stipulated quarter cells and full restrictions',cursor==len(records)==16
      and len(leaves)==len(saved['cells'])==len(claim['cells'])==16)
pi=F(old['exact']['pi_upper'])
x=F(4,5)
exp=sum((x**s/factorial(s) for s in range(33)),F(0))+x**33/factorial(33)/(1-x/34)
check('exact scalar reuse',3<pi<4 and pi==F(ap['pi']['upper'])==F(claim['exact']['pi_upper'])
      and exp==F(old['exact']['exp_upper'])==F(claim['exact']['exp_upper']))
total=F(0)
for i,(a,b,bounds) in enumerate(leaves):
    item=saved['cells'][i]
    cell=claim['cells'][i]
    check('full final cell '+str(i),a==F(16+i,4) and b-a==F(1,4)
          and item['interval']==[str(a),str(b)]==cell['interval']
          and bounds==[tuple(map(int,v)) for v in item['coefficients']] and len(bounds)==N+1)
    # beta(j+1,N-j+1)*binom(N,j)=1/(N+1), all parameters positive.
    coeff_sum=sum(-lo for lo,hi in bounds if lo<0)
    integral=(b-a)*F(coeff_sum,G*(N+1))
    value=exp*pi**6*integral
    check('complete cell allowance '+str(i),coeff_sum==int(cell['negative_coefficient_sum_numerator'])
          and integral==F(cell['normalized_integral_upper'])
          and value==F(cell['weighted_actual_units_upper'])
          and F(cell['enclosure']['lower'])<=value<=F(cell['enclosure']['upper']))
    total+=value
B=F(audit92['exact']['total_upper'])
m=F('8.935649629627030e-35')
combined=total+B
check('same audited B',B==F(claim['exact']['replacement_B']) and 0<B<m
      and report['inputs_sha256']['c948a-complete-budget-audit-92.json']
      ==claim['inputs_sha256']['c948a-complete-budget-audit-92.json'])
for key,value in [('compact_polynomial_upper',total),('combined_upper',combined),
                  ('required_strict_upper',m),('unused_margin',m-combined),('ratio',combined/m)]:
    check('exact final '+key,value==F(claim['exact'][key]))
for key,value in [('compact_upper',total),('replacement_upper',B),('combined_upper',combined),
                  ('unused_margin',m-combined),('ratio',combined/m)]:
    check('full final display '+key,F(claim['summary'][key]['lower'])<=value<=F(claim['summary'][key]['upper']))
check('complete threshold decision',(combined<m)==claim['summary']['pass_strict']
      and claim['summary']['omitted_coefficients']=='NONE' and claim['summary']['outer_tail']=='UNPAID')
report['exact']=dict(compact_upper=str(total),replacement_B=str(B),combined_upper=str(combined),
                     required_strict_upper=str(m),unused_margin=str(m-combined),ratio=str(combined/m))
report['summary']=dict(full_degree=N,global_coefficients=N+1,cells=16,
    all_final_cell_coefficients=16*(N+1),all_subdivision_coefficients_verified=True,
    compact_upper=claim['summary']['compact_upper'],combined_upper=claim['summary']['combined_upper'],
    unused_margin=claim['summary']['unused_margin'],ratio=claim['summary']['ratio'],
    pass_strict=combined<m,outer_tail='UNPAID',inherited_contracts=['theta inclusion',
    'original signed polynomial execution','C948a derivative-prefix execution','arithmetic execution'])
report['status']='PASSED_COMPLETE_ARITHMETIC_CHECK'
report['stage']='complete'
report['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print('Result:',report['status'],'; combined <=',report['summary']['combined_upper']['upper'])
print('Required <',m,'; strict pass:',combined<m,'; failures:',report['failures'])
print('Full checker:',OUT,'; exact global coefficients:',EXACT)
