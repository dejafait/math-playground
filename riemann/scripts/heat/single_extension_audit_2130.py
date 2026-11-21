"""Independent exact audit of C874b; no theta realization is inferred."""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path


# Polynomial variables c0,c1,c2,x,y. This does not import the original code.
ZERO = (0,) * 5


def add(*polys):
    result = {}
    for poly in polys:
        for monomial, coeff in poly.items():
            result[monomial] = result.get(monomial, 0) + coeff
    return {m: c for m, c in result.items() if c}


def scale(poly, scalar):
    return {m: c * scalar for m, c in poly.items() if c * scalar}


def mul(a, b):
    result = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            result[m] = result.get(m, 0) + ca * cb
    return {m: c for m, c in result.items() if c}


def power(poly, n):
    result = {ZERO: 1}
    for _ in range(n):
        result = mul(result, poly)
    return result


def diff(poly, variable):
    result = {}
    for m, c in poly.items():
        if m[variable]:
            new = list(m)
            new[variable] -= 1
            result[tuple(new)] = c * m[variable]
    return result


def variable(i):
    m = list(ZERO)
    m[i] = 1
    return {tuple(m): 1}


c = [variable(i) for i in range(3)]
x, y = variable(3), variable(4)
p = add(*(mul(c[i], power(x, i)) for i in range(3)))
py = add(*(mul(c[i], power(y, i)) for i in range(3)))
P = mul(power(x, 2), power(p, 2))
b = {n: add(*(mul(c[i], c[j]) for i in range(3)
              for j in range(3) if i + j + 2 == n)) for n in range(2, 7)}
Q = add(*(scale(mul(b[n], power(x, n - 2)), n) for n in b))
Qy = add(*(scale(mul(b[n], power(y, n - 2)), n) for n in b))
kernel = add(*(scale(mul(b[n], mul(power(x, a - 2), power(y, n - 1 - a))), n)
               for n in b for a in range(2, n)))


def residual(a, b):
    value = add(a, scale(b, -1))
    return [{"exponents": m, "coefficient": coefficient}
            for m, coefficient in sorted(value.items())]


identities = {
    "P_coefficient_identity": residual(P, add(*(mul(b[n], power(x, n)) for n in b))),
    "linear_kernel": residual(
        add(*(scale(mul(b[n], power(x, n - 1)), n * (2 * n + 1)) for n in b)),
        add(scale(mul(x, diff(diff(P, 3), 3)), 2), scale(diff(P, 3), 3))),
    "Q_identity": residual(Q, add(scale(power(p, 2), 2), scale(mul(x, mul(p, diff(p, 3))), 2))),
    "off_diagonal_denominator_cleared": residual(mul(add(x, scale(y, -1)), kernel), add(Q, scale(Qy, -1))),
    "P_second_derivative_root_reduction": residual(
        add(diff(diff(P, 3), 3), scale(mul(power(x, 2), power(diff(p, 3), 2)), -2)),
        mul(p, add(scale(p, 2), scale(mul(x, diff(p, 3)), 8), scale(mul(power(x, 2), diff(diff(p, 3), 3)), 2)))),
    "Q_diagonal_root_reduction": residual(
        add(diff(Q, 3), scale(mul(x, power(diff(p, 3), 2)), -2)),
        scale(mul(p, add(scale(diff(p, 3), 3), mul(x, diff(diff(p, 3), 3)))), 2)),
}


def determinant(matrix):
    if not matrix:
        return F(1)
    return sum(((-1) ** j * matrix[0][j] * determinant(
        [row[:j] + row[j + 1:] for row in matrix[1:]])
                for j in range(len(matrix))), F(0))


original_path = Path(__file__).with_name("single-extension-contact-2128.json")
original = json.loads(original_path.read_text())
atoms = [
    [(1, 2)], [(0, 1), (1, 2)], [(1, F(1, 2))],
    [(-1, F(1, 2))], [(1, 2)], [(1, 2), (2, 4)], [], [],
]
expected_flux = [F(16), F(16), F(-2), F(2), F(0), F(16), F(0), F(0)]
cases = []
for index, case in enumerate(original["cases"]):
    S = {int(k): F(v) for k, v in case["moments"].items()}
    vector = list(map(F, case["c"]))
    h3 = [[S[i + j + 2] for j in range(4)] for i in range(4)]
    minors = []
    for size in range(1, 5):
        for subset in combinations(range(4), size):
            minors.append({"indices": subset, "determinant": str(determinant(
                [[h3[i][j] for j in subset] for i in subset]))})
    null = [sum((S[i + j + 2] * vector[j] for j in range(3)), F(0)) for i in range(3)]
    flux_values = []
    for first in (F(0), F(1)):
        moments = dict(S)
        moments[1] = first
        D = {n: -2 * n * (2 * n + 1) * moments[n + 1]
             + 4 * n * sum((moments[a] * moments[n + 1 - a]
                            for a in range(1, n + 1)), F(0)) for n in range(2, 7)}
        flux_values.append(sum((vector[i] * vector[j] * D[i + j + 2]
                                for i in range(3) for j in range(3)), F(0)))
    root_residuals = [sum((vector[j] * F(t) ** j for j in range(3)), F(0))
                      for t, w in atoms[index]]
    atomic = sum((8 * F(w) * F(t) * (vector[1] + 2 * vector[2] * F(t)) ** 2
                  * (F(w) - F(t) ** 2) for t, w in atoms[index]), F(0))
    moment_residuals = [S[k] - sum((F(w) * F(t) ** (k - 2) for t, w in atoms[index]), F(0))
                        for k in range(2, 8)]
    failures = []
    if any(F(item["determinant"]) < 0 for item in minors):
        failures.append("negative principal minor")
    if [[str(v) for v in row] for row in h3] != case["H3"]:
        failures.append("saved matrix mismatch")
    if any(null) or any(root_residuals) or any(moment_residuals):
        failures.append("null, root or moment residual")
    if flux_values != [expected_flux[index]] * 2 or atomic != expected_flux[index]:
        failures.append("independent flux mismatch")
    if F(case["flux_constant"]) != expected_flux[index] or F(case["flux_S1_coefficient"]) != 0:
        failures.append("saved flux mismatch")
    cases.append(dict(name=case["name"], principal_minors=minors,
                      null_residuals=list(map(str, null)),
                      root_residuals=list(map(str, root_residuals)),
                      moment_residuals=list(map(str, moment_residuals)),
                      flux_at_S1_0_and_1=list(map(str, flux_values)),
                      atomic_flux=str(atomic), expected_flux=str(expected_flux[index]),
                      failures=failures))

failures = [name for name, value in identities.items() if value]
failures += [case["name"] for case in cases if case["failures"]]
if len(cases) != 8 or original["failures"]:
    failures.append("original case count or failure array")
output = Path(__file__).with_name("single-extension-audit-2130.json")
output.write_text(json.dumps(dict(polynomial_residuals=identities, cases=cases,
    failures=failures, summary=dict(polynomial_identities=len(identities), cases=len(cases),
    principal_minors_per_case=15, failures=len(failures), obstruction_flux="16",
    required_upper_bound="0", actual_theta_realization="not tested")), indent=2) + "\n")
print(f"Polynomial identities: {len(identities)}; cases: {len(cases)}; failures: {len(failures)}")
print("All 15 principal minors per matrix checked exactly. Obstruction: 16; required <= 0.")
print(f"Certificate: {output.relative_to(Path.cwd())}")
if failures:
    print(failures)
    raise SystemExit(1)
