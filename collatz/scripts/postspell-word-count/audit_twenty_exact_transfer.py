#!/usr/bin/env python3
"""Independent rational audit of L049; does not test cycle feasibility."""
import hashlib
import json
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

folder = Path(__file__).resolve().parent
original = folder / "twenty-exact-transfer-certificate.json"
before = original.read_bytes()
subprocess.run([sys.executable, str(folder / "certify_twenty_exact_transfer.py")],
               check=True, capture_output=True, text=True)
after = original.read_bytes()
data = json.loads(after)
checks = []


def check(name, actual, relation, required):
    a, b = F(actual), F(required)
    difference = a.numerator*b.denominator - b.numerator*a.denominator
    passed = {"=": difference == 0, "<": difference < 0,
              ">": difference > 0}[relation]
    checks.append(dict(name=name, actual=str(a), relation=relation,
                       required=str(b), cross_difference=str(difference),
                       passed=passed))


def saved(name, value):
    check("recomputed " + name, value, "=", data[name])


check("byte-identical regeneration", int(before == after), "=", 1)
saved("occurrences", 20)
saved("transfers", 19)
check("original check count", len(data["checks"]), "=", 29)
check("original failure count", len(data["failures"]), "=", 0)
for record in data["checks"]:
    check("cross-product: " + record["name"], record["actual"],
          record["relation"], record["required"])

# Independently accumulate successive odd powers, rather than using the
# generator's direct sum of powers. The proof justifies this finite remainder.
enclosures = {}
for name, t in [("log2", F(2)), ("log3", F(3)), ("cJ", F(11, 4))]:
    x = (t-1)/(t+1)
    power, lower = x, F(0)
    for denominator in range(1, 24, 2):
        lower += 2*power/denominator
        power *= x*x
    remainder = 2*power/(25*(1-x*x))
    values = dict(argument=t, x=x, terms=12, lower=lower,
                  remainder_upper=remainder, upper=lower+remainder)
    for field, value in values.items():
        check(name + ": " + field, value, "=", data["log_enclosures"][name][field])
    enclosures[name] = {key: str(value) for key, value in values.items()}

lo, hi = F(19, 12), F(793, 500)
for name, value in [("delta_lower", lo), ("delta_upper", hi),
                    ("q_lower", F(47, 25)), ("q_upper", F(189, 100)),
                    ("b_lower", F(19, 64)), ("b_upper", F(31, 100))]:
    saved(name, value)
check("positive delta lower minus one", lo-1, ">", 0)
check("positive 3delta lower minus four", 3*lo-4, ">", 0)
check("q lower exceeds one", F(47, 25), ">", 1)

# Horner evaluation of explicit multiplicity polynomials: U's coefficients
# are 19,18,...,1, and S has twenty coefficients equal to one.
sums = {}
for suffix, q in [("lower", F(47, 25)), ("upper", F(189, 100))]:
    S, U = F(0), F(0)
    for _ in range(20):
        S = q*S+1
    for coefficient in range(1, 20):
        U = q*U+coefficient
    saved("S_" + suffix, S)
    saved("U_" + suffix, U)
    check(suffix + " geometric identity", (q-1)*U, "=", S-20)
    sums[suffix] = (S, U)

# Accumulate factorial terms recursively, independently of math.factorial.
term, total = F(1), F(1)
for k in range(1, 5):
    term /= k
    total += term
term /= 5
e_lo, e_hi = total+term, total+F(6, 5)*term
saved("e_lower", e_lo)
saved("e_upper", e_hi)
for field, pair in [("log20_bounds", [2, 3]), ("logN_bounds", [19, 20])]:
    for index, value in enumerate(pair):
        check(field + str(index), value, "=", data[field][index])
for name, value in [("N", 370000000), ("C", 338460000), ("M", 225640000)]:
    saved(name, value)

constant = F(8, 5)*3*20 + F(69*20, 1034)
saved("constant", constant)
check("printed constant", constant, "=", F(50322, 517))
check("assembled logN coefficient", F(8, 5)*F(15, 4)*F(133, 10), "=", F(399, 5))
rhs = {}
for suffix, log_n, log_r, b in [("lower", 19, 2, F(19, 64)),
                               ("upper", 20, 3, F(31, 100))]:
    S, U = sums[suffix]
    height_sum = S*(F(133, 10)*log_n+8+log_r)+b*U
    bound = F(8, 5)*(F(15, 4)*height_sum+3*20)+F(69*20, 1034)
    saved("rhs_strict_" + suffix, bound)
    rhs[suffix] = bound
saved("survival_margin_strict_lower", rhs["lower"]-370000000)
check("lower RHS above witness", rhs["lower"], ">", 370000000)
check("printed lower RHS", rhs["lower"], ">", 545558861)
check("printed upper RHS", rhs["upper"], "<", 632443324)

failures = [record for record in checks if not record["passed"]]
certificate = dict(
    lemma="L049", scope="Audit of existing scalar obstruction only; no cycle feasibility test.",
    original_sha256=hashlib.sha256(after).hexdigest(),
    regeneration_identical=before == after, log_enclosures=enclosures,
    sums={key: {"S": str(pair[0]), "U": str(pair[1])} for key, pair in sums.items()},
    rhs={key: str(value) for key, value in rhs.items()},
    checks=checks, failures=failures)
path = folder / "twenty-exact-transfer-audit-certificate.json"
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"checks={len(checks)}, failures={len(failures)}; byte-identical regeneration={before == after}")
print("actual N=370000000; required N>338460000; 8M/5=361024000")
print("certified 545558861<R(N)<632443324; survival margin>175558861")
print(f"certificate: {path.relative_to(Path.cwd())}")
if failures:
    print("failed checks: " + ", ".join(record["name"] for record in failures))
    raise SystemExit(1)
