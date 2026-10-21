"""Exact arithmetic for L027; no graph enumeration or SDP optimization."""
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def rat(x):
    x = Fraction(x)
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    n, k, a, c = 1024, 64, 68, 61
    residual, v = a - c, n - c
    cores, incidences = comb(n, c), comb(a, c)
    q, denominator = 65537**28, 2**128
    threshold = Fraction(q, denominator)
    threshold_floor = q // denominator
    packing = Fraction(comb(v, 3), comb(residual, 3))
    packing_integer = packing.numerator // packing.denominator
    open_limit = Fraction(incidences * (threshold_floor + 1), cores)
    conservative_limit = threshold * incidences / cores
    safe_integer_cap = (incidences * (threshold_floor + 1) - 1) // cores
    support_ratio = Fraction(comb(n, k), comb(a, k))
    packing_transfer = cores * packing / incidences
    integer_packing_transfer = (cores * packing_integer) // incidences
    safe_transfer = cores * safe_integer_cap // incidences
    next_transfer = cores * (safe_integer_cap + 1) // incidences
    ratio = packing / conservative_limit
    lower_mill, upper_mill = 2766, 2767
    checks = {
        "factorial_core_count": cores == factorial(n) // (factorial(c) * factorial(n-c)),
        "factorial_incidence_count": incidences == factorial(a) // (factorial(c) * factorial(a-c)),
        "incidences_equal_68_choose_7": incidences == comb(a, residual),
        "packing_transfer_equals_L001_ratio": packing_transfer == support_ratio,
        "safe_cap_strict_open_test": cores * safe_integer_cap < incidences * (threshold_floor + 1),
        "next_cap_fails_open_test": cores * (safe_integer_cap + 1) >= incidences * (threshold_floor + 1),
        "safe_transfer_at_most_threshold_floor": safe_transfer <= threshold_floor,
        "next_transfer_above_threshold_floor": next_transfer > threshold_floor,
        "integer_packing_transfer_above_threshold_floor": integer_packing_transfer > threshold_floor,
        "ratio_above_2766_over_1000": ratio > Fraction(lower_mill, 1000),
        "ratio_below_2767_over_1000": ratio < Fraction(upper_mill, 1000),
    }
    failures = [name for name, ok in checks.items() if not ok]
    certificate = {
        "scope": "Exact incidence and threshold arithmetic only; no improved cap or SDP feasibility claim.",
        "parameters": {"n": n, "k": k, "agreement": a, "core_size": c,
                       "residual_size": residual, "residual_domain_size": v},
        "counts": {"cores": cores, "incidences_per_support": incidences,
                   "residual_triples": comb(v, 3), "triples_per_vertex": comb(residual, 3)},
        "threshold": {"q": q, "denominator": denominator, "floor": threshold_floor,
                      "remainder": q % denominator},
        "local_caps": {"ordinary_packing": rat(packing), "ordinary_packing_integer": packing_integer,
                       "conservative_safe_real": rat(conservative_limit),
                       "exact_safe_real_open_limit": rat(open_limit),
                       "exact_safe_integer": safe_integer_cap},
        "global_transfer": {"ordinary_packing": rat(packing_transfer),
                            "L001_ratio": rat(support_ratio),
                            "integer_packing_floor": integer_packing_transfer,
                            "safe_integer_floor": safe_transfer, "next_integer_floor": next_transfer},
        "strength_ratio": {"exact": rat(ratio), "lower": rat(Fraction(lower_mill, 1000)),
                           "upper": rat(Fraction(upper_mill, 1000))},
        "checks": checks, "failures": failures,
    }
    out = Path(__file__).with_name("core-theta-threshold-results.json")
    out.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"checks={len(checks)} failures={failures}")
    print(f"ordinary local cap={packing} (integer {packing_integer}); required uniform integer cap<={safe_integer_cap}")
    print("ordinary/required-real ratio lies strictly between 2.766 and 2.767")
    print(f"certificate={out.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
