"""Independent rational evidence checks for the step-198 proof audit.
Geometry/jet evaluation is covered by separate complete replays and the
canonical manual inclusion audit; this does not pretend to replace either.
"""
import json
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt
from pathlib import Path

P = Path(__file__).parent
OUT = P/'bulk-core-tail-audit-198.json'
checks = {}
records = {}
def read(name):
    return json.loads((P/name).read_text())
def iv(r):
    return F(r['lower']), F(r['upper'])
def enc(x):
    return {'lower':str(x[0]), 'upper':str(x[1])}
def contains(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]
def add(a,b):
    return a[0]+b[0],a[1]+b[1]
def sub(a,b):
    return a[0]-b[1],a[1]-b[0]
def mul(a,b):
    z=[x*y for x in a for y in b]
    return min(z),max(z)
def div(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def powi(a,n):
    assert a[0]>=0
    return a[0]**n,a[1]**n
one=(F(1),F(1))

def main():
    source=read('response-modulus-second-moment-certificate.json')
    audited=read('response-modulus-second-moment-audit-certificate.json')
    mo=read('bulk-core-tail-moments-196.json')
    old=read('bulk-haar-integral-enclosure-188.json')
    aa=read('bulk-haar-conditional-sign-194.json')
    bb=read('bulk-core-tail-196.json')
    assert not source['failures'] and not audited['failures']
    assert source['bounds']==mo['source']['source_bounds']==old['coefficients']['source_bounds']
    assert all(iv(source['bounds'][k])==iv(audited['bounds'][k]) for k in ('S','T','B13','B14'))
    assert all(iv(v)==iv(audited['moment_bounds'][j]) for j,v in source['bounds']['C'].items())
    bounds=source['bounds']; cs={int(j):iv(r) for j,r in bounds['C'].items()}
    s,t,b13,b14=[iv(bounds[k]) for k in ('S','T','B13','B14')]
    alpha=div(sub(b14,t),sub(b14,b13))
    theta={j:div(sub(s,cs[1]),sub(div(cs[j+1],cs[j]),cs[1])) for j in (13,14)}
    for co in (mo['source'],old['coefficients']):
        assert contains(iv(co['alpha']),alpha)
        assert all(contains(iv(co['theta'][str(j)]),theta[j]) for j in (13,14))
    weight={0:add(mul(alpha,sub(one,theta[13])),mul(sub(one,alpha),sub(one,theta[14]))),
            13:div(mul(alpha,theta[13]),cs[13]),14:div(mul(sub(one,alpha),theta[14]),cs[14])}
    assert all(v[0]>0 and contains(iv(mo['positive_weight'][str(j)]),v) for j,v in weight.items())
    checks['audited_source_and_exact_coefficient_containment']=True

    # Complete head range and full omitted response tail, using the reviewed
    # 24-place base arithmetic only here. No selector/state callback occurs.
    import enclose_bulk_haar_integral as base
    primes=[p for p in range(2,201) if all(p%d for d in range(2,isqrt(p)+1))]
    tail=base.I(0)
    for p in primes[3:]:
        q=base.I(1)/(p*p*base.I(p).sqrt())
        tail=tail+q/(1-q)
    residual=(base.I(2)/(3*200*base.I(200).sqrt()))/(1-base.I(1)/(201*201*base.I(201).sqrt()))
    tail=tail+residual
    factor=base.I((1-tail).square().lo,(base.I(1)/(1-tail).square()).hi,True)
    assert tail.enc()==old['full_log_tail'] and residual.enc()==old['log_tail_residual_above_200']
    assert factor.enc()==old['full_squared_modulus_tail_factor'] and 0<=tail.lo<=tail.hi<base.SCALE
    g,co=base.source_coefficients(P)
    assert co==old['coefficients'] and base.PI.enc()==old['pi']
    response=[]
    for ix in product(range(4),repeat=3):
        w=base.I(1)
        for p,k in zip((2,3,5),ix):
            angle=base.I((base.PI*base.I(F(k,4))).lo,(base.PI*base.I(F(k+1,4))).hi,True)
            q=base.I(1)/(p*p*base.I(p).sqrt())
            w=w*(base.I(1)/(1-2*q*base.trig(angle,True)+q.square()))
        w=w*factor; gg=g(w)
        response.append({'indices':list(ix),'W':w.enc(),'g':gg.enc()})
    assert response==old['response_cells']
    full=(min(iv(r['g'])[0] for r in response),max(iv(r['g'])[1] for r in response))
    assert enc(full)==old['g_full_range']==aa['g_full_range']==bb['g_full_range']
    checks['all_64_full_response_cells_and_tail']=True

    pi_hi=F(old['pi']['upper'])
    allocations=read('bulk-haar-conditional-sign-error-allocation-194.json')
    angular=[]
    for data,centers in ((aa,[F(r['g']) for r in aa['centers']]),(bb,[F(30)])):
        cells=data['cells']; previous=F(0); totals=[(F(0),F(0)) for _ in centers]
        strict=0; unresolved_mass=F(0); counts={}; budgets=[]
        allocations_now=[{'quadrature_narrower_cells':0,'range_narrower_cells':0,
            'retained_width_quadrature_narrower':F(0),'retained_width_range_narrower':F(0)} for _ in centers]
        for rec in cells:
            left,right,mass=map(F,(rec['left'],rec['right'],rec['mass']))
            assert left==previous and mass==right-left>0; previous=right
            assert len(rec['values'])==len(centers)
            is_strict='state_jets' in rec
            if is_strict:
                strict+=1
                gaps=[iv(r) for r in rec['selector']['gaps']]
                assert all(l>0 or h<0 for l,h in gaps)
                pair=next((i,j) for i in range(3) for j in range(3) if gaps[i][1]<0<gaps[j][0])
                unused=next(k for k in range(3) if k not in pair)
                pair2=(0,1) if gaps[unused][0]>0 else (1,0)
                assert rec['selector']['pairs']==[list(pair),list(pair2)]
                key=str((pair,pair2)); counts[key]=counts.get(key,0)+1
                assert len(rec['state_jets'])==3 and all(len(v)==3 for v in rec['state_jets'])
                for state in rec['state_jets']:
                    for coord in state:
                        assert all(iv(coord[k])[0]<=iv(coord[k])[1] for k in ('value','first','second'))
            else:
                unresolved_mass+=mass
            for k,(gg,v) in enumerate(zip(centers,rec['values'])):
                val=iv(v['integral']); totals[k]=add(totals[k],val)
                if not is_strict:
                    assert v['kind']=='unresolved'
                    rad=F(v['unresolved_radius'])
                    assert val==(-rad,rad) and 2*rad/mass>=1
                    assert (2*rad/mass-1)**2>=3*gg/80
                else:
                    assert v['kind']=='strict'
                    el,er=map(iv,v['endpoint_values'])
                    trap=iv(v['trapezoid']); assert contains(trap,mul(add(el,er),(mass/2,mass/2)))
                    deriv=iv(v['second']); err=F(v['quadrature_radius'])
                    assert err>=mass*(2*pi_hi*mass)**2*max(map(abs,deriv))/12
                    direct=mul(iv(v['range']),(mass,mass))
                    enlarged=(trap[0]-err,trap[1]+err)
                    intersection=(max(direct[0],enlarged[0]),min(direct[1],enlarged[1]))
                    assert contains(val,intersection)
                    # Saved retained intervals can widen direct rounding by one ulp.
                    tag='quadrature' if enlarged[1]-enlarged[0] < direct[1]-direct[0] else 'range'
                    allocations_now[k][tag+'_narrower_cells']+=1
                    allocations_now[k]['retained_width_'+tag+'_narrower']+=val[1]-val[0]
        assert previous==1
        expected=[iv(r['value']) for r in aa['centers']] if data is aa else [iv(bb['conditional_value'])]
        assert totals==expected
        if data is aa:
            for k,r in enumerate(allocations):
                assert r['g']==str(centers[k]) and r['strict_width_check']
                assert all(allocations_now[k][key]==(r[key] if isinstance(r[key],int) else F(r[key])) for key in allocations_now[k])
            assert unresolved_mass==F(aa['unresolved_mass'])
        angular.append({'cells':len(cells),'strict':strict,'unresolved_mass':str(unresolved_mass),
                        'strict_branch_counts':counts,'sums':[enc(x) for x in totals]})
    records['angular']=angular
    checks['all_3430_cell_partitions_branches_aggregate_errors_and_allocations']=True

    # Independent direct-binomial finite sums, not the generation recurrence.
    local={}; exact_records=[]
    for r in mo['local_factors']:
        j,p,e=r['j'],r['p'],r['e']
        assert 1<=e<=1024
        exact=sum((F(comb(j+k-1,k)**2,p**(5*k)) for k in range(e+1)),F(0))
        ratio=F((j+e)**2,(e+1)**2*p**5)
        last=F(comb(j+e-1,e)**2,p**(5*e)); bound=last*ratio/(1-ratio)
        assert 0<ratio<1 and str(ratio)==r['ratio']
        assert contains(iv(r['sum']),(exact,exact))
        assert F(r['tail']['upper'])>=bound and F(r['tail']['upper'])*10**110<=F(r['sum']['lower'])
        assert contains(iv(r['factor']),(exact,exact+bound))
        assert (j,p) not in local
        local[j,p]=iv(r['factor'])
        exact_records.append({'j':j,'p':p,'e':e,'exact_finite_sum':str(exact),'exact_geometric_tail_bound':str(bound),'contained':True})
    assert set(local)=={(r['j'],p) for r in mo['C'] for p in primes}
    cm={0:one}; global_checks=[]
    for r in mo['C']:
        j=r['j']; den=1-F(j*j,201**5); assert den>0
        tail=F(j*j,4*200**4)/den; assert 0<tail<1 and str(tail)==r['prime_log_tail']
        product_bound=one
        for p in primes: product_bound=mul(product_bound,local[j,p])
        full=(product_bound[0],product_bound[1]/(1-tail))
        assert contains(iv(r['moment']),full)
        cm[j]=iv(r['moment']); global_checks.append({'j':j,'denominator':str(den),'log_tail':str(tail),'contained':True})
    records['direct_local_euler_checks']=exact_records; records['global_euler_checks']=global_checks
    checks['all_2024_direct_binomial_sums_and_44_full_tails']=True
    # Independent multinomial coefficients, rather than iterative polynomial products.
    w={j:iv(mo['positive_weight'][str(j)]) for j in (0,13,14)}
    needed={0}
    assert [r['r'] for r in mo['G_moments']]==list(range(1,9))
    for r in mo['G_moments']:
        n=r['r']; poly={}
        for k in range(n+1):
            for l in range(n-k+1):
                j=13*k+14*l; coeff=comb(n,k)*comb(n-k,l)
                term=mul(mul(powi(w[13],k),powi(w[14],l)),powi(w[0],n-k-l))
                term=mul(term,(F(coeff),F(coeff)))
                poly[j]=add(poly.get(j,(F(0),F(0))),term)
        assert set(map(int,r['polynomial']))==set(poly)
        assert all(contains(iv(r['polynomial'][str(j)]),v) for j,v in poly.items())
        value=(F(0),F(0))
        for j in poly: value=add(value,mul(iv(r['polynomial'][str(j)]),cm[j]))
        assert contains(iv(r['raw_moment']),value)
        assert r['moment']==(enc(one) if n==1 else r['raw_moment'])
        if n==1: assert contains(iv(r['raw_moment']),one)
        needed.update(poly)
    assert sorted(needed)==mo['orders'] and max(needed)==112
    checks['all_eight_direct_multinomial_expansions']=True

    # Full failed/preliminary record lengths and recorded work accounting.
    pre=read('bulk-core-tail-preliminary-196.json'); fail=read('bulk-core-tail-failed-196.json')
    assert len(pre['cell_derivatives'])==len(aa['cells'])
    assert pre['state_response_derivative_callbacks']==3*angular[0]['strict']==4674
    assert fail['state_response_derivative_callbacks']==3*next(i for i,r in enumerate(aa['cells']) if 'state_jets' not in r)==900
    for d in (aa,bb): assert sum(d['callback_counts'].values())==d['callback_total']<=65536
    f=read('bulk-haar-conditional-sign-194-failed.json'); fv=read('bulk-haar-conditional-sign-194-verifier-failed.json')
    assert sum(f['one_execution_callbacks'].values())*f['executions']==f['total_callbacks']==42
    assert sum(fv['one_failed_verifier_callbacks'].values())*fv['executions']==fv['total_callbacks']==60
    assert aa['callback_counts']['failed_execution_callbacks']==42
    assert bb['callback_counts']['failed_execution_callbacks']==900
    checks['recorded_failures_and_full_preliminary_lengths']=True
    # Legacy counters include strict-state derivatives, but omit each
    # unresolved-cell universal derivative-bound evaluation. Charge those
    # in both the preliminary pass and its replay, plus the failed bound
    # attempt at the first unresolved cell. Do not alter historical records.
    unresolved=sum('state_jets' not in r for r in aa['cells'])
    v194=read('bulk-haar-conditional-sign-verification-194.json')
    v196=read('bulk-core-tail-verification-196.json')
    old196=v196['complete_callbacks']+2*unresolved+1
    new194=v194['verification_callback_total']
    new196=sum(v196['verification_callback_counts'].values())+unresolved
    corrected=v194['complete_callback_total']+old196+new194+new196
    assert bb['callback_total']+unresolved+1<=65536 and corrected<=262144
    records['work_accounting']={'legacy_196_total':v196['complete_callbacks'],
        'omitted_unresolved_derivative_bounds_per_pass':unresolved,
        'charged_failed_bound_attempt':1,'corrected_historical_196_total':old196,
        'new_194_replay':new194,'new_196_replay_including_fallback_bounds':new196,
        'current_audit_callbacks':new194+new196,'combined_historical_and_current':corrected,
        'cap':262144,'qualification':'Legacy totals exclude fallback derivative-bound evaluations; original evidence preserved.'}
    checks['corrected_work_accounting_with_all_fallback_bounds']=True
    tr=bb['transport']; a,b=full_range=iv(bb['g_full_range'])
    assert F(tr['a'])==a and F(tr['c'])==a+F(1,100000)
    assert tr['anchor']==aa['centers'][0]['value']
    delta=-F(tr['anchor']['upper'])-F(tr['sup_abs_derivative'])/100000
    assert delta==F(tr['delta'])==-F(tr['core_upper'])>0
    U=[F(r['moment']['upper']) for r in mo['G_moments']]
    floor=min([F(1)]+[u/F(30)**r for r,u in enumerate(U,1)])
    M=F(bb['M']); dmax=-F(tr['anchor']['lower'])
    assert a<30<b and iv(bb['conditional_value'])[0]>F(1,800000)
    assert floor>F(169,200000) and dmax<F(61,100000) and M>F(111,100)
    lower=-dmax*(1-floor)+M*floor
    weak=-F(61,100000)*(1-F(169,200000))+F(111,100)*F(169,200000)
    assert lower>weak==F(6569309,20000000000)>F(1,3100)
    obs=bb['global_M_obstruction']
    assert str(lower)==obs['optimistic_comparison_lower'] and str(floor)==obs['computed_pbar_lower_for_c_below_point']
    records['obstruction']={'computed_pbar_floor':str(floor),'exact_comparison_lower':str(lower),'weakened_comparison_lower':str(weak),'required_for_success':'strictly negative','core_delta':str(delta)}
    checks['core_anchor_and_universal_obstruction_rationals']=True
    out={'checks':checks,'records':records,'failures':[],
         'qualification':'Exact rational evidence supplement; complete jet replays and canonical analytic proof audit are also essential. No independent proof of Python.'}
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS:',len(checks),'checks; all 3430 angular cells and 2024 direct local Euler sums.')
    print('Comparison lower:',float(lower),'; required: < 0; certified lower > 1/3100.')
    print('Corrected combined callbacks:',corrected,'/ 262144; current audit:',new194+new196)
    print('Failures: []; certificate:',OUT)

if __name__=='__main__':
    try: main()
    except Exception as exc:
        OUT.write_text(json.dumps({'checks':checks,'records':records,'failures':[repr(exc)]},indent=2)+'\n')
        raise
