"""Dedicated L085 audit: original affine blocks and two invertible pullbacks.

No constructor, optimizer, parameter scan or new weights. Full rational
certificates are consumed; upstream decomposition contracts stay qualified.
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

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-plane-fixed-face-critical-audit.json'


def dec(M):
    return [[F(*v) for v in row] for row in M]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(M):
    return list(map(list, zip(*M))) if M else []


def mul(A, B):
    assert not A or len(A[0]) == len(B)
    return [[dot(row, col) for col in zip(*B)] for row in A]


def inverse(M):
    n = len(M)
    if not n:
        return []
    return tr([solve(M, col)[0] for col in eye(n)])


def coefficient(B, cross, bottom, j):
    n = len(B)
    P = [[F(0)]*(n+1) for _ in range(n+1)]
    if j == 0:
        for i in range(n):
            P[i][:n] = B[i][:]
    if j < 4:
        for i in range(n):
            P[i][n] = P[n][i] = cross[i][j]
    P[n][n] = bottom[j]
    return P


def av(v):
    return [F(v)] + [F(0)]*4


def main():
    names = ['zero-plane-fixed-face-results.json', 'zero-plane-fixed-face-verification.json',
             'zero-plane-joint-feasibility-results.json', 'zero-plane-joint-feasibility-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'fully-cancelling-separator-family-results.json', 'fully-cancelling-separator-family-verification.json',
             'zero-plane-positive-mode-compatibility-results.json', 'zero-plane-positive-mode-compatibility-verification.json',
             'eight-common-column-joint-completion-critical-audit.json',
             'eight-distance-full-base-kernel-results.json', 'maximizer-excluded-anchor-results.json',
             'maximizer-completion-results.json', 'delsarte-lp-results.json',
             'seven-distance-full-base-kernel-results.json', 'alternative-product-zero-plane-results.json',
             'seven-shell-affine-fixed-dual-results.json']
    paths = [ROOT/n for n in names]
    face, fv, old, ov, src, res, ver, eq, ev, a82, col, base, inc, lp, seven, plane, square = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)
    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    for name, data in zip(names, [face,fv,old,ov,src,res,ver,eq,ev,a82,col,base,inc,lp,seven,plane,square]):
        check('clean_'+name, not data['failures'])
        for rel,h in data.get('input_hashes',{}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)

    primal=[F(v['numerator'],v['denominator']) for v in lp['exact']['primal']]
    pairs=[F(1)]+[F(0)]*4+[x/(2*c(68,h)*c(956,h)) for h,x in zip(range(5,69),primal)]
    p8=pairs[8]
    rho=(F(c(1024,64),c(68,64))+1)/(2*c(1024,68))
    check('original_pairs_rho_p8', p8==F(16792471,1181138102168120460) and rho>0 and enc(rho)==base['rho'] and enc(pairs[:15])==base['pairs_through_14']==col['pairs_through_14'])
    # Reconstruct the old seven-column and completion, without re-auditing
    # their uniqueness or all source PSD proofs.
    sm,pm=dec(square['objective_matrix']),dec(plane['plane_matrix'])
    params=[F(0),-pm[0][2]/pm[2][2],-sm[0][3]/sm[3][3]]
    rr=dec(seven['equation_rref']); f7=[F(0)]*49
    for j,v in zip([27,33,42],params): f7[j]=v
    for k,j in enumerate(seven['equation_pivots']):
        f7[j]=rr[k][-1]-sum(rr[k][t]*f7[t] for t in [27,33,42])
    check('seven_original_RREF_column', enc(params)==inc['parameters'] and enc(f7)==inc['free_column']==src['original_seven_column'])
    defining=[0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,24,25,26,27,28,29,32,33,34,35,40,41,42,48,49,56]
    z7,piv7=solve([dec(inc['matrix'])[i] for i in defining]+[[F(j==28) for j in range(36)]], [F(*inc['rhs'][i]) for i in defining]+[F(0)])
    check('seven_completion_definition', enc(z7)==inc['certificate']['z']==src['completion'])
    entries={tuple(r['type']):av(F(*r['y'])) for r in base['entries']}
    for r in seven['column'][1:]:
        v=pairs[7]*f7[r['variable']] if r['kind']=='free' else F(*r['value'])
        check('old_seven_lookup_'+str(r['orbit']), entries[r['orbit'][0],7,*r['orbit'][1:]]==av(v))
    free7=[(r,q) for r,q in it.product(range(8),repeat=2) if r+q>=7]
    for j,(r,q) in enumerate(free7):
        check('old_completion_lookup_'+str(j), entries[7,7,7-r,7-q]==av(pairs[7]*z7[j]/(c(7,r)*c(61,r)*c(7,q)*c(949,q))))
    rr=dec(col['equation_rref']); nonpiv=[56,63,69,78]
    family=[[F(0)]*5 for _ in range(85)]
    for j,k in enumerate(nonpiv): family[k][j+1]=F(1)
    for i,j in enumerate(col['equation_pivots']): family[j]=[rr[i][-1]]+[-rr[i][k] for k in nonpiv]
    check('complete_original_family', enc(family)==src['family']==res['domain']==ver['domain']==a82['family'])
    column=[av(p8)]
    for r in col['column'][1:]:
        v=[p8*x for x in family[r['variable']]] if r['kind']=='free' else av(F(*r['value']))
        column.append(v); entries[r['orbit'][0],8,*r['orbit'][1:]]=v
    W=[1]+[c(8,i)*c(60,l-i)*c(8,j)*c(948,l-j) for l,i,j in col['orbits'][1:]]
    residuals=[]
    check('kernel_dimensions',len(col['kernel_basis'])==len(col['equations'])==90 and len(column)==len(W)==150)
    for i,(kr,row,rhs) in enumerate(zip(col['kernel_basis'],col['equations'],col['rhs'])):
        r=[sum(F(*v)*w*f[j] for v,w,f in zip(kr,W,column)) for j in range(5)]
        check('weighted_kernel_'+str(i),r==[F(0)]*5)
        check('original_equation_'+str(i),[sum(F(*v)*f[j] for v,f in zip(row,family)) for j in range(5)]==av(F(*rhs)))
        residuals.append(r)
    check('complete_column_residual_arrays',enc(column)==src['affine_column']==res['affine_column'] and enc(residuals)==src['weighted_kernel_residuals']==res['weighted_kernel_residuals']==ver['weighted_kernel_residuals'])
    # Reconstruct every full key and ordered presentation via bit-permuted atoms.
    types=[(l,m,i,j) for l,m in it.combinations_with_replacement([5,6,7,8],2) for i,j in it.product(range(l+1),repeat=2)]
    check('all_records_present',len(types)==len(src['records'])==len(ver['records'])==len(a82['records'])==500)
    for k,typ in enumerate(types):
        l,m,i,j=typ; atoms=[956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i]
        prs=[]; values=[]
        for order in it.permutations([2,1,0]):
            aa=[0]*8
            for mask,n in enumerate(atoms):
                dest=sum(((mask>>bit)&1)<<(2-h) for h,bit in enumerate(order))
                aa[dest]=n
            ds=[aa[4]+aa[5],aa[4]+aa[6],aa[2]+aa[6]]
            value=None
            if 0 in ds: value=av(pairs[max(ds)])
            elif any(0<h<5 for h in ds): value=av(0)
            else: value=entries.get((*sorted(ds[:2]),aa[4],aa[3]))
            if value is not None: values.append(value)
            prs.append({'atoms':aa,'distances':ds,'affine':value})
        value=values[0] if values else None
        key=min(v['atoms'] for v in prs)
        check('complete_presentation_'+str(k),all(v==value for v in values) and enc(prs)==ver['records'][k]['presentations'] and key==src['records'][k]['key']==a82['records'][k]['key'])
        check('complete_affine_value_'+str(k),enc(value)==src['records'][k]['affine']==ver['records'][k]['affine']==a82['records'][k]['affine'] and list(typ)==src['records'][k]['type'])
        entries[typ]=value
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    check('36_forced_45_free',sum(v is None for v in entries.values())==45 and all((entries[8,8,8-r,8-q] is None)==(r+q>=8) for r,q in it.product(range(9),repeat=2)) and list(map(list,free))==face['free']==old['free']==res['free'])
    A=[]; original=[]
    sizes={l:c(68,l)*c(956,l) for l in [5,6,7,8]}
    for idx in range(81):
        a,b=divmod(idx,9); ls=[l for l in [5,6,7] if l>=max(a,b)]
        D=c(68-2*a,8-a)*c(956-2*b,8-b); norm=p8*D
        def source(l,m):
            ll,mm=sorted([l,m])
            v=[sum(beta(68,ll,mm,a,i)*beta(956,ll,mm,b,j)*entries[ll,mm,i,j][k] for i,j in it.product(range(ll+1),repeat=2)) for k in range(5)]
            if idx==0: v[0]-=pairs[l]*pairs[m]*sizes[l]*sizes[m]
            return v
        B=[[source(l,m)[0] for m in ls] for l in ls]
        cross=[source(l,8) for l in ls]
        forced=[sum(F(beta(68,8,8,a,i)*beta(956,8,8,b,j),norm)*v[k] for (l,m,i,j),v in entries.items() if l==m==8 and v is not None) for k in range(5)]
        anchor=p8*sizes[8] if idx==0 else F(0)
        row=[-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D*c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
        check('fresh_original_source_'+str(idx),enc(B)==src['modes'][idx]['source_base']==res['modes'][idx]['base']==ver['modes'][idx]['base'] and enc(cross)==src['modes'][idx]['source_cross']==res['modes'][idx]['cross']==ver['modes'][idx]['cross'])
        check('both_rectangular_directions_'+str(idx),all(source(l,8)==source(8,l) for l in ls))
        check('forced_full_anchor_'+str(idx),enc(forced)==src['modes'][idx]['forced']==ver['modes'][idx]['forced'] and enc(anchor)==src['modes'][idx]['anchor']==ver['modes'][idx]['anchor'])
        check('all_original_moment_coefficients_'+str(idx),enc(row)==src['modes'][idx]['row']==old['matrix'][idx]==eq['full_matrix'][idx]==a82['matrix'][idx])
        inv=dec(src['modes'][idx]['inverse_affine'])
        check('full_affine_range_'+str(idx),mul(B,inv)==cross if B else not cross)
        A.append(row);original.append((norm,B,cross,forced,anchor))
    manuscript=(NB/'lemmas/L082-common-column-joint-completion-obstruction.md').read_text()
    part=manuscript.split('**Canonical exact separator.**')[1].split('Let K_')[0]
    I=[int(v) for v in re.search(r'I=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    K=[[-F(1) for i in I]]+[[A[i][j] for i in I] for j in range(45)]
    yy,piv=solve(K,[-F(1)]+[F(0)]*45); y=[F(0)]*81
    for i,v in zip(I,yy):y[i]=v
    check('canonical_weights',len(piv)==46 and all(piv) and min(y)==0 and sum(y)==1 and enc(y)==face['weights']==src['dual']==eq['weights']==res['weights']==ver['weights']==a82['dual'])
    selected=[i for i,v in enumerate(y) if v>0]
    check('exact_positive_support',selected==[9*a+b for a in range(7) for b in range(4)]==face['selected_modes']==eq['selected_modes'])
    Q=dec(src['M']);s=-Q[0][4]/Q[4][4]
    check('exact_plane',Q[4][4]<0 and enc(s)==face['stationary_t78']==old['stationary_t78']==eq['stationary_t78']==ver['stationary_t78'])
    domain=[[f[0]+s*f[4]]+f[1:4] for f in family]
    check('all_85_original_domain_rows',len(domain)==85 and enc(domain)==face['domain']==old['domain']==eq['domain']==ev['domain'])
    report.update(family=family,domain=domain,weighted_kernel_residuals=residuals,weights=y,weight_pivots=piv,stationary_t78=s)
    save('original_affine_system_reconstructed')
    print('Original system reconstructed: 500 types / 3000 presentations, 81 blocks, 90 kernel rows; failures:',failures,flush=True)
    totals=[F(0)]*49; rawtotals=[F(0)]*45; records=[]; retained=[]; reduced=[]; cases=Counter()
    check('81_complete_blocks',len(face['blocks'])==len(old['blocks'])==81)
    for idx,(norm,SB,SC,forced,anchor) in enumerate(original):
        B=[[v/norm for v in row] for row in SB]; cross=[[v/norm for v in row] for row in SC]
        cp=[[r[0]+s*r[4]]+r[1:4] for r in cross]
        ff=forced[:];ff[0]-=anchor
        bottom=[ff[0]+s*ff[4]]+ff[1:4]+[-v for v in A[idx]]
        saved=old['blocks'][idx]; target=face['blocks'][idx]
        check('normalized_original_pencil_'+str(idx),norm>0 and enc(norm)==saved['positive_original_norm'] and enc(B)==saved['original_base'] and enc(cp)==saved['original_cross_plane'] and enc(bottom[:4])==saved['fixed_plane'])
        T=dec(saved['congruence']);Ti=inverse(T)
        R=mul(mul(T,B),tr(T)); tc=mul(T,cp) if B else []
        check('invertible_old_congruence_'+str(idx),mul(T,Ti)==mul(Ti,T)==eye(len(B)) and enc(R)==saved['diagonalized_base'] and enc(tc)==saved['transformed_cross_plane'])
        check('all_fixed_pivots_'+str(idx),all(R[i][i]>=0 and all(R[i][j]==0 for j in range(len(R)) if i!=j) for i in range(len(R))))
        active=[i for i in range(len(B)) if R[i][i]>0]; r=len(active)
        check('complete_discarded_zero_rows_'+str(idx),all(not any(R[i]) and not any(tc[i]) for i in range(len(B)) if i not in active))
        d=[R[i][i] for i in active]; h=[tc[i] for i in active]
        check('all_retained_coordinates_'+str(idx),active==saved['retained_indices'] and enc(d)==saved['positive_diagonal'] and enc(h)==saved['cross_plane'])
        D=[[d[i] if i==j else F(0) for j in range(r)] for i in range(r)]
        lift=[[Ti[i][j] for j in active]+[F(0)] for i in range(len(B))]+[[F(0)]*r+[F(1)]]
        extract=[[T[i][j] for j in range(len(B))]+[F(0)] for i in active]+[[F(0)]*len(B)+[F(1)]]
        check('old_left_inverse_'+str(idx),mul(extract,lift)==eye(r+1))
        P=[coefficient(B,cp,bottom,j) for j in range(49)]
        M=[coefficient(D,h,bottom,j) for j in range(49)]
        for j in range(49):
            check('old_two_way_coefficient_'+str((idx,j)),mul(mul(lift,M[j]),tr(lift))==P[j] and mul(mul(extract,P[j]),tr(extract))==M[j])
        retained.append(r+1);reduced.append(r if idx in selected else r+1)
        cases[(len(B),r,idx in selected)]+=1
        if idx not in selected:
            check('untouched_block_'+str(idx),target['mode']==idx and F(*target['weight'])==0 and dec(target['kernel_basis'])==eye(r+1) and target['face_equations']==[])
            records.append({'mode':idx,'original_base':B,'original_cross_plane':cp,'bottom_coefficients':bottom,'old_inverse':Ti,'lift':lift,'extract':extract,'selected':False})
            continue
        check('whole_plane_constancy_'+str(idx),all(not any(row[1:]) for row in h) and all(not any(row[1:]) for row in cp))
        x=[row[0]/v for row,v in zip(h,d)];v=[-t for t in x]+[F(1)]
        U=eye(r)+[x[:]];H=[row+[v[i]] for i,row in enumerate(U)];Hi=inverse(H)
        original_v=[dot(row,v) for row in tr(extract)]
        check('all_fixed_multiplier_and_basis_values_'+str(idx),enc(v)==target['multiplier_vector']==target['complement_vector'] and enc(original_v)==target['original_multiplier_vector'] and enc(U)==target['kernel_basis'] and enc(Hi)==target['basis_inverse'] and enc(d)==target['positive_base_diagonal'] and enc([row[0] for row in h])==target['constant_cross'] and F(*target['weight'])==y[idx])
        S=[[y[idx]*a*b for b in v] for a in v]
        check('nontrivial_PSD_full_kernel_'+str(idx),y[idx]>0 and v[-1]==1 and dot(v,v)>0 and all(dot(v,col)==0 for col in zip(*U)) and mul(H,Hi)==mul(Hi,H)==eye(r+1) and mul(S,U)==[[F(0)]*r for _ in range(r+1)])
        slack=bottom[:];slack[0]-=sum(d0*t*t for d0,t in zip(d,x))
        traces=[]; transformed=[]; face_equations=[]; compressed=[]
        for j in range(49):
            G=mul(mul(tr(H),M[j]),H)
            q=[row[:r] for row in G[:r]]; mixed=[row[-1] for row in G[:r]]; rem=G[-1][-1]
            val=dot(original_v,[dot(row,original_v) for row in P[j]])
            # Also undo the positive normalization n_i explicitly.
            rawP=[[norm*z for z in row] for row in P[j]]
            unnorm=dot(original_v,[dot(row,original_v) for row in rawP])/norm
            check('all_trace_transports_'+str((idx,j)),val==unnorm==dot(v,[dot(row,v) for row in M[j]])==slack[j])
            check('all_mixed_removed_equations_'+str((idx,j)),mixed==[t*slack[j] for t in x] and rem==slack[j] and [row[-1] for row in G[:r]]==G[-1][:r])
            check('all_inverse_face_pullbacks_'+str((idx,j)),mul(mul(tr(Hi),G),Hi)==M[j])
            expected=dec(target['compressed_first_four_coefficients'][j]) if j<4 else [[-A[idx][j-4]*a*b for b in x] for a in x]
            check('all_compressed_coefficients_'+str((idx,j)),q==expected)
            totals[j]+=y[idx]*val;traces.append(y[idx]*val)
            face_equations.append(mixed+[rem]);transformed.append(G)
            if j<4: compressed.append(q)
            if j>=4:
                rr,qq=free[j-4]; V=c(8,rr)*c(60,rr)*c(8,qq)*c(948,qq)
                rawtotals[j-4]+=y[idx]*val*V/p8
        check('complete_saved_equations_and_trace_'+str(idx),enc(face_equations)==target['face_equation_coefficients'] and enc(slack)==target['scalar_face_equation'] and enc(traces)==target['weighted_trace_coefficients'])
        check('only_existing_selected_equalities_'+str(idx),enc(A[idx])==eq['original_equalities'][selected.index(idx)] and enc(slack[:4]+[F(0)]*6)==eq['rhs_coefficients'][selected.index(idx)])
        # Direct endpoint case: 0-dimensional compression still requires
        # the removed scalar zero. No invocation of proper-face wording.
        faceM=mul(mul(U,D),tr(U)) if r else [[F(0)]]
        onface=[row[:] for row in M[0]];onface[-1][-1]-=slack[0]
        K=[[F(i==j)+x[i]*x[j] for j in range(r)] for i in range(r)]
        check('face_factorization_including_empty_'+str(idx),onface==faceM and (mul(mul(tr(U),faceM),U)==mul(mul(K,D),K) if r else onface==[[F(0)]]))
        records.append({'mode':idx,'selected':True,'original_base':B,'original_cross_plane':cp,'bottom_coefficients':bottom,'old_inverse':Ti,'lift':lift,'extract':extract,'multiplier_vector':v,'original_multiplier_vector':original_v,'basis':H,'basis_inverse':Hi,'full_transformed_coefficients':transformed,'scalar_face_coefficients':slack,'weighted_trace_coefficients':traces,'face_factorization':faceM})
    check('49_affine_trace_coefficients',totals==[F(0)]*49 and enc(totals)==face['trace_coefficients']==face['original_trace_coefficients']==fv['original_trace_coefficients'])
    check('45_raw_trace_coefficients',rawtotals==[F(0)]*45 and enc(rawtotals)==face['raw_moment_trace_coefficients']==fv['raw_trace_coefficients'])
    check('exact_size_and_rank',sum(retained)==140 and sum(reduced)==112 and retained==face['retained_dimensions'] and reduced==face['reduced_dimensions'] and len(selected)==28)
    check('all_45_sign_rows_retained',len(free)==45 and all(p8/(c(8,r)*c(60,r)*c(8,q)*c(948,q))>0 for r,q in free))
    report.update(blocks=records,affine_trace=totals,raw_trace=rawtotals,retained_dimensions=retained,reduced_dimensions=reduced)
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),'types':500,'presentations':3000,'modes':81,'domain_rows':85,'sign_rows':45,'weighted_kernel_rows':90,'positive_multiplier_rank':len(selected),'retained_size':sum(retained),'reduced_size':sum(reduced),'affine_trace_actual_max_abs':max(map(abs,totals)),'raw_trace_actual_max_abs':max(map(abs,rawtotals)),'trace_required':0,'rank_cases':{str(k):v for k,v in sorted(cases.items())},'L084_rank_parametrization_review':'PENDING','full_plane_feasibility':'UNDECIDED'}
    save('completed_critical_audit')
    print(enc(report['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)


if __name__=='__main__':
    main()
