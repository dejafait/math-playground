"""Exact bounded harmonic-0--4 test; infinite sums justified in L432.

Run from riemann: python3 scripts/discriminant/prime_power_cubic_toeplitz.py
All field elements are rational pairs a+b*sqrt(2), without floating point.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    return a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def sign(a):
    p, q = a
    if not q:
        return (p > 0)-(p < 0)
    if not p:
        return (q > 0)-(q < 0)
    if p*q > 0:
        return (p > 0)-(p < 0)
    delta = p*p-2*q*q
    if delta == 0:
        raise ArithmeticError("nonzero rational square cannot equal twice a square")
    return ((p > 0)-(p < 0))*((delta > 0)-(delta < 0))


def determinant(matrix):
    total = (F(0), F(0))
    for perm in permutations(range(len(matrix))):
        inversions = sum(perm[i] > perm[j]
                         for i in range(len(perm)) for j in range(i+1, len(perm)))
        term = (F((-1)**inversions), F(0))
        for i, j in enumerate(perm):
            term = mul(term, matrix[i][j])
        total = add(total, term)
    return total


def encode(a):
    return {"rational": str(a[0]), "sqrt2": str(a[1])}


def rational_determinant(matrix):
    work = [row[:] for row in matrix]
    result = F(1)
    for k in range(len(work)):
        pivot = next((i for i in range(k, len(work)) if work[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            result = -result
        value = work[k][k]
        result *= value
        for i in range(k+1, len(work)):
            ratio = work[i][k]/value
            for j in range(k+1, len(work)):
                work[i][j] -= ratio*work[k][j]
    return result


x, y, z, D = F(1, 4), F(1, 8), F(1, 8), F(31, 32)


def local_factor(j):
    # d >= 0: the exponent d+j is nonnegative from L onward.
    L = max(0, -j)
    s0 = z**L/(1-z)
    s1 = z**L*(L/(1-z)+z/(1-z)**2)
    s2 = z**L*(L*L/(1-z)+2*L*z/(1-z)**2+z*(1+z)/(1-z)**3)
    positive = sum((x**d*(1+D*d) for d in range(L)), F(0))
    positive += F(2)**(-j)*((1+F(j, 2))*s0
                    +(D*(1+F(j, 2))+F(1, 2))*s1+D*s2/2)
    # d=-h < 0: the exponent j-h is nonpositive from M onward.
    M = max(1, j)
    negative = sum((y**h*F(2)**(-(j-h))*(1+F(j-h, 2))
                    for h in range(1, M)), F(0))
    negative += y**M/(1-y)
    return (positive+negative)/D**2


B = {j: local_factor(j) for j in range(-4, 5)}
c = []
for j in range(5):
    # 2^(j/2)=2^floor(j/2) times sqrt(2) for odd j;
    # 2^(-j/2)=2^(-floor(j/2)-1)*sqrt(2) for odd j.
    q = (F(2)**(j//2)*B[j]
         +F(2)**(-(j//2)-(j % 2))*B[-j])/(2*B[0])
    c.append((F(0), q) if j % 2 else (q, F(0)))

matrix = [[c[abs(a-b)] for b in range(5)] for a in range(5)]
minors = []
cross_checks = []
stopped = False
for size in range(1, 6):
    for indices in combinations(range(5), size):
        value = determinant([[matrix[a][b] for b in indices] for a in indices])
        s = sign(value)
        # Independent rational elimination after congruence by
        # diag(1,sqrt(2),1,sqrt(2),1).
        rational_matrix = []
        for a in indices:
            row = []
            for b in indices:
                entry = matrix[a][b]
                if a % 2:
                    entry = mul(entry, (F(0), F(1)))
                if b % 2:
                    entry = mul(entry, (F(0), F(1)))
                assert entry[1] == 0
                row.append(entry[0])
            rational_matrix.append(row)
        independent = rational_determinant(rational_matrix)/F(2)**sum(a % 2 for a in indices)
        cross_checks.append(value == (independent, F(0)))
        minors.append({"indices": list(indices), "determinant": encode(value), "sign": s})
        if s < 0:
            stopped = True
            break
    if stopped:
        break

checks = {
    "base_matches_L431": B[0] == F(571520, 329623),
    "plus_matches_L431": B[1] == F(425088, 329623),
    "minus_matches_L431": B[-1] == F(635904, 329623),
    "zeroth_is_one": c[0] == (F(1), F(0)),
    "first_matches_L431": c[1] == (F(0), F(1161, 1786)),
    "all_tested_minors_are_rational": all(m["determinant"]["sqrt2"] == "0" for m in minors),
    "independent_rational_elimination_agrees": all(cross_checks),
    "bounded_test_complete_or_negative": stopped or len(minors) == 31,
}
record = {
    "arithmetic": "exact Q(sqrt(2)); geometric tails evaluated symbolically",
    "harmonic_cutoff": 4,
    "local_factors": {str(j): str(B[j]) for j in B},
    "normalized_coefficients": [encode(a) for a in c],
    "toeplitz": [[encode(a) for a in row] for row in matrix],
    "principal_minors": minors,
    "tested_count": len(minors),
    "required_count_without_early_negative": 31,
    "strict_positive_count": sum(m["sign"] > 0 for m in minors),
    "minimum_by_size": {
        str(size): min((m for m in minors if len(m["indices"]) == size),
                      key=lambda m: F(m["determinant"]["rational"]))
        for size in sorted({len(m["indices"]) for m in minors})
    },
    "first_negative": next((m for m in minors if m["sign"] < 0), None),
    "decision": "OBSTRUCTION" if stopped else "FINITE_PREFIX_COMPATIBLE_ONLY",
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
}
path = Path(__file__).with_name("prime_power_cubic_toeplitz_certificate.json")
path.write_text(json.dumps(record, indent=2)+"\n")
print("normalized coefficients:", "; ".join(f"c{j}={a[0]}+({a[1]})sqrt(2)" for j, a in enumerate(c)))
print(f"principal minors: actual={len(minors)}, required unless early negative=31; "
      f"positive={record['strict_positive_count']}; first_negative={record['first_negative']}")
print(f"decision={record['decision']}; failures={record['failures']}")
print(f"certificate={path}")
assert not record["failures"]
