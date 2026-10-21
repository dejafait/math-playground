"""Independent exhaustive audit of the selected-block rational primal witness.

Rebuilds touched orbits, beta dictionaries using factorial binomials, every
scalar/pair row and every affine matrix. Verifies each saved congruence by
full matrix multiplication, including invertibility and zero pivots.
"""
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations
from math import factorial
from pathlib import Path

BASE=Path(__file__).parent
OUT=BASE/'selected-triple-sdp-audit-results.json'
W,V=68,956
BATCH=[(33,33,[33,34,35]),(34,34,[34]),(0,0,[0,5,6,68])]

def dec(x): return F(x[0],x[1])
def enc(x):
    x=F(x)
    return [x.numerator,x.denominator]

@lru_cache(None)
def binomial(n,k):
    if k<0 or k>n or n<0: return 0
    return factorial(n)//(factorial(k)*factorial(n-k))

@lru_cache(None)
def source_beta(i,j,k,t,n):
    total=0
    # Literal full source summation; no generator's restricted-u shortcut.
    for u in range(k,n-k+1):
        term=binomial(u,t)*binomial(n-2*k,u-k)*binomial(n-k-u,i-u)*binomial(n-k-u,j-u)
        total+=(-1 if (u-t)%2 else 1)*term
    return total

def canonical(i,j,t,s): return (*sorted([i,j,i+j-t-s]),t-s)
def valid_orbits(i,j):
    # Independent nonnegative parts test for both multinomials.
    for t in range(min(i,j)+1):
        if min(i-t,j-t,t,W-i-j+t)<0: continue
        for s in range(min(i,j)+1):
            if min(i-s,j-s,s,V-i-j+s)>=0: yield i,j,t,s

def determinant(a):
    a=[r[:] for r in a]; value=F(1)
    for k in range(len(a)):
        ix=next((i for i in range(k,len(a)) if a[i][k]),None)
        if ix is None: return F(0)
        if ix!=k: a[ix],a[k]=a[k],a[ix]; value=-value
        pivot=a[k][k]; value*=pivot
        for i in range(k+1,len(a)):
            factor=a[i][k]/pivot
            for j in range(k+1,len(a)): a[i][j]-=factor*a[k][j]
    return value

def main():
    cert=json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    failures=[]; checks={}; psd_records=[]
    def require(test,label):
        if not test: failures.append(label)
    require(cert['parameters']=={'n':1024,'w':68,'d':10},'parameters')
    p=list(map(dec,cert['p']))
    lp=json.loads((BASE/'delsarte-lp-results.json').read_text())
    expected_p=[F(1)]+[F(0)]*4+[F(z['numerator'],z['denominator'])/(2*binomial(W,i)*binomial(V,i))
                               for i,z in zip(range(5,69),lp['exact']['primal'])]
    require(p==expected_p and len(p)==69,'pair candidate specification')
    require(p[0]==1 and all(x==0 for x in p[1:5]),'normalization and pair zeros')
    require(all(x>=0 for x in p),'pair signs')
    touched=set((0,i,i,0) for i in range(69))
    for k,l,inds in BATCH:
        require(all(k<=i<=W-k and l<=i<=V-l for i in inds),'source block index bounds')
        for i in inds:
            for j in inds:
                if i<=j: touched.update(canonical(*o) for o in valid_orbits(i,j))
    records={tuple(r['key']):r for r in cert['orbits']}
    require(len(records)==len(cert['orbits']) and set(records)==touched,'complete orbit class set')
    values={}; closures={}; scalar_rows=[]
    for z in sorted(touched):
        a,b,c,u=z; cls=set()
        for i,j,h in permutations((a,b,c)):
            require((i+j-h+u)%2==0,'permutation parity')
            t=(i+j-h+u)//2; s=(i+j-h-u)//2
            require(min(i-t,j-t,t,W-i-j+t,i-s,j-s,s,V-i-j+s)>=0,'permutation multinomial')
            cls.add((i,j,t,s))
        closures[z]=sorted(cls)
        require(records[z]['closure']==list(map(list,closures[z])),'complete permutation closure '+str(z))
        val=F(0) if any(1<=h<=4 for h in (a,b,c)) else p[b] if a==0 else p[a]*p[b]*p[c]/p[68]
        values[z]=val
        require(dec(records[z]['value'])==val,'orbit value '+str(z))
        require(val>=0,'orbit nonnegativity '+str(z))
        scalar_rows.append({'key':list(z),'kind':'nonnegative','slack':enc(val)})
        for i,j in sorted(set((o[0],o[1]) for o in cls)):
            upper=p[i]-val; lower=1+val-p[i]-p[j]
            require(upper>=0 and lower>=0,'orbit scalar bounds '+str((z,i,j)))
            scalar_rows.extend([{'key':list(z),'kind':'upper','i':i,'j':j,'slack':enc(upper)},
                                {'key':list(z),'kind':'lower','i':i,'j':j,'slack':enc(lower)}])
    require(cert['scalar_rows']==scalar_rows,'all stored scalar rows and slacks')
    count=64+sum(z[0]>0 and not any(1<=h<=4 for h in z[:3]) for z in touched)
    require(count==cert['construction']['retained_orbit_variables'] and count<=20000,'variable cap and count')
    require(len(scalar_rows)+68==cert['construction']['scalar_rows'] and len(scalar_rows)+68<=200000,'row cap and count')
    pair_slacks=[]
    require(len(cert['pair_rows'])==68,'all 68 pair rows present')
    for j in range(1,69):
        # Polynomial convolution, independently generating all coefficients at once.
        first=[(-1 if h%2 else 1)*binomial(j,h) for h in range(j+1)]
        second=[binomial(W-j,r)*binomial(V-j,r) for r in range(W-j+1)]
        coeff=[sum(first[h]*second[i-h] for h in range(len(first)) if 0<=i-h<len(second)) for i in range(5,69)]
        slack=1+sum(c*p[i] for i,c in zip(range(5,69),coeff))
        pair_slacks.append(slack)
        require(slack>=0,'pair inequality '+str(j))
        require(cert['pair_rows'][j-1]=={'j':j,'coefficients':coeff,'slack':enc(slack)},'pair stored row '+str(j))
    require(len(cert['blocks'])==3,'block count')
    coefficient_entries=0
    for block,(k,l,inds) in zip(cert['blocks'],BATCH):
        require((block['k'],block['l'],block['indices'])==(k,l,inds),'block definition')
        affine={(r['i'],r['j']):r for r in block['coefficients']}
        require(len(affine)==len(inds)*(len(inds)+1)//2,'full upper-triangular coefficient dictionary')
        matrices=[[[F(0) for j in inds] for i in inds] for _ in range(2)]
        for row,i in enumerate(inds):
            for col in range(row,len(inds)):
                j=inds[col]; yc={}; pc={}
                for _,_,t,s in valid_orbits(i,j):
                    c=source_beta(i,j,k,t,W)*source_beta(i,j,l,s,V)
                    z=canonical(i,j,t,s); h=i+j-t-s
                    yc[z]=yc.get(z,0)+c; pc[h]=pc.get(h,0)+c
                yc={z:c for z,c in yc.items() if c}; pc={h:c for h,c in pc.items() if c}
                saved=affine[i,j]
                require(saved['y']==[[list(z),c] for z,c in sorted(yc.items())] and
                        saved['p']==[[h,c] for h,c in sorted(pc.items())],'affine coefficient dictionary '+str((k,l,i,j)))
                coefficient_entries+=len(yc)+len(pc)
                m0=sum(c*values[z] for z,c in yc.items())
                m1=sum(c*p[h] for h,c in pc.items())-m0
                for family,val in enumerate([m0,m1]): matrices[family][row][col]=matrices[family][col][row]=val
        require(len(block['families'])==2,'both PSD families')
        for family,(data,matrix) in enumerate(zip(block['families'],matrices)):
            require([[dec(x) for x in r] for r in data['matrix']]==matrix,'exact affine matrix '+str((k,l,family)))
            proof=data['certificate']; n=len(inds)
            require(proof['psd'],'candidate matrix reported PSD')
            T=[[dec(x) for x in r] for r in proof['congruence']]
            D=list(map(dec,proof['diagonal']))
            require(len(T)==n and all(len(r)==n for r in T) and len(D)==n,'PSD dimensions')
            det=determinant(T); require(det!=0,'PSD congruence invertible')
            transformed=[[sum(T[a][i]*matrix[a][b]*T[b][j] for a in range(n) for b in range(n)) for j in range(n)] for i in range(n)]
            require(all(transformed[i][j]==(D[i] if i==j else 0) for i in range(n) for j in range(n)),'complete PSD congruence identity')
            require(all(d>=0 for d in D),'all PSD diagonal signs')
            # Explicit zero pivots: congruence identity above verifies all their rows.
            psd_records.append({'k':k,'l':l,'family':family,'dimension':n,'invertible_det':enc(det),
                'positive_pivots':sum(d>0 for d in D),'zero_pivots':sum(d==0 for d in D),
                'diagonal':list(map(enc,D)), 'all_matrix_identities_checked':True})
    objective=sum(binomial(W,i)*binomial(V,i)*p[i] for i in range(69))
    U=F(binomial(1024,64),binomial(68,64))
    threshold=F(65537**28,2**128)
    excess=2**128*objective-65537**28
    require(objective==(U+1)/2,'objective from independent support ratio')
    require(excess>0,'strict threshold excess')
    floor_excess=2**128*(objective.numerator//objective.denominator)-65537**28
    require(floor_excess>0,'integer floor also strictly above threshold')
    summary=cert['summary']
    require(dec(summary['objective'])==objective and dec(summary['required_threshold'])==threshold and
            dec(summary['scaled_excess'])==excess and dec(summary['objective_ratio'])==objective/threshold,'complete objective fields')
    require(summary['candidate_feasible'] and summary['batch_ruled_out'] and not cert['failures'],'reported feasible conclusion')
    checks={'orbit_classes':len(touched),'permutation_closure':sum(map(len,closures.values())),
        'retained_variables':count,'scalar_rows':len(scalar_rows),'pair_rows':68,
        'affine_coefficient_entries':coefficient_entries,'PSD_families':len(psd_records),
        'all_normalization_distance_zeros_symmetries_checked':True,
        'min_pair_slack':enc(min(pair_slacks))}
    result={'verified':not failures,'checks':checks,'PSD_certificates':psd_records,
        'objective':enc(objective),'required_threshold':enc(threshold),'scaled_excess':enc(excess),
        'integer_floor_scaled_excess':floor_excess,
        'ratio_interval_1000':[1383,1384],
        'failures':failures,'scope':'only the selected-block relaxation; no full SDP/code/list feasibility'}
    require(F(1383,1000)<objective/threshold<F(1384,1000),'ratio interval')
    result['verified']=not failures
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print('Verified:',not failures,'; counts:',checks)
    print('Actual objective:',objective,'; required <=',threshold)
    print('Strict scaled excess:',excess,'; PSD positive/zero pivots:',[(r['k'],r['l'],r['family'],r['positive_pivots'],r['zero_pivots']) for r in psd_records])
    print('Failures:',failures,'; independent audit:',OUT)
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
