#!/usr/bin/env python3
"""Exact algebra supporting L599; analytic justifications remain in L599."""
from fractions import Fraction as Q
import json
from pathlib import Path


def clean(p):
    return {i: a for i, a in p.items() if a}


def add(*polys):
    p = {}
    for poly in polys:
        for i, a in poly.items():
            p[i] = p.get(i, Q(0)) + a
    return clean(p)


def scale(p, a):
    return clean({i: a * v for i, v in p.items()})


def mul(p, q):
    out = {}
    for i, a in p.items():
        for j, b in q.items():
            out[i + j] = out.get(i + j, Q(0)) + a * b
    return clean(out)


def deriv(p):
    return clean({i - 1: i * a for i, a in p.items() if i})


def evaluate(p, x):
    return sum((a * x**i for i, a in p.items()), Q(0))


def serial(p):
    return {str(i): str(a) for i, a in sorted(p.items())}


gd = [{0: Q(1)}]
for _ in range(4):
    gd.append(add(deriv(gd[-1]), mul({1: -Q(1, 4)}, gd[-1])))
kernel = add(gd[0], scale(gd[2], 2), gd[4])
kernel_required = {0: Q(11, 16), 2: Q(1, 32), 4: Q(1, 256)}
poly = {0: Q(1), 2: Q(-2), 4: Q(1)}
laguerre = add(mul(deriv(poly), deriv(poly)),
               scale(mul(poly, deriv(deriv(poly))), -1),
               scale(mul(poly, poly), 4))
spectral = mul(poly, {0: Q(2), 2: Q(-1), 4: Q(1)})
main = evaluate(spectral, Q(3)) / 3
odd_ratio = Q(1, 2**89)  # Proven analytically using e>2 in L599.
tail_prefactor = 2 * 5**7
relative_prefactor = Q(tail_prefactor) / main
relative_bound = Q(100, 2**64)  # Also uses e>2; not a numeric exp preview.

checks = {
    "inverse_kernel_polynomial": kernel == kernel_required,
    "inverse_kernel_positive_coefficients": all(a > 0 for a in kernel.values()),
    "spectral_polynomial": laguerre == scale(spectral, 4),
    "first_odd_coefficient_zero": evaluate(spectral, Q(1)) == 0,
    "third_odd_magnitude": main == Q(4736, 3),
    "odd_envelope_ratio_below_half": odd_ratio < Q(1, 2),
    "tail_relative_prefactor_below_100": relative_prefactor < 100,
    "complete_tail_relative_bound_below_half": relative_bound < Q(1, 2),
}
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "status": "PASS" if not failures else "FAIL",
    "scope": "EXACT_RATIONAL_CHECKS_SUPPORTING_ANALYTIC_PROOF",
    "analytic_proof": "lemmas/L599-real-zero-reflected-majorant-countermodel.md",
    "limitations": "Does not mechanically verify Fourier inversion, periodization, convergence or analytic inequalities; their full proof is in L599. No Xi or RH inference.",
    "gaussian_derivative_polynomials": [serial(p) for p in gd],
    "inverse_kernel_polynomial": serial(kernel),
    "spectral_polynomial_at_2x": serial(spectral),
    "fixed_pair": {"h": "pi/2", "r": "pi/4"},
    "negative_main_inside_2_over_pi": "-(4736/3)*exp(-36)",
    "complete_tail_absolute_upper_bound_inside_2_over_pi": "156250*exp(-100)",
    "odd_envelope_ratio_rational_upper_bound": str(odd_ratio),
    "tail_relative_prefactor": str(relative_prefactor),
    "tail_relative_rational_upper_bound": str(relative_bound),
    "required_relative_threshold": "1/2",
    "strict_negative_upper_bound": "-(4736/(3*pi))*exp(-36)",
    "checks": checks,
    "failures": failures,
}
dest = Path(__file__).with_name("fixed-pair-certificate.json")
dest.write_text(json.dumps(certificate, indent=2) + "\n")
print("Result:", certificate["status"], "(exact algebra; analytic proof in L599)")
print("Actual relative-tail upper bound:", relative_bound, "; required: < 1/2")
print("Failures:", failures)
print("Certificate:", dest)
raise SystemExit(bool(failures))
