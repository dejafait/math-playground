"""Exact allowance comparisons; analytic reduction is in C033x."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

CAP = 10**6
rows = []
failures = []
for bits in (8, 16, 32, 64):
    eps = F(1, 2**bits)
    cutoff = 4 * eps / 3
    j_bound = 27 * (1-cutoff)**2 / (128 * eps**3)
    j_min = j_bound.numerator // j_bound.denominator + 1
    outer = {}
    for s in (1, 2):
        ks = 42*s*s + 326*s + F(1915, 2)
        n_squared_bound = ks / (16*eps)
        n_min = isqrt(n_squared_bound.numerator // n_squared_bound.denominator) + 1
        if not ((n_min-1)**2 <= n_squared_bound < n_min**2):
            failures.append(f"outer node bound: bits={bits}, s={s}")
        outer[str(s)] = {
            "K_s": str(ks), "n_squared_strict_lower_bound": str(n_squared_bound),
            "minimum_n": n_min,
            "literal_nested_node_lower_bound": n_min * j_min,
        }
    if not (0 < cutoff < 1 and j_bound > CAP and j_min > j_bound):
        failures.append(f"compact cost comparison: bits={bits}")
    rows.append({
        "bits": bits, "epsilon": str(eps), "required_profile_d_strict_upper": str(eps/12),
        "small_cutoff_strict_upper": str(cutoff), "J_strict_lower_bound": str(j_bound),
        "minimum_integer_J": j_min, "total_operational_cap": CAP,
        "one_profile_exceeds_total_cap": j_bound > CAP, "outer": outer,
    })
certificate = {
    "scope": "C033m prescribed compact D=0 allowance, beta=epsilon/4; not actual-error or complexity lower bounds for other evaluators",
    "scalar_entries_required": 8, "scalar_entries_evaluated": 0,
    "matrix_certified": False, "TV_certified": False,
    "analytic_proof": "lemmas/C033x-compact-excision-scalar-preflight-cost-stop.md",
    "rows": rows, "failures": failures,
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate, indent=2) + '\n')
for row in rows:
    print(f"2^-{row['bits']}: required J>{row['J_strict_lower_bound']}; allowed total={CAP}; FAIL budget")
print(f"Exact arithmetic checks: {'PASS' if not failures else 'FAIL'}; failures={failures}")
print(f"Scalars evaluated=0/8; matrix and TV unresolved; certificate={out.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
