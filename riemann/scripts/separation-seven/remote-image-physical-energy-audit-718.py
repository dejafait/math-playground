#!/usr/bin/env python3
"""Replay716 without overwriting it; independently check its complete ideal ledger.

No h, scalar, Gram, quadrature grid or inherited source certificate is evaluated.
The analytic audit is canonical in C998t Section6, not established by this script.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from io import StringIO
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "remote-image-physical-energy-716.py"
OLD = BASE / "remote-image-physical-energy-716.json"
REPLAY = BASE / "remote-image-physical-energy-replay-718.json"
OUT = BASE / "remote-image-physical-energy-audit-718.json"
WITNESS = BASE / "defect-window-fixed-pair-707-witness.json"
PIN = "99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


pins_before = {p.name: digest(p) for p in (SOURCE, OLD, WITNESS)}
archived = json.loads(OLD.read_text())
source = SOURCE.read_text()
old_name = 'OUT = BASE / "remote-image-physical-energy-716.json"'
new_name = 'OUT = BASE / "remote-image-physical-energy-replay-718.json"'
if source.count(old_name) != 1:
    raise RuntimeError("Replay redirection is not unique; originals untouched")
replay_stdout = StringIO()
with redirect_stdout(replay_stdout):
    exec(compile(source.replace(old_name, new_name), str(SOURCE), "exec"),
         {"__file__": str(SOURCE), "__name__": "audit718_replay"})
replayed = json.loads(REPLAY.read_text())

# Separate exact reconstruction from the prose's fixed exponents. No values
# are read from the original certificate to construct the expected ledger.
m, b, bp = 1048576, 8388608, 16777216
a = m*b
d = F(1, 1180591620717411303424)
n, k = 75557863725914323419136, 9671406556917033397649408
v = a*146
near, outer = a*d*(1+d), F(v, 2*n)
eps = F(a, k)
mass = F(72)+1/(d*n)
norm, inside = 1024*eps, 256*eps
cap = F(2, 2**26)+norm+inside
calls = k+2*k*n

# Each original predicate is recomputed, rather than accepting stored true flags.
predicates = [
    ("witness unchanged", digest(WITNESS) == PIN),
    ("zero-extension variation includes both traces", 4194304+2*m < b),
    ("cutoff variation below uniform mollified bound", b+2*m < bp),
    ("correlation Lipschitz majorant", a == 8796093022208),
    ("uniform cosine coefficient constant", 4*bp == 67108864),
    ("difference coefficient dominated by2^27", 67108864+16777216 < 134217728),
    ("delta lies inside interval ell>1/2", 0 < d < F(1, 2)),
    ("omitted diagonal bound", near < F(1, 67108864)),
    ("outer variation cap", v < 2251799813685248),
    ("outer midpoint error", outer < F(1, 67108864)),
    ("product variation bound", 2*m*b == 17592186044416),
    ("uniform inner error", F(2*m*b, 2*k) == eps == F(1, 1099511627776)),
    ("kernel mass error", 1/(d*n) == F(1, 64)),
    ("sampled mass below128", mass < 128),
    ("scalar coefficient cap", 513+8 == 521 < 1024),
    ("external norm budget", norm == F(1, 1073741824)),
    ("inner correlations budget", inside == F(1, 4294967296)),
    ("complete ideal discretization budget", cap == F(133, 4294967296)),
    ("ideal bound below2^-24 and required1e-6", cap < F(1, 16777216) < F(1, 1000000)),
    ("exact prescribed streaming h requests", calls == 2**160+2**83),
    ("request count exceeds2^160", calls > 2**160),
]
checks = []


def check(label, condition, actual=None, required=None):
    checks.append({"label": label, "passed": bool(condition),
                   "actual": actual, "required": required})


expected_checks = [{"label": label, "passed": bool(value)} for label, value in predicates]
for label, passed in predicates:
    check("independent716: "+label, passed, bool(passed), True)
check("all21 checks and labels agree", archived["checks"] == expected_checks,
      archived["checks"], expected_checks)
check("full replay equals archived certificate", replayed == archived)
check("archived and replayed failure lists empty",
      archived["failures"] == replayed["failures"] == [])
expected_bounds = {
    "supremum": m, "full_line_variation": b,
    "uniform_approximant_variation": bp, "correlation_lipschitz": a,
    "delta": str(d), "outer_variation": v,
    "near_error_bound": str(near), "outer_error_bound": str(outer),
    "uniform_inner_error_bound": str(eps), "sampled_kernel_mass_bound": str(mass),
    "external_norm_error_cap": str(norm), "inner_correlations_error_cap": str(inside),
    "ideal_discretization_error_cap": str(cap),
    "required_total_scalar_error": "1/1000000",
    "proved_total_finite_arithmetic_error": None,
}
check("complete bounds mapping", archived["bounds"] == expected_bounds,
      archived["bounds"], expected_bounds)
expected_work = {
    "outer_nodes": n, "inner_nodes": k, "ideal_h_value_requests": calls,
    "kernel_value_requests": n, "inner_products": k*(n+1),
    "model": "Exact-value oracle; specified streaming loop recomputes base h values",
    "working_storage": "Constant number of exact scalar accumulators/nodes plus fixed profile description",
    "sufficient_precision": None, "actual_byte_storage": None,
    "total_elementary_operation_bound": None,
    "full_batch_executed": False, "scalar_evaluated": False, "gram_evaluated": False,
}
check("complete work and unpaid finite-arithmetic mapping",
      archived["work"] == expected_work, archived["work"], expected_work)
check("seven unpaid obligations retained", len(archived["unpaid"]) == 7,
      archived["unpaid"], "All seven obligations; prose independently reviewed718")
check("witness hash field matches actual pin", archived["witness_sha256"] == digest(WITNESS) == PIN)
check("unrounded ideal subtotal below recorded cap", near+outer+norm+inside < cap,
      str(near+outer+norm+inside), str(cap))
pins_after = {p.name: digest(p) for p in (SOURCE, OLD, WITNESS)}
check("source, old certificate and witness unchanged", pins_before == pins_after,
      pins_after, pins_before)

failures = [item["label"] for item in checks if not item["passed"]]
result = {
    "scope": "Independent exact budget/count audit plus output-redirected716 replay; no analytic proof by software",
    "checks": checks, "failures": failures,
    "original_checks_recomputed": len(predicates), "audit_check_count": len(checks),
    "pins_before": pins_before, "pins_after": pins_after,
    "replay_stdout": replay_stdout.getvalue(),
    "bounds": expected_bounds, "work": expected_work, "unpaid": archived["unpaid"],
    "decision": "Uphold the limited ideal ledger and preserve fixed prescription cost stop716",
    "analytic_evidence": "lemmas/C998t-fixed-remote-image-compensated-physical-energy.md Section6",
    "limitations": archived["limitations"],
}
OUT.write_text(json.dumps(result, indent=2)+"\n")
print(f"Original checks independently recomputed: {len(predicates)}; audit checks: {len(checks)}; failures: {failures}")
print(f"Ideal cap: {cap} < required 1/1000000; finite arithmetic: UNPAID")
print(f"Fixed-loop requests: {calls} = 2^160+2^83; scalar/Gram/grid: not evaluated")
print(f"Audit: {OUT.relative_to(BASE.parent.parent)}; replay: {REPLAY.relative_to(BASE.parent.parent)}")
if failures:
    raise SystemExit(1)
