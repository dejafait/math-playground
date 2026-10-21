"""Dedicated L084 audit: complete rank, compatibility and all-solution identities.

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
OUT = ROOT/'zero-plane-positive-mode-compatibility-critical-audit.json'


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
    # Reuse the reviewed face only as an original-coordinate comparison.
    # Its pending rank flag is historical and is not used as evidence here.
    facepath=ROOT/'zero-plane-fixed-face-critical-audit.json'
    facereview=json.loads(facepath.read_text())
    report['input_hashes'][str(facepath.relative_to(NB))]=hashlib.sha256(facepath.read_bytes()).hexdigest()
    check('face_review_clean',not facereview['failures'])
    for rel,h in facereview['input_hashes'].items():
        check('face_review_binding_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    check('face_same_domain_weights',facereview['domain']==enc(domain) and facereview['weights']==enc(y))

    monomials=list(it.combinations_with_replacement(range(4),2))
    H=eye(4)+[[s,F(0),F(0),F(0)]]
    Qall=[]; B=[]; rawrows=[]; planeQ=[]
    for idx,(norm,SB,SC,forced,anchor) in enumerate(original):
        inv=dec(src['modes'][idx]['inverse_affine'])
        cost=[[sum(SC[k][i]*inv[k][j] for k in range(len(SB)))/norm for j in range(5)] for i in range(5)]
        Q=[[-v for v in r] for r in cost]
        Q[0][0]+=forced[0]-anchor
        for j in range(1,5): Q[0][j]+=forced[j]/2; Q[j][0]+=forced[j]/2
        check('symmetric_original_quadratic_'+str(idx),Q==tr(Q) and enc(Q)==src['modes'][idx]['quadratic']==res['modes'][idx]['quadratic']==ver['modes'][idx]['quadratic']==eq['full_quadratics'][idx])
        Qall.append(Q)
        if idx not in selected: continue
        qp=mul(tr(H),mul(Q,H)); planeQ.append(qp)
        coeff=[qp[i][j]*(1 if i==j else 2) for i,j in monomials]; B.append(coeff)
        a,b=divmod(idx,9)
        rawrows.append([F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free])
        # L085 keeps the same scalar equality, with no quadratic terms
        # silently dropped. Compare its complete 49 affine coefficients.
        expected=[coeff[j] for j in range(4)]+[-v for v in A[idx]]
        check('selected_face_equality_'+str(idx),not any(coeff[4:]) and enc(expected)==face['blocks'][idx]['scalar_face_equation'])
    E=[A[i] for i in selected]
    check('complete_original_system',enc(E)==eq['original_equalities']==ev['original_matrix'] and enc(B)==eq['rhs_coefficients']==ev['rhs_coefficients'])
    check('coordinate_monomial_embedding_order',eq['monomials']==list(map(list,monomials)) and eq['free_coordinates']==list(map(list,free)) and eq['embedding']==enc(H))
    M=[[sum(y[k]*Qall[k][i][j] for k in range(81)) for j in range(5)] for i in range(5)]
    gamma=-M[4][4]; e=[-s,F(0),F(0),F(0),F(1)]
    check('full_original_negative_square',gamma>0 and M==[[-gamma*x*z for z in e] for x in e] and enc(M)==src['M']==res['M'])

    # Reconstruct the specified elimination, checking each saved elementary
    # operation at the moment it is applied, including its invertibility.
    R=[r[:] for r in E]; U=eye(28); ops=[]; pivcols=[]; pivvals=[]
    def operation(kind,k,h,v=None):
        op=[kind,k,h,v]; index=len(ops)
        check('operation_'+str(index),index<len(eq['row_operations']) and enc(op)==eq['row_operations'][index])
        check('operation_invertible_'+str(index),0<=k<28 and 0<=h<28 and (kind!='scale' or v!=0) and (kind!='add' or k!=h))
        for mat in [R,U]:
            if kind=='swap': mat[k],mat[h]=mat[h],mat[k]
            elif kind=='scale': mat[k]=[v*x for x in mat[k]]
            else: mat[k]=[x+v*z for x,z in zip(mat[k],mat[h])]
        ops.append(op)
    for j in range(45):
        k=len(pivcols)
        h=next((i for i in range(k,28) if R[i][j]),None)
        if h is None: continue
        if h!=k: operation('swap',k,h)
        pv=R[k][j]; pivvals.append(pv)
        operation('scale',k,k,1/pv)
        for i in range(28):
            if i!=k and R[i][j]: operation('add',i,k,-R[i][j])
        pivcols.append(j)
    wanted=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,21,22,23,24,28,29,30,36,37]
    check('all_674_operations',len(ops)==len(eq['row_operations'])==674)
    check('all_27_nonzero_pivots',pivcols==wanted==eq['pivot_columns'] and len(pivvals)==27 and all(pivvals))
    Ui=dec(eq['row_transform_inverse']); T=mul(U,B)
    check('complete_transform_and_RREF',enc(U)==eq['row_transform'] and enc(R)==eq['rref'] and enc(T)==eq['transformed_rhs'])
    inverse_replay=eye(28)
    for kind,k,h,v in reversed(ops):
        if kind=='swap': inverse_replay[k],inverse_replay[h]=inverse_replay[h],inverse_replay[k]
        elif kind=='scale': inverse_replay[k]=[x/v for x in inverse_replay[k]]
        else: inverse_replay[k]=[x-v*z for x,z in zip(inverse_replay[k],inverse_replay[h])]
    check('inverse_operations',inverse_replay==Ui)
    UE=mul(U,E); UU=mul(U,Ui); UU2=mul(Ui,U)
    for i in range(28):
        check('both_inverse_and_transform_row_'+str(i),UU[i]==UU2[i]==eye(28)[i] and UE[i]==R[i])
        check('all_RREF_pivot_entries_'+str(i),[R[i][j] for j in pivcols]==[F(i==k) for k in range(27)])
    check('entire_last_zero_row',R[27]==[0]*45)
    left=U[27]; multiple=left[0]/y[selected[0]]
    leftres=mul([left],E); compatibility=mul([left],B)
    check('entire_left_nullspace',multiple!=0 and left==[multiple*y[i] for i in selected] and leftres==[[0]*45] and enc([left])==eq['left_nullspace'])
    for j,v in enumerate(compatibility[0]):check('compatibility_coefficient_'+str(j),v==0 and eq['compatibility_coefficients'][0][j]==enc(v))

    # Independent rank lower bound from a square minor, eliminated in reverse
    # coordinate order. Its determinant is nonzero; the complete U supplies
    # the upper bound and left-kernel exhaustion.
    minor=[[E[i][j] for j in reversed(pivcols)] for i in range(27)]
    diag=[]; swaps=0
    for j in range(27):
        h=next(i for i in range(j,27) if minor[i][j])
        if h!=j: minor[j],minor[h]=minor[h],minor[j]; swaps+=1
        pv=minor[j][j];diag.append(pv)
        for i in range(j+1,27):
            factor=minor[i][j]/pv
            minor[i]=[x-factor*z for x,z in zip(minor[i],minor[j])]
    determinant=F((-1)**(swaps+27*26//2))
    for v in diag:determinant*=v
    check('independent_27_minor_nonzero',len(diag)==27 and all(diag) and determinant!=0)

    nonpiv=[j for j in range(45) if j not in pivcols]
    P=dec(eq['particular_coefficients']); N=dec(eq['right_kernel'])
    G=[[F(0)]*28 for _ in range(45)]
    for i,j in enumerate(pivcols): G[j]=U[i][:]
    Fselect=[[F(j==h) for j in range(45)] for h in nonpiv]
    check('solution_dimensions',len(P)==len(N)==45 and all(len(r)==10 for r in P) and all(len(r)==18 for r in N) and nonpiv==eq['nonpivot_columns'] and len(nonpiv)==18)
    GP=mul(G,B); EP=mul(E,P); EN=mul(E,N)
    GE=mul(G,E); NF=mul(N,Fselect)
    FN=mul(Fselect,N); FP=mul(Fselect,P)
    reverse=[[x+z-F(i==j) for j,(x,z) in enumerate(zip(r,t))] for i,(r,t) in enumerate(zip(GE,NF))]
    check('free_coordinate_inverse',FN==eye(18) and FP==[[0]*10 for _ in range(18)])
    for i in range(45):
        check('particular_recipe_'+str(i),P[i]==GP[i])
        check('reverse_all_solution_identity_'+str(i),reverse[i]==[0]*45)
    for i in range(28):
        check('forward_all_solution_identity_'+str(i),EP[i]==B[i] and EN[i]==[0]*18)
        check('saved_original_residuals_'+str(i),[F(*v) for v in eq['original_row_residuals'][i]]==[0]*10 and eq['right_kernel_residuals'][i]==enc(EN[i]))

    # Positive diagonal raw-coordinate change S: rawY=S*z. Both forward
    # homogeneous residuals and the reverse identity are checked explicitly.
    scales=[p8/F(c(8,r)*c(60,r)*c(8,q)*c(948,q)) for r,q in free]
    check('all_raw_scales_positive',len(scales)==45 and min(scales)>0)
    rawP=[[v*x for x in row] for v,row in zip(scales,P)]
    rawN=[[v*x for x in row] for v,row in zip(scales,N)]
    rawG=[[v*x for x in row] for v,row in zip(scales,G)]
    rawE=[[x/scales[j] for j,x in enumerate(row)] for row in E]
    rawF=[[x/scales[j] for j,x in enumerate(row)] for row in Fselect]
    rawGE=mul(rawG,rawE); rawNF=mul(rawN,rawF)
    rawreverse=[[x+z-F(i==j) for j,(x,z) in enumerate(zip(r,t))] for i,(r,t) in enumerate(zip(rawGE,rawNF))]
    rawres=[]; rawhom=[]
    check('raw_particular_recipe',enc(rawP)==eq['raw_particular_coefficients'])
    for k,idx in enumerate(selected):
        norm=original[idx][0]
        rp=[dot(rawrows[k],col)+norm*v for col,v in zip(zip(*rawP),B[k])]
        rn=[dot(rawrows[k],col) for col in zip(*rawN)]
        rawres.append(rp);rawhom.append(rn)
        check('raw_forward_particular_'+str(idx),rp==[0]*10 and enc(rp)==eq['raw_schur_residuals'][k]==ev['raw_schur_residuals'][k])
        check('raw_forward_all_18_directions_'+str(idx),rn==[0]*18)
        check('raw_original_sign_and_norm_'+str(idx),rawrows[k]==[-norm*x for x in rawE[k]])
    for i,row in enumerate(rawreverse):check('raw_reverse_all_solution_identity_'+str(i),row==[0]*45)
    check('raw_free_coordinate_inverse',mul(rawF,rawN)==eye(18) and mul(rawF,rawP)==[[0]*10 for _ in range(18)])
    point=[F(*v) for v in src['point']]; factors=[dot(r,point[:4]) for r in domain]
    check('same_imported_nonempty_domain',point[4]==s and enc(point)==eq['domain_witness'] and enc(factors)==src['factors']==eq['domain_witness_factors'] and min(factors)==0 and [i for i,v in enumerate(factors) if v==0]==[33,56] and sum(v>0 for v in factors)==83)
    report.update(original_matrix=E,rhs_coefficients=B,full_quadratics=Qall,restricted_quadratics=planeQ,
                  row_operations=ops,pivot_columns=pivcols,pivot_values=pivvals,row_transform=U,row_transform_inverse=Ui,rref=R,transformed_rhs=T,
                  independent_minor_echelon=minor,independent_minor_pivots=diag,independent_minor_determinant=determinant,
                  left_null_vector=left,left_weight_multiple=multiple,left_residuals=leftres,compatibility_coefficients=compatibility,
                  particular=P,kernel=N,free_extractor=Fselect,right_inverse_on_range=G,reverse_identity_residuals=reverse,
                  original_particular_residuals=[[x-z for x,z in zip(r,t)] for r,t in zip(EP,B)],original_kernel_residuals=EN,
                  raw_scales=scales,raw_particular=rawP,raw_kernel=rawN,raw_free_extractor=rawF,raw_right_inverse_on_range=rawG,
                  raw_particular_residuals=rawres,raw_kernel_residuals=rawhom,raw_reverse_identity_residuals=rawreverse,
                  domain_witness=point,domain_factors=factors)
    report['summary']={'verdict':'RETAINED' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
                       'rank_actual':len(pivcols),'rank_required':27,'left_nullity':1,'right_nullity':18,'row_operations':len(ops),
                       'compatibility_coefficients_checked':10,'actual_max_compatibility_residual':max(map(abs,compatibility[0])),
                       'required_residual':0,'original_rows':28,'raw_homogeneous_residuals':28*18,'reverse_identity_entries_each':45*45,
                       'domain_rows':85,'types':500,'presentations':3000,'modes':81,'joint_feasibility':'UNDECIDED',
                       'ancestor_contracts':'IMPORTED_WITH_EXISTING_QUALIFICATIONS'}
    save('completed')
    print(enc(report['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)


if __name__=='__main__': main()
