"""Exact rational certificate for L916's fixed-point full-theta witness.

No floating-point arithmetic, theta truncation, contact or parameter sweep.
Analytic justification of the tail and chain rules is canonical in L916.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


def add(a, b):
    return [(a[i] if i < len(a) else F(0))
            + (b[i] if i < len(b) else F(0))
            for i in range(max(len(a), len(b)))]


def scale(a, c):
    return [c * v for v in a]


def differentiate(a):
    return [i * a[i] for i in range(1, len(a))]


def spatial_derivative(p):
    # d_u(exp(u/2-v)*p(v)) = exp(u/2-v)*D(p)(v), v'=2v.
    return add(add([F(0)] + scale(differentiate(p), 2), scale(p, F(1, 2))),
               [F(0)] + scale(p, -2))


checks = []


def check(name, actual, relation, required):
    passed = {"<": lambda: actual < required,
              ">": lambda: actual > required,
              "==": lambda: actual == required}[relation]()
    checks.append(dict(name=name, actual=actual, relation=relation,
                       required=required, passed=passed))


polynomials = [[F(0), F(-12), F(8)]]
for j in range(3):
    polynomials.append(spatial_derivative(polynomials[-1]))
check("third_derivative_coefficients", polynomials[3], "==",
      list(map(F, [0, F(-375, 2), 1635, -2116, 720, -64])))
C = [sum(map(abs, p)) for p in polynomials]
check("exp_two_positive_partial", sum((F(2**j, factorial(j)) for j in range(5)), F(0)), "==", F(7))
check("exp_three_positive_partial", sum((F(3**j, factorial(j)) for j in range(9)), F(0)), ">", F(20))
# Elementary 3<pi<4, exp(2)>7 and e<3 give 21<v=pi*e^2<36.
vlo, vhi = F(21), F(36)
check("p0_coefficient_lower", 8 - 12/vlo, ">", F(7))
M = {j: C[j] * vhi**j / 7 for j in range(1, 4)}
E = {}
ratios = {}
for j in range(4):
    m = 2*j + 4
    ratios[j] = F(3, 2)**m / 20**35
    check(f"tail_geometric_ratio_j{j}", ratios[j], "<", F(1, 2))
    # n=2+k: n^m<=2^m*(3/2)^(mk), n^2-1>=3+5k.
    # exp(-63)<20^-21 and exp(-105)<20^-35.
    E[j] = C[j] * vhi**j * 2**(m+1) / (7 * 20**21)

d = {j: E[j] + M[j]*E[0] for j in range(1, 4)}
L = {}
L[1] = d[1]
L[2] = d[2] + d[1]*(2*M[1]+d[1])
L[3] = (d[3] + 3*(d[2]*M[1]+M[2]*d[1]+d[2]*d[1])
        + 2*d[1]*(3*M[1]**2+3*M[1]*d[1]+d[1]**2))
log_error = sum(L.values())
check("sum_three_log_derivative_errors", log_error, "<", F(1, 100))
# f1'-f1''-f1''' = 9/2+10v+6/d+24v/d^2-48v(2v+3)/d^3.
dlo = 2*vlo-3
head_S_lower = F(9, 2)+10*vlo - 48*vhi*(2*vhi+3)/dlo**3
check("head_curvature_numerator_lower", head_S_lower, ">", F(212))
full_S_lower = head_S_lower - log_error
hpp_lower = full_S_lower / 4
check("full_h_second_lower", hpp_lower, ">", F(50))
# f1'+f1'' = 9/2-6v+6/d-24v/d^2; lambda=1/40.
head_sum_upper = F(9, 2)-6*vlo + 6/dlo
head_sum_lower = F(9, 2)-6*vhi - 24*vhi/dlo**2
hp_lower = -F(1, 20) - (head_sum_upper+L[1]+L[2])/2
hp_upper = -F(1, 20) - (head_sum_lower-L[1]-L[2])/2
check("full_h_first_lower", hp_lower, ">", F(50))
check("full_h_first_upper", hp_upper, "<", F(110))
inverse_second_upper = -F(50)/110**3
check("negative_inverse_threshold", inverse_second_upper, "==", -F(1, 26620))

failures = [c['name'] for c in checks if not c['passed']]
certificate = dict(
    scope="lambda=1/40, x=1, full L019 theta kernel, inverse at y0=h(1); no contact or flux sign",
    analytic_contracts=[
        "Elementary 3<pi<4 and e<3; strict positive exp-series bounds as recorded.",
        "Uniform convergence through three derivatives near u=1, p_j recurrence, positive K1.",
        "For n=2+k, n<=2(3/2)^k and n^2-1>=3+5k; the geometric bound covers all n>=2.",
        "0<=tail K/K1<=E0, absolute tail derivative ratios<=Ej; rational perturbation bounds.",
        "Log derivative formulas and the inverse function chain rule.",
        "L915's source-qualified global h'>19/10 supplies invertibility, not inverse convexity."],
    derivative_polynomials=polynomials, coefficient_absolute_sums=C,
    bounds=dict(v_interval=[vlo,vhi], head_ratio_bounds=M, tail_ratio_bounds=E,
                geometric_ratio_bounds=ratios, normalized_ratio_errors=d,
                log_derivative_errors=L, sum_log_derivative_errors=log_error,
                head_curvature_numerator_lower=head_S_lower,
                full_curvature_numerator_lower=full_S_lower,
                h_second_lower=hpp_lower, h_first_lower=hp_lower,
                h_first_upper=hp_upper, inverse_second_upper=inverse_second_upper),
    checks=checks,
    summary=dict(checks=len(checks), passed=len(checks)-len(failures), failures=failures,
                 required_h_second_lower="50", required_h_first_interval="(50,110)",
                 certified_inverse_second_upper="-1/26620 (strict)",
                 global_inverse_convexity=False, contact_or_flux_certified=False,
                 analytic_contracts_independently_audited_by_script=False))
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(certificate, default=str, indent=2)+'\n')
print(f"Exact checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
print(f"Head numerator lower: {head_S_lower} > required 212.")
print(f"Full derivative-error bound < 1/100: {log_error < F(1,100)}.")
print(f"Full h''(1)>50 and 50<h'(1)<110: {hpp_lower > 50 and hp_lower > 50 and hp_upper < 110}.")
print(f"Inverse second derivative at h(1) < {inverse_second_upper} < required 0.")
print(f"Certificate: {output}")
raise SystemExit(bool(failures))
