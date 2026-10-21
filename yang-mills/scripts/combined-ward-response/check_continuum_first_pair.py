"""L080 continuum tensor diagnostic; retained numerics are NOT enclosures.

Save complete factors, quadrature rules, term values and failures. The
analytic exterior-tail formula is L081; refinement does not certify the
spatial/time quadrature or floating arithmetic of the retained tensor.
"""
import argparse
import json
from itertools import combinations
from pathlib import Path

import numpy as np


ROOT = Path(__file__).parent


def rule(panels, degree):
    z, w = np.polynomial.legendre.leggauss(degree)
    return (np.concatenate([(a+b)/2+(b-a)*z/2 for a, b in panels]),
            np.concatenate([(b-a)*w/2 for a, b in panels]))


def coefficients(x):
    r = np.zeros_like(x)
    rp = np.zeros_like(x)
    rpp = np.zeros_like(x)
    r[np.abs(x) <= 2.5] = 1
    m = (np.abs(x) > 2.5) & (np.abs(x) < 3)
    y = x[m]
    a, b = 9-y*y, y*y-6.25
    # rho=logistic(1/b-1/a); stable values include flat endpoint collars.
    h = 1/b-1/a
    pos = h >= 0
    p = np.empty_like(h)
    p[pos] = 1/(1+np.exp(-h[pos]))
    eh = np.exp(h[~pos])
    p[~pos] = eh/(1+eh)
    hp = -2*y*(1/b**2+1/a**2)
    hpp = -2*(1/b**2+1/a**2)+8*y*y*(1/b**3-1/a**3)
    r[m] = p
    rp[m] = p*(1-p)*hp
    rpp[m] = p*(1-p)*(hpp+(1-2*p)*hp**2)
    return dict(r=r, rp=rp, rpp=rpp, f=x*r, fp=r+x*rp,
                fpp=2*rp+x*rpp, hf=(x+4)*x*r)


def evaluate(k, space_degree, time_degree, label):
    x, wx = rule([(-3, -2.5), (-2.5, 2.5), (2.5, 3)], space_degree)
    co = coefficients(x)
    frequencies = {'E': np.arange(k+1)*np.pi/8, 'V': np.arange(1, k+1)*np.pi/8}
    basis = {}
    for t in ('E', 'V'):
        f = frequencies[t]
        angles = np.outer(x+4, f)
        if t == 'E':
            b, db = np.cos(angles)/2, -np.sin(angles)*f/2
            b[:, 0] = 1/np.sqrt(8)
            prefix = np.empty_like(b)
            prefix[:, 0] = (x+4)/np.sqrt(8)
            prefix[:, 1:] = np.sin(angles[:, 1:])/(2*f[None, 1:])
            top = np.cos(8*f)/2
            top[0] = 1/np.sqrt(8)
        else:
            b, db = np.sin(angles)/2, np.cos(angles)*f/2
            top = np.cos(8*f)*f/2
        basis[t, 'b'] = b
        basis[t, 'd'] = db
        basis[t, 'top'] = np.broadcast_to(top, b.shape)
        if t == 'E':
            basis[t, 'prefix'] = prefix
    types = lambda alpha: tuple('E' if j == alpha else 'V' for j in range(4))
    ordinary = lambda alpha: [(t, 'b') for t in types(alpha)]
    archive = dict(x=x, spatial_weights=wx)
    archive.update({f'coefficient_{a}': b for a, b in co.items()})
    archive.update({f'basis_{a}_{b}': c for (a, b), c in basis.items()})
    cache = {}

    def integral(a, weight, b):
        key = a, weight, b
        if key not in cache:
            cache[key] = basis[a].T @ ((wx*co[weight])[:, None]*basis[b])
        return cache[key]

    u = {0: [(1, ['f', 'r', 'fp', 'r'])],
         2: [(-1, ['fp', 'r', 'f', 'r'])], 1: [], 3: []}
    derivative = {'r': 'rp', 'f': 'fp', 'fp': 'fpp'}

    def deriv(terms, axis):
        answer = []
        for sign, factors in terms:
            factors = list(factors)
            factors[axis] = derivative[factors[axis]]
            answer.append((sign, factors))
        return answer

    w = {mu: deriv(u[mu], mu) for mu in range(4)}
    shear = {(mu, nu): deriv(u[nu], mu)+deriv(u[mu], nu)
             for mu, nu in combinations(range(4), 2)}

    def circulation(mu, nu):
        if mu > nu:
            return [(a, -s, b) for a, s, b in circulation(nu, mu)]
        answer = []
        for alpha, axis, sign in ((nu, mu, 1), (mu, nu, -1)):
            factors = ordinary(alpha)
            factors[axis] = (types(alpha)[axis], 'd')
            answer.append((alpha, sign, factors))
        return answer

    Q = {3: [], 6: []}

    def add_q(probe, left, right, coeffs, scale):
        for sign, coeff in coeffs:
            for alpha, sl, rows in left:
                for beta, sr, cols in right:
                    mats = [integral(a, c, b) for a, c, b in zip(rows, coeff, cols)]
                    Q[probe].append((alpha, beta, scale*sign*sl*sr, mats))

    for mu, nu in combinations(range(4), 2):
        row = circulation(mu, nu)
        add_q(3, row, row, w[mu]+w[nu], 1)
        for alpha in range(4):
            if alpha in (mu, nu):
                continue
            left, right = circulation(mu, alpha), circulation(nu, alpha)
            add_q(6, left, right, shear[mu, nu], .5)
            add_q(6, right, left, shear[mu, nu], .5)
    M = []
    for mu in (1, 2, 3):
        upper, lifted = [], []
        for alpha in (mu, 0):
            uf, vf = ordinary(alpha), ordinary(alpha)
            uf[0] = (types(alpha)[0], 'top')
            if alpha == mu:
                sign = 1
            else:
                vf[0] = ('E', 'prefix')
                uf[mu] = vf[mu] = ('V', 'd')
                sign = -1
            upper.append((alpha, sign, uf))
            lifted.append((alpha, sign, vf))
        for alpha, sl, rows in upper:
            for beta, sr, cols in lifted:
                mats = [integral(a, c, b) for a, c, b in zip(rows, ['hf', 'r', 'fp', 'r'], cols)]
                M.append((alpha, beta, sl*sr, mats))
    # F=integral_tau^infinity exp(-t Delta)dt, with both inverse factors.
    time_panels = [(0, 1/32)]+[(2.**j, 2.**(j+1)) for j in range(-5, 7)]
    t, wt = rule(time_panels, time_degree)
    t = t+1/16
    heats = {a: np.exp(-np.outer(t, f*f)) for a, f in frequencies.items()}
    archive.update(time_nodes=t, time_weights=wt, **{f'heat_{a}': b for a, b in heats.items()})
    terms = []
    values = {}
    for probe in (3, 6):
        total = 0.
        for im, (alpha, beta, cm, mm) in enumerate(M):
            for iq, (ba, al, cq, qq) in enumerate(Q[probe]):
                if (alpha, beta) != (al, ba):
                    continue
                product = np.ones((len(t), len(t)))
                for j in range(4):
                    # trace M_ab E_b(t) Q_ba E_a(s); s is the first axis.
                    factor = heats[types(alpha)[j]] @ (mm[j]*qq[j].T) @ heats[types(beta)[j]].T
                    product *= factor
                value = float(cm*cq*(wt @ product @ wt))
                total += value
                terms.append(dict(probe=probe, M=im, Q=iq, coefficient=cm*cq, value=value))
        values[probe] = total
    for name, terms_ in [('M', M), ('Q3', Q[3]), ('Q6', Q[6])]:
        for i, (a, b, c, mats) in enumerate(terms_):
            for j, mat in enumerate(mats):
                archive[f'{name}_{i}_{j}'] = mat
    factor_path = ROOT/f'continuum-first-pair-{label}-factors.npz'
    np.savez_compressed(factor_path, **archive)
    # Exact mathematical bound in L081; displayed float is only a preview.
    p_bound = 1296*1155*3/32
    tail_common = 2*(4*12**4)*(16*12**3)*512/(9*k)*np.exp(-9*k*k/1024)
    tails = {3: float(p_bound*3025*tail_common), 6: float(p_bound*820368*tail_common)}
    # Checks exercise constant mode, upper sign, strain identity, heat weights.
    checks = [dict(name='constant_prefix', actual_error=float(np.max(np.abs(basis['E', 'prefix'][:, 0]-(x+4)/np.sqrt(8)))), required_error=1e-14),
              dict(name='positive_upper_derivative_first_vertex_mode', actual_error=float(abs(basis['V', 'top'][0, 0]+np.pi/16)), required_error=1e-14),
              dict(name='rho_parity', actual_error=float(np.max(np.abs(co['r']-co['r'][::-1]))), required_error=1e-12),
              dict(name='rho_prime_parity', actual_error=float(np.max(np.abs(co['rp']+co['rp'][::-1]))), required_error=1e-10),
              dict(name='rho_second_parity', actual_error=float(np.max(np.abs(co['rpp']-co['rpp'][::-1]))), required_error=1e-8)]
    for c in checks:
        c['passed'] = c['actual_error'] <= c['required_error']
    counts = {p: sum(r['probe'] == p for r in terms) for p in (3, 6)}
    if k <= 3:
        # Independent evaluation of the two inverse heat weights by the
        # full finite diagonal spectral formula, rather than a Laplace rule.
        sizes = [int(np.prod([len(frequencies[t]) for t in types(a)])) for a in range(4)]
        cuts = np.cumsum([0, *sizes])
        def assemble(rows):
            dense = np.zeros((cuts[-1], cuts[-1]))
            for a, b, c, mats in rows:
                block = np.ones((1, 1))
                for mat in mats:
                    block = np.kron(block, mat)
                dense[cuts[a]:cuts[a+1], cuts[b]:cuts[b+1]] += c*block
            return dense
        lambdas = []
        for alpha in range(4):
            axes = np.meshgrid(*[frequencies[t]**2 for t in types(alpha)], indexing='ij')
            lambdas.append(sum(axes).ravel())
        lam = np.concatenate(lambdas)
        full_f = np.exp(-lam/16)/lam
        md = assemble(M)
        for p in (3, 6):
            qd = assemble(Q[p])
            direct = float(np.sum(md*qd.T*full_f[:, None]*full_f[None, :]))
            err = abs(direct-values[p])
            bound = 2e-10*max(1., abs(direct))
            checks.append(dict(name=f'full_modal_inverse_vs_double_time_probe_{p}',
                               actual_error=err, required_error=bound,
                               direct_modal_value=direct, double_time_value=values[p],
                               passed=err <= bound))
    return dict(K=k, spatial_degree=space_degree, time_degree=time_degree,
                continuum_values_preview=values, tensor_counts=dict(M=len(M), Q3=len(Q[3]), Q6=len(Q[6]), contractions=counts),
                exterior_tail_bound_preview=tails, analytic_tail_reference='lemmas/L081-continuum-diagnostic-tensor-and-tail.md',
                checks=checks, terms=terms, factors_path=str(factor_path.relative_to(ROOT.parent.parent)),
                missing_error_bounds=['spatial quadrature', 'retained time quadrature', 'floating arithmetic'],
                qualification='No continuum sign or nonvanishing is certified by these numerical values')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cutoff', type=int, required=True)
    parser.add_argument('--space-degree', type=int, required=True)
    parser.add_argument('--time-degree', type=int, required=True)
    parser.add_argument('--label', required=True)
    args = parser.parse_args()
    result = evaluate(args.cutoff, args.space_degree, args.time_degree, args.label)
    result['failures'] = [c for c in result['checks'] if not c['passed']]
    path = ROOT/f'continuum-first-pair-{args.label}-certificate.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('Retained continuum values (uncertified):', result['continuum_values_preview'])
    print('Analytic exterior tail bound preview:', result['exterior_tail_bound_preview'])
    print('Required total error: less than abs(retained value); actual total error: unbounded')
    print('Normalization/parity check failures:', len(result['failures']))
    print('Full certificate:', path)
    print('Full factors:', result['factors_path'])
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
