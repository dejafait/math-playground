"""Fixed L022 extension on ONLY both full (0,1) Schrijver matrices.

Streams actual orbits per entry; no optimization or full scalar closure.
All integer source coefficients are recoverable from saved beta arrays.
"""
import json
import sys
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
from selected_triple_sdp import psd_certificate

sys.set_int_max_str_digits(0)
BASE = Path(__file__).parent
OUT = BASE / 'mixed-zero-one-results.json'
W, V = 68, 956

def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]

def dec(x): return F(*x)

@lru_cache(None)
def choose(n, r): return comb(n, r) if 0 <= r <= n else 0

def beta(i, j, k, t, n):
    # Literal source expression restricted only by zero binomial factors.
    return sum((-1)**(u-t)*choose(u,t)*choose(n-2*k,u-k)
               *choose(n-k-u,i-u)*choose(n-k-u,j-u)
               for u in range(max(k,t), min(i,j,n-k)+1))

def assignment(p, i, j, h):
    if any(0 < b < 5 for b in (i,j,h)): return F(0)
    if min(i,j,h) == 0:
        a,b,c = sorted((i,j,h))
        if b != c: raise ValueError('invalid repeated-word orbit')
        return p[b]
    return p[i]*p[j]*p[h]/p[68]

def save(result): OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')

def main():
    lp=json.loads((BASE/'delsarte-lp-results.json').read_text())
    old=json.loads((BASE/'selected-triple-sdp-results.json').read_text())
    zero=json.loads((BASE/'full-zero-block-results.json').read_text())
    zero_entries={(r['i'],r['j']):r for r in zero['entries']}
    p=[F(1)]+[F(0)]*4+[F(x['numerator'],x['denominator'])/(2*comb(W,i)*comb(V,i))
                          for i,x in zip(range(5,69),lp['exact']['primal'])]
    failures=[]
    if p != list(map(dec,old['p'])): failures.append('old pair assignment mismatch')
    overlap=0
    for row in old['orbits']:
        a,b,c,u=row['key']
        if assignment(p,a,b,c) != dec(row['value']):
            failures.append('old orbit assignment mismatch '+str(row['key']))
        overlap+=1
    matrices=[[[F(0) for _ in range(68)] for _ in range(68)] for _ in range(2)]
    result={'parameters':{'n':1024,'w':68,'v':956,'d':10,'k':0,'l':1},
        'indices':list(range(1,69)), 'p':list(map(enc,p)),
        'assignment':'forbidden distance first; repeated word second; product(p_i,p_j,p_h)/p_68 otherwise',
        'scope':'fixed extension only; no full scalar or omitted-block feasibility claim',
        'stage':'construction','entries':[],'failures':failures,
        'overlap_checks':{'old_orbit_values':overlap,'old_zero_beta_w_entries':0}}
    save(result)
    orbit_count=0
    for i in range(1,69):
        for j in range(i,69):
            ts=list(range(max(0,i+j-W),min(i,j)+1))
            ss=list(range(max(0,i+j-V),min(i,j)+1))
            bw=[beta(i,j,0,t,W) for t in ts]
            bv=[beta(i,j,1,s,V) for s in ss]
            if bw != zero_entries[i,j]['beta_w']:
                failures.append('old zero beta_w mismatch '+str((i,j)))
            result['overlap_checks']['old_zero_beta_w_entries']+=1
            hc={}
            for t,a in zip(ts,bw):
                for s,b in zip(ss,bv):
                    h=i+j-t-s
                    hc[h]=hc.get(h,0)+a*b
                    orbit_count+=1
            hc={h:c for h,c in hc.items() if c}
            first=sum((c*assignment(p,i,j,h) for h,c in hc.items()),F(0))
            second=sum((c*p[h] for h,c in hc.items()),F(0))-first
            for family,val in enumerate((first,second)):
                matrices[family][i-1][j-1]=matrices[family][j-1][i-1]=val
            result['entries'].append({'i':i,'j':j,'t':ts,'s':ss,'beta_w':bw,'beta_v':bv,
                                      'h_coefficients':[[h,c] for h,c in sorted(hc.items())]})
        if i%8==0 or i==68:
            result['completed_through_row']=i
            save(result)
            print('Constructed upper rows through',i,'of 68; entries',len(result['entries']),flush=True)
    result['actual_orbit_count']=orbit_count
    result['families']=[{'matrix':[[enc(x) for x in row] for row in a]} for a in matrices]
    result['stage']='matrices_complete_before_sign_test'
    save(result)
    for family,a in enumerate(matrices):
        print('Exact sign test family',family,flush=True)
        result['families'][family]['certificate']=psd_certificate(a)
        save(result)
        c=result['families'][family]['certificate']
        print('Family',family,'PSD:',c['psd'],'stage:',c.get('stage'),flush=True)
    objective=sum(comb(W,i)*comb(V,i)*p[i] for i in range(69))
    threshold=F(65537**28,2**128)
    result['objective']=enc(objective)
    result['required_threshold']=enc(threshold)
    result['summary']={'full_matrices_constructed':True,
        'matrix_dimension':68,'upper_entries':len(result['entries']),
        'families_psd':[x['certificate']['psd'] for x in result['families']],
        'objective_above_threshold':objective>threshold,
        'fixed_extension_excluded':any(not x['certificate']['psd'] for x in result['families'])}
    result['stage']='completed'
    save(result)
    print('Actual objective:',objective,'; required <=',threshold)
    print('Summary:',result['summary'],'; consistency failures:',failures,'; certificate:',OUT)
    if failures: raise SystemExit(1)

if __name__=='__main__': main()
