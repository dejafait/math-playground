"""Separate L076 audit: exact full orbit action and saved elimination identities.

Imports no notebook implementation. No optimization or energy computation.
"""
import hashlib
import itertools as it
import json
import sys
from collections import Counter
from fractions import Fraction as F
from math import comb, gcd, isqrt, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-distance-full-base-kernel-critical-audit.json'


def c(n, k):
    return comb(n,k) if 0 <= k <= n else 0


def enc(x):
    if isinstance(x,F): return [x.numerator,x.denominator]
    if isinstance(x,dict): return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [enc(v) for v in x]
    return x


def mat(x): return [[F(*v) for v in r] for r in x]


def primitive(row):
    d=lcm(*(F(x).denominator for x in row))
    a=[int(x*d) for x in row]
    g=gcd(*a)
    return [x//g for x in a] if g else a


def rank_mod(A, p=2147483647):
    A=[[x%p for x in row] for row in A]; r=0
    for j in range(len(A[0])):
        s=next((s for s in range(r,len(A)) if A[s][j]),None)
        if s is None: continue
        A[r],A[s]=A[s],A[r]
        u=pow(A[r][j],-1,p)
        A[r]=[x*u%p for x in A[r]]
        for s in range(r+1,len(A)):
            v=A[s][j]
            if v: A[s]=[(x-v*y)%p for x,y in zip(A[s],A[r])]
        r+=1
        if r==len(A): break
    return r


def main():
    names=['eight-distance-full-base-kernel-results.json',
           'eight-distance-full-base-kernel-verification.json',
           'maximizer-excluded-anchor-results.json',
           'maximizer-excluded-anchor-critical-audit.json']
    paths=[ROOT/n for n in names]
    data,ver,src,old=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def ck(name,ok):
        checks.append(name)
        if not ok: failures.append(name)
    for path,obj in zip(paths,[data,ver,src,old]):
        ck('clean_'+path.name,obj['failures']==[])
        for rel,h in obj.get('input_hashes',{}).items():
            ck('immutable_'+path.name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    ck('fresh_verification_hash',ver['constructor_sha256']==hashlib.sha256(paths[0].read_bytes()).hexdigest())
    ck('prime',all(2147483647%d for d in range(2,isqrt(2147483647)+1)))
    ck('all_imported_original_parameters',src['parameters']==old['parameters'] and
       src['original_column']==old['column'] and src['completion_z']==old['z'] and
       src['rho']==old['rho'] and src['pairs_through_14']==old['pairs'])
    base={tuple(r['type']):F(*r['y']) for r in src['entries']}
    ck('all_imported_original_entries',base=={tuple(r['type']):F(*r['y']) for r in old['entries']})
    ck('base_domain',set(base)=={(l,m,k,h) for l in [5,6,7] for m in [5,6,7] if l<=m
        for k in range(l+1) for h in range(l+1)})
    for l,m,k,h in list(base): base[m,l,k,h]=base[l,m,k,h]
    p=[F(*v) for v in src['pairs_through_14']]
    ck('manuscript_p8',p[8]==F(16792471,1181138102168120460)>0)
    for l in [5,6,7]: ck('Boolean_base_'+str(l),base[l,l,l,l]==p[l])
    os=[(0,0,0)]+[(l,i,j) for l in [5,6,7] for i,j in it.product(range(l+1),repeat=2)]
    W=[1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in os[1:]]
    ck('orbit_domain',data['orbits']==list(map(list,os)) and data['weights']==W and min(W)>0)
    kinds=Counter(r['kind'] for r in data['column'])
    ck('manuscript_class_counts',dict(kinds)=={'anchor':1,'represented':45,'forbidden':19,'free':85})
    ck('unique_free_keys',len(set(map(tuple,data['free_keys'])))==85)
    # Count transitions by choices inside X', using s=|X' intersect X intersect U|.
    T={}
    for n in [68,956]:
        for l,m in it.product([5,6,7],repeat=2):
            for k in range(min(l,m)+1):
                T[n,l,m,k]=[[sum(c(i,s)*c(8-i,u-s)*c(l-i,k-s)*c(n-8-l+i,m-u-k+s)
                    for s in range(max(0,u-(8-i),k-(l-i)),min(i,u,k)+1))
                    for u in range(m+1)] for i in range(l+1)]
    saved={tuple(r['indices']):r['matrix'] for r in data['complete_transitions']}
    ck('complete_transition_keys',set(saved)==set(T) and len(saved)==len(data['complete_transitions'])==118)
    transition_balance=[]
    for (n,l,m,k),A in T.items():
        ck('every_count_'+str((n,l,m,k)),A==saved[n,l,m,k])
        residuals=[[c(8,i)*c(n-8,l-i)*A[i][u]-c(8,u)*c(n-8,m-u)*T[n,m,l,k][u][i]
            for u in range(m+1)] for i in range(l+1)]
        ck('reverse_weighted_transition_'+str((n,l,m,k)),not any(x for r in residuals for x in r))
        transition_balance.append({'indices':[n,l,m,k],'residuals':residuals})
    # Rebuild the entire Q by direct tensor subset counts, without gamma or modes.
    Q=[[F(0) for _ in os] for _ in os]
    Q[0][0]=F(1)
    index={o:i for i,o in enumerate(os)}
    for z,(l,i,j) in enumerate(os[1:],1): Q[0][z]=p[l]*W[z]; Q[z][0]=p[l]
    for l,m in it.product([5,6,7],repeat=2):
        d=lcm(*(base[l,m,k,h].denominator for k,h in it.product(range(min(l,m)+1),repeat=2)))
        Y=[[int(base[l,m,k,h]*d) for h in range(min(l,m)+1)] for k in range(min(l,m)+1)]
        for i,u in it.product(range(l+1),range(m+1)):
            partial=[sum(T[68,l,m,k][i][u]*Y[k][h] for k in range(min(l,m)+1)) for h in range(min(l,m)+1)]
            for j,v in it.product(range(l+1),range(m+1)):
                Q[index[l,i,j]][index[m,u,v]]=F(sum(partial[h]*T[956,l,m,h][j][v] for h in range(min(l,m)+1)),d)
    for i,row in enumerate(Q): ck('full_action_weighted_symmetry_'+str(i),all(W[i]*x==W[j]*Q[j][i] for j,x in enumerate(row)))
    Qi=[primitive(row) for row in Q]
    ck('full_action_modular_rank',rank_mod(Qi)==60)
    K=mat(data['kernel_basis']); Ki=[primitive(v) for v in K]
    ck('full_kernel_modular_independence',len(K)==90 and rank_mod(Ki)==90)
    full_residuals=[]
    for t,v in enumerate(Ki):
        residual=[sum(x*y for x,y in zip(row,v)) for row in Qi]
        full_residuals.append(residual)
        ck('all_150_direct_action_residuals_'+str(t),not any(residual))
    print('Direct action: rank 60; 90 independent vectors; all 13500 residuals checked.',flush=True)
    # Verify every saved fraction-free elimination operation is invertible, then
    # independently finish rational back reduction and compare the entire RREF.
    operation_counts=[]
    def replay(label,A,operations,pivots,expected):
        rows=[]
        for row in A:
            d=lcm(*(x.denominator for x in row)); rows.append([int(x*d) for x in row])
        for t,op in enumerate(operations):
            tag=op[0]; valid=True
            if tag=='swap':
                _,a,b=op; rows[a],rows[b]=rows[b],rows[a]
            elif tag=='divide':
                _,a,g=op; valid=g!=0 and all(x%g==0 for x in rows[a])
                if valid: rows[a]=[x//g for x in rows[a]]
            elif tag=='eliminate':
                _,a,b,x,y,g=op; valid=a!=b and x!=0
                new=[x*v-y*w for v,w in zip(rows[a],rows[b])]
                valid=valid and (g==0 and not any(new) or g!=0 and all(v%g==0 for v in new))
                if valid: rows[a]=[v//g for v in new] if g else new
            else: valid=False
            ck('invertible_operation_'+label+'_'+str(t),valid)
        rows=[[F(x) for x in row] for row in rows]
        ck('echelon_pivots_'+label,[next((j for j,x in enumerate(row) if x),None) for row in rows]==pivots+[None]*(len(rows)-len(pivots)))
        for r in reversed(range(len(pivots))):
            j=pivots[r]; z=rows[r][j]; rows[r]=[x/z for x in rows[r]]
            for s in range(r):
                z=rows[s][j]; rows[s]=[x-z*y for x,y in zip(rows[s],rows[r])]
        ck('complete_RREF_'+label,rows==mat(expected))
        operation_counts.append({'label':label,'operations':len(operations),'pivots':pivots})
        return rows
    factors={(r['n'],r['layer']):r for r in data['factor_bases']}
    for block in data['blocks']:
        label=str(tuple(block['mode'])); B=mat(block['action']); ns=[F(*x) for x in block['norms']]
        a,b=block['mode']
        expected_ns=[F(1) if l==0 else F(*factors[68,l]['norms'][a])*F(*factors[956,l]['norms'][b]) for l in block['layers']]
        ck('actual_block_norms_'+label,ns==expected_ns)
        ck('block_weighted_symmetry_'+label,all(ns[i]*B[i][j]==ns[j]*B[j][i] for i in range(len(B)) for j in range(len(B))))
        replay(label,B,block['operations'],block['pivots'],block['rref'])
    E=mat(data['equations']); rhs=[F(*x) for x in data['rhs']]
    R=replay('compatibility',[row+[v] for row,v in zip(E,rhs)],data['equation_operations'],data['equation_pivots'],data['equation_rref'])
    ck('compatibility_rank_and_consistency',len(data['equation_pivots'])==81 and 85 not in data['equation_pivots'])
    nonpiv=[j for j in range(85) if j not in data['equation_pivots']]
    intercept=[F(0)]*85; slopes=[[F(0)]*4 for _ in range(85)]
    for t,j in enumerate(nonpiv): slopes[j][t]=F(1)
    for r,j in enumerate(data['equation_pivots']): intercept[j]=R[r][-1]; slopes[j]=[-R[r][t] for t in nonpiv]
    ck('canonical_affine_recipe',enc(intercept)==data['affine']['intercept'] and enc(slopes)==data['affine']['slopes'] and nonpiv==[56,63,69,78])
    active=[27,33,56,63]
    ck('active_invertible',rank_mod([primitive(slopes[j]) for j in active])==4)
    params=[F(*x) for x in data['chosen_parameters']]
    sol=[x+sum(a*t for a,t in zip(row,params)) for x,row in zip(intercept,slopes)]
    ck('unique_active_solution',all(sol[j]==0 for j in active) and enc(sol)==data['solution'])
    for j,x in enumerate(sol): ck('free_sign_'+str(j),x==0 if j in active else x>0)
    zero_keys=[data['free_keys'][j] for j in active]
    ck('manuscript_zero_keys',zero_keys==[[948,0,0,8,2,6,6,54],[947,1,1,7,3,5,5,55],[948,0,0,8,1,7,7,53],[947,1,1,7,2,6,6,54]])
    column=[F(*v) for v in data['complete_column']]
    residuals=[sum(w*x*y for w,x,y in zip(W,v,column)) for v in K]
    for t,x in enumerate(residuals): ck('original_weighted_column_residual_'+str(t),x==0)
    initial=json.loads((ROOT/'eight-distance-full-base-kernel-critical-audit-initial.json').read_text())
    ck('preserved_initial_failure',initial['failures']==['canonical_affine_recipe'])
    ck('initial_affine_encoding_only',[[F(*x) if isinstance(x,list) else F(x) for x in row] for row in initial['affine_slopes']]==slopes)
    for key,value in {'direct_orbit_action':Q,'primitive_action':Qi,'primitive_kernel':Ki,
        'direct_action_residuals':full_residuals,'complete_compatibility_rref':R,
        'affine_intercept':intercept,'solution':sol,'original_weighted_residuals':residuals}.items():
        ck('initial_math_unchanged_'+key,initial[key]==enc(value))
    summary={'verdict':'AUDIT_FAILURE' if failures else 'RETAIN_L076','checks':len(checks),'failures':len(failures),
        'orbits':150,'full_orbit_action_rank':60,'independent_kernel_vectors':90,'direct_action_residuals':13500,
        'transition_matrices':118,'blocks':64,'replayed_operations':sum(x['operations'] for x in operation_counts),
        'equation_rank':81,'affine_dimension':4,'positive_free':81,'zero_free':4,
        'actual_minimum_free':min(sol),'required_minimum_free':0,'weighted_residuals':len(residuals),
        'all_weighted_residuals_zero':not any(residuals),'energy_tested':False}
    result={'summary':summary,'checks':checks,'failures':failures,
        'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'transition_reverse_balance':transition_balance,'direct_orbit_action':Q,'primitive_action':Qi,
        'primitive_kernel':Ki,'direct_action_residuals':full_residuals,'operation_counts':operation_counts,
        'complete_compatibility_rref':R,'affine_intercept':intercept,'affine_slopes':slopes,
        'solution':sol,'zero_keys':zero_keys,'original_weighted_residuals':residuals}
    OUT.write_text(json.dumps(enc(result),indent=2)+'\n')
    print(json.dumps(enc(summary),sort_keys=True),flush=True)
    print('Required: free minimum >= 0; all 90 weighted residuals = 0. Energy untested.')
    print('Full certificate:',OUT.relative_to(NB))
    if failures:
        print('Failures:',failures); raise SystemExit(1)


if __name__=='__main__': main()
