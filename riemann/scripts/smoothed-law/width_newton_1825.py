"""Exact checks for the C033z width-only Newton specialization.

The universal argument is in C033z. Samples check the implementation and
ledger; they are not a proof of the whole rational interval. No saved
evaluator inputs, profile values or unreplayed execution suffix are used.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def encode(value):
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def constructor(width, low_panel=False):
    counts = {}

    def charge(kind, value):
        counts[kind] = counts.get(kind, 0) + 1
        return value

    two = charge("constants", F(1) + 1)
    three = charge("constants", two + 1)
    four = charge("constants", two * two)
    quarter = charge("constants", F(1) / four)
    if charge("lower_range_check", width < 1):
        raise ValueError("width below contract")
    a, h = width, F(1)
    reductions = 0
    for _ in range(15):
        if not charge("normalization_comparisons", a > 1):
            break
        a = charge("normalization_divisions", a / four)
        h = charge("normalization_divisions", h / two)
        reductions += 1
    if charge("final_normalization_check", a > 1):
        raise ValueError("width above contract")
    normalized = a
    x = F(1)
    for _ in range(8):
        square = charge("newton", x * x)
        product = charge("newton", a * square)
        correction = charge("newton", three - product)
        numerator = charge("newton", x * correction)
        x = charge("newton", numerator / two)
    q = charge("rescaling", h * x)
    unclamped = q
    cap = quarter if low_panel else F(1)
    if charge("clamping", q < 0):
        q = F(0)
    if charge("clamping", q > cap):
        q = cap
    return q, unclamped, normalized, h, reductions, counts


def main():
    c = F(24, 11)
    relative_bounds = [F(5, 16)]
    for _ in range(7):
        relative_bounds.append(c * relative_bounds[-1] ** 2)
    eps = F(1, 2**65)
    perturbation = F(1, 2**123)
    universal_checks = {
        "first_step_bound": 1 - (3*F(1, 2)-F(1, 2)**3)/2 == F(5, 16),
        "invariant_multiplier": c * F(5, 16) == F(15, 22) < 1,
        "decisive_square_bound": F(15, 22)**2 == F(225, 484) < F(1, 2),
        "closed_form_e8": relative_bounds[-1] == F(11, 24)*F(15, 22)**128,
        "strict_error_bound": relative_bounds[-1] < eps,
        "perturbation_paid": eps + perturbation < F(1, 2**64) < F(1, 2**60),
        "width_upper_interface": 2 + 2**28 + F(1, 2**122) < 2**30,
        "ledger_bound": 4 + 1 + 16 + 30 + 40 + 1 + 2 == 94,
    }
    # Fifteen loop tests plus one final check; the lower check is separate.
    samples = []
    sample_checks = []
    for w, low_panel in ((F(1), False), (F(3), False), (F(4), False),
                         (F(16), True), (F(4**15), True)):
        q, raw, a, h, n, counts = constructor(w, low_panel)
        checks = {
            "normalization_identity": w == a/(h*h),
            "normalized_range": F(1, 4) < a <= 1,
            "invariant_and_one_sided_error": 0 < raw and w*raw*raw <= 1
                and w*(raw+eps)**2 >= 1,
            "cost": sum(counts.values()) <= 94,
            "clamp_inactive": q == raw,
        }
        sample_checks.extend(checks.values())
        samples.append({"width": encode(w), "low_panel": low_panel, "normalized": encode(a),
                        "scale": encode(h), "reductions": n, "q": encode(q),
                        "counts": counts, "operations": sum(counts.values()),
                        "checks": checks})
    # Test each normalization boundary from both sides without full Newton runs.
    boundaries = []
    for k in range(1, 16):
        center = F(4**k)
        for w in (center-F(1, 2), center, center+F(1, 2)):
            if w > 4**15:
                continue
            a, h, n = w, F(1), 0
            while a > 1:
                a /= 4
                h /= 2
                n += 1
            ok = n <= 15 and F(1, 4) < a <= 1 and w == a/(h*h)
            boundaries.append({"width": encode(w), "reductions": n, "passed": ok})
    universal_checks["worst_cost_attained"] = samples[-1]["operations"] == 94
    failures = [name for name, ok in universal_checks.items() if not ok]
    if not all(sample_checks):
        failures.append("sample check")
    if not all(item["passed"] for item in boundaries):
        failures.append("normalization boundary check")
    certificate = {
        "scope": "width-only specialization; no global evaluator or bit-cost claim",
        "universal_checks": universal_checks,
        "relative_error_bounds_e1_to_e8": [encode(x) for x in relative_bounds],
        "absolute_error_bound_required": encode(F(1, 2**60)),
        "absolute_error_bound_proved": encode(eps+perturbation),
        "operations_actual_upper": 94, "operations_required_upper": 100,
        "samples": samples, "normalization_boundaries": boundaries,
        "failures": failures,
    }
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"{'PASS' if not failures else 'FAIL'}: exact width-only checks; "
          f"operations<=94 (required<=100); error<2^-64 (required<=2^-60); "
          f"boundaries={len(boundaries)}; failures={failures}; certificate={path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
