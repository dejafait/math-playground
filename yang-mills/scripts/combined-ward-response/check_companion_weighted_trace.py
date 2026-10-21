"""Exact complete finite identities for L043; asymptotic bounds are analytic."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

O = (0, 0, 0)

def shift(n, j, s):
    return tuple(x + (s if k == j else 0) for k, x in enumerate(n))

def central(f, n, j):
    return (f(shift(n, j, 1))-f(shift(n, j, -1)))/2

def lap(f, n, j=None):
    return sum(2*f(n)-f(shift(n, k, 1))-f(shift(n, k, -1))
               for k in (range(3) if j is None else (j,)))

def green(n):
    # Complete kernel entries needed by the radius-two row. They obey
    # reflection/permutation symmetry, Delta g(0)=1, Delta g(+/-e_j)=0.
    radius = sum(abs(x) for x in n)
    if radius == 0:
        return F(1)
    if radius == 1:
        return F(5, 6)
    if radius == 2:
        return F(4, 5)
    raise ValueError("Stencil left its complete radius-two support")

def residual_diagonal(u):
    def w(n, j):
        return central(lambda y: u(y, j), n, j)
    def s(n, j, k):
        return central(lambda y: u(y, k), n, j)+central(lambda y: u(y, j), n, k)
    def kg(n):
        return sum(u(n, j)*central(green, n, j) for j in range(3))
    # K^T Delta g has zero diagonal because Delta g(+/-e_j)=0.
    sym = lap(kg, O)/2
    q3 = sum((w(O, j)+w(shift(O, j, sign), j))/2
             * (green(O)-green(shift(O, j, sign)))
             for j in range(3) for sign in (-1, 1))
    q6 = -sum((central(lambda n: s(n, j, k)*central(green, n, k), O, j)
               +central(lambda n: s(n, j, k)*central(green, n, j), O, k))/2
              for j in range(3) for k in range(j+1, 3))
    divergence = sum(w(O, j) for j in range(3))
    second = sum(lap(lambda n: w(n, j), O, j) for j in range(3))
    expected = F(-7, 30)*divergence+second/12
    return sym-q3-q6, expected, q6

records = []
positions = [n for n in product(range(-2, 3), repeat=3) if sum(abs(x) for x in n) <= 2]
for component in range(3):
    for position in positions:
        actual, expected, q6 = residual_diagonal(
            lambda n, k: F(k == component and n == position))
        records.append(dict(check="complete_coefficient_basis", component=component+2,
                            position=position, actual=str(actual), expected=str(expected),
                            shear_diagonal=str(q6), defect=str(actual-expected),
                            passed=actual == expected and q6 == 0))
# A divergence-free local stream polynomial has a nonzero second-order term.
def stream_u(n, k):
    x, _, z = n
    return F(x**3 if k == 0 else -(3*x*x+1)*z if k == 2 else 0)
actual, expected, q6 = residual_diagonal(stream_u)
records.append(dict(check="divergence_free_second_order_example", actual=str(actual),
                    expected="-1/2", defect=str(actual+F(1, 2)),
                    passed=actual == expected == F(-1, 2) and q6 == 0))


def graph(nmesh):
    vertices = list(product(range(1, nmesh), repeat=3))
    ids = {v: k for k, v in enumerate(vertices)}
    edges = []
    for j in range(3):
        for transverse in product(range(1, nmesh), repeat=2):
            for t in range(nmesh):
                v = list(transverse)
                v.insert(j, t)
                w = v.copy()
                w[j] += 1
                edges.append((ids.get(tuple(v)), ids.get(tuple(w))))
    return vertices, edges


def trace_identity(p, r, nvertices, edges):
    def entry(m, v, w):
        return F(0) if v is None or w is None else m.get(tuple(sorted((v, w))), F(0))
    diagp = [entry(p, v, v) for v in range(nvertices)]
    diagr = [entry(r, v, v) for v in range(nvertices)]
    lap_p = [F(0)]*nvertices
    lap_rdiag = [F(0)]*nvertices
    actual = F(0)
    last = F(0)
    for v, w in edges:
        pv, pw = entry(p, v, v), entry(p, w, w)
        rv, rw = entry(r, v, v), entry(r, w, w)
        pab, rab = entry(p, v, w), entry(r, v, w)
        actual += pv*rw+pw*rv-2*pab*rab
        last += (pv+pw-2*pab)*rab
        if v is not None:
            lap_p[v] += pv-pw
            lap_rdiag[v] += rv-rab
        if w is not None:
            lap_p[w] += pw-pv
            lap_rdiag[w] += rw-rab
    expected = sum(diagp[v]*lap_rdiag[v]-lap_p[v]*diagr[v]
                   for v in range(nvertices))+last
    return actual, expected

for nmesh in (2, 3):
    vertices, edges = graph(nmesh)
    pairs = [(v, w) for v in range(len(vertices)) for w in range(v, len(vertices))]
    for pkey, rkey in product(pairs, repeat=2):
        actual, expected = trace_identity({pkey: F(1)}, {rkey: F(1)}, len(vertices), edges)
        records.append(dict(check="complete_symmetric_matrix_basis", N=nmesh,
                            P_basis=pkey, R_basis=rkey, defect=str(actual-expected),
                            passed=actual == expected))
vertices, edges = graph(4)
for test in range(12):
    p = {(v, w): F(((v+2)*(w+3)+test*7) % 17-8, 3)
         for v in range(len(vertices)) for w in range(v, len(vertices))}
    r = {(v, w): F(((v+5)*(w+1)+test*11) % 19-9, 5)
         for v in range(len(vertices)) for w in range(v, len(vertices))}
    actual, expected = trace_identity(p, r, len(vertices), edges)
    records.append(dict(check="dense_symmetric_matrix", N=4, test=test,
                        defect=str(actual-expected), passed=actual == expected))
failures = [x for x in records if not x['passed']]
certificate = dict(scope="Exact finite edge-trace and complete local coefficient identities; no numerical asymptotic verification.",
                   records=records, failures=failures, passed=not failures,
                   actual_maximum_identity_defect="0" if not failures else "nonzero",
                   required_maximum_identity_defect="0",
                   analytic_result="L043 proves T_i,a=O(a^-2) including boundary strips; the rate follows from its analytic energy estimate.",
                   achieved_asymptotic_bound="O(a^-2)", required_stronger_power_threshold="O(a^-2)",
                   unresolved="Existence/value of a^2 T_i,a and comparison with +48 I_i; full response/logarithm and reflected error <=c_box/2.")
path = Path(__file__).with_name('companion-weighted-trace-certificate.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f'Exact identity records: {len(records)}; failures: {len(failures)}')
print('Actual/required identity defect:', certificate['actual_maximum_identity_defect'], '/ 0')
print('Analytic bound/required stronger-power threshold: O(a^-2) / O(a^-2)')
print('Scaled limit and cancellation remain unverified; certificate:', path)
if failures:
    raise SystemExit(1)
