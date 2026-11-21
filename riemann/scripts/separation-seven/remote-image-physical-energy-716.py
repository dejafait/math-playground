#!/usr/bin/env python3
"""Exact small budget/count check; no scalar, h-value or Gram evaluation."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / "remote-image-physical-energy-716.json"
WITNESS = BASE / "defect-window-fixed-pair-707-witness.json"
PIN = "99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a"
checks = []


def check(label, condition):
    checks.append({"label": label, "passed": bool(condition)})


M, B, Bprime = 2**20, 2**23, 2**24
A = M * B
delta, outer, inner = Q(1, 2**70), 2**76, 2**83
check("witness unchanged", sha256(WITNESS.read_bytes()).hexdigest() == PIN)
check("zero-extension variation includes both traces", 2**22 + 2*M < B)
check("cutoff variation below uniform mollified bound", B + 2*M < Bprime)
check("correlation Lipschitz majorant", A == 2**43)
check("uniform cosine coefficient constant", 4*Bprime == 2**26)
check("difference coefficient dominated by2^27", 2**26 + 2**24 < 2**27)
check("delta lies inside interval ell>1/2", 0 < delta < Q(1, 2))
near = A * (delta + delta**2)
near_cap = Q(1, 2**26)
check("omitted diagonal bound", near < near_cap)
variation = A * (2*72 + 2)
check("outer variation cap", variation < 2**51)
outer_error = Q(variation, 2*outer)
outer_cap = Q(1, 2**26)
check("outer midpoint error", outer_error < outer_cap)
product_var = 2*M*B
epsilon = Q(A, inner)
check("product variation bound", product_var == 2**44)
check("uniform inner error", Q(product_var, 2*inner) == epsilon == Q(1, 2**40))
kernel_midpoint_extra = Q(1, 1) / (delta*outer)
check("kernel mass error", kernel_midpoint_extra == Q(1, 64))
check("sampled mass below128", 72 + kernel_midpoint_extra < 128)
check("scalar coefficient cap", 513 + 8 == 521 < 2**10)
norm_cap = 2**10 * epsilon
inside_cap = 256 * epsilon
check("external norm budget", norm_cap == Q(1, 2**30))
check("inner correlations budget", inside_cap == Q(1, 2**32))
ideal_cap = near_cap + outer_cap + norm_cap + inside_cap
check("complete ideal discretization budget", ideal_cap == Q(133, 2**32))
check("ideal bound below2^-24 and required1e-6", ideal_cap < Q(1, 2**24) < Q(1, 10**6))
calls = inner * (2*outer + 1)
check("exact prescribed streaming h requests", calls == 2**160 + 2**83)
check("request count exceeds2^160", calls > 2**160)
failures = [c["label"] for c in checks if not c["passed"]]
unpaid = [
    "Enclosed nodes and all jump-boundary cases at those nodes",
    "All334 shift weights and the exact completed cosine profile",
    "Entire K14 image and suffix",
    "Both exact projection moments and inverse Gram matrix",
    "Scalar d0, exact support-tail scalar J and kernel node values",
    "Uniform h-value error and all accumulated rounding",
    "Sufficient arithmetic precision, actual byte storage and total elementary work",
]
result = {
    "scope": "Small exact budget/count replay only; analytic proof is prose in C998t",
    "witness_sha256": PIN,
    "checks": checks,
    "failures": failures,
    "bounds": {
        "supremum": M, "full_line_variation": B,
        "uniform_approximant_variation": Bprime, "correlation_lipschitz": A,
        "delta": str(delta), "outer_variation": variation,
        "near_error_bound": str(near), "outer_error_bound": str(outer_error),
        "uniform_inner_error_bound": str(epsilon),
        "sampled_kernel_mass_bound": str(72 + kernel_midpoint_extra),
        "external_norm_error_cap": str(norm_cap),
        "inner_correlations_error_cap": str(inside_cap),
        "ideal_discretization_error_cap": str(ideal_cap),
        "required_total_scalar_error": "1/1000000",
        "proved_total_finite_arithmetic_error": None,
    },
    "work": {
        "outer_nodes": outer, "inner_nodes": inner,
        "ideal_h_value_requests": calls, "kernel_value_requests": outer,
        "inner_products": inner*(outer+1),
        "model": "Exact-value oracle; specified streaming loop recomputes base h values",
        "working_storage": "Constant number of exact scalar accumulators/nodes plus fixed profile description",
        "sufficient_precision": None, "actual_byte_storage": None,
        "total_elementary_operation_bound": None,
        "full_batch_executed": False, "scalar_evaluated": False,
        "gram_evaluated": False,
    },
    "unpaid": unpaid,
    "decision": "Park this sufficient nested midpoint prescription; retain unaudited full-form identity",
    "limitations": [
        "No necessary complexity bound or actual-error lower bound",
        "No complete executable absolute1e-6 scalar certificate",
        "No sign, new general theorem or RH conclusion",
        "No software validation of the analytic BV-to-form bridge",
    ],
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(f"Checks: {len(checks)}; failures: {failures}")
print(f"Ideal discretization cap: {ideal_cap} < required total tolerance 1/1000000")
print("Finite arithmetic: UNPAID; complete scalar certificate: NOT ESTABLISHED")
print(f"Prescribed h-value requests: {calls} > 2^160; large batch: not run")
print(f"Certificate: {OUT.relative_to(BASE.parent.parent)}")
if failures:
    raise SystemExit(1)
