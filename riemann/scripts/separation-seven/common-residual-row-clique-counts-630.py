"""Exact registry/PSD-order arithmetic for C999x; no matrix or PSD test.

The support and reconstruction proof is in canonical C999x. This checks
its complete declared-symbol partition against C999w(10), retaining zero
radii. It does not read numerical arrays or assert witness feasibility.
"""
import json
from pathlib import Path


J, d, m, N, K = 1024, 1022, 2044, 512, 65536
high_rows = K - J
# (family, common-core count, count in EACH high-row group).
families = [
    ("Z ratios", d, 0),
    ("t0", 1, 0),
    ("M primitive", J * (J + 1) // 2, J),
    ("T primitive union", J * J, 2 * J),
    ("U primitive", J * J, 0),
    ("Y primitive", d * m, 0),
    ("V fresh", J * d, d),
    ("Fplus fresh", J * d, d),
    ("Fminus fresh", J * d, d),
    ("A fresh before symmetrization", d * d, 0),
    ("B fresh", d * m, 0),
    ("UZ fresh", J * d, 0),
    ("U0 fresh", d * d, 0),
    ("G fresh", J * m, 0),
    ("JY fresh", d * m, 0),
    ("VY fresh", J * m, m),
    ("rminus Z fresh", d, 0),
    ("rplus Z fresh", d, 0),
    ("re G fresh", m, 0),
    ("ro G fresh", m, 0),
    ("Delta head fresh", N * m, 0),
]
core = sum(c for _, c, _ in families)
local = sum(r for _, _, r in families)
p_partition = core + high_rows * local
p0 = (d + 1 + J * (J + 1) // 2 + (K - J) * J
      + 2 * K * J - J * J + J * J + d * m)
p_formula = (p0 + 3 * K * d + 2 * d * d + 2 * d * m
             + J * d + J * m + K * m + 2 * d + 2 * m + N * m)
full_order = (p_formula + 1) * m
core_order = (core + 1) * m
local_order = local * m
largest_order = core_order + local_order
failures = []
if p_partition != p_formula:
    failures.append("partition does not equal C999w(10)")
if local != 3 * J + 3 * d + m:
    failures.append("high-row symbol count mismatch")
if 2 * largest_order > full_order:
    failures.append("largest PSD order exceeds one-half gate")
if m > full_order // 2:
    failures.append("Lambda order exceeds one-half gate")
certificate = {
    "kind": "exact integer count check supporting symbolic proof, not PSD verification",
    "parameters": {"J": J, "d": d, "m": m, "N": N, "K": K},
    "registry_families": [
        {"family": name, "core": c, "per_high_row": r,
         "total": c + high_rows * r} for name, c, r in families
    ],
    "counts": {"p0": p0, "p_formula": p_formula,
               "p_partition": p_partition, "core_symbols": core,
               "per_high_row_symbols": local, "high_rows": high_rows},
    "orders": {"full": full_order, "core": core_order,
               "per_high_row": local_order, "largest_clique": largest_order,
               "each_Lambda": m, "number_of_Lambdas": p_formula,
               "required_largest_at_most": full_order // 2,
               "gate_passes": 2 * largest_order <= full_order},
    "symbolic_support": {
        "core": "all Z,Y, low-row and other symbols; also constant fibre 0",
        "row_n": "M[n,:], T[n,:], T[:,n], fresh V/Fplus/Fminus/VY[n,:]",
        "rho_n_high": "core union row_n",
        "other_P_terms_and_all_equalities": "core",
        "multipliers": "N_i only fibres 0/i; L_a only core/core",
        "cliques": "core fibres union row_n fibres, J <= n < K",
        "elimination": "all high-row groups in ascending n, then core",
    },
    "exact_reconstruction_obligations": {
        "core_core": "sum_n D_n = Q_core_core entrywise",
        "core_row_n": "B_n core,row_n = Q_core,row_n entrywise",
        "row_n_row_n": "B_n row_n,row_n = Q_row_n,row_n entrywise",
        "different_rows": "no clique contains both; Q entries identically zero",
        "fill": "prescribed zero entries in every preceding equality stay zero",
        "positivity": "every B_n and Lambda_i needs an exact rational PSD witness",
    },
    "no_witness_or_floor_established": True,
    "failures": failures,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"RESULT: {'PASS' if not failures else 'FAIL'} registry partition and order gate only")
print(f"p={p_formula}; core={core}; per-row={local}; cliques={high_rows}")
print(f"actual largest PSD order={largest_order}; required <= {full_order // 2}")
print(f"full order={full_order}; each Lambda order={m}; no factors or floor verified")
print(f"failures={failures}; certificate={path.as_posix()}")
raise SystemExit(bool(failures))
