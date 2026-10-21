#!/usr/bin/env python3
"""Independent exact audit of L045's saved scalar evidence; no orbit claim.

The generator is neither imported nor executed. Full rational values are
checked, with Horner evaluation of the logarithm polynomial. The analytic
justification and scope of these finite checks are in canonical L045.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path


def encode(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)} if isinstance(x, F) else x


def decode(x):
    return F(int(x["numerator"]), int(x["denominator"]))


def main():
    folder = Path(__file__).parent
    paths = [folder / name for name in ("retained-range-certificate.json", "retained-range-initial-certificate.json")]
    originals = [p.read_bytes() for p in paths]
    cert, initial = [json.loads(b) for b in originals]
    records = []

    def check(name, actual, relation, required):
        passed = {"=": lambda: actual == required, "<": lambda: actual < required,
                  ">": lambda: actual > required, ">=": lambda: actual >= required}[relation]()
        records.append(dict(name=name, actual=encode(actual), relation=relation,
                            required=encode(required), passed=passed))

    def match(name, saved, value):
        check(name, decode(saved), "=", value)

    ex, w = cert["exclusion"], cert["first_failure"]
    M, C = 225640000, F(3, 2)*225640000
    R = sum(2**j for j in range(17))
    A = F(399, 5)*R
    rhs = 20*A+72*R+F(69*17, 1034)
    for field, expected in {"last_r": 17, "R": R, "M": M, "C": C}.items():
        check("exclusion/"+field, ex[field], "=", expected)
    for field, expected in {"A": A, "rhs_upper": rhs, "margin_lower": C-rhs}.items():
        match("exclusion/"+field, ex[field], expected)
    check("exponential finite sum", sum(F(1, factorial(j)) for j in range(6)), "=", F(163, 60))
    check("exponential lower comparison", F(163, 60), ">", F(27, 10))
    check("log17 upper comparison", F(27, 10)**3, ">", 17)
    check("logC upper comparison", F(27, 10)**20, ">", C)
    check("derivative threshold", A, "<", C)
    check("real-ray initial margin", C-rhs, ">", 119833000)
    check("primitive length bridge", 3**2, ">", 2**3)

    check("eighteen words", w["r"], "=", 18)
    for key in ("r", "K", "L", "N", "d", "K0", "L0"):
        check(key+" positive integer", type(w[key]) is int and w[key] > 0, "=", True)
    for key, minimum in (("J", 2), ("H", 3), ("a", 0)):
        check(key+" array length", len(w[key]), "=", 18)
        for i, value in enumerate(w[key]):
            check(f"{key}[{i}] integer guard", type(value) is int and value >= minimum, "=", True)
    for i, value in enumerate(w["a"]):
        check(f"a[{i}] exact congruence", value % 18, "=", 2)
    sj, sh, sa = (sum(w[key]) for key in ("J", "H", "a"))
    for label, actual, expected in (("sumJ", sj, 36), ("sumH", sh, 225639893), ("suma", sa, 131990904)):
        check(label, actual, "=", expected)
    k, l, n = (w[key] for key in ("K", "L", "N"))
    check("odd count", k, "=", 3*sj+sh)
    check("even count", l, "=", sj+sa)
    check("total count", n, "=", 4*sj+sh+sa)
    check("N=K+L", n, "=", k+l)
    check("primitive odd scaling", k, "=", w["d"]*w["K0"])
    check("primitive even scaling", l, "=", w["d"]*w["L0"])
    check("primitive odd threshold", w["K0"], ">", M)
    check("length threshold", n, ">", C)
    check("logN lower comparison", n, ">", 3**17)
    r18 = sum(2**j for j in range(18))
    krhs = F(15, 4)*r18*(F(133, 10)*17+9)
    nrhs = r18*(F(399, 5)*17+54)+F(69*18, 1034)
    match("saved K lower bound", w["K_rhs_lower"], krhs)
    match("saved N lower bound", w["N_rhs_lower"], nrhs)
    check("aggregate odd-count bound", k, "<", krhs)
    check("aggregate length bound", n, "<", nrhs)
    check("length conversion, stronger form", n, "<", F(8, 5)*k)

    decimals = {2: (F(6931471805599453, 10**16), F(6931471805599454, 10**16)),
                3: (F(10986122886681096, 10**16), F(10986122886681097, 10**16))}
    for t in (2, 3):
        x = F(t-1, t+1)
        polynomial = F(0)
        for j in range(63, -1, -1):
            polynomial = polynomial*x*x+F(1, 2*j+1)
        low = 2*x*polynomial
        high = low+F(2, 129)*x**129/(1-x*x)
        match(f"log{t} complete lower endpoint", cert["log_evidence"][f"log{t}_lower"], low)
        match(f"log{t} complete upper endpoint", cert["log_evidence"][f"log{t}_upper"], high)
        check(f"log{t} decimal lower", decimals[t][0], "<", low)
        check(f"log{t} decimal upper", high, "<", decimals[t][1])
    low = n*decimals[2][0]-k*decimals[3][1]
    high = n*decimals[2][1]-k*decimals[3][0]
    match("saved lambda lower", w["lambda_lower"], low)
    match("saved lambda upper", w["lambda_upper"], high)
    check("positive lambda margin", low, ">", F(1, 2))
    check("lambda upper", high, "<", F(53, 100))
    check("upper cap", F(53, 100), "<", F(23*18, 517))
    check("lower-form exponent guard", F(133, 10), ">", 1)
    check("lower-form constant guard", F(6125581, 10**6), ">", 0)
    check("lower-form domination", F(1, k), "<", F(1, 2))

    # Verify every saved comparison including complete actual/required values.
    # The source and all 99 records were also inspected against the proof.
    check("saved comparison count", len(cert["checks"]), "=", 99)
    for row in cert["checks"]:
        check("replay/"+row["name"], decode(row["actual"]), row["relation"], decode(row["required"]))
        check("saved pass/"+row["name"], row["passed"], "=", True)
    check("saved summary count", cert["summary"]["checks"], "=", 99)
    check("saved failures", cert["summary"]["failures"], "=", [])
    olda = initial["first_failure"]["a"][0]
    check("initial failed tail", olda, "=", 131990860)
    check("initial tail residue", olda % 18, "=", 10)
    check("initial reported failure", initial["summary"]["failures"], "=", ["a[0] congruence"])
    for p, original in zip(paths, originals):
        check(p.name+" preserved", p.read_bytes() == original, "=", True)
    failures = [row["name"] for row in records if not row["passed"]]
    output = folder / "retained-range-audit-certificate.json"
    output.write_text(json.dumps({"scope": "Independent scalar arithmetic audit, not orbit realization or source computation verification",
        "input_sha256": {p.name: sha256(b).hexdigest() for p, b in zip(paths, originals)},
        "checks": records, "summary": {"checks": len(records), "failures": failures}}, indent=2)+"\n")
    print(f"checks: {len(records)}; failures: {failures}")
    print(f"r17 RHS upper: {rhs}; required < {C}; margin: {C-rhs} > 119833000")
    print(f"r18 K={k} < {krhs}; N={n} < {nrhs}")
    print(f"lambda: ({low}, {high}); required: > 1/2 and < 414/517")
    print(f"initial tail residue: {olda % 18}; required: 2 (preserved failure)")
    print(f"certificate: {output}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
