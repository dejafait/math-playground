#!/usr/bin/env python3
"""Independent exact contraction of the single approved L568 certificate.

No import of the first-variation program, no new probes, no quadrature.
Reuses C567a's fully audited coefficient source after checking its hash.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / "l568-certificate-audit.json"
EXPECTED_HASH = "431d77c0fe35350ae5730c2fd5cee4cfe5fd12ae9fd130bd001b168e78ad7e0b"
failures = []
checks = {}


def require(name, condition):
    checks[name] = bool(condition)
    if not condition:
        failures.append(name)


def interval(value):
    return tuple(Q(x) for x in value)


def encode(value):
    return [str(x) for x in value]


def inside(value, lower, upper):
    return Q(lower) <= value[0] <= value[1] <= Q(upper)


def signed_sum(coefficients, multipliers, first, last):
    """Collect the positive and negative multiplier sums separately."""
    positive = [(coefficients[n], multipliers[n]) for n in range(first, last + 1)
                if multipliers[n] >= 0]
    negative = [(coefficients[n], multipliers[n]) for n in range(first, last + 1)
                if multipliers[n] < 0]
    low = (sum((c[0] * v for c, v in positive), Q(0))
           + sum((c[1] * v for c, v in negative), Q(0)))
    high = (sum((c[1] * v for c, v in positive), Q(0))
            + sum((c[0] * v for c, v in negative), Q(0)))
    return low, high


def product(a, b):
    """Center/radius corners, retaining their true asymmetric extrema."""
    ca, ra = (a[0] + a[1]) / 2, (a[1] - a[0]) / 2
    cb, rb = (b[0] + b[1]) / 2, (b[1] - b[0]) / 2
    offsets = [s * ra * cb + t * rb * ca + s * t * ra * rb
               for s in (-1, 1) for t in (-1, 1)]
    return ca * cb + min(offsets), ca * cb + max(offsets)


def scaled(a, c):
    return tuple(sorted((c * a[0], c * a[1])))


def main():
    source_path = HERE / "global-dual-pairing-certificate.json"
    comparison_path = HERE / "c567a-audit-replay-comparison.json"
    original_path = HERE / "first-variation-certificate.json"
    raw = source_path.read_bytes()
    source = json.loads(raw)
    comparison = json.loads(comparison_path.read_bytes())
    original = json.loads(original_path.read_bytes())
    digest = sha256(raw).hexdigest()
    require("audited_source_hash", digest == EXPECTED_HASH == comparison["retained_sha256"])
    require("source_pass", source["status"] == "PASS" and source["failures"] == [])
    require("comparison_pass", comparison["status"] == "PASS" and comparison["failures"] == [])
    require("comparison_all_fields", all(comparison["all_mathematical_fields_equal"].values()))
    require("comparison_fresh_nodes", comparison["fresh_node_values_reused"] is False)
    require("source_parameters", source["parameters"] == dict(
        bits=2048, exp_order=320, degree=256, panels=128,
        length="1/32", limit=4, theta_terms=24))
    require("original_source_hash", original["source_sha256"] == digest)
    require("original_audit_hash", original["source_audit_sha256"] ==
            sha256(comparison_path.read_bytes()).hexdigest())
    require("single_approved_point", original["parameters"] == dict(
        T=1, N=64, M=256, derivative_orders=[0, 1, 2]) and
        original["evaluated_probes"] == 1 and len(original["probes"]) == 1)
    row = original["probes"][0]
    require("point_is_one", Q(row["t"]) == 1)
    require("original_no_failures", original["failures"] == [] and
            original["status"] == "NEGATIVE_WITNESS")
    arrays = [source["integral_totals_fixedpoint"], source["remainders"],
              source["moments"], source["coefficients_b_even"],
              original["coefficients_b_even"]]
    require("all_coefficient_array_lengths", all(len(v) == 257 for v in arrays))
    require("weight_count", len(source["weights"]) == 257)
    norm = sum((abs(Q(w)) for w in source["weights"]), Q(0))
    require("absolute_weight_norm", norm == Q(source["absolute_weight_norm"]))

    coefficients, coefficient_evidence = [], []
    for n in range(257):
        lo, hi = (Q(int(x), 1 << 2048) for x in source["integral_totals_fixedpoint"][n])
        require(f"raw_interval_order_{n}", lo <= hi)
        interpolation = Q(8 * (1 << 60) * 9 ** (2*n), 2 ** (2*n) * 16 ** 257)
        theta = Q(512 * 3 ** 18 * 4 ** (2*n), 1 << 1849) * norm
        spatial = Q(19200 * 3 ** 18 * 4 ** (2*n), 1 << 3072)
        errors = dict(interpolation=interpolation, theta=theta, spatial=spatial)
        require(f"all_three_coefficient_errors_{n}",
                all(Q(source["remainders"][n][k]) == v for k, v in errors.items()))
        moment = (2*lo - interpolation - theta, 2*hi + interpolation + theta + spatial)
        denominator = (1 << (2*n)) * factorial(2*n)
        coefficient = tuple(v / denominator for v in moment)
        require(f"full_moment_{n}", moment == interval(source["moments"][n]))
        require(f"full_coefficient_{n}", coefficient == interval(source["coefficients_b_even"][n])
                == interval(original["coefficients_b_even"][n]))
        require(f"coefficient_order_{n}", coefficient[0] <= coefficient[1])
        coefficients.append(coefficient)
        coefficient_evidence.append(dict(n=n, errors={k: str(v) for k, v in errors.items()},
                                         moment=encode(moment), coefficient=encode(coefficient)))

    # Independent integer finite formula, not recurrence as primary evaluation.
    hermite = [sum((-1)**r * comb(m, 2*r) * (factorial(2*r) // factorial(r))
                   * 2**(m-2*r) for r in range(m//2 + 1)) for m in range(513)]
    require("hermite_initial_values", hermite[:2] == [1, 2])
    require("all_hermite_recurrences", all(hermite[m+1] == 2*hermite[m] - 2*m*hermite[m-1]
                                          for m in range(1, 512)))
    require("all_original_hermite_values", len(row["hermite_values"]) == 513 and
            hermite == [Q(x) for x in row["hermite_values"]])
    multipliers = [[(-1)**n * hermite[2*n] for n in range(257)],
                   [(-1)**n * 4*n * hermite[2*n-1] if n else 0 for n in range(257)],
                   [(-1)**n * 8*n*(2*n-1) * hermite[2*n-2] if n else 0 for n in range(257)]]
    p = [signed_sum(coefficients, v, 0, 64) for v in multipliers]
    finite_r = [signed_sum(coefficients, v, 65, 256) for v in multipliers]

    # The exact sum follows by a geometric-series shift, not a rounded display.
    q = Q(1, 5)
    tail_series = q**257 * (Q(257)/(1-q) + q/(1-q)**2)
    require("exact_derivative_majorant_sum", tail_series == Q(1029, 16 * 5**256))
    error = 80000 * 9 * tail_series
    require("infinite_tail_allowance", error == Q(45000 * 1029, 5**256)
            == Q(row["infinite_tail_error_each_derivative"]))
    require("tail_below_stated_bound", 0 < error < Q("5.36176e-172"))
    r = [(lo-error, hi+error) for lo, hi in finite_r]
    for j in range(3):
        require(f"finite_P_jet_{j}", p[j] == interval(row["P_jets"][j]))
        require(f"finite_R_jet_{j}", finite_r[j] == interval(row["finite_R_jets"][j]))
        require(f"complete_R_jet_{j}", r[j] == interval(row["R_jets"][j]))

    coarse_p = [("0.485757", "0.485758"), ("-0.0224831", "-0.0224830"),
                ("-0.0215153", "-0.0215152")]
    coarse_r = [("-2.07165e-130", "-2.07164e-130"), ("1.35763e-129", "1.35764e-129"),
                ("5.65835e-128", "5.65836e-128")]
    for j in range(3):
        require(f"lemma_P_table_{j}", inside(p[j], *coarse_p[j]))
        require(f"lemma_R_table_{j}", inside(r[j], *coarse_r[j]))
    terms = [scaled(product(p[1], r[1]), 2), scaled(product(p[0], r[2]), -1),
             scaled(product(r[0], p[2]), -1)]
    for j, value in enumerate(terms):
        require(f"complete_signed_product_{j}", value == interval(row["B_terms"][j]))
        require(f"individual_product_negative_{j}", value[1] < 0)
    b = tuple(sum((v[k] for v in terms), Q(0)) for k in range(2))
    require("complete_B_matches", b == interval(row["B"]))
    require("complete_B_strictly_negative", b[0] <= b[1] < 0)
    require("complete_B_inside_lemma_enclosure", inside(b, "-2.75514e-128", "-2.75513e-128"))
    require("original_coarse_B", row["coarse_B"] == ["-275514e-133", "-275513e-133"])

    result = dict(status="PASS" if not failures else "FAIL", failures=failures,
                  approved_point=dict(T=1, t=1, N=64, M=256, derivatives=[0, 1, 2]),
                  required="Complete upper bound strictly below 0; all coefficient and tail errors included.",
                  source_sha256=digest, comparison_sha256=sha256(comparison_path.read_bytes()).hexdigest(),
                  original_certificate_sha256=sha256(original_path.read_bytes()).hexdigest(),
                  checks=checks, coefficient_evidence=coefficient_evidence,
                  hermite_integer_finite_formula=hermite, signed_derivative_multipliers=multipliers,
                  P_jets=[encode(v) for v in p], finite_R_jets=[encode(v) for v in finite_r],
                  infinite_tail_series=str(tail_series), infinite_tail_error_each_derivative=str(error),
                  R_jets=[encode(v) for v in r], B_terms=[encode(v) for v in terms], B=encode(b),
                  proven_B_enclosure=["-2.75514e-128", "-2.75513e-128"],
                  method="Independent finite integer Hermite formula, sign-separated jet contractions, centered-corner exact products.",
                  limitations=["Audited C567a coefficients reused; no fresh theta-node replay.",
                               "L564 analytic inputs reused and their tail applicability checked.",
                               "Single first-variation obstruction, no Xi discriminant or RH conclusion."])
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print("status", result["status"], "checks", len(checks), "coefficients", len(coefficients))
    print("complete B enclosure", result["proven_B_enclosure"], "required upper bound < 0")
    print("three infinite-tail allowances each < 5.36176e-172; all signed products negative:",
          all(v[1] < 0 for v in terms))
    print("failures", failures, "certificate", OUT.relative_to(ROOT))
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        OUT.write_text(json.dumps(dict(status="ERROR", checks=checks, failures=failures,
                                       error=repr(exc)), indent=2) + "\n")
        print("ERROR", repr(exc), "certificate", OUT.relative_to(ROOT))
        raise
