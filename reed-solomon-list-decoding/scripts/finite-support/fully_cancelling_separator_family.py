"""L082's unchanged separator over L076's entire original affine domain.
Exact reconstruction; no new separator, optimizer or completion search.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path
from functools import lru_cache
from verify_simultaneous_eight_shell import C, beta, det, cramer, basis_solve, enc
sys.set_int_max_str_digits(0)
beta=lru_cache(None)(beta)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'fully-cancelling-separator-family-results.json'
def dot(a,b):
    assert len(a)==len(b)
    return sum((x*y for x,y in zip(a,b)),F(0))
def av(x):return [F(x)]+[F(0)]*4
def quadratic(M,z):return dot(z,[dot(r,z) for r in M])
def main():
    names=['eight-family-fixed-separator-results.json',
           'eight-family-fixed-separator-critical-audit.json',
           'eight-distance-full-base-kernel-results.json',
           'maximizer-excluded-anchor-results.json',
           'eight-common-column-joint-completion-results.json',
           'eight-common-column-joint-completion-critical-audit.json']
    paths=[ROOT/n for n in names]
    family,fa,col,old,fixed82,audit=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def check(name,ok):
        checks.append(name)
        if not ok:failures.append(name)
    out={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        out.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    for name,obj in zip(names,[family,fa,col,old,fixed82,audit]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('input_binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    fs=[[F(*v)]+[F(*x) for x in row] for v,row in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('identical_85_row_domain',enc(fs)==family['domain']['nonnegative_affine'] and col['affine']['free_indices']==[56,63,69,78])
    for j,(row,rhs) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_affine_kernel_'+str(j),[sum(F(*v)*f[k] for v,f in zip(row,fs)) for k in range(5)]==av(F(*rhs)))
    p=[F(*v) for v in old['pairs_through_14']]
    check('original_normalization',F(*old['rho'])>0 and p[8]==F(16792471,1181138102168120460)>0)
    entries={tuple(r['type']):None if r['affine'] is None else [F(*x) for x in r['affine']] for r in family['records']}
    check('all_500_types_3000_presentations',len(entries)==500 and sum(len(r['presentations']) for r in family['records'])==3000)
    check('unchanged_full_key_domain',not family['domain']['key_equalities'] and not any(any(F(*v) for v in r) for r in family['domain']['all_key_residuals']))
    for rec in family['records']:
        y=entries[tuple(rec['type'])]
        for j,pr in enumerate(rec['presentations']):
            if pr['affine'] is not None:
                check('key_coefficients_'+str((rec['type'],j)),[F(*v) for v in pr['affine']]==y)
    check('270_unchanged_old_entries',all(entries[tuple(r['type'])]==av(F(*r['y'])) for r in old['entries']))
    free=[tuple(rq) for rq in family['free']]
    check('45_free_36_forced',free==[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8] and sum(l==m==8 and v is not None for (l,m,i,j),v in entries.items())==36)
    rr=[[F(*v) for v in r] for r in col['equation_rref']]
    reconstructed=[[F(0)]*5 for _ in range(85)]
    nonpiv=[56,63,69,78]
    for k,j in enumerate(nonpiv):reconstructed[j][k+1]=F(1)
    for i,j in enumerate(col['equation_pivots']):reconstructed[j]=[rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    check('complete_RREF_reconstruction',fs==reconstructed and len(col['equation_pivots'])==81)
    base={tuple(r['type']):av(F(*r['y'])) for r in old['entries']}
    column=[]
    for r in col['column']:
        v=[p[8]*x for x in fs[r['variable']]] if r['kind']=='free' else av(F(*r['value']))
        column.append(v)
        if r['orbit']!=[0,0,0]:base[r['orbit'][0],8,*r['orbit'][1:]]=v
    W=[1]+[C(8,i)*C(60,l-i)*C(8,j)*C(948,l-j) for l,i,j in col['orbits'][1:]]
    kernel_residuals=[]
    check('full_weighted_dimensions',len(column)==len(W)==150 and len(col['kernel_basis'])==90)
    for i,row in enumerate(col['kernel_basis']):
        residual=[sum(F(*v)*w*f[k] for v,w,f in zip(row,W,column)) for k in range(5)]
        check('all_affine_weighted_kernel_'+str(i),residual==[0]*5);kernel_residuals.append(residual)
    key_values={};free_keys=[]
    for rec in family['records']:
        l,m,i,j=rec['type'];atoms=[956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        sets=[set(),set(),set()];start=0
        for mask,n in enumerate(atoms):
            for S,bit in zip(sets,[4,2,1]):
                if mask&bit:S.update(range(start,start+n))
            start+=n
        check('actual_sets_'+str(rec['type']),min(atoms)>=0 and start==1024 and all(len(S)==68 for S in sets))
        orders=[];values=[]
        for k,(D,E,G) in enumerate(it.permutations(sets)):
            aa=[0]*8
            for x in range(1024):aa[4*(x in D)+2*(x in E)+(x in G)]+=1
            ds=[len(D-E),len(D-G),len(E-G)]
            if 0 in ds:v=av(p[max(ds)])
            elif any(0<d<5 for d in ds):v=av(0)
            else:v=base.get((*sorted(ds[:2]),len((D-E)&(D-G)),len((E-D)&(G-D))))
            saved=rec['presentations'][k]
            check('all_actual_affine_presentations_'+str((rec['type'],k)),aa==saved['atoms'] and ds==saved['distances'] and enc(v)==saved['affine'])
            orders.append(tuple(aa))
            if v is not None:values.append(v)
        key=min(orders)
        if key in key_values:values.append(key_values[key])
        value=values[0] if values else None
        check('all_shared_affine_keys_'+str(rec['type']),list(key)==rec['key'] and enc(value)==rec['affine'] and all(v==value for v in values))
        if value is None:free_keys.append(key)
        else:key_values[key]=value
    check('distinct_full_free_keys',len(free_keys)==len(set(free_keys))==45)
    out.update(affine_column=column,weighted_kernel_residuals=kernel_residuals)
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b; layers=[l for l in [5,6,7] if max(a,b)<=l]
        def block(l,m):
            ll,mm=sorted([l,m]);v=av(0)
            for i,j in it.product(range(ll+1),repeat=2):
                coef=beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)
                v=[x+coef*y for x,y in zip(v,entries[ll,mm,i,j])]
            if a==b==0:v[0]-=p[l]*p[m]*sizes[l]*sizes[m]
            return v
        B=[[block(l,m)[0] for m in layers] for l in layers]
        cross=[block(l,8) for l in layers];selected=[];minors=[]
        for k in range(1,len(B)+1):
            for inds in it.combinations(range(len(B)),k):
                d=det([[B[i][j] for j in inds] for i in inds]);minors.append(d)
                check('old_psd_'+str((a,b,inds)),d>=0)
                if d>0:selected=inds
        X=[[F(0)]*5 for _ in B]
        if selected:
            BB=[[B[i][j] for j in selected] for i in selected]
            for k in range(5):
                for j,v in zip(selected,cramer(BB,[cross[i][k] for i in selected])):X[j][k]=v
        residuals=[[sum(B[i][j]*X[j][k] for j in range(len(B)))-cross[i][k] for k in range(5)] for i in range(len(B))]
        check('all_affine_singular_ranges_'+str(idx),not any(any(r) for r in residuals))
        D8=C(68-2*a,8-a)*C(956-2*b,8-b)
        check('positive_normalization_'+str(idx),D8>0)
        cost=[[sum(cross[j][k]*X[j][h] for j in range(len(B)))/(p[8]*D8) for h in range(5)] for k in range(5)]
        fixed=av(0)
        for (l,m,i,j),y in entries.items():
            if l==m==8 and y is not None:
                coef=F(beta(68,8,8,a,i)*beta(956,8,8,b,j),p[8]*D8)
                fixed=[x+coef*v for x,v in zip(fixed,y)]
        if a==b==0:fixed[0]-=p[8]*sizes[8]
        row=[-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D8*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        saved=family['modes'][idx]
        check('common_family_mode_'+str(idx),enc(cost)==saved['required_quadratic'] and enc(fixed)==saved['fixed_minus_anchor_affine'] and enc(cross)==saved['cross_affine'] and enc(B)==saved['base'])
        check('original_mode_row_'+str(idx),enc(row)==family['matrix'][idx]==fixed82['matrix'][idx])
        Q=[[-v for v in r] for r in cost];Q[0][0]+=fixed[0]
        for j in range(1,5):Q[0][j]+=fixed[j]/2;Q[j][0]+=fixed[j]/2
        check('symmetric_mode_quadratic_'+str(idx),Q==list(map(list,zip(*Q))))
        modes.append({'mode':[a,b],'base':B,'cross':cross,'inverse_affine':X,'range_residuals':residuals,'cost':cost,'fixed_minus_anchor':fixed,'quadratic':Q,'D8':D8})
        matrix.append(row)
    out.update(domain=fs,free=free,modes=modes,matrix=matrix)
    save('common_mode_system_rebuilt')
    print('Common system: 85 domain rows; 500 keys/3000 presentations; 81 modes; failures:',failures,flush=True)
    manuscript=(NB/'lemmas/L082-common-column-joint-completion-obstruction.md').read_text()
    match=re.search(r'I=\((.*?)\),\s*J=\((.*?)\)\.',manuscript,re.S)
    assert match is not None
    I=[int(v) for v in re.findall(r'-?\d+',match.group(1))]
    J=[-1]+list(range(45))
    check('exact_canonical_dimensions',len(I)==len(J)==46 and match.group(2).replace(' ','').replace('\n','')=='-1,0,1,...,44')
    K=[[F(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
    yy,pivots=basis_solve(list(map(list,zip(*K))),[F(-1)]+[F(0)]*45)
    y=[F(0)]*81
    for i,v in zip(I,yy):y[i]=v
    check('unchanged_canonical_weights',all(pivots) and min(y)>=0 and sum(y)==1 and sum(v>0 for v in y)==28 and enc(y)==fixed82['exact']['dual'])
    sums=[sum(w*r[j] for w,r in zip(y,matrix)) for j in range(45)]
    # Compute raw coefficients independently, not by multiplying saved sums.
    raw=[-sum(y[9*a+b]*F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*modes[9*a+b]['D8']) for a,b in it.product(range(9),repeat=2)) for r,q in free]
    check('45_original_and_raw_cancellations',sums==raw==[0]*45 and enc(sums)==fixed82['exact']['sums'] and enc(raw)==fixed82['exact']['raw_sums'])
    M=[[sum(y[k]*modes[k]['quadratic'][i][j] for k in range(81)) for j in range(5)] for i in range(5)]
    check('symmetric_full_pairing',M==list(map(list,zip(*M))))
    check('only_original_t78_dependence',all(M[i][j]==0 for i in [1,2,3] for j in range(5)))
    check('negative_nonzero_curvature',M[4][4]<0)
    s=-M[0][4]/M[4][4]
    check('exact_negative_square',M[0][0]*M[4][4]==M[0][4]**2)
    # Preserve the rejected common point as an original-row checksum.
    oldpoint=[F(*v) for v in fixed82['point']]
    check('L082_fixed_point_pairing_retained',enc(quadratic(M,oldpoint))==fixed82['exact']['value'])
    endpoints=[]
    for inds in [[27,33,56,63],[5,26,33,56]]:
        t=cramer([fs[j][1:] for j in inds],[-fs[j][0] for j in inds]);z=[F(1)]+t
        factors=[dot(f,z) for f in fs]
        check('all_endpoint_domain_rows_'+str(inds),min(factors)>=0)
        endpoints.append({'active_indices':inds,'point':z,'factors':factors})
    z0,z1=[v['point'] for v in endpoints]
    check('stationary_parameter_strictly_between',z0[4]<s<z1[4])
    alpha=(s-z0[4])/(z1[4]-z0[4]);point=[(1-alpha)*a+alpha*b for a,b in zip(z0,z1)]
    factors=[dot(f,point) for f in fs]
    check('convex_interpolation_and_all_85_signs',0<alpha<1 and point[0]==1 and point[4]==s and min(factors)>=0)
    bounds=[quadratic(m['quadratic'],point) for m in modes]
    value=dot(y,bounds)
    check('attained_exact_zero_full_pairing',value==quadratic(M,point)==0)
    for i,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('witness_original_equation_'+str(i),dot([F(*v) for v in r],factors)==F(*b))
    actual_column=[dot(v,point) for v in column]
    for i,k in enumerate(col['kernel_basis']):
        check('witness_full_weighted_kernel_'+str(i),sum(F(*v)*w*f for v,w,f in zip(k,W,actual_column))==0)
    out.update(I=I,J=J,pivots=pivots,weights=y,scaled_sums=sums,raw_sums=raw,M=M,
               square={'coefficient':M[4][4],'stationary_t78':s,'constant_residual':M[0][0]-M[0][4]**2/M[4][4]},
               endpoints=endpoints,alpha=alpha,point=point,factors=factors,bounds=bounds,value=value)
    out['summary']={'verdict':'ATTAINED_ZERO_MAXIMUM' if not failures else 'FAILED',
                    'checks':len(checks),'failures':len(failures),'curvature_rank':1,
                    'actual_pairing':value,'required_nonnegative_pairing':0,
                    'actual_minimum_factor':min(factors),'required_minimum_factor':0,
                    'positive_factors':sum(v>0 for v in factors),'zero_factors':[j for j,v in enumerate(factors) if not v],
                    'positive_weights':sum(v>0 for v in y),'zero_scaled_coefficients':sum(v==0 for v in sums),
                    'zero_raw_coefficients':sum(v==0 for v in raw)}
    save('completed');print(enc(out['summary']),flush=True)
    print('Full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)
if __name__=='__main__':main()
