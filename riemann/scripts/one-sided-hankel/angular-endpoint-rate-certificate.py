"""Exact rational endpoint-rate bound; run from the active notebook."""
from fractions import Fraction as F
import json
from pathlib import Path

d, U, r = F(5, 4), F(121, 64), F(9, 20)
N, scale = 512, 10**12
rounded_sum = 0
for k in range(N):
    t = F(k, N)
    A = r*r/(d+t)**2
    B = r*r*t*t/(U+d*t)**2
    g = (A-A*A/2+A**3/3-B+B*B/2)/2
    scaled = g*scale
    rounded_sum += -(-scaled.numerator//scaled.denominator)
bound = F(rounded_sum, N*scale)
required = F(61, 2000)
failures = [] if bound < required else ["endpoint integral bound misses 61/2000"]
epsilon = F(1, 10**6)
checks = []
def check(name, actual, relation, threshold):
    passed = actual < threshold if relation == '<' else actual > threshold
    checks.append({"name": name, "actual": str(actual), "relation": relation,
                   "required": str(threshold), "passed": passed})
    if not passed:
        failures.append(name)

check("horizontal numerator lower bound", (U-1)*(d*U-r*r), '>', F(19, 10))
check("horizontal denominator upper bound",
      ((d+F(1, 2)+1)**2+r*r)*((U+d+F(1, 2))**2+r*r), '<', F(105))
check("angular single-factor logarithmic derivative", F(20, 23)+2/U, '<', F(2))
check("angular p derivative", F(20, 23)**2+1/U, '<', F(2))
check("real p after angular perturbation", F(19, 1050)-2*epsilon, '>', F(1, 100))
check("vertical connecting rate", F(35, 531)-4*epsilon, '>', F(3, 50))
check("finite-node remainder rate", F(16, 111)-F(2, 23)-4*epsilon, '>', F(11, 200))
check("endpoint rate after angular perturbation", required+4*epsilon, '<', F(31, 1000))
check("desired compact-band rate", F(31, 1000), '<', F(1, 32))
certificate = {
    "kind": "exact rational upper bound, not sampled quadrature",
    "formula": "g(t)=(A-A^2/2+A^3/3-B+B^2/2)/2; A=r^2/(d+t)^2; B=r^2*t^2/(U+d*t)^2",
    "parameters": {"d": "5/4", "U": "121/64", "r": "9/20"},
    "justification": "f(t)<=g(t); g decreasing; integral_0^1 g <= left Riemann sum. Each rational summand is rounded upward at scale.",
    "subintervals": N,
    "upward_rounding_scale": scale,
    "rounded_numerator_sum": rounded_sum,
    "upper_bound": {"numerator": bound.numerator, "denominator": bound.denominator},
    "required_upper_bound": "61/2000",
    "strict_margin": {"numerator": (required-bound).numerator, "denominator": (required-bound).denominator},
    "auxiliary_rational_checks": checks,
    "failures": failures,
    "scope": "Exact endpoint modulus rate and stated rational margins only; contour errors, phases, and angular integration require the analytic proof."
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(certificate, indent=2)+'\n')
print(f"Exact upper rate: {bound} ({float(bound):.12f}); required < {required} ({float(required):.12f})")
for item in checks:
    print(f"{item['name']}: {float(F(item['actual'])):.12f} {item['relation']} {float(F(item['required'])):.12f}; passed={item['passed']}")
print(f"Failures: {failures}; certificate: {path}")
if failures:
    raise SystemExit(1)
