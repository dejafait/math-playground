"""Exact full raw-symbol checks and omitted-spectrum arithmetic for L145.

Rational Laurent coefficients are checked exhaustively, not sampled.
No retained spatial, time or torus quadrature is performed.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def add(*ps):
    out = {}
    for p in ps:
        for power, value in p.items():
            out[power] = out.get(power, F(0)) + value
    return {k: v for k, v in out.items() if v}


def scale(p, v):
    return {k: v * x for k, x in p.items() if v * x}


def mul(*ps):
    out = {(0, 0, 0): F(1)}
    for p in ps:
        new = {}
        for a, v in out.items():
            for b, w in p.items():
                key = tuple(x + y for x, y in zip(a, b))
                new[key] = new.get(key, F(0)) + v * w
        out = {k: v for k, v in new.items() if v}
    return out


def shift(a, n):
    key = [0, 0, 0]
    key[a] = n
    return {tuple(key): F(1)}


def conj(p):
    return {tuple(-n for n in k): v for k, v in p.items()}


def even(p):
    for a in range(3):
        reflected = {tuple(-n if j == a else n for j, n in enumerate(k)): v
                     for k, v in p.items()}
        p = scale(add(p, reflected), F(1, 2))
    return p


def mm(a, b):
    return [[add(*(mul(a[i][k], b[k][j]) for k in range(len(b))))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a):
    return [[conj(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]


def rational(v):
    v = F(v)
    return dict(numerator=v.numerator, denominator=v.denominator)


def encode(p):
    return {','.join(map(str, k)): rational(v) for k, v in sorted(p.items())}


records = []


def check(name, actual, required):
    diff = add(actual, scale(required, -1))
    records.append(dict(identity=name, actual=encode(actual), required=encode(required),
                        difference=encode(diff), passed=not diff))


one = {(0, 0, 0): F(1)}
e = [shift(a, 1) for a in range(3)]
ei = [shift(a, -1) for a in range(3)]
tau = [add(one, scale(x, -1)) for x in e]
d = [add(one, x) for x in e]
p = [scale(add(e[a], scale(ei[a], -1)), F(1, 2)) for a in range(3)]  # i sin
x = [add(scale(one, 2), scale(e[a], -1), scale(ei[a], -1)) for a in range(3)]
eta2 = [scale(add(scale(one, 2), e[a], ei[a]), F(1, 4)) for a in range(3)]
lam = add(*x)
qnum = [[add(lam if a == b else {}, scale(mul(tau[a], conj(tau[b])), -1))
         for b in range(3)] for a in range(3)]
wc = [[scale(mul(add(one, ei[a]), p[a]), F(1, 2)) for a in range(3)]]
planes = [(0, 1), (0, 2), (1, 2)]
c, bpath, qpath = [], [], []
for a, b in planes:
    c.append([tau[b] if j == a else scale(tau[a], -1) if j == b else {}
              for j in range(3)])
    bpath.append([one if j == a else e[a] if j == b else {} for j in range(3)])
    qpath.append([scale(e[b], -1) if j == a else e[a] if j == b else {}
                  for j in range(3)])

omegas = []
for v in range(3):
    z = [[add(scale(qpath[j][r], int(v in (a, b))),
              scale(bpath[j][r], int(v == a) - int(v == b))) for r in range(3)]
         for j, (a, b) in enumerate(planes)]
    zc, cz = mm(adj(z), c), mm(adj(c), z)
    omega = [[add(zc[a][b], scale(cz[a][b], -1)) for b in range(3)]
             for a in range(3)]
    omegas.append(omega)
    lift = mm(mm(adj(c), z), [[t] for t in tau])
    for a in range(3):
        check(f'c-star-z-v{v+2}-tau-component-{a+2}', lift[a][0],
              mul(qnum[a][v], d[v]))
    projected = mm(mm(qnum, omega), qnum)
    for a in range(3):
        for b in range(3):
            check(f'projected-omega-v{v+2}-entry-{a+2}{b+2}', projected[a][b],
                  scale(mul(p[v], lam, qnum[a][b]), 4))

# Exact raw numerator of L107 after c*z*tau = lambda q Dv.
# The full integrand is this numerator divided by 2 lambda^3.
square_sum = add(*(mul(t, t) for t in x))
diagonals = []
for left in range(3):
    row = mm(mm(mm(wc, qnum), omegas[left]), qnum)[0]
    for right in range(3):
        raw = mul(row[right], d[right])
        diag = mul(x[right], eta2[right],
                   add(mul(x[right], lam), scale(square_sum, -1)))
        required = scale(mul(lam, diag), 2) if left == right else {}
        check(f'full-raw-parity-vl{left+2}-vk{right+2}', even(raw), required)
        if left == right:
            diagonals.append(diag)

pair_square = add(*(mul(x[a], x[b], add(x[a], scale(x[b], -1)),
                        add(x[a], scale(x[b], -1))) for a, b in planes))
check('complete-diagonal-sum-equals-G-numerator', add(*diagonals),
      scale(pair_square, F(-1, 4)))

cutoff = 96
c_r = F(1296 * 165 * 3, 4)
prefactor = F(2 * (4 * 12**4) * (16 * 12**3) * 512, 9 * cutoff)
bound = c_r * 1640736 * prefactor / 20**27
required = F(1, 10**12)
certificate = dict(
    method='Exact rational full raw Laurent matrix products and all coordinate reflections',
    qualification='No retained evaluation; analytic integration and convergence are proved in L145.',
    algebra=records,
    tail=dict(cutoff=cutoff, C_R=rational(c_r), full_probe_norm=1640736,
              exponent=rational(F(9*cutoff*cutoff, 1024)), H_prefactor=rational(prefactor),
              B_actual_upper_bound=rational(bound), K_actual_upper_bound=rational(bound/4),
              required=rational(required), passed=bound < required),
)
certificate['failures'] = [r['identity'] for r in records if not r['passed']]
if not certificate['tail']['passed']:
    certificate['failures'].append('full-spectrum-tail')
certificate['passed'] = not certificate['failures']
path = Path(__file__).with_name('r-physical-reduction-certificate.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f"Exact full-symbol checks: {sum(r['passed'] for r in records)}/{len(records)}")
print(f"K={cutoff} B omission <{float(bound):.9g}; R omission <{float(bound/4):.9g}; required <{float(required):.9g}")
print(f"Failures: {certificate['failures']}")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(0 if certificate['passed'] else 1)
