"""L083 dedicated audit of the unchanged fully cancelling family certificate.

Reuse L078's reviewed entry-independent direct actions. Import only arithmetic
helpers from its audit, no L083 constructor, verifier or optimizer. Consume
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
OUT = ROOT/'fully-cancelling-separator-family-critical-audit.json'


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

    extra_names = ['fully-cancelling-separator-family-results.json',
                   'fully-cancelling-separator-family-verification.json',
                   'eight-common-column-joint-completion-critical-audit.json',
                   'eight-common-column-joint-completion-results.json',
                   'fully-cancelling-family-diagnostic.json',
                   'fully-cancelling-family-initial-failure.json']
    extra_paths = [ROOT/n for n in extra_names]
    target, verified, audit82, fixed82, diagnostic, initial = [json.loads(p.read_text()) for p in extra_paths]
    for path, obj in zip(extra_paths, [target,verified,audit82,fixed82,diagnostic,initial]):
        report['input_hashes'][str(path.relative_to(NB))] = hashlib.sha256(path.read_bytes()).hexdigest()
        if 'failures' in obj: check('clean_'+path.name, not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('input_binding_'+path.name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)

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
        n,l,m,k=tr['indices']
        T=[[sum(c(i,h)*c(8-i,j-h)*c(l-i,k-h)*c(n-8-l+i,m-j-k+h) for h in range(9)) for j in range(m+1)] for i in range(l+1)]
        check('fresh_disjoint_region_transition_'+str((n,l,m,k)),T==tr['matrix'])
        check('transition_row_totals_'+str((n,l,m,k)),all(sum(row)==c(l,k)*c(n-l,m-k) for row in T))
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
            check('five_coherent_cross_coefficients_'+str((a,b,l)),q[i]==weighted(8,l)==[F(*v)*(N8/D8)*scales[l] for v in sv['cross_affine'][i]])
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

    # Bind the complete step-292 arrays and step-290 affine contracts to
    # this fresh original-domain and direct weighted reconstruction.
    check('full_85_row_domain',enc(fs)==target['domain']==verified['domain']==audit82['family'])
    check('full_150_affine_column',enc(column)==target['affine_column']==audit82['affine_column'])
    check('full_90_weighted_equations',enc(kernel_residuals)==target['weighted_kernel_residuals']==verified['weighted_kernel_residuals']==audit82['weighted_kernel_residuals'])
    for k,r in enumerate(records):
        vr=verified['records'][k]; ar=audit82['records'][k]
        check('entire_saved_record_'+str(k),enc(r)==ar and
              enc(r['type'])==vr['type'] and enc(r['key'])==vr['key'] and enc(r['affine'])==vr['affine'] and
              enc([{f:p[f] for f in ['atoms','distances','affine']} for p in r['presentations']])==vr['presentations'])
    check('original_free_order',list(map(list,free))==target['free'])
    def det_small(A):
        value=F(0)
        for perm in it.permutations(range(len(A))):
            term=F((-1)**sum(perm[i]>perm[j] for i in range(len(A)) for j in range(i+1,len(A))))
            for i,j in enumerate(perm):term*=A[i][j]
            value+=term
        return value
    minors=[];matrices=[];oldpoint=[F(*v) for v in fixed82['point']]
    for idx,m in enumerate(modes):
        a,b=m['mode'];ls=m['layers'];sv=target['modes'][idx];vv=verified['modes'][idx];aa=audit82['modes'][idx]
        D8=c(68-2*a,8-a)*c(956-2*b,8-b)
        def source(l,h):
            ll,mm=sorted([l,h]);v=[sum(beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)*entries[ll,mm,i,j][k] for i,j in it.product(range(ll+1),repeat=2)) for k in range(5)]
            if a==b==0:v[0]-=p[l]*p[h]*sizes[l]*sizes[h]
            return v
        SB=[[source(l,h)[0] for h in ls] for l in ls];cross=[source(l,8) for l in ls]
        check('all_old_entries_constant_'+str(idx),all(not any(source(l,h)[1:]) for l,h in it.product(ls,repeat=2)))
        check('all_source_bases_'+str(idx),enc(SB)==sv['base']==vv['base']==aa['source_base'])
        check('all_source_affine_cross_'+str(idx),enc(cross)==sv['cross']==vv['cross'])
        check('all_weighted_cost_coefficients_'+str(idx),enc(m['cost'])==sv['cost']==vv['cost'])
        inv=[[F(*v) for v in r] for r in sv['inverse_affine']]
        residuals=[[sum(SB[i][j]*inv[j][k] for j in range(len(ls)))-cross[i][k] for k in range(5)] for i in range(len(ls))]
        check('all_original_inverse_residuals_'+str(idx),all(not any(r) for r in residuals) and enc(residuals)==sv['range_residuals'])
        inv_cost=[[sum(cross[j][k]*inv[j][h] for j in range(len(ls)))/(p[8]*D8) for h in range(5)] for k in range(5)]
        check('all_inverse_bilinear_entries_'+str(idx),inv_cost==m['cost'])
        for k in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),k):
                d=det_small([[SB[i][j] for j in inds] for i in inds]);minors.append(d)
                check('all_old_minor_'+str((idx,inds)),d>=0)
        forced=[sum(F(beta(68,8,8,a,i)*beta(956,8,8,b,j),p[8]*D8)*v[k] for (l,h,i,j),v in entries.items() if l==h==8 and v is not None) for k in range(5)]
        anchor=p[8]*sizes[8] if a==b==0 else F(0)
        minus=forced[:];minus[0]-=anchor
        check('full_anchor_and_forced_'+str(idx),minus==m['fixed'] and enc(minus)==sv['fixed_minus_anchor'] and enc(forced)==vv['forced'] and enc(anchor)==vv['anchor'])
        row=[-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D8*c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        check('all_original_rows_'+str(idx),row==m['row'] and enc(row)==target['matrix'][idx]==verified['matrix'][idx]==audit82['matrix'][idx])
        M=[[-v for v in r] for r in m['cost']];M[0][0]+=minus[0]
        for j in range(1,5):M[0][j]+=minus[j]/2;M[j][0]+=minus[j]/2
        check('all_25_mode_coefficients_'+str(idx),M==list(map(list,zip(*M))) and enc(M)==sv['quadratic']==vv['quadratic'])
        check('step290_full_fixed_specialization_'+str(idx),enc([dot(r,oldpoint) for r in cross])==aa['source_cross'] and enc(dot(forced,oldpoint))==aa['fixed'] and enc(anchor)==aa['anchor'] and enc(dot(oldpoint,[dot(r,oldpoint) for r in m['cost']]))==aa['required'] and enc(dot(oldpoint,[dot(r,oldpoint) for r in M]))==audit82['rhs'][idx])
        multiplicity=(c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
        check('positive_normalizations_'+str(idx),D8>0 and multiplicity>0 and all(v>0 for v in m['scales'].values()) and m['scales'][8]==1)
        m.update(source_base=SB,source_cross=cross,inverse_affine=inv,original_residuals=residuals,forced=forced,anchor=anchor,quadratic=M,multiplicity=multiplicity,D8=D8)
        matrices.append(M)
    check('all_306_old_minors',len(minors)==306 and enc(minors)==verified['old_minors'] and enc(minors)==[r['source'] for r in audit82['old_minors']])
    for l in [5,6,7,8]:
        check('full_mode_dimension_'+str(l),sum(m['multiplicity'] for m in modes if max(m['mode'])<=l)==sizes[l])
    manuscript=(NB/'lemmas/L082-common-column-joint-completion-obstruction.md').read_text()
    part=manuscript.split('**Canonical exact separator.**')[1].split('Let K_')[0]
    I=[int(v) for v in re.search(r'I=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    check('manuscript_all_columns',re.search(r'J=\((.*?)\)',part,re.S).group(1)=='-1,0,1,...,44')
    J=[-1]+list(range(45));Kt=[[F(-1) if j==-1 else modes[i]['row'][j] for i in I] for j in J]
    rhs=[F(-1)]+[F(0)]*45;local,pivots=solve(Kt,rhs);y=[F(0)]*81
    for i,v in zip(I,local):y[i]=v
    check('same_nonsingular_46by46_definition',len(I)==len(set(I))==len(J)==len(pivots)==46 and all(pivots) and I==target['I']==audit82['dual_rows'] and J==target['J']==audit82['dual_columns'] and enc(Kt)==audit82['dual_matrix_transposed'])
    check('all_defining_equations',all(dot(r,local)==v for r,v in zip(Kt,rhs)))
    check('unchanged_canonical_weights',min(y)==0 and sum(y)==1 and sum(v>0 for v in y)==28 and enc(y)==target['weights']==verified['weights']==audit82['dual']==fixed82['exact']['dual'])
    sums=[];raw=[]
    for j,(r,q) in enumerate(free):
        scaled=sum(v*m['row'][j] for v,m in zip(y,modes))
        original=-sum(y[9*a+b]*F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*c(68-2*a,8-a)*c(956-2*b,8-b)) for a,b in it.product(range(9),repeat=2))
        check('each_original_and_raw_cancellation_'+str(j),scaled==original==0 and enc(scaled)==target['scaled_sums'][j]==verified['scaled_sums'][j]==audit82['scaled_sums'][j] and enc(original)==target['raw_sums'][j]==verified['raw_sums'][j]==audit82['raw_sums'][j])
        sums.append(scaled);raw.append(original)
    M=[[sum(v*m['quadratic'][i][j] for v,m in zip(y,modes)) for j in range(5)] for i in range(5)]
    check('full_exact_pairing_matrix',enc(M)==target['M']==verified['M'])
    gamma=-M[4][4];s=-M[0][4]/M[4][4];e=[-s,F(0),F(0),F(0),F(1)]
    squareM=[[-gamma*x*z for z in e] for x in e]
    check('all_25_negative_square_entries',gamma>0 and M==squareM and enc(gamma)==verified['gamma'] and enc(-gamma)==target['square']['coefficient'] and enc(s)==target['square']['stationary_t78']==verified['stationary_t78'] and target['square']['constant_residual']==[0,1])
    oldvalue=dot(oldpoint,[dot(r,oldpoint) for r in M])
    check('old_negative_pairing_unchanged',F(-1935470,10**14)<=oldvalue<F(-1935469,10**14) and enc(oldvalue)==audit82['pairing']==fixed82['exact']['value'])
    manuscript83=(NB/'lemmas/L083-fully-cancelling-separator-attained-zero-on-column-family.md').read_text()
    active_sets=[list(map(int,match.split(','))) for match in re.findall(r't[01]=-\(A_\(([^)]+)\)\)',manuscript83)]
    check('manuscript_endpoint_recipes',active_sets==[[27,33,56,63],[5,26,33,56]])
    endpoints=[]
    for k,inds in enumerate(active_sets):
        t,piv=solve([fs[j][1:] for j in inds],[-fs[j][0] for j in inds]);z=[F(1)]+t;signs=[dot(f,z) for f in fs]
        check('endpoint_nonsingular_'+str(k),len(piv)==4 and all(piv) and all(dot(fs[j],z)==0 for j in inds))
        for j,v in enumerate(signs):check('endpoint_sign_'+str((k,j)),v>=0)
        check('complete_endpoint_arrays_'+str(k),[j for j,v in enumerate(signs) if not v]==inds and enc(z)==target['endpoints'][k]['point']==verified['endpoints'][k] and enc(signs)==target['endpoints'][k]['factors'])
        endpoints.append({'active':inds,'point':z,'pivots':piv,'factors':signs})
    z0,z1=[r['point'] for r in endpoints];gaps=[s-z0[4],z1[4]-s]
    alpha=(s-z0[4])/(z1[4]-z0[4]);point=[(1-alpha)*x+alpha*z for x,z in zip(z0,z1)];factors=[dot(f,point) for f in fs]
    check('strict_interpolation',all(v>0 for v in gaps) and 0<alpha<1 and point[0]==1 and point[4]==s and enc(alpha)==target['alpha']==verified['alpha'])
    for j,v in enumerate(factors):check('interior_sign_and_affine_interpolation_'+str(j),v>=0 and v==(1-alpha)*endpoints[0]['factors'][j]+alpha*endpoints[1]['factors'][j])
    check('full_witness_and_83_positive_factors',sum(v>0 for v in factors)==83 and [j for j,v in enumerate(factors) if not v]==[33,56] and enc(point)==target['point']==verified['point'] and enc(factors)==target['factors']==verified['factors'])
    for i,(row,b) in enumerate(zip(col['equations'],col['rhs'])):check('witness_original_equation_'+str(i),dot([F(*v) for v in row],factors)==F(*b))
    for i,row in enumerate(col['kernel_basis']):check('witness_full_weighted_kernel_'+str(i),sum(F(*v)*w*dot(f,point) for v,w,f in zip(row,W,column))==0)
    bounds=[dot(point,[dot(r,point) for r in m['quadratic']]) for m in modes]
    fixedsum=sum(v*dot(m['forced'],point) for v,m in zip(y,modes))
    anchorsum=sum(v*m['anchor'] for v,m in zip(y,modes))
    costsum=sum(v*dot(point,[dot(r,point) for r in m['cost']]) for v,m in zip(y,modes))
    value=dot(y,bounds)
    check('all_81_original_witness_bounds',enc(bounds)==target['bounds']==verified['bounds'])
    check('attained_zero_separate_contributions',value==fixedsum-anchorsum-costsum==dot(point,[dot(r,point) for r in M])==0 and enc(fixedsum)==verified['weighted_forced'] and enc(anchorsum)==verified['weighted_anchor'] and enc(costsum)==verified['weighted_cost'])
    iz=[F(*v) for v in diagnostic['point']];isigns=[dot(f,iz) for f in fs]
    check('preserved_inadmissible_zero_representative',iz==[1,0,0,0,s] and [j for j,v in enumerate(isigns) if v<0]==[33] and enc(isigns)==diagnostic['factors'] and enc(M)==diagnostic['M'] and diagnostic['value']==[0,1])
    check('preserved_pre_verdict_TypeError',initial['stage']=='first original mode' and 'TypeError' in initial['error'] and initial['mathematical_verdict'] is None)
    report.update(modes=modes,old_minors=minors,dual=y,dual_rows=I,dual_columns=J,dual_matrix_transposed=Kt,dual_pivots=pivots,scaled_sums=sums,raw_sums=raw,M=M,square_matrix=squareM,gamma=gamma,stationary_t78=s,old_pairing=oldvalue,endpoints=endpoints,bracket_gaps=gaps,alpha=alpha,point=point,factors=factors,bounds=bounds,weighted_forced=fixedsum,weighted_anchor=anchorsum,weighted_cost=costsum,value=value)
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'types':500,'presentations':3000,'modes':81,'old_principal_minors':len(minors),'affine_weighted_kernel_equations':90,'rank_cases':{str(k):v for k,v in sorted(Counter((len(m['layers']),m['rank']) for m in modes).items())},'positive_weights':sum(v>0 for v in y),'cancelled_original_and_raw_coordinates':45,'actual_pairing':value,'required_nonnegative_pairing':0,'actual_minimum_factor':min(factors),'required_minimum_factor':0,'positive_factors':83,'zero_factors':[33,56],'joint_completion_asserted':False}
    save('completed')
    print(enc(report['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)

if __name__=='__main__':main()
