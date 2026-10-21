"""Approved L078 fixed-weight test on the full L076 four-parameter family.

All fractions, full-key comparisons and source rows are saved. No numerical
optimizer status is a mathematical certificate. Existing inputs are read-only.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, det, cramer, basis_solve, enc
from seven_distance_full_base_kernel import rref

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-family-fixed-separator-results.json'


def av(x):
    return [F(x)]+[F(0)]*4


def add(x,y,s=F(1)):
    return [a+s*b for a,b in zip(x,y)]


def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),F(0))


def interval(x):
    k=x.numerator*10**6//x.denominator
    return [F(k,10**6),F(k+1,10**6)]


def propose_axis_maximum(fs):
    """Decimal simplex proposes a domain vertex; only exact checks certify."""
    n,m=4,len(fs);scale=F(1,10**10)
    A=[[-v*scale for v in f[1:]] for f in fs];rhs=[f[0] for f in fs]
    for i,(row,b) in enumerate(zip(A,rhs)):
        norm=max(map(abs,row+[b]))
        if norm:A[i]=[v/norm for v in row];rhs[i]=b/norm
    with localcontext() as ctx:
        ctx.prec=180
        dec=lambda v:Decimal(v.numerator)/Decimal(v.denominator)
        D=[[dec(v) for v in row]+[Decimal(-1),dec(b)] for row,b in zip(A,rhs)]
        D += [[Decimal(0),Decimal(0),Decimal(0),Decimal(-1),Decimal(0),Decimal(0)],
              [Decimal(0)]*n+[Decimal(1),Decimal(0)]]
        B,N=list(range(n,n+m)),list(range(n))+[-1];eps=Decimal('1e-130');trace=[]
        def pivot(r,s):
            inv=1/D[r][s]
            for i in range(m+2):
                if i!=r:
                    for j in range(n+2):
                        if j!=s:D[i][j]-=D[r][j]*D[i][s]*inv
            for j in range(n+2):
                if j!=s:D[r][j]*=inv
            for i in range(m+2):
                if i!=r:D[i][s]*=-inv
            D[r][s]=inv;trace.append((N[s],B[r]));B[r],N[s]=N[s],B[r]
        def optimize(phase):
            obj=m+1 if phase==1 else m
            for _ in range(1000):
                opts=[j for j in range(n+1) if phase==1 or N[j]!=-1]
                s=min(opts,key=lambda j:(D[obj][j],N[j]))
                if D[obj][s]>=-eps:return 'optimal'
                opts=[i for i in range(m) if D[i][s]>eps]
                if not opts:return 'unbounded_or_scaling_failure'
                r=min(opts,key=lambda i:(D[i][-1]/D[i][s],B[i]));pivot(r,s)
            return 'iteration_limit'
        r=min(range(m),key=lambda i:D[i][-1])
        if D[r][-1]<-eps:
            pivot(r,n);status=optimize(1)
            if status!='optimal' or D[m+1][-1]<-eps:
                return {'status':'phase_one_failed','basis':B,'trace':trace}
            if -1 in B:
                r=B.index(-1);opts=[j for j in range(n+1) if N[j]!=-1 and abs(D[r][j])>eps]
                if opts:pivot(r,min(opts,key=lambda j:N[j]))
        status=optimize(2)
        return {'status':status,'basis':B,'trace':trace,'variable_scale':scale}


def main():
    names=['maximizer-excluded-anchor-results.json',
           'eight-distance-full-base-kernel-results.json',
           'simultaneous-eight-shell-results.json']
    paths=[ROOT/n for n in names]
    old,col,fixed=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def check(name,ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    out={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        out.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(out),indent=2)+'\n')
    for name,data in zip(names,[old,col,fixed]):
        check('clean_'+name,not data['failures'])
        for rel,h in data.get('input_hashes',{}).items():
            check('hash_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p=[F(*v) for v in old['pairs_through_14']]
    check('normalization',F(*old['rho'])>0 and p[8]==F(16792471,1181138102168120460)>0)
    check('same_original_pairs',col['pairs_through_14']==old['pairs_through_14'])
    fs=[[F(*v)]+[F(*x) for x in row] for v,row in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('original_four_nonpivots',col['affine']['free_indices']==[56,63,69,78] and len(fs)==85)
    for j,(row,rhs) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_affine_kernel_'+str(j),[sum(F(*v)*f[k] for v,f in zip(row,fs)) for k in range(5)]==av(F(*rhs)))
    base={tuple(row['type']):av(F(*row['y'])) for row in old['entries']}
    column=[]
    for row in col['column']:
        y=[p[8]*v for v in fs[row['variable']]] if row['kind']=='free' else av(F(*row['value']))
        column.append(y)
        if row['orbit']!=[0,0,0]:
            l,i,j=row['orbit'];base[l,8,i,j]=y
    # Construct actual supports and EVERY atom presentation. No distance-only
    # identification and no assumption that the fixed-point equalities persist.
    D=set(range(68)); entries={}; dictionary={}; eqs=[]; records=[]; free=[]; freekeys=[]
    for l,m in it.combinations_with_replacement([5,6,7,8],2):
        for i,j in it.product(range(l+1),repeat=2):
            E=(D-(set(range(i))|set(range(m,m+l-i))))|set(range(68,68+j))|set(range(68+m,68+m+l-j))
            G=(D-set(range(m)))|set(range(68,68+m))
            vals,orders,prs=[],[],[]
            check('support_sizes_'+str((l,m,i,j)),len(E)==len(G)==68)
            for A,B,H in it.permutations([D,E,G]):
                atoms=[0]*8
                for x in range(1024):
                    atoms[4*(x in A)+2*(x in B)+(x in H)]+=1
                ds=[len(A-B),len(A-H),len(B-H)]
                v=None;origin=None
                if 0 in ds:
                    v=av(p[max(ds)]);origin='Boolean'
                elif any(0<h<5 for h in ds):
                    v=av(0);origin='forbidden'
                else:
                    typ=(*sorted(ds[:2]),len((A-B)&(A-H)),len((B-A)&(H-A)))
                    if typ in base:
                        v=base[typ];origin='prescribed'
                if v is not None: vals.append(v)
                orders.append(tuple(atoms))
                prs.append({'atoms':atoms,'distances':ds,'origin':origin,'affine':v})
            key=min(orders)
            if key in dictionary: vals.append(dictionary[key])
            v=vals[0] if vals else None
            if v is not None:
                eqs.extend(add(w,v,-1) for w in vals[1:])
                dictionary[key]=v
            else:
                check('only_eight_eight_free_'+str((l,m,i,j)),l==m==8)
                free.append((8-i,8-j));freekeys.append(key)
            entries[l,m,i,j]=v
            records.append({'type':(l,m,i,j),'key':key,'affine':v,'presentations':prs})
    extra=sorted(set(tuple(e) for e in eqs if any(e)))
    free.sort()
    check('no_additional_key_constraints',not extra)
    check('45_distinct_free_keys',len(freekeys)==len(set(freekeys))==45)
    check('full_free_partition',free==[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8])
    active=[27,33,56,63]
    ta=cramer([fs[j][1:] for j in active],[-fs[j][0] for j in active])
    za=[F(1)]+ta
    check('original_active_column',[dot(f,za) for f in fs]==[F(*v) for v in col['solution']])
    for rec,saved in zip(records,fixed['records']):
        check('original_record_'+str(rec['type']),rec['key']==tuple(saved['key']) and
              (None if rec['affine'] is None else enc(dot(rec['affine'],za)))==saved['value'])
    out.update(domain={'nonnegative_affine':fs,'key_equalities':extra,'all_key_residuals':eqs},
               affine_column=column,records=records,free=free,original_point=za)
    save('domain_saved')
    print('Domain:',len(records),'types;',6*len(records),'presentations; additional key constraints:',len(extra),'; failures:',failures,flush=True)
    if failures: raise SystemExit(1)
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[];cost_total=[[F(0)]*5 for _ in range(5)];fixed_total=av(0)
    dual=[F(*v) for v in fixed['exact']['dual']]
    check('unchanged_81_weights',len(dual)==81 and min(dual)>=0 and sum(dual)==1 and sum(y>0 for y in dual)==27)
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;layers=[l for l in [5,6,7] if max(a,b)<=l]
        def block(l,m):
            ll,mm=sorted([l,m]);ans=av(0)
            for i,j in it.product(range(ll+1),repeat=2):
                ans=add(ans,entries[ll,mm,i,j],beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j))
            if a==b==0: ans[0]-=p[l]*p[m]*sizes[l]*sizes[m]
            return ans
        B=[[block(l,m)[0] for m in layers] for l in layers]
        cross=[block(l,8) for l in layers]
        selected=[];minors=[]
        for k in range(1,len(B)+1):
            for inds in it.combinations(range(len(B)),k):
                d=det([[B[i][j] for j in inds] for i in inds])
                minors.append({'indices':inds,'value':d})
                check('old_minor_'+str((a,b,inds)),d>=0)
                if d>0:selected=inds
        X=[[F(0)]*5 for _ in B]
        if selected:
            BB=[[B[i][j] for j in selected] for i in selected]
            for k in range(5):
                x=cramer(BB,[cross[i][k] for i in selected])
                for j,v in zip(selected,x):X[j][k]=v
        res=[[sum(B[i][j]*X[j][k] for j in range(len(B)))-cross[i][k] for k in range(5)] for i in range(len(B))]
        check('entire_affine_range_'+str((a,b)),not any(any(r) for r in res))
        D8=C(68-2*a,8-a)*C(956-2*b,8-b)
        check('positive_D8_'+str((a,b)),D8>0)
        cost=[[sum(cross[j][k]*X[j][h] for j in range(len(B)))/(p[8]*D8) for h in range(5)] for k in range(5)]
        check('symmetric_cost_'+str((a,b)),cost==list(map(list,zip(*cost))))
        fixedpart=av(0)
        for (l,m,i,j),y in entries.items():
            if l==m==8 and y is not None:
                fixedpart=add(fixedpart,y,F(beta(68,8,8,a,i)*beta(956,8,8,b,j),p[8]*D8))
        if a==b==0: fixedpart[0]-=p[8]*sizes[8]
        row=[-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D8*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        saved=fixed['modes'][idx]
        check('same_base_'+str((a,b)),enc(B)==saved['base'])
        check('same_original_cross_'+str((a,b)),enc([dot(t,za) for t in cross])==saved['cross'])
        check('same_original_cost_'+str((a,b)),enc(dot(za,[dot(r,za) for r in cost]))==saved['required'])
        check('same_original_bound_'+str((a,b)),enc(dot(fixedpart,za)-dot(za,[dot(r,za) for r in cost]))==fixed['rhs'][idx])
        check('same_original_row_'+str((a,b)),enc(row)==fixed['matrix'][idx])
        fixed_total=add(fixed_total,fixedpart,dual[idx])
        cost_total=[[x+dual[idx]*y for x,y in zip(r,s)] for r,s in zip(cost_total,cost)]
        matrix.append(row)
        modes.append({'mode':(a,b),'layers':layers,'base':B,'cross_affine':cross,'inverse_affine':X,
                      'range_residuals':res,'principal_minors':minors,'required_quadratic':cost,'fixed_minus_anchor_affine':fixedpart,'D8':D8})
    # Reconstruct canonical weights, not merely copy the constructor's dual.
    I=[1,2,3,4,7,9,10,11,12,14,15,18,19,20,21,22,23,24,27,28,29,30,31,32,33,36,37,38,39,40,45,46,47,48,49,54,55,56,57,64,72,73]
    J=[-1,0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,41,42,43,44]
    K=[[F(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
    yy,pivots=basis_solve(list(map(list,zip(*K))),[F(-1) if j==-1 else F(0) for j in J])
    rebuilt=[F(0)]*81
    for i,y in zip(I,yy):rebuilt[i]=y
    check('canonical_I_J_weights',rebuilt==dual and all(pivots))
    sums=[sum(y*r[j] for y,r in zip(dual,matrix)) for j in range(45)]
    raw=[s*C(8,r)*C(60,r)*C(8,q)*C(948,q)/p[8] for s,(r,q) in zip(sums,free)]
    check('original_scaled_sums',enc(sums)==fixed['exact']['column_sums'])
    check('original_raw_sums',enc(raw)==fixed['exact']['raw_moment_column_sums'])
    check('sole_essential_nonnegative_coordinate',[rq for rq,s in zip(free,sums) if s>0]==[(3,6)] and sum(s==0 for s in sums)==44)
    M=[[-v for v in r] for r in cost_total]
    M[0][0]+=fixed_total[0]
    for k in range(1,5):M[0][k]+=fixed_total[k]/2;M[k][0]+=fixed_total[k]/2
    oldvalue=dot(za,[dot(r,za) for r in M])
    check('original_pairing',enc(oldvalue)==fixed['exact']['fixed_value'])
    out.update(modes=modes,matrix=matrix,dual=dual,dual_basis_pivots=pivots,column_sums=sums,raw_moment_sums=raw,
               total_fixed_affine=fixed_total,total_cost_quadratic=cost_total,objective_matrix=M,original_value=oldvalue)
    save('quadratic_saved')
    print('All 81 affine ranges checked; 45 original scaled/raw columns retained; quadratic saved; failures:',failures,flush=True)
    if failures:raise SystemExit(1)
    H=[[-M[i][j] for j in range(1,5)] for i in range(1,5)];g=M[0][1:]
    rr,pv,_=rref([r+[v] for r,v in zip(H,g)])
    consistent=4 not in pv
    hs=[r[:] for r in H];squares=[]
    for _ in range(4):
        j=next((j for j in range(4) if hs[j][j]>0),None)
        if j is None:break
        pivot=hs[j][j];v=[r[j] for r in hs]
        squares.append({'coordinate':j,'pivot':pivot,'vector':v})
        hs=[[x-v[i]*v[k]/pivot for k,x in enumerate(r)] for i,r in enumerate(hs)]
    check('positive_semidefinite_H',not any(any(r) for r in hs))
    out['stationary_system']={'H':H,'g':g,'RREF':rr,'pivots':pv,'consistent':consistent,'square_decomposition':squares,'residual':hs}
    save('curvature_saved')
    print('Curvature rank:',len(squares),'; stationarity consistent:',consistent,flush=True)
    if not consistent:
        out['summary']={'verdict':'UNRESOLVED_LINEAR_NULL_DIRECTION','checks':len(checks),'failures':len(failures)}
        save('completed');return
    ts=[F(0)]*4
    for i,j in enumerate(pv):ts[j]=rr[i][-1]
    point=[F(1)]+ts
    signs=[dot(f,point) for f in fs];value=dot(point,[dot(r,point) for r in M])
    unconstrained={'point':point[:],'parameters':ts[:],'value':value,'free_values':signs[:]}
    check('stationarity_exact',all(dot(r,ts)==v for r,v in zip(H,g)))
    check('completed_square_value',value==M[0][0]+dot(g,ts))
    # A stationary affine space can meet the domain even if its canonical
    # zero-nonpivot representative does not. Here test its one observed
    # violated boundary with all square subsystems, preserving the original
    # four parameters. Each proposed point is checked against ALL 85 signs.
    trials=[]
    first_negative=[j for j,s in enumerate(signs) if s<0]
    if value>=0 and first_negative and len(squares)==1 and len(first_negative)==1:
        row_index=next(i for i,r in enumerate(H) if any(r))
        boundary=first_negative[0]
        for inds in it.combinations(range(4),2):
            AA=[[H[row_index][j] for j in inds],[fs[boundary][j+1] for j in inds]]
            if not det(AA): continue
            vv=cramer(AA,[g[row_index],-fs[boundary][0]])
            proposal=[F(0)]*4
            for j,v in zip(inds,vv):proposal[j]=v
            pp=[F(1)]+proposal;ss=[dot(f,pp) for f in fs]
            stationary=all(dot(r,proposal)==v for r,v in zip(H,g))
            trials.append({'coordinates':inds,'boundary':boundary,'parameters':proposal,
                           'negative_indices':[j for j,s in enumerate(ss) if s<0],
                           'stationary':stationary})
            if stationary and min(ss)>=0:
                point,ts,signs=pp,proposal,ss
                break
    check('final_stationarity',all(dot(r,ts)==v for r,v in zip(H,g)))
    check('final_objective_value',dot(point,[dot(r,point) for r in M])==value)
    line_test=None
    if value>=0 and min(signs)<0:
        # An admissible positive value alone decides this fixed-weight test;
        # a domain maximum is unnecessary. Test the original t78 axis by
        # intersecting ALL 85 exact half-lines and clamping its stationary s.
        lo=None;hi=None;empty=False;bounds=[]
        for j,f in enumerate(fs):
            c,b=f[0],f[4]
            if b>0:
                v=-c/b;lo=v if lo is None else max(lo,v);bounds.append((j,'lower',v))
            elif b<0:
                v=-c/b;hi=v if hi is None else min(hi,v);bounds.append((j,'upper',v))
            elif c<0:empty=True
        if lo is not None and hi is not None and lo>hi:empty=True
        line_test={'lower':lo,'upper':hi,'empty':empty,'bounds':bounds}
        if not empty and H[3][3]>0:
            s=g[3]/H[3][3]
            if lo is not None:s=max(s,lo)
            if hi is not None:s=min(s,hi)
            pp=[F(1),F(0),F(0),F(0),s]
            ss=[dot(f,pp) for f in fs];v=dot(pp,[dot(r,pp) for r in M])
            line_test.update(point=pp,value=v,free_values=ss)
            if min(ss)>=0 and v>=0:
                point,ts,signs,value=pp,pp[1:],ss,v
    check('candidate_objective_exact',dot(point,[dot(r,point) for r in M])==value)
    domain_lp=None
    if min(signs)<0 and len(squares)==1:
        axis_only=all(H[i][j]==0 for i,j in it.product(range(4),repeat=2) if (i,j)!=(3,3)) and not any(g[:3])
        check('objective_depends_only_on_original_t78',axis_only)
        if axis_only:
            proposal=propose_axis_maximum(fs)
            domain_lp={'proposal':proposal}
            out['domain_LP']=domain_lp;save('domain_LP_proposed')
            print('Domain LP proposal:',proposal['status'],flush=True)
            if proposal['status']=='optimal':
                basis=proposal['basis']
                active_rows=[j for j in range(85) if 4+j not in basis]
                active_rows += [col['affine']['free_indices'][j] for j in range(4) if j not in basis
                                and col['affine']['free_indices'][j] not in active_rows]
                check('four_active_domain_rows',len(active_rows)==4)
                if len(active_rows)==4:
                    AA=[fs[j][1:] for j in active_rows]
                    tt=cramer(AA,[-fs[j][0] for j in active_rows])
                    weights=cramer(list(map(list,zip(*AA))),[F(0),F(0),F(0),F(-1)])
                    lam=[F(0)]*85
                    for j,w in zip(active_rows,weights):lam[j]=w
                    pp=[F(1)]+tt;ss=[dot(f,pp) for f in fs]
                    upper=sum(l*f[0] for l,f in zip(lam,fs))
                    coeff=[sum(l*f[k+1] for l,f in zip(lam,fs)) for k in range(4)]
                    check('domain_LP_primal',min(ss)>=0)
                    check('domain_LP_dual',min(lam)>=0 and coeff==[0,0,0,-1])
                    check('domain_LP_equal_values',upper==tt[3] and not any(l*s for l,s in zip(lam,ss)))
                    vv=dot(pp,[dot(r,pp) for r in M])
                    sstar=g[3]/H[3][3]
                    domain_lp.update(active_rows=active_rows,parameters=tt,point=pp,free_values=ss,
                                     multipliers=lam,upper=upper,coefficient_sums=coeff,
                                     pairing_at_upper=vv,required_stationary=sstar,
                                     upper_below_stationary=upper<sstar)
                    if not failures:
                        point,ts,signs,value=pp,tt,ss,vv
                        # If the stationary s lies between two feasible points,
                        # their exact convex interpolation attains the global
                        # quadratic upper bound without needing strict curvature.
                        if za[4]<=sstar<=upper and za[4]<upper:
                            alpha=(sstar-za[4])/(upper-za[4])
                            candidate=[x+alpha*(y-x) for x,y in zip(za,pp)]
                            csigns=[dot(f,candidate) for f in fs]
                            cvalue=dot(candidate,[dot(r,candidate) for r in M])
                            check('convex_interpolation_feasible',0<=alpha<=1 and min(csigns)>=0)
                            check('convex_interpolation_stationary',candidate[4]==sstar and
                                  all(dot(r,candidate[1:])==v for r,v in zip(H,g)))
                            check('convex_interpolation_attains_upper',cvalue==unconstrained['value'])
                            domain_lp['stationary_interpolation']=alpha
                            point,ts,signs,value=candidate,candidate[1:],csigns,cvalue
    global_negative=domain_lp is not None and 'upper' in domain_lp and domain_lp['upper_below_stationary'] and value<0
    verdict='UNIFORM_STRICTLY_NEGATIVE' if (unconstrained['value']<0 or global_negative) else 'ADMISSIBLE_NONNEGATIVE' if value>=0 and min(signs)>=0 else 'UNRESOLVED_CONSTRAINED'
    out['optimization']={'point':point,'parameters':ts,'value':value,'free_values':signs,
                         'unconstrained_stationary':unconstrained,
                         'negative_indices':[j for j,s in enumerate(signs) if s<0],
                         'initial_negative_indices':first_negative,'flat_boundary_trials':trials,
                         'axis_domain_test':line_test}
    if domain_lp is not None:out['domain_LP']=domain_lp
    out['summary']={'verdict':verdict,'checks':len(checks),'failures':len(failures),'H_rank':len(squares),
                    'value_interval':interval(value),'value_zero':value==0,'required_pairing':'strictly negative everywhere',
                    'nonnegative_free':sum(s>=0 for s in signs),'zero_free':[j for j,s in enumerate(signs) if s==0]}
    save('completed')
    print(enc(out['summary']));print('Full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)


if __name__=='__main__':
    main()
