"""L034 exact incidence benchmark; no labeled-family optimization."""
import json
from fractions import Fraction
from math import comb, factorial
from pathlib import Path


def rational(value):
    value = Fraction(value)
    return {"numerator": value.numerator, "denominator": value.denominator}


def main():
    n, k, a, c = 1024, 64, 68, 60
    v, b, t = n - c, a - c, k - c
    N, D = comb(n, c), comb(a, c)
    q, denominator = 65537**28, 2**128
    T, M = Fraction(q, denominator), q // denominator
    cutoff = D * (M + 1)
    safe_cap, cap_remainder = divmod(cutoff - 1, N)
    packing = Fraction(comb(v, t), comb(b, t))
    ordinary_integer = packing.numerator // packing.denominator
    inner, stages = 1, []
    for i in reversed(range(t)):
        numerator, divisor = (v - i) * inner, b - i
        bound, remainder = divmod(numerator, divisor)
        stages.append({"i": i, "inner": inner, "numerator": numerator,
                       "divisor": divisor, "quotient": bound, "remainder": remainder})
        inner = bound
    nested = inner
    support_ratio = Fraction(comb(n, k), comb(a, k))
    transfers = {"safe_cap": N * safe_cap // D,
                 "adjacent_cap": N * (safe_cap + 1) // D,
                 "ordinary_integer": N * ordinary_integer // D,
                 "ordinary_nested_floor": N * nested // D}
    # Independent expanded integer expression checks the imported floor order.
    nested_expanded = v * ((v-1) * ((v-2) * ((v-3)//(b-3))//(b-2))//(b-1))//b
    ratio = Fraction(N * nested, D) / T
    checks = {
        "factorial_N": N == factorial(n)//(factorial(c)*factorial(n-c)),
        "factorial_D": D == factorial(a)//(factorial(c)*factorial(a-c)),
        "D_equals_68_choose_8": D == comb(a, b),
        "threshold_positive_nonintegral": M > 0 and 0 < q % denominator < denominator,
        "safe_cap_division_identity": cutoff-1 == N*safe_cap + cap_remainder and 0 <= cap_remainder < N,
        "safe_cap_strict_test": N*safe_cap < cutoff,
        "adjacent_cap_fails_strict_test": N*(safe_cap+1) >= cutoff,
        "safe_transfer_le_M": transfers["safe_cap"] <= M,
        "adjacent_transfer_gt_M": transfers["adjacent_cap"] > M,
        "nonuniform_safe_equality": (cutoff-1)//D == M,
        "nonuniform_unsafe_equality": cutoff//D == M+1,
        "packing_identity_N": N*comb(v,t) == comb(n,k)*comb(k,c),
        "packing_identity_D": D*comb(b,t) == comb(a,k)*comb(k,c),
        "unrounded_transfer_is_L001": N*packing/D == support_ratio,
        "nested_floor_independent_expression": nested == nested_expanded,
        "nested_division_identities": all(s["numerator"] == s["divisor"]*s["quotient"]+s["remainder"] and 0 <= s["remainder"] < s["divisor"] for s in stages),
        "nested_le_ordinary_integer": nested <= ordinary_integer,
        "nested_cap_above_required": nested > safe_cap,
        "nested_transfer_gt_M": transfers["ordinary_nested_floor"] > M,
        "ordinary_transfer_gt_M": transfers["ordinary_integer"] > M,
        "nested_transfer_ratio_lower": ratio > Fraction(2763,1000),
        "nested_transfer_ratio_upper": ratio < Fraction(2764,1000),
    }
    failures = [name for name, passed in checks.items() if not passed]
    certificate = {
        "scope": "Exact L034 benchmark only; no finite labeled cap or RS-list realization.",
        "parameters": {"n": n, "k": k, "agreement": a, "core": c,
                       "residual_domain": v, "block": b, "packing_strength": t},
        "counts": {"N": N, "D": D, "residual_4_subsets": comb(v,t), "block_4_subsets": comb(b,t)},
        "threshold": {"q": q, "denominator": denominator, "M": M, "remainder": q%denominator},
        "local_caps": {"safe_integer": safe_cap, "safe_cap_division_remainder": cap_remainder,
                       "exact_real_open_endpoint": rational(Fraction(cutoff,N)),
                       "conservative_real_closed_endpoint": rational(T*D/N),
                       "ordinary_packing": rational(packing), "ordinary_integer": ordinary_integer,
                       "ordinary_nested_floor": nested, "nested_stages": stages},
        "nonuniform_endpoint": {"strict_cutoff": cutoff, "greatest_safe_integer_sum": cutoff-1,
                                "safe_global_floor": (cutoff-1)//D, "unsafe_global_floor": cutoff//D},
        "global_transfer": {**transfers, "unrounded_packing": rational(N*packing/D),
                            "L001": rational(support_ratio), "nested_over_threshold": rational(ratio)},
        "checks": checks, "failures": failures,
    }
    out = Path(__file__).with_name("sixty-core-threshold-results.json")
    out.write_text(json.dumps(certificate, indent=2)+"\n")
    print(f"checks={len(checks)} failures={failures}")
    print(f"required uniform integer cap <= {safe_cap}; ordinary count cap={ordinary_integer}; nested-floor cap={nested}")
    print(f"safe cap passes={checks['safe_transfer_le_M']}; adjacent cap fails={checks['adjacent_transfer_gt_M']}; nested/threshold in (2.763,2.764)={checks['nested_transfer_ratio_lower'] and checks['nested_transfer_ratio_upper']}")
    print(f"certificate={out.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
