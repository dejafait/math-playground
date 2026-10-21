#!/usr/bin/env python3
"""Independent exact audit of L043's saved certificate; no orbit claim.

Run: python3 scripts/postspell-word-count/audit_cutoff.py
Uses a closed geometric sum and Horner evaluation of the logarithm
polynomial, without importing or executing the certificate generator.
The analytic remainder and monotonicity proofs are in canonical L043.
"""

from fractions import Fraction as F
import json
from pathlib import Path


def encode(value):
    if isinstance(value, F):
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}
    return value


def decode(value):
    return F(int(value["numerator"]), int(value["denominator"]))


def main():
    directory = Path(__file__).parent
    source = directory / "cutoff-certificate.json"
    cert = json.loads(source.read_text())
    checks = []

    def check(name, actual, relation, required):
        passed = {"==": lambda: actual == required,
                  "<": lambda: actual < required,
                  ">": lambda: actual > required}[relation]()
        checks.append(dict(name=name, actual=encode(actual), relation=relation,
                           required=encode(required), passed=passed))

    def rational_match(name, saved, expected):
        check(name, decode(saved), "==", expected)

    c12, c13, logs = cert["r12"], cert["r13"], cert["log_enclosures"]
    threshold = 225640000
    c = F(3, 2) * threshold
    check("threshold", c12["threshold"], "==", threshold)
    check("C", c12["C"], "==", c)
    q12 = F(8, 15) * (F(23, 8)**12 - 1)
    q13 = F(8, 15) * (F(23, 8)**13 - 1)
    a12, a13 = F(399, 5)*q12, F(399, 5)*q13
    rhs12 = F(8334, 5)*q12 + F(828, 1034)
    margin12 = c-rhs12
    for name, expected in {"Q": q12, "A": a12,
                           "conservative_rhs": rhs12, "margin": margin12}.items():
        rational_match("r12/"+name, c12[name], expected)
    check("A12 derivative threshold", a12, "<", c)
    check("r12 positive margin", margin12, ">", 54971760)
    check("displayed r12 margin", margin12, "==", F(610323442974809006259, 11102490460160))
    check("e partial sum", sum((F(1, x) for x in [1, 1, 2, 6, 24, 120]), F(0)), "==", F(163, 60))
    check("e lower comparison", F(163, 60), ">", F(27, 10))
    check("log12 comparison", F(27, 10)**3, ">", 12)
    check("logC comparison", F(27, 10)**20, ">", c)
    check("saved power", int(c12["exp20_integer_lhs"]), "==", 27**20)
    check("saved power threshold", int(c12["exp20_integer_rhs"]), "==", c*10**20)
    check("log ratio comparison", 3**2, ">", 2**3)

    r, k, ell, n = c13["r"], c13["K"], c13["L"], c13["N"]
    check("r13", r, "==", 13)
    check("integer count fields", all(type(c13[key]) is int for key in ["r", "K", "L", "N", "d", "K0", "L0"]), "==", True)
    for name, minimum in [("J", 2), ("H", 3), ("a", 2)]:
        check(name+" count", len(c13[name]), "==", r)
        check(name+" integer guards", all(type(v) is int and v >= minimum for v in c13[name]), "==", True)
    check("tail congruences", all(a % 18 == 2 for a in c13["a"]), "==", True)
    sj, sh, sa = (sum(c13[key]) for key in ["J", "H", "a"])
    check("K identity", k, "==", 3*sj+sh)
    check("L identity", ell, "==", sj+sa)
    check("N identity", n, "==", 4*sj+sh+sa)
    check("N=K+L", n, "==", k+ell)
    check("d positive", c13["d"], ">", 0)
    check("K scaling", k, "==", c13["d"]*c13["K0"])
    check("L scaling", ell, "==", c13["d"]*c13["L0"])
    check("primitive odd threshold", c13["K0"], ">", threshold)
    check("primitive even positivity", c13["L0"], ">", 0)
    check("minimum total length", n, ">", 13*r)
    rational_match("r13/Q", c13["Q"], q13)
    rational_match("r13/A", c13["A"], a13)
    margin13 = 17*a13-n
    rational_match("r13/lower_rhs_margin", c13["lower_rhs_margin"], margin13)
    check("displayed r13 margin", margin13, "==", F(105043938617475067559, 343597383680))
    check("r13 length margin", margin13, ">", 0)
    check("log N lower comparison", n, ">", 3**17)

    check("series terms", logs["terms"], "==", 64)
    for t in [2, 3]:
        x = F(t-1, t+1)
        poly = F(0)
        for j in reversed(range(64)):
            poly = F(1, 2*j+1) + x*x*poly
        lower = 2*x*poly
        upper = lower + 2*x**129/(129*(1-x*x))
        rational_match(f"log{t} Horner lower", logs[f"log{t}_lower"], lower)
        rational_match(f"log{t} geometric upper", logs[f"log{t}_upper"], upper)
        check(f"log{t} decimal lower", decode(logs[f"decimal_log{t}_lower"]), "<", lower)
        check(f"log{t} decimal upper", upper, "<", decode(logs[f"decimal_log{t}_upper"]))

    lo = n*decode(logs["decimal_log2_lower"])-k*decode(logs["decimal_log3_upper"])
    hi = n*decode(logs["decimal_log2_upper"])-k*decode(logs["decimal_log3_lower"])
    cap = F(23*r, 517)
    for name, value in [("lambda_lower", lo), ("lambda_upper", hi), ("lambda_cap", cap)]:
        rational_match("r13/"+name, c13[name], value)
    check("displayed lambda lower", lo, "==", F(40739498685267, 78125000000000))
    check("displayed lambda upper", hi, "==", F(2607328207492559, 5000000000000000))
    check("lambda lower", lo, ">", F(1, 2))
    check("lambda upper", hi, "<", F(53, 100))
    check("lambda cap", F(53, 100), "<", cap)
    check("lower-form comparison", F(1, k), "<", F(1, 2))
    check("original check count", len(cert["checks"]), "==", 23)
    check("original flags", all(v is True for v in cert["checks"].values()), "==", True)
    check("original failures", cert["failures"], "==", [])

    failures = [row["name"] for row in checks if not row["passed"]]
    result = dict(source=source.as_posix(), scope="Exact scalar arithmetic only; analytic justification in L043; no orbit constructed.", checks=checks, failures=failures)
    output = directory / "audit-certificate.json"
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(f"Independent exact audit: {len(checks)-len(failures)}/{len(checks)} checks; failures: {failures}")
    print(f"r12 margin > {margin12.numerator // margin12.denominator}; required > 0")
    print(f"r13 length margin > {margin13.numerator // margin13.denominator}; required > 0")
    print("r13: 1/2 < Lambda < 53/100 < 299/517; required 0 < Lambda < 299/517")
    print(f"Full exact checks and bounds: {output.as_posix()}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
