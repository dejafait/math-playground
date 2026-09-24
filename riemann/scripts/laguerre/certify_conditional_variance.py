"""Finite curvature and moment bounds, under L037's arithmetic contracts.

The compact calculation encloses W'''' for v in [3, 4]. The analytic
tail and conditional ordering arguments are in L309. This is not RH.
"""

import json
from fractions import Fraction
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
from certify_hankel import I, PRECISION  # noqa: E402


def derivative_polynomials():
    # (2x d/dx)^j [(2x^2 - 3x) exp(-x)] = P_j(x) exp(-x).
    polynomials = [[0, -3, 2]]
    for _ in range(4):
        old = polynomials[-1]
        new = [0] * (len(old) + 1)
        for degree, coefficient in enumerate(old):
            new[degree] += 2 * degree * coefficient
            new[degree + 1] -= 2 * coefficient
        polynomials.append(new)
    return polynomials


def evaluate(coefficients, x):
    value = I(0)
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def tail_bounds(polynomials):
    bounds = []
    for j, polynomial in enumerate(polynomials):
        degree = j + 2
        # For x >= 27, |P_j(x)| <= C_j x^(j+2).
        coefficient_bound = sum(
            (Fraction(abs(c), 27 ** (degree - i))
             for i, c in enumerate(polynomial)), Fraction(0)
        )
        # For m >= 3, the successive majorant ratio is below 1/2.
        ratio = Fraction(4, 3) ** (2*j + 4) / 20**7
        if ratio >= Fraction(1, 2):
            raise ArithmeticError("Tail geometric ratio is too large")
        bounds.append(2 * coefficient_bound * 3**(3*j + 6) / 20**8)
    return bounds


def certify(panels=1024):
    polynomials = derivative_polynomials()
    tails = tail_bounds(polynomials)
    lower_bounds, upper_bounds = [], []
    for panel in range(panels):
        left = I.rational(Fraction(3*panels + panel, panels))
        right = I.rational(Fraction(3*panels + panel + 1, panels))
        v = I(left.lo, right.hi)
        exponential = (-3*v).exp()
        derivatives = []
        for polynomial, tail in zip(polynomials, tails):
            head = evaluate(polynomial, v) + evaluate(polynomial, 4*v) * exponential
            radius = I.rational(tail).hi
            derivatives.append(head + I(radius.copy_negate(), radius))
        if derivatives[0].lo <= 0:
            raise ArithmeticError("Kernel denominator is not positive")
        ratios = [value / derivatives[0] for value in derivatives[1:]]
        r1, r2, r3, r4 = ratios
        curvature_derivative = (-r4 + 4*r3*r1 + 3*r2**2
                                - 12*r2*r1**2 + 6*r1**4)
        if curvature_derivative.lo <= 100:
            raise ArithmeticError(f"Fourth logarithmic derivative failed in panel {panel}")
        lower_bounds.append(curvature_derivative.lo)
        upper_bounds.append(curvature_derivative.hi)

    moment_path = ROOT / "scripts" / "hankel" / "hankel-certificate.json"
    source = json.loads(moment_path.read_text())
    moments = {j: I(source["moments"][str(j)]["lower"],
                    source["moments"][str(j)]["upper"])
               for j in (0, 2, 4)}
    # The stored moments are half-line moments. These ratios are unchanged.
    variance = (moments[4] / moments[2] - moments[2] / moments[0]) / 4
    if not (Fraction(2069, 100000) < Fraction(variance.lo)
            <= Fraction(variance.hi) < Fraction(207, 10000)
            < Fraction(50, 2401)):
        raise ArithmeticError("Variance enclosure missed the stated threshold")
    return {
        "scope": "compact W'''' certificate and V_1 bound; not RH",
        "arithmetic_contract": "L037",
        "precision": PRECISION,
        "v_interval": [3, 4],
        "panels": panels,
        "explicit_theta_terms": 2,
        "derivative_polynomials": polynomials,
        "normalized_derivative_tail_bounds": [str(tail) for tail in tails],
        "fourth_logarithmic_derivative": {
            "lower": str(min(lower_bounds)),
            "upper": str(max(upper_bounds)),
        },
        "moment_source": str(moment_path.relative_to(ROOT)),
        "V_1": variance.data(),
        "target_height": "49/10",
        "required_variance_upper_bound": "50/2401",
        "compact_curvature_certified": True,
        "variance_threshold_certified": True,
    }


if __name__ == "__main__":
    print(json.dumps(certify(), indent=2))
