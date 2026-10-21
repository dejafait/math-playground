"""Independent source-sum reconstruction and exact full-block sign audit.

Uses factorial binomials, literal full-u source ranges with zero terms
skipped, nonnegative multinomial admissibility, and integer common-
denominator direct orbit sums rather than the generator's h aggregation.
"""
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
BASE=Path(__file__).parent
OUT=BASE/'mixed-zero-one-audit-results.json'
W,V=68,956

def enc(x):
    x=F(x)
    return [x.numerator,x.denominator]
def dec(x): return F(*x)

@lru_cache(None)
def fac(n): return factorial(n)
@lru_cache(None)
def binomial(n,r):
    if min(n,r,n-r)<0: return 0
    return fac(n)//(fac(r)*fac(n-r))

def source_beta(i,j,k,t,n):
    total=0
    for u in range(k,n-k+1):
        # In these cases an explicit source binomial factor is zero.
        if u<t or u>i or u>j: continue
        term=binomial(u,t)*binomial(n-2*k,u-k)*binomial(n-k-u,i-u)*binomial(n-k-u,j-u)
        total+=(-1 if (u-t)%2 else 1)*term
    return total

def prescribed(p,i,j,h):
    distances=[i,j,h]
    if any(b in (1,2,3,4) for b in distances): return F(0)
    if 0 in distances:
        nonzero=[b for b in distances if b]
        if not nonzero: return F(1)
        if len(nonzero)!=2 or nonzero[0]!=nonzero[1]:
            raise ValueError('invalid repeated-word distances')
        return p[nonzero[0]]
    return p[i]*p[j]*p[h]/p[68]

def main():
    data=json.loads((BASE/'mixed-zero-one-results.json').read_text())
    old=json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    lp=json.loads((BASE/'delsarte-lp-results.json').read_text())
    zero=json.loads((BASE/'full-zero-block-results.json').read_text())
    zero_entries={(r['i'],r['j']):r for r in zero['entries']}
    failures=[]
    def require(test,label):
        if not test: failures.append(label)
    require(data['stage']=='completed','completed generator')
    require(data['parameters']=={'n':1024,'w':68,'v':956,'d':10,'k':0,'l':1},'parameters')
    require(data['indices']==list(range(1,69)),'all original indices')
    p=[F(1)]+[F(0)]*4+[F(x['numerator'],x['denominator'])/(2*binomial(W,i)*binomial(V,i))
                           for i,x in zip(range(5,69),lp['exact']['primal'])]
    require(p==list(map(dec,data['p']))==list(map(dec,old['p']))==list(map(dec,zero['p'])),'unchanged pair assignment')
    for row in old['orbits']:
        a,b,c,u=row['key']
        require(prescribed(p,a,b,c)==dec(row['value']),'old orbit '+str(row['key']))
    entries={(r['i'],r['j']):r for r in data['entries']}
    require(len(entries)==len(data['entries'])==2346,'complete unique upper entries')
    matrices=[[[F(0) for _ in range(68)] for _ in range(68)] for _ in range(2)]
    orbit_count=0; coefficient_count=0
    for i in range(1,69):
        for j in range(i,69):
            ts=[t for t in range(min(i,j)+1) if min(i-t,j-t,t,W-i-j+t)>=0]
            ss=[s for s in range(min(i,j)+1) if min(i-s,j-s,s,V-i-j+s)>=0]
            bw=[source_beta(i,j,0,t,W) for t in ts]
            bv=[source_beta(i,j,1,s,V) for s in ss]
            r=entries[i,j]
            require((r['t'],r['s'],r['beta_w'],r['beta_v'])==(ts,ss,bw,bv),'source coefficients '+str((i,j)))
            require(bw==zero_entries[i,j]['beta_w'],'old zero beta_w '+str((i,j)))
            coefficient_count+=len(bw)+len(bv)
            hs=sorted(set(i+j-t-s for t in ts for s in ss))
            first={h:prescribed(p,i,j,h) for h in hs}
            second={h:p[h]-first[h] for h in hs}
            den=lcm(*(x.denominator for x in list(first.values())+list(second.values())))
            nf={h:int(first[h]*den) for h in hs}
            ns={h:int(second[h]*den) for h in hs}
            sums=[0,0]; hc={}
            for t,a in zip(ts,bw):
                for s,b in zip(ss,bv):
                    h=i+j-t-s
                    require(0<=h<=68,'distance range')
                    if min(i,j,h)==0: require(t-s==0,'repeated-word invariant')
                    c=a*b
                    hc[h]=hc.get(h,0)+c
                    sums[0]+=c*nf[h]
                    sums[1]+=c*ns[h]
                    orbit_count+=1
            require(r['h_coefficients']==[[h,c] for h,c in sorted(hc.items()) if c],
                    'all h coefficients '+str((i,j)))
            for family in range(2):
                value=F(sums[family],den)
                matrices[family][i-1][j-1]=matrices[family][j-1][i-1]=value
        if i%16==0 or i==68: print('Independent reconstruction through row',i,flush=True)
    require(orbit_count==data['actual_orbit_count'],'complete orbit count')
    records=[]
    for family,a in enumerate(matrices):
        stored=data['families'][family]
        saved=[[dec(x) for x in r] for r in stored['matrix']]
        require(saved==a,'all 4624 source entry identities family '+str(family))
        require(all(saved[i][j]==saved[j][i] for i in range(68) for j in range(68)),
                'full symmetry family '+str(family))
        c=stored['certificate']
        if not c['psd']:
            x=list(map(dec,c['negative_vector']))
            require(len(x)==68,'negative vector dimension')
            q=sum((x[i]*a[i][j]*x[j] for i in range(68) for j in range(68) if x[i] and x[j]),F(0))
            require(q==dec(c['quadratic']) and q<0,'negative quadratic family '+str(family))
            support=[i for i,b in enumerate(x) if b]
            records.append({'family':family,'psd':False,'negative_support':[i+1 for i in support],
                'negative_vector_on_support':[enc(x[i]) for i in support],
                'quadratic':enc(q),'all_source_matrix_entries_checked':True,
                'load_bearing_principal_matrix':[[enc(a[i][j]) for j in support] for i in support]})
            print('Family',family,'negative original indices',[i+1 for i in support],'quadratic < 0:',q<0,flush=True)
        else:
            e=[[dec(x) for x in row] for row in c['congruence']]
            d=list(map(dec,c['diagonal']))
            require(len(e)==68 and all(len(row)==68 for row in e) and len(d)==68,'PSD dimensions')
            require(all(e[i][i]==1 and all(e[i][j]==0 for j in range(i)) for i in range(68)),
                    'unit upper triangular congruence hence determinant 1')
            # Clear denominators before full matrix multiplication. For
            # C=diag(cd), E=ei*C^{-1}, A=ai/ad. Every integer identity
            # ei^T ai ei = ad*C*D*C is exactly E^T A E=D.
            ad=lcm(*(x.denominator for row in a for x in row))
            cd=[lcm(*(e[k][j].denominator for k in range(68))) for j in range(68)]
            ai=[[int(x*ad) for x in row] for row in a]
            ei=[[int(e[i][j]*cd[j]) for j in range(68)] for i in range(68)]
            ae=[[sum(ai[i][k]*ei[k][j] for k in range(j+1)) for j in range(68)] for i in range(68)]
            identity_count=0
            for i in range(68):
                for j in range(68):
                    actual=sum(ei[k][i]*ae[k][j] for k in range(i+1))
                    expected=d[i]*ad*cd[i]*cd[j] if i==j else 0
                    require(actual==expected,'congruence entry '+str((family,i,j)))
                    identity_count+=1
                if i%16==0 or i==67:
                    print('Family',family,'integer congruence rows through',i,flush=True)
            require(all(x>=0 for x in d),'every diagonal sign family '+str(family))
            records.append({'family':family,'psd':True,'all_source_matrix_entries_checked':True,
                'all_congruence_identities_checked':True,'determinant':[1,1],
                'positive_pivots':sum(x>0 for x in d),'zero_pivots':sum(x==0 for x in d),
                'zero_pivot_indices':[i+1 for i,x in enumerate(d) if x==0],
                'all_diagonal_signs_checked':True,
                'diagonal_signs':[1 if x>0 else 0 if x==0 else -1 for x in d],
                'all_zero_residual_rows_verified':True,
                'congruence_entry_identities':identity_count,
                'diagonal':list(map(enc,d))})
            print('Family',family,'exact PSD identities verified',flush=True)
    objective=sum(binomial(W,i)*binomial(V,i)*p[i] for i in range(69))
    threshold=F(65537**28,2**128)
    require(objective==dec(data['objective'])==(F(binomial(1024,64),binomial(68,64))+1)/2,
            'unchanged objective')
    require(threshold==dec(data['required_threshold']) and objective>threshold,'unchanged threshold excess')
    require(not data['failures'],'generator consistency checks')
    result={'verified':not failures,'checks':{'upper_entries':2346,'source_beta_coefficients':coefficient_count,
        'actual_admissible_orbits':orbit_count,'full_source_matrix_entry_identities':9248,
        'old_orbit_values':len(old['orbits']),'old_zero_beta_w_entries':2346},
        'families':records,'objective':enc(objective),'required_threshold':enc(threshold),
        'failures':failures,'scope':'only this extension on both full mixed (0,1) blocks'}
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Verified:',not failures,'; checks:',result['checks'])
    print('Actual objective:',objective,'; required <=',threshold)
    print('Failures:',failures,'; independent certificate:',OUT)
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
