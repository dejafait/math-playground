#!/usr/bin/env python3
"""Independent exact arithmetic replay for C645k's conceptual audit.

Compare the literal canonical table and every stored rational row with
the combined positive formula (25), rather than generating replacement
floor entries. Analytic validity is checked in the canonical proof.
"""

from fractions import Fraction as F
import json
from pathlib import Path
import re


def rat(q):
    return {"numerator": q.numerator, "denominator": q.denominator}


def read_rat(q):
    return F(q["numerator"], q["denominator"])


root = Path(__file__).resolve().parents[2]
original = json.loads((Path(__file__).with_name(
    "fixed-third-counterfamily-check.json")).read_text())
proof = (root / "lemmas/C645k-fixed-third-circle-hankel-counterfamily.md").read_text()
entries = []
for line in proof.splitlines():
    if re.match(r"\| \d+--\d+ \|", line):
        entries.extend(int(v.strip()) for v in line.split("|")[2].split(","))

R, d, u, r, s, eta = F(11, 8), F(5, 4), F(523, 400), F(23, 400), F(67, 1000), F(1, 100)
checks = {}
failures = []


def check(name, actual, required, passed):
    checks[name] = {"actual": actual, "required": required, "passed": bool(passed)}
    if not passed:
        failures.append(name)


check("literal_table_length", len(entries), 64, len(entries) == 64)
check("stored_table_length", len(original["derivative_lower_table"]), 64,
      len(original["derivative_lower_table"]) == 64)
rows = []
for k, b in enumerate(entries, 1):
    t = F(k, 64)
    # Independent expression: the positive combined numerator in (25).
    value = u * (R**4 - t**4) / ((u*u + t*t) * (R**4 + u*u*t*t))
    cross = 10000 * value.numerator - b * value.denominator
    saved = original["derivative_lower_table"][k-1]
    flags = {
        "literal_lower_bound": cross >= 0,
        "saved_k": saved["k"] == k,
        "saved_t": read_rat(saved["t"]) == t,
        "saved_value": read_rat(saved["value"]) == value,
        "saved_integer": saved["lower_integer"] == b,
        "saved_scale": saved["rounding_scale"] == 10000,
        "saved_difference": read_rat(saved["difference"]) == value - F(b, 10000),
        "saved_pass": saved["passed"] is True,
    }
    rows.append({"k": k, "b": b, "value": rat(value),
                 "integer_cross_product": cross, "checks": flags})
    for name, passed in flags.items():
        if not passed:
            failures.append(f"table_{k}_{name}")

table_average = F(sum(entries), 640000)
check("literal_integer_sum", sum(entries), 353938, sum(entries) == 353938)
check("right_rectangle_average", str(table_average), "> 11/20", table_average > F(11, 20))
check("anchor", str(u-r), str(d), u-r == d)
check("pole_clearance", str(u+r), str(R-eta), u+r == R-eta)
check("auxiliary_disk_margin", str(R-u-s), "1/2000 > 0", R-u-s == F(1, 2000))
check("auxiliary_circle_encloses_roots", str(s-r), "> 0", s > r > 0)
check("disk_denominator_lower_bounds", [str(u-s), str(R*R-s)], "both > 0",
      u-s > 0 and R*R-s > 0)
check("product_monotonicity_parameters", [str(d), str(R*R-u)], "d>1 and R^2-u>0",
      d > 1 and R*R > u)
D0 = (u-s)*(R*R-s)
gamma, K = s*(R*R-F(1, 3))/D0, s/(2*D0)
check("gamma", str(gamma), "5008250/108585927 < 7/150",
      gamma == F(5008250, 108585927) and gamma < F(7, 150))
check("K", str(K), "536000/36195309 < 1/50",
      K == F(536000, 36195309) and K < F(1, 50))
check("gamma_cross_product", 7*gamma.denominator-150*gamma.numerator, 8863989,
      7*gamma.denominator-150*gamma.numerator == 8863989)
check("K_cross_product", K.denominator-50*K.numerator, 9395309,
      K.denominator-50*K.numerator == 9395309)
check("radius_ratio", str(r/s), "115/134", r/s == F(115, 134))
check("m8_geometric_threshold", str(8*(1-r/s)), "76/67 > 1", 8*(1-r/s) == F(76, 67))
error_rate = (1-r/s)/3-F(7, 150)
check("quadrature_error_rate", str(error_rate), "1/1675 > 0", error_rate == F(1, 1675))
prefactor = (1/(R-u)+8000)/3
check("operator_prefactor", str(prefactor), "< 2700", prefactor < 2700)
rate = r*F(11, 20)
check("product_rate", str(rate), "253/8000 > 1/32", rate == F(253, 8000) and rate > F(1, 32))
check("strict_rate_margin", str(rate-F(1, 32)), "3/8000 > 0", rate-F(1, 32) == F(3, 8000))

expected_bounds = {
    "gamma": gamma, "gamma_required_upper": F(7, 150), "K": K,
    "K_required_upper": F(1, 50), "right_sum_lower": table_average,
    "mean_required_lower": F(11, 20), "beta": rate, "target_rate": F(1, 32),
    "rate_margin": rate-F(1, 32), "quadrature_error_rate": error_rate,
}
for name, value in expected_bounds.items():
    saved = read_rat(original["bounds"][name])
    check("stored_bound_"+name, str(saved), str(value), saved == value)
check("stored_integer_sum", original["bounds"]["lower_integer_sum"], sum(entries),
      original["bounds"]["lower_integer_sum"] == sum(entries))
check("stored_literal_integers", original["lower_integers"], entries,
      original["lower_integers"] == entries)
check("original_checks", original["checks"], "all true", all(original["checks"].values()))
check("original_failures", original["failures"], [], original["failures"] == [])

summary = {
    "passed": not failures, "failures": failures, "table_rows_checked": len(rows),
    "table_checks_per_row": 8, "mean_lower": str(table_average), "mean_required": ">11/20",
    "gamma": str(gamma), "gamma_required": "<7/150", "K": str(K), "K_required": "<1/50",
    "operator_prefactor": str(prefactor), "prefactor_required": "<2700",
    "product_rate": str(rate), "required_rate": ">1/32",
    "strict_rate_margin": str(rate-F(1, 32)), "quadrature_error_rate": str(error_rate),
}
certificate = {"purpose": "Independent arithmetic audit; analytic proof remains canonical in C645k.",
               "summary": summary, "checks": checks, "table": rows}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Passed: {summary['passed']}; failures: {failures}; literal rows checked: {len(rows)}")
print(f"Mean: {table_average} > 11/20; gamma: {gamma} < 7/150; K: {K} < 1/50")
print(f"Prefactor: {prefactor} < 2700; rate: {rate} > 1/32; margin: {rate-F(1,32)}")
print(f"Quadrature error rate: {error_rate} > 0")
print(f"Certificate: {output}")
raise SystemExit(0 if not failures else 1)
