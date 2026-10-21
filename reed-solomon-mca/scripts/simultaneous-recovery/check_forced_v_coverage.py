"""Independent enumeration and forced-V filter; covers rejected configurations.

Reuses only the audited source cubic partition. Uses determinant solves, not
the producer RREF or mixed-cubic equations. Checks every admitted weight
record against all eight moments, including original triple compatibility.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).parent
P=97
H=tuple(x for x in range(1,P) if pow(x,16,P)==1)
POW={x:tuple(pow(x,j,P) for j in range(1,9)) for x in H}
INV={x:pow(x,-1,P) for x in range(1,P)}


def ev(roots,x):
    a=1
    for y in roots:a=a*(x-y)%P
    return a


def moments(word):
    return tuple(sum(a*POW[x][j] for x,a in word.items())%P for j in range(8))


def word(c,ys,zs,d,p,q,r,mu):
    n={x:-mu*c[x]%P for x in ys}
    n.update({x:c[x] for x in zs})
    n[1]=c[1]*(q-mu*p)%P
    n[d]=c[d]*(1-(1+mu)*r)%P
    return n


def recover(k,target):
    a=[[POW[x][j] for x in k]+[target[j]] for j in range(4)]
    for j in range(4):
        pivot=next(i for i in range(j,4) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        scale=INV[a[j][j]]
        a[j]=[x*scale%P for x in a[j]]
        for i in range(4):
            if i==j:continue
            scale=a[i][j]
            a[i]=[(x-scale*y)%P for x,y in zip(a[i],a[j])]
    weights=tuple(a[j][4] for j in range(4))
    assert moments(dict(zip(k,weights)))==target
    return weights


def main():
    data=json.loads((ROOT/'forced-v-mixed-result.json').read_text())
    assert data['complete']
    retained={}
    weight_records=0
    for case in data['cases']:
        ys,zs=tuple(case['Y']),tuple(case['Z'])
        d=case['d'];w=tuple(case['W']);p,q,r=case['p_q_r']
        residual=tuple(case['V'])
        s,ss=tuple(case['S']),tuple(case['SS'])
        common=set(s)&set(ss)
        assert len(common)==1 and common<=set(w)
        assert residual==tuple(sorted((set(s)|set(ss))-common))
        assert case['Bprime_minus_d']==sorted(common|set(residual))
        assert case['T0']==[x for x in H if x not in {1,d,*ys,*zs,*residual,*common}]
        assert {tuple(x['K']) for x in case['selected_recoveries']}=={
            tuple(sorted((d,*s))),tuple(sorted((d,*ss)))}
        assert case['V_recovery']['r']==r
        assert case['mixed_mus']==sorted({x['mu'] for x in case['mixed_records']})
        for rec in case['mixed_records']:
            support=set(rec['K'])
            assert len(support)==4
            assert len(support&{1,*ys,*zs})==1
            assert len(support&set(case['Bprime_minus_d']))==1
            assert len(support&set(case['T0']))==2
            assert rec['full_weight']==all(rec['omega'])
        key=(ys,zs,d,w,p,q,residual)
        assert key not in retained
        retained[key]=case
        c={int(x):a for x,a in case['c'].items()}
        assert p*q*(1-p-q)*r*(1-r)%P
        rows=[(residual,case['V_recovery']['mu'],case['V_recovery']['omega'])]
        rows += [(tuple(x['K']),x['mu'],x['omega']) for x in case['selected_recoveries']]
        rows += [(tuple(x['K']),x['mu'],x['omega']) for x in case['mixed_records']]
        for k,mu,omega in rows:
            assert moments(dict(zip(k,omega)))==moments(word(c,ys,zs,d,p,q,r,mu))
            if k==residual or d in k:assert all(omega)
            weight_records+=1
        # Check a genuine original affine pencil at a safe prime-field chart;
        # arbitrary other charts need only remove E=0, not add candidates.
        scalars={m for _,m,_ in rows}
        rho=next(a for a in range(2,P) if all((a-(1-a)*m)%P for m in scalars))
        e0={1:c[1]*p*INV[(1-rho)%P]%P,d:c[d]*r*INV[(1-rho)%P]%P}
        e0.update({x:c[x]*INV[(1-rho)%P]%P for x in ys})
        e1={1:c[1]*q*INV[rho]%P,d:c[d]*(1-r)*INV[rho]%P}
        e1.update({x:c[x]*INV[rho]%P for x in zs})
        e2={1:-c[1]*(1-p-q)%P,**{x:-c[x]%P for x in w}}
        m0,m1,m2=map(moments,(e0,e1,e2))
        assert all(e0.values()) and all(e1.values()) and all(e2.values())
        assert m2==tuple((a+rho*(b-a))%P for a,b in zip(m0,m1))

    source=json.loads((ROOT/'disjoint-d-pair-result.json').read_text())
    expected_choices={(y,z) for y in combinations([x for x in H if x!=1],2)
                      for z in combinations([x for x in H if x not in (1,*y)],2)}
    assert {(tuple(x['Y']),tuple(x['Z'])) for x in source['complete_groups']}==expected_choices
    assert len(source['complete_groups'])==len(expected_choices)==8190
    counters=Counter();seen=set();accepted=set();raw=0
    for index,choice in enumerate(source['complete_groups'],1):
        ys,zs=tuple(choice['Y']),tuple(choice['Z'])
        for _,gg in choice['groups']:
            if len(gg)<3:continue
            group=[tuple(s) for s in gg]
            for w in group:
                for s,ss in combinations([x for x in group if x!=w],2):
                    raw+=1
                    def coefficients(outside):
                        u=ev(outside,zs[0])*INV[ev(w,zs[0])]%P
                        mu=-u*ev(w,ys[0])*INV[ev(outside,ys[0])]%P
                        a=u*ev(w,1)*INV[ev(outside,1)]%P
                        return mu,a
                    mu,a=coefficients(s);nu,b=coefficients(ss)
                    if mu in (0,96) or nu in (0,96) or mu==nu:
                        counters['pair_scalar_gate']+=1;continue
                    p=(a-b)*INV[(nu-mu)%P]%P;q=(a+mu*p)%P
                    if p*q*(1-p-q)%P==0:
                        counters['p_q_gate']+=1;continue
                    shared=set(s)&set(ss)
                    assert len(shared)==1 and shared<=set(w)
                    residual=tuple(sorted((set(s)|set(ss))-shared))
                    used={1,*ys,*zs,*w,*s,*ss}
                    for d in H:
                        if d in used:continue
                        counters['d_pair_presentations']+=1
                        key=(ys,zs,d,w,p,q,residual)
                        if key in seen:
                            counters['duplicate_presentations']+=1;continue
                        seen.add(key)
                        U={1,d,*ys,*zs,*w};outside=[x for x in H if x not in U]
                        c={x:ev(outside,x) for x in U}
                        # Four recurrence rows, with two unknowns mu,beta_d.
                        fh=[ev(residual,1)*POW[1][j]%P for j in range(4)]
                        fd=[ev(residual,d)*POW[d][j]%P for j in range(4)]
                        fy=[(sum(c[x]*ev(residual,x)*POW[x][j] for x in ys)
                             +c[1]*p*fh[j])%P for j in range(4)]
                        rhs=[(sum(c[x]*ev(residual,x)*POW[x][j] for x in zs)
                              +c[1]*q*fh[j])%P for j in range(4)]
                        pair=next(((i,j) for i,j in combinations(range(4),2)
                                   if (fy[j]*fd[i]-fy[i]*fd[j])%P),None)
                        assert pair is not None
                        i,j=pair;det=(fy[j]*fd[i]-fy[i]*fd[j])%P
                        m=(fd[i]*rhs[j]-fd[j]*rhs[i])*INV[det]%P
                        beta=(fy[i]*rhs[j]-fy[j]*rhs[i])*INV[det]%P
                        if any((fy[t]*m-fd[t]*beta-rhs[t])%P for t in range(4)):
                            counters['V_inconsistent']+=1;assert key not in retained;continue
                        if m in (0,96):
                            counters['V_selected_scalar']+=1;assert key not in retained;continue
                        r=(1-beta*INV[c[d]])*INV[1+m]%P
                        if r in (0,1):
                            counters['r_gate']+=1;assert key not in retained;continue
                        if key in retained:
                            case=retained[key]
                            assert case['p_q_r']==[p,q,r] and case['V_recovery']['mu']==m
                            assert {tuple(case['S']),tuple(case['SS'])}=={s,ss}
                            assert {x['mu'] for x in case['selected_recoveries']}=={mu,nu}
                            assert {int(x):v for x,v in case['c'].items()}==c
                            accepted.add(key);counters['feasible']+=1
                        else:
                            om=recover(residual,moments(word(c,ys,zs,d,p,q,r,m)))
                            if not all(om):counters['V_lower_weight']+=1;continue
                            counters['feasible']+=1
                            k1=tuple(sorted((d,*s)));k2=tuple(sorted((d,*ss)))
                            first=recover(k1,moments(word(c,ys,zs,d,p,q,r,mu)))
                            second=recover(k2,moments(word(c,ys,zs,d,p,q,r,nu)))
                            assert not all(first) or not all(second),('missing full case',key)
                            counters['selected_lower_weight']+=1
        if index%2000==0:print(f'coverage choices {index}/8190; matched cases {len(accepted)}',flush=True)
    assert raw==75600 and accepted==set(retained)
    assert dict(counters)==data['counters'],(dict(counters),data['counters'])
    result={'summary':{'normalized_choices_checked':len(expected_choices),
                       'W_pair_presentations_checked':raw,
                       'unique_configurations_checked':len(seen),
                       'accepted_configurations_checked':len(accepted),
                       'all_weight_records_eight_moments_checked':weight_records,
                       'original_triples_checked':len(retained),
                       'all_retained_and_rejected_filters_match':True,'failures':[]},
            'complete_filter_counts':dict(counters)}
    out=ROOT/'forced-v-mixed-coverage.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],sort_keys=True));print(f'certificate {out}')


if __name__=='__main__':main()
