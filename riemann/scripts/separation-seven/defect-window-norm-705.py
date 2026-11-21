"""Exact scalar extraction from C744y's unchanged, audited full certificate.

This does not replay the inherited analytic/computational proof. It checks
its artifact identities and the new rational metric-conversion arithmetic.
No eigensolver, new factor, cutoff choice or parameter search is used.
"""
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "defect-window-norm-705.json"


def main():
    checks = []

    def check(label, value):
        checks.append({"label": label, "passed": bool(value)})

    audit_path = HERE / "matrix-tail-audit-541.json"
    audit = json.loads(audit_path.read_text())
    check("inherited audit failures empty", audit["failures"] == [])
    check("inherited paid floor", F(audit["complete_lower_bound"]) == F(".027998"))
    hashes = []
    for item in audit["input_hashes"]:
        actual = sha256((HERE / item["path"]).read_bytes()).hexdigest()
        passed = actual == item["actual"] == item["expected"] and item["passed"]
        hashes.append({"path": item["path"], "sha256": actual, "passed": passed})
        check("unchanged " + item["path"], passed)

    # All constants below are exact rational upper/lower bounds from the
    # canonical proofs, not rounded values read from a numerical eigensolver.
    tau, delta, tnorm = F("1.43"), F(".027998"), F("4.71")
    sqrt_count_upper = F(5770)
    check("finite rectangle square-root upper", sqrt_count_upper**2 > 65024 * 512)
    ef_upper = F(".000000181") + 3 * sqrt_count_upper * F(".0000001")
    finite_factor_upper = F("3.162") + ef_upper
    # ||Z||^2=256, hence ||U||=256/5000+1/125000.
    u_norm = F(256, 5000) + F(1, 125000)
    full_factor_squared_upper = finite_factor_upper**2 + u_norm
    f2 = F("10.061")
    check("orthogonal finite/high covariance bound", full_factor_squared_upper < f2)

    def condition(m):
        return (delta - m) * tau * (tau - m) - m * f2

    # Monotonicity of delta-m-m*f2/[tau*(tau-m)] gives a unique
    # admissibility endpoint in (0,delta). Bracket it on a fixed 1e-9
    # rational grid. This extracts a scalar bound, not a certificate retry.
    scale = 10**9
    lo, hi = 0, int(delta * scale)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if condition(F(mid, scale)) >= 0:
            lo = mid
        else:
            hi = mid
    mlo, mhi = F(lo, scale), F(hi, scale)
    check("positive full L2 floor", 0 < mlo < mhi < tau)
    check("admissible lower root bracket", condition(mlo) > 0)
    check("inadmissible upper root bracket", condition(mhi) < 0)
    kappa = tnorm / (tnorm + mlo)
    kappa_method_lower = tnorm / (tnorm + mhi)
    norm_squared_upper = kappa**2
    required = F(3, 4)
    check("strict normalized contraction", norm_squared_upper < 1)
    check("reported outward norm square", norm_squared_upper < F(".998001"))
    check("scalar method cannot reach window threshold",
          kappa_method_lower**2 > required)
    failures = [c["label"] for c in checks if not c["passed"]]

    certificate = {
        "scope": "C744y scalar full-covariance/energy-metric extraction only; fixed tau-window=1/4",
        "classification": "REPRODUCTION; local specialization of imported block/form methods",
        "inherited_audit_sha256": sha256(audit_path.read_bytes()).hexdigest(),
        "inherited_artifacts": hashes,
        "exact_inputs": {"tau": str(tau), "paid_head_floor": str(delta),
                         "T_norm_upper": str(tnorm), "finite_factor_norm_sum_upper": "1581/500",
                         "eQ_upper": ".000000181", "Z_norm_squared": 256},
        "exact_extraction": {"eF_upper": str(ef_upper),
                             "finite_factor_upper": str(finite_factor_upper),
                             "U_norm": str(u_norm),
                             "full_factor_squared_upper": str(full_factor_squared_upper),
                             "rounded_full_factor_squared_upper": str(f2),
                             "L2_floor_lower": str(mlo), "scalar_optimum_upper": str(mhi),
                             "lower_condition_numerator": str(condition(mlo)),
                             "upper_condition_numerator": str(condition(mhi)),
                             "relative_energy_margin_lower": str(mlo / (mlo + tnorm)),
                             "R_norm_upper": str(kappa),
                             "R_norm_squared_upper": str(norm_squared_upper),
                             "scalar_method_norm_squared_lower_endpoint": str(kappa_method_lower**2),
                             "defect_floor_lower": str(1 - norm_squared_upper)},
        "window_test": {"required_strict_norm_squared_upper": str(required),
                        "upper_bound_crosses_required_threshold": norm_squared_upper < required,
                        "interpretation": "Threshold missed by this scalarized comparison; actual windows neither empty nor nonempty certified."},
        "checks": checks, "failures": failures,
        "qualifications": "Inherits C744v/w/y analytic and IEEE754/Decimal contracts and C744z restricted-form/core setup; no upstream replay, sharp projector, full S3 sign, H2 or Xi transfer. c_* source certificate remains unreplayed."
    }
    OUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"exact checks={len(checks)}, failures={failures}")
    print(f"L2 floor bracket=({float(mlo):.9f},{float(mhi):.9f}); ||R||^2 <= {float(norm_squared_upper):.12f} < .998001")
    print("required ||R||^2 < .75: NOT REACHED; actual window relevance unresolved")
    print(f"certificate: {OUT.relative_to(HERE.parent.parent)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
