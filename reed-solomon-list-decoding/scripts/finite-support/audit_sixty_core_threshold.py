"""Independent arithmetic audit of L034; no admissible-family computation."""
import json
from fractions import Fraction as Q
from pathlib import Path


def choose(n, k):
    # Pascal addition only: independent of the generator's comb/factorial calls.
    row = [1] + [0] * k
    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            row[j] += row[j - 1]
    return row[k]


def rat(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


def main():
    here = Path(__file__).parent
    source = json.loads((here / "sixty-core-threshold-results.json").read_text())
    N, D = choose(1024, 60), choose(68, 8)
    q = 1
    for _ in range(28):
        q *= 65537
    den = 1 << 128
    T = Q(q, den)
    M = T.__floor__()
    cutoff = D * (M + 1)
    pack = Q(choose(964, 4), choose(8, 4))

    # Search using the actual rational safety test, not the proposed cap formula.
    def passes(b):
        return Q((N * b) // D) <= T

    low, high = 0, pack.__floor__() + 1
    assert passes(low) and not passes(high)
    search = []
    while high - low > 1:
        middle = (low + high) // 2
        accepted = passes(middle)
        search.append({"low": low, "high": high, "middle": middle,
                       "accepted": accepted})
        if accepted:
            low = middle
        else:
            high = middle
    cap = low

    stages = []

    def shortening(v, b, strength):
        if strength == 0:
            return 1
        inner = shortening(v - 1, b - 1, strength - 1)
        value = Q(v * inner, b).__floor__()
        stages.append({"i": 964 - v, "inner": inner, "numerator": v * inner,
                       "divisor": b, "quotient": value,
                       "remainder": v * inner - b * value})
        return value

    nested = shortening(964, 8, 4)
    support = Q(choose(1024, 64), choose(68, 64))
    transfers = {name: (N * b) // D for name, b in
                 [("safe_cap", cap), ("adjacent_cap", cap + 1),
                  ("ordinary_integer", pack.__floor__()),
                  ("ordinary_nested_floor", nested)]}
    ratio = Q(N * nested, D) / T
    expected = {
        "parameters": {"n": 1024, "k": 64, "agreement": 68, "core": 60,
                       "residual_domain": 964, "block": 8, "packing_strength": 4},
        "counts": {"N": N, "D": D, "residual_4_subsets": choose(964, 4),
                   "block_4_subsets": choose(8, 4)},
        "threshold": {"q": q, "denominator": den, "M": M,
                      "remainder": q - den * M},
        "local_caps": {"safe_integer": cap,
                       "safe_cap_division_remainder": cutoff - 1 - N * cap,
                       "exact_real_open_endpoint": rat(Q(cutoff, N)),
                       "conservative_real_closed_endpoint": rat(T * D / N),
                       "ordinary_packing": rat(pack),
                       "ordinary_integer": pack.__floor__(),
                       "ordinary_nested_floor": nested, "nested_stages": stages},
        "nonuniform_endpoint": {"strict_cutoff": cutoff,
                                "greatest_safe_integer_sum": cutoff - 1,
                                "safe_global_floor": (cutoff - 1) // D,
                                "unsafe_global_floor": cutoff // D},
        "global_transfer": {**transfers, "unrounded_packing": rat(N * pack / D),
                            "L001": rat(support), "nested_over_threshold": rat(ratio)},
    }
    comparisons = []

    def compare(actual, wanted, path):
        if isinstance(wanted, dict):
            comparisons.append({"path": path + "/keys", "passed": actual.keys() == wanted.keys()})
            for key, value in wanted.items():
                compare(actual[key], value, path + "/" + key)
        elif isinstance(wanted, list):
            comparisons.append({"path": path + "/length", "passed": len(actual) == len(wanted)})
            for i, value in enumerate(wanted):
                compare(actual[i], value, path + "/" + str(i))
        else:
            comparisons.append({"path": path, "passed": actual == wanted,
                                "actual": actual, "reconstructed": wanted})

    for key, value in expected.items():
        compare(source[key], value, "/" + key)

    tests = {
        "searched_cap": cap == 184665717 and high == 184665718,
        "closed_uniform_safety": passes(cap),
        "adjacent_uniform_failure": not passes(cap + 1),
        "cap_formula": cap == (cutoff - 1) // N,
        "cap_remainder_range": 0 <= cutoff - 1 - N * cap < N,
        "threshold_noninteger": 0 < q - den * M < den,
        "integer_sum_last_safe": (cutoff - 1) // D == M,
        "integer_sum_first_failing": cutoff // D == M + 1,
        "real_sum_below_endpoint": (Q(cutoff) - Q(1, 2)).__floordiv__(D) == M,
        "real_sum_at_endpoint": Q(cutoff, D).__floor__() == M + 1,
        "conservative_real_endpoint": (T * D / N * N / D).__floor__() == M,
        "local_floor_below_next_cap": (Q(cap + 1) - Q(1, 2)).__floor__() == cap,
        "subset_identity_ambient": N * choose(964, 4) == choose(1024, 64) * choose(64, 60),
        "subset_identity_support": D * choose(8, 4) == choose(68, 64) * choose(64, 60),
        "unrounded_transfer": N * pack / D == support,
        "nested_stages": [s["quotient"] for s in stages] == [192, 30784, 4234998, 510317259],
        "nested_below_ordinary": nested <= pack.__floor__(),
        "nested_above_required": nested > cap,
        "both_ordinary_caps_fail": not passes(nested) and not passes(pack.__floor__()),
        "ratio_interval": Q(2763, 1000) < ratio < Q(2764, 1000),
        "source_flags_all_true": len(source["checks"]) == 22 and all(source["checks"].values()),
        "source_failures_empty": source["failures"] == [],
    }
    failures = [c["path"] for c in comparisons if not c["passed"]]
    failures += [name for name, ok in tests.items() if not ok]
    out = here / "sixty-core-threshold-audit-results.json"
    out.write_text(json.dumps({
        "scope": "L034 arithmetic and source-certificate comparison only; symbolic membership audited in L034.",
        "reconstruction": expected, "binary_search": search,
        "source_checks_inspected": source["checks"],
        "comparisons": comparisons, "checks": tests, "failures": failures,
        "summary": {"comparisons": len(comparisons), "checks": len(tests),
                    "required_cap": cap, "adjacent_failing_cap": high,
                    "ordinary_cap": nested, "failures": len(failures)}
    }, indent=2) + "\n")
    print(f"comparisons={len(comparisons)} checks={len(tests)} failures={failures}")
    print(f"required cap <= {cap}; adjacent {high} fails; ordinary cap={nested}")
    print(f"certificate={out.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
