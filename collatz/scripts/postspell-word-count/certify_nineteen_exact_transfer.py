#!/usr/bin/env python3
"""Exact arithmetic for L048; analytic scope and monotonicity are in its proof."""
import json
from fractions import Fraction as F
from pathlib import Path

checks = []


def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {"<": actual < required, ">": actual > required,
              "=": actual == required}[relation]
    checks.append({"name": name, "actual": str(actual),
                   "relation": relation, "required": str(required),
                   "passed": passed})


def log_enclosure(t, m=12):
    x = (t - 1) / (t + 1)
    lower = 2 * sum((x**(2*k+1) / (2*k+1) for k in range(m)), F(0))
    remainder = 2*x**(2*m+1) / ((2*m+1)*(1-x*x))
    return {"argument": str(t), "x": str(x), "terms": m,
            "lower": str(lower), "remainder_upper": str(remainder),
            "upper": str(lower + remainder)}


logs = {"log2": log_enclosure(F(2)), "log3": log_enclosure(F(3)),
        "cJ": log_enclosure(F(11, 4))}
check("log2 strict lower bound", F(logs["log2"]["lower"]), ">", F(6931, 10000))
check("log3 strict upper bound", F(logs["log3"]["upper"]), "<", F(10987, 10000))
check("cJ strict upper bound", F(logs["cJ"]["upper"]), "<", F(41, 40))
delta_bound = F(793, 500)
check("delta rational bound", F(10987, 6931), "<", delta_bound)
q = F(189, 100)
b = F(31, 100)
check("exact-transfer coefficient enclosure", 3*delta_bound**2/4, "<", q)
check("exact-transfer additive enclosure", delta_bound*(3*delta_bound-4)*F(41, 40)/4, "<", b)
S = sum((q**j for j in range(19)), F(0))
U = sum((sum((q**k for k in range(j)), F(0)) for j in range(19)), F(0))
check("geometric closed form", S, "=", F(189**19-100**19, 89*100**18))
check("additive sum identity", U, "=", (S-19)/(q-1))
check("geometric upper enclosure", S, "<", 201100)
check("additive contribution enclosure", 6*b/(q-1), "<", F(21, 10))
check("e lower enclosure", F(163, 60), ">", F(27, 10))
check("log19 less than 3", 27**3, ">", 19*10**3)
C = 338460000
M = 225640000
check("logC less than 20", 27**20, ">", C*10**20)
check("primitive ray threshold", F(3, 2)*M, "=", C)
check("constant remainder enclosure", F(456, 5)+F(1311, 1034), "<", 93)
A = F(399, 5)*201100
B = (66+F(21, 10))*201100+93
check("coefficient evaluation", A, "=", 16047780)
check("constant evaluation", B, "=", 13695003)
check("positive derivative on entire ray", A, "<", C)
check("RHS at ray start", 20*A+B, "<", C)
failures = [record for record in checks if not record["passed"]]
certificate = {"lemma": "L048", "scope": "Exact-transfer rational enclosure for nineteen actual words; analytic applicability, logarithm remainder proof and all-real monotonicity are in L048. Not an independent proof audit.",
               "log_enclosures": logs, "delta_upper": str(delta_bound),
               "q_upper": str(q), "b_upper": str(b), "S": str(S), "U": str(U),
               "A": str(A), "B": str(B), "C": C,
               "rhs_at_C_strict_upper": str(20*A+B),
               "full_ray_positive_margin": str(C-20*A-B),
               "checks": checks, "failures": failures}
path = Path(__file__).with_name("nineteen-exact-transfer-certificate.json")
path.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"checks={len(checks)}, failures={len(failures)}")
print(f"certified q < {q}, b < {b}, S < 201100")
print(f"N < {A} log N + {B}; derivative requires A < C={C}: {A<C}")
print(f"at C, RHS < {20*A+B}; required RHS <= {C}; margin > {C-20*A-B}")
print(f"certificate: {path.relative_to(Path.cwd())}")
if failures:
    print("failed checks: "+", ".join(record["name"] for record in failures))
    raise SystemExit(1)
