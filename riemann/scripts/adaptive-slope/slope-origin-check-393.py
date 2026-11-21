#!/usr/bin/env python3
"""Exact finite germ diagnostics for C997y; not an all-n proof or audit."""

import json
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path


def z(a=0, b=0):
    return (F(a), F(b))


ZERO, ONE, I = z(), z(1), z(0, 1)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def div(a, b):
    den = b[0] ** 2 + b[1] ** 2
    assert den > 0
    return mul(a, (b[0] / den, -b[1] / den))


def power(a, k):
    out = ONE
    for _ in range(k):
        out = mul(out, a)
    return out


def total(xs):
    out = ZERO
    for x in xs:
        out = add(out, x)
    return out


def product(a, b, degree):
    return [total(mul(a[j], b[k-j]) for j in range(k+1)
                  if j < len(a) and k-j < len(b))
            for k in range(degree+1)]


def exponential(a, degree):
    return [div(power(a, k), z(factorial(k))) for k in range(degree+1)]


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, tuple):
        return {"real": str(value[0]), "imag": str(value[1])}
    if isinstance(value, list):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    return value


def check_germ(n, mode):
    m = isqrt(n) + (isqrt(n) ** 2 != n)
    p = [z(F((-1)**j * comb(n+3, j+2), (n+1)*factorial(j)))
         if j <= n+1 else ZERO for j in range(m+1)]
    p[0] = add(p[0], z(-F(1, n+1)))
    cosh = [z(F(3, 8)**j / factorial(j)) if j % 2 == 0 else ZERO
            for j in range(m+1)]
    g = product(product(p, exponential(z(-F(1, 2)), m), m), cosh, m)
    coefficients = {} if mode == "zero" else {
        0: z(F(1, 4), F(1, 8)), n: z(-F(1, 3), F(1, 7))}
    # This rational coordinate bound implies the original complex l1 cap.
    cap_sufficient = sum(abs(a[0]) + abs(a[1]) for a in coefficients.values())
    assert cap_sufficient < 1
    h = exponential(z(-F(1, 8), 1), m)
    for j, a in coefficients.items():
        gamma = F(15, 8) + F(j, 4*n)
        terms = exponential(z(0, gamma), m)
        h = [add(h[k], neg(mul(a, terms[k]))) for k in range(m+1)]
    q = product(g, h, m)
    b = [F((n+2)**(k+1)-n**(k+1), k+1) for k in range(m+1)]
    assert all(b[k] >= 2*n**k for k in range(m+1))
    # An arbitrary constant checks exact lower-window elimination, not a
    # numerical evaluation of the actual lower-window integral.
    lower_constant = z(F(7, 11), -F(2, 5))
    D = [neg(lower_constant)] + [mul(z(b[k]), q[k]) for k in range(m+1)]
    R = [mul(z(-2), x) for x in
         product(exponential(z(-F(n, 4)), m+1), D, m+1)]
    recovered_D = [mul(z(-F(1, 2)), x) for x in
                   product(exponential(z(F(n, 4)), m+1), R, m+1)]
    recovered_q = [div(recovered_D[k+1], z(b[k])) for k in range(m+1)]
    recovered_h = []
    for k in range(m+1):
        cross = total(mul(g[j], recovered_h[k-j]) for j in range(1, k+1))
        recovered_h.append(div(add(recovered_q[k], neg(cross)), g[0]))
    centered = product(exponential(z(0, -2), m), recovered_h, m)[m]
    d = z(-1, F(1, 8))
    extracted = div(mul(z(factorial(m)), centered), mul(power(I, m), power(d, m)))
    direct = ONE
    for j, a in coefficients.items():
        gamma_minus_two = F(15, 8) + F(j, 4*n) - 2
        direct = add(direct, neg(mul(a, power(div(z(gamma_minus_two), d), m))))
    flags = {
        "constant_term": g[0] == z(F(n+4, 2)),
        "gauge_identity": recovered_D == D,
        "window_inversion": recovered_q == q,
        "deconvolution": recovered_h == h,
        "centered_moment": extracted == direct,
    }
    return {
        "n": n, "m": m, "mode": mode,
        "coefficients": {str(j): a for j, a in coefficients.items()},
        "sufficient_l1_bound": cap_sufficient,
        "artificial_lower_constant": lower_constant,
        "g_coefficients": g, "q_coefficients": q, "b_coefficients": b,
        "gauged_coefficients": D, "residual_coefficients": R,
        "recovered_gauged_coefficients": recovered_D,
        "recovered_h_coefficients": recovered_h,
        "direct_moment": direct, "extracted_moment": extracted,
        "difference": add(extracted, neg(direct)), "checks": flags,
    }


def main():
    runs = [check_germ(n, mode) for n in (2, 8, 17, 64, 256)
            for mode in ("zero", "complex")]
    exp4_partial = sum(F(4)**j / factorial(j) for j in range(6))
    scalar_checks = {
        "exp4_partial_exceeds_256_over_7": exp4_partial > F(256, 7),
        "theta_star_less_than_one_tenth": 5**10 < 10*4**10,
        "scalar_cost_floor_exceeds_required": F(45, 8) > F(1, 64),
        "local_relative_K_error_below_half": F(10, 63) < F(1, 2),
    }
    with localcontext() as ctx:
        ctx.prec = 70
        kappa = Decimal(81)/8 + Decimal(2).ln()
        theta_star = (Decimal(5)/4).ln()/Decimal(10).ln()
        diagnostics = {
            "label": "Decimal diagnostics only; exact inequalities carry comparisons",
            "kappa": str(kappa), "Lambda": str(Decimal(131071)*kappa),
            "theta_star": str(theta_star),
            "best_scalar_cost_floor": str(Decimal(5)/8*(1/theta_star-1)),
        }
    failures = [f"n={run['n']},mode={run['mode']}:{key}"
                for run in runs for key, ok in run["checks"].items() if not ok]
    failures += [key for key, ok in scalar_checks.items() if not ok]
    result = {
        "scope": "Exact finite germ diagnostics, not the all-n proof or independent audit",
        "runs": runs,
        "exact_scalar_values": {
            "exp4_six_term_sum": exp4_partial,
            "exp4_required_threshold": F(256, 7),
            "propagation_alpha": F(1, 131072),
            "scalar_cost_strict_lower_bound": F(45, 8),
            "required_rate_upper_threshold": F(1, 64),
            "theta_test_integer_left": 5**10,
            "theta_test_integer_right": 10*4**10,
        },
        "scalar_checks": scalar_checks,
        "diagnostics": diagnostics,
        "failures": failures,
    }
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(encode(result), indent=2) + "\n")
    for run in runs:
        print(f"n={run['n']}, m={run['m']}, {run['mode']}: "
              f"all exact germ checks={all(run['checks'].values())}, "
              f"moment equality={run['checks']['centered_moment']}")
    print(f"Scalar checks: {scalar_checks}")
    print(f"Proved-rate Lambda diagnostic={diagnostics['Lambda']}; required <1/64")
    print("Best scalar cost >45/8; required <1/64. Fixed certificate misses.")
    print(f"Failures: {failures}")
    print(f"Certificate: {out.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
