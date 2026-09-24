"""Check the saved band certificate's final algebra with exact Fractions.

This separately pairs the Laguerre sum and uses exact interval squares.
It checks source hashes, height coverage, positive denominators, every
sign and the recorded minima. It does not independently reprove the
quadrature bounds or verify the Decimal implementation.
"""

from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERTIFICATE = ROOT / "scripts/laguerre/finite-witness-band-certificate.json"


def interval(data):
    a, b = Q(data["lower"]), Q(data["upper"])
    assert a <= b
    return a, b


def plus(a, b):
    return a[0] + b[0], a[1] + b[1]


def times(a, b):
    values = [x*y for x in a for y in b]
    return min(values), max(values)


def scale(a, c):
    values = [x*c for x in a]
    return min(values), max(values)


def square(a):
    low, high = a
    return (Q(0) if low <= 0 <= high else min(low*low, high*high),
            max(low*low, high*high))


def main():
    certificate_bytes = CERTIFICATE.read_bytes()
    certificate = json.loads(certificate_bytes)
    assert certificate["arithmetic_contract"] == "L037"
    source_bytes = (ROOT / certificate["source_moments"]).read_bytes()
    assert hashlib.sha256(source_bytes).hexdigest() == certificate["source_sha256"]
    source = json.loads(source_bytes)
    moments = {int(j): interval(v) for j, v in source["half_line_moments"].items()}
    levels = range(3, 17)
    denominators = {}
    for n in levels:
        mass = (Q(0), Q(0))
        for j in range(0, 2*n+1, 2):
            mass = plus(mass, scale(times(moments[j], moments[2*n-j]), comb(2*n, j)))
        assert mass[0] > 0
        stored = interval(certificate["mass_denominators"][str(n)])
        assert stored[0] <= mass[0] <= mass[1] <= stored[1]
        denominators[n] = mass
    minimums, exact_minimums = {}, {}
    previous = Q(10)
    assert len(certificate["cells"]) == certificate["height_cells"] == 512
    for index, row in enumerate(certificate["cells"]):
        left, right = map(Q, row["a_interval"])
        assert left == previous and left < right
        assert left == Q(10) + Q(10*index, 512)
        previous = right
        derivatives = [interval(v) for v in row["transform_derivatives"]]
        assert len(derivatives) == 33
        for n in levels:
            value = scale(square(derivatives[n]), comb(2*n, n))
            for j in range(n):
                coefficient = 2 * (-1)**(n+j) * comb(2*n, j)
                value = plus(value, scale(times(derivatives[j], derivatives[2*n-j]), coefficient))
            d = denominators[n]
            ratio = times(value, (1/d[1], 1/d[0]))
            saved = interval(row["normalized_Laguerre_coefficients"][str(n)])
            assert saved[0] <= ratio[0] <= ratio[1] <= saved[1]
            assert saved[0] > Q(1, 10**6)
            assert ratio[0] > Q(1, 10**6)
            if n not in minimums or saved[0] < minimums[n][0]:
                minimums[n] = saved[0], index
            if n not in exact_minimums or ratio[0] < exact_minimums[n]:
                exact_minimums[n] = ratio[0]
    assert previous == 20
    for n in levels:
        saved_min = certificate["minimum_lower_endpoints"][str(n)]
        assert minimums[n] == (Q(saved_min["value"]), saved_min["cell"])
    earlier = json.loads((ROOT / "scripts/laguerre/averaged-ordering-certificate.json").read_bytes())
    for new, old in zip(certificate["transform_derivatives_at_center"],
                        earlier["transform_derivatives_at_center"]):
        new, old = interval(new), interval(old)
        assert max(new[0], old[0]) <= min(new[1], old[1])
    print(json.dumps({
        "certificate_sha256": hashlib.sha256(certificate_bytes).hexdigest(),
        "checks_passed": True, "sign_enclosures_checked": 512 * 14,
        "height_band": [10, 20], "levels": [3, 16],
        "strict_normalized_margin": "1/1000000",
        "method": "exact rational paired sums, interval squares, source hash and coverage",
        "minimum_exact_rational_lower_bound": str(min(exact_minimums.values())),
        "qualification": "does not independently verify quadrature or Decimal implementation",
    }, indent=2))


if __name__ == "__main__":
    main()
