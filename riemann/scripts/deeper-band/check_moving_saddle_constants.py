#!/usr/bin/env python3
"""Exact fixed-constant checks; not a certificate of the analytic argument."""

import json
from fractions import Fraction as F
from pathlib import Path


def rational(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def main():
    d = F(1, 4096)
    r0, r1, r2, r3 = (F(k, 256) for k in (255, 282, 284, 286))
    checks = []

    def greater(name, actual, required):
        checks.append({"name": name, "actual": rational(actual),
                       "required_strict_lower_bound": rational(required),
                       "passed": actual > required})

    greater("inner Euler real-part margin", 2 - r0, F(1))
    greater("R1-R0", r1 - r0, F(0))
    greater("R2-R1", r2 - r1, F(0))
    greater("R3-R2", r3 - r2, F(0))
    greater("outer zero-free real-part margin", 2 - r3, F(7, 8))
    # theta < 15/16 iff R1^16 < R0*R2^15.
    power_left, power_right = 282**16, 255 * 284**15
    greater("interpolation power margin", F(power_right - power_left), F(0))
    greater("eight-d saddle disk reserve", r1 - (F(35, 32) + 8*d), F(0))
    greater("saddle disk zero-free clearance", F(29, 32) - 8*d, F(7, 8))
    greater("real x interval lower bound", F(13, 32) - d, F(2, 5))
    greater("real x interval upper reserve", F(1, 2) - (F(7, 16) + 2*d), F(0))
    greater("all-height sigma lower bound", F(29, 32) - d, F(9, 10))
    greater("all-height pole clearance", F(1, 16) - 2*d, F(1, 32))
    greater("middle-range logarithm reserve", r1 - (F(35, 32) + d), F(0))
    greater("Gaussian tail rate reserve", F(13, 32) * d*d, d*d/4)
    greater("curvature lower reserve before perturbation", F(13, 4), F(2))
    greater("curvature upper reserve before perturbation", F(8), F(25, 4))
    greater("far-tail quadratic rate", F(13, 8), F(1))
    failures = [item["name"] for item in checks if not item["passed"]]
    certificate = {
        "scope": "Exact constants only; no analytic theorem or external premise verified.",
        "parameters": {"d": rational(d), "p": rational(F(15, 16)),
                       "kappa": rational(d*d/4)},
        "interpolation": {"left": power_left, "right": power_right,
                          "required": "left < right; equivalent to theta < 15/16"},
        "checks": checks,
        "failures": failures,
        "passed": not failures,
    }
    path = Path(__file__).with_name("moving-saddle-constants-certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Exact constant checks: {len(checks) - len(failures)}/{len(checks)} passed")
    print(f"Interpolation: {power_left} < {power_right}; required theta < 15/16")
    print(f"Saddle disk reserve: {r1 - (F(35, 32) + 8*d)}; required > 0")
    print(f"Failures: {failures}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
