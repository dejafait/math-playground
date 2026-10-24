"""Independent exact rational reconstruction of the frozen scalar certificate."""
import gzip
import hashlib
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction as F
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
B = Path(__file__).resolve().parent
ROOT = B.parent.parent
SOURCE = B/'root-residual-functional.json.gz'
OUT = B/'root-residual-functional-verification.json'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def enc(q):
    return [q.numerator,q.denominator]


def choose(n,k):
    return comb(n,k) if 0<=k<=n else 0


def main():
    report = dict(stage='in_progress', failures=[], source_sha256=sha(SOURCE),
                  code_sha256=sha(Path(__file__)))
    counts = Counter()

    def save():
        report.update(checks=sum(counts.values()), checks_by_kind=dict(counts))
        OUT.write_text(json.dumps(report,indent=2)+'\n')

    def ck(kind,ok,detail=None):
        counts[kind] += 1
        if not ok:
            report['stage']='failed'
            report['failures'].append(dict(kind=kind,detail=detail))
            save()
            raise AssertionError((kind,detail))

    with gzip.open(SOURCE,'rt') as f:
        s=json.load(f)
    ck('constructor_complete', s['stage']=='complete' and not s['failures'] and
       s['code_sha256']==sha(B/'root_residual_functional.py'))
    for p,h in s['input_sha256'].items():
        ck('all_input_bindings',sha(ROOT/p)==h,p)
    for name,code in [('l112-l113-critical-audit.json','critical_audit_l112_l113.py'),
                      ('l114-critical-audit.json','critical_audit_l114.py'),
                      ('l120-critical-audit.json','critical_audit_l120.py')]:
        audit=json.loads((B/name).read_text())
        ck('retained_audit_status',audit['stage']=='verified' and not audit['failures'] and
           audit['code_sha256']==sha(B/code),name)
        for p,h in audit['input_sha256'].items():
            ck('retained_audit_input',sha(ROOT/p)==h,p)
    with gzip.open(B/'positive-factor-enclosure.json.gz','rt') as f:
        r=json.load(f)
    lp=json.loads((B/'delsarte-lp-results.json').read_text())
    audit=json.loads((B/'l112-l113-critical-audit.json').read_text())
    global_audit=json.loads((B/'l120-critical-audit.json').read_text())
    ck('all_source_coefficients',r['coefficients']==global_audit['contraction_coefficients'] and
       sum(map(len,r['coefficients']))==81355 and len(r['coefficients'])==64)
    ck('frozen_contract',set(s['frozen'])=={'N','H','Q','radius','point','scale_powers','box','preconditioner'}
       and s['frozen']=={k:r[k] for k in s['frozen']} and r['Q']==10**70 and
       r['radius']==10**25 and r['stage']=='exact_complete' and r['inclusion'] and
       len(r['preconditioner'])==64 and all(len(row)==64 for row in r['preconditioner']))
    for k,q in enumerate(r['point']):
        ck('all_original_boxes_and_margins',r['box'][k]==[q-10**25,q+10**25] and
           min(r['krawczyk_image'][k][0]+10**25,10**25-r['krawczyk_image'][k][1])
           ==r['inclusion_margins'][k]>0,k)
    N,H=65537**28//2**128+1,comb(1024,68)
    U=F(comb(1024,64),comb(68,64))
    av=[F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    g=[comb(68,i)*comb(956,i) for i in range(69)]
    c=[F(1)]+[F(0)]*4+[(N-1)*av[i-5]/((U-1)*g[i]) for i in range(5,69)]
    ck('canonical_pairs_and_cardinality',len(av)==64 and min(av)>0 and sum(av)==U-1 and
       list(map(enc,c))==r['c']==s['c'] and sum(g[i]*c[i] for i in range(69))==N and
       N==r['N'] and H==r['H'] and enc(F(N,H))==s['rho'])
    scales=[F(10)**p for p in r['scale_powers']]
    a=[F(q,10**70) for q in r['point']]
    radius=F(1,10**45)
    box=[(v-radius,v+radius) for v in a]
    ck('positive_box',len(a)==len(scales)==64 and all(0<l<u for l,u in box))
    ref=c[5]/(scales[0]*box[0][1])**2
    P=[choose(67,i)*choose(955,i)-choose(67,i-1)*choose(955,i-1) for i in range(5,69)]
    ck('all_johnson_coefficients',s['johnson_mode_one']==P)
    ck('fixed_positive_reference',ref>0 and s['reference']==enc(ref))
    w=[p*scale/ref for p,scale in zip(P,scales)]
    z=[sum(w[j]*F(r['preconditioner'][j][k],10**70) for j in range(64)) for k in range(64)]
    ck('all_exact_weights',s['w']==list(map(enc,w)) and s['z']==list(map(enc,z)))
    constant=F(1)+sum(z)
    ck('constant_including_all_residuals',s['constant']==enc(constant))
    # Independently gather source-row contributions and their derivatives.
    contributions=defaultdict(list)
    derivatives=[defaultdict(F) for _ in range(64)]
    residuals=[]
    for i,row in enumerate(r['coefficients']):
        value=F(-1)
        for j,h,A in row:
            b=F(A)*scales[i]*scales[j]*scales[h]/((N-2)*c[i+5])
            value+=b*a[i]*a[j]*a[h]
            key=tuple(sorted((i,j,h)))
            term=-z[i]*b
            contributions[key].append(term)
            # Each of the three occurrences contributes, including repetitions.
            for k,p,q in ((i,j,h),(j,i,h),(h,i,j)):
                derivatives[k][tuple(sorted((p,q)))]+=term
        residuals.append(value)
        ck('each_exact_residual',enc(value)==audit['exact_residuals'][i],i)
    keys=sorted(contributions)
    coefficients={key:sum(contributions[key],F(0)) for key in keys}
    ck('complete_cubic_shape',len(s['cubics'])==len(keys)==28215)
    T=s['arithmetic_grid']
    ck('fixed_arithmetic_grid',T==10**120)
    for idx,key in enumerate(keys):
        entry=s['cubics'][idx]
        value=coefficients[key]
        lo,hi=entry[2]
        ck('each_collected_cubic',entry[:2]==[list(key),enc(value)],idx)
        ck('each_outward_coefficient',F(lo,T)<=value<=F(hi,T) and
           value-F(lo,T)<F(1,T) and F(hi,T)-value<F(1,T),idx)
    ck('complete_derivative_shape',len(s['derivative'])==len(s['gradient_bounds'])==64)
    exact_derivative_bounds=[]
    for k in range(64):
        expected=[]
        for idx,key in enumerate(keys):
            if k in key:
                rest=list(key)
                rest.remove(k)
                expected.append([*rest,idx,key.count(k)])
        ck('all_derivative_occurrences',s['derivative'][k]==expected,k)
        ck('rowwise_derivative_identity',dict(derivatives[k])=={
            tuple(entry[:2]):coefficients[keys[entry[2]]]*entry[3] for entry in expected},k)
        lo=hi=w[k]
        for (p,q),value in derivatives[k].items():
            product_lo=box[p][0]*box[q][0]
            product_hi=box[p][1]*box[q][1]
            lo+=value*(product_lo if value>=0 else product_hi)
            hi+=value*(product_hi if value>=0 else product_lo)
        bound=s['gradient_bounds'][k]
        ck('each_full_exact_gradient_enclosed',F(bound[0],T)<=lo<=hi<=F(bound[1],T),k)
        exact_derivative_bounds.append(list(map(enc,(lo,hi))))
    exact_point=1+sum(v*x for v,x in zip(w,a))-sum(v*f for v,f in zip(z,residuals))
    ck('complete_corrected_point_enclosed',F(s['point_value'][0],T)<=exact_point<=F(s['point_value'][1],T))
    # Check the whole final mean-value interval with exact rational products;
    # integer-rounded additions in the constructor may only enlarge it.
    absolute_sum=sum(max(abs(F(lo,T)),abs(F(hi,T))) for lo,hi in s['gradient_bounds'])
    err=radius*absolute_sum
    ck('full_original_error_box',F(s['error_interval'][0],T)<=-err<=err<=F(s['error_interval'][1],T))
    result=[s['point_value'][j]+s['error_interval'][j] for j in (0,1)]
    ck('whole_mean_value_result',result==s['result_interval'] and
       list(map(lambda q:enc(F(q,T)),result))==s['result_fraction'] and
       F(result[0],T)<=exact_point-err<=exact_point+err<=F(result[1],T))
    grid=10**6
    bracket=[result[0]*grid//T,-((-result[1]*grid)//T)]
    ck('strict_straddle_and_grid',result[0]<0<result[1] and s['verdict']=='STRICT_STRADDLE' and
       s['normalized_grid']==grid and s['normalized_bracket']==bracket)
    # Deliberately do not output or use a point-value sign verdict.
    report.update(stage='verified',reference=enc(ref),
                  exact_point_value=enc(exact_point),
                  exact_gradient_bounds=exact_derivative_bounds,
                  point_interval=[enc(F(v,T)) for v in s['point_value']],
                  error_interval=[enc(F(v,T)) for v in s['error_interval']],
                  result_interval=s['result_fraction'], normalized_grid=grid,
                  normalized_bracket=bracket,verdict='STRICT_STRADDLE',
                  required='lower endpoint >= 0', cubics=len(keys),derivatives=64)
    save()
    print('Verified all 81355 source coefficients, 28215 collected cubics, 64 exact residuals and 64 complete derivatives')
    print('Enclosure of (lambda_1+R0)/R0 in [%s,%s]/%s; required lower >=0; STRICT_STRADDLE' % (*bracket,grid))
    print('Checks:',sum(counts.values()),'; failures:',len(report['failures']),'; certificate:',OUT)


if __name__=='__main__':
    main()
