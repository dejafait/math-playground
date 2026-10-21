"""L080 dedicated fixed-maximizer audit; no new family optimization.

Reuse L078's reviewed entry-independent direct actions. Import only arithmetic
helpers from its audit, no L080 constructor, verifier or optimizer. Consume
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
OUT = ROOT/'eight-maximizer-joint-completion-critical-audit.json'


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

    extra_names = ['eight-maximizer-joint-completion-results.json',
                   'eight-maximizer-joint-completion-verification.json',
                   'eight-family-fixed-separator-critical-audit.json']
    extra_paths = [ROOT/n for n in extra_names]
    fixed80, ver80, family_review = [json.loads(p.read_text()) for p in extra_paths]
    for path, obj in zip(extra_paths, [fixed80, ver80, family_review]):
        report['input_hashes'][str(path.relative_to(NB))] = hashlib.sha256(path.read_bytes()).hexdigest()
        check('clean_'+path.name, not obj['failures'])
        for rel, h in obj.get('input_hashes', {}).items():
            check('input_binding_'+path.name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)

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
    # Exact point from the manuscript, independent of the stored point.
    manuscript=(NB/'lemmas/L080-eight-maximizer-joint-completion-obstruction.md').read_text()
    active0=[int(v) for v in re.search(r'I0=\(([^)]+)\)',manuscript).group(1).split(',')]
    active1=[int(v) for v in re.search(r'J0=\(([^)]+)\)',manuscript).group(1).split(',')]
    vertices=[]
    for active in [active0,active1]:
        t,piv=solve([fs[i][1:] for i in active],[-fs[i][0] for i in active])
        check('vertex_'+str(active),len(piv)==4 and all(piv) and min(dot(f,[F(1)]+t) for f in fs)>=0)
        vertices.append({'active':active,'point':[F(1)]+t,'pivots':piv})
    M=[[F(*v) for v in row] for row in data['objective_matrix']]
    check('reviewed_stationary_parameter_contract',data['objective_matrix']==family_review['objective_matrix'] and M[4][4]<0)
    sstar=-M[0][4]/M[4][4]
    z0,z1=[v['point'] for v in vertices]
    alpha=(sstar-z0[4])/(z1[4]-z0[4])
    point=[(1-alpha)*x+alpha*y for x,y in zip(z0,z1)]
    check('exact_fixed_point',0<alpha<1 and point[4]==sstar and enc(point)==fixed80['point']==ver80['point']==family_review['maximizer'])
    signs=[dot(f,point) for f in fs]
    check('all_fixed_column_signs',min(signs)==0 and sum(v>0 for v in signs)==83 and [i for i,v in enumerate(signs) if not v]==[33,56])
    for i,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('fixed_original_equation_'+str(i),dot([F(*v) for v in r],signs)==F(*b))
    column_fixed=[dot(v,point) for v in column]
    for i,r in enumerate(col['kernel_basis']):
        check('fixed_weighted_residual_'+str(i),sum(F(*v)*w*f for v,w,f in zip(r,W,column_fixed))==0)
    fixed_entries={typ:None if v is None else dot(v,point) for typ,v in entries.items()}
    fixed_records=[]
    for rec, saved in zip(records,ver80['records']):
        typ=rec['type'];value=fixed_entries[typ];prs=[]
        check('fixed_full_key_'+str(typ),list(rec['key'])==saved['key'] and enc(value)==saved['value'])
        for j,pr in enumerate(rec['presentations']):
            v=None if pr['affine'] is None else dot(pr['affine'],point)
            new={'atoms':pr['atoms'],'distances':pr['distances'],'value':v};prs.append(new)
            check('fixed_presentation_'+str((typ,j)),enc(new)==saved['presentations'][j])
        if value is not None:check('fixed_entry_sign_'+str(typ),value>=0)
        fixed_records.append({'type':typ,'key':rec['key'],'value':value,'presentations':prs})
    check('unchanged_270_old_entries',all(fixed_entries[tuple(r['type'])]==F(*r['y']) for r in old['entries']))
    check('fixed_36_forced_45_free',sum(l==m==8 and v is not None for (l,m,i,j),v in fixed_entries.items())==36 and sum(v is None for v in fixed_entries.values())==45)
    report.update(point=point,alpha=alpha,vertices=vertices,column_signs=signs,fixed_records=fixed_records)
    save('fixed_point_and_normalization_checked')
    print('Exact point, all 500 keys/3000 presentations and coherent direct actions checked; failures:',failures,flush=True)

    sizes={l:c(68,l)*c(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[];rhs=[];minors=[]
    def det_small(A):
        # Complete Leibniz expansion, independent of elimination (size <=3).
        n=len(A);value=F(0)
        for perm in it.permutations(range(n)):
            term=F((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))
            for i,j in enumerate(perm):term*=A[i][j]
            value+=term
        return value
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;sv=fixed80['modes'][idx];ls=[l for l in [5,6,7] if l>=max(a,b)]
        N8=norms[68,8][a]*norms[956,8][b];D8=c(68-2*a,8-a)*c(956-2*b,8-b)
        scales={l:sigma[68,l,8,a]*sigma[956,l,8,b]/(N8/D8) for l in ls+[8]}
        check('positive_coherent_scales_'+str((a,b)),D8>0 and N8>0 and all(s>0 for s in scales.values()) and scales[8]==1)
        multiplicity=(c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
        check('positive_multiplicity_'+str((a,b)),multiplicity>0)
        def weighted(l,m):
            ll,mm=sorted([l,m])
            v=sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*fixed_entries[ll,mm,i,j] for i,j in it.product(range(ll+1),repeat=2))
            if (a,b)==(0,0):v-=p[l]*p[m]*sizes[m]
            return v*norms[68,l][a]*norms[956,l][b]
        def source(l,m):
            ll,mm=sorted([l,m])
            v=sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*fixed_entries[ll,mm,i,j] for i,j in it.product(range(ll+1),repeat=2))
            if (a,b)==(0,0):v-=p[l]*p[m]*sizes[l]*sizes[m]
            return v
        B=[[weighted(l,m) for m in ls] for l in ls];cross=[weighted(l,8) for l in ls]
        SB=[[source(l,m) for m in ls] for l in ls];st=[source(l,8) for l in ls]
        check('all_saved_source_entries_'+str((a,b)),enc(SB)==sv['base']==ver80['modes'][idx]['base'] and enc(st)==sv['cross']==ver80['modes'][idx]['cross'])
        for i,l in enumerate(ls):
            check('both_cross_directions_'+str((a,b,l)),cross[i]==weighted(8,l)==st[i]*(N8/D8)*scales[l])
            for j,m in enumerate(ls):
                check('whole_old_congruence_'+str((a,b,l,m)),B[i][j]==SB[i][j]*(N8/D8)*scales[l]*scales[m])
        for k in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),k):
                ds=det_small([[SB[i][j] for j in inds] for i in inds])
                dw=det_small([[B[i][j] for j in inds] for i in inds]);factor=F(1)
                for i in inds:factor*=(N8/D8)*scales[ls[i]]**2
                check('complete_principal_minor_'+str((a,b,inds)),ds>=0 and dw==ds*factor)
                minors.append({'mode':[a,b],'indices':inds,'source':ds,'weighted':dw,'factor':factor})
        # Reverse layer order and retain every zero-pivot cross equation.
        H=[list(reversed(r)) for r in reversed(B)];u=list(reversed(cross));cost=F(0);stages=[];rank=0
        for k in range(len(H)):
            pivot=H[k][k]
            check('reverse_pivot_'+str((a,b,k)),pivot>=0)
            if pivot==0:check('singular_original_range_'+str((a,b,k)),not any(H[k][k:]+[u[k]]))
            elif pivot>0:
                rank+=1;cost+=u[k]*u[k]/pivot
                for i in range(k+1,len(H)):
                    u[i]-=H[i][k]*u[k]/pivot
                    for j in range(k+1,len(H)):H[i][j]-=H[i][k]*H[k][j]/pivot
            stages.append({'pivot':pivot,'matrix':[r[:] for r in H],'cross':u[:]})
        inv=[F(*v) for v in ver80['modes'][idx]['inverse']]
        check('every_original_inverse_residual_'+str((a,b)),all(dot(r,inv)==t for r,t in zip(SB,st)))
        required=cost/(p[8]*N8)
        check('direct_source_singular_cost_'+str((a,b)),required==F(*sv['cost'])/(p[8]*D8)==dot(st,inv)/(p[8]*D8))
        fixedpart=sum(gamma[68,8,8,a,i]*gamma[956,8,8,b,j]*v/p[8] for (l,m,i,j),v in fixed_entries.items() if l==m==8 and v is not None)
        anchor=p[8]*sizes[8] if (a,b)==(0,0) else F(0)
        row=[-F(gamma[68,8,8,a,8-r]*gamma[956,8,8,b,8-q],c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        bound=fixedpart-anchor-required
        check('all_direct_fixed_terms_'+str((a,b)),enc(fixedpart)==sv['fixed'] and enc(anchor)==sv['anchor'])
        check('all_original_mode_rows_'+str((a,b)),enc(row)==fixed80['matrix'][idx]==ver80['matrix'][idx] and enc(bound)==fixed80['rhs'][idx]==ver80['rhs'][idx])
        modes.append({'mode':[a,b],'layers':ls,'multiplicity':multiplicity,'scales':scales,'N8':N8,'D8':D8,'source_base':SB,'source_cross':st,'weighted_base':B,'weighted_cross':cross,'inverse':inv,'reverse_stages':stages,'rank':rank,'fixed':fixedpart,'anchor':anchor,'required':required})
        matrix.append(row);rhs.append(bound)
    check('complete_306_old_minors',len(minors)==306 and [enc(r['source']) for r in minors]==ver80['old_principal_minors'])
    for l in [5,6,7,8]:
        check('full_mode_dimension_'+str(l),sum(m['multiplicity'] for m in modes if max(m['mode'])<=l)==sizes[l])
    report.update(modes=modes,matrix=matrix,rhs=rhs,old_minors=minors)
    save('all_direct_modes_and_singular_cases_checked')
    print('All 81 direct/source modes, full anchor, 306 minors and singular ranges checked; failures:',failures,flush=True)

    part=manuscript.split('**Compact rational separator.**')[1].split('Define the 43-by-43')[0]
    I=[int(v) for v in re.search(r'I=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    J=[int(v) for v in re.search(r'J=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    Kt=[[F(-1) if j==-1 else matrix[i][j] for i in I] for j in J]
    target=[F(-1) if j==-1 else F(0) for j in J]
    weights,pivots=solve(Kt,target);y=[F(0)]*81
    check('nonsingular_manuscript_basis',len(I)==len(J)==len(pivots)==43 and all(pivots) and len(set(I))==43 and len(set(J))==43)
    for i,v in zip(I,weights):y[i]=v
    check('complete_basis_substitution',all(dot(r,weights)==v for r,v in zip(Kt,target)))
    check('entire_dual',enc(y)==fixed80['exact']['dual']==ver80['dual'] and sum(y)==1 and sum(v>0 for v in y)==38)
    for i,v in enumerate(y):check('dual_nonnegative_'+str(i),v>=0)
    sums=[];raw=[]
    for j,(r,q) in enumerate(free):
        s=sum(v*row[j] for v,row in zip(y,matrix))
        rawval=-sum(y[9*a+b]*F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*c(68-2*a,8-a)*c(956-2*b,8-b)) for a,b in it.product(range(9),repeat=2))
        check('raw_and_scaled_'+str((r,q)),s>=0 and rawval==s*c(8,r)*c(60,r)*c(8,q)*c(948,q)/p[8] and enc(s)==fixed80['exact']['sums'][j]==ver80['scaled_sums'][j] and enc(rawval)==fixed80['exact']['raw_sums'][j]==ver80['raw_sums'][j])
        sums.append(s);raw.append(rawval)
    check('essential_6_3_sign',sum(v==0 for v in sums)==44 and [rq for rq,v in zip(free,sums) if v>0]==[(6,3)])
    weighted_fixed=dot(y,[m['fixed'] for m in modes]);weighted_anchor=dot(y,[m['anchor'] for m in modes]);weighted_required=dot(y,[m['required'] for m in modes])
    value=weighted_fixed-weighted_anchor-weighted_required
    check('full_pairing',value==dot(y,rhs) and enc(value)==fixed80['exact']['value']==ver80['pairing'])
    for name,v in [('weighted_fixed',weighted_fixed),('weighted_anchor',weighted_anchor),('weighted_required',weighted_required)]:
        check(name,enc(v)==ver80[name])
    lo=F(-25046444520,10**6);hi=F(-25046444519,10**6)
    gaps=[value-lo,hi-value]
    check('strict_negative_interval',gaps[0]>=0 and gaps[1]>0 and hi<0)
    report.update(dual=y,dual_rows=I,dual_columns=J,dual_matrix_transposed=Kt,dual_pivots=pivots,scaled_sums=sums,raw_sums=raw,weighted_fixed=weighted_fixed,weighted_anchor=weighted_anchor,weighted_required=weighted_required,pairing=value,interval_gaps=gaps)
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'types':500,'presentations':3000,'modes':81,'old_principal_minors':len(minors),'rank_cases':{str(k):v for k,v in sorted(Counter((len(m['layers']),m['rank']) for m in modes).items())},'positive_weights':sum(v>0 for v in y),'zero_sums':sum(v==0 for v in sums),'sign_coordinate':[6,3],'minimum_weight':min(y),'minimum_scaled_sum':min(sums),'required_pairing_lower_bound':0,'actual_pairing_interval':[lo,hi],'signed_completion_excluded':False,'family_excluded':False}
    save('completed')
    print(enc(report['summary']));print('Failures:',failures,'; full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
