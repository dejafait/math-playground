"""Three negative regulated first-Laguerre values for L358, under L037.

No binary floats, sampled sign extrapolation, or assertion about RH.
Gamma logarithms use a finite Stirling expression with an explicit
complex remainder; its first two derivatives use Cauchy's estimate.
The infinite damped series has a common geometric tail bound.
"""

from fractions import Fraction as Q
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
sys.path.insert(0, str(ROOT / "scripts" / "laguerre"))
from certify_hankel import I, PRECISION, pi_bounds  # noqa: E402
from certify_bessel_gaps import atan_interval, log_interval, widen  # noqa: E402
from certify_conditional_cosine import sin_cos  # noqa: E402

PI = pi_bounds()
HALF = I.rational(Q(1, 2))
QUARTER = I.rational(Q(1, 4))
SHIFT = 32


class C:
    """Rectangular complex intervals, with outward real operations."""

    def __init__(self, real=0, imag=0):
        self.real, self.imag = I.lift(real), I.lift(imag)

    @staticmethod
    def lift(value):
        return value if isinstance(value, C) else C(value)

    def __add__(self, other):
        other = C.lift(other)
        return C(self.real + other.real, self.imag + other.imag)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-C.lift(other))

    def __rsub__(self, other):
        return C.lift(other) + (-self)

    def __mul__(self, other):
        other = C.lift(other)
        return C(self.real * other.real - self.imag * other.imag,
                 self.real * other.imag + self.imag * other.real)

    __rmul__ = __mul__

    def inverse(self):
        denominator = self.real**2 + self.imag**2
        return C(self.real / denominator, -self.imag / denominator)

    def __truediv__(self, other):
        return self * C.lift(other).inverse()

    def __pow__(self, degree):
        if not isinstance(degree, int) or degree < 0:
            raise ValueError("Only nonnegative integer complex powers")
        result, base = C(1), self
        while degree:
            if degree & 1:
                result = result * base
            base = base * base
            degree //= 2
        return result


def complex_log_right(z):
    if z.real.lo <= 0 or z.imag.lo <= 0:
        raise ArithmeticError("Gamma arguments must be in the first quadrant")
    return C(log_interval(z.real**2 + z.imag**2) / 2,
             atan_interval(z.imag / z.real))


def gamma_data(xi):
    """Enclose log Gamma(s), psi(s), psi_1(s), s=1/4+i*xi/2."""
    s = C(QUARTER, xi / 2)
    w = s + SHIFT
    lw = complex_log_right(w)
    inverse = w.inverse()
    log_gamma = (w - HALF) * lw - w + log_interval(2 * PI) / 2 + inverse / 12
    psi = lw - inverse / 2 - inverse**2 / 12
    trigamma = inverse + inverse**2 / 2 + inverse**3 / 6
    for j in range(SHIFT):
        current = s + j
        log_gamma -= complex_log_right(current)
        reciprocal = current.inverse()
        psi -= reciprocal
        trigamma += reciprocal**2

    # DLMF 5.11(ii), first omitted term after 1/(12*w):
    # sec(arg(w)/2)^4/(360*|w|^3) <= 1/(90*|w|^3).
    # On the radius-one disk: Re(w)>0 and |w|>=xi/2-1.
    # Cauchy gives |R'|<=r and |R''|<=2*r on its center.
    radius = I(1) / (90 * (xi / 2 - 1)**3)
    if w.real.lo <= 1 or xi.lo <= 2:
        raise ArithmeticError("Stirling disk leaves its permitted sector")
    for value, error in ((log_gamma, radius), (psi, radius),
                         (trigamma, 2 * radius)):
        value.real = widen(value.real, error)
        value.imag = widen(value.imag, error)
    return log_gamma, psi, trigamma, radius


def damped_series(epsilon, xi, last):
    totals = [C(), C(), C()]
    for n in range(1, last + 1):
        log_n = log_interval(I(n))
        coefficient = (-PI * epsilon * n*n - log_n / 2).exp()
        sine, cosine = sin_cos(-xi * log_n, PI)
        term = C(coefficient * cosine, coefficient * sine)
        totals[0] += term
        totals[1] += term * C(0, -log_n)
        totals[2] -= term * log_n**2

    # For j=0,1,2, n^(-1/2)*(log n)^j <= n^2.
    # Successive ratios of n^2*exp(-pi*epsilon*n^2) decrease with n.
    first = last + 1
    ratio = (I.rational(Q(first + 1, first))**2
             * (-PI * epsilon * (2 * first + 1)).exp())
    if ratio.hi >= 1:
        raise ArithmeticError("The series-tail geometric ratio is not below one")
    tail = first**2 * (-PI * epsilon * first**2).exp() / (1 - ratio)
    for value in totals:
        value.real = widen(value.real, tail)
        value.imag = widen(value.imag, tail)
    return totals, tail


def certify_case(epsilon_q, xi_q, last):
    epsilon, xi = I.rational(epsilon_q), I.rational(xi_q)
    log_gamma, psi, trigamma, gamma_error = gamma_data(xi)
    (series, first, second), series_tail = damped_series(epsilon, xi, last)
    log_pi = log_interval(PI)
    log_epsilon = -log_interval(I.rational(1 / epsilon_q))
    polynomial = xi**2 + QUARTER
    curvature = I(2) / polynomial - 4 * xi**2 / polynomial**2 - trigamma.real / 4
    omega = (psi.real - log_pi) / 2
    omega_prime = -trigamma.imag / 4
    phase = log_gamma.imag - xi * log_pi / 2
    sine, cosine = sin_cos(phase, PI)
    rotation = C(cosine, sine)

    # F=A*y, A=(xi^2+1/4)*|Gamma(s)|*pi^(-1/4)>0.
    # The beta term divided by A is beta*cos(alpha*xi).
    beta = (log_gamma.real - (log_epsilon + log_pi) / 4).exp() / 2
    alpha = log_epsilon / 2
    beta_log_first = -psi.imag / 2
    beta_log_second = -trigamma.real / 4
    beta_sine, beta_cosine = sin_cos(alpha * xi, PI)
    y = -(rotation * series).real + beta * beta_cosine
    y_first = (-(rotation * (first + C(0, omega) * series)).real
               + beta * (beta_log_first * beta_cosine - alpha * beta_sine))
    y_second = (
        -(rotation * (second + C(0, 2 * omega) * first
                      + C(-omega**2, omega_prime) * series)).real
        + beta * ((beta_log_first**2 + beta_log_second - alpha**2) * beta_cosine
                  - 2 * alpha * beta_log_first * beta_sine)
    )
    scaled_laguerre = y_first**2 - y * y_second - curvature * y**2
    if scaled_laguerre.hi >= 0:
        raise ArithmeticError("Negative first-Laguerre sign not certified")
    return {
        "epsilon": str(epsilon_q), "xi": str(xi_q), "last_series_index": last,
        "stirling_disk_radius": "1", "log_gamma_remainder_bound": gamma_error.data(),
        "common_series_tail_bound": series_tail.data(),
        "F_over_A": y.data(), "y_first": y_first.data(), "y_second": y_second.data(),
        "log_A_second": curvature.data(), "beta_over_A_factor": beta.data(),
        "laguerre_over_A_squared": scaled_laguerre.data(),
        "negative_certified": True,
    }


def certify():
    cases = [(Q(1, 100), Q(42679, 5), 40),
             (Q(3, 1000), Q(87587, 10), 80),
             (Q(1, 1000), Q(87029, 5), 150)]
    return {
        "scope": "Three fixed positive regulators only; not arbitrarily small epsilon or RH",
        "arithmetic_contract": "L037", "precision": PRECISION,
        "cases": [certify_case(*case) for case in cases],
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
