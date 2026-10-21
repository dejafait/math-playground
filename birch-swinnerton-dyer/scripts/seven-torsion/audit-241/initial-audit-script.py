#!/usr/bin/env python3
"""Fixed L067 audit: distinct determinant arithmetic and fresh negative tests.

Uses no producer or verifier arithmetic. All old files are read-only.
The separate complete verifier replay must have been run first.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
from math import lcm
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "audit-241"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def determinant(matrix):
    """Integer Bareiss elimination, retaining exact-division evidence."""
    a = [row[:] for row in matrix]
    sign, previous = 1, 1
    pivots = []
    for k in range(len(a) - 1):
        pivotrow = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivotrow is None:
            return 0, pivots
        if pivotrow != k:
            a[k], a[pivotrow] = a[pivotrow], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = pivot * a[i][j] - a[i][k] * a[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError("nonexact Bareiss division")
                a[i][j] = quotient
            a[i][k] = 0
        pivots.append({"column": k, "pivot_row": pivotrow,
                       "pivot": str(pivot), "divisor": str(previous)})
        previous = pivot
    return sign * a[-1][-1], pivots


def main():
    original = json.loads((DEST / "original-manifest.json").read_text())
    if any(digest(ROOT / name) != value for name, value in original.items()):
        raise RuntimeError("original evidence changed before audit")
    cert = json.loads((ROOT / "certificate.json").read_text())
    replay = json.loads((DEST / "complete-replay.json").read_text())
    if replay["status"] != "PASS" or replay["sha256"] != digest(ROOT / "certificate.json"):
        raise RuntimeError("complete original replay missing or mismatched")
    f, h = ([Q(x) for x in cert[key]] for key in ("f", "h"))
    if len(f) != 25 or f[-1] != 1 or len(h) != 49 or h[-1] != 1:
        raise RuntimeError("wrong degrees")
    if any(h[j] for j in range(1, 49, 2)):
        raise RuntimeError("h is not even")

    # Multiplication by c(X) on Q[X]/f, independently of the saved
    # 48-dimensional Y-power matrix and its inverse. Only degrees up
    # through 26 occur, so explicit descending substitution suffices.
    columns = []
    for j in range(24):
        p = [Q(0)] * 27
        p[j] = 46224
        p[j + 1] = -3024
        p[j + 3] = 1
        for degree in range(26, 23, -1):
            coefficient = p[degree]
            for i in range(25):
                p[degree - 24 + i] -= coefficient * f[i]
        if any(p[24:]):
            raise RuntimeError("incomplete cubic reduction")
        columns.append(p[:24])
    scale = lcm(*(x.denominator for column in columns for x in column))
    scaled = [[int(scale * columns[j][i]) for j in range(24)] for i in range(24)]
    rows = []
    for t in range(25):
        matrix = [[(scale * t * t if i == j else 0) - scaled[i][j]
                   for j in range(24)] for i in range(24)]
        det, pivots = determinant(matrix)
        value = sum((coefficient * t**j for j, coefficient in enumerate(h)), Q(0))
        difference = Q(det) - scale**24 * value
        rows.append({"t": t, "z": t*t, "scaled_determinant": str(det),
                     "h_value": str(value), "difference": str(difference),
                     "bareiss_pivots": pivots})
    if any(Q(row["difference"]) for row in rows):
        raise RuntimeError("determinant cross-check failed")
    # Both sides are degree <=24 polynomials in z=T^2. These 25
    # distinct exact evaluation equalities establish their identity.
    determinant_report = {
        "status": "PASS", "method": "integer Bareiss at 25 distinct squares",
        "matrix_dimension": 24, "scale": scale, "scaled_cubic_matrix": scaled,
        "actual_evaluations": len(rows), "required_evaluations": 25,
        "polynomial_degree_bound_in_z": 24, "h_even": True,
        "identity": "det(T^2 I - multiplication_by_c_on_Q[X]/f) = h(T)",
        "evaluations": rows, "failures": []}
    (DEST / "determinant-crosscheck.json").write_text(json.dumps(determinant_report, indent=2) + "\n")

    cases = []
    for name, expected in [
        ("corrupted-psi7", "psi7_odd_recurrence"),
        ("missing-X-map", "required_fields"),
        ("corrupted-h", "h_annihilation_all_coordinates"),
        ("corrupted-frobenius-24", "mod5_frobenius_24"),
        ("preserved-degree47-draft", "h_monic_degree48")]:
        changed = json.loads(json.dumps(cert))
        if name == "corrupted-psi7":
            changed["psi7"][0] = str(Q(changed["psi7"][0]) + 1)
        elif name == "missing-X-map":
            del changed["X_of_t"]
        elif name == "corrupted-h":
            changed["h"][0] = str(Q(changed["h"][0]) + 1)
        elif name == "corrupted-frobenius-24":
            row = changed["modular_tests"][-1]["frobenius"][24]
            row[0] = (row[0] + 1) % 5
        else:
            changed = json.loads((ROOT / "producer-draft-v0.json").read_text())
        source, report = DEST / (name + ".json"), DEST / (name + "-report.json")
        source.write_text(json.dumps(changed, separators=(",", ":")) + "\n")
        completed = subprocess.run(
            [sys.executable, str(ROOT / "verify_certificate.py"),
             "--certificate", str(source), "--report", str(report)],
            capture_output=True, text=True)
        (DEST / (name + ".log")).write_text(completed.stdout + completed.stderr)
        actual = json.loads(report.read_text())
        passed = (completed.returncode == 1 and actual["status"] == "REJECTED"
                  and actual["failure"] == expected)
        cases.append({"case": name, "pass": passed, "expected_failure": expected,
                      "actual_failure": actual.get("failure"),
                      "checks_passed_before_rejection": actual["checks_passed"],
                      "report": str(report.relative_to(ROOT))})

    after = {name: digest(ROOT / name) for name in original}
    failures = [case["case"] for case in cases if not case["pass"]]
    if original != after:
        failures.append("original_bytes_changed")
    output = {"status": "PASS" if not failures else "FAIL", "failures": failures,
              "complete_replay_checks": replay["checks_passed"],
              "determinant_evaluations_actual": 25, "determinant_evaluations_required": 25,
              "rejections_actual": sum(case["pass"] for case in cases),
              "rejections_required": len(cases), "cases": cases,
              "original_files": len(original), "original_bytes_preserved": original == after,
              "original_sha256_before": original, "original_sha256_after": after,
              "invalid_draft_degree": len(changed["h"]) - 1,
              "required_degree": 48}
    path = DEST / "audit-report.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: v for k, v in output.items()
                      if k not in {"cases", "original_sha256_before", "original_sha256_after"}}))
    print("Full certificates:", path.relative_to(ROOT.parent.parent),
          (DEST / "determinant-crosscheck.json").relative_to(ROOT.parent.parent))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
