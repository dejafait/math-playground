"""Exact rational arithmetic for L431's isolated prime-2 factor.

Run from riemann: python3 scripts/discriminant/prime_cubic_recalibration.py
The infinite-sum reduction is proved in L431; this checks its rational
arithmetic and the squared nonnegative-polynomial feasibility bound.
"""
from fractions import Fraction as F
from pathlib import Path
import json

z, y, D = F(1, 8), F(1, 8), F(31, 32)
s0 = 1 / (1-z)
s1 = z / (1-z)**2
s2 = z * (1+z) / (1-z)**3
tail = y / (1-y)
base = (s0 + (D+F(1, 2))*s1 + D*F(1, 2)*s2 + tail) / D**2
plus = (F(3, 4)*s0 + (F(3, 4)*D+F(1, 4))*s1 + D*F(1, 4)*s2 + tail) / D**2
minus = (s0 + (D+1)*s1 + D*s2 + tail) / D**2
# rho = gamma_2/beta = sqrt(2) * rho_over_sqrt2.
rho_over_sqrt2 = (plus + minus/2) / (2*base)
rho_squared = 2*rho_over_sqrt2**2
degree = next(d for d in range(1, 1000) if rho_squared < F(d, d+1)**2)
required_squared = F(degree, degree+1)**2
checks = {
    "positive_ratio": rho_over_sqrt2 > 0,
    "ratio_below_one": rho_squared < 1,
    "ratio_below_kernel_first_coefficient": rho_squared < required_squared,
}
record = {
    "arithmetic": "exact fractions; no floating point or truncation",
    "prime_two": {"base": str(base), "plus": str(plus), "minus": str(minus)},
    "ratio_over_sqrt2": str(rho_over_sqrt2),
    "ratio_squared": str(rho_squared),
    "fejer_degree": degree,
    "required_squared": str(required_squared),
    "strict_squared_margin": str(required_squared-rho_squared),
    "checks": checks,
    "failures": [name for name, passed in checks.items() if not passed],
}
path = Path(__file__).with_name("prime_cubic_recalibration_certificate.json")
path.write_text(json.dumps(record, indent=2) + "\n")
print(f"prime-2 base={base}; plus={plus}; minus={minus}")
print(f"ratio=sqrt(2)*{rho_over_sqrt2}; ratio^2={rho_squared}")
print(f"degree={degree}; required ratio^2 < {required_squared}")
print(f"strict squared margin={required_squared-rho_squared}; failures={record['failures']}")
print(f"certificate={path}")
assert not record["failures"]
