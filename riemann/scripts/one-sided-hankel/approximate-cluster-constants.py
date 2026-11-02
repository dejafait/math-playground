"""Exact arithmetic witnesses for L655; not a proof of analytic claims."""

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


n0 = 8192
sigma2 = F(137, 5000)
check("upper product logarithm coefficient", F(22, 3), "<", F(8))
check("lower product logarithm coefficient", F(44, 7), "<", F(8))
check("adaptive radius ceiling", F(1, 24), "<", F(1, 16))
check("minimum Taylor order", F(n0, 512), ">=", F(16))
check("ceiling degree density at onset", F(1, 512) + F(1, n0),
      "<=", F(17, 8192))
check("pole radius / Taylor circle", F(512, 2048), "<=", F(1, 4))
check("relative error logarithm witness", F(112, 81), ">", F(11, 8))
check("relative error exponential witness", F(19, 3), ">", F(16, 3))
check("logarithm of norm base witness", F(2**21), ">", F(21 * 3**10))
check("norm exponent", F(187, 8192), "<", F(3, 128))
check("original diagonal prefactor", F(18) * sigma2 / F(15, 2),
      ">", F(1, 16))
check("polynomial cost absorption at onset", F(n0**3, 384 * 128**4),
      ">=", F(1))
check("correction coefficient squared", F(21), "<", F(2304) * sigma2)
check("correction at onset", F(393216, n0**2), "<", F(1, 2))

certificate = {
    "lemma": "L655",
    "scope": "Exact scalar witnesses only; analytic argument is in the lemma.",
    "required_squared_rate": "1/16",
    "proved_subfamily": "n>=8192; every |a-x|<=1/16384; original mass M<=n/3",
    "checks": checks,
    "failures": [c["name"] for c in checks if not c["passed"]],
}
path = Path(__file__).with_name("approximate-cluster-constants.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"{len(checks)} exact checks; failures: {certificate['failures']}")
print("Squared rate: actual 1/16; required 1/16 on the stated subfamily.")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(certificate["failures"]))
