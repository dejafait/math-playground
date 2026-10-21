"""Dedicated L087 fixed-witness audit. No optimizer or candidate variation.

Rebuild the original recipes, actual-support presentations and direct subset
actions. Check every original/raw remainder and the entire manuscript N/Q.
Only arithmetic helpers are imported; prior constructors are never invoked.
"""
import hashlib
import itertools as it
import json
import re
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from critical_audit_simultaneous_eight_shell import c, beta, dot, enc, solve
from verify_simultaneous_eight_shell import det, cramer

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'affine-sign-remaining-modes-critical-audit.json'


def dec(M):
    return [[F(*v) for v in r] for r in M]


def av(v):
    return [F(v)]+[F(0)]*4


def main():
    names = ['affine-sign-phase-one-results.json',
             'affine-sign-phase-one-critical-audit.json',
             'affine-sign-critical-original-verification.json',
             'affine-sign-critical-ancestor-reconstruction.json',
             'affine-sign-remaining-modes-results.json',
             'affine-sign-remaining-modes-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'simultaneous-eight-shell-critical-audit.json',
             'eight-distance-full-base-kernel-results.json',
             'maximizer-excluded-anchor-results.json',
             'maximizer-completion-results.json', 'delsarte-lp-results.json',
             'seven-distance-full-base-kernel-results.json',
             'alternative-product-zero-plane-results.json',
             'seven-shell-affine-fixed-dual-results.json',
             'simultaneous-shell-ordinary-scalars-results.json']
    paths = [ROOT/n for n in names]
    objects = [json.loads(p.read_text()) for p in paths]
    data, audit, oldver, ancestor, result, ver, src, direct, col, old, inc, lp, seven, plane, square, six = objects
    checks, failures = [], []
    report = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    for name, obj in zip(names, objects):
        check('clean_'+name, not obj['failures'])
        for rel, h in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)

    # Reconstruct original pairs and immutable seven-column/completion recipes.
    primal = [F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    for j in range(1,65):
        row = [F(sum((-1)**h*c(j,h)*c(68-j,i-h)*c(956-j,i-h) for h in range(i+1)),c(68,i)*c(956,i)) for i in range(5,69)]
        check('original_pair_equation_'+str(j), dot(row,primal)==-1)
    p = [F(1)]+[F(0)]*4+[x/(2*c(68,h)*c(956,h)) for h,x in zip(range(5,69),primal)]
    rho = (F(c(1024,64),c(68,64))+1)/(2*c(1024,68))
    p8 = p[8]
    check('rho_pairs_p8', rho>0 and enc(rho)==old['rho'] and enc(p[:15])==old['pairs_through_14']==col['pairs_through_14'] and p8==F(16792471,1181138102168120460))
    sm, pm = dec(square['objective_matrix']), dec(plane['plane_matrix'])
    params = [F(0),-pm[0][2]/pm[2][2],-sm[0][3]/sm[3][3]]
    rr = dec(seven['equation_rref']); f7 = [F(0)]*49
    for j,v in zip([27,33,42],params):
        f7[j]=v
    for k,j in enumerate(seven['equation_pivots']):
        f7[j]=rr[k][-1]-sum(rr[k][t]*f7[t] for t in [27,33,42])
    check('seven_column_recipe', enc(params)==inc['parameters'] and enc(f7)==inc['free_column'])
    for i,(r,b) in enumerate(zip(seven['equations'],seven['rhs'])):
        check('seven_original_equation_'+str(i),dot([F(*v) for v in r],f7)==F(*b))
    entries = {tuple(r['type']):av(F(*r['y'])) for r in six['types']}
    for r in seven['column'][1:]:
        entries[r['orbit'][0],7,*r['orbit'][1:]]=av(p[7]*f7[r['variable']] if r['kind']=='free' else F(*r['value']))
    defining = [0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,24,25,26,27,28,29,32,33,34,35,40,41,42,48,49,56]
    z7,_ = solve([dec(inc['matrix'])[i] for i in defining]+[[F(j==28) for j in range(36)]], [F(*inc['rhs'][i]) for i in defining]+[F(0)])
    check('immutable_completion', enc(z7)==inc['certificate']['z']==direct['completion'] and min(z7)==0)
    free7 = [(r,q) for r,q in it.product(range(8),repeat=2) if r+q>=7]
    for r,q in it.product(range(8),repeat=2):
        h=r+q
        entries[7,7,7-r,7-q] = av(p[7]) if h==0 else av(0) if h<=4 else entries[h,7,q,r] if h<=6 else av(p[7]*z7[free7.index((r,q))]/(c(7,r)*c(61,r)*c(7,q)*c(949,q)))
    check('entire_old_dictionary', entries=={tuple(r['type']):av(F(*r['y'])) for r in old['entries']} and len(entries)==270)

    w = [F(*v) for v in data['witness']['original']]
    raw = [F(*v) for v in data['witness']['raw_moments']]
    point = w[:4]+[F(*src['stationary_t78'])]
    check('immutable_full_point', len(w)==49 and w[0]==1 and enc(w)==audit['original_point']==oldver['original_point']==result['original_witness'] and enc(point)==result['point'])
    check('immutable_raw_point', enc(w[:4]+raw)==audit['raw_point']==oldver['raw_point'] and enc(raw)==result['raw_moments'])
    free = [(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    volumes = [c(8,r)*c(60,r)*c(8,q)*c(948,q) for r,q in free]
    check('positive_raw_scales_and_signs', p8>0 and min(volumes)>0 and raw==[p8*z/v for z,v in zip(w[4:],volumes)] and min(raw)>=0 and min(w[4:])>=0)
    rr = dec(col['equation_rref']); nonpiv=[56,63,69,78]
    family = [[F(0)]*5 for _ in range(85)]
    for k,j in enumerate(nonpiv):family[j][k+1]=F(1)
    for i,j in enumerate(col['equation_pivots']):family[j]=[rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    check('original_RREF_family', len(col['equation_pivots'])==81 and enc(family)==src['family']==ancestor['family'])
    factors = [dot(r,point) for r in family]
    check('all_85_domain_rows', enc(factors)==data['witness']['domain_values']==oldver['domain_values']==result['domain_factors'] and min(factors)==0 and [i for i,v in enumerate(factors) if v==0]==[26,27,56])
    column=[av(p8)]
    for r in col['column'][1:]:
        v=[p8*x for x in family[r['variable']]] if r['kind']=='free' else av(F(*r['value']))
        column.append(v);entries[r['orbit'][0],8,*r['orbit'][1:]]=v
    weights=[1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in col['orbits'][1:]]
    kernel=[]
    check('full_column_kernel_dimensions',len(column)==len(weights)==150 and len(col['kernel_basis'])==len(col['equations'])==90)
    for i,(kr,eq,rhs) in enumerate(zip(col['kernel_basis'],col['equations'],col['rhs'])):
        residual=[sum(F(*v)*W*f[k] for v,W,f in zip(kr,weights,column)) for k in range(5)]
        check('kernel_and_original_affine_row_'+str(i),residual==[0]*5 and [sum(F(*v)*f[k] for v,f in zip(eq,family)) for k in range(5)]==av(F(*rhs)))
        kernel.append(residual)
    check('full_ancestral_arrays',enc(column)==src['affine_column'] and enc(kernel)==src['weighted_kernel_residuals']==ancestor['weighted_kernel_residuals']==result['kernel_residuals'])

    # Point-by-point actual supports, independently of the bit-permutation code.
    records=[]; key_values={}
    types=[(l,m,i,j) for l,m in it.combinations_with_replacement([5,6,7,8],2) for i,j in it.product(range(l+1),repeat=2)]
    for idx,typ in enumerate(types):
        l,m,i,j=typ;counts=[956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        sets=[set(),set(),set()];start=0
        for mask,n in enumerate(counts):
            for s,bit in zip(sets,[4,2,1]):
                if mask&bit:s.update(range(start,start+n))
            start+=n
        check('actual_supports_'+str(idx),start==1024 and min(counts)>=0 and all(len(s)==68 for s in sets))
        prs=[];values=[]
        for A,B,G in it.permutations(sets):
            atoms=[0]*8
            for x in range(1024):atoms[4*(x in A)+2*(x in B)+(x in G)]+=1
            ds=[len(A-B),len(A-G),len(B-G)]
            v=av(p[max(ds)]) if 0 in ds else av(0) if any(0<h<5 for h in ds) else entries.get((*sorted(ds[:2]),len((A-B)&(A-G)),len((B-A)&(G-A))))
            prs.append({'atoms':atoms,'distances':ds,'affine':v})
            if v is not None:values.append(v)
        key=tuple(min(r['atoms'] for r in prs));value=values[0] if values else None
        check('all_six_presentations_'+str(idx),enc(prs)==result['records'][idx]['presentations'] and list(key)==result['records'][idx]['key']==src['records'][idx]['key'] and enc(value)==src['records'][idx]['affine'] and all(v==value for v in values) and (key not in key_values or key_values[key]==value))
        entries[typ]=value;key_values[key]=value
        records.append({'type':typ,'key':key,'presentations':prs,'affine':value})
    check('entire_type_records',len(records)==500 and enc(records)==result['records'])
    check('36_forced_45_free_keys',sum(v is None for v in entries.values())==45 and len({tuple(records[-81+9*(8-r)+(8-q)]['key']) for r,q in free})==45)
    for r,q in it.product(range(9),repeat=2):
        h=r+q;v=entries[8,8,8-r,8-q]
        check('forced_partition_'+str((r,q)),(v is None) if h>=8 else v==(av(p8) if h==0 else av(0) if h<=4 else entries[h,8,q,r]))
    report.update(original_point=w,point=point,raw_moments=raw,family=family,domain_factors=factors,records=records,kernel_residuals=kernel,original_seven_column=f7,completion=z7)
    save('original_recipes_and_fixed_witness_checked')
    print('Original recipes, full point, 500 types/3000 presentations and 90 kernel equations checked; failures:',failures,flush=True)

    # Generate monic orthogonal bases afresh; consume all 220 direct transitions.
    bases={};norms={};gamma={};ratios={};factor_records=[];transition_records=[]
    for n,l in it.product([68,956],[5,6,7,8]):
        W=[c(8,i)*c(n-8,l-i) for i in range(l+1)];hs=[];ns=[]
        for a in range(l+1):
            v=[F(i**a) for i in range(l+1)]
            for h,norm in zip(hs,ns):
                coeff=dot(W,[x*y for x,y in zip(v,h)])/norm
                v=[x-coeff*y for x,y in zip(v,h)]
            norm=dot(W,[x*x for x in v]);hs.append(v);ns.append(norm)
            check('positive_orthogonal_norm_'+str((n,l,a)),norm>0 and all(dot(W,[x*i**k for i,x in enumerate(v)])==0 for k in range(a)))
        saved=next(r for r in direct['factors'] if r['n']==n and r['layer']==l)
        check('independent_basis_'+str((n,l)),enc(hs)==saved['basis'] and enc(ns)==saved['norms'])
        bases[n,l]=hs;norms[n,l]=ns;factor_records.append({'n':n,'layer':l,'basis':hs,'norms':ns})
    expected_transitions={(n,l,m,k) for n in [68,956] for l,m in it.product([5,6,7,8],repeat=2) for k in range(min(l,m)+1)}
    check('complete_220_transitions',len(direct['transitions'])==220 and {tuple(r['indices']) for r in direct['transitions']}==expected_transitions)
    for tr in direct['transitions']:
        n,l,m,k=tr['indices']
        T=[[sum(c(i,h)*c(8-i,j-h)*c(l-i,k-h)*c(n-8-l+i,m-j-k+h) for h in range(9)) for j in range(m+1)] for i in range(l+1)]
        check('transition_'+str((n,l,m,k)),T==tr['matrix'] and all(sum(row)==c(l,k)*c(n-l,m-k) for row in T))
        actions=[]
        for a in range(m+1):
            v=[dot(row,bases[n,m][a]) for row in T]
            saved=next(r for r in tr['actions'] if r['degree']==a)
            check('full_action_'+str((n,l,m,k,a)),enc(v)==saved['action'])
            if a>l:
                check('absent_mode_'+str((n,l,m,k,a)),not any(v));continue
            index=next(i for i,x in enumerate(bases[n,l][a]) if x)
            g=v[index]/bases[n,l][a][index];gamma[n,l,m,a,k]=g
            check('scalar_action_'+str((n,l,m,k,a)),v==[g*x for x in bases[n,l][a]] and enc(g)==saved['coefficient'])
            be=beta(n,l,m,a,k)
            if be:
                ratio=norms[n,l][a]*g/be
                check('signed_beta_ratio_'+str((n,l,m,k,a)),ratio>0 and ratios.setdefault((n,l,m,a),ratio)==ratio)
            else:check('zero_beta_action_'+str((n,l,m,k,a)),g==0)
            actions.append({'degree':a,'coefficient':g,'action':v})
        transition_records.append({'indices':tr['indices'],'matrix':T,'actions':actions})
    for n in [68,956]:
        for a in range(9):
            check('reference_norm_'+str((n,a)),ratios[n,8,8,a]==norms[n,8][a]/c(n-2*a,8-a))
            for l,m in it.product([l for l in [5,6,7,8] if l>=a],repeat=2):
                check('coherent_congruence_'+str((n,l,m,a)),ratios[n,l,m,a]*ratios[n,8,8,a]==ratios[n,l,8,a]*ratios[n,m,8,a])
    report.update(factors=factor_records,transitions=transition_records)
    save('independent_subset_normalization_checked')
    print('Independent orthogonal bases and all 220 two-direction subset transitions checked; failures:',failures,flush=True)

    sizes={l:c(68,l)*c(956,l) for l in [5,6,7,8]};rows=[]
    selected=[9*a+b for a in range(7) for b in range(4)]
    check('partition_28_53',selected==data['selected_modes']==result['selected_modes'] and result['remaining_modes']==[i for i in range(81) if i not in selected] and len(result['rows'])==len(ver['rows'])==81)
    for idx in range(81):
        a,b=divmod(idx,9);ls=[l for l in [5,6,7] if l>=max(a,b)]
        D=F(c(68-2*a,8-a)*c(956-2*b,8-b));N=norms[68,8][a]*norms[956,8][b];norm=p8*D
        scales={l:ratios[68,l,8,a]*ratios[956,l,8,b]/(N/D) for l in ls+[8]}
        def source(l,m):
            ll,mm=sorted([l,m])
            v=[sum(beta(68,l,m,a,i)*beta(956,l,m,b,j)*entries[ll,mm,i,j][k] for i,j in it.product(range(ll+1),repeat=2)) for k in range(5)]
            if idx==0:v[0]-=p[l]*p[m]*sizes[l]*sizes[m]
            return v
        def weighted(l,m):
            ll,mm=sorted([l,m])
            value=sum(gamma[68,l,m,a,i]*gamma[956,l,m,b,j]*dot(entries[ll,mm,i,j],point) for i,j in it.product(range(ll+1),repeat=2))
            if idx==0:value-=p[l]*p[m]*sizes[m]
            return value*norms[68,l][a]*norms[956,l][b]
        B=[[source(l,m)[0] for m in ls] for l in ls];cross=[source(l,8) for l in ls];cv=[dot(v,point) for v in cross]
        saved=result['rows'][idx];ancestor_mode=src['modes'][idx]
        check('original_source_arrays_'+str(idx),enc(B)==saved['base']==ancestor_mode['source_base'] and enc(cross)==ancestor_mode['source_cross'] and enc(cv)==saved['cross'] and all(not any(source(l,m)[1:]) for l,m in it.product(ls,repeat=2)))
        inv=dec(ancestor_mode['inverse_affine'])
        residuals=[[sum(B[i][j]*inv[j][k] for j in range(len(ls)))-cross[i][k] for k in range(5)] for i in range(len(ls))]
        check('all_affine_source_ranges_'+str(idx),all(not any(r) for r in residuals) and enc(residuals)==saved['affine_inverse_residuals'])
        minors=[];chosen=()
        for size in range(1,len(ls)+1):
            for inds in it.combinations(range(len(ls)),size):
                value=det([[B[i][j] for j in inds] for i in inds]);minors.append({'indices':inds,'determinant':value})
                if value:chosen=inds
        check('old_minors_'+str(idx),all(r['determinant']>=0 for r in minors) and enc(minors)==saved['minors'])
        x=[F(0)]*len(ls)
        if chosen:
            vals=cramer([[B[i][j] for j in chosen] for i in chosen],[cv[i] for i in chosen])
            for j,v in zip(chosen,vals):x[j]=v
        check('fresh_Cramer_all_rows_'+str(idx),[dot(row,x)-v for row,v in zip(B,cv)]==[0]*len(ls) and enc(x)==saved['fresh_inverse'])
        cost=dot(cv,x)
        check('inverse_cost_'+str(idx),cost==dot(cv,[dot(r,point) for r in inv]) and enc(cost)==saved['energy'])
        WB=[[weighted(l,m) for m in ls] for l in ls];wc=[weighted(l,8) for l in ls]
        check('coherent_weighted_entries_'+str(idx),all(WB[i][j]==(N/D)*scales[l]*scales[m]*B[i][j] for i,l in enumerate(ls) for j,m in enumerate(ls)) and all(wc[i]==weighted(8,l)==(N/D)*scales[l]*cv[i] for i,l in enumerate(ls)) and all(v>0 for v in scales.values()) and scales[8]==1)
        H=[list(reversed(r)) for r in reversed(WB)];v=list(reversed(wc));energy=F(0);stages=[];rank=0
        for k in range(len(H)):
            pivot=H[k][k]
            check('weighted_pivot_'+str((idx,k)),pivot>=0)
            if pivot==0:check('weighted_singular_row_cross_'+str((idx,k)),not any(H[k][k:]+[v[k]]))
            elif pivot>0:
                rank+=1;energy+=v[k]*v[k]/pivot
                for i in range(k+1,len(H)):
                    v[i]-=H[i][k]*v[k]/pivot
                    for j in range(k+1,len(H)):H[i][j]-=H[i][k]*H[k][j]/pivot
            stages.append({'pivot':pivot,'matrix':[r[:] for r in H],'cross':v[:]})
        check('independent_weighted_energy_'+str(idx),energy/(p8*N)==cost/norm)
        forced=[sum(beta(68,8,8,a,i)*beta(956,8,8,b,j)*value[k] for (l,m,i,j),value in entries.items() if l==m==8 and value is not None) for k in range(5)]
        anchor=p8*p8*sizes[8]*sizes[8] if idx==0 else F(0)
        coeff=[F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        A=[-v/(D*V) for v,V in zip(coeff,volumes)]
        bound=(dot(forced,point)-anchor-cost)/norm
        slack=bound-dot(A,w[4:]);raw_value=dot(forced,point)+dot(coeff,raw)-anchor-cost
        diagonal=sum(gamma[68,8,8,a,i]*gamma[956,8,8,b,j]*dot(value,point) for (l,m,i,j),value in entries.items() if l==m==8 and value is not None)
        diagonal+=sum(gamma[68,8,8,a,8-r]*gamma[956,8,8,b,8-q]*Y for (r,q),Y in zip(free,raw))
        if idx==0:diagonal-=p8*p8*sizes[8]
        weighted_slack=(diagonal*N-energy)/(p8*N)
        check('every_original_coefficient_'+str(idx),enc(A)==saved['original_row']==ancestor_mode['row'] and enc(coeff)==saved['raw_beta'] and enc(forced)==saved['forced_raw'])
        check('full_anchor_and_bound_'+str(idx),enc(anchor)==saved['raw_anchor'] and enc(anchor/norm)==saved['anchor']==ancestor_mode['anchor'] and enc(bound)==saved['bound'] and enc(dot(forced,point)/norm)==saved['forced'] and bound==dot(point,[dot(r,point) for r in dec(ancestor_mode['quadratic'])]))
        check('all_original_raw_weighted_remainders_'+str(idx),norm>0 and raw_value==norm*slack and weighted_slack==slack and enc(slack)==saved['scaled_slack']==ver['rows'][idx]['scaled_slack'] and enc(raw_value)==saved['raw_Schur_remainder']==ver['rows'][idx]['raw_remainder'])
        if idx in selected:check('selected_equality_'+str(idx),slack==raw_value==0)
        multiplicity=(c(68,a)-c(68,a-1))*(c(956,b)-c(956,b-1))
        check('positive_multiplicity_'+str(idx),multiplicity>0)
        rows.append({'index':idx,'mode':[a,b],'layers':ls,'rank':rank,'base':B,'cross':cv,'inverse':x,'affine_range_residuals':residuals,'minors':minors,'weighted_base':WB,'weighted_cross':wc,'weighted_stages':stages,'energy':cost,'weighted_energy':energy,'norm':norm,'multiplicity':multiplicity,'raw_beta':coeff,'original_row':A,'forced_raw':forced,'raw_anchor':anchor,'bound':bound,'scaled_slack':slack,'raw_remainder':raw_value,'weighted_slack':weighted_slack})
    for l in [5,6,7,8]:check('full_layer_dimension_'+str(l),sum(r['multiplicity'] for r in rows if max(r['mode'])<=l)==sizes[l])
    negative=[r['index'] for r in rows if r['scaled_slack']<0]
    positive=[r['index'] for r in rows if r['scaled_slack']>0]
    zeros=[r['index'] for r in rows if r['scaled_slack']==0]
    expected=[4,6,8,14,16,23,24,32,33,41,50,58,60,64,67,68,73,75,77]
    check('complete_sign_partition',negative==expected==result['negative_indices']==ver['negative_indices'] and len(positive)==34 and zeros==selected)
    manuscript=(NB/'lemmas/L087-audited-sign-equality-witness-fails-remaining-modes.md').read_text()
    Ntext=int(re.search(r'^N=(-?\d+)$',manuscript,re.M)[1]);Qtext=int(re.search(r'^Q=(\d+)$',manuscript,re.M)[1])
    value=rows[8]['scaled_slack'];raw_value=rows[8]['raw_remainder']
    # Independent diagonal eigenvalue formula, using only the 81 actual moments.
    def eigen(n,a,r):return sum((-1)**h*c(a,h)*c(8-a,r-h)*c(n-8-a,r-h) for h in range(r+1))
    terms=[]
    for r,q in it.product(range(9),repeat=2):
        v=entries[8,8,8-r,8-q]
        Y=dot(v,point) if v is not None else raw[free.index((r,q))]
        terms.append(eigen(68,0,r)*eigen(956,8,q)*Y/p8)
    check('complete_manuscript_rational',Ntext==value.numerator and Qtext==value.denominator and Ntext<0 and Qtext>0)
    check('independent_81_term_negative_sum',sum(terms,F(0))==value and rows[8]['layers']==[] and rows[8]['raw_anchor']==rows[8]['energy']==0 and rows[8]['norm']==F(46806225362314,445376358283605) and raw_value==rows[8]['norm']*value<0)
    check('manuscript_interval_exact',F(-6896215747443,10**12)<=value<F(-6896215747442,10**12)<0)
    worst=min(range(81),key=lambda i:rows[i]['scaled_slack'])
    check('manuscript_worst',worst==73 and F(-7561447077392486,10**6)<=rows[worst]['scaled_slack']<F(-7561447077392485,10**6))
    ranks=Counter((len(r['layers']),r['rank']) for r in rows)
    check('all_old_case_counts',Counter(len(r['layers']) for r in rows)=={3:36,2:13,1:15,0:17} and sum(len(r['minors']) for r in rows)==306)
    report.update(rows=rows,negative_indices=negative,positive_indices=positive,zero_indices=zeros,new_only_0_8_terms=terms,manuscript_rational=[Ntext,Qtext])
    report['summary']={'verdict':'RETAINED_FIXED_WITNESS_REJECTION' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'original_raw_weighted_identities':81,'remaining_negative':len(negative),'remaining_positive':len(positive),'selected_zero':len(zeros),'rank_cases':{str(k):v for k,v in sorted(ranks.items())},'old_minors':306,'actual_0_8_scaled_interval':[-6896215747443,-6896215747442,10**12],'required_minimum':0,'complete_manuscript_rational_checked':True,'ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS','rs_boundary':[955,957]}
    save('completed')
    print('Verdict:',report['summary']['verdict'],'; checks:',len(checks),'; failures:',failures,flush=True)
    print('Actual (0,8) scaled slack in [-6896215747443,-6896215747442)/10^12; required >= 0. Complete original/raw/weighted values:',str(OUT.relative_to(NB))+' /rows/8',flush=True)
    print('81 identities; 19 negative, 34 positive, 28 zero. Full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)


if __name__=='__main__':
    main()
