"""Exact signed equality compatibility on L083's entire necessary plane.

No optimizer or remaining-inequality test. Imports audited family coefficients;
rebuilds original beta rows, canonical weights, and the full equality reduction.
"""
import hashlib
import itertools as it
import json
import re
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, basis_solve, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-plane-positive-mode-compatibility-results.json'


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a,b in zip(x,y)), F(0))


def matmul(A, B):
    return [[dot(r,c) for c in zip(*B)] for r in A]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def main():
    names = ['fully-cancelling-separator-family-results.json',
             'fully-cancelling-separator-family-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'eight-common-column-joint-completion-critical-audit.json',
             'eight-distance-full-base-kernel-results.json']
    paths = [ROOT/n for n in names]
    data, ver, audit, a82, col = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    report = {'input_hashes':{str(p.relative_to(NB)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        report.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(report), indent=2)+'\n')

    for name,obj in zip(names,[data,ver,audit,a82,col]):
        check('clean_'+name, not obj['failures'])
        for rel,h in obj.get('input_hashes',{}).items():
            check('input_binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == h)
    fs = [[F(*v)]+[F(*x) for x in row] for v,row in zip(col['affine']['intercept'],col['affine']['slopes'])]
    check('whole_original_domain', enc(fs) == data['domain'] == ver['domain'] == audit['family'])
    check('original_parameters', col['affine']['free_indices'] == [56,63,69,78])
    free = [tuple(rq) for rq in data['free']]
    check('unchanged_45_coordinates', free == [(r,q) for r,q in it.product(range(9),repeat=2) if r+q>=8])
    check('whole_affine_kernel_contract', data['affine_column'] == audit['affine_column'] and data['weighted_kernel_residuals'] == ver['weighted_kernel_residuals'] == audit['weighted_kernel_residuals'])
    check('whole_key_contract', len(audit['records']) == len(ver['records']) == 500 and sum(len(r['presentations']) for r in ver['records']) == 3000)
    # Consume every affine/full-key entry; imported audit retains its qualifications.
    for i,r in enumerate(ver['records']):
        saved = audit['records'][i]
        check('full_key_'+str(i), r['type'] == saved['type'] and r['key'] == saved['key'] and r['affine'] == saved['affine'])
    p8 = F(16792471,1181138102168120460)
    matrices, quadratics, norms = [], [], []
    for k,m in enumerate(data['modes']):
        a,b = divmod(k,9)
        D = C(68-2*a,8-a)*C(956-2*b,8-b)
        row = [-F(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q),D*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r,q in free]
        check('original_row_'+str(k), enc(row) == data['matrix'][k] == ver['matrix'][k] == a82['matrix'][k] == audit['modes'][k]['row'])
        cost = [[F(*v) for v in r] for r in m['cost']]
        fixed = [F(*v) for v in m['fixed_minus_anchor']]
        Q = [[-v for v in r] for r in cost]
        Q[0][0] += fixed[0]
        for j in range(1,5):
            Q[0][j] += fixed[j]/2
            Q[j][0] += fixed[j]/2
        check('full_quadratic_'+str(k), enc(Q) == m['quadratic'] == ver['modes'][k]['quadratic'] == audit['modes'][k]['quadratic'])
        check('full_forced_anchor_cost_'+str(k), m['cost'] == ver['modes'][k]['cost'] and fixed == [F(*v)-(F(*ver['modes'][k]['anchor']) if j==0 else 0) for j,v in enumerate(ver['modes'][k]['forced'])])
        check('all_singular_range_coefficients_'+str(k), not any(any(F(*v) for v in r) for r in m['range_residuals']))
        matrices.append(row);quadratics.append(Q);norms.append(p8*D)
    manuscript = (NB/'lemmas/L082-common-column-joint-completion-obstruction.md').read_text()
    part = manuscript.split('**Canonical exact separator.**')[1].split('Let K_')[0]
    I = [int(v) for v in re.search(r'I=\((.*?)\)',part,re.S).group(1).replace('\n','').split(',')]
    Kt = [[F(-1) if j==-1 else matrices[i][j] for i in I] for j in [-1]+list(range(45))]
    local, wpivots = basis_solve(Kt,[F(-1)]+[F(0)]*45)
    weights = [F(0)]*81
    for i,v in zip(I,local):weights[i] = v
    check('canonical_46_equations', len(wpivots)==46 and all(wpivots) and matmul(Kt,[[v] for v in local]) == [[F(-1)]]+[[F(0)]]*45)
    check('unchanged_weights', enc(weights) == data['weights'] == ver['weights'] == audit['dual'] == a82['dual'] and min(weights)==0 and sum(weights)==1)
    selected = [i for i,v in enumerate(weights) if v>0]
    check('exact_positive_support', len(selected)==28)
    E = [matrices[i] for i in selected]
    weighted = [sum(weights[i]*matrices[i][j] for i in selected) for j in range(45)]
    check('all_45_cancellations', weighted == [0]*45)
    M = [[sum(w*Q[i][j] for w,Q in zip(weights,quadratics)) for j in range(5)] for i in range(5)]
    gamma = -M[4][4];s = -M[0][4]/M[4][4]
    e = [-s,F(0),F(0),F(0),F(1)]
    check('complete_negative_square', gamma>0 and M == [[-gamma*x*y for y in e] for x in e] and enc(M) == data['M'] == audit['M'])
    check('same_stationary_parameter', enc(s) == data['square']['stationary_t78'] == ver['stationary_t78'] == audit['stationary_t78'])
    # zeta=H*q with q=(1,t56,t63,t69). This substitutes ONLY t78=s.
    H = identity(4)+[[s,F(0),F(0),F(0)]]
    monomials = list(it.combinations_with_replacement(range(4),2))
    restricted = [matmul(list(map(list,zip(*H))),matmul(Q,H)) for Q in quadratics]
    coefficients = [[Q[i][j]*(1 if i==j else 2) for i,j in monomials] for Q in restricted]
    B = [coefficients[i] for i in selected]
    domain = [[f[0]+s*f[4]]+f[1:4] for f in fs]
    check('all_85_rows_retained', len(domain)==85 and len(B)==28 and all(len(r)==10 for r in B))
    report.update(selected_modes=selected,free_coordinates=free,weights=weights,stationary_t78=s,
                  full_matrix=matrices,full_quadratics=quadratics,embedding=H,monomials=monomials,
                  original_equalities=E,rhs_coefficients=B,domain=domain)
    save('original_plane_system_saved')
    print('Saved original 28-by-45 system; three parameters, 85 domain rows; failures:',failures,flush=True)
    # R=U*E. Every recorded elementary operation is invertible.
    R = [r[:] for r in E];U = identity(28);operations=[];pivots=[]
    def op(kind,k,h,v=None):
        operations.append([kind,k,h,v])
        for T in [R,U]:
            if kind=='swap':T[k],T[h] = T[h],T[k]
            elif kind=='scale':T[k] = [v*x for x in T[k]]
            else:T[k] = [x+v*y for x,y in zip(T[k],T[h])]
    for j in range(45):
        k = len(pivots)
        h = next((h for h in range(k,28) if R[h][j]),None)
        if h is None:continue
        if h!=k:op('swap',k,h)
        op('scale',k,k,1/R[k][j])
        for h in range(28):
            if h!=k and R[h][j]:op('add',h,k,-R[h][j])
        pivots.append(j)
        if len(pivots)==28:break
    rank = len(pivots);T = matmul(U,B)
    # Invert the recorded operations, applied in reverse chronological order.
    inverse = identity(28)
    for kind,k,h,v in reversed(operations):
        if kind=='swap':inverse[k],inverse[h] = inverse[h],inverse[k]
        elif kind=='scale':inverse[k] = [x/v for x in inverse[k]]
        else:inverse[k] = [x-v*y for x,y in zip(inverse[k],inverse[h])]
    check('invertible_row_certificate_both_products', matmul(U,inverse)==identity(28) and matmul(inverse,U)==identity(28))
    check('all_original_constant_rows', matmul(U,E)==R)
    check('rref_pivots', all(R[i][j]==F(i==k) for k,j in enumerate(pivots) for i in range(28)) and all(not any(r) for r in R[rank:]))
    L = U[rank:];compatibility = T[rank:]
    check('complete_left_nullspace_rows', matmul(L,E)==[[F(0)]*45 for _ in L])
    proportionality = None
    if len(L)==1:
        proportionality = L[0][0]/weights[selected[0]]
        check('only_dependence_is_old_weights', proportionality!=0 and L[0]==[proportionality*weights[i] for i in selected])
    # Independence/completeness follows from invertible U and the rref pivots.
    particular = [[F(0)]*10 for _ in range(45)]
    for k,j in enumerate(pivots):particular[j] = T[k]
    nonpivots = [j for j in range(45) if j not in pivots]
    kernel = [[F(j==h) if j in nonpivots else -R[pivots.index(j)][h] for h in nonpivots] for j in range(45)]
    kernel_residuals = matmul(E,kernel)
    check('whole_right_kernel', kernel_residuals==[[F(0)]*len(nonpivots) for _ in E])
    check('right_kernel_free_coordinates', [kernel[j] for j in nonpivots]==identity(len(nonpivots)))
    residuals = [[x-y for x,y in zip(r,b)] for r,b in zip(matmul(E,particular),B)]
    automatic = not any(any(r) for r in compatibility)
    check('original_residual_equivalence', (not any(any(r) for r in residuals))==automatic)
    raw_particular = [[p8*x/F(C(8,r)*C(60,r)*C(8,q)*C(948,q)) for x in row] for (r,q),row in zip(free,particular)]
    raw_residuals=[]
    for k,i in enumerate(selected):
        a,b = divmod(i,9)
        lhs = [sum(beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)*raw_particular[j][h] for j,(r,q) in enumerate(free))+norms[i]*B[k][h] for h in range(10)]
        check('original_raw_schur_row_'+str(i), lhs==[-norms[i]*x for x in residuals[k]])
        raw_residuals.append(lhs)
    # Reuse L083's attained-domain witness, without restricting the domain to it.
    fullpoint = [F(*v) for v in data['point']];qpoint=fullpoint[:4]
    values = [dot(f,qpoint) for f in domain]
    check('original_domain_nonempty_on_plane', fullpoint[4]==s and matmul(H,[[x] for x in qpoint])==[[x] for x in fullpoint] and min(values)>=0 and enc(values)==data['factors']==audit['factors'])
    monpoint=[qpoint[i]*qpoint[j] for i,j in monomials]
    pointsol=[dot(r,monpoint) for r in particular]
    check('witness_compatibility', all(dot(r,monpoint)==0 for r in compatibility))
    report.update(row_operations=operations,row_transform=U,row_transform_inverse=inverse,rref=R,pivot_columns=pivots,
                  transformed_rhs=T,left_nullspace=L,compatibility_coefficients=compatibility,
                  left_nullspace_weight_multiple=proportionality,
                  particular_coefficients=particular,nonpivot_columns=nonpivots,right_kernel=kernel,
                  original_row_residuals=residuals,right_kernel_residuals=kernel_residuals,
                  raw_particular_coefficients=raw_particular,raw_schur_residuals=raw_residuals,
                  domain_witness=fullpoint,domain_witness_factors=values,signed_solution_at_witness=pointsol)
    report['summary']={'verdict':('AUTOMATIC_COMPATIBILITY' if automatic else 'FURTHER_COMPATIBILITY_REQUIRED') if not failures else 'FAILED',
                       'checks':len(checks),'failures':len(failures),'rows':28,'columns':45,'rank':rank,
                       'left_nullity':28-rank,'right_nullity':45-rank,'row_operations':len(operations),
                       'compatibility_polynomials':len(compatibility),'nonzero_compatibility_polynomials':sum(any(r) for r in compatibility),
                       'actual_original_residuals_zero':not any(any(r) for r in residuals),
                       'required_original_residual':0,'domain_rows':85,'domain_parameters':3,
                       'actual_domain_witness_minimum':min(values),'required_domain_minimum':0,
                       'joint_completion_asserted':False}
    save('completed')
    print(enc(report['summary']),flush=True)
    print('Failures:',failures,'; full certificate:',OUT.relative_to(NB),flush=True)
    if failures:raise SystemExit(1)


if __name__=='__main__':main()
