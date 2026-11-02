#!/usr/bin/env python3
"""Independent L588 audit: printed data, scaled recurrences, new cutoff.

Does not import or execute zero_atom_certificate.py and does not solve
its coefficient-fitting system. All arithmetic affecting the verdict is
integer/Fraction arithmetic. Decimal output is display only.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
original = json.loads((ROOT / "zero_atom_certificate.json").read_text())
failures = []


def check(name, condition):
    if not condition:
        failures.append(name)


spec = [("poly", 0), ("poly", 2), ("poly", 4),
        ("cos", 0), ("cos", 2), ("cos", 4), ("sin", 1), ("sin", 3)]
c = [F(20406931943878657), F(-24477043814885880, 7),
     F(2123114775919056, 35), F(-20406931943878656),
     F(8870803683860448, 7), F(-106482224695968, 35),
     F(-7974003096078624), F(3405467682859968, 35)]
q = [F(1), F(0), F(-36), F(0), F(1584, 5), F(0), F(-27456, 35)]
radius = F(1, 2)
last = 52

# Taylor contributions already multiplied by radius**degree.
# cos(u): t_0=1; sin(u): t_1=radius; both have the same recurrence.
cosine = [F(0)] * (last + 1)
sine = [F(0)] * (last + 1)
cosine[0] = F(1)
sine[1] = radius
for sequence, parity in [(cosine, 0), (sine, 1)]:
    for n in range(parity, last - 1, 2):
        sequence[n + 2] = -sequence[n] * radius**2 / ((n + 1) * (n + 2))

parts = []
for coefficient, (kind, shift) in zip(c, spec):
    sequence = [F(0)] * (last + 1)
    if kind == "poly":
        sequence[shift] = coefficient * radius**shift
    else:
        trig = cosine if kind == "cos" else sine
        for n in range(shift, last + 1):
            sequence[n] = coefficient * radius**shift * trig[n - shift]
    parts.append(sequence)
g_scaled = [sum(part[n] for part in parts) for n in range(last + 1)]
p = [sum(q[j] * q[n-j] for j in range(len(q)) if 0 <= n-j < len(q))
     for n in range(2 * len(q) - 1)]
p_scaled = [p[n] * radius**n if n < len(p) else F(0)
            for n in range(last + 1)]
check("all matched degrees 0 through 15", g_scaled[:16] == p_scaled[:16])
check("all odd coefficients vanish", all(g_scaled[n] == 0 for n in range(1, last + 1, 2)))
check("value at zero", g_scaled[0] == 1)

original_finite = sum(abs(g_scaled[n] - p_scaled[n]) for n in range(16, 51))
original_tail_terms = [abs(parts[j][52]) * F(4, 3) for j in range(3, 8)]
original_error = original_finite + sum(original_tail_terms)
printed_error = F(
    53765584323603286414215018684766367271819623359194798028350610463719655842783,
    25082513548667626541684295307238193041433991623155113914197688188928000000000000)
check("full printed E_50", original_error == printed_error)

# Different truncation: retain degrees through 28, then bound each
# shifted trig tail starting at degree 30 separately. Its unshifted
# exponent is at least 26, so every next absolute ratio is <= 1/3024.
cutoff = 28
first_omitted = 30
tail_ratio = F(1, 4 * 27 * 28)
independent_tail_terms = []
for j in range(3, 8):
    kind, shift = spec[j]
    exponent = first_omitted - shift
    check("first omitted parity " + str(j), exponent % 2 == (kind == "sin"))
    check("first omitted exponent " + str(j), exponent >= 26)
    check("tail ratio " + str(j), radius**2 / ((exponent + 1) * (exponent + 2)) <= tail_ratio)
    independent_tail_terms.append(abs(parts[j][first_omitted]) / (1 - tail_ratio))
independent_finite = sum(abs(g_scaled[n] - p_scaled[n]) for n in range(16, cutoff + 1))
independent_error = independent_finite + sum(independent_tail_terms)
check("original error threshold", original_error < F(11, 5000))
check("independent error threshold", independent_error < F(11, 5000) < F(1, 400))

integral = sum(p[n] * radius**n / (n + 1) for n in range(0, len(p), 2))
f0 = F(1) + F(1, 400)
zero_bound = (integral + F(1, 200)) / f0
clipped_bound = zero_bound / 64
gap = F(1, 288) - clipped_bound
check("square integral", integral == F(256, 1225))
check("zero bound", zero_bound == F(4194, 19649) < F(2, 9))
check("clipped bound", clipped_bound == F(2097, 628768) < F(1, 288))
check("strict gap", gap == F(97, 707364) > 0)

# Compare every original field, not a preview or only its PASS label.
expected_original = {
    "status": "PASS", "basis": [kind + ":" + str(shift) for kind, shift in spec],
    "basis_coefficients": [str(x) for x in c],
    "q_coefficients": {str(n): str(x) for n, x in enumerate(q) if x},
    "matched_even_degrees": list(range(0, 16, 2)), "tail_start_degree": 52,
    "uniform_error_exact": str(original_error),
    "uniform_error_proved_upper": "11/5000", "uniform_error_required_upper": "1/400",
    "square_integral": str(integral), "zero_atom_upper": str(zero_bound),
    "zero_atom_required_upper": "2/9", "clipped_mean_upper": str(clipped_bound),
    "clipped_mean_required": "1/288", "strict_gap": str(gap), "failures": []}
check("original key set", set(original) == set(expected_original))
for key, value in expected_original.items():
    check("original field " + key, original.get(key) == value)

certificate = {
    "status": "FAIL" if failures else "PASS",
    "method": "printed coefficients; scaled trig recurrences; independent degree-28 cutoff",
    "original_fields_checked": list(expected_original),
    "basis_coefficients": [str(x) for x in c],
    "square_coefficients": {str(n): str(x) for n, x in enumerate(p) if x},
    "matched_coefficients": [{"degree": n, "g": str(g_scaled[n] / radius**n),
                              "square": str(p_scaled[n] / radius**n)} for n in range(16)],
    "original_replay": {
        "finite_error_terms": {str(n): str(abs(g_scaled[n] - p_scaled[n])) for n in range(16, 51, 2)},
        "tail_majorant_terms": [str(x) for x in original_tail_terms],
        "error_exact": str(original_error)},
    "independent_bound": {
        "cutoff": cutoff, "first_omitted": first_omitted,
        "finite_error": str(independent_finite),
        "tail_ratio": str(tail_ratio),
        "tail_majorant_terms": [str(x) for x in independent_tail_terms],
        "error_exact": str(independent_error),
        "error_required": "11/5000",
        "positive_function_margin": str(F(1, 400) - independent_error)},
    "integral": str(integral), "zero_bound": str(zero_bound),
    "clipped_bound": str(clipped_bound), "clipped_required": "1/288",
    "strict_gap": str(gap), "failures": failures}
destination = ROOT / "audit_zero_atom_certificate.json"
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(certificate["status"] + ": all 16 original fields, degree matches, and independent complete-tail check")
print("Independent error =", independent_error, "< required 11/5000 < 1/400")
print("Zero mass <=", zero_bound, "< required 2/9; clipped mean <=", clipped_bound, "< required 1/288")
print("Strict gap =", gap, "; failures:", failures)
print("Full certificate:", destination)
raise SystemExit(bool(failures))
