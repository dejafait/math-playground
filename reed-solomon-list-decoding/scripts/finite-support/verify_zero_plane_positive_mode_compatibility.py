"""Independent exact equality verification, no constructor/optimizer invocation.

Rebuild bounds from the imported audited cross/inverse/forced data, independently
eliminate the transposed matrix in reversed column order, and check all solutions.
"""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path
from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
NB=ROOT.parent.parent
OUT=ROOT/'zero-plane-positive-mode-compatibility-verification.json'


def dot(x,y):
    assert len(x)==len(y)
    return sum((a*b for a,b in zip(x,y)),F(0))


def mm(A,B):
    return [[dot(r,c) for c in zip(*B)] for r in A]


def decode(A):
    return [[F(*v) for v in r] for r in A]


def main():
    names=['zero-plane-positive-mode-compatibility-results.json',
           'fully-cancelling-separator-family-critical-audit.json',
           'fully-cancelling-separator-family-results.json']
    paths=[ROOT/n for n in names]
    data,audit,source=[json.loads(p.read_text()) for p in paths]
    checks,failures=[],[]
    def check(n,ok):
        checks.append(n)
        if not ok:failures.append(n)
    for name,obj in zip(names,[data,audit,source]):
        check('clean_'+name,not obj['failures'])
        for rel,h in obj['input_hashes'].items():
            check('binding_'+name+'_'+rel,hashlib.sha256((NB/rel).read_bytes()).hexdigest()==h)
    y=[F(*v) for v in audit['dual']]
    selected=[i for i,w in enumerate(y) if w>0]
    check('all_and_only_positive_weights',selected==data['selected_modes'] and len(selected)==28 and min(y)==0 and sum(y)==1)
    free=[(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8]
    p8=F(16792471,1181138102168120460);s=F(*audit['stationary_t78'])
    E=[];B=[];Qall=[];raw_coefficients=[]
    pairs=list(it.combinations_with_replacement(range(4),2))
    check('monomials_and_free_order',list(map(list,pairs))==data['monomials'] and list(map(list,free))==data['free_coordinates'])
    # Rebuild selected bounds without consuming the constructor's plane matrices.
    for idx in selected:
        m=audit['modes'][idx];a,b=divmod(idx,9)
        D=C(68-2*a,8-a)*C(956-2*b,8-b)
        cross=decode(m['source_cross']);inverse=decode(m['inverse_affine']);base=decode(m['source_base'])
        check('original_range_'+str(idx),mm(base,inverse)==cross)
        cost=[[sum(cross[k][i]*inverse[k][j] for k in range(len(cross)))/(p8*D) for j in range(5)] for i in range(5)]
        fixed=[F(*v) for v in m['forced']];fixed[0]-=F(*m['anchor'])
        Q=[[-v for v in r] for r in cost];Q[0][0]+=fixed[0]
        for i in range(1,5):Q[0][i]+=fixed[i]/2;Q[i][0]+=fixed[i]/2
        check('full_anchor_quadratic_'+str(idx),enc(Q)==m['quadratic']==source['modes'][idx]['quadratic']==data['full_quadratics'][idx])
        q=[[Q[i][j] for j in range(4)] for i in range(4)]
        q[0][0]+=2*s*Q[0][4]+s*s*Q[4][4]
        for i in range(1,4):q[0][i]+=s*Q[4][i];q[i][0]+=s*Q[i][4]
        B.append([q[i][j]*(1 if i==j else 2) for i,j in pairs]);Qall.append(q)
        raw=[F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)) for r,q in free]
        E.append([-v/F(D*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for v,(r,q) in zip(raw,free)])
        raw_coefficients.append(raw)
    check('every_original_coefficient',enc(E)==data['original_equalities'])
    check('every_plane_rhs_coefficient',enc(B)==data['rhs_coefficients'])
    U=decode(data['row_transform']);Ui=decode(data['row_transform_inverse']);R=decode(data['rref']);T=decode(data['transformed_rhs'])
    eye=[[F(i==j) for j in range(28)] for i in range(28)]
    for i,r in enumerate(mm(U,Ui)):check('invertible_U_row_'+str(i),r==eye[i])
    for i,(r,t) in enumerate(zip(mm(U,E),mm(U,B))):check('every_transformed_row_'+str(i),r==R[i] and t==T[i])
    # Independent left-kernel calculation: transpose, reverse unknown order,
    # forward elimination, then back-substitute with its one free coordinate 1.
    At=[list(reversed(r)) for r in zip(*E)];pivots=[];diagonal=[]
    for j in range(28):
        k=len(pivots);h=next((h for h in range(k,45) if At[h][j]),None)
        if h is None:continue
        At[k],At[h]=At[h],At[k];v=At[k][j];diagonal.append(v)
        for h in range(k+1,45):
            v=At[h][j]/At[k][j]
            if v:At[h]=[x-v*z for x,z in zip(At[h],At[k])]
        pivots.append(j)
    nonpiv=[j for j in range(28) if j not in pivots]
    check('independent_rank_27',len(pivots)==27 and len(nonpiv)==1 and all(not any(r) for r in At[27:]))
    z=[F(j in nonpiv) for j in range(28)]
    for k,j in reversed(list(enumerate(pivots))):z[j]=-sum(At[k][h]*z[h] for h in range(j+1,28))/At[k][j]
    left=list(reversed(z));ratio=left[0]/y[selected[0]]
    check('complete_left_kernel_matches_weights',left==[ratio*y[i] for i in selected] and ratio!=0 and all(dot(left,c)==0 for c in zip(*E)))
    check('all_10_compatibility_coefficients_zero',all(dot(left,c)==0 for c in zip(*B)) and not any(any(F(*v) for v in r) for r in data['compatibility_coefficients']))
    P=decode(data['particular_coefficients']);N=decode(data['right_kernel']);rawP=decode(data['raw_particular_coefficients'])
    residuals=[];rawres=[]
    for k,(r,b) in enumerate(zip(E,B)):
        residual=[dot(r,c)-v for c,v in zip(zip(*P),b)]
        check('all_original_polynomial_residuals_'+str(selected[k]),residual==[0]*10 and enc(residual)==data['original_row_residuals'][k])
        residuals.append(residual)
        a,bmode=divmod(selected[k],9);D=C(68-2*a,8-a)*C(956-2*bmode,8-bmode)
        rr=[dot(raw_coefficients[k],c)+p8*D*v for c,v in zip(zip(*rawP),b)]
        check('all_raw_schur_coefficients_'+str(selected[k]),rr==[0]*10 and enc(rr)==data['raw_schur_residuals'][k]);rawres.append(rr)
    for j,(r,q) in enumerate(free):check('raw_scaling_'+str(j),rawP[j]==[p8*x/F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for x in P[j]])
    Ns=mm(E,N);check('all_original_kernel_residuals',Ns==[[0]*18 for _ in E])
    nonpivot=data['nonpivot_columns'];check('18_independent_solution_directions',len(nonpivot)==18 and [N[j] for j in nonpivot]==[[F(i==j) for j in range(18)] for i in range(18)])
    fs=decode(audit['family']);domain=[[f[0]+s*f[4]]+f[1:4] for f in fs]
    check('all_original_domain_rows',enc(domain)==data['domain'] and len(domain)==85)
    point=[F(*v) for v in audit['point']];factors=[dot(f,point[:4]) for f in domain]
    check('nonempty_full_domain_intersection',point[4]==s and min(factors)==0 and enc(factors)==audit['factors']==data['domain_witness_factors'])
    report={'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'checks':checks,'failures':failures,'original_matrix':E,'rhs_coefficients':B,'restricted_quadratics':Qall,
            'transpose_echelon':At,'transpose_pivots':pivots,'transpose_diagonal':diagonal,
            'independent_left_null_vector':left,'left_weight_multiple':ratio,
            'original_polynomial_residuals':residuals,'raw_schur_residuals':rawres,'kernel_residuals':Ns,
            'domain':domain,'domain_witness_factors':factors,
            'summary':{'verdict':'VERIFIED_EQUALITY_ONLY' if not failures else 'FAILED','checks':len(checks),'failures':len(failures),
                       'rank':len(pivots),'left_nullity':len(nonpiv),'right_nullity':18,'actual_compatibility_coefficients':0,
                       'required_compatibility_coefficients':0,'actual_domain_minimum':min(factors),'required_domain_minimum':0,
                       'original_rows_verified':28,'quadratic_coefficients_per_row':10,'joint_completion_asserted':False}}
    OUT.write_text(json.dumps(enc(report),indent=2)+'\n')
    print(enc(report['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
