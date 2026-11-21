"""Exact finite replay of post49 at lambda=3/4; no parameter search.

Run from the notebook: python3 scripts/pollaczek/fixed_step_audit_111.py
Only Python's standard library is used. Full polynomials go to JSON.
"""
from fractions import Fraction as R
from itertools import permutations
from math import factorial
from pathlib import Path
import json

NAMES = ("x", "A", "Q", "Y", "epsilon")
ZERO = (0,) * len(NAMES)


class Poly:
    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.t = dict(value.t)
        elif isinstance(value, dict):
            self.t = {k: R(v) for k, v in value.items() if v}
        else:
            self.t = {ZERO: R(value)} if value else {}

    def __add__(self, other):
        result = dict(self.t)
        for k, v in Poly(other).t.items():
            result[k] = result.get(k, 0) + v
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + -Poly(other)

    def __rsub__(self, other):
        return Poly(other) + -self

    def __mul__(self, other):
        result = {}
        for k, v in self.t.items():
            for l, w in Poly(other).t.items():
                m = tuple(a+b for a, b in zip(k, l))
                result[m] = result.get(m, 0) + v*w
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = Poly(1)
        for _ in range(n):
            result = result * self
        return result

    def __eq__(self, other):
        return self.t == Poly(other).t

    def coeff(self, var, n):
        i = NAMES.index(var)
        return Poly({k[:i]+(0,)+k[i+1:]: v
                     for k, v in self.t.items() if k[i] == n})

    def degree(self, var):
        i = NAMES.index(var)
        return max((k[i] for k in self.t), default=-1)

    def sub(self, **values):
        result = Poly()
        for k, v in self.t.items():
            term = Poly(v)
            for i, n in enumerate(k):
                term = term * Poly(values.get(NAMES[i], VARIABLES[i]))**n
            result += term
        return result

    def scalar(self):
        assert not self.t or set(self.t) == {ZERO}
        return self.t.get(ZERO, R(0))

    def terms(self):
        return [{"powers": dict(zip(NAMES, k)), "coefficient": str(v)}
                for k, v in sorted(self.t.items(), reverse=True)]


VARIABLES = [Poly({ZERO[:i]+(1,)+ZERO[i+1:]: 1})
             for i in range(len(NAMES))]
x, A, Q, Y, E = VARIABLES
checks = []


def check(name, condition):
    checks.append({"name": name, "passed": bool(condition)})


# First construction: imported three-term recurrence, fixed lambda.
lam = R(3, 4)
P = [Poly(1), x]
for n in range(1, 6):
    P.append(x*P[-1] - R(n, 4)*(n+2*lam-1)*P[-2])

# Independent construction from log of imported generating function:
# log G = -lambda log(1+z^2) + 2x arctan(z), as formal series.
h = [Poly()]
for k in range(1, 7):
    h.append(2*x*R((-1)**((k-1)//2), k) if k % 2
             else Poly(-lam*R((-1)**(k//2+1), k//2)))
g = [Poly(1)]
for n in range(1, 7):
    g.append(sum((k*h[k]*g[n-k] for k in range(1, n+1)), Poly())*R(1, n))
for n in range(7):
    check(f"recurrence_vs_generating_function_degree_{n}",
          P[n] == g[n]*R(factorial(n), 2**n))


def triangular(p):
    remainder, coefficients = Poly(p), {}
    for n in range(6, -1, -1):
        coefficients[n] = remainder.coeff("x", n)
        remainder -= coefficients[n]*P[n]
    check("triangular_zero_remainder", remainder == 0)
    return coefficients


def image_cubic(coefficients):
    image = sum((coefficients[n]*Q**(n//2)*P[n]
                 for n in (0, 2, 4, 6)), Poly())
    result = Poly()
    for n in range(7):
        coefficient = image.coeff("x", n)
        if n % 2:
            check(f"image_odd_coefficient_{n}_zero", coefficient == 0)
            continue
        # Each coefficient contains Q^(n/2); divide monomialwise exactly.
        for k, v in coefficient.t.items():
            kk = list(k)
            assert kk[2] >= n//2
            kk[2] -= n//2
            kk[3] += n//2
            result += Poly({tuple(kk): v})
    check("image_equals_F_Qx_squared", result.sub(Y=Q*x*x) == image)
    check("F_monic", result.coeff("Y", 3) == 1)
    return result


def discriminant(F):
    b, c, d = (F.coeff("Y", j) for j in (2, 1, 0))
    return b*b*c*c - 4*c**3 - 4*b**3*d - 27*d*d + 18*b*c*d


c = triangular((x*x-A)**3)
expected_c = {
    6: Poly(1), 4: -3*A+R(125, 8),
    2: 3*A*A-R(51, 4)*A+R(1849, 64),
    0: -A**3+R(9, 8)*A*A-R(117, 64)*A+R(1137, 512)}
for n in range(7):
    check(f"full_triangular_coefficient_{n}", c[n] == expected_c.get(n, 0))
F = image_cubic(c)
b, cc, d = (F.coeff("Y", j) for j in (2, 1, 0))
depressed_p = cc - R(1, 3)*b*b
depressed_q = R(2, 27)*b**3 - R(1, 3)*b*cc + d
D = discriminant(F)
check("depressed_cubic_identity", D == -4*depressed_p**3-27*depressed_q**2)
check("discriminant_A_degree_4", D.degree("A") == 4)
check("leading_A4_exact", D.coeff("A", 4) == -432*(Q-1)**2)
check("depressed_p_A_degree_1", depressed_p.degree("A") == 1)
check("depressed_p_A1", depressed_p.coeff("A", 1) == -R(37, 2)*(Q-1))
check("depressed_q_A_degree_2", depressed_q.degree("A") == 2)
check("depressed_q_A2", depressed_q.coeff("A", 2) == -4*(Q-1))
check("F_at_A_A2", F.sub(Y=A).coeff("A", 2) == -4*(Q-1))

# Independent resultant check: full 5x5 Sylvester determinant.
f = [Poly(1), b, cc, d]
fp = [Poly(3), 2*b, cc]
M = [f+[Poly()], [Poly()]+f,
     fp+[Poly(), Poly()], [Poly()]+fp+[Poly()], [Poly(), Poly()]+fp]
resultant = Poly()
for perm in permutations(range(5)):
    inversions = sum(perm[i] > perm[j] for i in range(5) for j in range(i+1, 5))
    term = Poly((-1)**inversions)
    for i in range(5):
        term *= M[i][perm[i]]
    resultant += term
check("discriminant_equals_negative_full_resultant", D == -resultant)

# One source witness, and one explicit small simple-root perturbation.
witness_D = D.sub(A=1000, Q=4).scalar()
check("source_exact_witness", witness_D == R(-29043991764668664081, 8192))
perturbed = (x*x-(A-E))*(x*x-A)*(x*x-(A+E))
ce = triangular(perturbed)
Fe = image_cubic(ce)
check("perturbation_limit", Fe.sub(epsilon=0) == F)
De = discriminant(Fe)
ep = R(1, 10)
perturbed_D = De.sub(A=1000, Q=4, epsilon=ep).scalar()
perturbed_coefficients = {n: ce[n].sub(A=1000, epsilon=ep).scalar()
                          for n in (0, 2, 4, 6)}
check("perturbed_witness_discriminant_negative", perturbed_D < 0)
check("perturbed_witness_strict_alternation",
      all(perturbed_coefficients[n]*(-1)**(n//2+1) > 0
          for n in (0, 2, 4, 6)))
check("perturbed_squared_roots_positive_distinct", 0 < ep < 1000)

output = {
    "scope": "lambda=3/4; symbolic A,Q; Q>0,Q!=1 fixed before A grows",
    "checks": checks,
    "failures": [r["name"] for r in checks if not r["passed"]],
    "basis": {str(n): P[n].terms() for n in range(7)},
    "triangular_coefficients": {str(n): c[n].terms() for n in range(7)},
    "F": F.terms(), "F_at_A": F.sub(Y=A).terms(),
    "depressed_p": depressed_p.terms(), "depressed_q": depressed_q.terms(),
    "discriminant_coefficients_in_A": {str(n): D.coeff("A", n).terms()
                                       for n in range(5)},
    "full_resultant": resultant.terms(),
    "perturbed_F": Fe.terms(), "perturbed_discriminant": De.terms(),
    "witness": {"A": "1000", "Q": "4", "epsilon": "1/10",
                "unperturbed_discriminant": str(witness_D),
                "perturbed_discriminant": str(perturbed_D),
                "perturbed_basis_coefficients": {str(n): str(v)
                                                 for n, v in perturbed_coefficients.items()}},
    "required_bound": "disc(F)<0 for all sufficiently large A at each fixed Q>0,Q!=1",
    "actual_bound": "disc(F)=-432(Q-1)^2 A^4 + polynomial_in_A_of_degree_at_most_3",
    "perturbation_qualification": "epsilon chosen after fixed Q and suitable A; no uniform epsilon claimed",
}
path = Path(__file__).with_name("fixed-step-audit-111.json")
path.write_text(json.dumps(output, indent=2)+"\n")
print(f"Checks: {sum(r['passed'] for r in checks)}/{len(checks)}; failures: {output['failures']}")
print("Actual/required: exact A4 coefficient -432(Q-1)^2<0 for fixed Q>0,Q!=1; remainder degree <=3.")
print(f"Witness: disc={witness_D}; perturbed disc={perturbed_D}<0.")
print(f"Certificate: {path}")
raise SystemExit(bool(output["failures"]))
