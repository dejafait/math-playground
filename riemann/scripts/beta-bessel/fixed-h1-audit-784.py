"""Independent exact audit of the already fixed C040c H_1 certificate."""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial, prod
from pathlib import Path
import json


def encode(value):
    return {"numerator": value.numerator, "denominator": value.denominator}


def decode(value):
    return Q(value["numerator"], value["denominator"])


def pochhammer(a, n):
    return prod((a + j for j in range(n)), start=Q(1))


source = Path(__file__).with_name("fixed-h1-782.json")
old = json.loads(source.read_text())
# Finite products, independent of the producer's coefficient recurrences.
gamma = [pochhammer(Q(3, 2), n) /
         (4**n * pochhammer(Q(1), n) * pochhammer(Q(100), n))
         for n in range(5)]
e = [gamma[n] / factorial(n) for n in range(5)]
_, e1, e2, e3, e4 = e
# Explicit expansion of -k[w^k]log(1-e1*w+e2*w^2-e3*w^3+e4*w^4).
# No Newton recurrence or polynomial-power loop is reused.
S = [e1,
     e1**2 - 2*e2,
     e1**3 - 3*e1*e2 + 3*e3,
     e1**4 - 4*e1**2*e2 + 2*e2**2 + 4*e1*e3 - 4*e4]
log_coefficients = [-value / k for k, value in enumerate(S, start=1)]
S1, S2, S3, S4 = S
H = [[S2, S3], [S3, S4]]
determinant = S2*S4 - S3*S3
v0, v1 = S3, -S2
quadratic_form = S2*v0*v0 + 2*S3*v0*v1 + S4*v1*v1

checks = {
    "normalization": gamma[0] == e[0] == 1,
    "complete_gamma_match": gamma == list(map(decode, old["gamma_0_to_4"])),
    "complete_e_match": e == list(map(decode, old["e_0_to_4"])),
    "complete_S_match": S == list(map(decode, old["S_1_to_4"])),
    "complete_log_match": log_coefficients == list(map(decode, old["log_coefficients_1_to_4"])),
    "complete_H_match": H == [list(map(decode, row)) for row in old["H_1"]],
    "determinant_match": determinant == decode(old["determinant"]),
    "threshold_zero": decode(old["required_determinant_upper_threshold"]) == 0,
    "witness_match": [v0, v1] == list(map(decode, old["witness"])),
    "form_match": quadratic_form == decode(old["witness_quadratic_form"]),
    "recorded_recurrence_residuals_zero": list(map(decode, old["recurrence_residuals"])) == [Q(0)]*4,
    "recorded_formal_log_residuals_zero": list(map(decode, old["formal_log_residuals"])) == [Q(0)]*4,
    "recorded_checks_pass": len(old["checks"]) == 8 and all(old["checks"].values()),
    "recorded_failures_empty": old["failures"] == [],
    "S2_positive": S2 > 0,
    "determinant_negative": determinant < 0,
    "witness_nonzero": v1 != 0,
    "quadratic_form_identity": quadratic_form == S2*determinant,
    "quadratic_form_negative": quadratic_form < 0,
}
certificate = {
    "target": "C040c fixed H_1 arithmetic audit; no additional model or minor",
    "arithmetic": "exact rational finite products and explicit degree-four log formulas",
    "input_certificate": "scripts/beta-bessel/fixed-h1-782.json",
    "input_sha256": sha256(source.read_bytes()).hexdigest(),
    "independent_gamma_0_to_4": list(map(encode, gamma)),
    "independent_e_0_to_4": list(map(encode, e)),
    "independent_S_1_to_4": list(map(encode, S)),
    "independent_log_coefficients_1_to_4": list(map(encode, log_coefficients)),
    "independent_H_1": [[encode(x) for x in row] for row in H],
    "determinant": encode(determinant),
    "required_strict_upper_threshold": encode(Q(0)),
    "witness": [encode(v0), encode(v1)],
    "quadratic_form": encode(quadratic_form),
    "checks": checks,
    "failures": [key for key, passed in checks.items() if not passed],
    "scope_limit": "Arithmetic only; the analytical joint-premise audit is in C040c.",
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"det(H_1)={determinant}; required <0; S2={S2}; required >0")
print(f"quadratic form={quadratic_form}; required <0")
print(f"checks={len(checks)}; failures={certificate['failures']}; certificate={output}")
if certificate["failures"]:
    raise SystemExit(1)
