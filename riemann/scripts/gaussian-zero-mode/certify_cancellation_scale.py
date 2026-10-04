"""Outward cancellation certificates for L359, under L037.

Reuse L358's gamma and infinite damped-series enclosures. Certify a
sufficient upper bound and independently evaluate its exact first sign.
No binary floats and no extrapolation of fixed regulators to zero.
"""

from fractions import Fraction as Q
import json

from certify_first_spectrum import (  # noqa: E402
    C, I, PI, PRECISION, QUARTER, damped_series, gamma_data,
    log_interval, sin_cos,
)


def log_positive(value):
    if value.lo <= 0:
        raise ArithmeticError("Positive logarithm required")
    if value.lo >= 1:
        return log_interval(value)
    if value.hi <= 1:
        return -log_interval(I(1) / value)
    return I(log_positive(I(value.lo)).lo, log_positive(I(value.hi)).hi)


def absolute(value):
    if value.lo >= 0:
        return value
    if value.hi <= 0:
        return -value
    return I(0, value.magnitude())


def norm_squared(value):
    return value.real**2 + value.imag**2


def norm(value):
    squared = norm_squared(value)
    if squared.lo <= 0:
        raise ArithmeticError("This certificate needs a positive norm enclosure")
    return (log_positive(squared) / 2).exp()


def upper(value):
    return I(value.hi)


def certify_case(epsilon_q, xi_q, last):
    epsilon, xi = I.rational(epsilon_q), I.rational(xi_q)
    log_gamma, psi, trigamma, gamma_error = gamma_data(xi)
    (series, first, second), tail = damped_series(epsilon, xi, last)
    log_pi = log_interval(PI)
    log_epsilon = -log_interval(I.rational(1 / epsilon_q))
    polynomial = xi**2 + QUARTER
    q = I(2) / polynomial - 4 * xi**2 / polynomial**2 - trigamma.real / 4
    omega = (psi.real - log_pi) / 2
    omega_prime = -trigamma.imag / 4
    sine, cosine = sin_cos(log_gamma.imag - xi * log_pi / 2, PI)
    rotation = C(cosine, sine)
    c, d, e = rotation * series, rotation * first, rotation * second
    velocity = first + C(0, omega) * series
    c_norm, d_norm, e_norm, v_norm = map(norm, (series, first, second, velocity))

    beta = (log_gamma.real - (log_epsilon + log_pi) / 4).exp() / 2
    alpha = log_epsilon / 2
    b = -psi.imag / 2
    b_prime = -trigamma.real / 4
    beta_sine, beta_cosine = sin_cos(alpha * xi, PI)
    y = -c.real + beta * beta_cosine
    y_first = (-(rotation * velocity).real
               + beta * (b * beta_cosine - alpha * beta_sine))
    y_second = (
        -(rotation * (second + C(0, 2 * omega) * first
                      + C(-omega**2, omega_prime) * series)).real
        + beta * ((b**2 + b_prime - alpha**2) * beta_cosine
                  - 2 * alpha * b * beta_sine)
    )
    exact_sign = y_first**2 - y * y_second - q * y**2
    base_sign = (norm_squared(velocity) - d.imag**2 - c.real * e.real
                 + omega_prime * c.real * c.imag - q * c.real**2)

    # These are positive exact Decimal bounds; evaluating them with I keeps
    # every new arithmetic operation outward rounded.
    cu, du, eu, vu = map(upper, (c_norm, d_norm, e_norm, v_norm))
    beta0 = upper(beta)
    beta1 = beta0 * (I(b.magnitude()) + I(alpha.magnitude()))
    beta2 = beta0 * ((I(b.magnitude()) + I(alpha.magnitude()))**2
                    + I(b_prime.magnitude()))
    ou, opu, qu = I(omega.magnitude()), I(omega_prime.magnitude()), I(q.magnitude())
    z_second = eu + 2 * ou * du + (opu + ou**2) * cu
    # Direct multiplication avoids the generic integer-power routine's
    # unused fourth power, which would underflow for this very small beta.
    beta_error = (2 * vu * beta1 + beta1 * beta1 + cu * beta2
                  + beta0 * z_second + beta0 * beta2
                  + qu * (2 * cu * beta0 + beta0 * beta0))
    sufficient_upper = (norm_squared(velocity) - d.imag**2 + cu * eu
                        + (opu / 2 + qu) * cu**2 + beta_error)
    if exact_sign.hi >= 0 or sufficient_upper.hi >= 0:
        raise ArithmeticError("The exact sign and sufficient upper bound must both be negative")
    difference = exact_sign - base_sign
    if max(difference.lo, beta_error.hi.copy_negate()) > min(difference.hi, beta_error.hi):
        raise ArithmeticError("Completed-square and differentiated formulas disagree")
    if exact_sign.hi > sufficient_upper.hi:
        raise ArithmeticError("Direct negative enclosure exceeds the upper certificate")
    return {
        "epsilon": str(epsilon_q), "xi": str(xi_q), "last_series_index": last,
        "log_gamma_remainder_bound": gamma_error.data(),
        "common_series_tail_bound": tail.data(),
        "omega": omega.data(), "series_modulus": c_norm.data(),
        "series_first_derivative_modulus": d_norm.data(),
        "series_second_derivative_modulus": e_norm.data(),
        "completed_velocity_modulus": v_norm.data(),
        "relative_cancellation_deviation": (v_norm / d_norm).data(),
        "rotated_imaginary_derivative_fraction": (absolute(d.imag) / d_norm).data(),
        "beta_error_bound": beta_error.data(),
        "sufficient_laguerre_upper": sufficient_upper.data(),
        "laguerre_over_A_squared": exact_sign.data(),
        "negative_certified": True,
    }


def certify():
    cases = [(Q(1, 10000), Q(2018091, 10), 360),
             (Q(1, 100000), Q(8129949, 10), 1140),
             (Q(1, 1000000), Q(769857, 10), 3600)]
    return {
        "scope": "Three fixed positive regulators; no arbitrarily-small-epsilon conclusion or RH",
        "arithmetic_contract": "L037", "precision": PRECISION,
        "cases": [certify_case(*case) for case in cases],
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
