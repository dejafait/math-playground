"""Independent exact finite-evidence audit of C033z's rounding1810.

No original evaluator is imported or executed. Universal containment and
cost interpretation are audited in canonical C033z, not proved by cases.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
checks, hashes = {}, {}


def check(name, condition):
    checks[name] = bool(condition)


def load(name):
    path = HERE / name
    raw = path.read_bytes()
    hashes[name] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


def main():
    old = load("direct_positive_real_ihat_rounding_1810.json")
    inherited = load("direct_positive_real_audit_1806.json")
    eta = Q(1, 2**32)
    check("schedule:all_fields", old["schedule"] == {
        "block_size": 4, "blocks": 56, "bisections": 43,
        "initial_lo": -2048, "initial_hi": 2048,
        "checkpoint_radius": str(eta), "grid_denominator_divides": 2**32})
    check("schedule:width", Q(4096, 2**43) == 2*eta)
    check("blocks:complete", len(old["blocks"]) == 56)
    block_evidence = []
    for r, row in enumerate(old["blocks"], 1):
        pre = 4*r*Q(7)+(r-1)*eta
        post = 4*r*Q(7)+r*eta
        expected = {"block": r, "summands": 4*r,
                    "input_abs_upper": str(pre), "output_abs_upper": str(post),
                    "error_from_exact_prefix_upper": str(r*eta),
                    "cumulative_extra_operations": 1+r*(43*3+2)}
        check(f"block{r}:complete_evidence", row == expected)
        check(f"block{r}:range_and_numerator", pre < 2048 and post < 2048
              and post*2**32 < 2**43)
        check(f"block{r}:error_recurrence", r*eta == (r-1)*eta+eta)
        block_evidence.append(expected)

    # Independent closed-form cell selection, including the midpoint tie.
    # Integer division here belongs to audit work, never the evaluator ledger.
    values = [Q(-2048), Q(2048), Q(0), Q(-1568), Q(1568),
              Q(-1, 3), Q(1, 3), Q(2048)-Q(1, 2**40)]
    check("cases:complete", len(old["boundary_cases"]) == len(values))
    cases = []
    spacing = 2*eta
    for i, (value, row) in enumerate(zip(values, old["boundary_cases"])):
        cell_coordinate = (value+2048)/spacing
        ceil_coordinate = -((-cell_coordinate.numerator)//cell_coordinate.denominator)
        cell = max(0, ceil_coordinate-1)
        lo = Q(-2048)+cell*spacing
        hi = lo+spacing
        midpoint = (lo+hi)/2
        expected = {"input": str(value), "output": str(midpoint),
                    "lo": str(lo), "hi": str(hi),
                    "error": str(abs(midpoint-value)), "operations": 131}
        check(f"case{i}:closed_form_match", row == expected)
        check(f"case{i}:containment_error_grid", lo <= value <= hi
              and abs(midpoint-value) <= eta
              and (midpoint*2**32).denominator == 1)
        cases.append(expected)

    check("inherited:audit_pass", inherited["status"] == "FINITE_EVIDENCE_PASS"
          and not inherited["failures"] and all(inherited["checks"].values()))
    epsF = Q(inherited["bounds"]["profile_error"])
    epsg = Q(inherited["bounds"]["outer_g_error"])
    epsB = Q(inherited["bounds"]["exponent_arithmetic_error"])
    final_error = Q(128*3, factorial(21))
    check("inherited:bounds", epsF < Q(1, 2**22) and epsg < Q(1, 2**35)
          and epsB < Q(1, 2**17)
          and final_error == Q(inherited["bounds"]["final_exp_error"]))
    # Telescope exact coefficient*g first, then computed g times weight error.
    weight_sum_upper = Q(13)+20*epsg+260*4*Q(1, 2**68)
    check("propagation:computed_weights", weight_sum_upper < 14)
    error_I = 56*eta
    error_K = error_I/6
    extra_B = 14*error_K
    beta = Q(1, 2**17)+extra_B
    profile_upper = Q(25, 4)+Q(1, 2**22)+error_K
    radius = Q(25, 16384)+beta+final_error
    bounds = {"Ihat_extra": error_I, "K_extra_strict_upper": error_K,
              "exponent_extra_strict_upper": extra_B,
              "exponent_total_strict_upper": beta, "final_exp_upper": final_error,
              "scalar_radius_strict_upper": radius,
              "computed_profile_strict_upper": profile_upper}
    for key, value in bounds.items():
        check("stored_bound:"+key, Q(old["bounds"][key]) == value)
    check("allowances:both", beta < Q(1, 1024) and final_error < Q(1, 1024))
    check("allowances:stored_thresholds", old["bounds"]["exponent_required"] == "1/1024"
          and old["bounds"]["final_exp_required"] == "1/1024"
          and old["bounds"]["scalar_required"] == "1/256")
    check("range:profiles_exponents", profile_upper < 7
          and 13*7+Q(25, 16384) < 128 and 14*7 < 128)
    check("radius:strict_display_and_requirement", radius < Q(767, 500000) < Q(1, 256))
    scalar_evidence = []
    for s in (1, 2):
        for sigma in ("1", "3/2", "2", "residual"):
            scalar_evidence.append({"s": s, "width": sigma,
                "compact_width": "1" if sigma == "residual" else sigma,
                "additional_exponent_strict_upper": str(extra_B),
                "scalar_radius_strict_upper": str(radius),
                "analytic_tail": "separate residual restriction" if sigma == "residual"
                                 else "full width law"})
    # Unchanged samples retain their weighted product and original addition.
    base = inherited["cost"]["total"]
    overhead = 56*(43*(1+1+1)+(1+1))+1
    operations = {"inherited_full_upper": base, "shared_negation": 1,
        "per_checkpoint": 131, "additional_upper": overhead,
        "full_upper": base+overhead, "required_cap": 1000000,
        "remaining_slack": 1000000-base-overhead,
        "runtime_error_tracking_operations": 0,
        "complete_evaluator_execution_count_verified": False}
    check("cost:all_fields", old["operations"] == operations)
    check("cost:cap", base == 989767 and base+overhead == 997104 <= 10**6)
    # Do not treat the original booleans as the independent evidence above.
    check("original:reported_checks", old["check_count"] == len(old["checks"]) == 161
          and not old["failures"] and all(old["checks"].values()))
    failures = [name for name, passed in checks.items() if not passed]
    report = {"status": "ROUNDING_AUDIT_PASS" if not failures else "FAILED",
        "inputs_sha256": hashes, "blocks": block_evidence, "cases": cases,
        "bounds": {**{key: str(value) for key, value in bounds.items()},
                   "computed_weight_sum_strict_upper": str(weight_sum_upper)},
        "all_eight_scalars": scalar_evidence, "operations": operations,
        "checks": checks, "check_count": len(checks), "failures": failures,
        "limits": ["Universal proof and inherited hypotheses audited in canonical C033z",
                   "No actual Ihat sample, scalar or completed-run operation count",
                   "Inherited1806 ledger; no new source-wide or zero-data verification",
                   "No bit-time, interpolation, TV, signed-height or Xi conclusion"]}
    path = HERE / "direct_positive_real_ihat_audit_1812.json"
    path.write_text(json.dumps(report, indent=2)+"\n")
    print(f"{report['status']}: {len(checks)} exact checks; failures={failures}")
    print("Complete evidence: 56 blocks, 8 boundary cases, 8 scalar uses; scalars evaluated=0")
    print(f"Exponent {float(beta):.12g} < 1/1024; final exp {float(final_error):.12g} < 1/1024")
    print(f"Radius {float(radius):.12g} < 1/256; ledger {base+overhead} <= 1000000; slack {1000000-base-overhead}")
    print(f"Certificate: {path.relative_to(HERE.parent.parent)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
