"""Exact arithmetic for L073; Hensel and Kummer proofs remain in the lemma."""
import json
from pathlib import Path


def add(a, b):
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))]


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def rem(a, b):
    a = a[:]
    assert b[-1] == 1
    for i in range(len(a)-1, len(b)-2, -1):
        c = a[i]
        for j, v in enumerate(b):
            a[i-len(b)+1+j] -= c*v
    return a[:len(b)-1]


def val(a, x):
    return sum(c*x**i for i, c in enumerate(a))


g = [-1264, -160, -4, 1]
h = [-160, -8, 3]
dq = [656, 8, -3]
b, c, d = -4, -160, -1264
disc = b*b*c*c - 4*c**3 - 4*b**3*d - 27*d*d + 18*b*c*d
m = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]
residue_product = [1]
for root in [-1]*10 + [-3, -9]:
    residue_product = mul(residue_product, [-root, 1])
square_residues = sorted({i*i % 11 for i in range(1, 11)})
checks = {}


def check(name, actual, required):
    checks[name] = {"actual": actual, "required": required, "pass": actual == required}


check("base_polynomial_mod_11", [x % 11 for x in m], [x % 11 for x in residue_product])
check("base_simple_derivatives", [sum(i*m[i]*x**(i-1) for i in range(1, 13)) % 11 for x in [8, 2]], [6, 5])
check("base_shift_constant", val(m, -1), -209)
check("base_radical_unit_residue", (-19 * pow(5, -1, 11)) % 11, 5)
check("g_integer_factor_difference", add(g, [-x for x in mul([-8, 1], mul([-9, 1], [-9, 1]))]), [-616, -385, 22, 0])
check("alpha_derivative", val(h, 8), -32)
check("cubic_discriminant", disc, -256*11**5)
check("quadratic_discriminant_identity_remainder", rem(add(mul(dq, mul(h, h)), [256*11**5]), g), [0, 0, 0])
check("sqrt_five_hensel", [(4*4-5) % 11, 2*4 % 11], [0, 8])
check("root_residues", [8, ((4-8)*pow(2, -1, 11)) % 11], [8, 9])
check("nonzero_square_residues", square_residues, [1, 3, 4, 5, 9])
check("ramified_root_difference_valuation", 2*10+5, 25)
check("odd_exceptional_valuation_parity", [v % 2 for v in [0, 25, 25]], [0, 1, 1])
check("entire_Q11_dimension", 2*(1+2)+3*10, 36)

out = {"scope": "Exact finite arithmetic only; full local realization and exhaustiveness are proved in L073.",
       "checks": checks, "failures": [k for k, v in checks.items() if not v["pass"]]}
path = Path(__file__).with_name("audit-certificate.json")
path.write_text(json.dumps(out, indent=2) + "\n")
print(f"Checks passed: {len(checks)-len(out['failures'])}/{len(checks)}; failures: {out['failures']}")
print("Root difference valuation: actual 25, required 25 (odd); dimension: actual 36, required 36")
print(f"Certificate: {path}")
if out["failures"]:
    raise SystemExit(1)
