"""Exact mixed-cubic regression checks; no actual-box cumulant asymptotics."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

n = 5  # Three vertex potentials and two correlated independent-noise coordinates.
m = 3*n
zero = (0,)*m
checks = []


def record(kind, actual, required, **details):
    checks.append(dict(kind=kind, actual=str(actual), required=str(required),
                       passed=actual == required, **details))


def add(*polys):
    out = {}
    for poly in polys:
        for e, v in poly.items():
            out[e] = out.get(e, F(0)) + v
    return {e: v for e, v in out.items() if v}


def scale(c, p):
    return {e: c*v for e, v in p.items() if c*v}


def mul(p, q):
    out = {}
    for e, v in p.items():
        for h, w in q.items():
            k = tuple(a+b for a, b in zip(e, h))
            out[k] = out.get(k, F(0)) + v*w
    return {e: v for e, v in out.items() if v}


def variable(i):
    return {tuple(int(j == i) for j in range(m)): F(1)}


cov = [[F(0) for _ in range(n)] for _ in range(n)]
for j, v in enumerate([2, 3, 5, F(1, 2), F(3, 4)]):
    cov[j][j] = F(v)
cov[3][4] = cov[4][3] = F(1, 4)


@lru_cache(None)
def moment(e):
    if not any(e):
        return F(1)
    if any(sum(e[c*n:(c+1)*n]) % 2 for c in range(3)):
        return F(0)
    i = next(j for j, v in enumerate(e) if v)
    tail = list(e)
    tail[i] -= 1
    ans = F(0)
    for j in range(i//n*n, (i//n+1)*n):
        if tail[j] and cov[i % n][j % n]:
            rest = tail.copy()
            rest[j] -= 1
            ans += tail[j]*cov[i % n][j % n]*moment(tuple(rest))
    return ans


def expect(p):
    return sum((v*moment(e) for e, v in p.items()), F(0))


def derivative(p, j):
    color, edge = divmod(j, 2)
    out = []
    for k in range(2):
        index = color*n+3+k
        for e, v in p.items():
            if e[index]:
                h = list(e)
                h[index] -= 1
                out.append({tuple(h): v*e[index]*cov[3+edge][3+k]})
    return add(*out)


def cross(p, q):
    return [add(mul(p[(c+1) % 3], q[(c+2) % 3]),
                scale(-1, mul(p[(c+2) % 3], q[(c+1) % 3]))) for c in range(3)]


def dot(p, q):
    return add(*(mul(v, w) for v, w in zip(p, q)))


def vadd(*vs):
    return [add(*(v[c] for v in vs)) for c in range(3)]


def vscale(t, v):
    return [scale(t, p) for p in v]


u = [[variable(c*n+j) for c in range(3)] for j in range(3)] + [[{}]*3]
eta = [[variable(c*n+3+j) for c in range(3)] for j in range(2)]
q_edges = [cross(u[0], u[1]), cross(u[1], u[2])]
Q = [q_edges[e][c] for c in range(3) for e in range(2)]
noise = [eta[e][c] for c in range(3) for e in range(2)]
C = scale(F(1, 2), add(*(mul(y, q) for y, q in zip(noise, Q))))
mean_edges = [vadd(u[j], vscale(-1, u[(j+1) % 4])) for j in range(4)]
ys = [vadd(mean_edges[j], eta[j % 2]) for j in range(4)]
D = scale(F(-1, 2), add(*(dot(ys[r], cross(ys[s], ys[t]))
                        for r in range(4) for s in range(r+1, 4)
                        for t in range(s+1, 4))))
H = scale(F(1, 2), add(*(mul(q, derivative(D, j)) for j, q in enumerate(Q))))
M = {e: v for e, v in H.items() if all(e[c*n+k] == 0
     for c in range(3) for k in [3, 4])}

# Check the exact polygon BCH identity, including a pinned vertex.
w2_vec = vscale(F(-1, 2), vadd(*(cross(mean_edges[r], mean_edges[s])
                 for r in range(4) for s in range(r+1, 4))))
polygon = vscale(F(-1, 2), vadd(*(cross(u[j], u[(j+1) % 4]) for j in range(4))))
for c in range(3):
    record('gradient_polygon_bch', add(w2_vec[c], scale(-1, polygon[c])), {}, color=c)

# Color-diagonal conditional averaging of each quadratic derivative keeps
# only its mean value; noise cross contractions vanish by the color tensor.
def condition(p):
    out = {}
    for e, v in p.items():
        ne = tuple(e[j] if j % n >= 3 else 0 for j in range(m))
        ue = tuple(e[j] if j % n < 3 else 0 for j in range(m))
        out[ue] = out.get(ue, F(0)) + v*moment(ne)
    return {e: v for e, v in out.items() if v}


record('conditional_mixed_product', condition(mul(C, D)), M)


def quad(entries):
    return add(*(scale(F(v), mul(variable(c*n+i), variable(c*n+j)))
                 for c in range(3) for i, j, v in entries))


def kappa3(f, r, t):
    ef, er, et = expect(f), expect(r), expect(t)
    return (expect(mul(mul(f, r), t)) - ef*expect(mul(r, t))
            - er*expect(mul(f, t)) - expect(mul(f, r))*et + 2*ef*er*et)


r = quad([(0, 0, 1), (1, 4, 3), (3, 3, -2), (3, 4, 1), (2, 2, -1)])
probes = [quad([(0, 0, 1), (1, 1, -1), (2, 2, 2)]),
          quad([(0, 3, 2), (1, 4, -1), (3, 3, 1), (4, 4, 2), (0, 1, 1)])]
for case, f in enumerate(probes):
    for label, h in [('1', {zero: F(1)}), ('f', f), ('r', r), ('fr', mul(f, r))]:
        correction = F(1, 2)*sum((expect(mul(mul(q, D), derivative(h, j)))
                                  for j, q in enumerate(Q)), F(0))
        record('single_ibp_moment', expect(mul(mul(h, C), D)),
               expect(mul(h, H)) + correction, case=case, polynomial=label)
    ef, er = expect(f), expect(r)
    fc = add(f, {zero: -ef})
    rc = add(r, {zero: -er})
    obs = F(1, 2)*sum((expect(mul(mul(q, D), add(mul(rc, derivative(f, j)),
                                     mul(fc, derivative(r, j)))))
                      for j, q in enumerate(Q)), F(0))
    effective = kappa3(f, r, M)
    fluctuation = kappa3(f, r, add(H, scale(-1, M)))
    actual = kappa3(f, r, mul(C, D))
    record('complete_mixed_cumulant', actual, effective + fluctuation + obs,
           case=case, effective=str(effective), fluctuation=str(fluctuation),
           observable_correction=str(obs))

# Exact endpoint Green row for all listed positive rational eigenvalues.
for N in [2, 4, 8, 16]:
    for lam in [F(1, N*N), F(1), F(4), F(12)]:
        seq = [F(0), F(1)]
        for s in range(1, N):
            seq.append((2+lam)*seq[-1]-seq[-2])
        g = [seq[s]/seq[N] for s in range(N+1)]
        b = 1-g[N-1]
        chi = lam*sum((F(s*s, N*N)*g[s] for s in range(1, N)), F(0))
        rhs = b-F(2, N)+F(1, N*N)+F(2, N*N)*sum(g[1:N], F(0))
        record('interval_symbol_recurrence', chi, rhs, N=N, eigenvalue=str(lam))
        ok = (chi > 0 and F(1, N) <= b-chi <= F(2, N)
              and all(0 <= g[s] <= F(s, N) for s in range(N)))
        record('full_frequency_bounds', ok, True, N=N, eigenvalue=str(lam),
               chi=str(chi), b_minus_chi=str(b-chi),
               required_bounds=[str(F(1, N)), str(F(2, N))])

failures = [x for x in checks if not x['passed']]
out = Path(__file__).with_name('top-other-cubic-certificate.json')
out.write_text(json.dumps(dict(
    scope='Exact Gaussian surrogate and interval symbols; analytic arbitrary-mesh identity in L058; no original-box response value',
    checks=checks, failures=failures,
    bounds=dict(actual='Conditional mixed quartic and complete finite cumulant identities; symbol discrepancy <=2/N',
                required='Full mixed a^2-scaled cumulant including fluctuations/observable derivatives; full logarithm; reflected error <=c_box/2')
), indent=2)+'\n')
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact checks; failures={len(failures)}")
print('Actual: finite identities and symbol discrepancy <=2/N; required: full mixed scaled response/log and reflected error <=c_box/2.')
for x in checks:
    if x['kind'] == 'complete_mixed_cumulant':
        print(f"case {x['case']}: complete={x['actual']}, effective={x['effective']}, fluctuation={x['fluctuation']}, observable={x['observable_correction']}")
print(f'Certificate: {out.relative_to(Path.cwd())}')
for x in failures:
    print('FAILURE:', x)
assert not failures
