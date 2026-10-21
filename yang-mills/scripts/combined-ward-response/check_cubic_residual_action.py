"""Exact (2,3,3) contraction checks. No actual-box asymptotic test."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations, product
from pathlib import Path
import json

N = 4
DIM = 3 * N


def parity(t):
    return (-1) ** sum(t[i] > t[j] for i in range(len(t)) for j in range(i + 1, len(t)))


EPS = [(t, parity(t)) for t in permutations(range(3))]
OMEGA = [(t, parity(t)) for t in permutations(range(4), 3)]


def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            k = tuple(a + b for a, b in zip(e, f))
            out[k] = out.get(k, F(0)) + c * d
    return {e: c for e, c in out.items() if c}


def linear(row, color):
    return {tuple(int(k == color * N + j) for k in range(DIM)): F(c)
            for j, c in enumerate(row) if c}


def cubic(rows, coeffs):
    result = {}
    for (r, s, t), coefficient in coeffs.items():
        for (c, d, e), sign in EPS:
            term = mul(mul(linear(rows[r], c), linear(rows[s], d)), linear(rows[t], e))
            result = add(result, {k: coefficient * sign * v for k, v in term.items()})
    return result


def quadratic(b):
    out = {}
    for color, i, j in product(range(3), range(N), range(N)):
        e = tuple(int(k == color * N + i) + int(k == color * N + j) for k in range(DIM))
        out[e] = out.get(e, F(0)) + F(b[i][j])
    return {e: c for e, c in out.items() if c}


def expectation(cov):
    @lru_cache(None)
    def moment(e):
        if not any(e):
            return F(1)
        if any(sum(e[c * N:(c + 1) * N]) % 2 for c in range(3)):
            return F(0)
        i = next(k for k, count in enumerate(e) if count)
        tail = list(e)
        tail[i] -= 1
        result = F(0)
        for j in range(i // N * N, (i // N + 1) * N):
            if tail[j] and cov[i % N][j % N]:
                rest = tail.copy()
                rest[j] -= 1
                result += tail[j] * cov[i % N][j % N] * moment(tuple(rest))
        return result

    return lambda p: sum((c * moment(e) for e, c in p.items()), F(0))


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    return [[sum((F(x) * F(y) for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def block(p, a, q):
    return mm(mm(p, a), transpose(q))


def alternating(coeffs):
    return [(tuple(key[j] for j in perm), F(c) * parity(perm))
            for key, c in coeffs.items() for perm in permutations(range(3))]


def contracted(p, q, h, cov, b):
    c = block(p, cov, q)
    u = block(p, mm(mm(cov, b), cov), q)
    return 3 * sum((hs * ws * u[r][v] * c[s][w] * c[t][z]
                    for (r, s, t), hs in alternating(h)
                    for (v, w, z), ws in OMEGA), F(0))


def pairings(xs):
    if not xs:
        yield ()
        return
    x, *tail = xs
    for j, y in enumerate(tail):
        for rest in pairings(tail[:j] + tail[j + 1:]):
            yield ((x, y),) + rest


checks = []


def record(kind, passed, **evidence):
    checks.append(dict(kind=kind, passed=bool(passed), **evidence))


groups = (0, 0, 1, 1, 1, 2, 2, 2)
counts = dict(total=0, connected=0, cubic_self=0, surviving=0)
for pairs in pairings(list(range(8))):
    counts['total'] += 1
    reached = {0}
    for _ in range(3):
        reached |= {groups[j] for i, j in pairs if groups[i] in reached}
        reached |= {groups[i] for i, j in pairs if groups[j] in reached}
    if len(reached) != 3:
        continue
    counts['connected'] += 1
    if any(groups[i] == groups[j] and groups[i] > 0 for i, j in pairs):
        counts['cubic_self'] += 1
    else:
        counts['surviving'] += 1
record('complete_pairing_count', counts == dict(total=105, connected=90, cubic_self=54, surviving=36),
       actual=counts, required=dict(total=105, connected=90, cubic_self=54, surviving=36))

identity = [[int(i == j) for j in range(N)] for i in range(N)]
lower = [[1, 0, 0, 0], [F(1, 2), 1, 0, 0], [0, F(-1, 3), 2, 0], [F(1, 4), 0, F(1, 2), 1]]
covariances = [identity, mm(lower, transpose(lower))]
bs = [identity, [[1, F(1, 3), 0, -1], [F(1, 3), -2, F(1, 2), 0],
                 [0, F(1, 2), 0, 1], [-1, 0, 1, -1]]]
zero_row = [0] * N
maps = [
    (identity, identity),
    (identity, [identity[2], [-x for x in identity[0]], identity[3], zero_row]),
    ([identity[0], identity[1], identity[0], identity[3]],
     [identity[1], identity[2], zero_row, identity[3]]),
]
h = {(0, 1, 2): F(2, 3), (0, 1, 3): F(-5, 4), (0, 2, 3): F(7, 5), (1, 2, 3): F(-1, 2)}
action_h = {t: F(-1, 2) for t in combinations(range(4), 3)}
for ci, cov in enumerate(covariances):
    expected = expectation(cov)
    for mi, (p, q) in enumerate(maps):
        r, s = cubic(p, h), cubic(q, action_h)
        rs = mul(r, s)
        for bi, b in enumerate(bs):
            f = quadratic(b)
            direct = -(expected(mul(f, rs)) - expected(f) * expected(rs))
            formula = contracted(p, q, h, cov, b)
            record('signed_cumulant', direct == formula, covariance=ci, maps=mi, probe=bi,
                   direct=str(direct), formula=str(formula), exact_error=str(direct - formula),
                   required_error='0')

# Three independent color vectors: E[det^2]=6 and radial covariance = 6 E[det^2].
p = identity[:3]
q = identity[:3] + [zero_row]
toy_h = {(0, 1, 2): F(1)}
expected = expectation(identity)
r, s, f = cubic(p, toy_h), cubic(q, action_h), quadratic(identity)
toy = -(expected(mul(f, mul(r, s))) - expected(f) * expected(mul(r, s)))
record('nonzero_algebraic_sign_control', toy == 18 == contracted(p, q, toy_h, identity, identity),
       actual=str(toy), required='18', scope='synthetic Gaussian, not either actual probe')

failures = [check for check in checks if not check['passed']]
certificate = dict(scope='Exact finite contraction algebra only; no mesh bound or actual-probe value',
                   checks=checks, failures=failures, passed=not failures)
path = Path(__file__).with_name('cubic-residual-action-certificate.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f"checks={len(checks)} failures={len(failures)}; exact errors required=0; toy actual={toy} required=18")
print(f"pairings actual={counts}; required total=105 connected=90 cubic_self=54 surviving=36")
print(f"certificate={path}")
if failures:
    raise SystemExit(1)
