"""Finite-state necessary Schur relaxation. Floating output is NOT a proof.

Run from riemann: OPENBLAS_NUM_THREADS=1 python3 scripts/coupled-flux/rational_schur_probe.py
All accelerations are retained through 3x3 LMIs at finitely many states.
The original family has 56 variables with ten quadratic-storage gauges.
"""
from pathlib import Path
import argparse
import json
import time
import numpy as np
from rational_sos_probe import spectral_matrix, monomials

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--states', type=int, default=192)
    parser.add_argument('--suffix', default='')
    args = parser.parse_args()
    started = time.monotonic()
    k_rat, _ = spectral_matrix()
    scales = np.array([1, 4, 8, 1, 4, 8])
    k = np.array([[float(a) for a in row] for row in k_rat]) / scales[:, None] / scales[None, :]
    perm = [0, 1, 3, 4, 2, 5]
    kr = k[np.ix_(perm, perm)]
    lw = np.linalg.cholesky(kr[:4, :4])
    mean = np.linalg.solve(kr[:4, :4], kr[:4, 4:]).T
    residual = kr[4:, 4:] - mean @ kr[:4, 4:]
    la = np.linalg.cholesky(residual)
    transform = np.zeros((6, 6))
    transform[:4, :4] = lw
    transform[4:, :4] = mean @ lw
    transform[4:, 4:] = la
    flow = transform[[1, 4, 3, 5], :]
    flow = np.linalg.solve(lw, flow)
    qmat = lw.T @ np.diag([.5, 6, .5, 6]) @ lw
    rng = np.random.default_rng(59402)
    n = args.states
    s = rng.normal(size=(n, 4))
    # Half the directions also explore q-small regions; no directions are
    # discarded on the basis of their numerical conditioning.
    s[n//2:] = np.linalg.solve(lw, rng.normal(size=(n-n//2, 4)).T).T
    s /= np.linalg.norm(s, axis=1)[:, None]
    # Save rational physical states, not rounded normalized accelerations.
    w_int = np.rint((s @ lw.T)*10**12).astype(np.int64)
    w = w_int / 10**12
    s = np.linalg.solve(lw, w.T).T
    p_basis = np.array(monomials(4, 4))
    powers = s[:, None, :] ** p_basis[None, :, :]
    pvals = np.prod(powers, axis=2)
    gradients = np.zeros((n, 35, 4))
    for i in range(4):
        e = p_basis.copy()
        e[:, i] = np.maximum(e[:, i]-1, 0)
        gradients[:, :, i] = np.prod(s[:, None, :]**e[None, :, :], axis=2)*p_basis[None, :, i]
    q = np.einsum('ni,ij,nj->n', s, qmat, s)
    qgrad = 2*s @ qmat
    gv = gradients/q[:, None, None] - pvals[:, :, None]*qgrad[:, None, :]/q[:, None, None]**2
    dv0 = np.einsum('npi,ni->np', gv, s @ flow[:, :4].T)
    dva = np.einsum('npi,ij->npj', gv, flow[:, 4:])
    h_basis = [(i, j) for i in range(6) for j in range(i, 6)]
    amap = np.zeros((n, 3, 3, 56))
    cost = np.zeros(56)
    for p, (i, j) in enumerate(h_basis):
        hh = np.zeros((6, 6)); hh[i, j] = hh[j, i] = 1
        amap[:, 0, 0, p] = np.einsum('ni,ij,nj->n', s, hh[:4, :4], s)
        amap[:, 1:, 0, p] = s @ hh[4:, :4].T
        amap[:, 0, 1:, p] = amap[:, 1:, 0, p]
        amap[:, 1:, 1:, p] = hh[4:, 4:]
        cost[p] = np.trace(hh)
    amap[:, 0, 0, 21:] = -dv0
    amap[:, 0, 1:, 21:] = -.5*dva.transpose(0, 2, 1)
    amap[:, 1:, 0, 21:] = amap[:, 0, 1:, 21:]
    bmat = np.zeros((n, 3, 3))
    bmat[:, 0, 0] = w[:, 0]*(s @ transform[4, :4]) - w[:, 1]**2
    bmat[:, 0, 1:] = .5*w[:, 0, None]*la[0, :]
    bmat[:, 1:, 0] = bmat[:, 0, 1:]
    amap = np.concatenate([amap, amap], axis=0)
    constant = np.concatenate([np.zeros_like(bmat), -bmat], axis=0)
    flat = amap.reshape(-1, 56)
    column_scale = 1/np.maximum(np.linalg.norm(flat, axis=0), 1e-30)
    u, singular, vt = np.linalg.svd(flat*column_scale, full_matrices=False)
    rank = 46  # exactly ten quadratic-storage gauges; do not infer rank by cutoff
    if singular[45] < 1e-10 or singular[46] > 1e-9:
        raise RuntimeError(f'Unexpected gauge singular values: {singular[45:47]}')
    change = column_scale[:, None]*vt[:rank].T/singular[:rank]
    aa = (flat @ change).reshape(2*n, 3, 3, rank)
    cc = cost @ change
    init = np.zeros(56)
    for p, (i, j) in enumerate(h_basis):
        if i == j: init[p] = 1
    theta = singular[:rank]*(vt[:rank] @ (init/column_scale))
    records = []
    stable = None
    for total_mu in [.1, .02, .004, .0008, .00016, .000032, .0000064, .00000128, .000000256]:
        mu = total_mu/(2*n)
        for iteration in range(80):
            mats = np.einsum('mijp,p->mij', aa, theta)+constant
            ev = np.linalg.eigvalsh(mats)
            if ev.min() <= 0: raise RuntimeError('Lost interior')
            inv = np.linalg.inv(mats)
            grad = cc-mu*np.einsum('mij,mjip->p', inv, aa)
            prod = np.einsum('mij,mjkp->mikp', inv, aa)
            hess = mu*np.einsum('mijp,mjiq->pq', prod, prod)
            step = np.linalg.solve(hess, -grad)
            decrement = -grad @ step
            if decrement < 0: break
            if decrement < 1e-22: break
            old = cc @ theta-mu*np.log(ev).sum()
            rate = 1.
            for backtrack in range(60):
                trial = theta+rate*step
                e = np.linalg.eigvalsh(np.einsum('mijp,p->mij', aa, trial)+constant)
                if e.min() > 0 and cc @ trial-mu*np.log(e).sum() <= old+.01*rate*(grad @ step):
                    theta = trial
                    break
                rate *= .5
            else: raise RuntimeError('Line search failed')
        dual = mu*inv
        record = dict(total_mu=total_mu, iterations=iteration+1, primal_cost=float(cc @ theta),
                      dual_value=float(-np.sum(dual*constant)), min_schur_eigenvalue=float(ev.min()),
                      reduced_dual_residual=float(np.linalg.norm(grad)), decrement=float(decrement))
        records.append(record)
        if np.linalg.norm(grad) < 1e-7 and (stable is None or record['dual_value'] > stable[0]['dual_value']):
            stable = (record.copy(), theta.copy(), dual.copy())
        if decrement < 0: break
    if stable is None:
        raise RuntimeError('No numerically stationary dual iterate')
    selected_record, theta, dual = stable
    variables = change @ theta
    dual_residual = cost-np.einsum('mij,mjip->p', dual, amap)
    data = dict(kind='FLOATING NECESSARY RELAXATION; NOT A GLOBAL OR LOWER-BOUND CERTIFICATE',
                states=n, threshold='1/288', required_cost=float(1/288), records=records, selected_record=selected_record,
                singular_values=singular.tolist(), covariance_eigenvalues=np.linalg.eigvalsh(k).tolist(),
                conditional_acceleration_covariance=residual.tolist(), state_denominator_min=float(q.min()),
                original_dual_residual=float(np.linalg.norm(dual_residual)),
                variables=variables.tolist(), transform=transform.tolist(), state_integer_denominator=10**12,
                state_integers=w_int.tolist(), dual_matrices=dual.tolist(),
                failures=['Finite states do not prove global positivity.',
                          'Floating dual residuals do not prove a family-wide lower bound.',
                          'Covariance scaling and gauge removal are numerical in this probe.'],
                elapsed_seconds=time.monotonic()-started)
    stem = 'rational_schur_probe'+args.suffix
    path = ROOT/(stem+'.json')
    path.write_text(json.dumps(data, indent=2)+'\n')
    np.savez_compressed(ROOT/(stem+'_maps.npz'), amap=amap, constant=constant, cost=cost,
                        change=change, theta=theta, transform=transform, dual=dual)
    print(json.dumps({key:data[key] for key in ['kind','states','required_cost','original_dual_residual','failures','elapsed_seconds']}, indent=2))
    print(json.dumps(selected_record, indent=2))
    print('Full artifacts:', path, ROOT/(stem+'_maps.npz'))


if __name__ == '__main__':
    main()
