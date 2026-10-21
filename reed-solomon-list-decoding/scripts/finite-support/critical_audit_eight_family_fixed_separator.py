"""L079 dedicated audit of full affine domain and attained square maximum.

Reuse L078's reviewed entry-independent direct actions. Import only arithmetic
helpers from its audit, no L079 constructor, verifier or optimizer. Consume
complete certificates, and save complete rational evidence with bounded output.
"""
import hashlib
import itertools as it
import json
import re
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from critical_audit_simultaneous_eight_shell import c, beta, dot, enc, solve

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'eight-family-fixed-separator-critical-audit.json'


def av(v):
    return [F(v)]+[F(0)]*4


def main():
    names = ['eight-family-fixed-separator-results.json',
             'eight-family-fixed-separator-verification.json',
             'simultaneous-eight-shell-results.json',
             'simultaneous-eight-shell-critical-audit.json',
             'eight-distance-full-base-kernel-results.json',
             'maximizer-excluded-anchor-results.json',
             'maximizer-completion-results.json', 'delsarte-lp-results.json',
             'seven-distance-full-base-kernel-results.json',
             'alternative-product-zero-plane-results.json',
             'seven-shell-affine-fixed-dual-results.json',
             'simultaneous-shell-ordinary-scalars-results.json']
    paths = [ROOT/n for n in names]
    data, ver, fixed, reviewed, col, old, inc, lp, seven, plane, square, six = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    for name, obj in zip(names,[data, ver, fixed, reviewed, col, old, inc, lp, seven, plane, square, six]):
        check('clean_'+name,not obj['failures'])
    for obj in [data, ver, fixed, reviewed, col, old, inc]:
        for rel,h in obj.get('input_hashes',{}).items():
            check('input_binding_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)

    # Reconstruct the essential immutable recipes, importing their reviewed
    # uniqueness/kernel contracts rather than asserting a recursive audit.
    primal=[F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    for j in range(1,65):
        row=[F(sum((-1)**h*c(j,h)*c(68-j,i-h)*c(956-j,i-h) for h in range(i+1)),c(68,i)*c(956,i)) for i in range(5,69)]
        check('original_pair_equation_'+str(j),dot(row,primal)==-1)
    p=[F(1)]+[F(0)]*4+[x/(2*c(68,h)*c(956,h)) for h,x in zip(range(5,69),primal)]
    rho=(F(c(1024,64),c(68,64))+1)/(2*c(1024,68))
    check('rho_and_original_pairs',rho>0 and enc(rho)==old['rho'] and enc(p[:15])==old['pairs_through_14']==col['pairs_through_14'] and p[8]==F(16792471,1181138102168120460))
    sm=[[F(*v) for v in row] for row in square['objective_matrix']]
    pm=[[F(*v) for v in row] for row in plane['plane_matrix']]
    params=[F(0),-pm[0][2]/pm[2][2],-sm[0][3]/sm[3][3]]
    rr=[[F(*v) for v in row] for row in seven['equation_rref']]
    f7=[F(0)]*49
    for j,v in zip([27,33,42],params): f7[j]=v
    for k,j in enumerate(seven['equation_pivots']):
        f7[j]=rr[k][-1]-sum(rr[k][t]*f7[t] for t in [27,33,42])
    check('original_seven_parameters_column',enc(params)==inc['parameters'] and enc(f7)==inc['free_column'] and min(f7)>=0)
    for i,(r,b) in enumerate(zip(seven['equations'],seven['rhs'])):
        check('original_seven_equation_'+str(i),dot([F(*v) for v in r],f7)==F(*b))
    base={tuple(r['type']):av(F(*r['y'])) for r in six['types']}
    for r in seven['column'][1:]:
        base[r['orbit'][0],7,*r['orbit'][1:]]=av(p[7]*f7[r['variable']] if r['kind']=='free' else F(*r['value']))
    defining=[0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,24,25,26,27,28,29,32,33,34,35,40,41,42,48,49,56]
    z7,piv7=solve([[F(*v) for v in inc['matrix'][i]] for i in defining]+[[F(j==28) for j in range(36)]], [F(*inc['rhs'][i]) for i in defining]+[F(0)])
    check('original_completion',enc(z7)==inc['certificate']['z']==reviewed['completion'] and min(z7)==0)
    free7=[(r,q) for r,q in it.product(range(8),repeat=2) if r+q>=7]
    for r,q in it.product(range(8),repeat=2):
        h=r+q
        v=av(p[7]) if h==0 else av(0) if h<=4 else base[h,7,q,r] if h<=6 else av(p[7]*z7[free7.index((r,q))]/(c(7,r)*c(61,r)*c(7,q)*c(949,q)))
        base[7,7,7-r,7-q]=v
    check('entire_original_dictionary',base=={tuple(r['type']):av(F(*r['y'])) for r in old['entries']} and len(base)==270)

    # Recover all five affine coefficients from the original RREF definition.
    nonpiv=[56,63,69,78]
    rr=[[F(*v) for v in row] for row in col['equation_rref']]
    fs=[[F(0)]*5 for _ in range(85)]
    for k,j in enumerate(nonpiv):fs[j][k+1]=F(1)
    for i,j in enumerate(col['equation_pivots']):fs[j]=[rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    check('entire_RREF_family',len(col['equation_pivots'])==81 and [j for j in range(85) if j not in col['equation_pivots']]==nonpiv and enc(fs)==data['domain']['nonnegative_affine'] and enc([f[0] for f in fs])==col['affine']['intercept'] and enc([f[1:] for f in fs])==col['affine']['slopes'])
    column=[av(p[8])]
    for r in col['column'][1:]:
        v=[p[8]*x for x in fs[r['variable']]] if r['kind']=='free' else av(F(*r['value']))
        column.append(v);base[r['orbit'][0],8,*r['orbit'][1:]]=v
    W=[1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in col['orbits'][1:]]
    kernel_residuals=[]
    check('kernel_and_column_dimensions',len(col['kernel_basis'])==90 and len(W)==len(column)==150)
    for i,r in enumerate(col['kernel_basis']):
        res=[sum(F(*v)*w*f[k] for v,w,f in zip(r,W,column)) for k in range(5)]
        check('all_five_weighted_kernel_residuals_'+str(i),res==[0]*5);kernel_residuals.append(res)
    for i,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('original_affine_equation_'+str(i),[sum(F(*v)*f[k] for v,f in zip(r,fs)) for k in range(5)]==av(F(*b)))

    # Build actual supports by disjoint membership regions, not by the
    # constructor's removed/added interval sets or verifier's bit permutation.
    expected=[(l,m,i,j) for l,m in it.combinations_with_replacement([5,6,7,8],2) for i,j in it.product(range(l+1),repeat=2)]
    check('complete_type_enumeration',[tuple(r['type']) for r in data['records']]==expected and len(expected)==500)
    entries, key_values, records, free_keys = {}, {}, [], []
    for typ, saved in zip(expected,data['records']):
        l,m,i,j=typ;counts=[956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        sets=[set(),set(),set()];start=0
        for mask,n in enumerate(counts):
            for s,bit in zip(sets,[4,2,1]):
                if mask&bit:s.update(range(start,start+n))
            start+=n
        check('actual_supports_'+str(typ),start==1024 and all(len(s)==68 for s in sets) and min(counts)>=0)
        prs=[];values=[]
        for A,B,G in it.permutations(sets):
            atoms=[0]*8
            for x in range(1024):atoms[4*(x in A)+2*(x in B)+(x in G)]+=1
            ds=[len(A-B),len(A-G),len(B-G)]
            v=None;origin=None
            if 0 in ds:v=av(p[max(ds)]);origin='Boolean'
            elif any(0<h<5 for h in ds):v=av(0);origin='forbidden'
            else:
                key=(*sorted(ds[:2]),len((A-B)&(A-G)),len((B-A)&(G-A)))
                if key in base:v=base[key];origin='prescribed'
            prs.append({'atoms':atoms,'distances':ds,'origin':origin,'affine':v})
            if v is not None:values.append(v)
        key=tuple(min(x['atoms'] for x in prs))
        if key in key_values and key_values[key] is not None:values.append(key_values[key])
        v=values[0] if values else None
        check('all_six_complete_presentations_'+str(typ),enc(prs)==saved['presentations'] and list(key)==saved['key'])
        check('all_five_shared_coefficients_'+str(typ),all(x==v for x in values) and enc(v)==saved['affine'] and (key not in key_values or key_values[key]==v))
        key_values[key]=v;entries[typ]=v
        if v is None:free_keys.append(key)
        records.append({'type':typ,'key':key,'presentations':prs,'affine':v})
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    check('free_key_partition',len(free_keys)==len(set(free_keys))==45 and [tuple(v) for v in data['free']]==free and sorted((8-i,8-j) for (l,m,i,j),v in entries.items() if v is None)==free)
    for r,q in it.product(range(9),repeat=2):
        if r+q<=7:
            expected_value=av(p[8]) if r+q==0 else av(0) if r+q<=4 else entries[r+q,8,q,r]
            check('forced_new_new_'+str((r,q)),entries[8,8,8-r,8-q]==expected_value)
    report.update(original_seven_column=f7,completion=z7,completion_pivots=piv7,family=fs,affine_column=column,weighted_kernel_residuals=kernel_residuals,records=records)
    save('family_domain_checked')
    print('Full family domain: 500 types, 3000 presentations, 450 weighted residuals; failures:',failures,flush=True)

    # These finite subset transitions were critically audited in L078 and
    # depend only on sizes/layers. Consume all action coordinates again and
    # use them on every affine coefficient of the new family.
    bases={};norms={};gamma={};sigma={}
    for r in reviewed['factors']:
        n,l=r['n'],r['layer'];hs=[[F(*x) for x in h] for h in r['basis']];ns=[F(*v) for v in r['norms']]
        weights=[c(8,i)*c(n-8,l-i) for i in range(l+1)]
        for a,h in enumerate(hs):
            check('orthogonal_basis_'+str((n,l,a)),ns[a]>0 and dot(weights,[x*x for x in h])==ns[a] and all(dot(weights,[x*i**k for i,x in enumerate(h)])==0 for k in range(a)))
        bases[n,l]=hs;norms[n,l]=ns
    check('all_direct_transitions_present',len(reviewed['transitions'])==220)
    for tr in reviewed['transitions']:
        n,l,m,k=tr['indices'];T=tr['matrix']
        for act in tr['actions']:
            a=act['degree'];v=[dot(row,bases[n,m][a]) for row in T]
            check('complete_direct_action_'+str((n,l,m,k,a)),enc(v)==act['action'])
            if a>l:check('absent_mode_action_'+str((n,l,m,k,a)),not any(v));continue
            g=F(*act['coefficient']);gamma[n,l,m,a,k]=g
            check('direct_action_coefficient_'+str((n,l,m,k,a)),v==[g*x for x in bases[n,l][a]])
            be=beta(n,l,m,a,k)
            if be:
                ratio=norms[n,l][a]*g/be
                check('coherent_factor_ratio_'+str((n,l,m,k,a)),ratio>0 and sigma.setdefault((n,l,m,a),ratio)==ratio)
            else:check('zero_factor_action_'+str((n,l,m,k,a)),g==0)
    for n in [68,956]:
        for a in range(9):
            check('reference_scale_'+str((n,a)),sigma[n,8,8,a]==norms[n,8][a]/c(n-2*a,8-a))
            for l,m in it.product([l for l in [5,6,7,8] if l>=a],repeat=2):
                check('whole_block_congruence_'+str((n,l,m,a)),sigma[n,l,m,a]*sigma[n,8,8,a]==sigma[n,l,8,a]*sigma[n,m,8,a])
    sizes={l:c(68,l)*c(956,l) for l in [5,6,7,8]};modes=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;sv=data['modes'][idx];ls=[l for l in [5,6,7] if l>=max(a,b)]
        N8=norms[68,8][a]*norms[956,8][b];D8=c(68-2*a,8-a)*c(956-2*b,8-b)
        scales={l:sigma[68,l,8,a]*sigma[956,l,8,b]/(N8/D8) for l in ls+[8]}
        def weighted(l,m):
            ll,mm=sorted([l,m]);v=[sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*entries[ll,mm,i,j][k] for i,j in it.product(range(ll+1),repeat=2)) for k in range(5)]
            if (a,b)==(0,0):v[0]-=p[l]*p[m]*sizes[m]
            return [x*norms[68,l][a]*norms[956,l][b] for x in v]
        B=[[weighted(l,m)[0] for m in ls] for l in ls];q=[weighted(l,8) for l in ls]
        for i,l in enumerate(ls):
            check('five_coherent_cross_coefficients_'+str((a,b,l)),q[i]==[F(*v)*(N8/D8)*scales[l] for v in sv['cross_affine'][i]])
            for j,m in enumerate(ls):check('coherent_old_entry_'+str((a,b,l,m)),B[i][j]==F(*sv['base'][i][j])*(N8/D8)*scales[l]*scales[m])
        H=[list(reversed(r)) for r in reversed(B)];u=[r[:] for r in reversed(q)];cost=[[F(0)]*5 for _ in range(5)];stages=[];rank=0
        for k in range(len(H)):
            pivot=H[k][k];check('reverse_pivot_'+str((a,b,k)),pivot>=0)
            if pivot==0:check('all_affine_zero_pivot_residuals_'+str((a,b,k)),not any(H[k][k:]+u[k]))
            elif pivot>0:
                rank+=1
                for h,j in it.product(range(5),repeat=2):cost[h][j]+=u[k][h]*u[k][j]/pivot
                for i in range(k+1,len(H)):
                    u[i]=[v-H[i][k]*w/pivot for v,w in zip(u[i],u[k])]
                    for j in range(k+1,len(H)):H[i][j]-=H[i][k]*H[k][j]/pivot
            stages.append({'pivot':pivot,'matrix':[r[:] for r in H],'affine_cross':[r[:] for r in u]})
        cost=[[x/(p[8]*N8) for x in r] for r in cost]
        check('all_25_direct_quadratic_coefficients_'+str((a,b)),enc(cost)==sv['required_quadratic']==enc([[F(*v) for v in r] for r in ver['modes'][idx]['cost']]))
        fa=[sum(gamma[68,8,8,a,i]*gamma[956,8,8,b,j]*v[k]/p[8] for (l,m,i,j),v in entries.items() if l==m==8 and v is not None) for k in range(5)]
        if (a,b)==(0,0):fa[0]-=p[8]*sizes[8]
        row=[-F(gamma[68,8,8,a,8-r]*gamma[956,8,8,b,8-q],c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        check('direct_diagonal_affine_'+str((a,b)),enc(fa)==sv['fixed_minus_anchor_affine'])
        check('direct_all_45_coefficients_'+str((a,b)),enc(row)==data['matrix'][idx]==fixed['matrix'][idx])
        modes.append({'mode':(a,b),'layers':ls,'base':B,'cross':q,'scales':scales,'rank':rank,'reverse_stages':stages,'cost':cost,'fixed':fa,'row':row})
    report.update(modes=modes)
    save('all_affine_direct_modes_checked')
    print('All 81 affine direct/source modes and singular branches checked; failures:',failures,flush=True)

    manuscript=(NB/'lemmas/L078-simultaneous-eight-shell-fixed-column-obstruction.md').read_text()
    part=manuscript.split('**Compact exact separator.**')[1].split('Define the 42-by-42')[0]
    I=[int(v) for v in re.search(r'I=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    J=[int(v) for v in re.search(r'J=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    yi,pivy=solve([[F(-1) if j==-1 else modes[i]['row'][j] for i in I] for j in J],[F(-1) if j==-1 else F(0) for j in J])
    y=[F(0)]*81
    for i,v in zip(I,yi):y[i]=v
    check('entire_manuscript_separator',enc(y)==data['dual']==fixed['exact']['dual'] and min(y)==0 and sum(y)==1 and sum(v>0 for v in y)==27)
    sums=[];raw=[]
    for j,(r,q) in enumerate(free):
        s=sum(v*m['row'][j] for v,m in zip(y,modes))
        rawval=-sum(y[9*a+b]*F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*c(68-2*a,8-a)*c(956-2*b,8-b)) for a,b in it.product(range(9),repeat=2))
        check('raw_and_scaled_'+str((r,q)),s>=0 and rawval==s*c(8,r)*c(60,r)*c(8,q)*c(948,q)/p[8] and enc(s)==data['column_sums'][j] and enc(rawval)==data['raw_moment_sums'][j])
        sums.append(s);raw.append(rawval)
    check('only_3_6_sign',sum(v==0 for v in sums)==44 and [rq for rq,v in zip(free,sums) if v>0]==[(3,6)])
    M=[[-sum(v*m['cost'][i][j] for v,m in zip(y,modes)) for j in range(5)] for i in range(5)]
    fa=[sum(v*m['fixed'][i] for v,m in zip(y,modes)) for i in range(5)]
    M[0][0]+=fa[0]
    for i in range(1,5):M[0][i]+=fa[i]/2;M[i][0]+=fa[i]/2
    check('complete_symmetric_objective',M==list(map(list,zip(*M))) and enc(M)==data['objective_matrix']==ver['objective_matrix'])
    kappa=-M[4][4];sstar=M[0][4]/kappa;V=M[0][0]+M[0][4]**2/kappa
    square_matrix=[[F(0)]*5 for _ in range(5)]
    square_matrix[0][0]=V-kappa*sstar*sstar;square_matrix[0][4]=square_matrix[4][0]=kappa*sstar;square_matrix[4][4]=-kappa
    check('entire_square_identity',kappa>0 and M==square_matrix)
    gaplo=V-F(351861924105,10**6);gaphi=F(351861924106,10**6)-V
    check('strict_positive_manuscript_interval',gaplo>=0 and gaphi>0 and V>0)
    manuscript=(NB/'lemmas/L079-eight-family-fixed-separator-attained-positive-maximum.md').read_text()
    active0=[int(v) for v in re.search(r'I0=\(([^)]+)\)',manuscript).group(1).split(',')]
    active1=[int(v) for v in re.search(r'J0=\(([^)]+)\)',manuscript).group(1).split(',')]
    vertices=[]
    for active in [active0,active1]:
        t,piv=solve([fs[i][1:] for i in active],[-fs[i][0] for i in active]);z=[F(1)]+t;signs=[dot(f,z) for f in fs]
        check('manuscript_vertex_'+str(active),len(piv)==4 and all(piv) and min(signs)>=0 and [j for j,v in enumerate(signs) if v==0]==active)
        vertices.append({'active':active,'parameters':t,'point':z,'pivots':piv,'free_values':signs})
    z0,z1=[v['point'] for v in vertices]
    check('original_vertex_and_value',enc(z0)==data['original_point'] and enc(vertices[0]['free_values'])==col['solution'] and enc(dot(z0,[dot(r,z0) for r in M]))==fixed['exact']['fixed_value'])
    check('second_vertex',enc(z1[1:])==data['domain_LP']['parameters'])
    check('row_five_support',fs[5][4]<0 and not any(fs[5][1:4]))
    lam=-1/fs[5][4];U=lam*fs[5][0]
    check('row_five_bound_identity',[lam*x for x in fs[5]]==[U,0,0,0,-1] and U==z1[4])
    multipliers,pivlam=solve(list(map(list,zip(*[fs[i][1:] for i in active1]))),[F(0),F(0),F(0),F(-1)])
    check('independent_domain_dual',multipliers==[lam,0,0,0] and min(multipliers)==0)
    gaps=[sstar-z0[4],U-sstar];alpha=gaps[0]/(U-z0[4])
    check('strict_interpolation_bracket',all(v>0 for v in gaps) and 0<alpha<1)
    zstar=[(1-alpha)*x+alpha*y for x,y in zip(z0,z1)];signs=[dot(f,zstar) for f in fs]
    check('exact_interpolation_and_attainment',zstar[0]==1 and zstar[4]==sstar and dot(zstar,[dot(r,zstar) for r in M])==V and enc(zstar)==data['optimization']['point']==ver['domain_point'])
    check('all_85_interpolated_signs',signs==[(1-alpha)*x+alpha*y for x,y in zip(vertices[0]['free_values'],vertices[1]['free_values'])] and sum(v>0 for v in signs)==83 and [j for j,v in enumerate(signs) if v==0]==[33,56] and min(signs)==0)
    for typ,v in entries.items():
        if v is not None:check('every_fixed_forced_sign_'+str(typ),dot(v,zstar)>=0)
    for i,r in enumerate(col['kernel_basis']):check('maximizer_full_weighted_residual_'+str(i),sum(F(*v)*w*dot(f,zstar) for v,w,f in zip(r,W,column))==0)
    initial=data['optimization']['unconstrained_stationary'];iz=[F(*v) for v in initial['point']]
    check('preserved_inadmissible_stationary',[j for j,f in enumerate(fs) if dot(f,iz)<0]==[33] and dot(fs[33],iz)<0)
    failure_path=ROOT/'eight-family-fixed-separator-initial-domain-bound.json'
    failed=json.loads(failure_path.read_text())
    check('preserved_wrong_bound_direction','domain_upper_below_stationary' in failed['failures'] and U>sstar and not data['domain_LP']['upper_below_stationary'])
    report['input_hashes'][str(failure_path.relative_to(NB))]=hashlib.sha256(failure_path.read_bytes()).hexdigest()
    report.update(dual=y,dual_pivots=pivy,scaled_sums=sums,raw_sums=raw,objective_matrix=M,square_matrix=square_matrix,kappa=kappa,stationary_s=sstar,value=V,interval_gaps=[gaplo,gaphi],vertices=vertices,row_five_multiplier=lam,domain_upper=U,domain_dual_pivots=pivlam,bracket_gaps=gaps,alpha=alpha,maximizer=zstar,maximizer_free_values=signs)
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'types':500,'presentations':3000,'affine_weighted_kernel_residuals':450,'modes':81,'rank_cases':{str(k):v for k,v in sorted(Counter((len(m['layers']),m['rank']) for m in modes).items())},'positive_separator_weights':27,'cancelled_raw_scaled_columns':44,'sign_coordinate':[3,6],'value_interval':[351861924105,351861924106,10**6],'required_for_strict_exclusion':'negative everywhere','maximizer_positive_free_entries':83,'maximizer_zero_free_indices':[33,56],'strict_bracket':True,'joint_PSD_completion_asserted':False}
    save('completed')
    print(enc(report['summary']));print('Failures:',failures,'; full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)


if __name__=='__main__':
    main()
