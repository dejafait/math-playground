"""Exact finite algebra checks for L874; no contact search or sign test.

Uses only the standard library. The analytic argument and arbitrary-degree
proof are in L874. Formal g coefficients are indeterminates, not zero data.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


NVARS = 6
ZERO_POWER = (0,) * NVARS


def const(value):
    value = Q(value)
    return {ZERO_POWER: value} if value else {}


def variable(index):
    power = list(ZERO_POWER)
    power[index] = 1
    return {tuple(power): Q(1)}


def add(*polynomials):
    result = {}
    for poly in polynomials:
        for power, coefficient in poly.items():
            result[power] = result.get(power, Q(0)) + coefficient
    return {power: coefficient for power, coefficient in result.items()
            if coefficient}


def scale(poly, scalar):
    return {power: coefficient * scalar for power, coefficient in poly.items()
            if coefficient * scalar}


def mul(left, right):
    result = {}
    for p, a in left.items():
        for q, b in right.items():
            power = tuple(x + y for x, y in zip(p, q))
            result[power] = result.get(power, Q(0)) + a * b
    return {power: coefficient for power, coefficient in result.items()
            if coefficient}


def derivative(poly, index):
    result = {}
    for power, coefficient in poly.items():
        if power[index]:
            reduced = list(power)
            reduced[index] -= 1
            result[tuple(reduced)] = coefficient * power[index]
    return result


def encoded(poly):
    return [{"powers": list(power), "coefficient": str(coefficient)}
            for power, coefficient in sorted(poly.items())]


checks = []


def check(name, residual):
    checks.append({"name": name, "passed": not residual,
                   "exact_residual": encoded(residual)})


# q_n=[z^(2n)]g, q_0=1. Derive log g via g'=g (log g)',
# independently of the proposed time evolution for S.
q = [const(1)] + [variable(i) for i in range(NVARS)]
S = [{}]
inverse = [const(1)]
for n in range(1, NVARS + 1):
    S.append(add(scale(q[n], -n),
                 scale(add(*(mul(S[j], q[n-j])
                             for j in range(1, n))), -1)))
    inverse.append(scale(add(*(mul(q[j], inverse[n-j])
                               for j in range(1, n+1))), -1))

# Normalized heat flow: q_n'=-(2n+2)(2n+1)q_(n+1)+2q_1 q_n.
q_dot = [{}] + [add(scale(q[n+1], -(2*n+2)*(2*n+1)),
                       scale(mul(q[1], q[n]), 2))
                   for n in range(1, NVARS)]
moments = [scale(q[j], (-1)**j * factorial(2*j))
           for j in range(NVARS + 1)]

for n in range(1, NVARS):
    direct_dot = add(*(mul(derivative(S[n], j-1), q_dot[j])
                       for j in range(1, n+1)))
    proposed_dot = add(scale(S[n+1], -2*n*(2*n+1)),
                       scale(add(*(mul(S[a], S[n+1-a])
                                   for a in range(1, n+1))), 4*n))
    check(f"coefficient_flow_k{n}", add(direct_dot, scale(proposed_dot, -1)))
    terms = [scale(inverse[n-j], Q((-1)**j, factorial(2*j)))
             for j in range(n+1)]
    expectation = add(*(mul(terms[j], moments[j]) for j in range(n+1)))
    dilation = add(*(scale(mul(terms[j], moments[j]), 2*j)
                     for j in range(n+1)))
    u2_response = add(*(mul(terms[j], moments[j+1]) for j in range(n+1)))
    check(f"response_mean_k{n}", expectation)
    check(f"response_dilation_k{n}", add(dilation, scale(S[n], 2)))
    check(f"response_time_k{n}", add(direct_dot, scale(u2_response, n)))

# Scalar contact: m_4=3m_2^2; direct normalized moment differentiation.
M, T = variable(0), variable(1)
M2, M3 = mul(M, M), mul(mul(M, M), M)
m4 = scale(M2, 3)
scalar_flux = scale(add(scale(mul(M, add(m4, scale(M2, -1))), 6),
                        scale(T, -1), mul(m4, M)), Q(1, 12))
scalar_expected = scale(add(scale(T, -1), scale(M3, 15)), Q(1, 12))
check("scalar_contact_flux", add(scalar_flux, scale(scalar_expected, -1)))

# d=1 full-degree contact. a=S_2>0,b=S_3,t=S_5,w=S_1;
# multiply c^T H_1' c by a^2 before substituting S_4=b^2/a.
a, b, t, w = (variable(i) for i in range(4))
a2, b2 = mul(a, a), mul(b, b)
a3, b3 = mul(a2, a), mul(b2, b)
scaled_flux = add(
    mul(b2, add(scale(b, -20), scale(mul(w, a), 16))),
    scale(mul(b, add(scale(b2, -42), scale(mul(w, mul(a, b)), 24),
                     scale(a3, 12))), -2),
    mul(a, add(scale(mul(a, t), -72), scale(mul(w, b2), 32),
               scale(mul(a2, b), 32))))
scaled_expected = add(scale(mul(a2, t), -72), scale(b3, 64),
                      scale(mul(a3, b), 8))
check("rank_one_contact_flux_scaled_by_a_squared",
      add(scaled_flux, scale(scaled_expected, -1)))

failures = [item["name"] for item in checks if not item["passed"]]
certificate = {
    "scope": "Exact formal algebra for k=1,...,5 and d=0,1 checks; no actual contacts or theta sign certified.",
    "method": "Sparse multivariate polynomials over Fraction, normalized heat coefficient differentiation, finite reciprocal-series response.",
    "variables_for_series": [f"q_{j}" for j in range(1, NVARS+1)],
    "logarithmic_coefficients": {f"S_{n}": encoded(S[n])
                                 for n in range(1, NVARS+1)},
    "checks": checks,
    "scalar_bound_comparison": {
        "premise": "m_4=3m_2^2, m_2>0 (hypothetical actual-theta scalar contact)",
        "actual_available_cauchy_schwarz_constant": 9,
        "required_constant_for_nonpositive_flux": 15,
        "certifies_requested_sign": False,
        "is_actual_contact_or_counterexample": False},
    "summary": {"checks": len(checks), "passed": len(checks)-len(failures),
                "failures": failures, "actual_theta_sign_proved": False},
}
output = Path(__file__).with_name("reciprocal-hankel-contact-algebra-20261106.json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact algebra: {len(checks)-len(failures)}/{len(checks)} pass; failures: {failures}")
print("Scalar contact bound: available 9; required 15; actual theta sign unproved.")
print(f"Certificate: {output}")
raise SystemExit(bool(failures))
