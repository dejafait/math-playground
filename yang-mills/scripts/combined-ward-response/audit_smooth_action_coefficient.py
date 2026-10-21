"""Independent raw Fourier-symbol replay of the complete L180 certificate.

Uses no production module or floating-point arithmetic. Analytic limits and
upstream heat intervals remain imported hypotheses; this audits their exact
local use only. Full comparisons, individual orders and endpoints go to disk.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path(__file__).with_name('smooth-action-coefficient-certificate.json')
saved = json.loads(SOURCE.read_text())
zero = (0, 0, 0, 0)
one = {zero: F(1)}


def plus(*ps):
    q = {}
    for p in ps:
        for z, c in p.items():
            q[z] = q.get(z, F(0)) + c
    return {z: c for z, c in q.items() if c}


def times(p, q):
    r = {}
    for z, c in p.items():
        for w, d in q.items():
            t = tuple(a+b for a, b in zip(z, w))
            r[t] = r.get(t, F(0)) + c*d
    return {z: c for z, c in r.items() if c}


def scaled(p, c):
    return {z: c*v for z, v in p.items() if c*v}


def star(p):
    return {tuple(-a for a in z): c for z, c in p.items()}


def monomial(j, n=1):
    return {tuple(n if j == k else 0 for k in range(4)): F(1)}


def axial_sum(p):
    q = {}
    for z, c in p.items():
        t = z[1:]
        q[t] = q.get(t, F(0)) + c
    return {z: c for z, c in q.items() if c}


def encode(p):
    return [dict(offset=list(z), coefficient=str(c)) for z, c in sorted(p.items())]


def decode(entries):
    p = {}
    for e in entries:
        z, c = tuple(e['offset']), F(e['coefficient'])
        assert len(z) == 3 and all(type(a) is int for a in z)
        assert z not in p and c != 0
        p[z] = c
    return p


# Raw tail-based Fourier rows: D_(rho,nu)=(z_rho-1)A_nu
# -(z_nu-1)A_rho. L is formed from all six oriented rows via D*D.
z = [monomial(j) for j in range(4)]
d = [plus(zj, scaled(one, -1)) for zj in z]
D = []
for rho, nu in combinations(range(4), 2):
    row = [{} for _ in range(4)]
    row[nu], row[rho] = d[rho], scaled(d[nu], -1)
    D.append(row)
L = [[plus(*(times(star(row[i]), row[j]) for row in D))
      for j in range(4)] for i in range(4)]
records, failures = [], []
source_records = {r['name']: r for r in saved['identities']}
assert len(source_records) == len(saved['identities']) == 17


def compare(name, independently_required, extra=None):
    r = source_records[name]
    actual, required, error = (decode(r[k]) for k in ('actual', 'required', 'error'))
    checks = dict(actual=actual == independently_required,
                  required=required == independently_required,
                  recorded_error=error == plus(actual, scaled(required, -1)),
                  zero_error=not error)
    if not all(checks.values()):
        failures.append(name)
    records.append(dict(name=name, independently_required=encode(independently_required),
                        saved_actual=r['actual'], saved_required=r['required'],
                        saved_error=r['error'], checks=checks, orders=extra))


for rho in range(4):
    K = [[{} for _ in range(4)] for _ in range(4)]
    for nu in range(4):
        if rho == nu:
            continue
        endpoint = scaled(plus(one, z[nu]), F(1, 2))
        clover = scaled(times(plus(one, star(z[rho])),
                              plus(one, star(z[nu]))), F(1, 4))
        filt = times(endpoint, clover)
        K[nu][nu] = times(filt, d[rho])
        K[nu][rho] = scaled(times(filt, d[nu]), -1)
    for mu in range(4):
        lk = plus(*(times(L[0][j], K[j][mu]) for j in range(4)))
        ktl = plus(*(times(star(K[j][0]), L[j][mu]) for j in range(4)))
        endpoint_sum = plus(one, z[mu])
        full = times(scaled(plus(lk, ktl), F(1, 2)), endpoint_sum)
        compare(f'Gamma_S_b{rho+1}_component{mu+1}', axial_sum(full),
                dict(LK=encode(axial_sum(times(lk, endpoint_sum))),
                     KstarL=encode(axial_sum(times(ktl, endpoint_sum))),
                     uncollapsed_GammaS=encode(full)))

# Independent diagonal pairing: algebra in the X variables, then substitute
# X_j=2-z_j-z_j^-1 into the asserted unordered-pair polynomial.
X = [plus(scaled(one, 2), scaled(z[j], -1), scaled(star(z[j]), -1))
     for j in (1, 2, 3)]
paired = plus(*(scaled(times(times(X[j], X[k]),
                             times(plus(X[j], scaled(X[k], -1)),
                                   plus(X[j], scaled(X[k], -1)))), F(-1, 4))
                for j, k in combinations(range(3), 2)))
compare('complete_diagonal_pairing', axial_sum(paired))

# Source values were matched to the canonical conclusion statements. Check
# every stored input and output, rather than trusting the passed flag.
g = (F('-0.061'), F('-0.043'))
inputs = {
    '3': {'G': ('2408.3740053', '2408.3740056'),
          'D': ('-237.289643', '-237.289642'),
          'R': ('1228.1260684', '1228.1260686'), 'P': ('2359.1', '2359.2'),
          'KR': ('-74.916', '-52.809'), 'KT': ('84000', '100000')},
    '6': {'G': ('5174.7326818', '5174.7326826'),
          'D': ('-98.877430', '-98.877429'),
          'R': ('451.5469823', '451.5469825'), 'P': ('703.6', '703.7'),
          'KR': ('-27.545', '-19.416'), 'KT': ('-47000', '-38000')},
}
assert tuple(map(F, saved['intervals']['g'])) == g
results = {}
for probe, entries in inputs.items():
    pairs = {k: tuple(map(F, v)) for k, v in entries.items()}
    assert {k: tuple(map(F, v)) for k, v in saved['intervals']['inputs'][probe].items()} == pairs
    corners = []
    for gv, G, diag, R, P, KR, KT in product(g, *(pairs[k] for k in ('G', 'D', 'R', 'P', 'KR', 'KT'))):
        BV = G-diag-R/2+P/2
        Vmix = -3*gv*BV
        corners.append(dict(point=[str(v) for v in (gv, G, diag, R, P, KR, KT)],
                            BV=str(BV), Vmix=str(Vmix), complete_response=str(KT+Vmix-6*KR)))
    hulls = {k: (min(F(c[k]) for c in corners), max(F(c[k]) for c in corners))
             for k in ('BV', 'Vmix', 'complete_response')}
    required = {'Vmix': (F(414), F(588)) if probe == '3' else (F(696), F(989)),
                'complete_response': (F(84730), F(101038)) if probe == '3' else (F(-46188), F(-36845))}
    checks = {k: hulls[k] == tuple(map(F, saved['intervals']['results'][probe][k])) for k in hulls}
    for k, req in required.items():
        checks['saved_required_'+k] = req == tuple(map(F, saved['intervals']['results'][probe]['required_'+('complete' if k == 'complete_response' else k)]))
        checks['inclusion_'+k] = req[0] < hulls[k][0] <= hulls[k][1] < req[1]
    if not all(checks.values()):
        failures.append('probe_'+probe+'_intervals')
    results[probe] = dict(corners=corners, hulls=hulls, required=required, checks=checks)
    for k, req in required.items():
        print(f'Probe {probe} {k}: actual {tuple(map(str, hulls[k]))}; required {tuple(map(str, req))}')

assert saved['passed'] is True and saved['failures'] == []
paths = ['lemmas/L180-smooth-action-coefficient-and-complete-cubic-nonvanishing.md',
         'lemmas/L179-smooth-action-signed-prefix-limit.md',
         'lemmas/L080-first-pair-diagnostic-continuum-limit.md',
         'lemmas/L132-other-other-actual-physical-heat-contractions.md',
         'lemmas/L140-other-other-g-cumulative-physical-contraction.md',
         'lemmas/L145-other-other-r-physical-contraction.md',
         'lemmas/L082-continuum-diagnostic-sign-enclosure.md',
         'lemmas/L133-other-other-actual-physical-heat-enclosures.md',
         'lemmas/L141-other-other-g-scalar-enclosure.md',
         'lemmas/L144-other-other-g-physical-heat-enclosures.md',
         'lemmas/L146-other-other-r-physical-heat-enclosures.md',
         'lemmas/L172-cubic-residual-third-scalar-exact-ibp.md',
         'lemmas/L174-action-hessian-complete-coefficient-contraction.md']
out = dict(scope='Independent complete raw Fourier-symbol and exact rational audit only; upstream analytic/IEEE premises imported',
           source_certificate_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
           inspected_input_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
           identities=records, intervals=results, failures=failures, passed=not failures)
path = Path(__file__).with_name('smooth-action-coefficient-audit-certificate.json')
path.write_text(json.dumps(out, default=str, indent=2)+'\n')
print(f'Complete comparisons: {len(records)}; endpoint corners: {sum(len(v["corners"]) for v in results.values())}; failures: {failures}')
print(f'Certificate: {path.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
