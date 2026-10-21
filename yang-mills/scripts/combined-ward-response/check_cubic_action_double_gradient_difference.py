"""Exact L162 order/endpoint checks; no actual-probe or cutoff inference."""
from fractions import Fraction as Q
from pathlib import Path
import json


def tp(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def chain(*xs):
    a = xs[0]
    for b in xs[1:]:
        a = mm(a, b)
    return a


def eye(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def add(a, b, sign=1):
    return [[x+sign*y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, x):
    return [[x*y for y in row] for row in a]


def inv(a):
    n = len(a)
    work = [list(map(Q, row))+ident for row, ident in zip(a, eye(n))]
    for i in range(n):
        j = next(j for j in range(i, n) if work[j][i])
        work[i], work[j] = work[j], work[i]
        pivot = work[i][i]
        work[i] = [x/pivot for x in work[i]]
        for j in range(n):
            if j != i:
                multiple = work[j][i]
                work[j] = [x-multiple*y for x, y in zip(work[j], work[i])]
    return [row[n:] for row in work]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def hs2(a):
    return sum(x*x for row in a for x in row)


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def diag(v):
    return [[Q(v[i]) if i == j else Q(0) for j in range(len(v))] for i in range(len(v))]


def kron(a, b):
    return [[x*y for x in ar for y in br] for ar in a for br in b]


def ad(q):
    # Same bracket convention as L156/L161: [q,z]=-q cross z.
    x, y, z = q
    return [[Q(0), z, -y], [-z, Q(0), x], [y, -x, Q(0)]]


def block_ad(qs):
    blocks = [ad(q) for q in qs]
    return [[blocks[i//3][i % 3][j % 3] if i//3 == j//3 else Q(0)
             for j in range(3*len(qs))] for i in range(3*len(qs))]


def pivots(a):
    work = [row[:] for row in a]
    result = []
    for i in range(len(a)):
        pivot = work[i][i]
        result.append(pivot)
        if pivot <= 0:
            break
        for j in range(i+1, len(a)):
            for k in range(i+1, len(a)):
                work[j][k] -= work[j][i]*work[i][k]/pivot
    return result


identities = []


def check(name, actual, required):
    error = max(abs(x-y) for ar, br in zip(actual, required) for x, y in zip(ar, br))
    identities.append(dict(name=name, actual=actual, required=required, exact_error=error))


# Pinned path plus a second root edge: boundary potentials are absent,
# but every normal end edge is present. The columns are two cycles.
d = [[Q(x) for x in row] for row in
     [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1], [0, 1, 0]]]
s = [[Q(x) for x in row] for row in
     [[1, 0, 0], [1, 1, 0], [0, 1, 1], [0, 0, 1], [0, 1, 0]]]
cycles = tp([[Q(x) for x in row] for row in [[1, 1, 1, 1, 0], [1, 1, 0, 0, -1]]])
l = mm(cycles, tp(cycles))
sigma = inv(add(l, mm(d, tp(d))))
phi = [[Q(x) for x in row] for row in
       [[1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0]]]
f = mm(phi, sigma)
hat = lambda a: kron(a, eye(3))
dh, sh, fh = hat(d), hat(s), hat(f)
transport_records = []
for profile in ([2, -1, 4, 1, -2], [-3, 2, 0, 1, 5], [0, 0, 0, 0, 0]):
    qscalar = mv(l, profile)
    for color in range(3):
        qs = [[qscalar[e]*Q(c == color) for c in range(3)] for e in range(5)]
        w = block_ad(qs)
        div = [mv(tp(d), [q[c] for q in qs]) for c in range(3)]
        rhs = scale(block_ad(tp(div)), 2)
        name = f'profile={profile}, color={color}'
        o = chain(tp(dh), w, sh)
        moved = scale(chain(tp(sh), w, dh), -1)
        check(name+': co-closed column', rhs, scale(eye(9), 0))
        check(name+': pinned product identity', add(o, chain(tp(sh), w, dh)), rhs)
        check(name+': transported operator', o, moved)
        # Signed symmetric test matrix: no residual/probe interpretation.
        m = [[Q((i+1)*(j+1) % 7-3) for j in range(15)] for i in range(15)]
        original = tr(chain(o, fh, m, tp(fh)))
        transported = -tr(chain(tp(sh), w, dh, fh, m, tp(fh)))
        check(name+': ordered signed trace', [[original]], [[transported]])
        of2, mf2, f2 = hs2(mm(o, fh)), hs2(mm(m, tp(fh))), hs2(fh)
        mbound = max(sum(abs(x) for x in row) for row in m)
        transport_records.append(dict(name=name, q=qs, divergence=tp(div),
                                      original=original, transported=transported,
                                      actual_trace_squared=original**2,
                                      required_Cauchy_upper=of2*mf2,
                                      actual_MF_squared=mf2,
                                      required_matrix_norm_upper=mbound**2*f2,
                                      passed=original**2 <= of2*mf2 and mf2 <= mbound**2*f2))

# Non-co-closed control must keep the nonzero diagonal term.
control_q = [[Q(e+1), Q(2-e), Q((-1)**e)] for e in range(5)]
cw = block_ad(control_q)
cdiv = tp([mv(tp(d), [q[c] for q in control_q]) for c in range(3)])
crhs = scale(block_ad(cdiv), 2)
check('non-co-closed control: full diagonal retained',
      add(chain(tp(dh), cw, sh), chain(tp(sh), cw, dh)), crhs)
control_nonzero = any(x != 0 for row in crhs for x in row)

prefix_records = []
for mesh_n in (4, 6, 8):
    n = mesh_n-1
    b = [[Q(int(j == i+1)-int(j == i)) for j in range(mesh_n)] for i in range(n)]
    ld, le = mm(b, tp(b)), mm(tp(b), b)
    h = [[Q(j < i) for j in range(mesh_n)] for i in range(1, mesh_n)]
    maxial = [[Q(min(i+1, j+1)) for j in range(n)] for i in range(n)]
    check(f'N={mesh_n}: complete axial energy count', [[tr(mm(ld, maxial))]], [[Q(2*n)]])
    check(f'N={mesh_n}: axial trace count', [[tr(maxial)]], [[Q(n*(n+1), 2)]])
    end_count = dict(lower=Q(1), interior=Q(n-1), upper=Q(n))
    check(f'N={mesh_n}: both end contributions', [[sum(end_count.values())]], [[Q(2*n)]])
    for lam in (Q(1, 4), Q(1), Q(12, mesh_n**2)):
        ie = inv(add(le, scale(eye(mesh_n), lam)))
        gram = chain(h, ie, ie, tp(h))
        upper = scale(maxial, 1/lam**2)
        delta_v = add(ld, scale(eye(n), lam))
        actual = tr(mm(delta_v, gram))
        required = Q(2*n)/lam**2+Q(n*(n+1), 2)/lam
        check(f'N={mesh_n}, lambda={lam}: tensor energy upper formula',
              [[tr(mm(delta_v, upper))]], [[required]])
        pd = pivots(add(upper, gram, -1))
        prefix_records.append(dict(N=mesh_n, lambda_value=lam, F=mm(h, ie),
                                   squared_prefix=gram, dominating_matrix=upper,
                                   vertex_energy=delta_v, exact_positive_difference_pivots=pd,
                                   actual_energy=actual, required_energy_upper=required,
                                   axial_end_contributions=end_count,
                                   passed=0 <= actual <= required and len(pd) == n and all(x > 0 for x in pd)))

failures = [x['name'] for x in identities if x['exact_error']]
failures += [x['name'] for x in transport_records if not x['passed']]
failures += [f'prefix N={x["N"]}, lambda={x["lambda_value"]}' for x in prefix_records if not x['passed']]
if not control_nonzero:
    failures.append('non-co-closed control failed to detect retained diagonal')
certificate = dict(
    scope='Pinned graph transport/order checks and rational transverse-mass prefix energy checks; no actual-probe values or cutoff inference.',
    matrices=dict(D=d, S=s, L=l, Sigma=sigma, Phi=phi, F=f),
    identities=identities, transport_records=transport_records, prefix_records=prefix_records,
    non_co_closed_control=dict(q=control_q, divergence=cdiv, required_nonzero_diagonal=crhs,
                               nonzero_detected=control_nonzero),
    summary=dict(identity_count=len(identities), transport_case_count=len(transport_records),
                 prefix_case_count=len(prefix_records), maximum_exact_error=max(x['exact_error'] for x in identities),
                 required_exact_error=0, analytic_prefix_energy_bound='||D Phi Sigma||_HS^2 <= (9/8) N^5',
                 analytic_action_group_bound='O(N^(5/2)); a^3 limit zero',
                 required_complete_response='o(N^3); four E,E traces and both mixed limits unresolved'),
    failures=failures, passed=not failures)
path = Path(__file__).with_name('cubic-action-double-gradient-difference-certificate.json')
path.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f'Exact identities: {len(identities)}; signed transport cases: {len(transport_records)}; prefix cases: {len(prefix_records)}.')
print(f'Maximum exact error: {certificate["summary"]["maximum_exact_error"]}; required: 0; failures: {failures}.')
print('Analytical prefix energy <= (9/8) N^5; action double-gradient group O(N^(5/2)), below required N^3 scale.')
print('Complete response: unresolved; first four E,E traces and both mixed branch limits retained.')
print(f'Certificate: {path.relative_to(Path.cwd())}.')
assert not failures
