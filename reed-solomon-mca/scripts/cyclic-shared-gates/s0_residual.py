"""Exact one-parameter rational diagnostic, with no H-label or rank search."""
import json
from pathlib import Path

MOD = 97


def trim(p):
    p = [a % MOD for a in p]
    while len(p) > 1 and not p[-1]:
        p.pop()
    return p


def pa(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def ps(p, a):
    return trim([a*b for b in p])


def pm(p, q):
    r = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return trim(r)


def pd(p, q):
    p, q = trim(p), trim(q)
    assert q != [0]
    out = [0]*max(1, len(p)-len(q)+1)
    while p != [0] and len(p) >= len(q):
        shift = len(p)-len(q)
        a = p[-1]*pow(q[-1], -1, MOD) % MOD
        out[shift] = a
        p = pa(p, [0]*shift+ps(q, -a))
    return trim(out), p


def pg(p, q):
    while q != [0]:
        p, q = q, pd(p, q)[1]
    return ps(p, pow(p[-1], -1, MOD)) if p != [0] else p


def pe(p, a):
    out = 0
    for b in reversed(p):
        out = (out*a+b) % MOD
    return out


def ppow(a, n, modulus):
    out = [1]
    while n:
        if n & 1:
            out = pd(pm(out, a), modulus)[1]
        a = pd(pm(a, a), modulus)[1]
        n //= 2
    return out


def pinv(a, modulus):
    old, current = modulus[:], a[:]
    old_b, current_b = [0], [1]
    while current != [0]:
        quotient, remainder = pd(old, current)
        old, current = current, remainder
        old_b, current_b = current_b, pa(old_b, ps(pm(quotient,current_b),-1))
    assert len(old) == 1 and old[0]
    return pd(ps(old_b,pow(old[0],-1,MOD)),modulus)[1]


def ratmod(value, modulus):
    return pd(pm(value.n,pinv(value.d,modulus)),modulus)[1]


class Rat:
    """Canonical F_97(G); ascending coefficient order throughout."""
    def __init__(self, n=0, d=None):
        if isinstance(n, Rat):
            self.n, self.d = n.n[:], n.d[:]
            return
        n = trim(n if isinstance(n, list) else [n])
        d = trim([1] if d is None else d)
        assert d != [0]
        common = pg(n, d)
        n, rn = pd(n, common)
        d, rd = pd(d, common)
        assert rn == rd == [0]
        a = pow(d[-1], -1, MOD)
        self.n, self.d = ps(n, a), ps(d, a)

    def __add__(self, b):
        b = Rat(b)
        return Rat(pa(pm(self.n, b.d), pm(b.n, self.d)), pm(self.d, b.d))

    __radd__ = __add__

    def __neg__(self):
        return Rat(ps(self.n, -1), self.d)

    def __sub__(self, b):
        return self+-Rat(b)

    def __rsub__(self, b):
        return Rat(b)+-self

    def __mul__(self, b):
        b = Rat(b)
        return Rat(pm(self.n, b.n), pm(self.d, b.d))

    __rmul__ = __mul__

    def __truediv__(self, b):
        b = Rat(b)
        return Rat(pm(self.n, b.d), pm(self.d, b.n))

    def __eq__(self, b):
        b = Rat(b)
        return self.n == b.n and self.d == b.d

    def at(self, g):
        return pe(self.n, g)*pow(pe(self.d, g), -1, MOD) % MOD

    def data(self):
        return dict(numerator=self.n, denominator=self.d)


def xt(p):
    p = [Rat(a) for a in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def xa(p, q):
    return xt([(p[i] if i < len(p) else Rat(0))+
               (q[i] if i < len(q) else Rat(0))
               for i in range(max(len(p), len(q)))])


def xs(p, a):
    return xt([b*a for b in p])


def xm(p, q):
    r = [Rat(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] = r[i+j]+a*b
    return xt(r)


def xd(p, q):
    p, q = xt(p), xt(q)
    out = [Rat(0)]*max(1, len(p)-len(q)+1)
    while p != [Rat(0)] and len(p) >= len(q):
        shift = len(p)-len(q)
        a = p[-1]/q[-1]
        out[shift] = a
        p = xa(p, [Rat(0)]*shift+xs(q, -a))
    return xt(out), p


def xe(p, x):
    out = Rat(0)
    for a in reversed(p):
        out = out*x+a
    return out


def main():
    c, d, e, g = Rat(2), Rat(3), Rat(4), Rat([0, 1])
    j = c*(1-g)/(1-c)
    k = (d*e+g*j-d*(g+j))/(e-d)
    ell = c-k
    C = (j-g)*(k-d)/((j-c)*(j-d)*(k-g))
    t = j*C
    u = j*(1-t)
    alpha, beta, gamma = e*(k-1), k-e, k*(e-1)
    Q = xt([gamma*u, beta*u+gamma*t-alpha, beta*t])
    M, Y = xt([k*c, -k]), xt([u, t])
    N = xs(xa([g*ell], xs(M, -1)), d*e)
    O = xa(xs(xa([(d+e)*ell], xs(M, -1)), g), [-d*e*ell])
    A, B, C2 = xt([c+d-j, -1]), xt([-c*d, j]), xt([c*d*j, c*d-j*(c+d)])
    Z = xs(xa(xm(B, N), xm(C2, O)), -1)
    W = xa(xm(A, N), xm(B, O))
    U = xa(xs(xa([j-k], xs(Y, 1-j)), ell), xs(M, k-1))
    V = xa(xs(xm(Y, xa(M, [ell*(k-1)])), j),
           xs(xm(M, xa([1-j], xs(Y, -1))), k))
    E = xa(xm(Z, U), xm(W, V))
    X = xt([0, 1])
    P = xa(xs(xm(xa(Y, xs(X, -1)), xa(Z, xs(W, -c))), d*(d-g)*(d-j)),
           xs(xm(xm(xm(xa(Z, xs(W, -j)), xa(X, [-g])), X),
                 xa([d], xs(Y, -1))), d-c))
    eq, rho = xd(E, Q)
    pq, sigma = xd(P, Q)
    rho = rho+[Rat(0)]*(2-len(rho))
    sigma = sigma+[Rat(0)]*(2-len(sigma))
    a, b = -Q[1]/Q[2], -Q[0]/Q[2]
    aa, bb = a*a, b*b
    pp = P+[Rat(0)]*(6-len(P))
    sigma_formula = [pp[0]+b*pp[2]+a*b*pp[3]+(aa*b+bb)*pp[4]
                     +(aa*a*b+2*a*bb)*pp[5],
                     pp[1]+a*pp[2]+(aa+b)*pp[3]+(aa*a+2*a*b)*pp[4]
                     +(aa*aa+3*aa*b+bb)*pp[5]]
    delta = Q[2]*rho[0]*rho[0]-Q[1]*rho[0]*rho[1]+Q[0]*rho[1]*rho[1]
    psi = rho[1]*sigma[0]-rho[0]*sigma[1]
    root = -rho[0]/rho[1]
    yy, mm = xe(Y, root), xe(M, root)/ell
    nn, zz = xe(N, root)/xe(O, root), xe(Z, root)/xe(W, root)
    # D_0 pairs (Y,infinity),(z,X),(h4,g); D_4 then gives h13.
    h4 = (yy*(zz+root-g)-zz*root)/(yy-g)
    a4, b4, c4 = e+h4-j-mm, j*mm-e*h4, e*h4*(j+mm)-j*mm*(e+h4)
    h13 = (-b4*root-c4)/(a4*root+b4)
    labels = {1:c, 2:d, 3:e, 4:h4, 5:Rat(1), 6:zz, 7:Rat(0),
              8:root, 9:g, 10:j, 11:nn, 12:mm, 13:h13, 14:k, 15:yy}
    gates = {'rho1':rho[1], 'q2':Q[2], 'ell':ell,
             'O_at_X':xe(O, root), 'W_at_X':xe(W, root),
             'D15_pole':beta*root+gamma, 'D0_pole':yy-g,
             'D4_pole':a4*root+b4, 'delta_den':Rat(delta.d),
             'psi_den':Rat(psi.d)}
    for i, value in labels.items():
        gates[f'finite_{i}'] = Rat(value.d)
    indices = sorted(labels)
    for pos, i in enumerate(indices):
        for jidx in indices[pos+1:]:
            gates[f'difference_{i}_{jidx}'] = labels[i]-labels[jidx]
    remaining = delta.n[:]
    removed = []
    for name, value in gates.items():
        for branch, polynomial in [('numerator',value.n),('denominator',value.d)]:
            while len(remaining) > 1:
                common = pg(remaining, polynomial)
                if len(common) == 1:
                    break
                remaining, remainder = pd(remaining, common)
                assert remainder == [0]
                removed.append(dict(gate=name, part=branch, factor=common))
    remaining = ps(remaining, pow(remaining[-1], -1, MOD))
    distinct_degree = {}
    power = [0,1]
    for degree in range(1, 15):
        power = ppow(power, MOD, remaining)
        distinct_degree[str(degree)] = pg(remaining, pa(power,[0,-1]))
    witness_modulus = distinct_degree['13']
    assert len(witness_modulus) == 14
    witness = dict(modulus=witness_modulus, field='F_97[G]/(modulus)',
                   labels={str(i):ratmod(v,witness_modulus) for i,v in labels.items()},
                   Q_at_X=ratmod(xe(Q,root),witness_modulus),
                   E_at_X=ratmod(xe(E,root),witness_modulus),
                   P_at_X=ratmod(xe(P,root),witness_modulus),
                   rho=[ratmod(v,witness_modulus) for v in rho],
                   sigma=[ratmod(v,witness_modulus) for v in sigma],
                   psi=ratmod(psi,witness_modulus),
                   gates={name:ratmod(v,witness_modulus) for name,v in gates.items()})
    # Euclidean gcd finds rational roots algebraically, without seed enumeration.
    rational = pg(delta.n, [-0, -1]+[0]*95+[1])
    result = dict(scope='One symbolic c=2,d=3,e=4,G slice; not an H-labeling search',
                  coefficient_order='ascending',
                  polynomials={name: [a.data() for a in poly] for name, poly in
                               dict(Q=Q, E=E, P=P, M=M, N=N, O=O, Z=Z, W=W,
                                    E_quotient=eq, P_quotient=pq,
                                    rho=rho, sigma=sigma).items()},
                  delta=delta.data(), psi=psi.data(),
                  gcd_delta_psi=pg(delta.n, psi.n), rational_root_factor=rational,
                  reconstructed_labels={str(i):v.data() for i,v in labels.items()},
                  reconstruction_gates={name:v.data() for name,v in gates.items()},
                  removed_factors=removed, admissible_factor=remaining,
                  gcd_admissible_psi=pg(remaining,psi.n),
                  distinct_degree_factors=distinct_degree,
                  witness=witness,
                  bound=dict(actual_P_degree=len(P)-1, required_P_degree_max=5,
                             actual_remainder_degree=max(len(xt(rho)),len(xt(sigma)))-1,
                             required_remainder_degree_max=1),
                  failures=[], H_assignments_tested=0, rank_tests=0)
    for name, poly, quotient, remainder in [('E', E, eq, rho), ('P', P, pq, sigma)]:
        if xa(xm(quotient, Q), remainder) != poly:
            result['failures'].append(name+' division identity')
    if witness['Q_at_X'] != [0] or witness['E_at_X'] != [0] or witness['P_at_X'] == [0]:
        result['failures'].append('witness separating values')
    if any(value == [0] for value in witness['gates'].values()):
        result['failures'].append('witness gate zero')
    if sigma_formula != sigma:
        result['failures'].append('closed degree-five remainder formula')
    path = Path(__file__).with_name('s0-residual-certificate.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['bound','gcd_admissible_psi',
                                           'failures','H_assignments_tested','rank_tests']}))
    print('Complete certificate:', path)
    if result['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
