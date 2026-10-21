"""Exact arithmetic supporting L044; the analytic proof is in the lemma."""

from fractions import Fraction as F
import json
from pathlib import Path


def main():
    q = 2**13 - 1
    threshold = 338460000
    a = F(399, 5) * q
    b = 72 * q + F(897, 1034)
    records = []

    def check(name, actual, relation, required):
        passed = {"<": actual < required, ">": actual > required,
                  "=": actual == required}[relation]
        records.append({"name": name, "actual": str(actual),
                        "relation": relation, "required": str(required),
                        "passed": passed})

    check("delta lower sign", 27, ">", 16)
    check("delta upper bound", 3**5, "<", 2**8)
    check("transfer coefficient", F(3, 4) * F(8, 5)**2, "=", F(48, 25))
    check("transfer additive bound", F(8, 5) * F(4, 5) * F(4, 3) / 4,
          "=", F(32, 75))
    check("coefficient below two", F(48, 25), "<", 2)
    check("additive bound below one", F(32, 75), "<", 1)
    check("exponential partial sum", sum((F(1), F(1), F(1, 2), F(1, 6),
                                          F(1, 24), F(1, 120))),
          ">", F(27, 10))
    check("log thirteen below three", 27**3, ">", 13 * 10**3)
    check("thirteen occurrence sum", sum(2**j for j in range(13)), "=", q)
    check("seed times count coefficient", 6 * F(133, 10), "=", F(399, 5))
    check("A", a, "=", F(3268209, 5))
    check("primitive threshold scaling", F(3, 2) * 225640000, "=", threshold)
    check("log threshold below twenty", 27**20, ">", threshold * 10**20)
    check("positive derivative on entire ray", a, "<", threshold)
    check("threshold right side", 20 * a + b, "<", 13662589)
    check("integer margin", threshold - 13662589, "=", 324797411)
    check("strict margin positive", threshold - 20 * a - b,
          ">", 324797411)

    failures = [r["name"] for r in records if not r["passed"]]
    certificate = {"lemma": "L044", "scope": "Exact constants only; analytic proof in lemma",
                   "checks": records, "failures": failures,
                   "summary": {"A": str(a), "B": str(b), "threshold": threshold,
                               "threshold_rhs_upper": str(20 * a + b),
                               "margin_lower": str(threshold - 20 * a - b),
                               "required_margin": "0"}}
    path = Path(__file__).with_name("thirteen-certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"{len(records)} exact checks; failures: {failures}")
    for key, value in certificate["summary"].items():
        print(f"{key}: {value}")
    print(f"certificate: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
