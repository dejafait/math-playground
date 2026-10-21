"""Exact raw Laurent algebra and full spectral-tail arithmetic for L140.

No sampling or retained physical/torus quadrature is used. The proof of
angle integration, signs and heat estimates is in the canonical lemma.
"""
from fractions import Fraction as F
import json
from pathlib import Path


def add(*ps):
    out = {}
    for p in ps:
        for power, value in p.items():
            out[power] = out.get(power, F(0)) + value
    return {p: v for p, v in out.items() if v}


def scale(p, v):
    return {power: v * value for power, value in p.items() if v * value}


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


def reflect(p, a):
    out = {}
    for key, v in p.items():
        target = tuple(-n if j == a else n for j, n in enumerate(key))
        out[target] = v
    return out


def conj(p):
    return {tuple(-n for n in key): v for key, v in p.items()}


def even(p):
    for a in range(3):
        p = scale(add(p, reflect(p, a)), F(1, 2))
    return p


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
p = [scale(add(e[a], scale(ei[a], -1)), F(1, 2)) for a in range(3)]  # i sin
X = [add(scale(one, 2), scale(e[a], -1), scale(ei[a], -1)) for a in range(3)]
eta2 = [scale(add(scale(one, 2), e[a], ei[a]), F(1, 4)) for a in range(3)]
wc = [scale(mul(add(one, ei[a]), p[a]), F(1, 2)) for a in range(3)]
planes = [(0, 1), (0, 2), (1, 2)]
cs, bs, qs = [], [], []
for a, b in planes:
    cs.append([tau[b] if j == a else scale(tau[a], -1) if j == b else {}
               for j in range(3)])
    bs.append([one if j == a else e[a] if j == b else {} for j in range(3)])
    qs.append([scale(e[b], -1) if j == a else e[a] if j == b else {}
               for j in range(3)])

diag = []
for b in range(3):  # physical v component
    f = []
    for j, (a0, b0) in enumerate(planes):
        z = [add(scale(qs[j][a], int(b in (a0, b0))),
                 scale(bs[j][a], int(b == a0) - int(b == b0))) for a in range(3)]
        actual = add(*(mul(z[a], tau[a]) for a in range(3)))
        required = mul(add(one, e[a0]), tau[b0]) if b == a0 else \
            scale(mul(add(one, e[b0]), tau[a0]), -1) if b == b0 else {}
        check(f'raw-z-tau-plane-{a0+2}{b0+2}-v{b+2}', actual, required)
        f.append(actual)
    contraction = add(*(mul(wc[a], conj(cs[j][a]), f[j])
                        for a in range(3) for j in range(3)))
    sum_other = add(*(mul(X[a], add(X[a], scale(X[b], -1)))
                      for a in range(3) if a != b))
    for r in range(3):  # physical h component
        raw = mul(scale(p[r], 2), contraction)
        required_raw = mul(p[r], p[b], sum_other)
        check(f'complete-raw-h{r+2}-v{b+2}', raw, required_raw)
        required_even = scale(mul(X[b], eta2[b], sum_other), -1) if r == b else {}
        check(f'complete-parity-h{r+2}-v{b+2}', even(raw), required_even)
        if r == b:
            diag.append(required_even)

pair_sum = add(*(mul(X[a], X[b], add(X[a], scale(X[b], -1)),
                    add(X[a], scale(X[b], -1))) for a, b in planes))
check('diagonal-sum-pair-square', add(*diag), scale(pair_sum, F(-1, 4)))
# Exact single-angle moments: mean X=2, mean X^2=6.
check('single-angle-X-mean', { (0, 0, 0): X[0].get((0, 0, 0), 0)}, scale(one, 2))
xx = mul(X[0], X[0])
check('single-angle-X2-mean', {(0, 0, 0): xx.get((0, 0, 0), 0)}, scale(one, 6))
delta2 = mul(add(X[0], scale(X[1], -1)), add(X[0], scale(X[1], -1)))
check('independent-angle-difference-square-mean',
      {(0, 0, 0): delta2.get((0, 0, 0), 0)}, scale(one, 4))

C_G = F(1296 * 7 * 165 * 3, 16)
K = 144
S_half = 4 * 16**4
tail_half_prefactor = F(16 * 16**3 * 1024, 9 * K)
H_half_prefactor = 2 * S_half * tail_half_prefactor
B_bound = 16 * C_G * 1640736 * H_half_prefactor / 20**30
G_bound = B_bound / 4
required = F(1, 10**12)
certificate = dict(
    method='Exact rational Laurent coefficients, all separate reflections, and rational tail arithmetic',
    qualification='No retained physical or torus evaluation; analytic inclusion and sign proof are in L140.',
    algebra=records,
    tail=dict(cutoff=K, C_G=rational(C_G), full_probe_norm=1640736,
              exponent=rational(F(9*K*K, 2048)), lower_exponent=90,
              H_half_prefactor=rational(H_half_prefactor),
              B_actual_upper_bound=rational(B_bound), G_actual_upper_bound=rational(G_bound),
              required=rational(required), passed=B_bound < required),
)
certificate['failures'] = [r['identity'] for r in records if not r['passed']]
if not certificate['tail']['passed']:
    certificate['failures'].append('full-spectrum-tail')
certificate['passed'] = not certificate['failures']
path = Path(__file__).with_name('g-physical-reduction-certificate.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f"Exact algebra/parity/moment checks: {sum(r['passed'] for r in records)}/{len(records)}")
print(f"K={K} complete B omission bound <{float(B_bound):.9g}; G <{float(G_bound):.9g}; required <{float(required):.9g}")
print(f"Failures: {certificate['failures']}")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(0 if certificate['passed'] else 1)
