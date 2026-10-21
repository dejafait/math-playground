"""L072 at N=24: full tensor Gauss enclosure, no mode truncation.

Integer enclosures for coefficients/bases/heat/rule; L039 midpoint-radius
arithmetic under its explicit IEEE model. All tensor factors and retained
trace terms are saved. A finite diagnostic only, not the original trace.
"""
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import factorial, isqrt
from pathlib import Path
import numpy as np

# Import order is deliberate: sw sets fixed-point precision before sr binds it.
import check_stored_fourier_enclosure as sw
import check_signed_retained_enclosure as sr
ar = sw.arithmetic
I, S = ar.I, ar.S
rat, rec = I.rational, sw.record
N, DEGREE = 24, 20
A = F(8, N)
T0 = F(1, 16)/A**2
ROOT = Path(__file__).parent
OUT = ROOT/'first-pair-retained-enclosure-certificate.json'


def exact(x):
    c = np.asarray(x, dtype=float)
    return c, np.zeros_like(c)


def enclosed(rows):
    obj = np.asarray(rows, dtype=object)
    pairs = np.asarray([sr.midpoint_radius(z) for z in obj.ravel()])
    return pairs[:, 0].reshape(obj.shape), pairs[:, 1].reshape(obj.shape)


def transpose(p):
    return p[0].T, p[1].T


def diag(p):
    return np.diag(p[0]), np.diag(p[1])


def dot(p, q):
    # sr.dot's n<=276 applies to all coordinate products. The final
    # 320-node integral is contracted in <=160-node blocks below.
    return sr.dot(p, q)


def scalar(p, c):
    return sr.multiply(p, enclosed(rat(c)))


def subtract(p, q):
    return sr.add(p, (-q[0], q[1]))


def sqrt_rational(q):
    q = F(q)
    z = isqrt(q.numerator*S*S//q.denominator)
    assert z*z*q.denominator <= q.numerator*S*S < (z+1)**2*q.denominator
    return I(z, z+1)


def rational_record(q):
    q = F(q)
    return dict(numerator=str(q.numerator), denominator=str(q.denominator))


def pair_record(z):
    assert np.asarray(z[0]).size == np.asarray(z[1]).size == 1
    return dict(center_hex=float(z[0]).hex(), radius_hex=float(z[1]).hex())


def main():
    pi = rat(16)*sw.arctan_enclosure(F(1, 5))-rat(4)*sw.arctan_enclosure(F(1, 239))
    @lru_cache(None)
    def trig(k):
        # Every basis angle is an integer multiple of pi/(2N).
        return sw.sin_cos(pi*rat(F(k % (4*N), 2*N)))
    nv, ne = N-1, N
    norm, zero_norm = sqrt_rational(F(2, N)), sqrt_rational(F(1, N))
    basis_raw = {
        'V': [[norm*trig(2*j*k)[0] for k in range(1, N)] for j in range(1, N)],
        'E': [[zero_norm]+[norm*trig((2*j+1)*k)[1] for k in range(1, N)] for j in range(N)]}
    basis = {k: enclosed(v) for k, v in basis_raw.items()}
    lambdas = [rat(0)]+[rat(4)*trig(k)[0]*trig(k)[0] for k in range(1, N)]
    rraw = []
    for j in range(1, N):
        x = F(-4)+j*A
        if abs(x) <= F(5, 2):
            rraw.append(rat(1))
        elif abs(x) >= 3:
            rraw.append(rat(0))
        else:
            x2 = rat(x*x)
            b1 = ar.exp_negative(rat(1)/(rat(9)-x2))
            b2 = ar.exp_negative(rat(1)/(x2-rat(F(25, 4))))
            rraw.append(b1/(b1+b2))
    r = enclosed(rraw)
    f = enclosed([rat(-4+j*A)*v for j, v in enumerate(rraw, 1)])
    h = enclosed([rat(j*A) for j in range(1, N)])
    g = np.zeros((ne, nv)); av = np.zeros((nv, ne))
    for j in range(nv):
        g[j, j] = 1; g[j+1, j] = -1
        av[j, j:j+2] = .5
    G, AV = exact(g), exact(av)
    c = np.zeros((nv, nv))
    for j in range(nv):
        if j+1 < nv: c[j, j+1] = 1/(2*float(A))
        if j: c[j, j-1] = -1/(2*float(A))
    # At N=24 these entries are exactly +/-3/2.
    assert A == F(1, 3)
    C = exact(c)
    cf = dot(C, f)
    ident = {'V': exact(np.eye(nv)), 'E': exact(np.eye(ne))}
    prefix = exact(np.asarray([[int(ell < j) for ell in range(N)] for j in range(1, N)]))
    top = exact(np.eye(N)[-1:])
    ones = exact(np.ones((nv, 1)))
    types = lambda alpha: tuple('E' if j == alpha else 'V' for j in range(4))
    # Every displacement term is (sign, four one-dimensional vectors).
    u = {0: [(1, [f, r, cf, r])], 2: [(-1, [cf, r, f, r])], 1: [], 3: []}
    def derivative(terms, axis):
        out = []
        for sign, factors in terms:
            factors = list(factors); factors[axis] = dot(C, factors[axis])
            out.append((sign, factors))
        return out
    w = {mu: derivative(u[mu], mu) for mu in range(4)}
    shears = {(mu, nu): derivative(u[nu], mu)+derivative(u[mu], nu)
              for mu, nu in combinations(range(4), 2)}
    # Include even algebraically canceling coefficient summands: no
    # numerical zero threshold or unproved cancellation enters coverage.
    def circulation(mu, nu, clover=False):
        if mu > nu:
            return [(a, -s, f) for a, s, f in circulation(nu, mu, clover)]
        out = []
        for alpha, other, sign in ((nu, mu, 1), (mu, nu, -1)):
            factors = [ident[t] for t in types(alpha)]
            factors[other] = G
            if clover:
                for j in (mu, nu): factors[j] = dot(AV, factors[j])
            out.append((alpha, sign, factors))
        return out
    Q = {3: [], 6: []}
    def add_q(probe, row1, row2, coeffs, factor):
        for sign, vectors in coeffs:
            for alpha, sl, left in row1:
                for beta, sr_, right in row2:
                    mats = [dot(dot(transpose(l), diag(v)), z) for l, v, z in zip(left, vectors, right)]
                    Q[probe].append((alpha, beta, factor*sign*sl*sr_, mats))
    for mu, nu in combinations(range(4), 2):
        co = []
        for sign, vectors in w[mu]+w[nu]:
            vectors = list(vectors)
            for j in (mu, nu): vectors[j] = dot(transpose(AV), vectors[j])
            co.append((sign, vectors))
        row = circulation(mu, nu)
        add_q(3, row, row, co, F(1))
        for alpha in range(4):
            if alpha in (mu, nu): continue
            left, right = circulation(mu, alpha, True), circulation(nu, alpha, True)
            add_q(6, left, right, shears[mu, nu], F(1, 2))
            add_q(6, right, left, shears[mu, nu], F(1, 2))
    W = [sr.multiply(h, f), r, cf, r]
    M = []
    for mu in (1, 2, 3):
        upper, lifted = [], []
        for alpha in (mu, 0):
            uf = [ident['V'] for _ in range(4)]
            vf = list(uf)
            if alpha == mu:
                uf[0] = dot(ones, dot(top, G)); uf[mu] = AV
                vf[mu] = AV
                sign = 1
            else:
                uf[0] = dot(ones, top); uf[mu] = dot(AV, G)
                vf[0] = prefix; vf[mu] = dot(AV, G)
                sign = -1
            upper.append((alpha, sign, uf)); lifted.append((alpha, sign, vf))
        for alpha, su, uf in upper:
            for beta, sv, vf in lifted:
                mats = [dot(dot(transpose(l), diag(v)), z) for l, v, z in zip(uf, W, vf)]
                M.append((alpha, beta, A*su*sv, mats))
    # All finite matrices, before and after the explicit eigenbasis.
    archive = {}
    def spectral(terms, label):
        out = []
        for index, (alpha, beta, coeff, mats) in enumerate(terms):
            transformed = []
            for j, m in enumerate(mats):
                b1, b2 = basis[types(alpha)[j]], basis[types(beta)[j]]
                sm = dot(dot(transpose(b1), m), b2)
                for side, value in zip(('c', 'r'), m): archive[f'{label}_{index}_{j}_physical_{side}'] = value
                for side, value in zip(('c', 'r'), sm): archive[f'{label}_{index}_{j}_spectral_{side}'] = value
                transformed.append(sm)
            out.append((alpha, beta, coeff, transformed))
        return out
    M = spectral(M, 'M'); Q = {i: spectral(v, f'Q{i}') for i, v in Q.items()}
    print(f'Constructed all component terms: M={len(M)}, Q3={len(Q[3])}, Q6={len(Q[6])}', flush=True)
    sw.DEGREE = DEGREE
    roots, weights, root_rows = sw.roots_and_weights()
    panels = [(F(0), F(1, 32))]+[(F(2)**j, F(2)**(j+1)) for j in range(-5, 10)]
    nodes, wr, mapped = [], [], []
    for p, (left, right) in enumerate(panels):
        for k, (root, weight) in enumerate(zip(roots, weights)):
            v = rat((left+right)/2)+rat((right-left)/2)*root
            z = rat(T0)+v; wt = rat((right-left)/2)*weight
            nodes.append(z); wr.append(wt)
            mapped.append(dict(panel=p, root=k, time=rec(z), weight=rec(wt)))
    heat_raw = [[ar.exp_negative(z*lam) for lam in lambdas] for z in nodes]
    heat_e = enclosed(heat_raw)
    heat = {'E': heat_e, 'V': (heat_e[0][:, 1:], heat_e[1][:, 1:])}
    weights_mr = enclosed(wr)
    archive['weights_c'], archive['weights_r'] = weights_mr
    archive['heat_c'], archive['heat_r'] = heat_e
    print(f'Enclosed all {len(nodes)} quadrature nodes and {len(nodes)*N} heat entries', flush=True)
    # Rigorous norms: |rho|<=1, |f|<=3, ||C||_infinity<=1/a.
    # W*<=8*3*(3/a), W3<=2*(3/a)^2, S6<=2*3*(3/a^2).
    # These deliberately loose bounds cover all tensor coefficient sums.
    wstar = 72/A; w3 = 18/A**2; s6 = 18/A**2
    bm = 12*A*N*(1+4*N)*wstar  # sqrt(N-1)<=N
    bi = {3: 16*w3, 6: 192*s6}
    d = 4*N*(N-1)**3
    # sin(pi/(2N)) >= 1/N by concavity on [0,pi/2].
    gap = F(12, N*N)
    cg = F(factorial(DEGREE)**4, (2*DEGREE+1)*factorial(2*DEGREE)**3)
    quad_rel = cg*(1+15*factorial(2*DEGREE+1))
    # Tail is bounded separately, at actual positive-spectrum lower bound.
    actual_gap = 3*F(lambdas[1].lo, S)
    assert actual_gap >= gap
    tail_rel = ar.exp_negative(rat(1024)*rat(actual_gap)).absolute_upper()
    # ||F||<=1/gap, ||F-F_rule||<= (quad_rel+tail_rel)/gap.
    norm_errors = {i: F(d)*bm*b/gap**2*(2*(quad_rel+tail_rel)+(quad_rel+tail_rel)**2)
                   for i, b in bi.items()}
    results, coverage = [], []
    count = len(nodes)
    def integrate(z):
        total = exact(0.)
        for lo in range(0, count, 160):
            hi = min(lo+160, count)
            for p in range(0, count, 160):
                q = min(p+160, count)
                block = z[0][lo:hi, p:q], z[1][lo:hi, p:q]
                wl = weights_mr[0][lo:hi], weights_mr[1][lo:hi]
                ww = weights_mr[0][p:q], weights_mr[1][p:q]
                total = sr.add(total, dot(dot(wl, block), ww))
        return total
    for probe in (3, 6):
        total = exact(0.)
        term_number = 0
        for im, (alpha, beta, cm, mm) in enumerate(M):
            for iq, (qa, qb, cq, qq) in enumerate(Q[probe]):
                if (qa, qb) != (beta, alpha): continue
                value = exact(np.ones((count, count)))
                for j, (m, q) in enumerate(zip(mm, qq)):
                    # K_ab=M_ab Q_ba: row index alpha, col index beta.
                    k = sr.multiply(m, transpose(q))
                    hs, ht = heat[types(alpha)[j]], heat[types(beta)[j]]
                    feature = dot(dot(hs, k), transpose(ht))
                    value = sr.multiply(value, feature)
                value = scalar(value, cm*cq)
                term = integrate(value)
                total = sr.add(total, term)
                coverage.append(dict(probe=probe, M=im, Q=iq, coefficient=str(cm*cq), integral=pair_record(term)))
                term_number += 1
        center, radius = F(float(total[0])), F(float(total[1]))
        error = radius+norm_errors[probe]
        row = dict(probe=probe, retained=pair_record(total), terms=term_number,
                   quadrature_and_tail_error=rational_record(norm_errors[probe]),
                   total_error=rational_record(error), lower=rational_record(center-error),
                   upper=rational_record(center+error), error_at_most_one=error <= 1,
                   sign=('positive' if center > error else 'negative' if center < -error else 'unresolved'))
        results.append(row)
        print(f'Probe {probe}: center={float(center):.12g}, arithmetic radius={float(radius):.6g}, quadrature/tails={float(norm_errors[probe]):.6g}; total error={float(error):.6g}, required <=1; sign={row["sign"]}', flush=True)
    saved = ROOT/'first-pair-retained-enclosure-factors.npz'
    np.savez_compressed(saved, **archive)
    failures = [f'probe {r["probe"]}: error exceeds 1' for r in results if not r['error_at_most_one']]
    certificate = dict(scope='L070(9)/L072 diagnostic only at N=24; all relative modes', N=N,
        precision_scale=str(S), arithmetic_model='L039 IEEE addition/product or FMA, no overflow, local underflow allowance 1e-290',
        degree=DEGREE, panels=[[str(x), str(y)] for x,y in panels], roots=root_rows, mapped_rule=mapped,
        pi=rec(pi), basis={k:[[rec(z) for z in row] for row in v] for k,v in basis_raw.items()},
        rho=[rec(z) for z in rraw], eigenvalues=[rec(z) for z in lambdas],
        heat=[[rec(z) for z in row] for row in heat_raw],
        component_terms={'M':[[a,b,str(c)] for a,b,c,_ in M],
                         'Q3':[[a,b,str(c)] for a,b,c,_ in Q[3]], 'Q6':[[a,b,str(c)] for a,b,c,_ in Q[6]]},
        norm_bounds={k:str(v) for k,v in dict(BM=bm,B3=bi[3],B6=bi[6],dimension=d,gap=gap,actual_gap_lower=actual_gap).items()},
        relative_quadrature_error=rational_record(quad_rel), relative_tail_error=rational_record(tail_rel),
        tensor_terms=coverage, results=results, failures=failures,
        factor_archive=saved.name, factor_archive_sha256=hashlib.sha256(saved.read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        support_sha256={Path(module.__file__).name:hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
                        for module in (ar,sw,sr)},
        unresolved=['original-trace reduction', 'mesh asymptotic', 'other response terms and cutoff logarithm'])
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(f'Failures: {failures}; certificate: {OUT}; factors: {saved}', flush=True)


if __name__ == '__main__':
    main()
