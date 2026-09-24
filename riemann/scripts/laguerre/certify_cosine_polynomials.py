"""Certify the remaining Laguerre levels on |a| <= 10 using L310 moments.

The global cosine minorants and Bernstein conversion are proved in L311.
Arithmetic retains L037's contracts. This is a compact result, not RH.
"""

import hashlib
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "hankel"))
from certify_hankel import I, PRECISION, self_check  # noqa: E402

SOURCE = "scripts/laguerre/variance-cutoff-certificate.json"
MARGIN = Fraction(1, 400)
ORDER_BANDS = ((3, 11), (6, 9), (11, 7), (21, 5), (47, 3), (63, 1))


def coefficient(n, j, degree):
    """Coefficient of u^degree v^(2n+2j-degree) in the even product."""
    return sum((-1)**b * comb(2*j, b) * comb(2*n, degree-b)
               for b in range(max(0, degree-2*n), min(degree, 2*j)+1))


def moment_sum(n, j, moments):
    """Enclose one quarter of the full-plane weighted integral H_(n,j)."""
    degree = 2*(n+j)
    total = I(0)
    # Odd moments vanish. Combine equal swapped terms using exact integers.
    for power in range(0, degree//2+1, 2):
        weight = coefficient(n, j, power)
        if 2*power != degree:
            weight *= 2
        total = total + weight * moments[power] * moments[degree-power]
    return total


def certify():
    source_bytes = (ROOT / SOURCE).read_bytes()
    source = json.loads(source_bytes)
    if (source["arithmetic_contract"] != "L037"
            or source["maximum_moment_degree"] != 130
            or not source["variance_threshold_certified"]):
        raise ValueError("Unexpected source moment certificate")
    moments = {int(k): I(v["lower"], v["upper"])
               for k, v in source["half_line_moments"].items()}
    if set(moments) != set(range(0, 131, 2)) or any(v.lo <= 0 for v in moments.values()):
        raise ValueError("Missing or nonpositive moment enclosure")

    rows = []
    global_minimum = None
    minimum_location = None
    for n in range(1, 64):
        order = next(m for upper, m in ORDER_BANDS if n <= upper)
        assert order % 2 == 1 and 2*(n+order) <= 130
        sums = [moment_sum(n, j, moments) for j in range(order+1)]
        if any(value.lo <= 0 for value in sums):
            raise ArithmeticError("A positive weighted moment was not resolved")
        z = sums[0]
        # q = a^2/100 lies in [0,1]. The constant coefficient is exactly one.
        powers = [I(1)] + [(-1)**j * 100**j * sums[j] / (factorial(2*j) * z)
                          for j in range(1, order+1)]
        bernstein = [
            sum((powers[j] * I.rational(Fraction(comb(i, j), comb(order, j)))
                 for j in range(i+1)), I(0))
            for i in range(order+1)
        ]
        for i, value in enumerate(bernstein):
            if Fraction(value.lo) <= MARGIN:
                raise ArithmeticError(f"Margin failed at n={n}, coefficient={i}")
            if global_minimum is None or value.lo < global_minimum:
                global_minimum = value.lo
                minimum_location = {"level": n, "bernstein_index": i}
        rows.append({
            "level": n,
            "cosine_taylor_index": order,
            "cosine_polynomial_degree": 2*order,
            "maximum_moment_degree": 2*(n+order),
            "weighted_moment_sums": [v.data() for v in sums],
            "power_coefficients_in_q": [v.data() for v in powers],
            "bernstein_coefficients": [v.data() for v in bernstein],
            "minimum_bernstein_lower_endpoint": str(min(v.lo for v in bernstein)),
        })
    assert Fraction(global_minimum) > MARGIN
    return {
        "scope": "levels 1 through 63 on every |a| <= 10; L310 covers n >= 64; not RH",
        "arithmetic_contract": "L037",
        "precision": PRECISION,
        "source_moments": SOURCE,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "q_interval": ["0", "1"],
        "q_definition": "a^2/100",
        "strict_normalized_margin": str(MARGIN),
        "minimum_bernstein_lower_endpoint": str(global_minimum),
        "minimum_location": minimum_location,
        "levels": rows,
        "finite_band_certified": True,
    }


if __name__ == "__main__":
    self_check()
    print(json.dumps(certify(), indent=2))
