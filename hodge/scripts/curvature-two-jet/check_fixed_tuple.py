"""Exact necessary two-jet test for the fixed L143 tuple; no realization claim.

All coefficients are rational. Output includes full affine solutions, defining
bases, elimination trace, and checks of every original tensor equation.
"""
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
import json
from pathlib import Path


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def bracket(a, b):
    return [2*(a[1]*b[2]-a[2]*b[1]),
            2*(a[2]*b[0]-a[0]*b[2]),
            2*(a[0]*b[1]-a[1]*b[0])]


I4 = [[int(a == b) for b in range(4)] for a in range(4)]
M1 = [[0, 1, 0, 0], [-1, 0, 0, 0],
      [0, 0, 0, -1], [0, 0, 1, 0]]
M2 = [[0, 0, 1, 0], [0, 0, 0, 1],
      [-1, 0, 0, 0], [0, -1, 0, 0]]
M3 = matmul(M1, M2)
M = [M1, M2, M3]
LI = [[0, -1, 0, 0], [1, 0, 0, 0],
      [0, 0, 0, -1], [0, 0, 1, 0]]
LJ = [[0, 0, -1, 0], [0, 0, 0, 1],
      [1, 0, 0, 0], [0, -1, 0, 0]]
LK = matmul(LI, LJ)
left = []
for l in [LI, LJ, LK]:
    left.append([[l[a % 4][b % 4] if a//4 == b//4 else 0
                  for b in range(8)] for a in range(8)])

# Ten invariant curvature form matrices: P_1..P_3,Q_1..Q_3,A_0..A_3.
B = []
for block in range(2):
    for m in M:
        B.append([[m[a % 4][b % 4] if a//4 == b//4 == block else 0
                   for b in range(8)] for a in range(8)])
for m in [I4]+M:
    B.append([[m[a][b-4] if a < 4 <= b else
               -m[b][a-4] if b < 4 <= a else 0
               for b in range(8)] for a in range(8)])
coeff = [[0, 0, 2], [0, 0, 0], [0, 0, 0],
         [0, 0, 1], [0, 0, 0], [0, 0, 0],
         [1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 0]]
R = [[[sum(B[t][a][b]*coeff[t][c] for t in range(10))
        for c in range(3)] for b in range(8)] for a in range(8)]

# G[h][i][j][c][a] is the c component of R^g(e_i,e_j)e_a.
# h indexes two arbitrary symmetric trace-free ASD curvature operators.
H = [[[1, 0, 0], [0, -1, 0], [0, 0, 0]],
     [[0, 0, 0], [0, 1, 0], [0, 0, -1]]]
for k, l in combinations(range(3), 2):
    H.append([[int((a, b) in [(k, l), (l, k)])
               for b in range(3)] for a in range(3)])
G = []
for block in range(2):
    for h in H:
        G.append([[[[sum(h[k][l]*M[k][i % 4][j % 4]*M[l][c % 4][a % 4]
                         for k, l in product(range(3), repeat=2))
                      if i//4 == j//4 == c//4 == a//4 == block else 0
                      for a in range(8)] for c in range(8)]
                    for j in range(8)] for i in range(8)])

pairs = list(combinations(range(8), 2))
triples = list(combinations(range(8), 3))
dpairs = list(combinations_with_replacement(range(8), 2))
unknown = {(i, j, t): n for n, (i, j, t) in enumerate(
    (i, j, t) for i, j in dpairs for t in range(10))}
NU = len(unknown)
NR = 33  # three su coordinates, each affine in ten base parameters


def comm_rhs(i, j, a, b):
    """The 33 coefficient vector for [nabla_i,nabla_j]R_ab."""
    out = [F(0)]*NR
    comm = bracket(R[i][j], R[a][b])
    for c in range(3):
        out[11*c] = F(comm[c])
        for h in range(10):
            out[11*c+1+h] = F(-sum(
                G[h][i][j][k][a]*R[k][b][c]
                + G[h][i][j][k][b]*R[a][k][c] for k in range(8)))
    return out


W = {(i, j, a, b): comm_rhs(i, j, a, b)
     for i, j in pairs for a, b in pairs}


def signed_w(i, j, a, b):
    if i == j or a == b:
        return [F(0)]*NR
    sign = (-1 if i > j else 1)*(-1 if a > b else 1)
    return [sign*v for v in W[min(i, j), max(i, j), min(a, b), max(a, b)]]


def add_v(row, rhs, i, j, a, b):
    # V_ij=V_ji+W_ij for i>j, leaving upper derivative pairs unknown.
    if i > j:
        for k, value in enumerate(signed_w(i, j, a, b)):
            rhs[k] -= value
    for t in range(10):
        if B[t][a][b]:
            n = unknown[min(i, j), max(i, j), t]
            row[n] = row.get(n, F(0)) + B[t][a][b]
            if not row[n]:
                del row[n]


rows = []
labels = []
for i in range(8):
    for j, a, b in triples:
        row, rhs = {}, [F(0)]*NR
        for d, x, y in [(j, a, b), (a, b, j), (b, j, a)]:
            add_v(row, rhs, i, d, x, y)
        rows.append((row, rhs))
        labels.append([i, j, a, b])

# Sparse rational row reduction. Pivot rows are normalized and only contain
# their own pivot and larger unknown columns. Apply identical operations to
# the 33 affine right sides. All free unknowns are set to zero afterwards.
pivots = {}
trace = []
residuals = []
for source, (original, right) in enumerate(rows):
    row, rhs = dict(original), list(right)
    ops = []
    while row:
        p = min(row)
        if p not in pivots:
            factor = row[p]
            row = {k: F(v)/factor for k, v in row.items()}
            rhs = [v/factor for v in rhs]
            pivots[p] = row, rhs
            trace.append({"source": source, "eliminate": ops,
                          "pivot": p, "divide": str(factor)})
            break
        factor = row[p]
        pr, pb = pivots[p]
        for k, v in pr.items():
            row[k] = row.get(k, F(0))-factor*v
            if not row[k]:
                del row[k]
        rhs = [v-factor*w for v, w in zip(rhs, pb)]
        ops.append([p, str(factor)])
    else:
        trace.append({"source": source, "eliminate": ops, "pivot": None})
        if any(rhs):
            residuals.append({"source": source,
                              "right": [str(v) for v in rhs]})

solution = [[F(0)]*NR for _ in range(NU)]
for p in sorted(pivots, reverse=True):
    row, rhs = pivots[p]
    solution[p] = [rhs[c]-sum(v*solution[k][c]
                             for k, v in row.items() if k != p)
                   for c in range(NR)]


def value(i, j, a, b):
    out = [F(0)]*NR
    for t in range(10):
        scale = B[t][a][b]
        if scale:
            for c, v in enumerate(solution[unknown[min(i, j), max(i, j), t]]):
                out[c] += scale*v
    if i > j:
        out = [v+w for v, w in zip(out, signed_w(i, j, a, b))]
    return out


checks, failures = {}, []


def check(name, ok):
    checks[name] = bool(ok)
    if not ok:
        failures.append(name)


# Validate defining bases and every relevant base-curvature component.
check("basis_skew", all(B[t][a][b] == -B[t][b][a]
                          for t, a, b in product(range(10), range(8), range(8))))
check("basis_quaternionic_type", all(
    matmul(matmul([[l[b][a] for b in range(8)] for a in range(8)], bt), l) == bt
    for bt in B for l in left))
check("base_hyperkahler_symmetries", all(
    g[i][j][c][a] == -g[j][i][c][a]
    and g[i][j][c][a] == -g[i][j][a][c]
    and g[i][j][c][a] == g[a][c][j][i]
    and g[i][j][c][a]+g[j][a][c][i]+g[a][i][c][j] == 0
    for g in G for i, j, c, a in product(range(8), repeat=4)))
check("base_ricci_zero", all(sum(g[i][j][i][a] for i in range(8)) == 0
                             for g in G for j, a in product(range(8), repeat=2)))
check("base_commutes_with_quaternions", all(
    matmul(g[i][j], l) == matmul(l, g[i][j])
    for g in G for i, j in pairs for l in left))
check("elimination_residual_zero", not residuals)
check("all_original_linear_rows", all(
    all(sum(v*solution[k][c] for k, v in row.items()) == rhs[c]
        for c in range(NR)) for row, rhs in rows))
check("full_differentiated_bianchi", all(
    all(x+y+z == 0 for x, y, z in zip(
        value(i, j, a, b), value(i, a, b, j), value(i, b, j, a)))
    for i, j, a, b in product(range(8), repeat=4)))
check("full_ricci_commutation", all(
    all(x-y == z for x, y, z in zip(value(i, j, a, b),
                                    value(j, i, a, b), signed_w(i, j, a, b)))
    for i, j, a, b in product(range(8), repeat=4)))
check("full_V_curvature_skew", all(
    all(x == -y for x, y in zip(value(i, j, a, b), value(i, j, b, a)))
    for i, j, a, b in product(range(8), repeat=4)))
# Type for lower derivative pairs also tests every W coefficient.
check("full_V_quaternionic_type", all(
    all(sum(l[x][a]*l[y][b]*value(i, j, x, y)[c]
            for x, y in product(range(8), repeat=2)
            if l[x][a] and l[y][b]) == value(i, j, a, b)[c]
        for c in range(NR))
    for i, j, a, b in product(range(8), repeat=4) for l in left))
# U=0 solves real type, first Bianchi and Yang--Mills divergence. The
# differentiated divergence follows from type/Bianchi but is checked in full.
check("full_differentiated_yang_mills", all(
    all(sum(value(i, j, j, b)[c] for j in range(8)) == 0 for c in range(NR))
    for i, b in product(range(8), repeat=2)))
# In a normal orthonormal frame nabla* nabla R=-sum_i V_ii. Compare
# the entire mixed output to L143: sum_i V_ii;a,mu = C_a,mu.
contracted = []
for a in range(4):
    for mu in range(4, 8):
        coupling = [-2*sum(bracket(R[a][k], R[k][mu])[c] for k in range(8))
                    for c in range(3)]
        expected = [F(0)]*NR
        for c in range(3):
            expected[11*c] = F(coupling[c])
        actual = [sum(value(i, i, a, mu)[c] for i in range(8))
                  for c in range(NR)]
        contracted.append({"indices": [a, mu],
                           "actual": [str(v) for v in actual],
                           "required": [str(v) for v in expected]})
check("L143_contracted_equation", all(r["actual"] == r["required"]
                                         for r in contracted))
energy = sum(-4*sum(x*x for x in R[a][mu])
             for a in range(4) for mu in range(4, 8))
check("L143_negative_energy", energy == -32)

certificate = {
    "target": "L143 (r,s)=(2,1) necessary real covariant curvature two-jet",
    "convention": "V_ij;ab - V_ji;ab = [R_ij,R_ab] - R(Rg_ij e_a,e_b) - R(e_a,Rg_ij e_b)",
    "parameter_order": ["constant"]+[f"base{b+1}_H{h+1}" for b in range(2) for h in range(5)],
    "rhs_order": "three consecutive su(2) coordinates, each with eleven affine coefficients",
    "curvature_basis": B, "su2_coefficients": coeff,
    "base_operator_basis": H,
    "base_curvature_formula": "Rg_ij[c,a]=sum_kl H_kl M_k[i,j] M_l[c,a], independently on each factor",
    "first_derivative": "U=0 (prospective tensor only)",
    "unknown_order": [[i, j, t] for i, j in dpairs for t in range(10)],
    "unknown_count_per_su_coordinate": NU,
    "bianchi_rows_per_su_coordinate": len(rows),
    "rank": len(pivots), "free_dimension_per_su_coordinate": NU-len(pivots),
    "elimination_trace": trace, "nonzero_residual_conditions": residuals,
    "solution": [[str(v) for v in r] for r in solution],
    "solution_sparse": {f"{i},{j},{t}": {
        f"{c},{h}": str(solution[unknown[i, j, t]][11*c+h])
        for c in range(3) for h in range(11)
        if solution[unknown[i, j, t]][11*c+h]}
        for i, j in dpairs for t in range(10)
        if any(solution[unknown[i, j, t]])},
    "solution_sparse_key": "outer i,j,t: upper derivative pair and invariant basis index; inner c,h: su coordinate and affine parameter (all zero-based); omitted values zero",
    "lower_derivative_pair_rule": "V_ij=V_ji+W_ij for i>j; W is the stated full commutator",
    "mixed_contracted_equation": contracted,
    "actual_energy": energy, "required_universal_sign_lower_bound": 0,
    "checks": checks, "failures": failures,
    "verdict": "uniformly compatible necessary two-jet" if not failures else "FAILED; inspect failures",
    "limitations": "No prescribed actual K3 values, sufficiency, local/global connection, equality kernel or Hodge-class realization is asserted."
}
path = Path(__file__).with_name("fixed_tuple_certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"rank {len(pivots)}/{NU}; free dimension {NU-len(pivots)} per su(2) coordinate")
print(f"symbolic base parameters: 10/10 retained; residual conditions: {len(residuals)}")
print(f"checks {sum(checks.values())}/{len(checks)}; failures: {failures}")
print(f"energy {energy}; universal-sign threshold 0; certificate: {path}")
print(certificate["verdict"])
raise SystemExit(bool(failures))
