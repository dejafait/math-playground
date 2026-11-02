"""Exact normalization checks for L652; no angular-mean claim.

The uniform exponential estimates are proved in the lemma, not inferred
from these finite rational computations. All certificate data stay on disk.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def product(factors):
    out = [F(1)]
    for factor in factors:
        out = mul(out, factor)
    return out


def series(num, den, length):
    out = []
    for k in range(length):
        rhs = num[k] if k < len(num) else F(0)
        rhs -= sum(den[j] * out[k-j]
                   for j in range(1, min(k, len(den)-1)+1))
        out.append(rhs / den[0])
    return out


def value(poly, z):
    out = F(0)
    for c in reversed(poly):
        out = out * z + c
    return out


d, R = F(5, 4), F(11, 8)
x, U = -d, R*R
g = lambda t: 1/(d+t) - t/(U+d*t)
quarter_values = [g(F(k, 4)) for k in range(1, 5)]
lambda_star = sum(quarter_values)/32
constants = {
    "quarter_values": quarter_values,
    "lambda_star": lambda_star,
    "required_amplitude_rate": F(1, 32),
    "proved_amplitude_rate": F(1, 25),
    "lambda_minus_proved_rate": lambda_star-F(1, 25),
    "squared_exponent_margin": F(2, 25)-F(1, 16),
    "tail_base_per_mass": F(125, 128),
    "exp_24_over_25_lower": 1+F(24, 25)+F(24, 25)**2/2,
    "constant_dual_relative_energy": (U-d*d)/U,
}
constant_checks = {
    "lambda_above_one_over_25": lambda_star > F(1, 25),
    "tail_base_below_one": F(125, 128) < 1,
    "n24_exp_lower_above_two": constants["exp_24_over_25_lower"] > 2,
    "positive_squared_margin": constants["squared_exponent_margin"] > 0,
    "constant_dual_ratio": constants["constant_dual_relative_energy"] == F(21, 121),
}

records = []
for n in (6, 12, 24, 36):
    m = n//3
    ts = [F(j, n) for j in range(n)]
    av = [t/(U+d*t) for t in ts]
    cv = [1/(d+t) for t in ts]
    num_h = product([[F(1), -a] for a in av])
    den_h = product([[F(1), -c] for c in cv])
    coeff_h = series(num_h, den_h, m)
    # H(x+w)=sum a_k*(-w)^k. Verify modular equality in w.
    coeff_w = [(-1)**k * a for k, a in enumerate(coeff_h)]
    num_w = product([[F(1), a] for a in av])
    den_w = product([[F(1), c] for c in cv])
    multiplied = mul(coeff_w, den_w)
    residual = [multiplied[k]-num_w[k] for k in range(m)]
    # Convert H(R*zeta)=sum a_k*(x-R*zeta)^k without sampling.
    s = [sum(coeff_h[k] * comb(k, ell) * x**(k-ell) * (-R)**ell
             for k in range(ell, m)) for ell in range(m)]
    norm_s2 = sum(v*v for v in s)
    boundary = value(s, F(-1))
    phi_h = value(num_h, F(1, 8))/value(den_h, F(1, 8))
    actual_tail = phi_h-boundary
    tail_bound = F(1, 2)**m * F(5, 4)**n
    # Entire negative part of b J s: every beta up to m-1 suffices.
    alphas = [t/R for t in ts]
    bnum = product([[-a, F(1)] for a in alphas])
    bden = product([[F(1), -a] for a in alphas])
    beta = series(bnum, bden, m)
    e = [sum(beta[k-j]*s[k] for k in range(j, m)) for j in range(m)]
    norm_e2 = sum(v*v for v in e)
    norm_v2 = norm_s2-norm_e2
    bx = F(1)
    for t in ts:
        bx *= R*(x-t)/(U-t*x)
    hv = [m/R*(x/R)**j for j in range(m)]
    correction = bx*sum(hj*ej for hj, ej in zip(hv, e))
    response = correction-m/R
    monomial_response = [bx*sum(hv[j]*beta[k-j] for j in range(k+1))-hv[k]
                         for k in range(m)]
    response_residual = response-sum(a*b for a, b in zip(s, monomial_response))
    diag = m*m/(U-d*d)
    checks = {
        "all_modular_coefficients_zero": all(v == 0 for v in residual),
        "all_phi_coefficients_nonnegative": all(v >= 0 for v in coeff_h),
        "interpolation_value_one": value(s, x/R) == 1,
        "boundary_eval_matches_series": boundary == value(coeff_h, F(1, 8)),
        "complete_tail_nonnegative": actual_tail >= 0,
        "complete_tail_within_bound": actual_tail <= tail_bound,
        "boundary_cauchy_schwarz": boundary*boundary <= m*norm_s2,
        "gram_lower_five_thirteenths": norm_v2 >= F(5, 13)*norm_s2,
        "full_response_identity": response_residual == 0,
    }
    records.append({
        "n": n, "mass": m, "u": 1,
        "in_asymptotic_subsequence": n % 12 == 0 and n >= 24,
        "phi_coefficients": coeff_h, "polynomial_coefficients": s,
        "modular_residual": residual, "response_residual": response_residual,
        "norm_s_squared": norm_s2, "boundary_value": boundary,
        "actual_tail": actual_tail, "required_tail_upper": tail_bound,
        "norm_negative_squared": norm_e2, "norm_dual_squared": norm_v2,
        "correction": correction, "response": response,
        "diagonal": diag, "normalized_relative_response": response**2/norm_v2/diag,
        "checks": checks,
    })

failures = [key for key, passed in constant_checks.items() if not passed]
failures += [f"n={r['n']}:{key}" for r in records
             for key, passed in r["checks"].items() if not passed]
certificate = {
    "scope": "Exact finite repeated-anchor remainder normalization; no angular mean or uniform numerical proof.",
    "constants": constants, "constant_checks": constant_checks,
    "cases": records, "failures": failures,
    "limitations": ["Only u=1 is tested.", "Uniform estimates are analytic in L652.",
                    "Close-pair and confluent limits are proved analytically, not sampled."],
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate, default=str, indent=2)+"\n")
print(f"Exact checks: {len(constant_checks)+sum(len(r['checks']) for r in records)}; failures: {failures}")
print(f"lambda={float(lambda_star):.9f} > proved 1/25=0.04 > required amplitude 1/32=0.03125")
print(f"Squared margin: {constants['squared_exponent_margin']}; full certificate: {path}")
for r in records:
    print(f"n={r['n']}: norm^2={float(r['norm_s_squared']):.6g}; actual tail={float(r['actual_tail']):.6g} <= {float(r['required_tail_upper']):.6g}; residuals=0: {r['checks']['all_modular_coefficients_zero'] and r['checks']['full_response_identity']}")
raise SystemExit(bool(failures))
