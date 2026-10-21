"""Exact finite SU(2) two-cubic contraction checks; no box asymptotics."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from pathlib import Path
import json

N = 4
DIM = 3 * N
ZERO = (0,) * DIM


def add(*polys):
    out = {}
    for poly in polys:
        for e, c in poly.items():
            out[e] = out.get(e, F(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(c, poly):
    return {e: c * v for e, v in poly.items() if c * v}


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            h = tuple(a + b for a, b in zip(e, f))
            out[h] = out.get(h, F(0)) + c * d
    return {e: c for e, c in out.items() if c}


def parity(indices):
    return (-1) ** sum(indices[i] > indices[j]
                       for i in range(len(indices)) for j in range(i + 1, len(indices)))


OMEGA = [(indices, parity(indices)) for indices in permutations(range(4), 3)]
EPSILON = [(indices, parity(indices)) for indices in permutations(range(3))]


def linear(row, color):
    return {tuple(int(k == color * N + j) for k in range(DIM)): F(c)
            for j, c in enumerate(row) if c}


def cubic(edges):
    ys = [[linear(row, color) for color in range(3)] for row in edges]
    # Ordered product trace gives -1/2 on every increasing edge triple.
    terms = []
    for r in range(4):
        for s in range(r + 1, 4):
            for t in range(s + 1, 4):
                for (c, d, e), sign in EPSILON:
                    terms.append(scale(F(-sign, 2), mul(mul(ys[r][c], ys[s][d]), ys[t][e])))
    return add(*terms)


def quadratic(matrix):
    terms = []
    for color in range(3):
        for i, j in product(range(N), repeat=2):
            e = tuple(int(k == color * N + i) + int(k == color * N + j)
                      for k in range(DIM))
            if matrix[i][j]:
                terms.append({e: F(matrix[i][j])})
    return add(*terms)


def expectation_function(cov):
    @lru_cache(None)
    def moment(e):
        if not any(e):
            return F(1)
        # Independent colors permit early exact zero tests.
        if any(sum(e[c * N:(c + 1) * N]) % 2 for c in range(3)):
            return F(0)
        i = next(k for k, count in enumerate(e) if count)
        tail = list(e)
        tail[i] -= 1
        total = F(0)
        for j in range(i // N * N, (i // N + 1) * N):
            count = tail[j]
            if count and cov[i % N][j % N]:
                rest = tail.copy()
                rest[j] -= 1
                total += count * cov[i % N][j % N] * moment(tuple(rest))
        return total

    def expected(poly):
        return sum((c * moment(e) for e, c in poly.items()), F(0))
    return expected


def mm(a, b):
    return [[sum((F(x) * F(y) for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def block(jp, matrix, jq):
    return mm(mm(jp, matrix), transpose(jq))


def contraction(left, middle, right):
    return sum((F(sp * sq) * left[r][u] * middle[s][v] * right[t][w]
                for (r, s, t), sp in OMEGA for (u, v, w), sq in OMEGA), F(0))


def pairings(indices):
    if not indices:
        yield ()
        return
    a, *rest = indices
    for j, b in enumerate(rest):
        for tail in pairings(rest[:j] + rest[j + 1:]):
            yield ((a, b),) + tail


groups = (0, 0, 1, 1, 2, 2, 2, 3, 3, 3)
counts = {"same_F_p": 0, "same_F_q": 0, "split": 0,
          "path_F_p": 0, "path_F_q": 0}
all_pairings = connected = self_cubic = 0
for pairs in pairings(list(range(10))):
    all_pairings += 1
    reached = {0}
    while True:
        expanded = reached | {groups[j] for i, j in pairs if groups[i] in reached}
        expanded |= {groups[i] for i, j in pairs if groups[j] in reached}
        if reached == expanded:
            break
        reached = expanded
    if len(reached) != 4:
        continue
    connected += 1
    if any(groups[i] == groups[j] and groups[i] >= 2 for i, j in pairs):
        self_cubic += 1
        continue
    fr = sum({groups[i], groups[j]} == {0, 1} for i, j in pairs)
    fp = sum({groups[i], groups[j]} == {0, 2} for i, j in pairs)
    if fr:
        key = "path_F_p" if fp else "path_F_q"
    else:
        key = "same_F_p" if fp == 2 else "same_F_q" if fp == 0 else "split"
    counts[key] += 1

checks = []
failures = []


def record(kind, passed, **fields):
    checks.append({"type": kind, "pass": passed, **fields})
    if not passed:
        failures.append({"type": kind, **fields})


record("pairing_counts", all_pairings == 945 and counts == {
    "same_F_p": 36, "same_F_q": 36, "split": 144,
    "path_F_p": 72, "path_F_q": 72}, counts=counts,
    all_pairings=all_pairings, connected_pairings=connected,
    connected_with_cubic_self_pair=self_cubic)

# Independent formal scalar/vector SU(2) product at rational numeric edges.
def cross(x, y):
    return [x[(i + 1) % 3] * y[(i + 2) % 3]
            - x[(i + 2) % 3] * y[(i + 1) % 3] for i in range(3)]


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def cubic_from_product(edges):
    scalar = [F(1), F(0), F(0), F(0)]
    vector = [[F(0)] * 3 for _ in range(4)]
    for y in edges:
        norm = dot(y, y)
        sy = [F(1), F(0), -norm / 8, F(0)]
        vy = [[F(0)] * 3, list(map(F, y)), [F(0)] * 3,
              [-norm * F(z) / 24 for z in y]]
        new_s = [F(0)] * 4
        new_v = [[F(0)] * 3 for _ in range(4)]
        for d in range(4):
            for k in range(d + 1):
                l = d - k
                new_s[d] += scalar[k] * sy[l] - dot(vector[k], vy[l]) / 4
                bracket = [-z for z in cross(vector[k], vy[l])]
                for c in range(3):
                    new_v[d][c] += scalar[k] * vy[l][c] + sy[l] * vector[k][c] + bracket[c] / 2
        scalar, vector = new_s, new_v
    return -4 * scalar[3]


numeric_edges = [
    [(1, 2, 0), (0, 1, 3), (-1, 1, 2), (2, 0, -1)],
    [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)],
    [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)],
]
for k, edges in enumerate(numeric_edges):
    direct = cubic_from_product(edges)
    triple = -sum((dot(edges[r], cross(edges[s], edges[t]))
                   for r in range(4) for s in range(r + 1, 4)
                   for t in range(s + 1, 4)), F(0)) / 2
    record("ordered_product_cubic", direct == triple, case=k,
           product=str(direct), triple_formula=str(triple))

I = [[int(i == j) for j in range(N)] for i in range(N)]
edge_pairs = [
    (I, [I[1], I[2], [0] * N, I[3]]),
    ([I[0], [0] * N, I[1], I[2]], [I[1], I[2], I[3], I[0]]),
    (I, I),
]
covariances = [
    [[2, 1, 0, 0], [1, 3, 1, 0], [0, 1, 3, 1], [0, 0, 1, 2]],
    [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]],
]
Bs = [
    [[2, -1, 1, 0], [-1, 0, 2, 1], [1, 2, -2, 0], [0, 1, 0, 1]],
    [[0, 1, 0, 2], [1, -2, 1, 0], [0, 1, 3, -1], [2, 0, -1, 0]],
]
A = [[0, 1, -1, 0], [1, 3, 0, 1], [-1, 0, 1, 2], [0, 1, 2, -1]]
for edge_case, js in enumerate(edge_pairs):
    qs = [cubic(j) for j in js]
    for cov_case, cov in enumerate(covariances):
        expected = expectation_function(cov)
        r = quadratic(A)
        er = expected(r)
        for probe_case, b in enumerate(Bs):
            f = quadratic(b)
            ef = expected(f)
            fr = mul(f, r)
            efr = expected(fr)
            u = mm(mm(cov, b), cov)
            v = mm(mm(cov, A), cov)
            w = mm(mm(u, A), cov)
            wr = mm(mm(v, b), cov)
            total_moment = total_formula = F(0)
            cells = []
            for p, q in product(range(2), repeat=2):
                cd = mul(qs[p], qs[q])
                ecd = expected(cd)
                kappa = (expected(mul(fr, cd)) - ef * expected(mul(r, cd))
                         - er * expected(mul(f, cd)) - efr * ecd + 2 * ef * er * ecd)
                cpq = block(js[p], cov, js[q])
                upq = block(js[p], u, js[q])
                vpq = block(js[p], v, js[q])
                wpq = block(js[p], w, js[q])
                wrpq = block(js[p], wr, js[q])
                mixed = 3 * contraction(upq, vpq, cpq)
                path = F(3, 2) * (contraction(wpq, cpq, cpq)
                                  + contraction(wrpq, cpq, cpq))
                cell = mixed + path
                cells.append({"p": p, "q": q, "half_cumulant": str(kappa / 2),
                              "split_class": str(mixed), "path_class": str(path),
                              "pass": cell == kappa / 2})
                total_moment += kappa / 2
                total_formula += mixed + 3 * contraction(wpq, cpq, cpq)
            record("exact_color_diagonal_cumulant", all(x["pass"] for x in cells)
                   and total_moment == total_formula,
                   edge_case=edge_case, covariance_case=cov_case, probe_case=probe_case,
                   covariance=cov, probe_matrix=b, residual_matrix=A, edge_maps=js,
                   cells=cells, moment_total=str(total_moment), formula_total=str(total_formula))

out = Path(__file__).with_name("two-cubic-action-certificate.json")
out.write_text(json.dumps({
    "scope": "Exact finite color-diagonal Gaussian algebra; not the original-box numerical response",
    "checks": checks, "failures": failures,
    "bounds": {"actual": "fixed-mesh identity only; no cutoff bound",
               "required": "complete response power/log control and interacting reflected error <= c_box/2"},
}, indent=2) + "\n")
print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact checks; failures={len(failures)}")
print(f"Pairing classes without cubic self-pairs: {counts}")
print("Actual bound: finite identity only. Required: full power/log control and reflected error <= c_box/2.")
print(f"Certificate: {out.relative_to(Path.cwd())}")
assert not failures, failures
