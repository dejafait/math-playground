"""Independent finite application audit of C033z1830, not a scalar run.

No original mathematical script is imported or executed. An integer cell
formula and additive Newton update independently replay every saved value.
A separate instrumented factored implementation checks the operation ledger.
The uniform proof and all source qualifications are canonical in C033z.
"""
from collections import Counter
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)


def enc(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def dec(q):
    return F(int(q["numerator"]), int(q["denominator"]))


def cell(a):
    # Equality selects the cell immediately below, except at the left end.
    position = (a-F(1, 4))*F(2**66, 3)
    index = max(0, -((-position.numerator)//position.denominator)-1)
    left = F(1, 4)+F(3*index, 2**66)
    right = left+F(3, 2**66)
    return left, right, (left+right)/2


def counted(w, low):
    counts = Counter({"normalization_divisions": 0})
    group = "constants"

    def op(kind, a, b):
        counts[group] += 1
        if kind == "+":
            return a+b
        if kind == "-":
            return a-b
        if kind == "*":
            return a*b
        if kind == "/":
            return a/b
        if kind == "<=":
            return a <= b
        if kind == ">":
            return a > b
        if kind == "<":
            return a < b
        raise ValueError(kind)

    zero, one = F(0), F(1)
    two = op("+", one, one)
    three = op("+", two, one)
    four = op("*", two, two)
    quarter = op("/", one, four)
    group = "lower_check"
    assert op("<=", one, w)
    a, h, k = w, one, 0
    for _ in range(15):
        group = "normalization_comparisons"
        if op("<=", a, one):
            break
        group = "normalization_divisions"
        a, h = op("/", a, four), op("/", h, two)
        k += 1
    group = "final_check"
    assert op("<=", a, one)
    left, right = quarter, one
    branch_checks = []
    group = "conversion"
    for n in range(64):
        midpoint = op("/", op("+", left, right), two)
        if op(">", a, midpoint):
            left = midpoint
        else:
            right = midpoint
        # Verification arithmetic below is outside the instrumented algorithm.
        branch_checks.append(left <= a <= right and right-left == F(3, 2**(n+3)))
    b = op("/", op("+", left, right), two)
    x = one
    group = "newton"
    for _ in range(8):
        square = op("*", x, x)
        product = op("*", b, square)
        bracket = op("-", three, product)
        x = op("/", op("*", x, bracket), two)
    group = "rescaling"
    raw = op("*", h, x)
    q = raw
    cap = quarter if low else one
    group = "clamping"
    if op("<", q, zero):
        q = zero
    if op(">", q, cap):
        q = cap
    return a, h, k, b, raw, q, dict(counts), branch_checks


def main():
    source = Path(__file__).with_name("width_dyadic_1830.json")
    original = source.read_bytes()
    saved = json.loads(original)
    checks = {}

    def check(name, value):
        checks[name] = bool(value)

    c, envelope = F(24, 11), [F(5, 16)]
    for n in range(1, 8):
        envelope.append(c*envelope[-1]**2)
        check(f"invariant_and_closed_envelope_{n+1}",
              0 < envelope[-1] < envelope[-2] <= F(5, 16)
              and envelope[-1] == F(11, 24)*F(15, 22)**(2**n))
    check("saved_all_error_envelopes", list(map(dec, saved["error_envelopes_e1_to_e8"])) == envelope)
    check("first_step_and_decisive_square", (3*F(1, 2)-F(1, 2)**3)/2 == F(11, 16)
          and F(225, 484) < F(1, 2) and c*F(5, 16) < 1)
    check("Newton_error_lt_2^-65", envelope[-1] < F(1, 2**65))
    log_error = F(9, 4*129*3**129)
    v_error = 30*log_error+F(7, 10*2**168)
    E_error = F(96*3**21, factorial(41))+3**21*v_error
    for name, actual, required in (
        ("log", log_error, F(1, 2**200)), ("v", v_error, F(1, 2**160)),
        ("E", E_error, F(1, 2**120)), ("width", E_error/4, F(1, 2**122)),
        ("inverse_root_input", E_error/8, F(1, 2**123))):
        check(f"1802_{name}_error", actual < required)
    check("all_panel_brackets", all(2 <= 30-F(7*j, 5)-F(7, 10)*(1+r) <= 30
          for j in range(20) for r in (F(-1), F(1))))
    check("width_range", 2+2**28+F(1, 2**122) < 2**30)
    check("first17_true_clamp", all(28-F(7*j, 5) >= F(21, 5) > 4 for j in range(1, 18)))
    total = 2*envelope[-1]+F(3, 2**65)+E_error/8
    safe = F(5, 2**65)+F(1, 2**123)
    check("simultaneous_error", total < safe < F(1, 2**62) < F(1, 2**60))
    exponents = [0]
    for _ in range(8):
        exponents.append(3*exponents[-1]+68)
    check("denominator_induction", exponents == [34*(3**n-1) for n in range(9)]
          and exponents[-1] == 223040 and exponents[-1]+15 == 223055)
    expected_bounds = {
        "conversion_error": enc(F(3, 2**67)), "coefficient_output_error": enc(F(3, 2**65)),
        "newton_output_error": enc(2*envelope[-1]), "input_output_error": enc(E_error/8),
        "total_error": enc(total), "safe_total_error": enc(safe),
        "required_error": enc(F(1, 2**60)), "operations_actual": 288,
        "operations_required": 322, "iterate_denominator_exponents": exponents,
        "raw_denominator_exponent_upper": 223055}
    check("all_saved_bounds_exact", saved["bounds"] == expected_bounds)

    expected_coefficients = [F(1, 4), F(1), F(5, 8), F(7, 16), F(13, 16),
                             F(1, 4)+F(1, 10**100+267), F(1)-F(1, 10**100+267)]
    expected_coefficients += [F(1, 4)+F(3, 2**(j+2)) for j in range(1, 65)]
    check("all71_conversion_inputs", list(map(lambda r: dec(r["a"]), saved["conversion_cases"]))
          == expected_coefficients)
    conversions = []
    for i, row in enumerate(saved["conversion_cases"]):
        a = dec(row["a"])
        left, right, b = cell(a)
        ok = left <= a <= right and right-left == F(3, 2**66)
        ok = ok and F(1, 4) < b < 1 and abs(a-b) <= F(3, 2**67) and b.denominator == 2**67
        ok = ok and row == {"a": enc(a), "lower": enc(left), "upper": enc(right),
                            "b": enc(b), "oracle": enc(b), "passed": True}
        # Also independently execute the 64-slot comparison rule, including endpoints.
        l, r = F(1, 4), F(1)
        for n in range(64):
            m = (l+r)/2
            l, r = (m, r) if a > m else (l, m)
            ok = ok and l <= a <= r and r-l == F(3, 2**(n+3))
        ok = ok and (l, r, (l+r)/2) == (left, right, b)
        check(f"conversion_{i}_all_values_and_branches", ok)
        conversions.append({"index": i, "a": enc(a), "b": enc(b), "passed": ok})

    ledgers = []
    for k in range(16):
        counts = {"constants": 4, "lower_check": 1,
                  "normalization_comparisons": min(k+1, 15), "normalization_divisions": 2*k,
                  "final_check": 1, "conversion": 194, "newton": 40, "rescaling": 1, "clamping": 2}
        ledgers.append({"reductions": k, "counts": counts, "operations": sum(counts.values())})
    check("all16_saved_ledgers", saved["ledgers"] == ledgers)
    check("full_ledger_formula_and_bound", all(row["operations"] == (244+3*k if k < 15 else 288)
          for k, row in enumerate(ledgers)) and max(row["operations"] for row in ledgers) == 288 <= 322)

    inputs = [(F(1), False), (F(3), False), (F(4), False), (F(16), True), (F(2**30), True),
              (F(1)+F(1, 10**100+267), False), (F(4)-F(1, 2**100), False),
              (F(4)+F(1, 2**100), False)]
    check("all8_sample_inputs", [(dec(r["w"]), r["low_panel"]) for r in saved["samples"]] == inputs)
    replays = []
    for i, ((w, low), row) in enumerate(zip(inputs, saved["samples"])):
        k = next(j for j in range(16) if w <= 4**j)
        a, h = w/F(4**k), F(1, 2**k)
        left, right, b = cell(a)
        x, states, step_checks = F(1), [{"x": enc(F(1)), "denominator_exponent": 0}], []
        for n in range(8):
            previous = x
            x = previous+(previous/2)*(1-b*previous*previous)
            d = exponents[n]
            u, v = previous**2, b*previous**2
            z, p = 3-v, previous*(3-v)
            facts = {
                "positive_monotone_under_rounded_root": 0 < previous <= x and b*x*x <= 1,
                "exact_iterate_denominator": x.denominator == 2**exponents[n+1],
                "square_denominator": 2**(2*d) % u.denominator == 0,
                "coefficient_product_denominator": 2**(67+2*d) % v.denominator == 0,
                "subtraction_denominator": 2**(67+2*d) % z.denominator == 0,
                "cubic_product_denominator": 2**(67+3*d) % p.denominator == 0}
            step_checks.append(facts)
            states.append({"x": enc(x), "denominator_exponent": exponents[n+1]})
        raw, cap = h*x, F(1, 4) if low else F(1)
        q = min(cap, max(F(0), raw))
        allowance = F(3, 2**65)+F(1, 2**64)
        facts = {
            "normalization": k == row["k"] and a == dec(row["a"]) and h == dec(row["h"])
                and F(1, 4) < a <= 1 and w == a/(h*h),
            "conversion": abs(a-b) <= F(3, 2**67) and b.denominator == 2**67,
            "all_iteration_checks": all(all(r.values()) for r in step_checks),
            "raw_error": 0 < raw-allowance and w*(raw-allowance)**2 < 1 < w*(raw+allowance)**2,
            "true_root_in_clamp": w*cap*cap >= 1,
            "clamped_error": 0 < q-allowance and w*(q-allowance)**2 < 1 < w*(q+allowance)**2,
            "raw_denominator": raw.denominator == 2**(223040+k),
            "clamped_denominator": 2**223055 % q.denominator == 0,
            "complete_ledger": row["counts"] == ledgers[k]["counts"]
                and row["operations"] == ledgers[k]["operations"]}
        check(f"sample_{i}_all_iterates_intermediates_flags", states == row["states"]
              and step_checks == row["iteration_checks"] and facts == row["checks"] and all(facts.values()))
        check(f"sample_{i}_all_other_values", all(dec(row[key]) == value for key, value in
              {"b": b, "lower": left, "upper": right, "raw": raw, "q": q}.items()))
        ca, ch, ck, cb, cr, cq, cc, branch_checks = counted(w, low)
        check(f"sample_{i}_instrumented_algorithm", (ca, ch, ck, cb, cr, cq) == (a, h, k, b, raw, q)
              and cc == ledgers[k]["counts"] and all(branch_checks))
        replays.append({"w": enc(w), "low_panel": low, "states": states,
                        "iteration_checks": step_checks, "raw": enc(raw), "q": enc(q),
                        "checks": facts, "instrumented_counts": cc})

    boundaries = [F(4**j)+offset for j in range(1, 16) for offset in (F(-1, 2), F(0), F(1, 2))
                  if F(4**j)+offset <= 4**15]
    check("all44_boundary_inputs", [dec(r["w"]) for r in saved["normalization_boundaries"]] == boundaries)
    for i, (w, row) in enumerate(zip(boundaries, saved["normalization_boundaries"])):
        k = next(j for j in range(16) if w <= 4**j)
        a = w/F(4**k)
        left, right, b = cell(a)
        check(f"boundary_{i}_all_values", row == {"w": enc(w), "k": k, "a": enc(a),
              "b": enc(b), "passed": True} and F(1, 4) < a <= 1 and left <= a <= right)
    # Every stored claim has been recomputed, rather than accepting its Boolean flag.
    expected_names = {"closed_envelope", "invariant", "first_step_endpoints", "decisive_comparison",
                      "newton_relative_error", "coefficient_mvt", "input_perturbation", "total_error",
                      "width_range_interface", "denominator_recurrence", "last_denominator",
                      "all_reduction_ledgers", "normalization_boundaries"}
    expected_names |= {f"conversion_{i}" for i in range(71)} | {f"sample_{i}" for i in range(8)}
    check("saved92_flags_consistent", saved["checks"] == dict.fromkeys(expected_names, True))
    check("saved_failures_empty", saved["failures"] == [])
    check("source_unchanged", source.read_bytes() == original)
    failures = [name for name, ok in checks.items() if not ok]
    result = {"scope": "C033z1830 independent application audit; uniform proof in C033z1832",
              "audit_implementation_correction": "Initial certificate preserved as width_dyadic_audit_1832_initial.json: sample0 failed dictionary equality because Counter omitted a zero normalization_divisions key. Explicit zero initialization repairs schema only; arithmetic and counts unchanged.",
              "source_certificate": str(source), "source_sha256": hashlib.sha256(original).hexdigest(),
              "checks": checks, "bounds": expected_bounds,
              "input_bounds": {"log_error": enc(log_error), "v_error": enc(v_error), "E_error": enc(E_error)},
              "error_envelopes": list(map(enc, envelope)), "conversions": conversions,
              "ledgers": ledgers, "sample_replays": replays, "boundaries_replayed": len(boundaries),
              "failures": failures}
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"{'PASS' if not failures else 'FAIL'}: {len(checks)} independent checks; "
          "error<2^-62 (required<=2^-60); operations<=288 (required<=322); "
          "den(x_n)=2^[34*(3^n-1)], rescaled denominator<=2^223055; "
          f"8 full paths, 71 conversion cases, 44 boundaries, 16 ledgers; failures={failures}; certificate={path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
