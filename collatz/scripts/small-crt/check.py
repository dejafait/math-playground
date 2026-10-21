"""Bounded exact diagnostic; no inference about infinitely many horizons."""
import json
from fractions import Fraction
from pathlib import Path


def direct_root(ell):
    binary = 2 ** (ell + 1)
    ternary = 3 ** (ell + 4)
    u = (-3904 * pow(81 * ternary, -1, binary)) % binary
    return (47 + ternary * u) % (binary * ternary)


rows = []
failures = []
hits = {str(b): [] for b in range(4)}
run = 0
root = direct_root(6)
for ell in range(6, 257):
    modulus = 162 * 6 ** ell
    lower = 4 ** ell
    n = root + modulus * ((lower - root) // modulus + 1)
    a = (root - 47) // 3 ** (ell + 4)
    c = (81 * root + 97) // 2 ** (ell + 1)
    digits = [d for d in range(6)
              if (a + d * 2 ** (ell + 1)) % 3 == 0
              and (c + d * 3 ** (ell + 8)) % 2 == 0]
    checks = {
        "range": 0 <= root < modulus,
        "ternary_congruence": (root - 47) % 3 ** (ell + 4) == 0,
        "binary_congruence": (81 * root + 97) % 2 ** (ell + 1) == 0,
        "independent_formula": root == direct_root(ell),
        "unique_digit": len(digits) == 1,
        "strict_guarded_selection": lower < n <= lower + modulus,
        "selected_root_congruences": ((n - 47) % 3 ** (ell + 4) == 0
                                     and (81 * n + 97) % 2 ** (ell + 1) == 0),
    }
    for name, passed in checks.items():
        if not passed:
            failures.append({"L": ell, "check": name})
    digit = digits[0]
    bounds = {}
    for b in range(4):
        upper = 6 ** (ell - b)
        passed = n <= upper
        bounds[str(b)] = {"required_upper": upper, "selected_n": n,
                          "hit": passed}
        if passed:
            hits[str(b)].append(ell)
    rows.append({"L": ell, "r": root, "M": modulus,
                 "required_strict_lower": lower, "least_guarded_n": n,
                 "r_above_lower": root > lower,
                 "carry_a": a, "carry_c": c, "next_digit": digit,
                 "zero_run_ending_here": run, "checks": checks,
                 "bounds": bounds})
    if ell < 256:
        root += digit * modulus
        run = run + 1 if digit == 0 else 0

best = min((row for row in rows if row["r_above_lower"]),
           key=lambda row: Fraction(row["r"], 6 ** row["L"]))
ratio = Fraction(best["r"], 6 ** best["L"])
max_run = max(row["zero_run_ending_here"] for row in rows)
summary = {
    "range": [6, 256], "rows": len(rows), "failures": failures,
    "hit_L_by_integer_B": hits,
    "max_observed_zero_run": max_run,
    "max_run_end_L": [row["L"] for row in rows
                      if row["zero_run_ending_here"] == max_run],
    "guard_failures_for_least_representative": [row["L"] for row in rows
                                                if not row["r_above_lower"]],
    "minimum_guarded_normalized_height": {
        "L": best["L"], "numerator": ratio.numerator,
        "denominator": ratio.denominator,
        "display_only_approximation": float(ratio),
        "required_for_B0": 1, "required_for_B1": "1/6"},
    "scope": "Finite exact diagnostic only; infinite assertion unresolved.",
}
path = Path(__file__).with_name("certificate.json")
path.write_text(json.dumps({"summary": summary, "rows": rows}, indent=2) + "\n")
print(f"Checked {len(rows)} horizons, L=6..256; failures: {len(failures)}")
print(f"Longest observed zero run: {max_run}")
print(f"Hits by integer B (required 4^L < n <= 6^(L-B)): {hits}")
print(f"Minimum guarded r/6^L: approximately {float(ratio):.10g}, "
      f"at L={best['L']}; required <=1 for B=0, <=1/6 for B=1")
print(f"Complete exact certificate: {path}")
if failures:
    raise SystemExit(1)
