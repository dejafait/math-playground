#!/usr/bin/env python3
"""One fixed-budget closed cover. See L946 for exact integer range proof."""
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE = Path(__file__).resolve().parent
OUT = BASE/'l938-direct-cover-76.json'
S = 2**1024
J, K = 768, 128
report = {'status':'IN_PROGRESS', 'checks':[], 'failures':[], 'nodes':[],
          'arithmetic':{'scale':str(S),'retained_power_exponents':J,
                        'taylor_order':K,'maximum_depth':12,'maximum_intervals':8191}}

def save():
    OUT.write_text(json.dumps(report,indent=2)+'\n')

def check(name, truth):
    report['checks'].append({'name':name,'passed':bool(truth)})
    if not truth:
        report['failures'].append(name)
        report['status']='FAILED'
        save()
        raise AssertionError(name)

def read(name):
    raw=(BASE/name).read_bytes()
    report.setdefault('input_hashes',{})[name]=hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def ceildiv(a,b):
    return -((-a)//b)

def up(q):
    return ceildiv(q.numerator*S,q.denominator)

def display(q):
    with localcontext() as ctx:
        ctx.prec=12
        return str(Decimal(q.numerator)/Decimal(q.denominator))

save()
prior=read('l944-c944a-audit-75.json')
sharp=read('l938-two-bound-endpoint-73.json')
poly=read('actual-h2-energy-cell-polynomial-48.json')
data=read('actual-h2-energy-cell-48.json')
old=read('actual-h2-energy-cell-audit-50.json')
check('complete step75 audit', prior['status']=='PASSED' and not prior['failures'] and
      len(prior['checks'])==15620 and all(x['passed'] is True for x in prior['checks']))
for name in ['l938-two-bound-endpoint-73.json','actual-h2-energy-cell-polynomial-48.json',
             'actual-h2-energy-cell-48.json','actual-h2-energy-cell-audit-50.json']:
    check('step75 input identity '+name, report['input_hashes'][name]==prior['inputs_sha256'][name])
for name, expected in old['inputs_sha256'].items():
    actual=hashlib.sha256((BASE/name).read_bytes()).hexdigest()
    check('step50 input identity '+name, actual==expected)
check('complete step50 audit',old['status']=='PASSED' and not old['failures'] and
      len(old['checks'])==5101 and all(x['passed'] is True for x in old['checks']))
check('complete inherited polynomial identity',old['integer_identity']['residual']=='0' and
      old['integer_identity']['difference_bound_lt_half_base'] is True)
check('sharp endpoint complete', sharp['status']=='SCOPED_ENDPOINT_PASS' and not sharp['failures'] and
      all(x['passed'] is True for x in sharp['checks']))
ap=data['approximation']
check('fixed input budgets',(ap['degree'],ap['nodes'],ap['theta_terms'],ap['precision'],
      int(ap['chebyshev_denominator']))==(256,257,8,200,10**120))
rr=list(map(int,poly['numerators'])); den=int(poly['denominator'])
check('all3073 signed coefficients and normalization',len(rr)==3073 and den==
      (2*factorial(12)*int(ap['power_denominator'])*4**262)**12)
bounds={k:F(v) for k,v in sharp['bounds'].items()}
check('complete sharp bounds',bounds['epsilon']==F(ap['epsilon']) and
      bounds['common_factor_bound']==2+bounds['epsilon'] and
      bounds['product_error']==12*bounds['epsilon']*bounds['common_factor_bound']**11 and
      bounds['product_derivative_error']==bounds['delta']*bounds['common_factor_bound']**11+
          11*bounds['B']*bounds['epsilon']*bounds['common_factor_bound']**10 and
      bounds['beta_constant']==F(293,540*2**36*factorial(17)))
report['bounds']={k:str(v) for k,v in bounds.items()}

# f_s(y)=sum_l R_l 4^(s+l)y^(s+l)/(C^12(s+l)!), s=17,16.
# Every coefficient is converted by an exact Euclidean division.
polys=[]
for s in [17,16]:
    values=[(0,0)]*s
    fac=factorial(s); pow4=4**s
    for ell, a in enumerate(rr):
        numerator=a*pow4*S; denominator=den*fac
        lo,rem=divmod(numerator,denominator)
        check('exact coefficient division '+str(s)+','+str(ell),
              0<=rem<denominator and numerator==lo*denominator+rem)
        values.append((lo,lo+(rem!=0)))
        fac*=s+ell+1; pow4*=4
    retained=values[:J]
    tail=sum(max(abs(lo),abs(hi)) for lo,hi in values[J:])
    remainder_coefficients=[max(abs(lo),abs(hi))*comb(j,K)
                            for j,(lo,hi) in enumerate(retained) if j>=K]
    polys.append((retained,tail,remainder_coefficients))
    report.setdefault('coefficient_enclosures',[]).append({
        'offset':s,'intervals':[[str(lo),str(hi)] for lo,hi in values],
        'uniform_discarded_tail_scaled':str(tail)})
save()

def positive_horner_upper(coeffs,x):
    acc=0
    for a in reversed(coeffs):
        acc=ceildiv(acc*x.numerator,x.denominator)+a
    return acc

def polynomial_range(index,c,h,b):
    coefficients,tail,remcoeff=polys[index]
    los=[0]*K; his=[0]*K
    cn,cd=c.numerator,c.denominator
    # In-place descending recurrence computes first K coefficients of f(c+z).
    for alo,ahi in reversed(coefficients):
        for k in range(K-1,0,-1):
            los[k]=(los[k]*cn)//cd+los[k-1]
            his[k]=ceildiv(his[k]*cn,cd)+his[k-1]
        los[0]=(los[0]*cn)//cd+alo
        his[0]=ceildiv(his[0]*cn,cd)+ahi
    # Outward interval polynomial coefficients include all fixed-point errors.
    variation=0
    for k in range(K-1,0,-1):
        variation=ceildiv((variation+max(abs(los[k]),abs(his[k])))*h.numerator,h.denominator)
    # Taylor remainder at order K on [a,b], with nonnegative y<=b<=1.
    derivative_bound=positive_horner_upper(remcoeff,b)
    hp=h**K
    remainder=ceildiv(derivative_bound*hp.numerator,hp.denominator)
    extra=variation+remainder+tail
    return los[0]-extra,his[0]+extra,{
        'center_coefficient':[str(los[0]),str(his[0])],
        'variation_scaled':str(variation),'taylor_derivative_bound_scaled':str(derivative_bound),
        'taylor_remainder_scaled':str(remainder),'discarded_tail_scaled':str(tail)}

A=bounds['product_error']; D=bounds['product_derivative_error']; Z=bounds['beta_constant']
stack=[(0,0)]; leaves=[]
while stack:
    depth,index=stack.pop()
    n=2**depth
    a=F(n+15*index,16*n); b=F(n+15*(index+1),16*n)
    c=(a+b)/2; h=(b-a)/2; E=4*b
    r0=up(Z*E**17*A)
    r1=up(Z*E**16*(17*A+E*D))
    lo,hi,evidence=polynomial_range(0,c,h,b)
    rec={'depth':depth,'index':index,'E':[str(4*a),str(4*b)],
         'value':{'polynomial_scaled':[str(lo),str(hi)],'actual_radius_scaled':str(r0),
                  'actual_scaled':[str(lo-r0),str(hi+r0)],'evidence':evidence}}
    v_excludes=lo-r0>0 or hi+r0<0
    if v_excludes:
        rec['decision']='VALUE_POSITIVE' if lo-r0>0 else 'VALUE_NEGATIVE'
    else:
        dlo,dhi,devidence=polynomial_range(1,c,h,b)
        rec['derivative']={'polynomial_scaled':[str(dlo),str(dhi)],'actual_radius_scaled':str(r1),
                           'actual_scaled':[str(dlo-r1),str(dhi+r1)],'evidence':devidence}
        if dlo-r1>0:
            rec['decision']='DERIVATIVE_POSITIVE'
        elif depth==12:
            rec['decision']='UNRESOLVED'
        else:
            rec['decision']='BISECT'
            stack.extend([(depth+1,2*index+1),(depth+1,2*index)])
    report['nodes'].append(rec)
    if rec['decision']!='BISECT':leaves.append(rec)
    if len(report['nodes'])%32==0:
        report['partial_summary']={'examined':len(report['nodes']),'pending':len(stack),'leaves':len(leaves)}
        save()
        print('Examined',len(report['nodes']),'pending',len(stack),'leaves',len(leaves),flush=True)
    if len(report['nodes'])>8191:check('interval budget',False)

# Exact closed-cover validation, independent of the traversal order.
ordered=sorted(leaves,key=lambda x:F(x['E'][0]))
check('outer closed endpoints',F(ordered[0]['E'][0])==F(1,4) and F(ordered[-1]['E'][1])==4)
check('every shared closed endpoint',all(F(a['E'][1])==F(b['E'][0]) for a,b in zip(ordered,ordered[1:])))
check('all depth and interval budgets',len(report['nodes'])<=8191 and max(x['depth'] for x in report['nodes'])<=12)
check('every positive length leaf',all(F(x['E'][0])<F(x['E'][1]) for x in ordered))
for i,rec in enumerate(report['nodes']):
    vlo,vhi=map(int,rec['value']['actual_scaled'])
    dlo=int(rec.get('derivative',{}).get('actual_scaled',['0'])[0])
    decision=rec['decision']
    check('node decision '+str(i), {'VALUE_POSITIVE':vlo>0,'VALUE_NEGATIVE':vhi<0,
          'DERIVATIVE_POSITIVE':dlo>0,'UNRESOLVED':vlo<=0<=vhi and dlo<=0 and rec['depth']==12,
          'BISECT':vlo<=0<=vhi and dlo<=0 and rec['depth']<12}[decision])
unknown=[x for x in ordered if x['decision']=='UNRESOLVED']
report.pop('partial_summary',None)
report['summary']={'intervals_examined':len(report['nodes']),'closed_leaves':len(leaves),
    'maximum_depth_reached':max(x['depth'] for x in report['nodes']),
    'leaf_counts':{tag:sum(x['decision']==tag for x in leaves) for tag in
                   ['VALUE_NEGATIVE','VALUE_POSITIVE','DERIVATIVE_POSITIVE','UNRESOLVED']},
    'unresolved_closed_intervals':[x['E'] for x in unknown],
    'actual_required_condition':'Each closed leaf excludes zero for actual v, or actual vprime lower >0.',
    'normalization':'unchanged v/pi^6 and vprime/pi^6; y=E/4 is the argument only'}
margins=[]
for rec in leaves:
    decision=rec['decision']
    obj=rec['derivative'] if decision=='DERIVATIVE_POSITIVE' else rec['value']
    if decision=='UNRESOLVED':continue
    plo,phi=map(int,obj['polynomial_scaled']); radius=int(obj['actual_radius_scaled'])
    clearance=-phi if decision=='VALUE_NEGATIVE' else plo
    check('strict leaf margin '+str(rec['depth'])+','+str(rec['index']),clearance>radius>0)
    ratio=F(clearance,radius)
    margins.append((ratio,rec['depth'],rec['index'],decision,clearance-radius))
ratio,depth,index,decision,gap=min(margins)
report['summary']['minimum_clearance_over_radius']={
    'exact_ratio':str(ratio),'display_ratio':display(ratio),
    'required':'strictly greater than 1', 'node':[depth,index], 'decision':decision,
    'strict_gap_scaled':str(gap), 'display_strict_gap':display(F(gap,S))}
report['status']='CERTIFIED_COMPACT_COVER' if not unknown else 'INCONCLUSIVE_COMPACT_COVER'
report['producer_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
save()
print(report['status'],json.dumps(report['summary']),flush=True)
print('Failures:',report['failures'],'certificate:',OUT,flush=True)
