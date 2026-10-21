"""Exact L161 tensor-order checks, not actual-probe or cutoff values."""
from fractions import Fraction as Q
from pathlib import Path
import json


def tp(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def chain(*matrices):
    a = matrices[0]
    for b in matrices[1:]:
        a = mm(a, b)
    return a


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def scale(a, x):
    return [[x*y for y in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def inv(a):
    n = len(a)
    rows = [list(map(Q, row))+ident for row, ident in zip(a, eye(n))]
    for i in range(n):
        j = next(j for j in range(i, n) if rows[j][i])
        rows[i], rows[j] = rows[j], rows[i]
        pivot = rows[i][i]
        rows[i] = [x/pivot for x in rows[i]]
        for j in range(n):
            if j != i:
                multiple = rows[j][i]
                rows[j] = [x-multiple*y for x, y in zip(rows[j], rows[i])]
    return [row[n:] for row in rows]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def kron(a, b):
    return [[x*y for x in ar for y in br] for ar in a for br in b]


def epsilon(i, j, k):
    if len({i, j, k}) < 3:
        return 0
    return (-1)**sum(x > y for x, y in ((i, j), (i, k), (j, k)))


def bracket(a, b):
    return [a[2]*b[1]-a[1]*b[2], a[0]*b[2]-a[2]*b[0], a[1]*b[0]-a[0]*b[1]]


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def bh(h):
    # The endpoint sum on the four-edge pinned path, with both ends zero.
    return [[s[e][v]*bracket(h[3*e:3*e+3], eye(3)[c])[color]
             for v in range(3) for c in range(3)]
            for e in range(4) for color in range(3)]


def action_matrix(h):
    # Direct ordered action Taylor tensor: T=-omega*epsilon/12.
    return [[-sum(h[alpha]*epsilon(alpha//3, beta//3, gamma//3)
                  *epsilon(alpha % 3, beta % 3, gamma % 3)
                  for alpha in range(12))/Q(12)
             for gamma in range(12)] for beta in range(12)]


identities = []


def check(name, actual, required):
    error = max(abs(x-y) for ar, br in zip(actual, required) for x, y in zip(ar, br))
    identities.append(dict(name=name, actual=actual, required=required, exact_error=error))


d = [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1]]
s = [[1, 0, 0], [1, 1, 0], [0, 1, 1], [0, 0, 1]]
l = [[Q(1)]*4 for _ in range(4)]
sigma = inv(add(l, mm(d, tp(d))))
phi = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0]]
cross = mm(phi, sigma)
r = add(eye(4), scale(mm(d, phi), -1))
e = add(add(sigma, scale(mm(d, cross), -1)), scale(mm(tp(cross), tp(d)), -1))
hat = lambda a: kron(a, eye(3))
dh, sh, fh, eh, lh = hat(d), hat(sigma), hat(cross), hat(e), hat(l)
records = []
profiles = [([1, 2, -1, 3], [2, -1, 4, 1], False),
            ([0, 1, 0, -1], [1, 3, 2, -2], False),
            ([1, 2, -1, 3], [2, -1, 4, 1], True)]
for rho in (Q(2), Q(-3)):
    ah = scale(lh, rho/2)
    for profile_index, (hk, hl, retract) in enumerate(profiles):
        if retract:
            hk, hl = mv(r, hk), mv(r, hl)
        for color in range(3):
            h = [x*int(c == color) for x in hk for c in range(3)]
            ell = [x*int(c == color) for x in hl for c in range(3)]
            m, n = scale(action_matrix(h), rho), action_matrix(ell)
            bah, bl = bh(mv(ah, h)), bh(mv(lh, ell))
            qa = add(mm(ah, bh(h)), scale(bah, -1))
            ql = add(mm(lh, bh(ell)), scale(bl, -1))
            name = f'rho={rho}, profile={profile_index}, color={color}'
            check(name+': residual single-gradient identity', mm(m, dh), scale(qa, -Q(1, 6)))
            check(name+': action single-gradient identity', mm(n, dh), scale(ql, -Q(1, 12)))
            check(name+': residual double-gradient identity', chain(tp(dh), m, dh),
                  scale(mm(tp(dh), bah), Q(1, 6)))
            check(name+': action double-gradient identity', chain(tp(dh), n, dh),
                  scale(mm(tp(dh), bl), Q(1, 12)))
            terms = [
                -36*tr(chain(m, sh, n, sh)),
                -12*tr(chain(qa, fh, n, sh)),
                -6*tr(chain(ql, fh, m, sh)),
                -tr(chain(qa, fh, ql, fh)),
                -6*tr(chain(tp(dh), bah, fh, n, tp(fh))),
                -3*tr(chain(tp(dh), bl, fh, m, tp(fh)))]
            # Independent index contraction of the original two E lines.
            direct = -36*sum(m[b][c]*n[u][v]*eh[b][u]*eh[c][v]
                             for b in range(12) for c in range(12)
                             for u in range(12) for v in range(12))
            check(name+': full six-trace reduction', [[direct]], [[sum(terms)]])
            record = dict(name=name, h=h, ell=ell, residual_scale=rho,
                          direct=direct, ordered_six_terms=terms, reduced=sum(terms),
                          exact_error=direct-sum(terms))
            records.append(record)


prefix_records = []
for mesh_n in (4, 6, 8):
    nv = mesh_n-1
    b = [[Q(int(j == i+1)-int(j == i)) for j in range(mesh_n)] for i in range(nv)]
    le, ld = mm(tp(b), b), mm(b, tp(b))
    hprefix = [[Q(j < i) for j in range(mesh_n)] for i in range(1, mesh_n)]
    maxial = [[Q(min(i+1, j+1)) for j in range(nv)] for i in range(nv)]
    for lam in (Q(1, 4), Q(1), Q(12, mesh_n**2)):
        ie = inv(add(le, scale(eye(mesh_n), lam)))
        rv = inv(add(ld, scale(eye(nv), lam)))
        actual = chain(hprefix, ie, ie, tp(hprefix))
        positive_difference = add(scale(rv, 1/lam**2), scale(mm(rv, rv), 1/lam))
        bound_matrix = scale(maxial, 1/lam**2)
        required = add(bound_matrix, scale(positive_difference, -1))
        check(f'N={mesh_n}, lambda={lam}: squared prefix identity', actual, required)
        # Exact LDL pivots test the asserted positive difference in these cases.
        work = [list(row) for row in positive_difference]
        pivots = []
        for j in range(nv):
            pivot = work[j][j]
            pivots.append(pivot)
            if pivot <= 0:
                break
            for row in range(j+1, nv):
                for col in range(j+1, nv):
                    work[row][col] -= work[row][j]*work[j][col]/pivot
        prefix_records.append(dict(N=mesh_n, lambda_value=lam,
                                   squared_prefix=actual, required=required,
                                   actual_trace=tr(actual), required_trace_upper=tr(bound_matrix),
                                   positive_difference=positive_difference, exact_LDL_pivots=pivots,
                                   passed=len(pivots) == nv and all(x > 0 for x in pivots)
                                   and 0 <= tr(actual) <= tr(bound_matrix)))

failures = [item['name'] for item in identities if item['exact_error']]
failures += [f'prefix N={item["N"]}, lambda={item["lambda_value"]}'
             for item in prefix_records if not item['passed']]
certificate = dict(
    scope='Exact pinned-cycle action tensors with scaled residual, all six traces and squared-prefix identities; no actual probes or cutoff inference.',
    matrices=dict(D=d, S=s, L=l, Sigma=sigma, Phi=phi, F=cross, E=e, R=r),
    identities=identities, complete_contractions=records, prefix_records=prefix_records,
    summary=dict(identity_count=len(identities), contraction_count=len(records),
                 prefix_case_count=len(prefix_records), maximum_exact_error=max(x['exact_error'] for x in identities),
                 required_exact_error=0, analytic_prefix_bound='||Phi Sigma||_HS^2 <= C N^6',
                 analytic_residual_double_gradient_bound='O(N), hence zero a^3 limit',
                 analytic_action_double_gradient_bound='O(N^3); scaled limit unresolved'),
    failures=failures, passed=not failures)
path = Path(__file__).with_name('cubic-ee-gauge-reduction-certificate.json')
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Exact identities: {len(identities)}; full contractions: {len(records)}; prefix cases: {len(prefix_records)}.')
print(f'Maximum exact error: {certificate["summary"]["maximum_exact_error"]}; required: 0; failures: {failures}.')
print('Analytic bounds: squared prefix <= C N^6; residual two-gradient O(N); action two-gradient O(N^3).')
print('Required complete-response threshold: o(N^3); four traces and cubic action coefficient remain unresolved.')
print(f'Certificate: {path.relative_to(Path.cwd())}.')
assert not failures
