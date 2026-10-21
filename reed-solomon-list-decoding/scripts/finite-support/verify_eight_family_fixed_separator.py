"""Independent exact reconstruction; standard library only, no notebook imports."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'eight-family-fixed-separator-verification.json'


def enc(x):
    if isinstance(x,Q):return [x.numerator,x.denominator]
    if isinstance(x,dict):return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [enc(v) for v in x]
    return x


def C(n,k):return comb(n,k) if 0<=k<=n else 0


@lru_cache(None)
def beta(n,l,m,a,k):
    return sum((-1)**(u-k)*C(u,k)*C(n-2*a,u-a)*C(n-a-u,l-u)*C(n-a-u,m-u)
               for u in range(max(a,k),min(l,m,n-a)+1))


def solve(A,b):
    n=len(b);M=[[Q(x) for x in r]+[Q(v)] for r,v in zip(A,b)]
    for j in range(n):
        k=next(k for k in range(j,n) if M[k][j]);M[j],M[k]=M[k],M[j]
        d=M[j][j];M[j]=[x/d for x in M[j]]
        for k in range(n):
            if k!=j:
                d=M[k][j];M[k]=[x-d*y for x,y in zip(M[k],M[j])]
    return [r[-1] for r in M]


def determinant(A):
    M=[r[:] for r in A];d=Q(1)
    for j in range(len(M)):
        k=next((k for k in range(j,len(M)) if M[k][j]),None)
        if k is None:return Q(0)
        if k!=j:M[j],M[k]=M[k],M[j];d=-d
        v=M[j][j];d*=v
        for k in range(j+1,len(M)):
            q=M[k][j]/v
            for h in range(j+1,len(M)):M[k][h]-=q*M[j][h]
    return d


def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))


def av(x):return [Q(x)]+[Q(0)]*4


def main():
    paths=[ROOT/n for n in ['eight-family-fixed-separator-results.json',
          'maximizer-excluded-anchor-results.json','eight-distance-full-base-kernel-results.json',
          'simultaneous-eight-shell-results.json']]
    data,old,col,fixed=[json.loads(p.read_text()) for p in paths]
    checks=[];failures=[]
    def check(n,v):
        checks.append(n)
        if not v:failures.append(n)
    check('constructor_clean',not data['failures'])
    for rel,h in data['input_hashes'].items():check('hash_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p=[Q(*x) for x in old['pairs_through_14']]
    check('original_rho_p8',Q(*old['rho'])>0 and p[8]==Q(16792471,1181138102168120460)>0 and old['pairs_through_14']==col['pairs_through_14'])
    fs=[[Q(*c)]+[Q(*x) for x in r] for c,r in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('original_affine_family',enc(fs)==data['domain']['nonnegative_affine'] and col['affine']['free_indices']==[56,63,69,78])
    for j,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('all_five_kernel_coefficients_'+str(j),[sum(Q(*v)*f[k] for v,f in zip(r,fs)) for k in range(5)]==av(Q(*b)))
    base={tuple(r['type']):av(Q(*r['y'])) for r in old['entries']}
    for r in col['column'][1:]:
        base[r['orbit'][0],8,*r['orbit'][1:]]=[p[8]*x for x in fs[r['variable']]] if r['kind']=='free' else av(Q(*r['value']))
    entries={};known_keys={};newkeys=[];free=[]
    # Mask permutations independent of the constructor's actual-support loop.
    for rec in data['records']:
        l,m,i,j=rec['type'];aa=[956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        check('valid_atoms_'+str(rec['type']),min(aa)>=0 and sum(aa)==1024 and all(sum(v for k,v in enumerate(aa) if k&b)==68 for b in [1,2,4]))
        orders=[];vs=[]
        for kk,perm in enumerate(it.permutations([4,2,1])):
            a=[0]*8
            for mask,n in enumerate(aa):
                new=sum(bit for bit,oldbit in zip([4,2,1],perm) if mask&oldbit);a[new]=n
            ds=[a[4]+a[5],a[4]+a[6],a[2]+a[6]]
            v=None;origin=None
            if 0 in ds:v=av(p[max(ds)]);origin='Boolean'
            elif any(0<h<5 for h in ds):v=av(0);origin='forbidden'
            else:
                typ=(*sorted(ds[:2]),a[4],a[3])
                if typ in base:v=base[typ];origin='prescribed'
            check('full_presentation_'+str((l,m,i,j,kk)),rec['presentations'][kk]==enc({'atoms':a,'distances':ds,'origin':origin,'affine':v}))
            if v is not None:vs.append(v)
            orders.append(tuple(a))
        key=min(orders);check('full_key_'+str(rec['type']),list(key)==rec['key'])
        if key in known_keys:vs.append(known_keys[key])
        v=vs[0] if vs else None
        check('coefficientwise_shared_key_'+str(rec['type']),all(w==v for w in vs))
        if v is not None:known_keys[key]=v
        else:newkeys.append(key);free.append((8-i,8-j));check('only_new_free_'+str(rec['type']),l==m==8)
        check('saved_affine_'+str(rec['type']),enc(v)==rec['affine'])
        entries[l,m,i,j]=v
    free.sort();check('complete_domain',len(entries)==500 and len(newkeys)==len(set(newkeys))==45 and free==list(map(tuple,data['free'])))
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[];fixed_affines=[];costs=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;saved=data['modes'][idx];ls=[l for l in [5,6,7] if l>=max(a,b)]
        def block(l,m):
            l0,m0=sorted([l,m]);v=[sum(beta(68,l0,m0,a,i)*beta(956,l0,m0,b,j)*entries[l0,m0,i,j][k]
                for i,j in it.product(range(l0+1),repeat=2)) for k in range(5)]
            if a==b==0:v[0]-=p[l]*p[m]*sizes[l]*sizes[m]
            return v
        B=[[block(l,m)[0] for m in ls] for l in ls];t=[block(l,8) for l in ls]
        check('base_and_five_cross_coefficients_'+str((a,b)),enc(B)==saved['base'] and enc(t)==saved['cross_affine'])
        selected=[]
        for k in range(1,len(B)+1):
            for inds in it.combinations(range(len(B)),k):
                d=determinant([[B[i][j] for j in inds] for i in inds]);check('old_PSD_minor_'+str((a,b,inds)),d>=0)
                if d>0:selected=inds
        X=[[Q(0)]*5 for _ in ls]
        if selected:
            sub=[[B[i][j] for j in selected] for i in selected]
            for k in range(5):
                vals=solve(sub,[t[i][k] for i in selected])
                for i,v in zip(selected,vals):X[i][k]=v
        for i,k in it.product(range(len(ls)),range(5)):
            check('complete_singular_range_'+str((a,b,i,k)),sum(B[i][j]*X[j][k] for j in range(len(ls)))==t[i][k])
        d=C(68-2*a,8-a)*C(956-2*b,8-b);check('positive_mode_scale_'+str((a,b)),d>0)
        cost=[[sum(t[i][k]*X[i][h] for i in range(len(ls)))/(p[8]*d) for h in range(5)] for k in range(5)]
        fa=[sum(Q(beta(68,8,8,a,i)*beta(956,8,8,b,j),p[8]*d)*v[k]
            for (l,m,i,j),v in entries.items() if l==m==8 and v is not None) for k in range(5)]
        if a==b==0:fa[0]-=p[8]*sizes[8]
        row=[-Q(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),d*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        check('all_quadratic_coefficients_'+str((a,b)),enc(cost)==saved['required_quadratic'])
        check('all_affine_diagonal_coefficients_'+str((a,b)),enc(fa)==saved['fixed_minus_anchor_affine'])
        check('all_original_mode_row_coefficients_'+str((a,b)),enc(row)==data['matrix'][idx]==fixed['matrix'][idx])
        modes.append({'mode':(a,b),'inverse':X,'cost':cost,'fixed':fa});matrix.append(row);costs.append(cost);fixed_affines.append(fa)
    I=[1,2,3,4,7,9,10,11,12,14,15,18,19,20,21,22,23,24,27,28,29,30,31,32,33,36,37,38,39,40,45,46,47,48,49,54,55,56,57,64,72,73]
    J=[-1,0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,41,42,43,44]
    K=[[Q(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
    yy=solve(list(map(list,zip(*K))),[Q(-1) if j==-1 else Q(0) for j in J]);y=[Q(0)]*81
    for i,v in zip(I,yy):y[i]=v
    check('canonical_exact_weights',enc(y)==data['dual']==fixed['exact']['dual'] and min(y)>=0 and sum(y)==1 and sum(v>0 for v in y)==27)
    sums=[sum(v*r[k] for v,r in zip(y,matrix)) for k in range(45)]
    raw=[s*C(8,r)*C(60,r)*C(8,q)*C(948,q)/p[8] for s,(r,q) in zip(sums,free)]
    check('scaled_and_raw_sums',enc(sums)==data['column_sums'] and enc(raw)==data['raw_moment_sums'] and min(sums)>=0 and [rq for rq,s in zip(free,sums) if s>0]==[(3,6)])
    T=[[sum(y[i]*costs[i][k][h] for i in range(81)) for h in range(5)] for k in range(5)]
    fa=[sum(y[i]*fixed_affines[i][k] for i in range(81)) for k in range(5)]
    M=[[-v for v in r] for r in T];M[0][0]+=fa[0]
    for k in range(1,5):M[0][k]+=fa[k]/2;M[k][0]+=fa[k]/2
    check('entire_pairing_polynomial',enc(M)==data['objective_matrix'])
    H=[[-M[i][j] for j in range(1,5)] for i in range(1,5)];g=M[0][1:]
    check('rank_one_curvature_and_null_linear_terms',H[3][3]>0 and not any(g[:3]) and
          all(H[i][j]==0 for i,j in it.product(range(4),repeat=2) if (i,j)!=(3,3)))
    lp=data['domain_LP'];active=lp['active_rows'];AA=[fs[j][1:] for j in active]
    ts=solve(AA,[-fs[j][0] for j in active]);lam0=solve(list(map(list,zip(*AA))),[Q(0),Q(0),Q(0),Q(-1)])
    lam=[Q(0)]*85
    for j,v in zip(active,lam0):lam[j]=v
    point=[Q(1)]+ts;signs=[dot(f,point) for f in fs];upper=sum(l*f[0] for l,f in zip(lam,fs))
    check('exact_domain_primal',enc(ts)==lp['parameters'] and min(signs)>=0 and enc(signs)==lp['free_values'])
    check('exact_domain_dual',enc(lam)==lp['multipliers'] and min(lam)>=0 and
          [sum(l*f[k+1] for l,f in zip(lam,fs)) for k in range(4)]==[0,0,0,-1])
    check('attainment_and_complementarity',upper==ts[3] and all(l*s==0 for l,s in zip(lam,signs)))
    sstar=g[3]/H[3][3]
    endpoint_value=dot(point,[dot(r,point) for r in M])
    check('LP_endpoint_value',enc(endpoint_value)==lp['pairing_at_upper'])
    za=[Q(*v) for v in data['original_point']]
    check('original_domain_feasible',min(dot(f,za) for f in fs)>=0)
    check('stationary_parameter_bracket',za[4]<sstar<upper)
    alpha=(sstar-za[4])/(upper-za[4])
    check('interpolation_coefficient',0<alpha<1 and enc(alpha)==lp['stationary_interpolation'])
    point=[x+alpha*(y-x) for x,y in zip(za,point)];ts=point[1:];signs=[dot(f,point) for f in fs]
    check('stationary_domain_point',min(signs)>=0 and enc(point)==data['optimization']['point'] and
          all(dot(r,ts)==v for r,v in zip(H,g)))
    value=dot(point,[dot(r,point) for r in M]);unrestricted_max=M[0][0]+g[3]**2/H[3][3]
    check('attained_global_quadratic_upper',point[4]==sstar and value==unrestricted_max and
          enc(value)==data['optimization']['value'])
    # For every real t, Phi(t)=value-H33*(t78-sstar)^2. This gives
    # a global bound with no compactness, strict-curvature or KKT assumption.
    for typ,v in entries.items():
        if v is not None:check('every_forced_moment_nonnegative_'+str(typ),dot(v,point)>=0)
    for i,r in enumerate(col['equations']):
        check('point_original_compatibility_'+str(i),sum(Q(*a)*f for a,f in zip(r,signs))==Q(*col['rhs'][i]))
    check('original_negative_pairing_preserved',enc(dot(za,[dot(r,za) for r in M]))==fixed['exact']['fixed_value'])
    lo=value.numerator*10**6//value.denominator;iv=[Q(lo,10**6),Q(lo+1,10**6)]
    verdict='UNIFORM_STRICTLY_NEGATIVE' if value<0 else 'ADMISSIBLE_NONNEGATIVE'
    check('verdict_matches',verdict==data['summary']['verdict'])
    summary={'verdict':verdict if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
             'types':500,'presentations':3000,'range_modes':81,'free_domain_constraints':85,'new_new_variables':45,
             'domain_active_rows':active,'positive_domain_multipliers':[j for j,v in enumerate(lam) if v>0],
             'pairing_interval':iv,'required_uniform_sign':'strictly negative','positive_free_values':sum(v>0 for v in signs),
             'zero_free_values':[j for j,v in enumerate(signs) if v==0]}
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'modes':modes,'objective_matrix':M,'H':H,'g':g,'domain_point':point,'free_values':signs,
            'domain_multipliers':lam,'domain_upper':upper,'stationary_s':sstar,
            'interpolation_alpha':alpha,'curvature':H[3][3],
            'pairing':value,'summary':summary,'checks':checks,'failures':failures}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n');print(enc(summary));print('Full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
