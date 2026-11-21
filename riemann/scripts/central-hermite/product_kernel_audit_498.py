"""Independent exact audit of the fixed step496 certificate; standard library.

Uses the finite formal logarithm expansion, not the generating script's
Newton recurrence. Run from the notebook; writes a separate full report.
"""
from fractions import Fraction as Q
from math import factorial, prod
from pathlib import Path
import json

HERE = Path(__file__).parent
source = HERE / "product-kernel-496.json"
saved = json.loads(source.read_text())
checks = []


def check(name, actual, required):
    checks.append({"name": name, "actual": actual, "required": required,
                   "pass": actual == required})


def encoded(p):
    return [{"exponents_m0_to_m6": list(e), "coefficient": str(c)}
            for e, c in sorted(p.items()) if c]


def partitions(k, j=1):
    if j == 6:
        if k % 6 == 0:
            yield (k // 6,)
        return
    for n in range(k // j + 1):
        for rest in partitions(k - j*n, j+1):
            yield (n,) + rest


# Direct coefficient division in P_6 simplifies c_j to
# (-1)^j 12!/[j!(12-2j)!] * m_(6-j)/m_6.
constants = [Q((-1)**j * factorial(12), factorial(j)*factorial(12-2*j))
             for j in range(1, 7)]
check("monic coefficients", saved["monic_constants_c1_to_c6"],
      [str(c) for c in constants])

# If C(z)=1+sum c_j z^j, then sum_(k>=1) s_k z^k=-z C'(z)/C(z).
# Expanding -k[z^k]log C gives the independent partition formula below.
s = [{(0,)*7: Q(6)}]
for k in range(1, 11):
    p = {}
    for counts in partitions(k):
        r = sum(counts)
        factor = Q(k * (-1)**r * factorial(r-1),
                   prod(factorial(n) for n in counts))
        coefficient = factor * prod(c**n for c, n in zip(constants, counts))
        e = [0]*7
        for j, n in enumerate(counts, 1):
            e[6-j] = n
        e[6] = -r
        e = tuple(e)
        p[e] = p.get(e, Q(0)) + coefficient
    s.append({e: c for e, c in p.items() if c})

check("all Laurent coefficients s0..s10", saved["newton_sums_s0_to_s10"],
      [encoded(p) for p in s])
N = max(-e[6] for p in s for e in p)
check("least denominator power", saved["least_denominator_power"], N)
check("required denominator power", N, 10)
minimal = {"exponents": [0, 0, 0, 0, 0, 10, -10],
           "coefficient": str(132**10)}
check("noncancelling minimality monomial", saved["minimality_witness"], minimal)
check("minimality coefficient computed independently",
      str(s[10][tuple(minimal["exponents"])]), minimal["coefficient"])
b = [{e[:6] + (e[6]+10,): c for e, c in p.items()} for p in s]
check("all cleared coefficients b0..b10", saved["cleared_polynomials_b0_to_b10"],
      [encoded(p) for p in b])
check("nonnegative exponents", all(min(e) >= 0 for p in b for e in p), True)
check("total degree of every monomial",
      sorted({sum(e) for p in b for e in p}), [10])
check("saved total degree", saved["homogeneous_total_degree"], 10)
check("index weight in every bk",
      all(sum(j*n for j, n in enumerate(e)) == 60-k
          for k, p in enumerate(b) for e in p), True)
check("saved index-weight convention", saved["weighted_degree_bk"], "60-k")

# A labelled slot is the exceptional slot in exactly 9! permutations.
f = [[sum(c*e[j] for e, c in p.items())/10 for j in range(7)] for p in b]
check("all one-outlier coefficients", saved["one_outlier_coefficients_t0_t2_to_t12"],
      [[str(x) for x in row] for row in f])
written_first_five = [
    [0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, Q(66, 5), Q(594, 5)],
    [0, 0, 0, 0, -1188, Q(17424, 5), Q(16236, 5)],
    [0, 0, 0, 33264, -235224, Q(2273832, 5), Q(137808, 5)],
    [0, 0, -332640, 5854464, -27285984, Q(222469632, 5), Q(-36713952, 5)],
]
check("five polynomials printed in L794", f[:5], written_first_five)
A = [[f[i+j][6] for j in range(6)] for i in range(6)]
check("complete leading matrix", saved["one_outlier_leading_matrix"],
      [[str(x) for x in row] for row in A])

# Independent elimination of just the complete 3x3 witness block.
d0 = A[0][0]
l10, l20 = A[1][0]/d0, A[2][0]/d0
d1 = A[1][1] - l10*l10*d0
l21 = (A[2][1] - l20*l10*d0)/d1
d2 = A[2][2] - l20*l20*d0 - l21*l21*d1
check("leading LDL pivots", saved["leading_LDL_pivots_until_stop"],
      [str(x) for x in [d0, d1, d2]])
check("pivot sign pattern", [d0 > 0, d1 > 0, d2 < 0], [True]*3)
v = [l10*l21-l20, -l21, Q(1), Q(0), Q(0), Q(0)]


def quadratic(vector, a):
    return sum(vector[i]*vector[j]*f[i+j][a] for i in range(6) for j in range(6))


q = [quadratic(v, a) for a in range(7)]
w = [Q(-152988), Q(4638), Q(113), Q(0), Q(0), Q(0)]
qw = [quadratic(w, a) for a in range(7)]
primitive = [0, 0, -893830, 23068724, -121938843, 206347856, -28504137]
check("integer witness is 113 times rational witness", w, [113*x for x in v])
check("all integer quadratic coefficients", qw, [4752*x for x in primitive])
C = sum(abs(x) for x in q[:6])
ratio = C/(-q[6])
value = sum(x*4**(2*a) for a, x in enumerate(q))
integer_value = sum(x*4**(2*a) for a, x in enumerate(qw))
expected_witness = {
    "vector": [str(x) for x in v],
    "quadratic_coefficients_t0_t2_to_t12": [str(x) for x in q],
    "leading_coefficient": str(q[6]),
    "lower_absolute_sum_C": str(C),
    "required_t_squared_strictly_greater_than": str(ratio),
    "integer_tail_threshold": 4,
    "actual_threshold_squared": 16,
    "exact_quadratic_value_at_threshold": str(value),
    "integer_vector": [str(x) for x in w],
    "integer_quadratic_common_factor": 4752,
    "integer_quadratic_primitive_coefficients_t0_t2_to_t12": primitive,
    "integer_quadratic_exact_value_at_t4": str(integer_value),
}
check("complete negative witness object", saved["negative_witness"], expected_witness)
check("exact value printed in lemma", str(integer_value), "-1281831933403422720")
check("lower absolute coefficient sum", sum(abs(x) for x in primitive[:6]), 352249253)
check("threshold strict", Q(16) > ratio, True)
check("threshold product", 16*28504137, 456066192)
check("negative value", integer_value < 0, True)
check("leading rational quadratic equals pivot", q[6], d2)
check("result", saved["result"], "NEGATIVE_POINTWISE_PSD")

report = {
    "source_certificate": str(source),
    "method": "independent finite formal-log partition expansion; all saved algebraic values compared",
    "checks": checks,
    "check_count": len(checks),
    "failures": [c["name"] for c in checks if not c["pass"]],
    "actual_t_squared": 16,
    "required_t_squared_strictly_greater_than": str(ratio),
    "exact_integer_quadratic_value_at_t4": str(integer_value),
    "analytic_scope": "Fubini, minimality and open-set proof require written audit; not software claims",
}
output = HERE / "product-kernel-audit-498.json"
output.write_text(json.dumps(report, indent=2, default=str) + "\n")
print("Independent coefficient/witness checks:", len(checks))
print("Failures:", report["failures"])
print("Actual t^2: 16; required >", ratio)
print("Exact integer witness:", integer_value, "; required < 0")
print("Full audit certificate:", output)
if report["failures"]:
    raise SystemExit(1)
