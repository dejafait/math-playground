#!/usr/bin/env python3
"""Exact constants for L677; does not audit its analytic proof."""
from fractions import Fraction as F
from pathlib import Path
import json


def main():
    checks = []

    def check(name, actual, relation, required):
        passed = actual == required if relation == "=" else actual > required
        checks.append({"name": name, "actual": str(actual),
                       "relation": relation, "required": str(required),
                       "passed": passed})

    t = F(9, 25)
    rho2, sigma2 = 1 / (1 + t*t), t*t / (1 + t*t)
    check("segment endpoint y", F(5, 4)*t, "=", F(9, 20))
    check("rho squared", rho2, "=", F(625, 706))
    check("sigma squared", sigma2, "=", F(81, 706))
    check("squared sine cosine sum", rho2 + sigma2, "=", F(1))
    check("cos theta0", 1-2*sigma2, "=", F(272, 353))
    check("s rho exceeds one, squared", F(11, 10)**2*rho2, ">", F(1))
    kappa2 = F(23, 22)**2 / (F(11, 10)**2*rho2)
    check("kappa squared", kappa2, "=", F(373474, 366025))
    check("kappa squared exceeds one", kappa2, ">", F(1))
    alpha = F(9, 11)
    check("prescribed zero under circle map", (1+alpha)/2, "=", F(10, 11))
    kernel_min, kernel_max = (1-alpha)/(1+alpha), (1+alpha)/(1-alpha)
    check("kernel minimum", kernel_min, "=", F(1, 10))
    check("kernel maximum", kernel_max, "=", F(10))
    prefactor = t*kernel_min/kernel_max
    check("norm lower-bound prefactor", prefactor, "=", F(9, 2500))
    rate_lower = (kappa2-1)/(kappa2+1)
    check("logarithm series variable", rate_lower, "=", F(7449, 739499))
    check("rate lower bound exceeds required rate", rate_lower, ">", F(1, 100))
    margin = rate_lower-F(1, 100)
    check("strict rate margin", margin, "=", F(5401, 73949900))
    failures = [row["name"] for row in checks if not row["passed"]]
    certificate = {
        "result": "PASS" if not failures else "FAIL",
        "scope": "Exact constants only; this certificate does not establish L677's analytic inequalities or its L675 input. See L677 Section 7 for the separate analytic audit.",
        "checks": checks,
        "failures": failures,
        "cost_bound": {
            "norm_lower_bound": "9*kappa^(n-1)/(2500*(2*n+3))",
            "allowed_n": "n=12q+3, integer q>=1",
            "kappa_squared": str(kappa2),
            "proved_rate_strict_lower_bound": str(rate_lower),
            "required_rate": "1/100",
            "strict_margin": str(margin),
            "prefactor": str(prefactor),
            "uniform_consequence": "Exceeds exp(n/100)*n^C eventually for every fixed real C, under all L677 hypotheses."
        },
        "limitations": ["Constants do not verify the all-preimage coefficient bound",
                        "Constants do not verify the positive-arc mass or Poisson argument",
                        "Nonpolynomial and differently constrained actions remain open",
                        "No positive-cone, H, support, Xi or RH conclusion"]
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"{certificate['result']}: {len(checks)} exact constant checks; failures={failures}")
    print(f"Proved rate > {rate_lower}; required <= 1/100; strict margin={margin}")
    print("Norm lower bound: 9*kappa^(n-1)/(2500*(2*n+3))")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
