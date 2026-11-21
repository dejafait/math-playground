"""Exact scalar checks for C488c; not an analytic theorem verifier."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json


checks = []


def less(name, actual, required):
    actual, required = F(actual), F(required)
    checks.append({"name": name, "actual": str(actual),
                   "required_strict_upper_bound": str(required),
                   "passed": actual < required})


def exp_lower(x, degree):
    return sum((x ** k / factorial(k) for k in range(degree + 1)), F(0))


less("b squared exceeds 48 squared using pi<22/7", 48 ** 2, F(29399, 2) * F(7, 44))
less("a/b at most 1001/1000", 1 + F(1, 184320), F(1001, 1000) ** 2)
less("a/b power below 3/2", F(1001, 1000) ** 3, F(3, 2))
less("log14000<10 from e>8/3", 14000, F(8, 3) ** 10)
less("log2<7/10 by Taylor lower sum", 2, exp_lower(F(7, 10), 3))
less("log9<11/5 by Taylor lower sum", 9, exp_lower(F(11, 5), 10))
less("eta plus pi/4 below 1", F(3, 13997) + F(11, 14), 1)
less("first sum n>=2 below 2/3", sum((F(1, n*n) for n in range(2, 6)), F(1, 5)), F(2, 3))
less("h bound", F(33, 10 * 13997), F(1, 1000))
less("gamma exponential below 2", 1 / (1-F(4, 1000)), 2)
less("reflected heat exponent", F(30, 20 * 13997), F(1, 1000))
less("r error exponent", F(9, 4 * 13996), F(1, 6000))
less("r relative error", F(1, 5999), F(1, 1000))
less("total r errors", (F(5, 3) + F(1, 8))/1000, F(1, 500))
less("positive remainder coefficient", F(121, 700), F(1, 5))
less("negative envelope exponential", F(461, 400), F(6, 5))
less("exp(6/5) envelope from e<3", 3 / (1-F(1, 5)), 4)
less("negative convex envelope at k=1", F(9, 40), F(1, 4))

q, t, sigma = F(1, 10000), F(1, 5), F(5, 2)
d0 = 1-t*q
less("Gaussian first square root squared", 1/d0, F(1001, 1000)**2)
less("Gaussian first exponent", q*sigma*sigma/d0, F(1, 1000))
less("Gaussian shifted exponent", q*F(68, 25)**2/d0, F(1, 1000))
less("Gaussian first expectation", F(1001, 999), 2)
less("Gaussian tilted expectation divided by243", F(1001, 999)*F(500, 379), 2)
d = q + F(1, 2)
less("Gaussian last square root squared", 1/(1-t*d), F(10, 9)**2)
less("Gaussian last exponent", d*sigma*sigma/(1-t*d), F(7, 2))
less("remainder outside exponent", F(1, 32)+q, F(1, 30))
less("remainder Gaussian bracket", 1 + F(486, 4*47) + F(16, 48)*90, 34)
less("remainder bound36", 34*F(30, 29), 36)
less("remainder bound40", 36, 40)
less("M0 horizontal normalization exponent", F(5, 2*14000**2), F(1, 1000))
less("M0 normalization exponential below2", F(1000, 999), 2)
total = F(2, 3) + F(1, 8) + F(1, 500) + F(5, 72)
less("total comparison", total, F(9, 10))
less("required C488b comparison", F(9, 10), F(99, 100))

failures = [row["name"] for row in checks if not row["passed"]]
result = {
    "lemma": "C488c", "kind": "exact rational scalar certificate",
    "scope": "Scalar comparisons only; analytic reductions and cited theorems require proof audit.",
    "checks": checks, "failures": failures,
    "summary": {"passed": len(checks)-len(failures), "total_checks": len(checks),
                "normalized_error_upper_bound": str(total),
                "claimed_strict_threshold": "9/10", "required_threshold": "99/100",
                "uniform_domain": "x>=29399, 3<=y<=4, 0<t<=1/5; t=0 by analytic limit"},
}
output = Path(__file__).with_name("local-count-off-axis-2114.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(f"Scalar checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}")
print(f"Normalized error <= {total} < 9/10 < required 99/100")
print(f"Certificate: {output.as_posix()}")
if failures:
    raise SystemExit(1)
