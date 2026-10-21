"""Independent original-row verification of the unchanged L082 family pairing.
Uses only standard-library exact arithmetic helpers from the L082 verifier.
Reverse-order singular elimination replaces the constructor's Cramer solves.
"""
import hashlib
import itertools as it
import json
import re
from collections import Counter
from pathlib import Path
from verify_eight_common_column_joint_completion import Q, C, beta, solve, determinant, dot, enc, av
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'fully-cancelling-separator-family-verification.json'
def main():
    names=['fully-cancelling-separator-family-results.json',
           'eight-family-fixed-separator-results.json',
           'eight-distance-full-base-kernel-results.json',
           'maximizer-excluded-anchor-results.json',
           'eight-common-column-joint-completion-critical-audit.json',
           'eight-common-column-joint-completion-results.json']
    paths=[ROOT/n for n in names]
    data,family,col,old,audit,fixed82=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def check(n,ok):
        checks.append(n)
        if not ok:failures.append(n)
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def save(stage):
        report.update(stage=stage,checks=checks,failures=failures)
        OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    for n,obj in zip(names,[data,family,col,old,audit,fixed82]):
        check('clean_'+n,not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('input_binding_'+n+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    p=[Q(*v) for v in old['pairs_through_14']]
    check('positive_original_rho_p8',Q(*old['rho'])>0 and p[8]==Q(16792471,1181138102168120460)>0 and old['pairs_through_14']==col['pairs_through_14'])
    nonpiv=[56,63,69,78];rr=[[Q(*v) for v in r] for r in col['equation_rref']]
    fs=[[Q(0)]*5 for _ in range(85)]
    for k,j in enumerate(nonpiv):fs[j][k+1]=Q(1)
    for i,j in enumerate(col['equation_pivots']):fs[j]=[rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    check('full_RREF_domain',len(col['equation_pivots'])==81 and enc(fs)==data['domain']==family['domain']['nonnegative_affine'])
    for i,(r,b) in enumerate(zip(col['equations'],col['rhs'])):
        check('all_affine_compatibility_'+str(i),[sum(Q(*v)*f[k] for v,f in zip(r,fs)) for k in range(5)]==av(Q(*b)))
    base={tuple(r['type']):av(Q(*r['y'])) for r in old['entries']}
    column=[]
    for r in col['column']:
        v=[p[8]*x for x in fs[r['variable']]] if r['kind']=='free' else av(Q(*r['value']))
        column.append(v)
        if r['orbit']!=[0,0,0]:base[r['orbit'][0],8,*r['orbit'][1:]]=v
    W=[1]+[C(8,i)*C(60,l-i)*C(8,j)*C(948,l-j) for l,i,j in col['orbits'][1:]]
    check('step290_full_affine_contracts',enc(fs)==audit['family'] and enc(column)==audit['affine_column'])
    residuals=[]
    check('full_kernel_dimensions',len(col['kernel_basis'])==90 and len(column)==len(W)==150 and enc(column)==data['affine_column'])
    for i,k in enumerate(col['kernel_basis']):
        res=[sum(Q(*v)*w*f[j] for v,w,f in zip(k,W,column)) for j in range(5)]
        residuals.append(res);check('full_affine_weighted_kernel_'+str(i),res==[0]*5)
    check('entire_saved_kernel_residuals',enc(residuals)==data['weighted_kernel_residuals']==audit['weighted_kernel_residuals'])
    entries={};dictionary={};free=[];free_keys=[];records=[]
    # Algebraic bit permutation of complete atom vectors, independent of
    # the constructor's actual-support membership enumeration.
    for l,m in it.combinations_with_replacement([5,6,7,8],2):
        for i,j in it.product(range(l+1),repeat=2):
            atoms=[956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
            values=[];keys=[];prs=[]
            for perm in it.permutations([0,1,2]):
                aa=[0]*8
                for mask,n in enumerate(atoms):
                    bits=[bool(mask&b) for b in [4,2,1]]
                    aa[4*bits[perm[0]]+2*bits[perm[1]]+bits[perm[2]]]+=n
                ds=[sum(n for mask,n in enumerate(aa) if mask&a and not mask&b) for a,b in [(4,2),(4,1),(2,1)]]
                ii=sum(n for mask,n in enumerate(aa) if mask&4 and not mask&2 and not mask&1)
                jj=sum(n for mask,n in enumerate(aa) if not mask&4 and mask&2 and mask&1)
                if 0 in ds:v=av(p[max(ds)])
                elif any(0<d<5 for d in ds):v=av(0)
                else:v=base.get((*sorted(ds[:2]),ii,jj))
                saved=family['records'][len(records)]['presentations'][len(prs)]
                check('complete_affine_presentation_'+str((l,m,i,j,perm)),aa==saved['atoms'] and ds==saved['distances'] and enc(v)==saved['affine'])
                keys.append(tuple(aa));prs.append({'atoms':aa,'distances':ds,'affine':v})
                if v is not None:values.append(v)
            key=min(keys)
            if key in dictionary:values.append(dictionary[key])
            value=values[0] if values else None
            rec=family['records'][len(records)]
            check('all_key_consistency_'+str((l,m,i,j)),all(v==value for v in values) and list(key)==rec['key'] and enc(value)==rec['affine'])
            entries[l,m,i,j]=value
            if value is None:free.append((8-i,8-j));free_keys.append(key)
            else:dictionary[key]=value
            records.append({'type':[l,m,i,j],'key':key,'affine':value,'presentations':prs})
    free.sort()
    check('all_500_types_3000_presentations',len(records)==500 and sum(len(r['presentations']) for r in records)==3000)
    check('full_free_partition',free==[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8] and len(set(free_keys))==45 and list(map(list,free))==data['free'])
    for r,q in it.product(range(9),repeat=2):
        if r+q>=8:continue
        expected=av(p[8]) if r+q==0 else av(0) if r+q<=4 else entries[r+q,8,q,r]
        check('every_forced_88_'+str((r,q)),entries[8,8,8-r,8-q]==expected)
    report.update(domain=fs,records=records,weighted_kernel_residuals=residuals)
    save('original_affine_dictionary_checked')
    sizes={l:C(68,l)*C(956,l) for l in [5,6,7,8]}
    modes=[];matrix=[];all_minors=[];ranks=[]
    for a,b in it.product(range(9),repeat=2):
        idx=9*a+b;ls=[l for l in [5,6,7] if l>=max(a,b)]
        def block(l,m):
            ll,mm=sorted([l,m]);v=av(0)
            for i,j in it.product(range(ll+1),repeat=2):
                coef=beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)
                v=[x+coef*y for x,y in zip(v,entries[ll,mm,i,j])]
            if a==b==0:v[0]-=p[l]*p[m]*sizes[l]*sizes[m]
            return v
        B=[[block(l,m)[0] for m in ls] for l in ls];cross=[block(l,8) for l in ls]
        sv=data['modes'][idx]
        check('all_original_base_cross_coefficients_'+str(idx),enc(B)==sv['base'] and enc(cross)==sv['cross'])
        check('reviewed_fixed_base_contract_'+str(idx),enc(B)==audit['modes'][idx]['source_base'])
        for k in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),k):
                v=determinant([[B[i][j] for j in inds] for i in inds]);all_minors.append(v)
                check('all_old_principal_minors_'+str((idx,inds)),v>=0)
        H=[list(reversed(r)) for r in reversed(B)];u=list(reversed(cross));cost=[[Q(0)]*5 for _ in range(5)];stages=[];rank=0
        for k in range(len(H)):
            pivot=H[k][k];check('reverse_pivot_'+str((idx,k)),pivot>=0)
            if not pivot:check('all_affine_zero_pivot_ranges_'+str((idx,k)),not any(H[k][k:]+u[k]))
            else:
                rank+=1
                cost=[[v+u[k][i]*u[k][j]/pivot for j,v in enumerate(r)] for i,r in enumerate(cost)]
                for i in range(k+1,len(H)):
                    u[i]=[x-H[i][k]*y/pivot for x,y in zip(u[i],u[k])]
                    for j in range(k+1,len(H)):H[i][j]-=H[i][k]*H[k][j]/pivot
            stages.append({'pivot':pivot,'matrix':[r[:] for r in H],'cross':[r[:] for r in u]})
        d8=C(68-2*a,8-a)*C(956-2*b,8-b)
        cost=[[v/(p[8]*d8) for v in r] for r in cost]
        check('all_independent_reverse_cost_coefficients_'+str(idx),enc(cost)==sv['cost'])
        inv=[[Q(*v) for v in r] for r in sv['inverse_affine']]
        check('all_5_original_inverse_equations_'+str(idx),all(sum(B[i][j]*inv[j][k] for j in range(len(B)))==cross[i][k] for i in range(len(B)) for k in range(5)))
        forced=av(0)
        for (l,m,i,j),v in entries.items():
            if l==m==8 and v is not None:
                coef=Q(beta(68,8,8,a,i)*beta(956,8,8,b,j),p[8]*d8)
                forced=[x+coef*y for x,y in zip(forced,v)]
        anchor=p[8]*sizes[8] if a==b==0 else Q(0)
        minus=forced[:];minus[0]-=anchor
        check('full_forced_and_anchor_coefficients_'+str(idx),enc(minus)==sv['fixed_minus_anchor'])
        row=[-Q(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),d8*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        check('original_mode_rows_'+str(idx),enc(row)==data['matrix'][idx]==fixed82['matrix'][idx])
        check('positive_normalization_'+str(idx),d8>0 and (C(68,a)-C(68,a-1))*(C(956,b)-C(956,b-1))>0)
        M=[[-v for v in r] for r in cost];M[0][0]+=minus[0]
        for j in range(1,5):M[0][j]+=minus[j]/2;M[j][0]+=minus[j]/2
        check('complete_bound_quadratic_'+str(idx),enc(M)==sv['quadratic'])
        oldpoint=[Q(*v) for v in fixed82['point']]
        am=audit['modes'][idx]
        check('step290_original_fixed_specialization_'+str(idx),
              [dot(r,oldpoint) for r in cross]==[Q(*v) for v in am['source_cross']] and
              dot(oldpoint,[dot(r,oldpoint) for r in cost])==Q(*am['required']) and
              dot(forced,oldpoint)==Q(*am['fixed']) and anchor==Q(*am['anchor']) and
              dot(oldpoint,[dot(r,oldpoint) for r in M])==Q(*audit['rhs'][idx]))
        modes.append({'mode':[a,b],'base':B,'cross':cross,'reverse_stages':stages,'cost':cost,'forced':forced,'anchor':anchor,'quadratic':M,'D8':d8})
        ranks.append([len(ls),rank]);matrix.append(row)
    check('complete_old_minor_count',len(all_minors)==306)
    text=(NB/'lemmas/L082-common-column-joint-completion-obstruction.md').read_text()
    match=re.search(r'I=\((.*?)\),\s*J=\((.*?)\)\.',text,re.S)
    I=list(map(int,re.findall(r'-?\d+',match.group(1))));J=[-1]+list(range(45))
    K=[[Q(-1) if j==-1 else matrix[i][j] for j in J] for i in I]
    local=solve(list(map(list,zip(*K))),[Q(-1)]+[Q(0)]*45);y=[Q(0)]*81
    for i,v in zip(I,local):y[i]=v
    check('canonical_46by46_original_definition',I==data['I'] and J==data['J'] and all(dot(r,local)==v for r,v in zip(zip(*K),[Q(-1)]+[Q(0)]*45)))
    check('unchanged_28_positive_weights',min(y)>=0 and sum(y)==1 and sum(v>0 for v in y)==28 and enc(y)==data['weights']==fixed82['exact']['dual'])
    sums=[sum(y[i]*matrix[i][j] for i in range(81)) for j in range(45)]
    raw=[-sum(y[k]*Q(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),p[8]*modes[k]['D8']) for k,(a,b) in enumerate(it.product(range(9),repeat=2))) for r,q in free]
    check('all_45_scaled_raw_cancellations',sums==raw==[0]*45 and enc(sums)==data['scaled_sums'] and enc(raw)==data['raw_sums'])
    M=[[sum(y[k]*modes[k]['quadratic'][i][j] for k in range(81)) for j in range(5)] for i in range(5)]
    check('entire_pairing_quadratic',enc(M)==data['M'])
    s=-M[0][4]/M[4][4];gamma=-M[4][4]
    e=[-s,Q(0),Q(0),Q(0),Q(1)]
    square=[[-gamma*x*v for v in e] for x in e]
    check('full_exact_negative_square_identity',gamma>0 and M==square and enc(s)==data['square']['stationary_t78'])
    endpoints=[]
    for inds in [[27,33,56,63],[5,26,33,56]]:
        mat=[fs[j][1:] for j in inds];b=[-fs[j][0] for j in inds]
        check('nonsingular_endpoint_recipe_'+str(inds),determinant(mat)!=0)
        z=[Q(1)]+solve(mat,b);signs=[dot(f,z) for f in fs]
        check('all_endpoint_signs_'+str(inds),min(signs)>=0)
        endpoints.append(z)
    z0,z1=endpoints;alpha=(s-z0[4])/(z1[4]-z0[4])
    point=[(1-alpha)*x+alpha*v for x,v in zip(z0,z1)];factors=[dot(f,point) for f in fs]
    check('strict_convex_interpolation',z0[4]<s<z1[4] and 0<alpha<1 and point[4]==s)
    check('same_exact_point_and_factors',enc(point)==data['point'] and enc(alpha)==data['alpha'] and enc(factors)==data['factors'])
    check('all_85_original_domain_rows',min(factors)==0 and [j for j,v in enumerate(factors) if not v]==[33,56] and sum(v>0 for v in factors)==83)
    bounds=[dot(point,[dot(r,point) for r in m['quadratic']]) for m in modes]
    # Separate full forced, anchor, and range contributions at the witness.
    weighted_forced=sum(y[k]*dot(m['forced'],point) for k,m in enumerate(modes))
    weighted_anchor=sum(y[k]*m['anchor'] for k,m in enumerate(modes))
    weighted_cost=sum(y[k]*dot(point,[dot(r,point) for r in m['cost']]) for k,m in enumerate(modes))
    value=dot(y,bounds)
    check('all_81_original_bounds_at_witness',enc(bounds)==data['bounds'])
    check('attained_zero_all_contributions',value==weighted_forced-weighted_anchor-weighted_cost==dot(point,[dot(r,point) for r in M])==0 and data['value']==[0,1])
    report.update(modes=modes,old_minors=all_minors,ranks=ranks,matrix=matrix,weights=y,scaled_sums=sums,raw_sums=raw,M=M,gamma=gamma,stationary_t78=s,
                  endpoints=endpoints,alpha=alpha,point=point,factors=factors,bounds=bounds,weighted_forced=weighted_forced,weighted_anchor=weighted_anchor,weighted_cost=weighted_cost,value=value)
    report['summary']={'verdict':'ATTAINED_ZERO_MAXIMUM' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
                       'actual_pairing':value,'required_nonnegative_pairing':0,'actual_minimum_factor':min(factors),'required_minimum_factor':0,
                       'positive_factors':sum(v>0 for v in factors),'zero_factors':[j for j,v in enumerate(factors) if not v],
                       'types':500,'presentations':3000,'modes':81,'old_principal_minors':len(all_minors),'weighted_kernel_equations':90}
    save('completed');print(enc(report['summary']),flush=True);print('Full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)
if __name__=='__main__':main()
