"""Step 306: one fixed-face, exactly equality-eliminated conic proposal.

Pre-solve rational identities check both affine parametrization directions.
Numerics supply a proposal only. Exactly one coordinate rounding follows.
All original-coordinate residuals, including failed ones, stay on disk.
"""
import hashlib
import itertools as it
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'reduced-zero-plane-joint-results.json'
CAP = 10000


def dot(a, b):
    assert len(a) == len(b)
    return sum((x*y for x, y in zip(a, b)), F(0))


def tr(A):
    return list(map(list, zip(*A))) if A else []


def mm(A, B):
    assert not A or len(A[0]) == len(B)
    return [[dot(r, c) for c in zip(*B)] for r in A]


def dec(A):
    return [[F(*v) for v in row] for row in A]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def pencil(B, cross, bottom, j):
    n = len(B)
    M = [[F(0)]*(n+1) for _ in range(n+1)]
    if j == 0:
        for i in range(n):
            M[i][:n] = B[i][:]
    if j < 4:
        for i in range(n):
            M[i][n] = M[n][i] = cross[i][j]
    M[n][n] = bottom[j]
    return M


def det(A):
    if not A:
        return F(1)
    R = [r[:] for r in A]
    value = F(1)
    for j in range(len(R)):
        p = next((i for i in range(j, len(R)) if R[i][j]), None)
        if p is None:
            return F(0)
        if p != j:
            R[p], R[j] = R[j], R[p]
            value = -value
        pivot = R[j][j]
        value *= pivot
        for i in range(j+1, len(R)):
            a = R[i][j]/pivot
            for k in range(j+1, len(R)):
                R[i][k] -= a*R[j][k]
    return value


def minors(A):
    return [{'indices': list(I), 'determinant': det([[A[i][j] for j in I] for i in I])}
            for size in range(1, len(A)+1) for I in it.combinations(range(len(A)), size)]


def main():
    names = ['zero-plane-joint-feasibility-results.json',
             'zero-plane-fixed-face-results.json', 'zero-plane-fixed-face-critical-audit.json',
             'zero-plane-positive-mode-compatibility-results.json',
             'zero-plane-positive-mode-compatibility-critical-audit.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'fully-cancelling-separator-family-verification.json',
             'eight-common-column-joint-completion-critical-audit.json',
             'eight-distance-full-base-kernel-results.json']
    paths = [ROOT/n for n in names]
    old, face, fa, eq, ea, src, ver, a82, col = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    out = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
           'iteration_cap_before_solve': CAP, 'numerical_runs_allowed': 1,
           'reconstruction_passes_allowed': 1}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        out.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for name, obj in zip(names, [old, face, fa, eq, ea, src, ver, a82, col]):
        check('clean_'+name, not obj['failures'])
        for rel, digest in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p8 = F(16792471, 1181138102168120460)
    s = F(*eq['stationary_t78'])
    family = [[F(*v)]+[F(*x) for x in row] for v, row in zip(col['affine']['intercept'], col['affine']['slopes'])]
    domain = [[f[0]+s*f[4]]+f[1:4] for f in family]
    check('original_domain', len(domain) == 85 and enc(domain) == old['domain'] == face['domain'] == eq['domain'])
    check('all_90_kernel_equations', len(col['equations']) == 90 and all(
        [sum((F(*v)*f[j] for v, f in zip(row, family)), F(0)) for j in range(5)] == [F(*b)]+[F(0)]*4
        for row, b in zip(col['equations'], col['rhs'])))
    check('weighted_whole_kernel_contract', src['weighted_kernel_residuals'] == ver['weighted_kernel_residuals'] and
          len(src['weighted_kernel_residuals']) == 90 and all(not any(F(*v) for v in r) for r in src['weighted_kernel_residuals']))
    check('500_types_3000_presentations', len(src['records']) == 500 and sum(len(r['presentations']) for r in ver['records']) == 3000)
    for k, (a, b) in enumerate(zip(src['records'], ver['records'])):
        check('full_key_'+str(k), a['key'] == b['key'] and a['type'] == b['type'] and a['affine'] == b['affine'])
    free = [(r, q) for r, q in it.product(range(9), repeat=2) if r+q >= 8]
    A = dec(eq['full_matrix'])
    P, N, E, rhs, U = map(dec, [eq['particular_coefficients'], eq['right_kernel'], eq['original_equalities'], eq['rhs_coefficients'], eq['row_transform']])
    check('no_quadratic_particular_coefficients', all(not any(row[4:]) for row in P))
    check('no_quadratic_selected_rhs', all(not any(row[4:]) for row in rhs))
    Pa = [r[:4] for r in P]
    nonp = eq['nonpivot_columns']
    # Augmented original coordinate order is (1,u1,u2,u3,z0,...,z44).
    # Augmented reduced order is (1,u1,u2,u3,h0,...,h17).
    L = [row+[F(0)]*18 for row in eye(4)]+[p+n for p, n in zip(Pa, N)]
    reverse = [eye(49)[i] for i in list(range(4))+[4+j for j in nonp]]
    constraints = [[-v for v in b[:4]]+e for e, b in zip(E, rhs)]
    K = [[F(0)]*28 for _ in range(49)]
    for k, p in enumerate(eq['pivot_columns']):
        K[4+p] = [-v for v in U[k]]
    delta = [[x-y for x, y in zip(a, b)] for a, b in zip(mm(L, reverse), eye(49))]
    check('all_forward_equalities', mm(constraints, L) == [[F(0)]*22 for _ in range(28)])
    check('reduced_left_inverse', mm(reverse, L) == eye(22))
    check('original_reverse_modulo_all_equalities', delta == mm(K, constraints))
    check('all_18_homogeneous_coordinates', len(nonp) == 18 and [N[j] for j in nonp] == eye(18))
    check('reviewed_original_matrix', enc(E) == [eq['full_matrix'][i] for i in eq['selected_modes']])
    scalar_rows = [r+[F(0)]*18 for r in domain]+L[4:]
    original_pencils, retained_pencils, reduced_pencils, face_zero_rows = [], [], [], []
    for k, (m, b, f) in enumerate(zip(src['modes'], old['blocks'], face['blocks'])):
        a, bb = divmod(k, 9)
        D = C(68-2*a, 8-a)*C(956-2*bb, 8-bb)
        norm = p8*D
        row = [-F(beta(68,8,8,a,8-r)*beta(956,8,8,bb,8-q), D*C(8,r)*C(60,r)*C(8,q)*C(948,q)) for r, q in free]
        check('original_beta_'+str(k), row == A[k] and enc(row) == m['row'] == a82['matrix'][k])
        B = [[v/norm for v in r] for r in dec(m['source_base'])]
        c5 = dec(m['source_cross'])
        cross = [[(r[0]+s*r[4])/norm]+[v/norm for v in r[1:4]] for r in c5]
        forced = [F(*v) for v in m['forced']]
        forced[0] -= F(*m['anchor'])
        bottom = [forced[0]+s*forced[4]]+forced[1:4]+[-v for v in row]
        check('original_affine_block_'+str(k), enc(B) == b['original_base'] and enc(cross) == b['original_cross_plane'] and enc(bottom[:4]) == b['fixed_plane'])
        T, R, TC = dec(b['congruence']), dec(b['diagonalized_base']), dec(b['transformed_cross_plane'])
        check('old_congruence_'+str(k), mm(mm(T,B),tr(T)) == R and mm(T,cross) == TC if B else not R and not TC)
        active = b['retained_indices']
        check('all_old_removed_zero_rows_'+str(k), all(not any(R[i]) and not any(TC[i]) for i in range(len(B)) if i not in active))
        d, c = [R[i][i] for i in active], [TC[i] for i in active]
        check('positive_old_base_'+str(k), all(v > 0 for v in d))
        diagonal = [[v if i == j else F(0) for j, v in enumerate(d)] for i in range(len(d))]
        original = [pencil(B,cross,bottom,j) for j in range(49)]
        retained = [pencil(diagonal,c,bottom,j) for j in range(49)]
        def substitute(pencils):
            n = len(pencils[0])
            return [[[sum((pencils[j][a][b]*L[j][v] for j in range(49)), F(0)) for b in range(n)] for a in range(n)] for v in range(22)]
        original_lifted = substitute(original)
        retained_lifted = substitute(retained)
        # Check the old extraction/inverse pullback in all affine coefficients.
        Ti = eye(len(B))
        for i in range(len(B)):
            for j in range(i):
                Ti[i][j] = -sum((T[i][h]*Ti[h][j] for h in range(j,i)), F(0))
        oldlift = [[Ti[i][j] for j in active]+[F(0)] for i in range(len(B))]+[[F(0)]*len(d)+[F(1)]]
        check('invertible_old_congruence_'+str(k), mm(T,Ti) == mm(Ti,T) == eye(len(B)) if B else not Ti)
        for j in range(49):
            check('original_pullback_'+str((k,j)), mm(mm(oldlift,retained[j]),tr(oldlift)) == original[j])
        if k in eq['selected_modes']:
            kernel, comp, inv = dec(f['kernel_basis']), [F(*v) for v in f['complement_vector']], dec(f['basis_inverse'])
            H = [r+[v] for r, v in zip(kernel,comp)]
            check('face_basis_inverse_'+str(k), mm(H,inv) == mm(inv,H) == eye(len(H)))
            transformed = [mm(mm(tr(H),p),H) for p in retained]
            for j in range(49):
                check('all_face_pullback_'+str((k,j)), mm(mm(tr(inv),transformed[j]),inv) == retained[j])
            mixed_removed = [[transformed[j][a][-1] for j in range(49)] for a in range(len(H))]
            check('all_saved_mixed_removed_'+str(k), enc(tr(mixed_removed)) == f['face_equation_coefficients'])
            eliminated = mm(mixed_removed,L)
            check('every_mixed_removed_equation_after_lift_'+str(k), all(not any(r) for r in eliminated))
            face_zero_rows.append({'mode': k, 'original_coefficients': mixed_removed, 'reduced_coefficients': eliminated})
            reduced = [mm(mm(tr(kernel),p),kernel) if len(d) else [] for p in retained_lifted]
            check('selected_compressed_constant_'+str(k), all(not any(any(r) for r in p) for p in reduced[1:]))
            # Keep a rational inverse congruence to the positive diagonal D.
            x = kernel[-1]
            den = 1+dot(x,x)
            Q = [[F(i == j)-x[i]*x[j]/den for j in range(len(d))] for i in range(len(d))]
            check('selected_compressed_positive_factorization_'+str(k), mm(mm(Q,reduced[0]),Q) == diagonal if d else not reduced[0])
        else:
            reduced = retained_lifted
            Q = eye(len(d)+1)
        original_pencils.append(original)
        retained_pencils.append(retained)
        reduced_pencils.append({'mode': k, 'coefficients': reduced, 'constant_congruence': Q})
    check('140_to_112_exact', sum(len(p[0]) for p in retained_pencils) == 140 and sum(len(p['coefficients'][0]) for p in reduced_pencils) == 112)
    out.update(stationary_t78=s, domain=domain, free=free, matrix=A,
               lift=L, reverse=reverse, reverse_identity_multipliers=K,
               selected_constraints=constraints, particular=Pa, kernel=N,
               selected_modes=eq['selected_modes'], nonpivots=nonp,
               scalar_rows=scalar_rows, original_pencils=original_pencils,
               retained_pencils=retained_pencils, reduced_pencils=reduced_pencils,
               face_equations=face_zero_rows)
    save('exact_affine_elimination_both_directions_and_full_model_saved')
    print('Exact 48-to-21 variable lift and 140-to-112 face model: checks',len(checks),'failures',failures,flush=True)
    if failures:
        raise SystemExit('Stop before numerical work: exact model failed')
    # Invertible coordinate scales, followed by normalized scalar/block rows.
    scales = [F(1,10**11)]*3+[F(*old['numerical_scaling']['zscale'][j]) for j in nonp]
    scalar_scales = [max(abs(r[0]),*(abs(a*b) for a,b in zip(r[1:],scales))) or F(1) for r in scalar_rows]
    offset = [float(r[0]/t) for r,t in zip(scalar_rows,scalar_scales)]
    rows = [[float(a*b/t) for a,b in zip(r[1:],scales)] for r,t in zip(scalar_rows,scalar_scales)]
    layouts, normalizations = [], []
    for data in reduced_pencils:
        k = data['mode']
        coeff = data['coefficients']
        d = len(coeff[0])
        start = len(offset)
        if k in eq['selected_modes']:
            Q = data['constant_congruence']
            mat = mm(mm(Q,coeff[0]),tr(Q)) if d else []
            diagonals = [mat[i][i] for i in range(d)]
            check('selected_positive_numerical_congruence_'+str(k), all(v>0 for v in diagonals))
            diagscales = [float(v)**(-0.5) for v in diagonals]
            bottomscale = None
        else:
            # Positive old diagonal, plus one last coordinate. Bound every
            # affine bottom coefficient and every cross-energy coefficient.
            diagonals = [coeff[0][i][i] for i in range(d-1)]
            bottomscale = max([abs(coeff[0][-1][-1])]+[abs(p[-1][-1]*t) for p,t in zip(coeff[1:],scales)])
            for i,v in enumerate(diagonals):
                crossbound = abs(coeff[0][i][-1])+sum(abs(p[i][-1]*t) for p,t in zip(coeff[1:],scales))
                bottomscale += crossbound**2/v
            bottomscale = bottomscale or F(1)
            diagscales = [float(v)**(-0.5) for v in diagonals]+[float(bottomscale)**(-0.5)]
            mat = coeff[0]
        for i in range(d):
            for j in range(d):
                t = diagscales[i]*diagscales[j]
                offset.append(float(mat[i][j])*t)
                rows.append([0.0]*21 if k in eq['selected_modes'] else [float(p[i][j]*v)*t for p,v in zip(coeff[1:],scales)])
        layouts.append([start,d])
        normalizations.append({'mode':k,'bottom_scale':bottomscale,'positive_diagonal_scales':diagscales,'constant_congruence':data['constant_congruence']})
    M, offset = np.asarray(rows), np.asarray(offset)
    # One invertible diagonal column equilibration; no equations discarded.
    column_norms = np.linalg.norm(M,axis=0)
    check('all_21_columns_nonzero_finite', bool(np.all(np.isfinite(column_norms)) and np.all(column_norms>0)))
    column_scales = [F(float(v)) for v in 1/column_norms]
    scales = [a*b for a,b in zip(scales,column_scales)]
    M = M*np.asarray([float(v) for v in column_scales])
    Uv, singular, Vt = np.linalg.svd(M,full_matrices=False)
    check('all_21_numerical_singular_values_retained', len(singular)==21 and singular[-1]>singular[0]*1e-13)
    pinv = (Vt.T*(1/singular))@Uv.T
    out.update(numerical_scaling={'coordinate_scales':scales,'scalar_scales':scalar_scales,
                                 'blocks':normalizations,'layouts':layouts,'M':M.tolist(),
                                 'offset':offset.tolist(),'singular_values':singular.tolist()},
               numerical_method='One NumPy product-cone ADMM; relaxation 1.6; cap 10000; residual tolerance 1e-9; no bounds.',
               reconstruction_rule='Round all 21 numerical coordinates once, denominator<=10^9; apply saved invertible scales and rational affine lift; no repair or search.')
    save('before_single_numerical_run')
    if failures:
        raise SystemExit('Stop before solve: scaling/rank check failed')
    print('Single reduced proposal: cap',CAP,'affine map',M.shape,'singular range',float(singular[-1]),float(singular[0]),flush=True)
    def project(v):
        w = v.copy()
        w[:130] = np.maximum(w[:130],0)
        for start,d in layouts:
            if d==0:
                continue
            if d==1:
                w[start] = max(w[start],0)
            else:
                block = w[start:start+d*d].reshape(d,d)
                eig,basis = np.linalg.eigh((block+block.T)/2)
                w[start:start+d*d] = ((basis*np.maximum(eig,0))@basis.T).ravel()
        return w
    dual = np.zeros(len(offset))
    cone = project(offset)
    trace = []
    status = 'ITERATION_CAP'
    for iteration in range(1,CAP+1):
        x = pinv@(cone-dual-offset)
        affine = offset+M@x
        relaxed = 1.6*affine-0.6*cone
        newcone = project(relaxed+dual)
        dual += relaxed-newcone
        primal = float(np.linalg.norm(affine-newcone))
        dualres = float(np.linalg.norm(M.T@(newcone-cone)))
        cone = newcone
        if iteration==1 or iteration%1000==0:
            trace.append({'iteration':iteration,'primal_residual':primal,'dual_residual':dualres})
            print('iteration',iteration,'primal',format(primal,'.6g'),'dual',format(dualres,'.6g'),flush=True)
        if not np.all(np.isfinite(x)):
            status = 'NONFINITE_PROPOSAL'
            break
        if primal<1e-9 and dualres<1e-9:
            status = 'APPROXIMATE_PROPOSAL'
            break
    residual = affine-project(affine)
    out['proposal'] = {'status':status,'iterations':iteration,'trace':trace,'x':x.tolist(),
                       'affine':affine.tolist(),'cone':cone.tolist(),'dual_iterate':dual.tolist(),
                       'cone_projection_residual':residual.tolist(),'cone_distance':float(np.linalg.norm(residual)),
                       'primal_residual':primal,'dual_residual':dualres}
    save('single_proposal_saved_before_one_reconstruction')
    if not np.all(np.isfinite(x)):
        out['summary'] = {'verdict':'INCONCLUSIVE','reason':status,'reconstructions':0,'runs':1}
        save('completed')
        return
    rounded = [F(float(v)).limit_denominator(10**9) for v in x]
    reduced = [F(1)]+[t*v for t,v in zip(scales,rounded)]
    lifted = [dot(r,reduced) for r in L]
    q,z = lifted[:4],lifted[4:]
    point = q+[s]
    factors = [dot(f,q) for f in domain]
    raw = [p8*v/F(C(8,r)*C(60,r)*C(8,qq)*C(948,qq)) for (r,qq),v in zip(free,z)]
    bounds,slacks,rawslacks,block_evidence = [],[],[],[]
    for k,m in enumerate(src['modes']):
        a,b = divmod(k,9)
        norm = p8*C(68-2*a,8-a)*C(956-2*b,8-b)
        cross = [dot(r,point) for r in dec(m['source_cross'])]
        inverse = [dot(r,point) for r in dec(m['inverse_affine'])]
        check('original_candidate_range_'+str(k), [dot(r,inverse) for r in dec(m['source_base'])] == cross)
        bound = dot([F(*v) for v in m['forced']],point)-F(*m['anchor'])-dot(cross,inverse)/norm
        slack = bound-dot(A[k],z)
        rawslack = sum((beta(68,8,8,a,8-r)*beta(956,8,8,b,8-qq)*v for (r,qq),v in zip(free,raw)),F(0))+norm*bound
        check('original_raw_scaling_'+str(k), rawslack==norm*slack)
        op = original_pencils[k]
        block = [[sum((p[i][j]*v for p,v in zip(op,lifted)),F(0)) for j in range(len(op[0]))] for i in range(len(op[0]))]
        ms = minors(block)
        block_evidence.append({'mode':k,'original_normalized_block':block,'principal_minors':ms,
                               'negative_minor_indices':[h for h,r in enumerate(ms) if r['determinant']<0]})
        bounds.append(bound)
        slacks.append(slack)
        rawslacks.append(rawslack)
    eqres = [dot(r,lifted) for r in constraints]
    check('all_28_original_selected_equalities', not any(eqres) and all(slacks[i]==0 for i in eq['selected_modes']))
    check('candidate_reverse_lift', [dot(r,lifted) for r in reverse]==reduced)
    badf=[i for i,v in enumerate(factors) if v<0]
    badz=[i for i,v in enumerate(z) if v<0]
    badm=[i for i,v in enumerate(slacks) if v<0]
    badblocks=[r['mode'] for r in block_evidence if r['negative_minor_indices']]
    check('full_original_block_psd_matches_all_modes', badblocks==badm)
    out['reconstruction'] = {'passes':1,'rounded_numerical_coordinates':rounded,'reduced_coordinates':reduced,
                             'lifted_coordinates':lifted,'q':q,'point':point,'z':z,'h':reduced[4:],
                             'raw_moments':raw,'domain_factors':factors,'bounds':bounds,
                             'mode_slacks':slacks,'raw_schur_slacks':rawslacks,'selected_equality_residuals':eqres,
                             'negative_domain_rows':badf,'negative_moment_indices':badz,'negative_modes':badm,
                             'original_blocks':block_evidence,'negative_original_blocks':badblocks,
                             'required_minimum':0,'domain_minimum':min(factors),'moment_minimum':min(z),'mode_minimum':min(slacks)}
    verdict = 'RATIONAL_FEASIBLE_WITNESS' if not (failures or badf or badz or badm or badblocks) else 'INCONCLUSIVE'
    out['summary'] = {'verdict':verdict,'checks':len(checks),'model_failures':len(failures),
                      'variables_before':48,'variables_after':21,'retained_size_before':140,'retained_size_after':112,
                      'domain_rows':85,'moment_signs':45,'modes':81,'selected_equalities':28,
                      'iterations':iteration,'cap':CAP,'numerical_runs':1,'exact_reconstruction_passes':1,
                      'cone_distance':float(np.linalg.norm(residual)),'required_exact_violation':0,
                      'negative_domain_rows':len(badf),'negative_moments':len(badz),'negative_modes':len(badm),
                      'negative_original_blocks':len(badblocks),'original_principal_minors':sum(len(r['principal_minors']) for r in block_evidence),
                      'full_domain_feasibility_decided':verdict=='RATIONAL_FEASIBLE_WITNESS'}
    save('completed')
    print(out['summary'],flush=True)
    print('Failed rows:',{'domain':badf,'moments':badz,'modes':badm},flush=True)
    print('Full certificate:',OUT.relative_to(NB),flush=True)
    if failures:
        raise SystemExit(1)


if __name__=='__main__':
    main()
