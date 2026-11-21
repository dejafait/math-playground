"""Exact finite checks for C033z1830; the continuum proof is canonical there.

Only the coefficient conversion precedes eight exact Newton steps. No
profile/scalar execution, bit-cost claim or revised global ledger is made.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)


def enc(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def conversion(a):
    lower, upper = F(1, 4), F(1)
    for _ in range(64):
        midpoint = (lower + upper) / 2
        if a > midpoint:
            lower = midpoint
        else:
            upper = midpoint
    return lower, upper, (lower + upper) / 2


def construct(w, low_panel):
    counts = {"constants": 4, "lower_check": 1,
              "normalization_comparisons": 0, "normalization_divisions": 0,
              "final_check": 1, "conversion": 64*3+2,
              "newton": 8*5, "rescaling": 1, "clamping": 2}
    one = F(1)
    two = one + one
    three = two + one
    four = two * two
    quarter = one / four
    assert w >= one
    a, h, k = w, one, 0
    for _ in range(15):
        counts["normalization_comparisons"] += 1
        if a <= one:
            break
        a = a / four
        h = h / two
        counts["normalization_divisions"] += 2
        k += 1
    assert a <= one
    lower, upper = quarter, one
    for _ in range(64):
        midpoint = (lower + upper) / two
        if a > midpoint:
            lower = midpoint
        else:
            upper = midpoint
    b = (lower + upper) / two
    x = one
    states = [{"x": enc(x), "denominator_exponent": 0}]
    checks = []
    for n in range(8):
        u = x*x
        v = b*u
        z = three-v
        p = x*z
        y = p/two
        d, next_d = 34*(3**n-1), 34*(3**(n+1)-1)
        checks.append({
            "positive_monotone_under_rounded_root": 0 < x <= y and b*y*y <= 1,
            "exact_iterate_denominator": y.denominator == 2**next_d,
            "square_denominator": 2**(2*d) % u.denominator == 0,
            "coefficient_product_denominator": 2**(67+2*d) % v.denominator == 0,
            "subtraction_denominator": 2**(67+2*d) % z.denominator == 0,
            "cubic_product_denominator": 2**(67+3*d) % p.denominator == 0,
        })
        x = y
        states.append({"x": enc(x), "denominator_exponent": next_d})
    raw = h*x
    q = raw
    if q < 0:
        q = F(0)
    cap = quarter if low_panel else one
    if q > cap:
        q = cap
    return {"w": w, "low_panel": low_panel, "a": a, "h": h, "k": k,
            "b": b, "lower": lower, "upper": upper, "states": states,
            "iteration_checks": checks, "raw": raw, "q": q,
            "counts": counts, "operations": sum(counts.values())}


def main():
    checks = {}

    def check(name, value):
        checks[name] = bool(value)

    c = F(24, 11)
    envelopes = [F(5, 16)]
    for _ in range(7):
        envelopes.append(c*envelopes[-1]**2)
    e8 = envelopes[-1]
    check("closed_envelope", e8 == F(11, 24)*F(15, 22)**128)
    check("invariant", c*F(5, 16) < 1)
    check("first_step_endpoints", (3*F(1, 2)-F(1, 2)**3)/2 == F(11, 16))
    check("decisive_comparison", F(225, 484) < F(1, 2))
    check("newton_relative_error", e8 < F(1, 2**65))
    coefficient_error = F(3, 2**65)
    log_tail = F(9, 4*129*3**129)
    v_error = 30*log_tail + F(7, 10*2**168)
    e_error = F(96*3**21, factorial(41)) + 3**21*v_error
    input_error = e_error/8
    total = coefficient_error + 2*e8 + input_error
    safe_total = F(5, 2**65) + F(1, 2**123)
    check("coefficient_mvt", 4*F(3, 2**67) == coefficient_error)
    check("input_perturbation", input_error < F(1, 2**123))
    check("total_error", total < safe_total < F(1, 2**62) < F(1, 2**60))
    check("width_range_interface", 2+2**28+F(1, 2**122) < 2**30)
    exponents = [34*(3**n-1) for n in range(9)]
    check("denominator_recurrence", exponents[0] == 0 and
          all(exponents[n+1] == 3*exponents[n]+68 for n in range(8)))
    check("last_denominator", exponents[-1] == 223040 and exponents[-1]+15 == 223055)

    # Independent integer cell oracle is evidence only, not a constructor primitive.
    coefficient_cases = [F(1, 4), F(1), F(5, 8), F(7, 16), F(13, 16),
                         F(1, 4)+F(1, 10**100+267), F(1)-F(1, 10**100+267)]
    # Every distinct depth of exact midpoint equality; conversion does not stop early.
    coefficient_cases += [F(1, 4)+F(3, 2**(j+2)) for j in range(1, 65)]
    conversions = []
    for i, a in enumerate(coefficient_cases):
        lower, upper, b = conversion(a)
        position = (a-F(1, 4))*F(4, 3)*2**64
        ceiling = -((-position.numerator)//position.denominator)
        cell = max(0, ceiling-1)
        oracle = F(1, 4)+F(3*(2*cell+1), 2**67)
        ok = (lower <= a <= upper and upper-lower == F(3, 2**66)
              and F(1, 4) < b < 1 and abs(a-b) <= F(3, 2**67)
              and b == oracle and b.denominator == 2**67)
        check(f"conversion_{i}", ok)
        conversions.append({"a": enc(a), "lower": enc(lower), "upper": enc(upper),
                            "b": enc(b), "oracle": enc(oracle), "passed": ok})

    ledgers = []
    for k in range(16):
        counts = {"constants": 4, "lower_check": 1,
                  "normalization_comparisons": min(k+1, 15),
                  "normalization_divisions": 2*k, "final_check": 1,
                  "conversion": 194, "newton": 40, "rescaling": 1, "clamping": 2}
        ledgers.append({"reductions": k, "counts": counts, "operations": sum(counts.values())})
    check("all_reduction_ledgers", max(row["operations"] for row in ledgers) == 288 <= 322)

    samples = []
    sample_inputs = [(F(1), False), (F(3), False), (F(4), False),
                     (F(16), True), (F(2**30), True),
                     (F(1)+F(1, 10**100+267), False),
                     (F(4)-F(1, 2**100), False), (F(4)+F(1, 2**100), False)]
    for i, (w, low_panel) in enumerate(sample_inputs):
        result = construct(w, low_panel)
        k, a, b, raw, q = [result[key] for key in ("k", "a", "b", "raw", "q")]
        independent_k = next(j for j in range(16) if w <= 4**j)
        allowance = coefficient_error + F(1, 2**64)
        cap = F(1, 4) if low_panel else F(1)
        # Positive squared inequalities certify two-sided error without an approximate sqrt.
        sample_checks = {
            "normalization": k == independent_k and a == w/F(4**k)
                and result["h"] == F(1, 2**k) and F(1, 4) < a <= 1,
            "conversion": abs(a-b) <= F(3, 2**67) and b.denominator == 2**67,
            "all_iteration_checks": all(all(row.values()) for row in result["iteration_checks"]),
            "raw_error": 0 < raw-allowance and w*(raw-allowance)**2 < 1
                and w*(raw+allowance)**2 > 1,
            "true_root_in_clamp": w*cap*cap >= 1,
            "clamped_error": 0 < q-allowance and w*(q-allowance)**2 < 1
                and w*(q+allowance)**2 > 1,
            "raw_denominator": raw.denominator == 2**(223040+k),
            "clamped_denominator": 2**223055 % q.denominator == 0,
            "complete_ledger": result["counts"] == ledgers[k]["counts"]
                and result["operations"] == ledgers[k]["operations"],
        }
        check(f"sample_{i}", all(sample_checks.values()))
        for key in ("w", "a", "h", "b", "lower", "upper", "raw", "q"):
            result[key] = enc(result[key])
        result["checks"] = sample_checks
        samples.append(result)

    boundaries = []
    for j in range(1, 16):
        for offset in (F(-1, 2), F(0), F(1, 2)):
            w = F(4**j)+offset
            if w > 4**15:
                continue
            k = next(n for n in range(16) if w <= 4**n)
            a = w/F(4**k)
            lower, upper, b = conversion(a)
            ok = F(1, 4) < a <= 1 and lower <= a <= upper and abs(a-b) <= F(3, 2**67)
            boundaries.append({"w": enc(w), "k": k, "a": enc(a), "b": enc(b), "passed": ok})
    check("normalization_boundaries", len(boundaries) == 44 and all(x["passed"] for x in boundaries))
    failures = [name for name, value in checks.items() if not value]
    result = {
        "scope": "C033z1830 finite specialization; continuum proof is in canonical C033z",
        "checks": checks, "error_envelopes_e1_to_e8": [enc(x) for x in envelopes],
        "bounds": {"conversion_error": enc(F(3, 2**67)),
                   "coefficient_output_error": enc(coefficient_error),
                   "newton_output_error": enc(2*e8), "input_output_error": enc(input_error),
                   "total_error": enc(total), "safe_total_error": enc(safe_total),
                   "required_error": enc(F(1, 2**60)), "operations_actual": 288,
                   "operations_required": 322, "iterate_denominator_exponents": exponents,
                   "raw_denominator_exponent_upper": 223055},
        "conversion_cases": conversions, "ledgers": ledgers,
        "samples": samples, "normalization_boundaries": boundaries, "failures": failures,
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} exact checks; "
          "error<2^-62 (required<=2^-60); operations<=288 (required<=322); "
          "den(x_n)=2^[34*(3^n-1)], den(raw)<=2^223055; "
          f"{len(samples)} full samples, {len(conversions)} conversion cases, "
          f"44 boundaries, 16 ledgers; failures={failures}; certificate={path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
