"""Exact L160 pinned-block and prefix checks; no actual-probe computation."""
from fractions import Fraction as F
from pathlib import Path
import json


def tp(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def chain(*xs):
    result = xs[0]
    for item in xs[1:]:
        result = mm(result, item)
    return result


def inv(a):
    n = len(a)
    rows = [list(map(F, row))+ident for row, ident in zip(a, eye(n))]
    for i in range(n):
        j = next(j for j in range(i, n) if rows[j][i])
        rows[i], rows[j] = rows[j], rows[i]
        pivot = rows[i][i]
        rows[i] = [value/pivot for value in rows[i]]
        for j in range(n):
            if j != i:
                factor = rows[j][i]
                rows[j] = [x-factor*y for x, y in zip(rows[j], rows[i])]
    return [row[n:] for row in rows]


identities = []


def check(name, actual, required):
    error = max(abs(x-y) for ar, br in zip(actual, required)
                for x, y in zip(ar, br))
    identities.append(dict(name=name, actual=actual, required=required,
                           maximum_exact_error=error))


# A pinned graph with two cycle directions and three gradient directions.
# Its entire matrices are retained; its role is exact algebra verification.
d = [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1], [0, 1, 0]]
cycles = tp([[1, 1, 1, 1, 0], [1, 1, 0, 0, -1]])
lmat = mm(cycles, tp(cycles))
delta = add(lmat, mm(d, tp(d)))
sigma = inv(delta)
delta_v = mm(tp(d), d)
phi = [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]]
r = add(eye(5), mm(d, phi), -1)
k = chain(phi, sigma, tp(phi))
e = add(chain(r, sigma, tp(r)), chain(d, k, tp(d)), -1)
p = mm(sigma, lmat)
q = add(eye(5), p, -1)
zero = [[F(0)]*5 for _ in range(5)]
check('prefix is a left inverse of the pinned gradient', mm(phi, d), eye(3))
check('signed E expansion', e,
      add(add(sigma, chain(d, phi, sigma), -1),
          chain(sigma, tp(phi), tp(d)), -1))
check('P is symmetric', p, tp(p))
check('P is a projector', mm(p, p), p)
check('P and Q are orthogonal', mm(p, q), zero)
check('Q is the gradient projector', q, chain(d, inv(delta_v), tp(d)))
check('co-closed signed block', chain(p, e, p), mm(sigma, p))
check('gradient signed block', chain(q, e, q),
      [[-x for x in row] for row in mm(sigma, q)])
check('off-diagonal signed block', chain(q, e, p),
      [[-x for x in row] for row in chain(d, phi, sigma, p)])
check('off-diagonal transpose', chain(p, e, q), tp(chain(q, e, p)))
energy_square = add(add(sigma, chain(d, phi, sigma, p, tp(phi), tp(d))),
                    chain(sigma, p, tp(phi), tp(d), delta, d, phi, sigma, p))
check('unwhitened square of the exact energy blocks',
      chain(e, delta, e), energy_square)


prefix_records = []
packet_records = []
for mesh_n in (4, 8, 16, 32, 64):
    n = mesh_n-1
    ld = [[F(2 if i == j else -1 if abs(i-j) == 1 else 0)
           for j in range(n)] for i in range(n)]
    h = [[F(r < s) for r in range(mesh_n)] for s in range(1, mesh_n)]
    b = [[F(int(r == s)-int(r == s-1)) for r in range(mesh_n)]
         for s in range(1, mesh_n)]
    m = list(map(F, range(1, mesh_n)))
    actual_ldh = mm(ld, h)
    required_ldh = [[-b[i][j]+int(i == n-1) for j in range(mesh_n)]
                    for i in range(n)]
    check(f'N={mesh_n}: full pinned prefix Laplacian', actual_ldh, required_ldh)
    actual_ldm = mv(ld, m)
    required_ldm = [F(mesh_n*int(i == n-1)) for i in range(n)]
    check(f'N={mesh_n}: pinned upper linear-prefix jump',
          [[x] for x in actual_ldm], [[x] for x in required_ldm])
    prefix_records.append(dict(N=mesh_n, H=h, B=b, L_D=ld,
                               actual_L_D_m=actual_ldm))
    for lam in (F(1, 4), F(1), F(5, 2), F(12, mesh_n**2)):
        applied = mv(add(ld, [[lam*x for x in row] for row in eye(n)]), m)
        actual = sum(x*x for x in applied)/(mesh_n*lam)
        required = (F(mesh_n)/lam+2*n+lam*F(n*(2*mesh_n-1), 6))
        omitted_endpoint = lam*sum(x*x for x in m)/mesh_n
        endpoint_difference = F(mesh_n)/lam+2*n
        check(f'N={mesh_n}, lambda={lam}: complete energy packet',
              [[actual]], [[required]])
        check(f'N={mesh_n}, lambda={lam}: effect of omitting the upper jump',
              [[actual-omitted_endpoint]], [[endpoint_difference]])
        packet_records.append(dict(N=mesh_n, lambda_value=lam,
                                   actual_squared_norm=actual,
                                   required_squared_norm=required,
                                   error=actual-required,
                                   omitted_upper_endpoint_squared_norm=omitted_endpoint,
                                   missing_endpoint_contribution=endpoint_difference))

failures = [item['name'] for item in identities if item['maximum_exact_error']]
maximum_error = max(item['maximum_exact_error'] for item in identities)
path = Path(__file__).with_name('signed-remainder-energy-certificate.json')
certificate = dict(
    scope='Exact pinned graph blocks and axial prefix identities. Rational lambda checks are not actual sine eigenvalues; no probe response or cutoff inference.',
    graph=dict(D=d, L=lmat, Delta=delta, Sigma=sigma, Phi=phi, E=e, P=p, Q=q),
    identities=identities, prefix_records=prefix_records, packets=packet_records,
    summary=dict(identity_count=len(identities), packet_count=len(packet_records),
                 maximum_exact_error=maximum_error, required_error=F(0),
                 analytic_actual_cube_lower_bound='||W||^2 >= 1+N^3/(3*pi^2)',
                 proposed_shortcut_required_bound='||W|| <= C independent of N',
                 result='Global uniform Hodge-energy remainder bound is false; actual E,E response remains unresolved.'),
    failures=failures, passed=not failures)
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Exact identities: {len(identities)}; complete packets: {len(packet_records)}.')
print(f'Maximum exact error: {maximum_error}; required: 0; failures: {len(failures)}.')
print('Actual-cube analytic bound: ||W||^2 >= 1+N^3/(3*pi^2); shortcut requires ||W||=O(1).')
print('No actual-probe or signed E,E response bound is certified.')
print(f'Certificate: {path}')
if failures:
    raise SystemExit(1)
