#!/usr/bin/env python3
"""Exact arithmetic supporting L675; not an audit of its analytic proof."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def add(left, right):
    result = [F(0)] * max(len(left), len(right))
    for k, value in enumerate(left):
        result[k] += value
    for k, value in enumerate(right):
        result[k] += value
    return result


def multiply(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def evaluate(coefficients, at):
    return sum(value * at**k for k, value in enumerate(coefficients))


def encode(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(item) for item in value]
    return value


def main():
    checks = []

    def check(name, actual, relation, required):
        passed = actual == required if relation == "=" else actual > required
        checks.append(dict(name=name, actual=actual, relation=relation,
                           required=required, passed=passed))

    polynomial = multiply(multiply([F(0), F(1)], [F(-10), F(11)]),
                          [F(3), F(-2)])
    check("expanded cubic", polynomial, "=", list(map(F, [0, -30, 53, -22])))
    for at, required in [(F(0), F(0)), (F(1), F(1)), (F(10, 11), F(0))]:
        check(f"P({at})", evaluate(polynomial, at), "=", required)

    # Re (1+i*t)^k, with v=t^2; common denominator (1+v)^3.
    numerator = [F(0)]
    for k in range(1, 4):
        real_power = [F((-1)**j * comb(k, 2*j)) for j in range(k//2 + 1)]
        denominator_complement = [F(comb(3-k, j)) for j in range(4-k)]
        term = multiply(real_power, denominator_complement)
        numerator = add(numerator, [polynomial[k] * value for value in term])
    check("full real-part numerator", numerator, "=", list(map(F, [1, 6, -83])))
    endpoint = evaluate(numerator, F(81, 625))
    check("closed-segment endpoint numerator", endpoint, "=", F(149812, 390625))
    check("endpoint positivity", endpoint, ">", F(0))

    s, grid_mean = F(11, 10), F(4, 11)
    check("angular minimum at grid mean", (s+grid_mean)/(1+s*grid_mean), "=", F(23, 22))
    check("angular maximum factor", (s-F(8, 11))/(1-s*F(8, 11)), "=", F(41, 22))
    check("half-circle coefficient factor", (F(1, 2)+grid_mean)/(1+grid_mean/2), "=", F(19, 26))
    check("combined cost base", F(23, 22)*F(26, 19), "=", F(299, 209))
    check("cost prefactor", F(6, 5)*F(209, 299), "=", F(1254, 1495))
    z = F(3, 8)
    log_upper = 2*(z+z**3/(3*(1-z**2)))
    check("logarithm upper constant", log_upper, "=", F(87, 110))
    rate = F(45, 127)-F(3, 7)*log_upper
    check("lower cost exponent", rate, "=", F(1503, 97790))
    check("required cost exponent exceeded", rate, ">", F(1, 100))
    check("rate excess", rate-F(1, 100), "=", F(5251, 977900))
    beta_margin = 13*F(57, 88)**2-2
    check("beta2 bracket at J=14", beta_margin, "=", F(26749, 7744))
    check("beta2 bracket positivity", beta_margin, ">", F(0))
    check("cubic inverse base", F(23, 22)*F(11, 4), "=", F(23, 8))

    failures = [row["name"] for row in checks if not row["passed"]]
    path = Path(__file__).with_suffix(".json")
    certificate = {
        "result": "PASS" if not failures else "FAIL",
        "scope": "Exact rational support for L675; no verification of analytic interchanges or a higher-degree cost bound.",
        "checks": checks,
        "failures": failures,
        "degree_obstruction": {
            "degree_fraction_at_most": F(3, 7),
            "actual_proved_rate_lower_bound": rate,
            "required_rate": F(1, 100),
            "prefactor": F(1254, 1495),
        },
        "unresolved": ["Degrees greater than 3n/7", "higher coefficient zeros and inverse costs",
                       "a budget-feasible continuum-positive polynomial", "original H and Xi realization"],
    }
    path.write_text(json.dumps(encode(certificate), indent=2) + "\n")
    print(f"{certificate['result']}: {len(checks)} exact arithmetic checks; failures={failures}")
    print(f"Proved rate >= {rate}; required rate <= 1/100; excess={rate-F(1, 100)}")
    print(f"Certificate: {path.relative_to(Path.cwd())}")
    raise SystemExit(bool(failures))


if __name__ == "__main__":
    main()
