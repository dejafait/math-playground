"""L081 dedicated common-witness audit; no completion or optimization.

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
OUT = ROOT/'eight-two-separator-critical-audit.json'


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

    witness_names = ['eight-two-separator-intersection-results.json',
                     'eight-two-separator-slice-results.json',
                     'eight-two-separator-intersection-verification.json']
    witness_paths = [ROOT/n for n in witness_names]
    assembly, witness, verified = [json.loads(p.read_text()) for p in witness_paths]
    for path, obj in zip(witness_paths, [assembly, witness, verified]):
        report['input_hashes'][str(path.relative_to(NB))] = hashlib.sha256(path.read_bytes()).hexdigest()
        check('clean_'+path.name, not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('binding_'+path.name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)

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
        direct=[[sum(c(i,s)*c(8-i,u-s)*c(l-i,k-s)*c(n-8-l+i,m-u-k+s)
                     for s in range(9)) for u in range(m+1)] for i in range(l+1)]
        check('full_subset_transition_'+str((n,l,m,k)),T==direct)
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
    # Build every quadratic from affine weighted actions, in reverse layer
    # elimination order. No stored objective matrix defines the point.
    sizes={l:c(68,l)*c(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[];minor_records=[]
    def determinant(A):
        value=F(0)
        for perm in it.permutations(range(len(A))):
            v=F((-1)**sum(perm[i]>perm[j] for i in range(len(A)) for j in range(i+1,len(A))))
            for i,j in enumerate(perm):v*=A[i][j]
            value+=v
        return value
    def quad(M,z):return dot(z,[dot(r,z) for r in M])
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;ls=[l for l in [5,6,7] if l>=max(a,b)]
        N8=norms[68,8][a]*norms[956,8][b];D8=c(68-2*a,8-a)*c(956-2*b,8-b)
        scales={l:sigma[68,l,8,a]*sigma[956,l,8,b]/(N8/D8) for l in ls+[8]}
        check('positive_scales_'+str(idx),N8>0 and D8>0 and all(v>0 for v in scales.values()) and scales[8]==1)
        multiplicity=(c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
        check('positive_multiplicity_'+str(idx),multiplicity>0)
        def block(l,m,direct):
            ll,mm=sorted([l,m]);v=av(0)
            for i,j in it.product(range(ll+1),repeat=2):
                coef=(gamma[68,l,m,a,i]*gamma[956,l,m,b,j] if direct else beta(68,l,m,a,i)*beta(956,l,m,b,j))
                v=[x+coef*y for x,y in zip(v,entries[ll,mm,i,j])]
            if a==b==0:v[0]-=p[l]*p[m]*sizes[m]*(1 if direct else sizes[l])
            if direct:v=[x*norms[68,l][a]*norms[956,l][b] for x in v]
            return v
        Bs=[[block(l,m,False) for m in ls] for l in ls]
        Bd=[[block(l,m,True) for m in ls] for l in ls]
        check('immutable_old_blocks_'+str(idx),not any(any(v[1:]) for row in Bs+Bd for v in row))
        SB=[[v[0] for v in row] for row in Bs];B=[[v[0] for v in row] for row in Bd]
        st=[block(l,8,False) for l in ls];cross=[block(l,8,True) for l in ls]
        for i,l in enumerate(ls):
            check('both_affine_cross_directions_'+str((idx,l)),cross[i]==block(8,l,True)==[v*(N8/D8)*scales[l] for v in st[i]])
            for j,m in enumerate(ls):check('old_congruence_'+str((idx,l,m)),B[i][j]==SB[i][j]*(N8/D8)*scales[l]*scales[m])
        sv=assembly['modes'][idx]
        check('complete_source_affine_entries_'+str(idx),enc(SB)==sv['base'] and enc(st)==sv['cross'])
        for k in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),k):
                ds=determinant([[SB[i][j] for j in inds] for i in inds])
                dw=determinant([[B[i][j] for j in inds] for i in inds]);fac=F(1)
                for i in inds:fac*=(N8/D8)*scales[ls[i]]**2
                check('old_minor_'+str((idx,inds)),ds>=0 and dw==ds*fac)
                minor_records.append({'mode':[a,b],'indices':inds,'source':ds,'weighted':dw})
        H=[list(reversed(r)) for r in reversed(B)];u=[r[:] for r in reversed(cross)]
        cost=[[F(0)]*5 for _ in range(5)];stages=[];rank=0
        for k in range(len(H)):
            pivot=H[k][k];check('reverse_pivot_'+str((idx,k)),pivot>=0)
            if pivot==0:check('all_affine_singular_residuals_'+str((idx,k)),not any(H[k][k:]+u[k]))
            elif pivot>0:
                rank+=1
                cost=[[v+u[k][i]*u[k][j]/pivot for j,v in enumerate(row)] for i,row in enumerate(cost)]
                for i in range(k+1,len(H)):
                    u[i]=[x-H[i][k]*y/pivot for x,y in zip(u[i],u[k])]
                    for j in range(k+1,len(H)):H[i][j]-=H[i][k]*H[k][j]/pivot
            stages.append({'pivot':pivot,'matrix':[r[:] for r in H],'affine_cross':[r[:] for r in u]})
        cost=[[v/(p[8]*N8) for v in row] for row in cost]
        inv=[[F(*v) for v in r] for r in sv['inverse_affine']]
        residuals=[[sum(SB[i][j]*inv[j][k] for j in range(len(ls)))-st[i][k] for k in range(5)] for i in range(len(ls))]
        sourcecost=[[sum(st[j][i]*inv[j][k] for j in range(len(ls)))/(p[8]*D8) for k in range(5)] for i in range(5)]
        check('complete_inverse_and_weighted_cost_'+str(idx),not any(any(r) for r in residuals) and enc(residuals)==sv['range_residuals'] and cost==sourcecost and enc(cost)==sv['cost'])
        fixedpart=av(0)
        for (l,m,i,j),v in entries.items():
            if l==m==8 and v is not None:
                coef=gamma[68,8,8,a,i]*gamma[956,8,8,b,j]/p[8]
                fixedpart=[x+coef*y for x,y in zip(fixedpart,v)]
        anchor=p[8]*sizes[8] if a==b==0 else F(0)
        fixedminus=fixedpart[:];fixedminus[0]-=anchor
        Q=[[-x for x in row] for row in cost];Q[0][0]+=fixedminus[0]
        for k in range(1,5):Q[0][k]+=fixedminus[k]/2;Q[k][0]+=fixedminus[k]/2
        row=[-gamma[68,8,8,a,8-r]*gamma[956,8,8,b,8-q]/(c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        check('original_rows_and_full_quadratic_'+str(idx),enc(row)==assembly['matrix'][idx]==fixed['matrix'][idx]==fixed80['matrix'][idx] and enc(fixedminus)==sv['fixed_minus_anchor'] and enc(Q)==sv['quadratic'] and Q==list(map(list,zip(*Q))))
        modes.append({'mode':[a,b],'layers':ls,'multiplicity':multiplicity,'N8':N8,'D8':D8,'scales':scales,'source_base':SB,'source_cross':st,'weighted_base':B,'weighted_cross':cross,'reverse_stages':stages,'rank':rank,'cost':cost,'fixed':fixedpart,'anchor':anchor,'quadratic':Q})
        matrix.append(row)
    for l in [5,6,7,8]:check('full_layer_dimension_'+str(l),sum(m['multiplicity'] for m in modes if max(m['mode'])<=l)==sizes[l])
    check('all_old_minors',len(minor_records)==306)
    report.update(modes=modes,matrix=matrix,old_minors=minor_records);save('all_affine_modes_rebuilt')
    print('All 81 affine bounds, full anchor and singular ranges rebuilt; failures:',failures,flush=True)

    # Manuscript systems, independent of stored active rows/columns.
    certificates=[]
    for h,(ID,header,n,positive,rq,saved) in enumerate([
            ('L078','**Compact exact separator.**',42,27,(3,6),fixed),
            ('L080','**Compact rational separator.**',43,38,(6,3),fixed80)]):
        path=next((NB/'lemmas').glob(ID+'-*.md'))
        text=path.read_text().split(header)[1].split('Define the')[0]
        I=[int(v) for v in re.search(r'I=\((.*?)\)',text,re.S).group(1).replace('\n','').split(',')]
        J=[int(v) for v in re.search(r'J=\((.*?)\)',text,re.S).group(1).replace('\n','').split(',')]
        Kt=[[F(-1) if j==-1 else matrix[i][j] for i in I] for j in J]
        target=[F(-1) if j==-1 else F(0) for j in J]
        weights,pivots=solve(Kt,target);y=[F(0)]*81
        for i,v in zip(I,weights):y[i]=v
        check(ID+'_canonical_system',len(I)==len(J)==len(set(I))==len(set(J))==len(pivots)==n and all(pivots) and all(dot(r,weights)==v for r,v in zip(Kt,target)))
        check(ID+'_unchanged_weights',min(y)>=0 and sum(y)==1 and sum(v>0 for v in y)==positive and enc(y)==saved['exact']['dual']==assembly['pairings'][h]['weights']==verified['certificates'][h]['weights'])
        sums=[];raw=[]
        for j,(r,q) in enumerate(free):
            v=dot(y,[row[j] for row in matrix]);V=c(8,r)*c(60,r)*c(8,q)*c(948,q)
            rawval=-sum(y[9*a+b]*F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*c(68-2*a,8-a)*c(956-2*b,8-b)) for a,b in it.product(range(9),repeat=2))
            check(ID+'_raw_original_'+str(j),v>=0 and rawval==v*V/p[8] and enc(v)==assembly['pairings'][h]['scaled_sums'][j]==verified['certificates'][h]['scaled_sums'][j] and enc(rawval)==assembly['pairings'][h]['raw_sums'][j]==verified['certificates'][h]['raw_sums'][j])
            sums.append(v);raw.append(rawval)
        check(ID+'_sole_positive_coordinate',[ij for ij,v in zip(free,sums) if v>0]==[rq] and sum(v==0 for v in sums)==44)
        M=[[sum(y[k]*modes[k]['quadratic'][i][j] for k in range(81)) for j in range(5)] for i in range(5)]
        check(ID+'_complete_quadratic',enc(M)==assembly['pairings'][h]['M'])
        certificates.append({'label':ID,'I':I,'J':J,'system_transposed':Kt,'pivots':pivots,'weights':y,'scaled_sums':sums,'raw_sums':raw,'M':M})
    M1,M2=[r['M'] for r in certificates]
    check('old_stationary_contract',M1[4][4]<0 and enc(M1)==family_review['objective_matrix'] and all(M1[i][j]==0 for i,j in it.product(range(5),repeat=2) if i in [1,2,3] or j in [1,2,3]))
    s=-M1[0][4]/M1[4][4]
    G=[[M2[i][j] for j in [2,3]] for i in [2,3]];g=[M2[i][0]+M2[i][4]*s for i in [2,3]]
    detG=determinant(G);check('recipe_nonsingular',detG!=0)
    uv,pivots=solve(G,[-v for v in g]);point=[F(1),F(0),*uv,s]
    check('identical_point',enc(point)==witness['point']==verified['point'])
    factors=[dot(f,point) for f in fs]
    check('complete_domain_and_zeros',len(factors)==85 and min(factors)==0 and sum(v>0 for v in factors)==84 and [i for i,v in enumerate(factors) if v==0]==[56] and enc(factors)==witness['column_factors']==verified['factors'])
    for j,(r,b) in enumerate(zip(col['equations'],col['rhs'])):check('original_point_equation_'+str(j),dot([F(*v) for v in r],factors)==F(*b))
    check('all_90_original_equations',len(col['equations'])==len(col['rhs'])==90)
    fullcolumn=[dot(r,point) for r in column]
    for j,r in enumerate(col['kernel_basis']):check('original_weighted_point_kernel_'+str(j),dot([F(*v)*w for v,w in zip(r,W)],fullcolumn)==0)
    # Full fixed-key evidence, independent actual supports above.
    check('all_verifier_types_present',len(verified['records'])==500)
    for rec,sv in zip(records,verified['records']):
        typ=rec['type'];v=None if rec['affine'] is None else dot(rec['affine'],point)
        keys=[x['atoms'] for x in rec['presentations']]
        check('full_point_presentations_'+str(typ),list(typ)==sv['type'] and sorted(keys)==sorted(sv['keys']) and enc(v)==sv['value'] and all(pr['affine'] is None or dot(pr['affine'],point)==v for pr in rec['presentations']))
        if v is not None:check('all_fixed_moment_signs_'+str(typ),v>=0)
    bounds=[];fixedmodes=[]
    for idx,(m,sv) in enumerate(zip(modes,verified['modes'])):
        st=[dot(v,point) for v in m['source_cross']];SB=m['source_base']
        inv=[F(*v) for v in sv['inverse']];res=[dot(r,inv)-v for r,v in zip(SB,st)]
        check('complete_original_inverse_'+str(idx),not any(res) and enc(res)==sv['range_residuals'] and enc(SB)==sv['base'] and enc(st)==sv['cross'])
        cost=dot(st,inv)/(p[8]*m['D8']);fixedpart=dot(m['fixed'],point);anchor=m['anchor'];bound=fixedpart-anchor-cost
        check('complete_original_bound_'+str(idx),cost==quad(m['cost'],point) and enc(cost)==sv['cost'] and enc(fixedpart)==sv['fixed'] and enc(anchor)==sv['anchor'] and enc(bound)==sv['bound']==verified['rhs'][idx]==witness['original_mode_rhs'][idx] and bound==quad(m['quadratic'],point) and enc(matrix[idx])==verified['matrix'][idx])
        fixedmodes.append({'mode':m['mode'],'cross':st,'inverse':inv,'residuals':res,'fixed':fixedpart,'anchor':anchor,'cost':cost,'bound':bound});bounds.append(bound)
    intervals=[[F(351861924105,10**6),F(351861924106,10**6)],[F(401569066,10**6),F(401569067,10**6)]]
    for h,cert in enumerate(certificates):
        y=cert['weights'];value=dot(y,bounds);lo,hi=intervals[h]
        parts={key:dot(y,[m[key] for m in fixedmodes]) for key in ['fixed','anchor','cost']}
        check(cert['label']+'_same_point_pairing',value==quad(cert['M'],point)==parts['fixed']-parts['anchor']-parts['cost'] and enc(value)==verified['certificates'][h]['pairing']==witness['pairings'][h] and enc(parts)==verified['certificates'][h]['parts'])
        check(cert['label']+'_strict_interval',0<lo<=value<hi)
        check(cert['label']+'_zero_completion_aggregate',dot(cert['scaled_sums'],[F(0)]*45)==0<value)
        cert.update(pairing=value,parts=parts,interval=[lo,hi],interval_gaps=[value-lo,hi-value])
    report.update(certificates=certificates,point=point,factors=factors,stationary_system=G,stationary_rhs=[-v for v in g],stationary_determinant=detG,stationary_pivots=pivots,full_column=fullcolumn,fixed_modes=fixedmodes,bounds=bounds)
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'types':500,'presentations':3000,'original_domain_rows':85,'original_kernel_rows':90,'modes':81,'old_minors':len(minor_records),'rank_cases':{str(k):v for k,v in sorted(Counter((len(m['layers']),m['rank']) for m in modes).items())},'actual_minimum_factor':min(factors),'required_factor_bound':0,'positive_factors':84,'zero_factors':[56],'actual_pairing_intervals':intervals,'required_pairing_bound':0,'simultaneous_completion_tested':False}
    save('completed')
    print(enc(report['summary']));print('Failures:',failures,'; full certificate:',OUT.relative_to(NB))
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
