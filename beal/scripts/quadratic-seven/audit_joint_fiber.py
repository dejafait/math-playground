#!/usr/bin/env python3
"""Independent integer/F7 replay of L105; exact existence is proved in L105."""
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "joint-fiber-certificate.json"
OUT = HERE / "joint-fiber-audit.json"
raw = SOURCE.read_bytes()
saved = json.loads(raw)
checks = {}
evidence = {}


def check(name, actual, required):
    checks[name] = actual == required
    evidence[name] = {"actual": actual, "required": required}


def qpower(n):
    # Independent multinomial expansion of (1+t+3t^2)^n.
    a = [0] * (2*n+1)
    for twos in range(n+1):
        for ones in range(n-twos+1):
            a[2*twos+ones] += comb(n, twos)*comb(n-twos, ones)*3**twos
    return a


def ev(a, x):
    return sum(c*x**i for i, c in enumerate(a))


def der(a):
    return [i*c for i, c in enumerate(a)][1:]


def v7(n):
    assert n
    ans = 0
    while n % 7 == 0:
        ans, n = ans+1, n//7
    return ans


def norm(a):
    a = [x % 7 for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def mul(a, b):
    return norm([sum(a[i]*b[k-i] for i in range(len(a))
                     if 0 <= k-i < len(b))
                 for k in range(len(a)+len(b)-1)])


def rem(a, b):
    a, b = norm(a), norm(b)
    for k in range(len(a)-len(b), -1, -1):
        c = a[k+len(b)-1]*pow(b[-1], -1, 7) % 7
        for j in range(len(b)):
            a[k+j] = (a[k+j]-c*b[j]) % 7
    return norm(a)


def gcd(a, b):
    a, b = norm(a), norm(b)
    while b != [0]:
        a, b = b, rem(a, b)
    return norm([c*pow(a[-1], -1, 7) for c in a])


def sub(a, b):
    return norm([(a[i] if i < len(a) else 0) -
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def irreducibility(h):
    n = len(h)-1
    # Iterated Frobenius by exponent substitution, not binary powering.
    frob = [[0, 1]]
    for _ in range(n):
        a = [0] * (7*(len(frob[-1])-1)+1)
        for j, c in enumerate(frob[-1]):
            a[7*j] = c
        frob.append(rem(a, h))
    primes = [p for p in range(2, n+1) if n % p == 0
              and all(p % d for d in range(2, p))]
    final = rem(sub(frob[n], [0, 1]), h)
    tests = [{"q": p, "gcd": gcd(h, sub(frob[n//p], [0, 1]))}
             for p in primes]
    return {"degree": n, "frobenius_final_remainder": final,
            "proper_subdegree_gcds": tests,
            "passes": final == [0] and all(t["gcd"] == [1] for t in tests)}


def lift(a, seed):
    # Newton's unique next digit, unlike the original exhaustive digit loop.
    x, modulus, steps = seed, 7, []
    assert ev(a, x) % 7 == 0 and ev(der(a), x) % 7 != 0
    for precision in [2, 3]:
        digit = -(ev(a, x)//modulus)*pow(ev(der(a), x), -1, 7) % 7
        x += digit*modulus
        modulus *= 7
        assert ev(a, x) % modulus == 0
        steps.append({"precision": precision, "root": x, "modulus": modulus,
                      "error_valuation": v7(ev(a, x)),
                      "derivative_residue": ev(der(a), x) % 7})
    return {"seed": seed, "seed_error": ev(a, seed),
            "seed_error_valuation": v7(ev(a, seed)),
            "seed_derivative_residue": ev(der(a), seed) % 7,
            "steps": steps, "root_mod_343": x}


q5 = qpower(5)
phi = [(q5[i] if i < len(q5) else 0) -
       (5*q5[i-1] if i else 0) for i in range(12)]
check("phi_all_coefficients", saved["phi"], phi)
check("derivative_identity", der(phi), [0, 0]+[-165*c for c in qpower(4)])
check("leading_coefficient", phi[-1], -1215)
check("low_coefficients", phi[:4], [1, 0, 0, -55])
check("coefficient_order", saved["coefficient_order"], "low first")
check("prime", saved["prime"], 7)
original_checks = {"degree_eleven": len(phi)-1 == 11,
                   "derivative_identity": der(phi) == [0, 0]+[-165*c for c in qpower(4)]}
check("regular_scalar_coverage", [r["scalar"] for r in saved["regular"]], list(range(2, 7)))
for row in saved["regular"]:
    s = row["scalar"]
    f = [phi[0]-s]+phi[1:]
    reconstruction = [phi[-1] % 7]
    for i, factor in enumerate(row["complete_factors"]):
        h, multiplicity = factor["coefficients_low_first"], factor["multiplicity"]
        check(f"{s}_factor_{i}_monic", h[-1], 1)
        check(f"{s}_factor_{i}_multiplicity", multiplicity, 1)
        cert = irreducibility(h)
        check(f"{s}_factor_{i}_certificate", factor["irreducibility"], cert)
        original_checks[f"regular_{s}_factor_{i}_irreducible"] = cert["passes"]
        for _ in range(multiplicity):
            reconstruction = mul(reconstruction, h)
    check(f"{s}_reconstruction", reconstruction, norm(f))
    check(f"{s}_leading_unit", row["leading_unit"], phi[-1] % 7)
    check(f"{s}_squarefree", gcd(f, der(f)), [1])
    roots = [r for r in range(7) if ev(f, r) % 7 == 0]
    check(f"{s}_root_list", row["rational_residue_roots"], roots)
    tuples = [list(t) for t in product(range(1, 7), repeat=3)
              if (t[0]**3+t[1]**5-t[2]**11) % 7 == 0
              and (t[1]**5-s*t[2]**11) % 7 == 0]
    check(f"{s}_complete_tuples", row["all_unit_primitive_residue_tuples"], tuples)
    original_checks[f"regular_{s}_reconstruction"] = reconstruction == norm(f)
    original_checks[f"regular_{s}_squarefree"] = gcd(f, der(f)) == [1]
    original_checks[f"regular_{s}_fewer_than_three_roots"] = len(roots) < 3

quadratic = [3, 0, 1]
check("entire_quadratic_record", saved["quadratic"],
      {"polynomial": quadratic, "lifts": [lift(quadratic, a) for a in [2, 5]]})
numerators = [-343]+[-c*7**i for i, c in enumerate(phi) if i]
check("normalized_integrality", [n % 343 for n in numerators], [0]*12)
g = [n//343 for n in numerators]
roots = [a for a in range(7) if ev(g, a) % 7 == 0]
check("normalized_root_residues", roots, [3, 5, 6])
bp = [342, 0, 0, 0, 0, 1]
branch = {"A": 7, "C": 1, "scalar": -342, "one_minus_scalar": 343,
          "B_polynomial": bp, "B_seed": 1, "B_error": ev(bp, 1),
          "B_error_valuation": v7(ev(bp, 1)), "B_derivative_residue": 5,
          "B_lift": lift(bp, 1), "normalized_g": g, "g_reduction": norm(g),
          "roots": [lift(g, a) for a in roots], "required_rational_factors": 3,
          "certified_rational_factors": len(roots), "complement_degree": 11-len(roots),
          "max_normalized_precision": 343}
check("entire_branch_record", saved["branch"], branch)
check("common_tuple_identity", 7**3-342, 1**11)
check("normalized_strict_hensel_margins",
      [v7(ev(g, a))-2*v7(ev(der(g), a)) for a in roots], [1, 1, 2])
check("scaled_identity", [343*c for c in g],
      [-phi[0]-342]+[-phi[i]*7**i for i in range(1, 12)])
check("distinct_root_difference_units", [((a-b) % 7 != 0)
      for a, b in [(3, 5), (3, 6), (5, 6)]], [True]*3)
check("critical_values_nonzero", [phi[0]+342 != 0, 342 != 0], [True, True])
check("degree_accounting", 3+branch["complement_degree"], 11)
original_checks.update({
    "normalized_reduction": norm(g) == [6, 0, 0, 6],
    "normalized_three_simple_roots": roots == [3, 5, 6] and all(
        ev(der(g), a) % 7 != 0 for a in roots),
    "scaled_identity_all_coefficients": [343*c for c in g] ==
        [-343]+[-phi[i]*7**i for i in range(1, 12)],
    "common_B_strict_hensel": v7(ev(bp, 1)) == 3 and ev(der(bp), 1) % 7 == 5,
    "quadratic_split_simple_roots": all(
        ev(quadratic, a) % 7 == 0 and ev(der(quadratic), a) % 7 != 0 for a in [2, 5]),
    "whole_fiber_etale": -342 not in [0, 1] and phi[0] == 1})
check("all_original_checks_recomputed", saved["checks"], original_checks)
check("all_original_checks_true", all(original_checks.values()), True)
check("original_failures", saved["failures"], [])
failures = [name for name, ok in checks.items() if not ok]
summary = {"audit_checks": len(checks), "original_checks": len(original_checks),
           "failures": failures, "rational_factors_actual": len(roots),
           "rational_factors_required": 3, "complement_degree_actual": 11-len(roots),
           "complement_degree_required": 8, "precision_actual": 343, "precision_cap": 343,
           "proof_scope": "Arithmetic replay only; exact Hensel/CRT existence audited in L105."}
OUT.write_text(json.dumps({"source_sha256": sha256(raw).hexdigest(),
                          "summary": summary, "checks": checks, "evidence": evidence},
                         indent=2)+"\n")
print(json.dumps(summary))
print("certificate:", OUT)
assert not failures
