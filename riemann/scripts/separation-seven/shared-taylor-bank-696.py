#!/usr/bin/env python3
"""Exact finite planning evidence for C998p, never a square-value certificate."""
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "shared-taylor-bank-696.json"
checks = []


def enc(x):
    x = F(x)
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def ck(name, value):
    checks.append({"name": name, "pass": bool(value)})


b, K, A = F(1, 8), 192, 2**18
c_error, D_error = F(1, 2**1024), F(1, 2**760)
c_tail = 2 * F(1, 3)**1025 / (1025 * (1-F(1, 9)))
D_tail = F(1, 2**768) / 769**2 + c_error
ck("512-term log2 positive tail", c_tail < c_error)
ck("768-term D(1) transformed tail including log2", D_tail < D_error)
ck("A1 truncation auxiliary smallness", 8*b**K < 1)

bank_rows = []
max_bank = F()
for p in range(2, 257, 2):
    q = p+K+1
    trunc = 32*b**(K+1)*(F(4, q)+F(1, q*q))
    constant = 16*(c_error+D_error)
    error = trunc+constant
    ck(f"bank power{p} truncation < 2^-571", trunc < F(1, 2**571))
    ck(f"bank power{p} complete analytic error < 2^-570", error < F(1, 2**570))
    bank_rows.append({"power": p, "nonreciprocal_truncation_upper": enc(trunc),
                      "constant_substitution_upper": enc(constant),
                      "nonreciprocal_bank_error_upper": enc(error),
                      "reciprocal_bank_error": enc(0)})
    max_bank = max(max_bank, error)

p = 258
weighted_masses = {
    "Qbar": b*(F(25, 2*(p+1))+F(5, (p+1)**2)+F(1, (p+1)**3)),
    "Abar1": b*(F(4, p+1)+F(1, (p+1)**2)),
    "Abar2": b*(F(4, p+1)+F(1, (p+1)**2)),
    "1/z": F(1, p), "-1/z^2": 1/(b*(p-1)),
    "1/(1+z)": b/(p+1), "-1/(1+z)^2": b/(p+1)
}
for name, value in weighted_masses.items():
    ck(f"Taylor remainder absolute weighted mass {name} < 1", value < 1)
taylor = F(64**258, factorial(258))
ck("uniform Taylor remainder < 2^-150", taylor < F(1, 2**150))
ck("dotted Taylor prefactor no larger", F(129, 512**2) < 1)
endpoint = taylor + 2**96*max_bank
ck("endpoint bank plus Taylor < 2^-149", endpoint < F(1, 2**149))

panels = []
interior = F()
for j, N in ((1, 117), (2, 81), (3, 63)):
    left = F(1, 2**j)
    ck(f"panel{j} degree balance", 2*(N-1) == 88+288*left)
    ck(f"panel{j} holomorphic prefactor", left**2*(j+3)**2 <= 4)
    error = F(32, 45)*left*F(1, 2**65)
    interior += error
    panels.append({"j": j, "left": enc(left), "right": enc(2*left),
                   "nodes": N, "ideal_error_upper": enc(error)})
ck("interior exactly covers [1/8,1]", sum((F(1, 2**j) for j in (1,2,3)), F()) == 1-b)
eps = interior+endpoint
ck("complete ideal moment error < 2^-64", eps < F(1, 2**64))
ck("both W endpoints off-diagonal bound", 10*A+1028+4*eps < 2**22)
ck("both V endpoints all positive diagonal bound", 5*A+521+4*eps < 2**22)

archive = HERE / "frozen-reference-proposal-652.npz"
pin = "2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6"
ck("complete frozen witness archive hash", sha256(archive.read_bytes()).hexdigest() == pin)
with np.load(archive, allow_pickle=False) as z:
    free = z["free_middle_dyadics"].copy()
ck("762 finite binary64 free coefficients", free.shape == (254, 3)
   and free.dtype == np.dtype("float64") and np.isfinite(free).all())
columns = [[F(*float(x).as_integer_ratio()) for x in free[:, j]] for j in range(3)]
masses = [sum(map(abs, col), F()) for col in columns]
pairs = []
for j, m in enumerate(masses):
    ck(f"column{j} free l1 < 7/3", m < F(7, 3))
    ck(f"column{j} exact completed l1 <= 2M < 8", 2*m < 8)
for i in range(3):
    for j in range(3):
        error = 4*masses[i]*masses[j]*2**21*eps
        ck(f"ideal complete square entry{i}{j} < 2^-37", error < F(1, 2**37))
        pairs.append({"i": i, "j": j, "ideal_error_upper": enc(error)})
ck("ideal allowance below required 1e-10", F(1, 2**37) < F(1, 10**10))

# Give the three exact midpoint nodes away in both dots and primitives.
retained_nodes, families, modes, terms = 258, 14, 255, 128
interval_dot_cost = lambda count: 8*count-4
work = {
    "audited_C998o_setup": 3290939,
    "interior_interval_dots_258_nodes": families*modes*interval_dot_cost(retained_nodes),
    "endpoint_interval_dots_128_terms": families*modes*interval_dot_cost(terms),
    "three_D_Horner_pairs_258_nodes": 3*retained_nodes*8*(768-1),
    "three_log_Horner_pairs_258_nodes": 3*retained_nodes*8*(512-1),
}
total = sum(work.values())
required = 20000000
ck("mandatory prescribed prefix exceeds full cap", total > required)
ck("exact node and bank counts", 117+81+63 == 261 and len(bank_rows) == 128)
failures = [c["name"] for c in checks if not c["pass"]]
report = {
    "result": "PRESCRIPTION_WORK_STOP" if not failures else "FAILED_PLANNING_CHECK",
    "scope": "Finite bank formula error and exact-node/constant-density ideal contraction; mandatory interval-program prefix only",
    "prescription": {"b": enc(b), "Taylor_terms": 128, "weight_series_terms": K,
                     "log_terms": 512, "Li2_terms": 768, "panels": panels,
                     "scalar_model": "each arithmetic operation plus destination assignment costs 2; comparisons cost 1",
                     "free_midpoint_nodes_in_work_lower_bound": 3},
    "bank": {"rows": bank_rows, "uniform_error_bound": enc(F(1, 2**570)),
             "maximum_computed_bound": enc(max_bank), "log2_tail": enc(c_tail),
             "D1_tail_upper": enc(D_tail), "actual_bank_evaluated": False},
    "error": {"weighted_remainder_mass": {k: enc(v) for k,v in weighted_masses.items()},
              "Taylor_remainder_upper": enc(taylor), "endpoint_upper": enc(endpoint),
              "interior_ideal_upper": enc(interior), "complete_ideal_moment_upper": enc(eps),
              "complete_ideal_square_pairs": pairs,
              "finite_interior_and_density_coefficient_error_paid": False},
    "coefficients": {"archive_sha256": pin, "exact_free_columns": [[enc(x) for x in col] for col in columns],
                     "free_l1": [enc(x) for x in masses],
                     "exact_Z_computation_paid": False},
    "work": {"categories": work, "mandatory_lower_bound": total, "required_upper_bound": required,
             "excess": total-required,
             "omitted": ["all bank generation", "all coefficient and constant preparation", "all division guards",
                         "three midpoint nodes", "D/log transformations and tails", "trigonometric evaluation",
                         "node uncertainty propagation", "moment-to-entry assembly", "exact Z", "final contraction"]},
    "service_failures": ["mandatory work exceeds 20000000", "finite interior/primitive/density/Z errors remain unpaid",
                         "no square entry or complete residual has been evaluated"],
    "checks": checks, "failures": failures,
}
OUT.write_text(json.dumps(report, indent=2)+"\n")
print("result:", report["result"])
print("checks:", len(checks), "failures:", failures)
print("bank error < 2^-570; endpoint error < 2^-149; ideal square error < 2^-37 < 1e-10")
print("mandatory scalar work:", total, "required <=", required, "excess:", total-required)
print("certificate:", OUT.relative_to(HERE.parent.parent))
raise SystemExit(bool(failures))
