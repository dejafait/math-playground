"""Exact contract checks for C033z's Ihat-only block rounding1810.

No Ihat samples, profiles or scalars are evaluated. Certificate arithmetic
is outside the evaluator ledger; that ledger is justified in C033z's proof.
Boundary cases supplement, and do not replace, the universal interval proof.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent
OUT = HERE / "direct_positive_real_ihat_rounding_1810.json"


def checkpoint(value):
    lo, hi = Q(-2048), Q(2048)
    operations = 0
    for _ in range(43):
        mid = (lo + hi) / 2
        operations += 2
        upper_half = value > mid
        operations += 1
        if upper_half:
            lo = mid
        else:
            hi = mid
    result = (lo + hi) / 2
    operations += 2
    return result, lo, hi, operations


def main():
    checks = {}

    def check(name, value):
        checks[name] = bool(value)

    eta = Q(1, 2**32)
    error_I = 56 * eta
    error_K = error_I / 6
    added_exponent = 14 * error_K
    old_exponent_upper = Q(1, 2**17)
    exponent_upper = old_exponent_upper + added_exponent
    final_exp_upper = Q(384, factorial(21))
    scalar_upper = Q(25, 16384) + exponent_upper + final_exp_upper
    overhead = 1 + 56 * (43 * 3 + 2)
    full_upper = 989767 + overhead
    check("radius_after43_bisections", Q(4096, 2**44) == eta)
    check("checkpoint_dyadic_grid", Q(4096, 2**44) == Q(1, 2**32))
    check("sample_partition", 56 * 4 == 224)
    check("full_operation_cap", full_upper <= 1000000)
    check("exponent_allowance", exponent_upper < Q(1, 1024))
    check("final_exp_allowance", final_exp_upper < Q(1, 1024))
    check("scalar_radius", scalar_upper < Q(1, 256))
    check("scalar_display_bound", scalar_upper < Q(767, 500000))
    # Uniform known bound for every original computed profile, with slack.
    profile_upper = Q(25, 4) + Q(1, 2**22) + error_K
    check("rounded_profile_range", profile_upper < 7)
    blocks = []
    for r in range(1, 57):
        input_upper = Q(28*r) + (r-1)*eta
        output_upper = Q(28*r) + r*eta
        check(f"block{r}:input_range", input_upper < 2048)
        check(f"block{r}:output_range", output_upper < 2048)
        blocks.append({"block": r, "summands": 4*r,
                       "input_abs_upper": str(input_upper),
                       "output_abs_upper": str(output_upper),
                       "error_from_exact_prefix_upper": str(r*eta),
                       "cumulative_extra_operations": 1+r*131})
    cases = []
    for i, value in enumerate((Q(-2048), Q(2048), Q(0), Q(-1568),
                               Q(1568), Q(-1, 3), Q(1, 3),
                               Q(2048)-Q(1, 2**40))):
        result, lo, hi, operations = checkpoint(value)
        check(f"case{i}:containment", lo <= value <= hi)
        check(f"case{i}:width", hi-lo == 2*eta)
        check(f"case{i}:error", abs(result-value) <= eta)
        check(f"case{i}:grid", (result*2**32).denominator == 1)
        check(f"case{i}:operations", operations == 131)
        cases.append({"input": str(value), "output": str(result),
                      "lo": str(lo), "hi": str(hi),
                      "error": str(abs(result-value)), "operations": operations})
    failures = [name for name, ok in checks.items() if not ok]
    report = {
        "status": "CONTRACT_CHECKS_PASS" if not failures else "FAILED",
        "assessment": "drafts/literature/2026-11-19-direct-positive-real-ihat-rounding-review-1809.md",
        "canonical_proof": "lemmas/C033z-direct-positive-real-stable-inner-arithmetic.md",
        "scope": "Ihat accumulation only; all224 samples remain exact",
        "schedule": {"block_size": 4, "blocks": 56, "bisections": 43,
                     "initial_lo": -2048, "initial_hi": 2048,
                     "checkpoint_radius": str(eta), "grid_denominator_divides": 2**32},
        "bounds": {"Ihat_extra": str(error_I), "K_extra_strict_upper": str(error_K),
                   "exponent_extra_strict_upper": str(added_exponent),
                   "exponent_total_strict_upper": str(exponent_upper),
                   "exponent_required": "1/1024", "final_exp_upper": str(final_exp_upper),
                   "final_exp_required": "1/1024", "scalar_radius_strict_upper": str(scalar_upper),
                   "scalar_required": "1/256", "computed_profile_strict_upper": str(profile_upper)},
        "operations": {"inherited_full_upper": 989767, "shared_negation": 1,
                       "per_checkpoint": 131, "additional_upper": overhead,
                       "full_upper": full_upper, "required_cap": 1000000,
                       "remaining_slack": 1000000-full_upper,
                       "runtime_error_tracking_operations": 0,
                       "complete_evaluator_execution_count_verified": False},
        "blocks": blocks, "boundary_cases": cases, "checks": checks,
        "check_count": len(checks), "failures": failures,
        "limits": ["Universal correctness is proved in canonical C033z, not by boundary tests",
                   "Full total inherits the audited989767 construction ledger",
                   "No bit-time bound or actual scalar enclosure",
                   "Other denominators, sources, zero-data and law assumptions remain qualified"]}
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"{report['status']}: {len(checks)} exact checks; failures={failures}")
    print(f"Operations {full_upper} <= 1000000; extra {overhead}; slack {1000000-full_upper}")
    print(f"Exponent bound {float(exponent_upper):.12g} < 1/1024; final exp {float(final_exp_upper):.12g} < 1/1024")
    print(f"Scalar radius bound {float(scalar_upper):.12g} < 1/256; scalars evaluated=0")
    print(f"Certificate: {OUT.relative_to(HERE.parent.parent)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
