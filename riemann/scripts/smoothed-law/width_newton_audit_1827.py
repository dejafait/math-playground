"""Independent exact replay for the approved C033z extension1825 audit.

Does not import or execute the original constructor. The continuum proof
and the source-theorem hypothesis audit remain in C033z. No scalar/profile
execution, rounded algorithm, global ledger or bit-cost theorem is tested.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json


def enc(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def dec(x):
    return F(int(x["numerator"]), int(x["denominator"]))


def main():
    source = Path(__file__).with_name("width_newton_1825.json")
    source_bytes = source.read_bytes()
    old = json.loads(source_bytes)
    checks = {}

    def check(name, value):
        checks[name] = bool(value)

    eps, perturb, required = F(1, 2**65), F(1, 2**123), F(1, 2**60)
    c, bounds = F(24, 11), [F(5, 16)]
    for n in range(1, 8):
        bounds.append(c*bounds[-1]*bounds[-1])
        check(f"envelope_invariant_e{n+1}", 0 < bounds[-1] < bounds[-2] <= F(5, 16))
        check(f"envelope_closed_form_e{n+1}",
              bounds[-1] == F(11, 24)*F(15, 22)**(2**n))
    check("all_eight_saved_bounds_recomputed",
          [dec(x) for x in old["relative_error_bounds_e1_to_e8"]] == bounds)
    check("first_step_endpoint", (3*F(1, 2)-F(1, 2)**3)/2 == F(11, 16))
    check("decisive_square", F(225, 484) < F(1, 2))
    check("strict_newton_bound", bounds[-1] < F(11, 24)*F(1, 2**64) < eps)
    check("complete_error", eps+perturb < F(1, 2**64) < required)
    check("saved_error_fields", dec(old["absolute_error_bound_required"]) == required
          and dec(old["absolute_error_bound_proved"]) == eps+perturb)

    # Reconstruct (14)-(16), using the already audited root radius (11).
    eta = F(1, 2**168)
    log_tail = F(9, 4*129*3**129)
    v_error = 30*log_tail+F(7, 10)*eta
    e_error = F(96*3**21, factorial(41))+3**21*v_error
    check("log_tail_lt_2^-200", log_tail < F(1, 2**200))
    check("v_error_lt_2^-160", v_error < F(1, 2**160))
    check("E_error_lt_2^-120", e_error < F(1, 2**120))
    check("width_perturbation_lt_2^-122", e_error/4 < F(1, 2**122))
    check("inverse_root_input_error_lt_2^-123", e_error/8 < perturb)
    check("width_interface_upper", 2+2**28+F(1, 2**122) < 2**30)
    check("panel17_exponent", 28-F(7*17, 5) == F(21, 5) > 4)
    check("outer_panel_brackets",
          all(2 <= 30-F(7*j, 5)-F(7, 10)*(1+r) <= 30
              for j in range(20) for r in (F(-1), F(1))))

    # Exhaust all possible reduction counts. All counts include constants,
    # lower/final checks, separately counted Newton arithmetic and clamps.
    ledgers = []
    for k in range(16):
        counts = {"constants": 4, "lower_range_check": 1,
                  "normalization_comparisons": min(k+1, 15),
                  "normalization_divisions": 2*k,
                  "final_normalization_check": 1, "newton": 8*5,
                  "rescaling": 1, "clamping": 2}
        ledgers.append({"reductions": k, "counts": counts,
                        "operations": sum(counts.values())})
    check("all_possible_ledgers", max(x["operations"] for x in ledgers) == 94 < 100)
    check("saved_operation_fields", old["operations_actual_upper"] == 94
          and old["operations_required_upper"] == 100)

    sample_replays = []
    expected_samples = [(F(1), False), (F(3), False), (F(4), False),
                        (F(16), True), (F(4**15), True)]
    check("sample_count", len(old["samples"]) == len(expected_samples))
    for i, ((w, low_panel), saved) in enumerate(zip(expected_samples, old["samples"])):
        # Power comparisons choose k independently of repeated division.
        k = next(j for j in range(16) if w <= 4**j)
        a, h = w/F(4**k), F(1, 2**k)
        x = F(1)
        iterates = [enc(x)]
        invariant_checks = []
        for n in range(8):
            previous = x
            # Additive source form, distinct from the original factored code.
            x = previous+(previous/2)*(1-a*previous*previous)
            invariant_checks.append(0 < previous <= x and a*x*x <= 1)
            iterates.append(enc(x))
        raw = h*x
        q = min(F(1, 4) if low_panel else F(1), max(F(0), raw))
        replay = {
            "saved_inputs": dec(saved["width"]) == w and saved["low_panel"] == low_panel,
            "normalization": dec(saved["normalized"]) == a
                and dec(saved["scale"]) == h and saved["reductions"] == k
                and F(1, 4) < a <= 1 and w == a/(h*h),
            "all_iterates_positive_monotone_under_root": all(invariant_checks),
            "saved_value": dec(saved["q"]) == q,
            "strict_error_without_sqrt": 0 < raw and w*raw*raw <= 1
                and w*(raw+eps)*(raw+eps) > 1,
            "clamp": q == raw,
            "saved_ledger": saved["operations"] == ledgers[k]["operations"]
                and {name: saved["counts"].get(name, 0)
                     for name in ledgers[k]["counts"]} == ledgers[k]["counts"]
                and set(saved["counts"]) <= set(ledgers[k]["counts"]),
        }
        check(f"sample_{i}_complete_replay", all(replay.values()))
        # Check the saved flags only AFTER recomputing their mathematical values.
        check(f"sample_{i}_saved_flags_consistent", saved["checks"] == {
            "normalization_identity": True, "normalized_range": True,
            "invariant_and_one_sided_error": True, "cost": True, "clamp_inactive": True})
        sample_replays.append({"width": enc(w), "normalized": enc(a), "scale": enc(h),
                               "x0_through_x8": iterates, "q": enc(q),
                               "checks": replay})

    expected_boundaries = [F(4**k)+offset for k in range(1, 16)
                           for offset in (F(-1, 2), F(0), F(1, 2))
                           if F(4**k)+offset <= 4**15]
    check("all_44_boundary_inputs", len(old["normalization_boundaries"]) == 44
          and [dec(x["width"]) for x in old["normalization_boundaries"]] == expected_boundaries)
    boundary_checks = []
    for saved in old["normalization_boundaries"]:
        w = dec(saved["width"])
        k = next(j for j in range(16) if w <= 4**j)
        boundary_checks.append(saved["reductions"] == k
                               and F(1, 4) < w/F(4**k) <= 1 and saved["passed"] is True)
    check("all_44_boundary_values", all(boundary_checks))

    # Every original Boolean is now supported by the independent checks above.
    expected_universal = {name: True for name in (
        "first_step_bound", "invariant_multiplier", "decisive_square_bound",
        "closed_form_e8", "strict_error_bound", "perturbation_paid",
        "width_upper_interface", "ledger_bound", "worst_cost_attained")}
    check("invariant_multiplier", c*F(5, 16) == F(15, 22) < 1)
    check("worst_cost_attained_at_endpoint", ledgers[15]["operations"] == 94
          and old["samples"][-1]["operations"] == 94)
    check("old_universal_flags_consistent", old["universal_checks"] == expected_universal)
    check("old_failure_list_empty", old["failures"] == [])
    check("source_certificate_unchanged", source.read_bytes() == source_bytes)

    failures = [key for key, ok in checks.items() if not ok]
    result = {
        "scope": "independent C033z1825 application audit; finite replay supports written continuum proof",
        "source_certificate": str(source),
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "checks": checks,
        "error_envelopes_e1_to_e8": [enc(x) for x in bounds],
        "input_bounds": {"eta": enc(eta), "log_tail": enc(log_tail),
                         "v_error": enc(v_error), "E_error": enc(e_error),
                         "q_input_error": enc(e_error/8)},
        "error_actual_upper": enc(eps+perturb), "error_required_upper": enc(required),
        "operations_actual_upper": 94, "operations_required_upper": 100,
        "all_reduction_ledgers": ledgers, "sample_replays": sample_replays,
        "normalization_boundaries_replayed": len(boundary_checks), "failures": failures,
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact audit checks; "
          "error<2^-64 (required<=2^-60); operations<=94 (required<=100); "
          f"5 complete samples, 44 boundaries, 16 ledgers; failures={failures}; certificate={path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
