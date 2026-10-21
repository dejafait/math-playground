"""Independent verification of all L069 certificate data by exact identities.

Does not import or execute check_diagnostic.py. Sturm division witnesses
are verified by convolution, remainder degree and positive rescaling;
uniqueness of polynomial division then certifies each recorded division.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
source = HERE / "diagnostic-certificate.json"
raw = source.read_bytes()
data = json.loads(raw)
checks = {}
evidence = {}


def test(name, condition):
    checks[name] = bool(condition)


def coeffs(values):
    return list(map(Q, values))


def add(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] += c
    for i, c in enumerate(b):
        out[i] += c
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i + j] += c * d
    return out


def scale(a, c):
    return [c * x for x in a]


def derivative(a):
    return [i * a[i] for i in range(1, len(a))]


def val(a, x):
    out = 0
    for c in reversed(a):
        out = out * x + c
    return out


def determinant(matrix):
    a = [coeffs(row) for row in matrix]
    result = Q(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        p = a[i][i]
        result *= p
        for j in range(i + 1, len(a)):
            c = a[j][i] / p
            a[j] = [x - c * y for x, y in zip(a[j], a[i])]
    return result


m = coeffs([-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1])
g = coeffs([-1264, -160, -4, 1])
test("inputs_match_L033_and_transformed_curve", data["inputs"] == {"m": m, "g": g})


def audit_sturm(key, polynomial, derivative_scale):
    record = data[key]
    chain = [coeffs(p) for p in record["ascending_polynomials"]]
    test(key + "_initial_polynomials", chain[0] == polynomial and
         chain[1] == scale(derivative(polynomial), derivative_scale))
    test(key + "_complete_degrees", [len(p) - 1 for p in chain] ==
         list(range(len(polynomial) - 1, -1, -1)))
    test(key + "_division_count", len(record["divisions"]) == len(chain) - 2)
    identities = []
    for i, row in enumerate(record["divisions"]):
        quotient, remainder = coeffs(row["quotient"]), coeffs(row["remainder"])
        c = Q(row["positive_normalization"])
        residual = add(add(mul(quotient, chain[i + 1]), remainder), scale(chain[i], -1))
        normalization_residual = add(chain[i + 2], scale(remainder, c))
        passed = (residual == [0] and normalization_residual == [0] and c > 0
                  and len(remainder) < len(chain[i + 1]) and remainder[-1] != 0)
        test(f"{key}_division_{i}", passed)
        identities.append({"index": i, "quotient": list(map(str, quotient)),
                           "remainder": list(map(str, remainder)),
                           "normalization": str(c), "identity_residual": list(map(str, residual)),
                           "normalization_residual": list(map(str, normalization_residual)),
                           "remainder_degree": len(remainder) - 1, "passed": passed})
    plus = [1 if p[-1] > 0 else -1 for p in chain]
    minus = [s * (-1) ** (len(p) - 1) for p, s in zip(chain, plus)]
    vm = sum(minus[i] != minus[i - 1] for i in range(1, len(minus)))
    vp = sum(plus[i] != plus[i - 1] for i in range(1, len(plus)))
    expected = {"minus_infinity_signs": minus, "plus_infinity_signs": plus,
                "minus_variations": vm, "plus_variations": vp, "real_roots": vm - vp,
                "last_polynomial_is_nonzero_constant": len(chain[-1]) == 1 and chain[-1][0] != 0}
    test(key + "_all_signs_and_counts", all(record[k] == v for k, v in expected.items()))
    test(key + "_terminal_minus_one", chain[-1] == [-1])
    evidence[key] = {"verified_polynomials": record["ascending_polynomials"],
                     "verified_divisions": identities, **expected}
    return vm - vp


rk = audit_sturm("base_sturm", m, Q(1, 6))
rg = audit_sturm("cubic_sturm", g, Q(1))
# Sylvester determinant, independent of the original explicit discriminant formula.
gd = derivative(g)
rows = []
for i in range(2):
    rows.append([0] * i + list(reversed(g)) + [0] * (1 - i))
for i in range(3):
    rows.append([0] * i + list(reversed(gd)) + [0] * (2 - i))
disc = -determinant(rows)
test("discriminant_sylvester", disc == data["cubic_discriminant"] == -256 * 11**5)
evidence["sylvester_matrix"] = [[str(c) for c in row] for row in rows]
evidence["discriminant"] = str(disc)
# Substitute X=4x, Y=8y+4 and reduce the y-polynomial by the original equation.
model = add(scale(coeffs([-20, -10, -1, 1]), 64), [16])
transformed = [c * 4**i for i, c in enumerate(g)]
test("model_identity", model == transformed == data["model"]["lhs_reduced"] == data["model"]["rhs"])
residues = [int(val(g, x) % 5) for x in range(5)]
test("all_five_residues", residues == data["cubic_residue_values_modulo_five"] == [1, 3, 3, 2, 1])
root = {"root": 0, "m_value": int(val(m, 0) % 5),
        "derivative_value": int(val(derivative(m), 0) % 5)}
test("hensel_place", root == data["base_simple_root_modulo_five"] ==
     {"root": 0, "m_value": 0, "derivative_value": 1})
ck = (12 - rk) // 2
rd, cd = rk, rk + 3 * ck
sig = {"K": [rk, ck], "D": [rd, cd]}
test("all_embeddings", rg == 1 and rk + 2 * ck == 12 and rd + 2 * cd == 36 and
     sig == data["signatures"] == {"K": [2, 5], "D": [2, 17]})
dims = {"base_unit_squares": rk + ck, "cubic_unit_squares": rd + cd,
        "norm_square_unit_kernel": rd + cd - rk - ck, "rational_two_torsion": 0,
        "corrected_ambient_lower_bound": rd + cd - rk - ck, "required_upper_bound": 11}
test("dimension_records", dims == data["dimensions"])
test("threshold", dims["corrected_ambient_lower_bound"] == 12 > dims["required_upper_bound"])
expected_flags = {"integral_model_identity", "base_sturm_squarefree", "base_degree_and_signature",
                  "cubic_discriminant", "cubic_one_real_root", "cubic_no_root_modulo_five",
                  "simple_base_root_modulo_five", "entire_cubic_signature", "unit_kernel_dimension",
                  "strict_threshold_fails"}
test("original_flags_agree_with_verified_claims", set(data["checks"]) == expected_flags and
     all(v is True for v in data["checks"].values()) and data["failures"] == [])
expected_keys = {"inputs", "model", "base_sturm", "cubic_sturm", "cubic_discriminant",
                 "cubic_residue_values_modulo_five", "base_simple_root_modulo_five", "signatures",
                 "dimensions", "checks", "failures", "qualification"}
test("no_uninspected_arithmetic_fields", set(data) == expected_keys)
evidence.update(model=list(map(str, model)), residues=residues, hensel=root, signatures=sig, dimensions=dims)
failures = [k for k, v in checks.items() if not v]
out = {"source_sha256": hashlib.sha256(raw).hexdigest(), "method": __doc__,
       "checks": checks, "failures": failures, "evidence": evidence,
       "qualification": "Arithmetic audit only; L069 supplies field, units, norms and Kummer proof. No rank lower bound."}
destination = HERE / "audit-certificate.json"
destination.write_text(json.dumps(out, indent=2) + "\n")
print(f"Independent checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
print(f"Verified all 13 division records and all 17 Sturm polynomials; signatures: {sig}")
print(f"Ambient lower bound: {dims['corrected_ambient_lower_bound']}; required upper bound: 11")
print(f"Certificate: {destination}")
if failures:
    raise SystemExit(1)
