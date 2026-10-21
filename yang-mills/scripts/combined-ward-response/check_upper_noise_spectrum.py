"""Full-edge boundary covariance checks; exact N=2, numerical N=4.

The analytic proof in L050, rather than numerical tolerances, establishes
the arbitrary-mesh identity and rates. No actual probe cumulant is computed.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np


def interval(n):
    d = np.zeros((n, n-1), dtype=int)
    for e in range(n):
        if e > 0:
            d[e, e-1] -= 1
        if e < n-1:
            d[e, e] += 1
    return d, d @ d.T, d.T @ d


def tensor(items):
    out = np.ones((1, 1), dtype=int)
    for item in items:
        out = np.kron(out, item)
    return out


def laplacian(items):
    out = np.zeros((np.prod([len(m) for m in items]),)*2, dtype=int)
    for j, item in enumerate(items):
        out += tensor([item if k == j else np.eye(len(m), dtype=int)
                       for k, m in enumerate(items)])
    return out


def geometry(n):
    d, le, lv = interval(n)
    eyev = np.eye(n-1, dtype=int)
    t = np.vstack([-tensor([d if k == mu else eyev for k in range(3)])
                   for mu in range(3)])
    edge_laps = [laplacian([le if k == mu else lv for k in range(3)])
                 for mu in range(3)]
    sizes = [len(m) for m in edge_laps]
    dt = np.zeros((sum(sizes),)*2, dtype=int)
    pos = 0
    for m in edge_laps:
        dt[pos:pos+len(m), pos:pos+len(m)] = m
        pos += len(m)
    # Actual four-dimensional Hodge component blocks. Selecting last axial
    # edge/vertex rows produces the covariance of L049's d, with end edges.
    axial = laplacian([le, lv, lv, lv])
    transverse = [laplacian([lv]+[le if k == mu else lv for k in range(3)])
                  for mu in range(3)]
    return le, laplacian([lv, lv, lv]), t, dt, axial, transverse


def rational(m):
    return [[F(int(v)) for v in row] for row in m]


def inverse(m):
    size = len(m)
    rows = [row[:] + [F(i == j) for j in range(size)] for i, row in enumerate(m)]
    for j in range(size):
        pivot = next(i for i in range(j, size) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        c = rows[j][j]
        rows[j] = [v/c for v in rows[j]]
        for i in range(size):
            if i != j:
                c = rows[i][j]
                rows[i] = [v-c*w for v, w in zip(rows[i], rows[j])]
    return [row[size:] for row in rows]


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def plus(a, b, sign=1):
    return [[x+sign*y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scaled(a, c):
    return [[c*v for v in row] for row in a]


def corner(a, size):
    return [row[-size:] for row in a[-size:]]


def exact_test():
    n = 2
    le, dv, t, dt, axial, transverse = geometry(n)
    t, dt = rational(t), rational(dt)
    size = len(dt)
    ident = [[F(i == j) for j in range(size)] for i in range(size)]
    p = mm(mm(t, inverse(rational(dv))), tr(t))
    cv = corner(inverse(rational(axial)), len(dv))
    kd = mm(mm(t, cv), tr(t))
    offset = 0
    for lap in transverse:
        m = len(lap)//(n-1)
        block = corner(inverse(rational(lap)), m)
        for i in range(m):
            for j in range(m):
                kd[offset+i][offset+j] += block[i][j]
        offset += m
    k = plus(kd, scaled(p, F(1, n)), -1)
    large = np.kron(le, np.eye(size, dtype=int)) + np.kron(np.eye(n, dtype=int), np.array(dt, dtype=int))
    end_resolvent = corner(inverse(rational(large)), size)
    b = mm(dt, end_resolvent)
    defect = plus(ident, k, -1)
    formula = plus(scaled(p, F(1, n)), mm(b, plus(ident, p, -1)))
    checks = []

    def check(label, a, wanted):
        error = max(abs(x-y) for r, s in zip(a, wanted) for x, y in zip(r, s))
        checks.append({'label': label, 'actual_error': str(error),
                       'required_error': '0', 'pass': error == 0})

    check('full_boundary_defect', defect, formula)
    check('gradient_projection', mm(p, p), p)
    check('commuting_laplacian', mm(dt, p), mm(p, dt))
    check('gradient_rate', mm(defect, p), scaled(p, F(1, n)))
    # Constant own-direction edge mode, transverse sine indices (1,1).
    high = [[F(1)], [F(1)]] + [[F(0)] for _ in range(size-2)]
    check('high_mode_zero_divergence', mm(tr(t), high), [[F(0)]])
    check('high_mode_eigenvalue_4', mm(dt, high), scaled(high, F(4)))
    check('high_mode_defect_5_over_6', mm(defect, high), scaled(high, F(5, 6)))
    return {'N': n, 'checks': checks,
            'actual_defect_matrix': [[str(v) for v in row] for row in defect],
            'required_defect_matrix': [[str(v) for v in row] for row in formula]}


def numerical_test(n):
    le, dv, t, dt, axial, transverse = geometry(n)
    p = t @ np.linalg.solve(dv, t.T)
    cv = np.linalg.inv(axial)[-len(dv):, -len(dv):]
    kd = t @ cv @ t.T
    offset = 0
    for lap in transverse:
        m = len(lap)//(n-1)
        kd[offset:offset+m, offset:offset+m] += np.linalg.inv(lap)[-m:, -m:]
        offset += m
    k = kd-p/n
    vals, vectors = np.linalg.eigh(dt)
    bvals = np.ones_like(vals)/n
    for j in range(1, n):
        angle = j*np.pi/(2*n)
        bvals += (2/n)*vals*np.cos(angle)**2/(vals+4*np.sin(angle)**2)
    b = (vectors*bvals) @ vectors.T
    ident = np.eye(len(dt))
    defect = ident-k
    formula = p/n+b @ (ident-p)
    gamma = 2*np.arcsinh(np.sqrt(vals)/2)
    closed = np.sqrt(vals*(vals+4))/2/np.tanh(n*gamma)-vals/2
    checks = []
    for label, error in [
        ('full_boundary_defect', np.max(np.abs(defect-formula))),
        ('gradient_rate', np.max(np.abs(defect @ p-p/n))),
        ('scalar_closed_form', np.max(np.abs(bvals-closed))),
        ('upper_fractional_bound', max(0., float(np.max(bvals-1/n-np.sqrt(vals))))),
        ('lower_bound', max(0., float(np.max(vals/(vals+4)-bvals))))]:
        checks.append({'label': label, 'actual_error': float(error),
                       'required_error': 1e-11, 'pass': bool(error < 1e-11)})
    return {'N': n, 'vertex_rows': len(dv), 'all_edge_rows': len(dt),
            'checks': checks, 'noise_eigenvalue_range': np.linalg.eigvalsh(k)[[0, -1]].tolist(),
            'defect_eigenvalue_range': np.linalg.eigvalsh(defect)[[0, -1]].tolist()}


def actual_product_test():
    # A realizable Q=u(v) cross u(v') circulation, not an arbitrary edge field.
    n = 4
    _, _, t, dt, _, _ = geometry(n)
    u = {(1, 1, 1): (1, 0, 0), (2, 1, 1): (0, 1, 0),
         (2, 2, 1): (-1, 0, 0), (1, 2, 1): (0, -1, 0)}
    q = []
    for mu in range(3):
        shape = [n if k == mu else n-1 for k in range(3)]
        for index in np.ndindex(*shape):
            v = tuple(index[k] if k == mu else index[k]+1 for k in range(3))
            w = tuple(v[k]+(k == mu) for k in range(3))
            q.append(int(np.cross(u.get(v, (0, 0, 0)), u.get(w, (0, 0, 0)))[2]))
    q = np.array(q, dtype=int)
    checks = []
    for label, value, wanted in [
        ('actual_Q_zero_divergence', int(np.max(np.abs(t.T @ q))), 0),
        ('actual_Q_squared_norm', int(q @ q), 4),
        ('actual_Q_laplacian_energy', int(q @ dt @ q), 28)]:
        checks.append({'label': label, 'actual': value, 'required': wanted, 'pass': value == wanted})
    return {'N': n, 'checks': checks, 'Q_third_color_all_edges': q.tolist(),
            'q_A': '1/2', 'analytic_Z_lower_bound': '7/32',
            'analytic_Z_over_q_A_lower_bound': '7/16',
            'qualification': 'Pointwise u test for every N>=4 by translation; not a cumulant or cutoff growth test'}


exact = exact_test()
numerical = numerical_test(4)
actual_product = actual_product_test()
checks = exact['checks'] + numerical['checks'] + actual_product['checks']
failures = [check for check in checks if not check['pass']]
out = Path(__file__).with_name('upper-noise-spectrum-certificate.json')
out.write_text(json.dumps({
    'scope': 'Actual unscaled relative cochain boundary covariance; all transverse end edges; no probe response',
    'exact': exact, 'numerical': numerical, 'actual_product': actual_product, 'failures': failures,
    'bounds': {'actual': 'Analytic L050: gradient defect=1/N; co-closed defect b_N(lambda)<=1/N+sqrt(lambda); operator norm>=1/2',
               'required': 'Complete a^2-scaled -kappa(f,r,Z+R)+E, cross-plaquette compensation, full log and reflected error<=c_box/2'},
}, indent=2)+'\n')
print(f"{'PASS' if not failures else 'FAIL'}: {len(exact['checks'])} exact and {len(numerical['checks'])} numerical checks; failures={len(failures)}")
print('Exact full-boundary identity error: '+exact['checks'][0]['actual_error']+'; required: 0.')
print(f"N=4 full-boundary identity error: {numerical['checks'][0]['actual_error']:.3g}; required: <1e-11 (diagnostic).")
print(f"Actual product: {len(actual_product['checks'])} exact integer checks; Z/q_A>=7/16 analytically, so no uniform o(1) relative defect.")
print('Actual analytic bounds: gradient=1/N, co-closed<=1/N+sqrt(lambda), norm>=1/2; no complete cumulant bound.')
print('Required: complete scaled response/log and reflected error<=c_box/2.')
print(f'Certificate: {out.relative_to(Path.cwd())}')
assert not failures
