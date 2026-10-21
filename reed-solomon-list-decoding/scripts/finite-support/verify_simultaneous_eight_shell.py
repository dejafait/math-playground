"""Independent rational verification of the immutable joint-eight test.

No notebook imports or optimizer. Actual supports, original beta rows,
all old principal minors, range inverse and raw-moment separator rebuilt.
"""
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
OUT=ROOT/'simultaneous-eight-shell-verification.json'


def C(n,k):
    return comb(n,k) if 0<=k<=n else 0


def enc(x):
    if isinstance(x,Q):
        return [x.numerator,x.denominator]
    if isinstance(x,dict):
        return {str(k):enc(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [enc(v) for v in x]
    return x


@lru_cache(None)
def beta(n,l,m,a,t):
    return sum((-1)**(u-t)*C(u,t)*C(n-2*a,u-a)*C(n-a-u,l-u)*C(n-a-u,m-u)
               for u in range(a,min(l,m,n-a)+1) if u>=t)


def det(M):
    n=len(M)
    return sum((-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
               *product(M[i][p[i]] for i in range(n)) for p in it.permutations(range(n)))


def product(xs):
    v=Q(1)
    for x in xs:
        v*=x
    return v


def cramer(M,b):
    d=det(M)
    if not d:
        raise ValueError('singular principal system')
    return [det([[b[i] if k==j else x for k,x in enumerate(row)] for i,row in enumerate(M)])/d for j in range(len(b))]


def basis_solve(M,b):
    a=[[Q(v) for v in row]+[Q(r)] for row,r in zip(M,b)]
    pivots=[]
    for j in range(len(b)):
        k=next(k for k in range(j,len(b)) if a[k][j])
        a[k],a[j]=a[j],a[k]
        p=a[j][j];pivots.append(p)
        a[j]=[v/p for v in a[j]]
        for k in range(len(b)):
            if k!=j:
                t=a[k][j]
                a[k]=[v-t*w for v,w in zip(a[k],a[j])]
    return [row[-1] for row in a],pivots


def main():
    names=['simultaneous-eight-shell-results.json','maximizer-excluded-anchor-results.json',
           'eight-distance-full-base-kernel-results.json','eight-distance-fixed-column-energy-results.json']
    paths=[ROOT/n for n in names]
    data,old,col,energy=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    check('constructor_clean',not data['failures'])
    for rel,h in data['input_hashes'].items():
        check('input_hash_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p=[Q(*v) for v in old['pairs_through_14']]
    check('positive_rho_and_original_p8',Q(*old['rho'])>0 and p[8]==Q(16792471,1181138102168120460)>0)
    base={tuple(r['type']):Q(*r['y']) for r in old['entries']}
    ci=[Q(*v) for v in col['affine']['intercept']]
    cs=[[Q(*v) for v in r] for r in col['affine']['slopes']]
    active=[27,33,56,63]
    params=cramer([cs[j] for j in active],[-ci[j] for j in active])
    f=[v+sum(x*y for x,y in zip(r,params)) for v,r in zip(ci,cs)]
    check('same_active_set',col['active_zero_indices']==active)
    check('same_85_coordinates',enc(f)==col['solution'] and min(f)==0)
    check('all_compatibility_equations',all(sum(Q(*a)*x for a,x in zip(row,f))==Q(*b) for row,b in zip(col['equations'],col['rhs'])))
    column=[p[8]*f[r['variable']] if r['kind']=='free' else Q(*r['value']) for r in col['column']]
    check('same_complete_column',enc(column)==col['complete_column'])
    for r,y in zip(col['column'][1:],column[1:]):
        l,i,j=r['orbit'];base[l,8,i,j]=y
    D=set(range(68))
    entries,keys,free,records={},{},[],[]
    for l,m in it.combinations_with_replacement([5,6,7,8],2):
        for i,j in it.product(range(l+1),repeat=2):
            E=(D-(set(range(i))|set(range(m,m+l-i))))|set(range(68,68+j))|set(range(68+m,68+m+l-j))
            G=(D-set(range(m)))|set(range(68,68+m))
            check('actual_support_sizes_'+str((l,m,i,j)),len(E)==len(G)==68)
            saved=data['records'][len(records)]
            vals,orders=[],[]
            for k,(A,B,Fset) in enumerate(it.permutations([D,E,G])):
                atoms=[0]*8
                for x in range(1024):
                    atoms[4*(x in A)+2*(x in B)+(x in Fset)]+=1
                distances=[len(A-B),len(A-Fset),len(B-Fset)]
                y,origin=None,None
                if 0 in distances:
                    y,origin=p[max(distances)],'Boolean'
                elif any(0<h<5 for h in distances):
                    y,origin=Q(0),'forbidden'
                else:
                    typ=(*sorted(distances[:2]),len((A-B)&(A-Fset)),len((B-A)&(Fset-A)))
                    if typ in base:
                        y,origin=base[typ],'immutable'
                rec={'atoms':atoms,'distances':distances,'origin':origin,'value':y}
                check('presentation_'+str((l,m,i,j,k)),enc(rec)==saved['presentations'][k])
                if y is not None:
                    vals.append(y)
                orders.append(tuple(atoms))
            key=min(orders)
            check('all_presentations_agree_'+str((l,m,i,j)),len(set(vals))<=1)
            y=vals[0] if vals else None
            check('original_type_and_key_'+str((l,m,i,j)),saved['type']==[l,m,i,j] and saved['key']==list(key))
            check('original_value_'+str((l,m,i,j)),saved['value']==enc(y))
            check('equal_union_key_'+str((l,m,i,j)),key not in keys or keys[key]==y)
            keys[key]=y;entries[l,m,i,j]=y
            if y is None:
                check('only_new_new_free_'+str((l,m,i,j)),l==m==8)
                free.append((8-i,8-j))
            else:
                check('fixed_sign_'+str((l,m,i,j)),y>=0)
            records.append({'type':(l,m,i,j),'key':key,'value':y})
    free.sort()
    check('full_free_domain',free==[(r,q) for r in range(9) for q in range(9) if r+q>=8] and data['free']==list(map(list,free)))
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    matrix,rhs,modes=[],[],[]
    for a,b in it.product(range(9),repeat=2):
        oldls=[l for l in [5,6,7] if l>=max(a,b)]
        def block(l,m):
            ll,mm=sorted([l,m])
            return sum(beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)*entries[ll,mm,i,j]
                for i,j in it.product(range(ll+1),repeat=2))- (p[l]*p[m]*sizes[l]*sizes[m] if a==b==0 else 0)
        B=[[block(l,m) for m in oldls] for l in oldls]
        t=[block(l,8) for l in oldls]
        minors=[]
        selected=[]
        for k in range(1,len(B)+1):
            for inds in it.combinations(range(len(B)),k):
                d=det([[B[i][j] for j in inds] for i in inds])
                check('old_principal_minor_'+str((a,b,inds)),d>=0)
                minors.append({'indices':inds,'value':d})
                if d>0:
                    selected=inds
        x=[Q(0)]*len(B)
        if selected:
            z=cramer([[B[i][j] for j in selected] for i in selected],[t[i] for i in selected])
            for i,v in zip(selected,z):
                x[i]=v
        residuals=[sum(v*w for v,w in zip(row,x))-r for row,r in zip(B,t)]
        check('all_singular_ranges_'+str((a,b)),not any(residuals))
        cost=sum(v*w for v,w in zip(t,x))
        D8=C(68-2*a,8-a)*C(956-2*b,8-b)
        check('positive_D8_'+str((a,b)),D8>0)
        fixed=sum(beta(68,8,8,a,i)*beta(956,8,8,b,j)*y/(p[8]*D8)
            for (l,m,i,j),y in entries.items() if l==m==8 and y is not None)
        anchor=p[8]*sizes[8] if a==b==0 else Q(0)
        required=cost/(p[8]*D8)
        row=[-Q(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D8*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        bound=fixed-anchor-required
        mode_index=9*a+b
        saved=data['modes'][mode_index]
        check('original_mode_matrix_'+str((a,b)),enc(B)==saved['base'] and enc(t)==saved['cross'])
        check('original_mode_row_'+str((a,b)),enc(row)==data['matrix'][mode_index])
        check('original_mode_bound_'+str((a,b)),enc(bound)==data['rhs'][mode_index])
        check('original_cost_'+str((a,b)),enc(required)==saved['required'])
        matrix.append(row);rhs.append(bound)
        modes.append({'mode':(a,b),'layers':oldls,'base':B,'cross':t,'principal_minors':minors,
                      'selected_principal_inverse':x,'range_residuals':residuals,'required':required,'fixed':fixed,'anchor':anchor})
    mult=lambda a,b:(C(68,a)-C(68,a-1))*(C(956,b)-C(956,b-1))
    trace=p[8]**2+p[8]*sum(mult(*r['mode'])*r['required'] for r in modes)/sizes[8]
    check('full_L077_trace',trace==Q(*energy['energy']))
    for l in [5,6,7,8]:
        check('dimension_'+str(l),sum(mult(a,b) for a,b in it.product(range(l+1),repeat=2))==sizes[l])
    exact=data['exact']
    check('negative_certificate_kind',exact['kind']=='FARKAS')
    y=[Q(*v) for v in exact['dual']]
    check('all_81_dual_signs',len(y)==81 and min(y)>=0)
    I=[1,2,3,4,7,9,10,11,12,14,15,18,19,20,21,22,23,24,27,28,29,30,31,32,33,36,37,38,39,40,45,46,47,48,49,54,55,56,57,64,72,73]
    J=[-1,0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,41,42,43,44]
    M=[[Q(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
    yy,pivots=basis_solve(list(map(list,zip(*M))),[Q(-1) if j==-1 else Q(0) for j in J])
    rebuilt_y=[Q(0)]*81
    for i,v in zip(I,yy):
        rebuilt_y[i]=v
    check('independent_explicit_42_basis',rebuilt_y==y and len(pivots)==42 and all(pivots))
    sums=[sum(v*row[j] for v,row in zip(y,matrix)) for j in range(len(free))]
    raw=[s*C(8,r)*C(60,r)*C(8,q)*C(948,q)/p[8] for s,(r,q) in zip(sums,free)]
    for j,(s,raw_sum) in enumerate(zip(sums,raw)):
        r,q=free[j]
        direct_raw=-sum(y[9*a+b]*Q(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*C(68-2*a,8-a)*C(956-2*b,8-b)) for a,b in it.product(range(9),repeat=2))
        check('scaled_original_column_'+str(j),s==Q(*exact['column_sums'][j]) and s>=0)
        check('raw_original_column_'+str(j),raw_sum==direct_raw==Q(*exact['raw_moment_column_sums'][j]) and raw_sum>=0)
    value=sum(v*b for v,b in zip(y,rhs))
    check('exact_fixed_pairing',value==Q(*exact['fixed_value']) and value<0)
    totals={name:sum(y[i]*r[name] for i,r in enumerate(modes)) for name in ['fixed','anchor','required']}
    check('fixed_anchor_energy_identity',value==totals['fixed']-totals['anchor']-totals['required'])
    k=value.numerator*10**6//value.denominator
    bounds=[Q(k,10**6),Q(k+1,10**6)]
    summary={'verdict':'EXCLUDED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
             'types':len(records),'presentations':6*len(records),'free':len(free),'modes':len(modes),
             'old_principal_minors':sum(len(r['principal_minors']) for r in modes),
             'positive_dual_weights':sum(v>0 for v in y),'zero_column_sums':sum(v==0 for v in sums),
             'positive_sign_columns':[(r,q) for (r,q),s in zip(free,sums) if s>0],
             'pairing_interval':bounds,'required_pairing_lower_bound':0}
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'records':records,'modes':modes,'matrix':matrix,'rhs':rhs,'dual':y,'column_sums':sums,
            'explicit_basis_rows':I,'explicit_basis_columns':J,'explicit_basis_pivots':pivots,
            'raw_moment_column_sums':raw,'fixed_pairing':value,'pairing_parts':totals,
            'checks':checks,'failures':failures,'summary':summary}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(enc(summary))
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB))
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
