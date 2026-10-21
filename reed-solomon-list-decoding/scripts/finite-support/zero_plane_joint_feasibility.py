"""One capped joint affine-LMI proposal, then one original-row exact check.

NumPy ADMM supplies no proof. Exact Fraction data and failed residuals are saved.
No parameter box, point scan, extra dependency, or repeated optimization run.
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
OUT = ROOT/'zero-plane-joint-feasibility-results.json'
CAP = 10000


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a, b in zip(x, y)), F(0))


def decode(x):
    return [[F(*v) for v in r] for r in x]


def mm(A, B):
    return [[dot(r, c) for c in zip(*B)] for r in A]


def main():
    names = ['zero-plane-positive-mode-compatibility-results.json',
             'zero-plane-positive-mode-compatibility-verification.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'fully-cancelling-separator-family-results.json',
             'fully-cancelling-separator-family-verification.json',
             'eight-common-column-joint-completion-critical-audit.json',
             'eight-distance-full-base-kernel-results.json']
    paths = [ROOT/n for n in names]
    eq, eqv, audit, source, ver, a82, col = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []
    out = {'iteration_cap_before_solve': CAP, 'numerical_runs_allowed': 1,
           'exact_reconstruction_passes_allowed': 1,
           'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    def save(stage):
        out.update(stage=stage, checks=checks, failures=failures)
        OUT.write_text(json.dumps(enc(out), indent=2)+'\n')

    for name, obj in zip(names, [eq, eqv, audit, source, ver, a82, col]):
        check('clean_'+name, not obj['failures'])
        for rel, digest in obj.get('input_hashes', {}).items():
            check('binding_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == digest)
    p8 = F(16792471, 1181138102168120460)
    s = F(*eq['stationary_t78'])
    free = [(r, q) for r, q in it.product(range(9), repeat=2) if r+q >= 8]
    family = [[F(*v)]+[F(*x) for x in row] for v, row in zip(col['affine']['intercept'], col['affine']['slopes'])]
    check('original_full_domain', enc(family) == audit['family'] == source['domain'])
    domain = [[f[0]+s*f[4]]+f[1:4] for f in family]
    check('plane_85_original_rows', len(domain) == 85 and enc(domain) == eq['domain'] == eqv['domain'])
    check('same_full_affine_column', source['affine_column'] == audit['affine_column'])
    # Check every original column-compatibility coefficient, not a preview.
    for k, (r, b) in enumerate(zip(col['equations'], col['rhs'])):
        check('original_kernel_equation_'+str(k),
              [sum(F(*v)*f[j] for v, f in zip(r, family)) for j in range(5)] == [F(*b)]+[F(0)]*4)
    kernels = source['weighted_kernel_residuals']
    check('whole_weighted_kernel_contract', kernels == audit['weighted_kernel_residuals'] and
          len(kernels) == 90 and not any(F(*v) for row in kernels for v in row))
    check('all_full_keys_and_presentations', len(audit['records']) == 500 and
          sum(len(r['presentations']) for r in ver['records']) == 3000)
    for k, (r, v) in enumerate(zip(audit['records'], ver['records'])):
        check('whole_key_'+str(k), r['type'] == v['type'] and r['key'] == v['key'] and r['affine'] == v['affine'])
    A = []
    blocks = []
    quadratics = []
    for k, m in enumerate(audit['modes']):
        a, b = divmod(k, 9)
        D = C(68-2*a, 8-a)*C(956-2*b, 8-b)
        norm = p8*D
        row = [-F(beta(68, 8, 8, a, 8-r)*beta(956, 8, 8, b, 8-q),
                  D*C(8, r)*C(60, r)*C(8, q)*C(948, q)) for r, q in free]
        check('original_beta_row_'+str(k), enc(row) == m['row'] == eq['full_matrix'][k] == a82['matrix'][k])
        A.append(row)
        B = [[v/norm for v in r] for r in decode(m['source_base'])]
        cross5 = [[v/norm for v in r] for r in decode(m['source_cross'])]
        cross = [[r[0]+s*r[4]]+r[1:4] for r in cross5]
        forced = [F(*v) for v in m['forced']]
        forced[0] -= F(*m['anchor'])
        fixed = [forced[0]+s*forced[4]]+forced[1:4]
        inv = decode(m['inverse_affine'])
        check('original_whole_range_'+str(k), mm(decode(m['source_base']), inv) == decode(m['source_cross']) if B else not cross)
        cost = [[sum((cross5[h][i]*inv[h][j] for h in range(len(B))), F(0)) for j in range(5)] for i in range(5)]
        Q = [[-v for v in r] for r in cost]
        Q[0][0] += forced[0]
        for j in range(1, 5):
            Q[0][j] += forced[j]/2
            Q[j][0] += forced[j]/2
        check('full_anchor_quadratic_'+str(k), enc(Q) == m['quadratic'] == eq['full_quadratics'][k])
        quadratics.append(Q)
        # Exact invertible simultaneous row/column eliminations on the fixed
        # base. A zero row is discarded only after the transformed cross is
        # identically zero on the WHOLE plane. No numerical kernel is used.
        R = [r[:] for r in B]
        T = [[F(i == j) for j in range(len(B))] for i in range(len(B))]
        for j in range(len(B)):
            check('nonnegative_fixed_pivot_'+str((k, j)), R[j][j] >= 0)
            if R[j][j] == 0:
                check('fixed_zero_row_'+str((k, j)), not any(R[j]))
                continue
            for i in range(j+1, len(B)):
                v = R[i][j]/R[j][j]
                T[i] = [x-v*y for x, y in zip(T[i], T[j])]
                for h in range(len(B)):
                    R[i][h] -= v*R[j][h]
                for h in range(len(B)):
                    R[h][i] -= v*R[h][j]
        TC = mm(T, cross) if B else []
        check('exact_base_congruence_'+str(k), mm(mm(T, B), list(map(list, zip(*T)))) == R if B else not R)
        check('invertible_unit_triangular_'+str(k), all(T[i][i] == 1 and all(T[i][j] == 0 for j in range(i+1, len(T))) for i in range(len(T))))
        check('diagonal_fixed_base_'+str(k), all(R[i][j] == 0 for i in range(len(R)) for j in range(len(R)) if i != j))
        active = [i for i in range(len(B)) if R[i][i] > 0]
        check('all_discarded_cross_zero_'+str(k), all(not any(TC[i]) for i in range(len(B)) if i not in active))
        blocks.append({'mode': [a, b], 'original_base': B, 'original_cross_plane': cross,
                       'congruence': T, 'diagonalized_base': R, 'transformed_cross_plane': TC,
                       'retained_indices': active, 'positive_diagonal': [R[i][i] for i in active],
                       'cross_plane': [TC[i] for i in active], 'fixed_plane': fixed, 'row': row,
                       'positive_original_norm': norm})
    E, P, N = decode(eq['original_equalities']), decode(eq['particular_coefficients']), decode(eq['right_kernel'])
    check('all_equality_particular_coefficients', mm(E, P) == decode(eq['rhs_coefficients']))
    check('all_18_homogeneous_directions', mm(E, N) == [[F(0)]*18 for _ in E])
    out.update(stationary_t78=s, free=free, domain=domain, blocks=blocks,
               full_quadratics=quadratics, matrix=A, selected_modes=eq['selected_modes'],
               particular=P, kernel=N, nonpivots=eq['nonpivot_columns'])
    save('exact_original_model_and_congruences_saved')
    print('Exact model: 3 column parameters, 45 moments, 85 domain rows, 81 modes; checks', len(checks), 'failures', failures, flush=True)
    if failures:
        raise SystemExit('Model construction failed before numerical solve')
    # Invertible variable and block scaling only. It imposes no bounds.
    qscale = F(1, 10**11)
    preliminary = []
    for block in blocks:
        f = block['fixed_plane']
        size = abs(f[0])+sum(abs(v*qscale) for v in f[1:])
        for d, c in zip(block['positive_diagonal'], block['cross_plane']):
            size += (abs(c[0])+sum(abs(v*qscale) for v in c[1:]))**2/d
        preliminary.append(size or F(1))
    zscale = [1/max(abs(A[i][j])/preliminary[i] for i in range(81)) for j in range(45)]
    lower = []
    constant = []
    for f in domain:
        v = [f[0]]+[x*qscale for x in f[1:]]
        scale = max(map(abs, v)) or F(1)
        constant.append(float(v[0]/scale))
        lower.append([float(x/scale) for x in v[1:]]+[0.0]*45)
    for j in range(45):
        constant.append(0.0)
        lower.append([0.0]*3+[float(k == j) for k in range(45)])
    layouts = []
    blockscales = []
    for k, block in enumerate(blocks):
        size = max([preliminary[k]]+[abs(v*t) for v, t in zip(A[k], zscale)])
        blockscales.append(size)
        d = len(block['positive_diagonal'])+1
        start = len(constant)
        for i in range(d):
            for j in range(d):
                v = np.zeros(48)
                if i == j == d-1:
                    c = float(block['fixed_plane'][0]/size)
                    v[:3] = [float(x*qscale/size) for x in block['fixed_plane'][1:]]
                    v[3:] = [-float(x*t/size) for x, t in zip(A[k], zscale)]
                elif i == d-1 or j == d-1:
                    h = min(i, j)
                    den = math.sqrt(float(block['positive_diagonal'][h]*size))
                    c = float(block['cross_plane'][h][0])/den
                    v[:3] = [float(x*qscale)/den for x in block['cross_plane'][h][1:]]
                else:
                    c = float(i == j)
                constant.append(c)
                lower.append(v)
        layouts.append([start, d])
    M = np.asarray(lower)
    offset = np.asarray(constant)
    U, singular, Vt = np.linalg.svd(M, full_matrices=False)
    cutoff = singular[0]*1e-13
    pinv = (Vt.T*np.where(singular > cutoff, 1/singular, 0))@U.T
    out.update(numerical_scaling={'qscale': qscale, 'zscale': zscale, 'blockscales': blockscales,
                                  'domain_rows': 85, 'sign_rows': 45, 'layouts': layouts,
                                  'M': M.tolist(), 'offset': offset.tolist(), 'singular_values': singular.tolist(),
                                  'pseudoinverse_cutoff': cutoff, 'retained_rank': int(sum(singular > cutoff))},
               numerical_method='single NumPy product-cone ADMM, relaxation 1.6, tolerance 1e-9, no variable caps',
               reconstruction_rule='Round scaled q and nonpivot z once to denominator <=10^9; use exact P(q)+N*h; check every original row.')
    save('before_single_numerical_run')
    print('Single conic run: cap', CAP, '; affine map', M.shape, '; retained numerical rank', sum(singular > cutoff), flush=True)

    def project(v):
        w = v.copy()
        w[:130] = np.maximum(w[:130], 0)
        for start, d in layouts:
            if d == 1:
                w[start] = max(w[start], 0)
            else:
                B = w[start:start+d*d].reshape(d, d)
                eigen, basis = np.linalg.eigh((B+B.T)/2)
                w[start:start+d*d] = ((basis*np.maximum(eigen, 0))@basis.T).ravel()
        return w

    dual = np.zeros(len(offset))
    cone = project(offset)
    trace = []
    status = 'ITERATION_CAP'
    x = np.zeros(48)
    for iteration in range(1, CAP+1):
        x = pinv@(cone-dual-offset)
        affine = offset+M@x
        relaxed = 1.6*affine-0.6*cone
        newcone = project(relaxed+dual)
        dual += relaxed-newcone
        primal = float(np.linalg.norm(affine-newcone))
        dualres = float(np.linalg.norm(M.T@(newcone-cone)))
        cone = newcone
        if iteration == 1 or iteration % 1000 == 0:
            trace.append({'iteration': iteration, 'primal_residual': primal, 'dual_residual': dualres})
            print('iteration', iteration, 'primal', format(primal, '.6g'), 'dual', format(dualres, '.6g'), flush=True)
        if not np.all(np.isfinite(x)):
            status = 'NONFINITE_PROPOSAL'
            break
        if primal < 1e-9 and dualres < 1e-9:
            status = 'APPROXIMATE_PROPOSAL'
            break
    violation = affine-project(affine)
    out['proposal'] = {'status': status, 'iterations': iteration, 'trace': trace,
                       'x': x.tolist(), 'affine': affine.tolist(), 'cone': cone.tolist(),
                       'dual_iterate': dual.tolist(), 'cone_projection_residual': violation.tolist(),
                       'primal_residual': primal, 'dual_residual': dualres,
                       'cone_distance': float(np.linalg.norm(violation)),
                       'domain_minimum_scaled': float(min(affine[:85])),
                       'moment_minimum_scaled': float(min(affine[85:130]))}
    save('single_numerical_proposal_saved')
    if not np.all(np.isfinite(x)):
        out['summary'] = {'verdict': 'INCONCLUSIVE', 'reason': status, 'exact_reconstruction_passes': 0}
        save('completed')
        return
    # One exact reconstruction. Nonpivot coordinates are precisely h; P has
    # zero rows there. No fixed-point LP or second numerical run is made.
    q = [F(1)]+[qscale*F(float(v)).limit_denominator(10**9) for v in x[:3]]
    mon = [q[i]*q[j] for i, j in eq['monomials']]
    h = [zscale[j]*F(float(x[3+j])).limit_denominator(10**9) for j in eq['nonpivot_columns']]
    z = [dot(p, mon)+dot(n, h) for p, n in zip(P, N)]
    point = q+[s]
    bounds = [dot(point, [dot(row, point) for row in Q]) for Q in quadratics]
    slacks = [b-dot(row, z) for b, row in zip(bounds, A)]
    factors = [dot(f, q) for f in domain]
    raw = [p8*v/F(C(8, r)*C(60, r)*C(8, qq)*C(948, qq)) for (r, qq), v in zip(free, z)]
    rawslacks = []
    for k in range(81):
        a, b = divmod(k, 9)
        rawslacks.append(sum(beta(68, 8, 8, a, 8-r)*beta(956, 8, 8, b, 8-qq)*v for (r, qq), v in zip(free, raw))
                         +blocks[k]['positive_original_norm']*bounds[k])
    check('all_original_raw_slack_scalings', rawslacks == [m['positive_original_norm']*v for m, v in zip(blocks, slacks)])
    check('all_28_selected_exact_equalities', all(slacks[i] == 0 for i in eq['selected_modes']))
    badf = [i for i, v in enumerate(factors) if v < 0]
    badz = [i for i, v in enumerate(z) if v < 0]
    badm = [i for i, v in enumerate(slacks) if v < 0]
    # Failed candidate inequalities are evidence, not model-check failures.
    out['reconstruction'] = {'passes': 1, 'q': q, 'point': point, 'h': h, 'z': z, 'raw_moments': raw,
                             'bounds': bounds, 'domain_factors': factors, 'mode_slacks': slacks, 'raw_schur_slacks': rawslacks,
                             'negative_domain_rows': badf, 'negative_moment_indices': badz, 'negative_modes': badm,
                             'domain_minimum': min(factors), 'moment_minimum': min(z), 'mode_minimum': min(slacks),
                             'required_minimum': 0, 'all_selected_equalities_exact': all(slacks[i] == 0 for i in eq['selected_modes'])}
    verdict = 'RATIONAL_FEASIBLE_WITNESS' if not (failures or badf or badz or badm) else 'INCONCLUSIVE'
    out['summary'] = {'verdict': verdict, 'checks': len(checks), 'model_failures': len(failures),
                      'numerical_status': status, 'iterations': iteration, 'cap': CAP,
                      'numerical_cone_distance': float(np.linalg.norm(violation)), 'required_exact_violation': 0,
                      'negative_domain_rows': len(badf), 'negative_moments': len(badz), 'negative_modes': len(badm),
                      'selected_equalities_exact': all(slacks[i] == 0 for i in eq['selected_modes']),
                      'numerical_runs': 1, 'exact_reconstruction_passes': 1,
                      'full_domain_feasibility_decided': verdict == 'RATIONAL_FEASIBLE_WITNESS'}
    save('completed')
    print(out['summary'], flush=True)
    print('Exact failed candidate rows:', {'domain': badf, 'moments': badz, 'modes': badm}, flush=True)
    print('Full evidence:', OUT.relative_to(NB), flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
