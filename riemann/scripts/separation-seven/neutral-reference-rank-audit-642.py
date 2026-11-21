#!/usr/bin/env python3
"""Audit the saved640 witness with integer-lifted exact arithmetic.

No eigensolver, proposed new witness, analytic premise, or source mutation.
NumPy only decodes and checks the pinned binary64 archive.
"""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
EXPECTED = {
    "joint-galerkin-family-certificate-598.npz": "f5035b5e28bf85b7b8329a6675f910a8545208ad931bb983938ee14f30970876",
    "joint-galerkin-family-certificate-598.json": "42a2b96a000ec519cb926a752e32bf364c3e880cfb06436d59a6ecc4cdbfb290",
    "joint-galerkin-family-ledger-598.json": "d531db86b4b1c98ae9e41a9c973d8d5528336c7e6e6b0649c921b16df587dce2",
}
checks, failures, pins = [], [], {}
report = {
    "target": "Audit C999y's restricted-form inverse identity, correction rank, and exact three-dimensional stop for the unchanged certificate598 repair.",
    "checks": checks, "failures": failures, "input_sha256": pins,
    "qualification": "Exact fixed lower-matrix obstruction only. Analytic applicability is the separate canonical conditional proof; no598 analytic revalidation or actual-form sign follows.",
}


def sha(name):
    return hashlib.sha256((BASE / name).read_bytes()).hexdigest()


def check(ok, name):
    checks.append({"check": name, "passed": bool(ok)})
    if not ok:
        raise ValueError(name)


def pin(name, expected=None):
    pins[name] = sha(name)
    if expected is not None:
        check(pins[name] == expected, "pin " + name)


def decode(v):
    return Q(int(v["numerator"]), int(v["denominator"]))


def encode(v):
    return {"numerator": str(v.numerator), "denominator": str(v.denominator)}


def matrix_encode(a):
    return [[encode(v) for v in row] for row in a]


def dd(a):
    return [a[i][i] - sum(abs(a[i][j]) for j in range(3) if j != i)
            for i in range(3)]


def minors(a):
    return [a[0][0], a[0][0]*a[1][1]-a[0][1]*a[1][0],
            a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]
            +a[0][2]*a[1][0]*a[2][1]-a[0][2]*a[1][1]*a[2][0]
            -a[0][1]*a[1][0]*a[2][2]-a[0][0]*a[1][2]*a[2][1]]


try:
    for name, expected in EXPECTED.items():
        pin(name, expected)
    saved_name = "neutral-reference-rank-obstruction-640.json"
    pin(saved_name)
    saved = json.loads((BASE / saved_name).read_text())
    pin("neutral-reference-rank-obstruction-640.py", saved["script_sha256"])
    check(saved["input_sha256"] == EXPECTED, "all three saved640 input pins")
    check(saved["failures"] == [] and all(c["passed"] for c in saved["checks"]),
          "saved640 checks and failures")
    check(saved["result"] == "FIXED_LOWER_MATRIX_RANK_TWO_REPAIR_IMPOSSIBLE",
          "saved640 result label")
    cert = json.loads((BASE / "joint-galerkin-family-certificate-598.json").read_text())
    ledger = json.loads((BASE / "joint-galerkin-family-ledger-598.json").read_text())
    check(cert["archive"]["sha256"] == EXPECTED["joint-galerkin-family-certificate-598.npz"],
          "598 certificate archive pin")
    check(ledger["certificate_sha256"] == EXPECTED["joint-galerkin-family-certificate-598.json"],
          "598 ledger certificate pin")
    pin("joint-galerkin-family-certificate-598.py", cert["script_sha256"])
    pin("joint-galerkin-family-ledger-598.py", ledger["script_sha256"])
    for name, expected in cert["input_hashes"].items():
        pin(name, expected)
    failed598 = [c["label"] for c in cert["checks"] if not c["passed"]]
    check(failed598 == cert["failures"] == ["quarter_comparison factor unavailable"],
          "only original final-factor failure; retained")
    check(ledger["failures"] == [] and all(c["passed"] for c in ledger["checks"]),
          "598 recorded ledger checks (not an analytic replay)")
    blocks = cert["ledger"]["row_blocks"]
    check(len(blocks) == 126 and all(b["first"] == 1024+512*j and
          b["last"] == 1535+512*j for j, b in enumerate(blocks)),
          "saved allowance partition includes every row1024:65535")
    with np.load(BASE / "joint-galerkin-family-certificate-598.npz", allow_pickle=False) as archive:
        m = archive["comparison_lower"]
        check(m.dtype == np.dtype("float64") and m.shape == (2044, 2044),
              "complete exact binary64 lower matrix")
        check(np.isfinite(m).all() and np.array_equal(m, m.T), "full finite symmetry")
        check(np.count_nonzero(archive["quarter_metric_upper"]) == 0,
              "598 target is the Euclidean floor; no quarter-metric subtraction")
        w = saved["witness"]
        support = w["support_indices_zero_based"]
        integers, den = w["integer_columns_by_row"], w["denominator"]
        check(w["ambient_dimension"] == 2044 and w["omitted_coordinates"] == "exactly zero",
              "full2044 zero extension")
        check(support == list(range(16)) + list(range(1022, 1038)),
              "both endpoint supports exactly as claimed")
        check(den == 2**24 and len(integers) == 32 and all(len(row) == 3 and
              all(type(v) is int for v in row) for row in integers), "all96 saved integers")
        # Independent algorithm: lift the entire principal matrix to a common
        # integer denominator, contract with integer columns, then divide once.
        ratios = [[float(m[i, j]).as_integer_ratio() for j in support] for i in support]
        common = max(d for row in ratios for _, d in row)
        check(common & (common-1) == 0 and all(common % d == 0 for row in ratios for _, d in row),
              "exact common dyadic denominator")
        lifted = [[n*(common//d) for n, d in row] for row in ratios]
    t = Q(999, 10**6)
    check(decode(saved["required_floor"]) == t, "exact requested floor999/10^6")
    gram, shifted = [], []
    for a in range(3):
        gram.append([])
        shifted.append([])
        for b in range(3):
            g = Q(sum(row[a]*row[b] for row in integers), den**2)
            z = Q(sum(integers[i][a]*lifted[i][j]*integers[j][b]
                      for i in range(32) for j in range(32)), common*den**2)-t*g
            gram[a].append(g)
            shifted[a].append(z)
    check(matrix_encode(gram) == saved["exact"]["gram"], "all nine exact Gram entries match")
    check(matrix_encode(shifted) == saved["exact"]["shifted_compression"],
          "all nine exact shifted compression entries match")
    negative = [[-x for x in row] for row in shifted]
    gd, nd = dd(gram), dd(negative)
    check(min(gd) == Q(281474955222765, 281474976710656), "canonical exact Gram bound")
    check(min(nd) == Q(72695772437179941380714963210255091,
                      811296384146066816957890051440640000), "canonical exact negative bound")
    check(min(gd) > Q(999, 1000), "strict Gram floor.999")
    check(min(nd) > Q(8, 100), "strict negative-compression floor.08")
    for key, a in [("gram", gram), ("negative_shifted_compression", negative)]:
        values = minors(a)
        check([encode(x) for x in values] == saved["exact"]["leading_principal_determinants"][key]
              and all(x > 0 for x in values), "all alternate exact minors " + key)
    check(decode(saved["exact"]["gram_diagonal_dominance_lower"]) == min(gd)
          and decode(saved["exact"]["negative_compression_diagonal_dominance_lower"]) == min(nd),
          "saved strict bounds match")
    report["witness"] = w
    report["exact"] = {"common_matrix_denominator": str(common), "gram": matrix_encode(gram),
        "shifted_compression": matrix_encode(shifted),
        "gram_row_bounds": [encode(v) for v in gd], "negative_row_bounds": [encode(v) for v in nd],
        "gram_actual": encode(min(gd)), "gram_required_strict": encode(Q(999, 1000)),
        "negative_actual": encode(min(nd)), "negative_required_strict": encode(Q(8, 100)),
        "target_floor": encode(t)}
    report["original598_failures"] = cert["failures"]
    report["retained_allowances"] = {key: cert["bounds"][key] for key in
        ["trial_error", "head_inverse_matrix_error", "finite_covariance_error",
         "complete_tail_remainder", "exact_predictor_covariance_error"]}
    check(all(sha(name) == value for name, value in pins.items()), "all original artifacts unchanged")
    report["result"] = "PASS_FIXED_LOWER_MATRIX_RANK_TWO_STOP"
except Exception as exc:
    failures.append(type(exc).__name__ + ": " + str(exc))
    report["result"] = "INCONCLUSIVE"
report["script_sha256"] = sha(Path(__file__).name)
out = BASE / "neutral-reference-rank-audit-642.json"
out.write_text(json.dumps(report, indent=2) + "\n")
print("Result:", report["result"])
if "exact" in report:
    print("Gram actual:", float(min(gd)), "required > .999")
    print("Negative shifted compression actual:", float(min(nd)), "required > .08")
print("Target floor: 999/1000000; failures:", failures)
print("Full certificate:", out.relative_to(BASE.parent.parent))
raise SystemExit(bool(failures))
