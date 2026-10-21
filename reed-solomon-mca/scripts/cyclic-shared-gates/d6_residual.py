"""One normalized seed diagnostic, not an H-label or rank search."""
import json
from pathlib import Path

P = 97


def trim(a):
    a = [x % P for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*x for x in a])


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def div(a, b):
    return a * pow(b % P, -1, P) % P


def ev(a, x):
    out = 0
    for c in reversed(a):
        out = (out*x+c) % P
    return out


def det3(rows):
    a, b, c = rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0])) % P


def main():
    c, d, e, g = 2, 3, 4, 6
    j = div(c*(1-g), 1-c)
    k = div(d*e+g*j-d*(g+j), e-d)
    ell = (c-k) % P
    C = div((j-g)*(k-d), (j-c)*(j-d)*(k-g))
    t = j*C % P
    u = j*(1-t) % P
    alpha, beta, gamma = e*(k-1) % P, (k-e) % P, k*(e-1) % P
    Q = trim([gamma*u, beta*u+gamma*t-alpha, beta*t])
    M, Y = [k*c % P, -k % P], [u, t]
    N = scale(sub([g*ell], M), d*e)
    O = sub(scale(sub([(d+e)*ell], M), g), [d*e*ell])
    A, B, C2 = [c+d-j, -1], [-c*d, j], [c*d*j, c*d-j*(c+d)]
    Z = scale(add(mul(B, N), mul(C2, O)), -1)
    W = add(mul(A, N), mul(B, O))
    U = add(scale(add([j-k], scale(Y, 1-j)), ell), scale(M, k-1))
    V = add(scale(mul(Y, add(M, [ell*(k-1)])), j),
            scale(mul(M, sub([1-j], Y)), k))
    E = add(mul(Z, U), mul(W, V))
    a, b = div(-Q[1], Q[2]), div(-Q[0], Q[2])
    ee = E+[0]*(5-len(E))
    rho = [(ee[0]+b*ee[2]+a*b*ee[3]+(a*a*b+b*b)*ee[4]) % P,
           (ee[1]+a*ee[2]+(a*a+b)*ee[3]+(a*a*a+2*a*b)*ee[4]) % P]
    # Independent polynomial long division checks the closed remainder formula.
    rem, quotient = E[:], [0]*max(1, len(E)-2)
    while len(rem) >= len(Q) and rem != [0]:
        shift = len(rem)-len(Q)
        coef = div(rem[-1], Q[-1])
        quotient[shift] = coef
        rem = sub(rem, [0]*shift+scale(Q, coef))
    failures = []
    if trim(rho) != rem:
        failures.append('remainder formula')
    delta = (Q[2]*rho[0]**2-Q[1]*rho[0]*rho[1]+Q[0]*rho[1]**2) % P
    if len(set([0, 1, c, d, e, g, j, k])) != 8:
        failures.append('assigned finite distinctness')
    if det3([[c, 1, 0], [j, 1+j, 1], [0, g, 1]]) != 0:
        failures.append('D_1')
    if det3([[g*j, g+j, 1], [k*e, k+e, 1], [d, 1, 0]]) != 0:
        failures.append('D_10')
    rows = []
    for x in range(P):
        nv, ov, zv, wv = (ev(poly, x) for poly in [N, O, Z, W])
        mv, y = ev(M, x), ev(Y, x)
        direct = det3([[zv, zv+wv, wv],
                       [j*y, j+y, 1], [k*mv, mv+k*ell, ell]])
        if direct != ev(E, x):
            failures.append(f'cleared determinant at {x}')
        if ov and wv:
            m, n, z = div(mv, ell), div(nv, ov), div(zv, wv)
            for name, mat in [
                ('D_8', [[0, x, 1], [k, 1, 0], [m*c, m+c, 1]]),
                ('D_3', [[d*e, d+e, 1], [0, m, 1], [g*n, g+n, 1]]),
                ('D_2', [[c*d, c+d, 1], [x*j, x+j, 1], [z*n, z+n, 1]])]:
                if det3(mat):
                    failures.append(f'{name} at {x}')
        rows.append({'x': x, 'Q': ev(Q, x), 'E': ev(E, x),
                     'cleared_D6': direct, 'N_den': ov, 'Z_den': wv})
    result = {
        'scope': 'One rational-function nonidentity diagnostic over F_97; no H-label claim',
        'seeds': dict(c=c, d=d, e=e, g=g, j=j, k=k),
        'coefficients_order': 'ascending',
        'normalization': dict(ell=ell, t=t, u=u, alpha=alpha, beta=beta, gamma=gamma),
        'polynomials': dict(Q=Q, M=M, N=N, O=O, Z=Z, W=W, U=U, V=V, E=E),
        'quotient': trim(quotient), 'remainder': rem, 'rho': rho,
        'delta': delta, 'rows': rows, 'failures': failures,
        'bound': {'actual_remainder_degree': len(rem)-1, 'required_maximum': 1},
        'H_assignments_tested': 0, 'rank_tests': 0,
    }
    path = Path(__file__).with_name('d6-residual-certificate.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in
                      ['seeds', 'rho', 'delta', 'bound', 'failures',
                       'H_assignments_tested', 'rank_tests']}))
    print(f'Complete certificate: {path}')
    if failures or delta == 0:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
