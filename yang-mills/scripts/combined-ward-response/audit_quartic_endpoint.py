"""Independent exact color/Wick and pinned-incidence checks for C212i.

Synthetic algebra only; analytic mesh bounds are proved in the lemma.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def add(*polys):
    out = {}
    for p in polys:
        for word, value in p.items():
            out[word] = out.get(word, F(0)) + value
    return {w: v for w, v in out.items() if v}


def scale(p, c):
    return {w: c * v for w, v in p.items() if c * v}


def mul(p, q):
    out = {}
    for u, a in p.items():
        for v, b in q.items():
            w = tuple(sorted(u + v))
            out[w] = out.get(w, F(0)) + a * b
    return {w: v for w, v in out.items() if v}


def vsum(*vectors):
    return [add(*(v[c] for v in vectors)) for c in range(3)]


def vscale(v, c):
    return [scale(p, c) for p in v]


def bracket(v, w):
    # [v,w] = -v cross w, implemented in color coordinates.
    return [add(mul(v[(c+2) % 3], w[(c+1) % 3]),
                scale(mul(v[(c+1) % 3], w[(c+2) % 3]), -1))
            for c in range(3)]


def dot(v, w):
    return add(*(mul(v[c], w[c]) for c in range(3)))


external, direct, tail, head = [
    [{((r, c),): F(1)} for c in range(3)] for r in range(4)]
p, q = vscale(tail, -1), head
u = vsum(direct, tail, vscale(head, -1))
j = vsum(direct, vscale(head, -1))
weights = [F(1, 12), F(1, 12), F(-1, 4), F(1, 12), F(1, 12)]
triples = [(p, p, u), (u, u, p), (q, p, u), (j, j, q), (q, q, j)]
cubic = vsum(*(vscale(bracket(x, bracket(y, z)), omega)
               for (x, y, z), omega in zip(triples, weights)))
h = vscale(vsum(tail, head), F(1, 2))
d = vsum(head, vscale(tail, -1))
pure = vscale(bracket(h, bracket(h, d)), F(-1, 3))
full_poly, pure_poly = scale(dot(external, cubic), 2), scale(dot(external, pure), 2)


def bilinear(x, matrix, y):
    return sum(x[a] * matrix[a][b] * y[b] for a in range(4) for b in range(4))


def wick_derivative(poly, covariance, tilt, internal_only=False):
    def entry(matrix, x, y):
        return matrix[x[0]][y[0]] if x[1] == y[1] else F(0)
    total = F(0)
    for word, coefficient in poly.items():
        assert len(word) == 4
        for pairing in [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]:
            for tilted in range(2):
                ab, cd = pairing[tilted], pairing[1-tilted]
                if internal_only and any(word[k][0] == 0 for k in ab):
                    continue
                total += coefficient * entry(tilt, word[ab[0]], word[ab[1]]) * entry(
                    covariance, word[cd[0]], word[cd[1]])
    return total


row_p, row_q = [0, 0, -1, 0], [0, 0, 0, 1]
row_u, row_j = [0, 1, 1, -1], [0, 1, 0, -1]
row_h, row_d, row_ext = [0, 0, F(1, 2), F(1, 2)], [0, 0, -1, 1], [1, 0, 0, 0]
row_triples = [(row_p, row_p, row_u), (row_u, row_u, row_p),
               (row_q, row_p, row_u), (row_j, row_j, row_q), (row_q, row_q, row_j)]


def fixture(name, rows):
    # Covariance=L L^T; tilt=L H L^T with H symmetric and indefinite.
    size = len(rows[0])
    H = [[F((-1)**a * (a+1) if a == b else (a+b) % 3-1)
          for b in range(size)] for a in range(size)]
    S = [[sum(F(x[k])*y[k] for k in range(size)) for y in rows] for x in rows]
    M = [[sum(F(x[k])*H[k][l]*y[l] for k in range(size) for l in range(size))
          for y in rows] for x in rows]
    C = lambda x, y: bilinear(x, S, y)
    K = lambda x, y: bilinear(x, M, y)
    E = lambda x: C(x, row_ext)
    T = lambda x: K(x, row_ext)
    contracted = 12 * sum(w * (T(y)*C(x, z)+E(y)*K(x, z)
                              -T(z)*C(x, y)-E(z)*K(x, y))
                          for (x, y, z), w in zip(row_triples, weights))
    direct_value = wick_derivative(full_poly, S, M)
    pure_internal = wick_derivative(pure_poly, S, M, True)
    diagonal = -4 * (E(row_h)*(M[3][3]-M[2][2])/2
                      -E(row_d)*(M[2][2]+2*M[2][3]+M[3][3])/4)
    return {"name": name, "full_wick": str(direct_value),
            "full_contraction": str(contracted), "pure_internal_wick": str(pure_internal),
            "diagonal_formula": str(diagonal), "checks": {
                "full_factor_and_sign": direct_value == contracted,
                "pure_internal_diagonal": pure_internal == diagonal,
                "half_factor_detected": direct_value != 0 and direct_value != contracted/2}}


base = [[2, 1, 0, 1], [1, -2, 1, 0], [0, 1, 3, 1], [1, 0, -1, 2]]
fixtures = [fixture("correlated_full_rank", base),
            fixture("singular_correlated", [[2, 1], [1, -2], [3, 1], [-1, 2]]),
            fixture("pinned_tail", [base[0], base[1], [0]*4, base[3]]),
            fixture("pinned_head", [base[0], base[1], base[2], [0]*4])]


def incidence_fixture(N):
    vertices = list(product(range(1, N), repeat=4))
    interior = set(vertices)
    k = {v: F((-1)**sum(v) * (1+sum((j+1)*x*x for j, x in enumerate(v)))) for v in vertices}
    div = dict.fromkeys(vertices, F(0))
    edge_sum, boundary_sum = F(0), F(0)
    edge_count = boundary_count = 0
    for mu in range(4):
        domains = [range(N) if j == mu else range(1, N) for j in range(4)]
        for v in product(*domains):
            w = tuple(v[j]+(j == mu) for j in range(4))
            coeff = F((-1)**(sum(v)+mu) * (1+sum((j+2)*x for j, x in enumerate(v))), mu+2)
            term = coeff * (k.get(w, 0)-k.get(v, 0))
            edge_sum += term
            edge_count += 1
            if v in interior:
                div[v] -= coeff
            if w in interior:
                div[w] += coeff
            if v not in interior or w not in interior:
                boundary_count += 1
                boundary_sum += term
    vertex_sum = sum(k[v]*div[v] for v in vertices)
    collar = sum(any(x == 1 or x == N-1 for x in v) for v in vertices)
    return {"N": N, "edges": edge_count, "normal_end_edges": boundary_count,
            "collar_vertices": collar, "edge_sum": str(edge_sum), "vertex_sum": str(vertex_sum),
            "normal_end_contribution": str(boundary_sum), "checks": {
                "pinned_transpose": edge_sum == vertex_sum,
                "normal_rows_required": boundary_sum != 0,
                "full_edge_count": edge_count == 4*N*(N-1)**3,
                "full_boundary_count": boundary_count == 8*(N-1)**3,
                "collar_count": collar == (N-1)**4-max(N-3, 0)**4}}


incidence = [incidence_fixture(N) for N in (4, 6)]
records = fixtures + incidence
failures = [f"{r.get('name', r.get('N'))}: {key}" for r in records
            for key, passed in r["checks"].items() if not passed]
certificate = {"scope": "Exact synthetic algebra; no actual-probe values or analytic bounds certified.",
               "color_wick_fixtures": fixtures, "pinned_incidence_fixtures": incidence,
               "checks_passed": sum(sum(r["checks"].values()) for r in records),
               "checks_required": sum(len(r["checks"]) for r in records), "failures": failures}
path = Path(__file__).with_name("quartic-endpoint-critical-audit-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact audit: {certificate['checks_passed']}/{certificate['checks_required']} checks.")
print(f"Failures: {failures}; certificate: {path}")
print("Analytic threshold: endpoint O(N^(5/2)); required o(N^3). This script tests algebra only.")
if failures:
    raise SystemExit(1)
