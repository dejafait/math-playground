#!/usr/bin/env python3
"""Exact algebra/scalar certificate for C034e; analytic argument is in the lemma."""
import json
from fractions import Fraction
from math import comb
from pathlib import Path


def add(p, q):
    out = [0] * max(len(p), len(q))
    for i, a in enumerate(p):
        out[i] += a
    for i, a in enumerate(q):
        out[i] += a
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def scale(p, c):
    return [c*a for a in p]


def sub(p, q):
    return add(p, scale(q, -1))


def diff(p):
    return [i*p[i] for i in range(1, len(p))] or [0]


def power(p, n):
    out = [1]
    for _ in range(n):
        out = mul(out, p)
    return out


def product(*polys):
    out = [1]
    for p in polys:
        out = mul(out, p)
    return out


def shift(p):
    return [sum(p[i]*comb(i, j) for i in range(j, len(p)))
            for j in range(len(p))]


def numerator_matrix(a1, a2, b1, b2):
    def coefficient(p, i):
        return p[i] if i < len(p) else 0
    n = max(map(len, (a1, a2, b1, b2)))
    return [[coefficient(a2, i)*coefficient(b1, j)
             + coefficient(b1, i)*coefficient(a2, j)
             - coefficient(a1, i)*coefficient(b2, j)
             - coefficient(b2, i)*coefficient(a1, j)
             for j in range(n)] for i in range(n)]


t = [0, 1]
a1 = product([1, 3], t, power([1, 1], 2), power([2, 1], 4))
a2 = product([2, 3], t, power([2, 1], 2), power([1, 1], 4))
b1 = product([1, 4, 5, 10], power([2, 1], 4))
b2 = product([8, 16, 10, 10], power([1, 1], 4))
raw = numerator_matrix(a1, a2, b1, b2)
shifted = numerator_matrix(*map(shift, (a1, a2, b1, b2)))
negative_raw = [[i, j, a] for i, row in enumerate(raw)
                for j, a in enumerate(row) if a < 0]
negative_shifted = [[i, j, a] for i, row in enumerate(shifted)
                    for j, a in enumerate(row) if a < 0]
H = product(power(t, 2), power([1, 1], 4), power([2, 1], 4))
identity_differences = {}
for j, a, b in ((1, a1, b1), (2, a2, b2)):
    # Start from q_j(t)=4j(3t+j)/(t(t+j)^2), differentiate by the
    # quotient rule, and use d_z^2=2 d_t+4t d_t^2, t=z^2.
    n = scale([j, 3], 4*j)
    d = product(t, power([j, 1], 2))
    r = sub(mul(diff(n), d), mul(n, diff(d)))
    second_num = add(scale(mul(r, d), 2),
                     scale(mul(t, sub(mul(diff(r), d),
                                      scale(mul(r, diff(d)), 2))), 4))
    second_den = power(d, 3)
    Nj = [j**3, 4*j**2, 5*j, 10]
    expected_second_den = product(power(t, 2), power([j, 1], 4))
    identity_differences[f'Q{j}_second_formula'] = sub(
        mul(second_num, expected_second_den),
        mul(scale(Nj, 24*j), second_den))
    identity_differences[f'Q{j}_cleared'] = sub(mul(n, H), scale(mul(a, d), 4*j))
    identity_differences[f'Q{j}_second_cleared'] = sub(
        mul(second_num, H), scale(mul(b, second_den), 24*j))

# Second construction: translate the full raw bivariate matrix by
# the binomial theorem, independently of translating its four factors.
binomial_shift = [[sum(raw[i][j]*comb(i, k)*comb(j, ell)
                       for i in range(k, 9) for j in range(ell, 9))
                   for ell in range(9)] for k in range(9)]
shift_difference = [[shifted[i][j]-binomial_shift[i][j]
                     for j in range(9)] for i in range(9)]
angle = Fraction(52, 671)
v = Fraction(31, 20)
cos_lower = 1-v**2/2+v**4/24-v**6/720
block_margin = 2*105*Fraction(7, 8)-100
bounds = {
    "Re_T_min": str(Fraction(671, 4)),
    "tan_theta_max": str(angle),
    "shift_argument_scale_min": str(Fraction(671, 683)),
    "shift_argument_scale_used": "4/5",
    "all_term_angle_upper": str(20*angle),
    "all_term_angle_threshold": str(v),
    "cosine_lower_at_threshold": str(cos_lower),
    "exceptional_block_angle_upper": str(6*angle),
    "exceptional_block_angle_threshold": "1/2",
    "exceptional_block_cosine_lower": "7/8",
    "block_margin": str(block_margin),
    "kernel_margin": str(96*block_margin),
}
checks = {name: all(a == 0 for a in p) for name, p in identity_differences.items()}
checks.update({
    "independent_binomial_shift": all(a == 0 for row in shift_difference for a in row),
    "symmetric_shifted_matrix": shifted == list(map(list, zip(*shifted))),
    "only_negative_coefficient": negative_shifted == [[7, 7, -100]],
    "exceptional_positive_pair": shifted[8][6] == shifted[6][8] == 105,
    "strictly_positive_constant": shifted[0][0] == 508032,
    "degree_at_most_eight_each": len(shifted) == 9 and all(len(row) == 9 for row in shifted),
    "shift_angle_scale": Fraction(671, 683) > Fraction(4, 5),
    "all_term_angle": 20*angle < v < 2,
    "cosine_polynomial_decreasing": v**2 < 6,
    "positive_cosine_lower": cos_lower > 0,
    "exceptional_block_angle": 6*angle < Fraction(1, 2),
    "positive_block_margin": block_margin == Fraction(335, 4) > 0,
    "kernel_margin": 96*block_margin == 8040,
    "real_corner_normalization": Fraction(96*shifted[0][0], 1296**2) == Fraction(784, 27),
})
certificate = {
    "scope": "Exact rational complex-strip sign target only; no contour or C034c(20).",
    "identity": "-K(z,w)=96 P(z^2,w^2)/(H(z^2)H(w^2)); H(t)=t^2(t+1)^4(t+2)^4",
    "coefficient_order": "matrix[i][j] is the coefficient of t^i u^j; shifted substitutes t=T+1,u=U+1",
    "factors": {"a1": a1, "a2": a2, "b1": b1, "b2": b2},
    "raw_coefficients": raw,
    "shifted_coefficients": shifted,
    "negative_raw": negative_raw,
    "negative_shifted": negative_shifted,
    "identity_difference_numerators": identity_differences,
    "independent_shift_difference": shift_difference,
    "exact_bounds": bounds,
    "checks": checks,
    "algebra_and_scalar_checks_pass": all(checks.values()),
    "analytic_proof": "lemmas/C034e-complex-strip-rational-kernel-sign.md; separate audit pending",
    "actual_bound": "Re K < -8040 |z^2-1|^7 |w^2-1|^7 / (|H(z^2)| |H(w^2)|) < 0, via the lemma's domain/argument proof",
    "required_bound": "Re K(z,w)<0 for Re z,Re w>=13 and |Im z|,|Im w|<=1/2",
    "remaining_threshold": "C034c(20) and the contour/cutoff/origin estimates are NOT certified",
    "failed_simple_tests": {"unshifted_all_nonnegative": False,
                            "shifted_all_nonnegative": False},
    "failures": [name for name, ok in checks.items() if not ok],
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate, indent=2)+'\n')
print(f"Raw negative coefficients: {len(negative_raw)}; shifted: {len(negative_shifted)}")
print(f"Shifted constant: {shifted[0][0]}; matrix size: {len(shifted)}x{len(shifted[0])}")
print(f"Actual: {certificate['actual_bound']}; required: {certificate['required_bound']}")
print(f"Exact algebra/scalar checks: {sum(checks.values())}/{len(checks)}; failures: {certificate['failures']}")
print(certificate['remaining_threshold'])
print(f"Certificate: {out.relative_to(Path.cwd())}")
if certificate['failures']:
    raise SystemExit(1)
