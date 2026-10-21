"""Independent exact Laurent checks of L219; no sampled frequencies.

Variables z_j=exp(i theta_j/2), six independent real skew entries,
and real/imaginary parts of an arbitrary prefix amplitude. Coefficients
are Gaussian rationals, represented by a final exponent of i modulo 2.
No production contraction routines are imported.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

DIM = 13
ZERO = (0,) * DIM


def const(c):
    return {ZERO: F(c)} if c else {}


def var(j):
    e = list(ZERO)
    e[j] = 1
    return {tuple(e): F(1)}


def add(*args):
    out = {}
    for p in args:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(c, p):
    return {e: F(c)*v for e, v in p.items() if c*v}


def mul(*args):
    out = const(1)
    for p in args:
        nxt = {}
        for e, c in out.items():
            for h, v in p.items():
                k = [a+b for a, b in zip(e, h)]
                sign = (-1)**(k[-1]//2)
                k[-1] %= 2
                k = tuple(k)
                nxt[k] = nxt.get(k, F(0)) + sign*c*v
        out = {e: c for e, c in nxt.items() if c}
    return out


def conj(p):
    out = {}
    for e, c in p.items():
        h = tuple(-v if j < 4 else v for j, v in enumerate(e))
        out[h] = c*(-1)**e[-1]
    return out


def sub(p, q):
    return add(p, scale(-1, q))


def matmul(a, b):
    return [[add(*(mul(a[j][k], b[k][l]) for k in range(len(b))))
             for l in range(len(b[0]))] for j in range(len(a))]


def row(j, p):
    return [p if k == j else {} for k in range(4)]


def pair(a, w, b):
    return add(*(mul(a[j], w[j][k], conj(b[k]))
                 for j in range(4) for k in range(4)))


checks = []


def check(name, p):
    checks.append({'name': name, 'required': 'zero Laurent polynomial',
                   'actual_nonzero_coefficients': len(p),
                   'complete_defect': [{'powers': e, 'coefficient': str(c)}
                                       for e, c in sorted(p.items())],
                   'passed': not p})


one, I = const(1), var(12)
z = [var(j) for j in range(4)]
d = [mul(scale(-1, I), sub(v, conj(v))) for v in z]
eta = [scale(F(1, 2), add(v, conj(v))) for v in z]
energy = add(*(mul(v, v) for v in d))

# Reconstruct the original four-plaquette site clover and endpoint
# average in lower-vertex coordinates, separately for each u_rho.
for rho in range(4):
    raw = [[{} for _ in range(4)] for _ in range(4)]
    for a in range(4):
        if a == rho:
            continue
        filt = scale(F(1, 8), mul(add(one, mul(z[a], z[a])),
                    add(one, mul(conj(z[rho]), conj(z[rho]))),
                    add(one, mul(conj(z[a]), conj(z[a])))))
        raw[a][a] = mul(filt, sub(mul(z[rho], z[rho]), one))
        raw[a][rho] = scale(-1, mul(filt, sub(mul(z[a], z[a]), one)))
    for a in range(4):
        for b in range(4):
            centered = mul(conj(z[a]), raw[a][b], z[b])
            wanted = mul(I, eta[a], eta[a], eta[rho],
                         sub(d[rho] if a == b else {}, d[a] if b == rho else {}))
            check(f'raw_generator_u{rho+1}_{a+1}{b+1}', sub(centered, wanted))

# For arbitrary skew Q, verify every coefficient in the three direct
# and both mixed contractions, without using Q's particular formula.
Q = [[{} for _ in range(4)] for _ in range(4)]
for j, (a, b) in enumerate(combinations(range(4), 2)):
    Q[a][b] = var(4+j)
    Q[b][a] = scale(-1, Q[a][b])
W = [[mul(I, p) for p in r] for r in Q]
s = add(var(10), mul(I, var(11)))
H = [
    [[1,2,1,2],[2,0,2,6],[1,2,1,2],[2,6,2,0]],
    [[0,2,6,2],[2,1,2,1],[6,2,0,2],[2,1,2,1]],
    [[0,3,0,-3],[3,0,-3,0],[0,-3,0,3],[-3,0,3,0]],
]
for mu, nu in combinations(range(1, 4), 2):
    common = conj(mul(z[mu], z[nu]))
    # Raw selectors include the input edge-center phase.
    direct = [row(mu, mul(common, z[mu])),
              row(nu, mul(common, z[mu], z[mu], z[nu])),
              row(mu, scale(-1, mul(common, z[nu], z[nu], z[mu]))),
              row(nu, scale(-1, mul(common, z[nu])))]
    endminusstart = [sub(mul(z[mu], z[mu]), one),
                    mul(z[mu], z[mu], sub(mul(z[nu], z[nu]), one)),
                    mul(z[nu], z[nu], sub(one, mul(z[mu], z[mu]))),
                    sub(one, mul(z[nu], z[nu]))]
    prefix = [row(0, mul(common, v, s)) for v in endminusstart]
    components = (mu, nu, mu, nu)
    for l, n in enumerate(components):
        check(f'raw_endpoint_plane{mu+1}{nu+1}_row{l+1}',
              sub(prefix[l][0], mul(direct[l][n], I, d[n], s)))
    zQ = sub(mul(d[mu], Q[nu][0]), mul(d[nu], Q[mu][0]))
    brackets = [
        sub(mul(d[mu], d[nu], zQ), scale(12, mul(eta[mu], eta[mu], d[nu], Q[nu][0]))),
        sub(scale(-1, mul(d[mu], d[nu], zQ)), scale(12, mul(eta[nu], eta[nu], d[mu], Q[mu][0]))),
        scale(12, mul(eta[mu], eta[nu], add(mul(d[nu], Q[mu][0]), mul(d[mu], Q[nu][0])))),
    ]
    for k, h in enumerate(H):
        dd = add(*(scale(h[l][m], pair(direct[l], W, direct[m]))
                   for l in range(4) for m in range(4)))
        mixed = add(*(scale(-h[l][m], add(pair(direct[l], W, prefix[m]),
                                         pair(prefix[l], W, direct[m])))
                      for l in range(4) for m in range(4)))
        check(f'direct_plane{mu+1}{nu+1}_tensor{k}', dd)
        check(f'mixed_plane{mu+1}{nu+1}_tensor{k}',
              add(mixed, scale(2, mul(var(10), brackets[k]))))

# Actual half-fiber centers r+1/2 with r=-1,...,-R. Check raw
# positions against the finite geometric formula, including R=1.
for length in (1, 2, 7):
    terms = []
    for r in range(-length, 0):
        e = list(ZERO)
        e[0] = 2*r+1
        terms.append({tuple(e): F(1)})
    total = add(*terms)
    tail = list(ZERO)
    tail[0] = -2*length
    check(f'prefix_endpoint_length{length}',
          sub(mul(sub(one, mul(conj(z[0]), conj(z[0]))), total),
              mul(conj(z[0]), sub(one, {tuple(tail): F(1)}))))

# Verify Q_(a,1) at theta_1=0 from the full residual numerator
# lambda*(R-R^T)-d*d^T*R+R^T*d*d^T = 2 lambda^2 Q.
dd = [const(0)] + d[1:]
ee = [const(1)] + eta[1:]
lam = add(*(mul(v, v) for v in dd))
R = [[scale(-1, mul(ee[a], ee[a], dd[a])) if b == 0 else {}
      for b in range(4)] for a in range(4)]
outer = [[mul(dd[a], dd[b]) for b in range(4)] for a in range(4)]
dr = matmul(outer, R)
rt = [list(r) for r in zip(*R)]
rd = matmul(rt, outer)
sum4 = add(*(mul(v, v, v, v) for v in dd))
for a in range(1, 4):
    num = add(mul(lam, sub(R[a][0], R[0][a])), scale(-1, dr[a][0]), rd[a][0])
    expected = scale(F(1, 4), mul(dd[a], sub(mul(dd[a], dd[a], lam), sum4)))
    check(f'zero_axial_residual_entry{a+1}1', sub(num, expected))

failures = [c for c in checks if not c['passed']]
result = {'scope': 'All-frequency finite Laurent identities only; analytic limits and heat forms require the canonical proof audit.',
          'arithmetic': 'fractions.Fraction; exact Laurent monomials; i^2=-1',
          'checks': checks, 'actual_passed': len(checks)-len(failures),
          'required_passed': len(checks), 'failures': failures}
path = Path(__file__).with_name('joint-action-critical-audit-certificate.json')
path.write_text(json.dumps(result, indent=2)+'\n')
print('Exact all-frequency checks:', result['actual_passed'], 'required:', len(checks))
print('Failures:', [c['name'] for c in failures])
print('Certificate:', path)
if failures:
    raise SystemExit(1)
