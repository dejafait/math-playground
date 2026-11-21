"""Exact prescribed d=6 Newton-sum/product-kernel diagnostic. Stdlib only.

Run from the notebook: python3 scripts/central-hermite/product_kernel_496.py
Certificate: scripts/central-hermite/product-kernel-496.json.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json

ZERO = (0,) * 7


def add(*polys):
    out = {}
    for poly in polys:
        for e, c in poly.items():
            out[e] = out.get(e, Q(0)) + c
    return {e: c for e, c in out.items() if c}


def scale(poly, scalar):
    return {e: c * scalar for e, c in poly.items() if c * scalar}


def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            g = tuple(a + b for a, b in zip(e, f))
            out[g] = out.get(g, Q(0)) + c * d
    return {e: c for e, c in out.items() if c}


def shifted(poly, n):
    return {e[:6] + (e[6] + n,): c for e, c in poly.items()}


def encode(poly):
    return [{"exponents_m0_to_m6": list(e), "coefficient": str(c)}
            for e, c in sorted(poly.items())]


def dot(v, matrix, w):
    return sum(v[i] * matrix[i][j] * w[j]
               for i in range(6) for j in range(6))


# c[k] is the coefficient of x^(6-k) in the monic P_6.
c = [{}]
constants = []
for k in range(1, 7):
    a = ((-1)**k * comb(6, k) * Q(factorial(6-k), factorial(12-2*k))
         / Q(factorial(6), factorial(12)))
    e = [0] * 7
    e[6-k] += 1
    e[6] -= 1
    c.append({tuple(e): a})
    constants.append(str(a))

# Formal Newton recurrence, collected as Laurent polynomials.
s = [{ZERO: Q(6)}]
for k in range(1, 11):
    if k <= 6:
        total = add(*(mul(c[j], s[k-j]) for j in range(1, k)))
        total = add(total, scale(c[k], k))
    else:
        total = add(*(mul(c[j], s[k-j]) for j in range(1, 7)))
    s.append(scale(total, -1))

N = max(-e[6] for poly in s for e in poly)
assert N == 10
b = [shifted(poly, N) for poly in s]
assert all(all(a >= 0 for a in e) for poly in b for e in poly)
assert all(sum(e) == N for poly in b for e in poly)
assert all(sum(a * e[a] for a in range(7)) == 6*N-k
           for k, poly in enumerate(b) for e in poly)
minimality_exponent = (0, 0, 0, 0, 0, 10, -10)
assert s[10][minimality_exponent] == 132**10

# Polarization is fully specified by b's monomials. The one-outlier
# specialization of Sym(prod u_l^(2a_l)) is sum_a e_a*t^(2a)/N.
outlier = []
for poly in b:
    outlier.append([sum(coef * e[a] / N for e, coef in poly.items())
                    for a in range(7)])
matrices = [[[outlier[i+j][a] for j in range(6)] for i in range(6)]
            for a in range(7)]

# Exact unpivoted LDL on the leading matrix. At the first negative
# pivot construct a rational vector by solving L^T v=e_k on its block.
A = matrices[6]
L = [[Q(i == j) for j in range(6)] for i in range(6)]
D = []
v = None
for k in range(6):
    pivot = A[k][k] - sum(L[k][j]**2 * D[j] for j in range(k))
    D.append(pivot)
    if pivot < 0:
        v = [Q(0)] * 6
        v[k] = Q(1)
        for i in range(k-1, -1, -1):
            v[i] = -sum(L[j][i] * v[j] for j in range(i+1, k+1))
        assert dot(v, A, v) == pivot
        break
    if pivot == 0:
        break
    for i in range(k+1, 6):
        L[i][k] = (A[i][k] - sum(L[i][j]*L[k][j]*D[j]
                                 for j in range(k))) / pivot

certificate = {
    "target": "Fixed degree-six central Jensen Hermite product kernel; one-outlier family",
    "monic_constants_c1_to_c6": constants,
    "newton_sums_s0_to_s10": [encode(poly) for poly in s],
    "least_denominator_power": N,
    "minimality_witness": {"exponents": list(minimality_exponent),
                           "coefficient": str(s[10][minimality_exponent])},
    "cleared_polynomials_b0_to_b10": [encode(poly) for poly in b],
    "homogeneous_total_degree": N,
    "weighted_degree_bk": "60-k",
    "one_outlier_coefficients_t0_t2_to_t12": [[str(x) for x in row] for row in outlier],
    "one_outlier_leading_matrix": [[str(x) for x in row] for row in A],
    "leading_LDL_pivots_until_stop": [str(x) for x in D],
}
if v is not None:
    q = [dot(v, M, v) for M in matrices]
    assert q[6] < 0
    C = sum(abs(x) for x in q[:6])
    # For t>=1, q(t)<=q_6*t^12+C*t^10. Choose integer t with
    # t^2 > C/(-q_6); isqrt on a rational ceiling is exact.
    from math import isqrt
    ratio = C / (-q[6])
    ceiling = (ratio.numerator + ratio.denominator - 1)//ratio.denominator
    threshold = max(1, isqrt(ceiling) + 1)
    exact_value = sum(q[a]*threshold**(2*a) for a in range(7))
    assert Q(threshold**2) > ratio
    assert exact_value < 0
    # A small, fixed integer witness makes the load-bearing arithmetic
    # independently readable without the LDL computation.
    w = [Q(-152988), Q(4638), Q(113), Q(0), Q(0), Q(0)]
    primitive = [0, 0, -893830, 23068724, -121938843,
                 206347856, -28504137]
    integer_q = [dot(w, M, w) for M in matrices]
    assert integer_q == [4752 * x for x in primitive]
    integer_value = sum(integer_q[a] * 4**(2*a) for a in range(7))
    assert integer_value == -1281831933403422720
    assert 16 * 28504137 > 352249253
    certificate["negative_witness"] = {
        "vector": [str(x) for x in v],
        "quadratic_coefficients_t0_t2_to_t12": [str(x) for x in q],
        "leading_coefficient": str(q[6]),
        "lower_absolute_sum_C": str(C),
        "required_t_squared_strictly_greater_than": str(ratio),
        "integer_tail_threshold": threshold,
        "actual_threshold_squared": threshold**2,
        "exact_quadratic_value_at_threshold": str(exact_value),
        "integer_vector": [str(x) for x in w],
        "integer_quadratic_common_factor": 4752,
        "integer_quadratic_primitive_coefficients_t0_t2_to_t12": primitive,
        "integer_quadratic_exact_value_at_t4": str(integer_value),
    }
    certificate["result"] = "NEGATIVE_POINTWISE_PSD"
else:
    certificate["result"] = "INCONCLUSIVE_LEADING_MATRIX_TEST"

path = Path(__file__).with_name("product-kernel-496.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print("N:", N, "; required: least common denominator power; homogeneity: PASS")
print("Newton term counts:", [len(poly) for poly in s])
print("Leading LDL pivot signs:", ["negative" if x < 0 else "positive" if x > 0 else "zero" for x in D])
print("Result:", certificate["result"])
if v is not None:
    print("Tail threshold t:", threshold, "; actual t^2:", threshold**2,
          "; required >", ratio)
    print("Exact negative witness verified; failures: none")
print("Full certificate:", path)
