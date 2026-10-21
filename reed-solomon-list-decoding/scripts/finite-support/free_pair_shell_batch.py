"""Exact rational candidate test for the gate-approved free-pair coupled shells-5–8 batch.

No optimization or full-SDP feasibility is claimed. All touched orbits are
included modulo exactly the source's distance permutations and t-s invariant.
"""
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
from math import comb
from pathlib import Path

N, W, V = 1024, 68, 956
BASE = Path(__file__).parent
OUT = BASE / 'free-pair-shell-batch-results.json'
BATCH = [(k,l,tuple(i for i in (5,6,7,8) if k<=i<=68-k and l<=i<=956-l))
         for k in range(9) for l in range(9)]
BATCH[0] = (0,0,(0,5,6,7,8,68))
BATCH += [(33,33,(33,34,35)), (34,34,(34,))]

def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]

def dec(x):
    return F(*x)

def choose(n,r):
    return comb(n,r) if 0 <= r <= n else 0

@lru_cache(None)
def beta(i,j,k,t,n):
    return sum((-1)**(u-t)*choose(u,t)*choose(n-2*k,u-k)
               *choose(n-k-u,i-u)*choose(n-k-u,j-u)
               for u in range(max(k,t), min(i,j,n-k)+1))

def orbits(i,j):
    for t in range(max(0,i+j-W),min(i,j)+1):
        for s in range(max(0,i+j-V),min(i,j)+1):
            yield (i,j,t,s)

def key(o):
    i,j,t,s=o
    return (*sorted((i,j,i+j-t-s)),t-s)

def closure(z):
    a,b,c,u=z
    result=set()
    for i,j,h in permutations((a,b,c)):
        if (i+j-h+u)%2:
            raise ValueError('nonintegral permutation index')
        t=(i+j-h+u)//2
        s=(i+j-h-u)//2
        if not (max(0,i+j-W)<=t<=min(i,j) and
                max(0,i+j-V)<=s<=min(i,j)):
            raise ValueError('invalid permuted orbit')
        result.add((i,j,t,s))
    return sorted(result)

def psd_certificate(matrix):
    """Exact symmetric elimination; zero pivots require a zero residual row.

    Saves L,D when PSD. Otherwise saves a rational negative quadratic
    witness in original coordinates (including the zero-diagonal case).
    """
    n=len(matrix)
    r=[row[:] for row in matrix]
    transform=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    stages=[]
    for k in range(n):
        pivot=r[k][k]
        if pivot < 0:
            v=[transform[i][k] for i in range(n)]
            return {'psd':False,'stage':k,'reason':'negative pivot',
                    'negative_vector':list(map(enc,v)), 'quadratic':enc(pivot),
                    'stages':stages}
        if pivot == 0:
            j=next((j for j in range(k+1,n) if r[k][j]),None)
            if j is not None:
                # q(e_j+c e_k)=r_jj+2c*r_kj. Choose it to be -1.
                c=-(r[j][j]+1)/(2*r[k][j])
                v=[transform[i][j]+c*transform[i][k] for i in range(n)]
                return {'psd':False,'stage':k,'reason':'zero pivot nonzero row',
                        'negative_vector':list(map(enc,v)), 'quadratic':enc(-1),
                        'stages':stages}
            stages.append({'pivot':enc(0),'row_zero':True})
            continue
        factors=[r[k][j]/pivot for j in range(k+1,n)]
        stages.append({'pivot':enc(pivot),'factors':list(map(enc,factors))})
        for j in range(k+1,n):
            for i in range(n):
                transform[i][j]-=factors[j-k-1]*transform[i][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                r[i][j]-=factors[i-k-1]*pivot*factors[j-k-1]
        for j in range(k+1,n):
            r[k][j]=r[j][k]=F(0)
    return {'psd':True,'stages':stages,
            'congruence':[[enc(x) for x in row] for row in transform],
            'diagonal':list(map(enc,(r[i][i] for i in range(n))))}

def main():
    # Construction and cap test precede expensive coefficient generation.
    touched=set()
    for k,l,indices in BATCH:
        for i,j in combinations_with_replacement(indices,2):
            touched.update(key(o) for o in orbits(i,j))
    # All pair variables are also actual repeated-word orbits.
    touched.update((0,i,i,0) for i in range(W+1))
    keys=sorted(touched)
    orbit_closure={z:closure(z) for z in keys}
    active=[z for z in keys if z[0]>0 and not any(0<h<5 for h in z[:3])]
    row_count=sum(1+2*len(set((o[0],o[1]) for o in orbit_closure[z])) for z in keys)
    cap_ok=len(active)+64<=20000 and row_count+68<=200000
    result={'parameters':{'n':N,'w':W,'d':10},
            'scope':'approved free-pair two-family shells-5–8 batch; no solve or retuning',
            'construction':{'retained_orbit_variables':len(active)+64,
                'distinct_triple_variables':len(active),
                'orbit_classes_including_fixed':len(keys),
                'permutation_closure_count':sum(map(len,orbit_closure.values())),
                'scalar_rows':row_count+68, 'variable_cap':20000,
                'scalar_row_cap':200000,'caps_passed':cap_ok},
            'failures':[]}
    OUT.with_name('free-pair-shell-batch-initial-state.json').write_text(json.dumps(result,indent=2)+'\n')
    if not cap_ok:
        result['failures'].append('construction cap exceeded; no mathematical impossibility claim')
        OUT.write_text(json.dumps(result,indent=2)+'\n')
        print('Construction cap exceeded:',result['construction'], 'path:',OUT)
        return
    lp=json.loads((BASE/'delsarte-lp-results.json').read_text())
    p=[F(1)]+[F(0)]*4
    for i,x in zip(range(5,W+1),lp['exact']['primal']):
        p.append(F(x['numerator'],x['denominator'])/(2*comb(W,i)*comb(V,i)))
    lam=p[68]
    values={}
    rows=[]
    for z in keys:
        a,b,c,u=z
        if any(0<h<5 for h in (a,b,c)):
            value=F(0)
        elif a==0:
            value=p[b]
        else:
            value=p[a]*p[b]*p[c]/lam
        values[z]=value
        rows.append({'key':list(z),'kind':'nonnegative','slack':enc(value)})
        for i,j in sorted(set((o[0],o[1]) for o in orbit_closure[z])):
            rows.append({'key':list(z),'kind':'upper','i':i,'j':j,
                         'slack':enc(p[i]-value)})
            rows.append({'key':list(z),'kind':'lower','i':i,'j':j,
                         'slack':enc(1+value-p[i]-p[j])})
    pair_rows=[]
    for j in range(1,W+1):
        coefficients=[sum((-1)**h*choose(j,h)*choose(W-j,i-h)*choose(V-j,i-h)
                          for h in range(i+1)) for i in range(5,W+1)]
        slack=1+sum(c*p[i] for i,c in zip(range(5,W+1),coefficients))
        pair_rows.append({'j':j,'coefficients':coefficients,'slack':enc(slack)})
    blocks=[]
    for k,l,indices in BATCH:
        coeffs=[]
        matrices=[[[F(0) for j in indices] for i in indices] for b in range(2)]
        for ri,i in enumerate(indices):
            for rj in range(ri,len(indices)):
                j=indices[rj]
                ycoeff={}
                pcoeff={}
                original_orbits=[]
                for o in orbits(i,j):
                    _,_,t,s=o
                    c=beta(i,j,k,t,W)*beta(i,j,l,s,V)
                    original_orbits.append([o[2],o[3],list(key(o)),c])
                    if c:
                        z=key(o)
                        ycoeff[z]=ycoeff.get(z,0)+c
                        h=i+j-t-s
                        pcoeff[h]=pcoeff.get(h,0)+c
                ycoeff={z:c for z,c in ycoeff.items() if c}
                pcoeff={h:c for h,c in pcoeff.items() if c}
                first=sum(c*values[z] for z,c in ycoeff.items())
                second=sum(c*p[h] for h,c in pcoeff.items())-first
                matrices[0][ri][rj]=matrices[0][rj][ri]=first
                matrices[1][ri][rj]=matrices[1][rj][ri]=second
                coeffs.append({'i':i,'j':j,'original_orbits':original_orbits,'y':[[list(z),c] for z,c in sorted(ycoeff.items())],
                               'p':[[h,c] for h,c in sorted(pcoeff.items())]})
        blocks.append({'k':k,'l':l,'indices':list(indices),'coefficients':coeffs,
            'families':[{'matrix':[[enc(x) for x in row] for row in matrix],
                         'certificate':psd_certificate(matrix)} for matrix in matrices]})
    scalar_failed=[r for r in rows if dec(r['slack'])<0]
    pair_failed=[r['j'] for r in pair_rows if dec(r['slack'])<0]
    psd_failed=[(b['k'],b['l'],f) for b in blocks for f,x in enumerate(b['families'])
                if not x['certificate']['psd']]
    objective=sum(comb(W,i)*comb(V,i)*p[i] for i in range(W+1))
    threshold=F(65537**28,2**128)
    result.update({'candidate':'one-half L021 pair witness; distinct triples product(p_i,p_j,p_h)/p_68',
        'p':list(map(enc,p)), 'normalization':{'p_0':enc(p[0]),'p_1_through_4_zero':all(p[i]==0 for i in range(1,5))},
        'orbits':[{'key':list(z),'closure':list(map(list,orbit_closure[z])),
                   'value':enc(values[z])} for z in keys],
        'scalar_rows':rows,'pair_rows':pair_rows,'blocks':blocks,
        'summary':{'scalar_failed_count':len(scalar_failed),'pair_failed_rows':pair_failed,
            'psd_failed_blocks':psd_failed,'objective':enc(objective),
            'required_threshold':enc(threshold),'objective_ratio':enc(objective/threshold),
            'scaled_excess':enc(2**128*objective-65537**28),
            'candidate_feasible':not(scalar_failed or pair_failed or psd_failed),
            'integer_threshold_K':65537**28//2**128,
            'objective_at_least_K_plus_one':objective>=65537**28//2**128+1,
            'objective_above_threshold':objective>threshold,
            'batch_ruled_out':not(scalar_failed or pair_failed or psd_failed) and objective>=65537**28//2**128+1}})
    if scalar_failed: result['failures'].append('candidate violates scalar constraints')
    if pair_failed: result['failures'].append('candidate violates basic pair inequalities')
    if psd_failed: result['failures'].append('candidate violates selected PSD constraints')
    OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print('Construction:', result['construction'])
    print('Exact candidate objective:', objective, '; required <=',threshold)
    print('Scalar failures:',len(scalar_failed),'; pair failures:',len(pair_failed),'; PSD failures:',len(psd_failed),'of',2*len(blocks))
    print('Feasible:',result['summary']['candidate_feasible'],'; batch ruled out:',result['summary']['batch_ruled_out'])
    print('Failures:',result['failures'],'; full certificate:',OUT)

if __name__=='__main__': main()
