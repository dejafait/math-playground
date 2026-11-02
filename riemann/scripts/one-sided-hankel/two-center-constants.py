"""Exact scalar witnesses for L656, not verification of its analytic proof."""

from fractions import Fraction as F
import json
from pathlib import Path


checks = []


def check(name, actual, relation, required):
    passed = {"<": actual < required, ">": actual > required,
              "<=": actual <= required, ">=": actual >= required}[relation]
    checks.append({"name": name, "actual": str(actual),
                   "relation": relation, "required": str(required),
                   "passed": passed})


n0 = 32768
m0 = 16
sigma2 = F(137, 5000)
rmin = F(1, 2**14)
h = F(1, 2**34)
check("general contour radius ceiling", F(1, 48), "<", F(1, 16))
check("center ordinate squared", F(12029, 40000), "<", F(1))
check("kernel factor bound", F(33, 16), "<", F(11, 4))
check("contour analytic clearance", F(273, 200) + F(1, 16), "<", F(3, 2))
check("product logarithm coefficient", F(22, 3), "<", F(8))
check("minimum chosen order", F(n0, 2048), ">=", F(m0))
check("ceiling density", F(1, 2048) + F(1, n0), "<=", F(17, 32768))
check("pole radius over contour radius", h/rmin, "<=", F(1, 2**20))
check("Cauchy prefactor", 2/(1-h/rmin), "<", F(3))
check("two-center numerator ratio", 3*h/rmin**2, "<=", F(3, 64))
check("error exponential base", F(9, 64), "<", F(1, 4))
check("weighted error at minimum order", F(6144*m0, 4**m0), "<", F(1, 4))
check("norm-base exponential witness", F(8, 3)**11, ">", F(45056))
check("norm exponent", F(425, 32768), "<", F(1, 64))
check("original diagonal prefactor squared", 108*sigma2, ">", F(11, 8)**2)
check("square-root cost absorption", F(n0**3, 2**32), ">=", F(1))
check("correction coefficient squared", F(21), "<", 2304*sigma2)
check("correction at onset", F(393216, n0**2), "<", F(1, 2))
check("small-mass density for L654", F(17, 16384), "<", F(1, 384))

certificate = {
    "lemma": "L656",
    "scope": "Exact scalar witnesses only; the canonical lemma proves the analytic claims.",
    "required_squared_rate": "1/16",
    "actual_squared_rate": "1/16 on the stated two-cloud subfamily only",
    "squared_prefactor": "1/4",
    "proved_subfamily": "n>=32768; two centers in Z; distance to their union <=2^(-34); original M<=n/3",
    "checks": checks,
    "failures": [c["name"] for c in checks if not c["passed"]],
}
path = Path(__file__).with_name("two-center-constants.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{len(checks)} exact checks; failures: {certificate['failures']}")
print("Squared rate: actual 1/16; required 1/16 on the two-cloud subfamily.")
print("Full norm exponent: 425/32768 < 1/64; weighted error: 3/131072 < 1/4.")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(certificate["failures"]))

