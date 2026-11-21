#!/usr/bin/env python3
"""Independent exact-field audit of696; no constructor or service is run."""
from collections import Counter
from fractions import Fraction as R
from hashlib import sha256
from math import prod
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "shared-taylor-bank-audit-698.json"
counts, failures, checked_files = Counter(), [], {}


def check(group, label, predicate):
    counts[group] += 1
    if not predicate:
        failures.append(group + ": " + label)


def read(name):
    path = HERE / name
    raw = path.read_bytes()
    checked_files[name] = sha256(raw).hexdigest()
    return json.loads(raw)


def rational(value):
    if set(value) != {"numerator", "denominator"}:
        raise ValueError("Unexpected rational schema")
    return R(int(value["numerator"]), int(value["denominator"]))


def enc(value):
    value = R(value)
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def same(group, label, stored, expected):
    check(group, label, rational(stored) == expected)


def invpow(n):
    return R(1, 2**n)


cert = read("shared-taylor-bank-696.json")
checked_files["shared-taylor-bank-696.py"] = sha256(
    (HERE / "shared-taylor-bank-696.py").read_bytes()).hexdigest()
check("scope", "top-level schema", set(cert) == {
    "result", "scope", "prescription", "bank", "error", "coefficients",
    "work", "service_failures", "checks", "failures"})
p = cert["prescription"]
same("prescription", "b", p["b"], R(1, 8))
for key, expected in {"Taylor_terms": 128, "weight_series_terms": 192,
                      "log_terms": 512, "Li2_terms": 768,
                      "free_midpoint_nodes_in_work_lower_bound": 3}.items():
    check("prescription", key, p[key] == expected)

# An independent positive geometric tail, and all128 bounds, exactly.
ctail = R(9, 4 * 1025 * 3**1025)
dtail = invpow(768)/769**2 + invpow(1024)
bank = cert["bank"]
same("constants", "log2 tail", bank["log2_tail"], ctail)
same("constants", "D1 tail", bank["D1_tail_upper"], dtail)
check("constants", "log2 threshold", ctail < invpow(1024))
check("constants", "D1 threshold", dtail < invpow(760))
same("bank", "announced radius", bank["uniform_error_bound"], invpow(570))
check("bank", "all powers in order", [r["power"] for r in bank["rows"]]
      == list(range(2, 257, 2)))
errors = []
constant = 16*(invpow(1024) + invpow(760))
for row in bank["rows"]:
    exponent = row["power"]
    denominator = exponent + 193
    truncation = R(4*denominator + 1, 2**574 * denominator**2)
    expected = truncation + constant
    for key, value in {"nonreciprocal_truncation_upper": truncation,
                       "constant_substitution_upper": constant,
                       "nonreciprocal_bank_error_upper": expected,
                       "reciprocal_bank_error": R(0)}.items():
        same("bank", str(exponent)+"/"+key, row[key], value)
    check("bank", str(exponent)+" strict truncation", truncation < invpow(571))
    check("bank", str(exponent)+" strict total", expected < invpow(570))
    errors.append(expected)
same("bank", "maximum over every row", bank["maximum_computed_bound"], max(errors))
check("bank", "not evaluated", bank["actual_bank_evaluated"] is False)

# Compute Taylor ratio as a product of rational factors, not factorial API.
taylor = prod((R(64, j) for j in range(1, 259)), start=R(1))
error = cert["error"]
same("endpoint", "Taylor bound", error["Taylor_remainder_upper"], taylor)
check("endpoint", "Taylor threshold", taylor < invpow(150))
check("endpoint", "dotted prefactor", R(258, 2 * 512**2) < 1)
masses = {
    "Qbar": R(25, 16*259) + R(5, 8*259**2) + R(1, 8*259**3),
    "Abar1": R(1, 2*259) + R(1, 8*259**2),
    "Abar2": R(1, 2*259) + R(1, 8*259**2),
    "1/z": R(1, 258), "-1/z^2": R(8, 257),
    "1/(1+z)": R(1, 8*259), "-1/(1+z)^2": R(1, 8*259)}
check("endpoint", "seven weights", set(error["weighted_remainder_mass"]) == set(masses))
for key, value in masses.items():
    same("endpoint", key, error["weighted_remainder_mass"][key], value)
    check("endpoint", key+" integrable bound", 0 < value < 1)
endpoint = taylor + 2**96 * max(errors)
same("endpoint", "complete bound", error["endpoint_upper"], endpoint)
check("endpoint", "required threshold", endpoint < invpow(149))

interior = R(0)
check("panels", "all three", len(p["panels"]) == 3)
right = R(1)
for panel, N in zip(p["panels"], (117, 81, 63)):
    left = right / 2
    j = {R(1, 2): 1, R(1, 4): 2, R(1, 8): 3}[left]
    check("panels", str(j)+" node/degree", panel["nodes"] == N and panel["j"] == j)
    same("panels", str(j)+" left", panel["left"], left)
    same("panels", str(j)+" right", panel["right"], right)
    degree_exp = 23 + 288*left - 2*(N-1)
    check("panels", str(j)+" exponent", degree_exp == -65)
    panel_error = R(32, 45) * left * invpow(65)
    same("panels", str(j)+" error", panel["ideal_error_upper"], panel_error)
    check("panels", str(j)+" prefactor", left**2*(j+3)**2 <= 4)
    interior += panel_error
    right = left
check("panels", "join at endpoint bank", right == R(1, 8))
same("panels", "total", error["interior_ideal_upper"], interior)
epsilon = interior + endpoint
same("propagation", "complete moment", error["complete_ideal_moment_upper"], epsilon)
check("propagation", "moment threshold", epsilon < invpow(64))
A = 2**18
off = 4*(2*A*epsilon + epsilon**2) + (2*A + 1028)*epsilon
diag = 4*((A+1)*epsilon + epsilon**2) + (A+517)*epsilon
check("propagation", "both off-diagonal endpoints", off < 2**22*epsilon)
check("propagation", "both diagonal endpoints", diag < 2**22*epsilon)

archive = HERE / "frozen-reference-proposal-652.npz"
pin = "2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6"
checked_files[archive.name] = sha256(archive.read_bytes()).hexdigest()
check("witness", "archive pin", checked_files[archive.name] == pin == cert["coefficients"]["archive_sha256"])
with np.load(archive, allow_pickle=False) as stored:
    raw = stored["free_middle_dyadics"].copy()
check("witness", "shape/type/finite", raw.shape == (254, 3)
      and raw.dtype == np.dtype("float64") and np.isfinite(raw).all())
cols = cert["coefficients"]["exact_free_columns"]
check("witness", "complete stored coefficient dimensions", len(cols) == 3 and all(len(c) == 254 for c in cols))
column_masses = []
for j in range(3):
    total = R(0)
    for n in range(254):
        value = R.from_float(float(raw[n, j]))
        same("witness", f"mode{n+2}/column{j}", cols[j][n], value)
        total += abs(value)
    same("witness", f"column{j} mass", cert["coefficients"]["free_l1"][j], total)
    check("witness", f"column{j} threshold", total < R(7, 3) and 2*total < 8)
    column_masses.append(total)
pairs = error["complete_ideal_square_pairs"]
check("propagation", "all nine ordered column pairs", [(x["i"], x["j"]) for x in pairs]
      == [(i, j) for i in range(3) for j in range(3)])
square_bounds = []
for pair in pairs:
    i, j = pair["i"], pair["j"]
    value = (2*column_masses[i])*(2*column_masses[j])*2**21*epsilon
    same("propagation", f"square{i}{j}", pair["ideal_error_upper"], value)
    check("propagation", f"square{i}{j} threshold", value < invpow(37) < R(1, 10**10))
    square_bounds.append(value)

# Reuse audited695, binding its complete saved artifacts by their hashes
# and checking its inventory sum, without repeating its rational replay.
setup = read("scalar-register-gauss-audit-695.json")
for field, name in (("source_sha256", "scalar-register-gauss-694.py"),
                    ("certificate_sha256", "scalar-register-gauss-694.json"),
                    ("trace_sha256", "scalar-register-gauss-694.trace.jsonl.gz"),
                    ("script_sha256", "scalar-register-gauss-audit-695.py")):
    digest = sha256((HERE / name).read_bytes()).hexdigest()
    checked_files[name] = digest
    check("setup input", field, setup[field] == digest)
check("setup input", "audited result/failures", setup["result"] == "PASS_SOURCE_CORRESPONDENCE_AND_SCALAR_THRESHOLDS"
      and setup["failures"] == [])
inventory = setup["instruction_inventory"]
setup_cost = sum(inventory[k]*2 for k in ("+", "-", "*", "/")) + sum(
    inventory[k] for k in ("literal", "copy", "compare"))
check("setup input", "inventory cost", setup_cost == setup["scalar_work"] == 3290939)
check("setup input", "complete event inventory", sum(inventory.values()) == setup["complete_source_events"] == 1909636)

# Charge one product pair per term and one addition pair per subsequent term.
interior_dot = 14*255*(4*258 + 4*257)
endpoint_dot = 14*255*(4*128 + 4*127)
D_cost = (261-3)*3*2*(768-1)*(2+2)
log_cost = (261-3)*3*2*(512-1)*(2+2)
categories = {
    "audited_C998o_setup": setup_cost,
    "interior_interval_dots_258_nodes": interior_dot,
    "endpoint_interval_dots_128_terms": endpoint_dot,
    "three_D_Horner_pairs_258_nodes": D_cost,
    "three_log_Horner_pairs_258_nodes": log_cost}
work = cert["work"]
check("work", "complete category equality", work["categories"] == categories)
mandatory = sum(categories.values())
check("work", "total", work["mandatory_lower_bound"] == mandatory == 22199915)
check("work", "required/excess", work["required_upper_bound"] == 20000000
      and work["excess"] == mandatory-20000000 == 2199915)
check("work", "prescription fails cap", mandatory > 20000000)
check("scope", "original claims no numerical service", cert["result"] == "PRESCRIPTION_WORK_STOP"
      and cert["failures"] == [] and cert["service_failures"] == [
          "mandatory work exceeds 20000000", "finite interior/primitive/density/Z errors remain unpaid",
          "no square entry or complete residual has been evaluated"])
check("scope", "finite errors remain unpaid", error["finite_interior_and_density_coefficient_error_paid"] is False
      and cert["coefficients"]["exact_Z_computation_paid"] is False)
check("reported checks", "all original299 check records, unique and passing", len(cert["checks"]) == 299
      and len({x["name"] for x in cert["checks"]}) == 299
      and all(set(x) == {"name", "pass"} and x["pass"] is True for x in cert["checks"]))

def dyadic_ceiling(value):
    exponent = value.numerator.bit_length() - value.denominator.bit_length()
    if value > R(2)**exponent:
        exponent += 1
    return exponent


actual_bounds = {"bank": max(errors), "endpoint": endpoint,
                 "moment": epsilon, "ideal square": max(square_bounds)}
dyadic_exponents = {key: dyadic_ceiling(value) for key, value in actual_bounds.items()}
for key, value in actual_bounds.items():
    check("summary", key+" exact dyadic enclosure", value <= R(2)**dyadic_exponents[key])

report = {
    "result": "PASS_SCOPED_CONCEPTUAL_AUDIT" if not failures else "AUDIT_FAILURE",
    "check_counts": dict(counts), "total_checks": sum(counts.values()), "failures": failures,
    "complete_evidence": {"bank_rows": len(errors), "witness_coefficients": int(raw.size),
                          "panels": 3, "ordered_square_bounds": len(pairs),
                          "setup_status": "Audited695 reused with full artifact hash binding; rational transcript not rerun"},
    "bounds": {"bank_actual_maximum_upper": enc(max(errors)), "bank_required": enc(invpow(570)),
               "endpoint_actual_upper": enc(endpoint), "endpoint_required": enc(invpow(149)),
               "moment_actual_upper": enc(epsilon), "moment_required": enc(invpow(64)),
               "square_actual_maximum_upper": enc(max(square_bounds)),
               "square_ideal_bound": enc(invpow(37)), "square_required": enc(R(1, 10**10))},
    "actual_upper_dyadic_exponents": dyadic_exponents,
    "work": {"categories": categories, "actual_mandatory_lower_bound": mandatory,
             "required_upper_bound": 20000000, "excess": mandatory-20000000},
    "unchanged_artifact_sha256": checked_files,
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "qualification": "Exact-field audit plus canonical analytic argument in C998p Section8; no evaluated bank or square, finite service, universal cost bound or original operator/source-contract audit",
}
OUT.write_text(json.dumps(report, indent=2) + "\n")
print("result:", report["result"], "checks:", report["total_checks"], "failures:", failures)
print("verified complete evidence:128 banks,762 coefficients,3 panels,9 square bounds; audited695 input hashes")
print("actual certified upper bounds:", "; ".join(key+"<=2^"+str(value) for key, value in dyadic_exponents.items()))
print("required: bank<2^-570; endpoint<2^-149; moment<2^-64; ideal square<2^-37<1e-10")
print("mandatory scalar work:", mandatory, "required<=20000000; excess:", mandatory-20000000)
print("certificate:", OUT.relative_to(HERE.parent.parent))
raise SystemExit(bool(failures))
