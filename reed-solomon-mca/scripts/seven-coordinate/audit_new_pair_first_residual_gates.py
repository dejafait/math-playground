"""Fresh, isolated L126 producer/replay audit; never rewrites source evidence."""
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
INPUTS = [
    "new_pair_first_residual_gates.py",
    "verify_new_pair_first_residual_gates.py",
    "zero_anchor_support_filter.py",
    "residual_kernel_gates.py",
    "l125-critical-audit.json",
    "new-pair-filter/third-058.json",
]
OUTPUTS = [
    "new-pair-first-residual-gates.json",
    "new-pair-first-residual-gates-replay.json",
]


def run():
    paths = INPUTS + OUTPUTS
    before = {name: (HERE / name).read_bytes() for name in paths}
    report = {
        "step_id": "2026-10-20-mca-362-new-pair-first-residual-critical-audit",
        "target": [58, 355],
        "input_sha256": {
            name: sha256(raw).hexdigest() for name, raw in before.items()
        },
        "runs": [],
        "checks": {},
        "failures": [],
    }
    checks = report["checks"]

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            report["failures"].append(name)

    with TemporaryDirectory(prefix="l126-audit-") as directory:
        work = Path(directory)
        for name in INPUTS:
            target = work / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(HERE / name, target)
        for program in INPUTS[:2]:
            completed = subprocess.run(
                [sys.executable, "-B", str(work / program)],
                cwd=work, capture_output=True, text=True, check=False,
            )
            report["runs"].append({
                "program": program, "returncode": completed.returncode,
                "stdout": completed.stdout.replace(str(work), "<isolated-copy>"),
                "stderr": completed.stderr.replace(str(work), "<isolated-copy>"),
            })
            check(program + "_exit", completed.returncode == 0)
            if completed.returncode:
                break
        for name in OUTPUTS:
            check(name + "_byte_identical",
                  (work / name).exists() and (work / name).read_bytes() == before[name])

    for name in paths:
        check(name + "_original_unchanged", (HERE / name).read_bytes() == before[name])

    cert, replay = [json.loads(before[name]) for name in OUTPUTS]
    # Every value in these original outputs was independently regenerated and
    # compared above. These checks also bind the canonical proof's exact claims.
    expected_summary = {
        "matrix_entries_compared": 504, "rank": 19,
        "complete_kernel_vectors": 2, "plucker_equations": 35,
        "complete_points": 2, "row_gates_replayed": 8,
        "nonzero_exterior_pivots": 7, "all_projection_pivot_checks": 106,
        "lambda_zero_rows": 6, "full_weight_rows": 2,
        "moment_residuals": 64, "pointwise_entries": 128,
    }
    check("complete_replay_summary", replay["summary"] == expected_summary)
    check("replay_bound_to_certificate",
          replay["certificate_sha256"] == sha256(before[OUTPUTS[0]]).hexdigest())
    check("original_minor_rows",
          cert["rank_minor_rows"] == list(range(16)) + [18, 19, 20])
    check("original_minor_columns",
          cert["rank_minor_columns"] == list(range(5)) + list(range(7, 21)))
    check("signed_integer_minor",
          cert["rank_minor_integer_determinant"]
          == replay["rank_minor_integer_determinant"]
          == -16304398318117198723155451969536000)
    check("nonzero_minor_residue",
          cert["rank_minor_integer_determinant"] % 97 == cert["rank_minor_residue"] == 8)
    check("all_homogeneous_coefficients",
          cert["plucker_coefficients_s2_st_t2"]
          == [[0, x, 0] for x in [2, 44, 54, 1]] + [[0, 0, 0]] * 31)
    check("affine_and_infinity_complete",
          cert["affine_gcd"] == [0, 1]
          and cert["complete_projective_parameter_locus"] == [[1, 0], [0, 1]])
    expected = [
        (0, [85, 0], [85, 0, 0, 0]),
        (30, [19, 12], [9, 94, 10, 9]),
        (0, [56, 0], [56, 0, 0, 0]),
        (29, [61, 90], [88, 28, 9, 53]),
        (0, [81, 0], [0, 81, 0, 0]),
        (0, [0, 75], [75, 0, 0, 0]),
        (0, [0, 70], [0, 70, 0, 0]),
        (0, [28, 0], [28, 0, 0, 0]),
    ]
    rows = [row for point in cert["points_and_all_row_gates"]
            for row in point["row_gates"]]
    check("complete_proof_weight_table",
          [(r["lambda_value"], r["direction_coefficients"], r["error_weights"])
           for r in rows] == expected)
    check("all_eight_rank_one_projections", len(rows) == 8
          and all(r["projection_rank"] == 1 for r in rows))
    check("all_pointwise_identities", all(
        r["h_minus_error_minus_lambda_g_on_H"] == [0] * 16 for r in rows))
    check("all_shifted_moments", all(r["moment_residuals"] == [0] * 8 for r in rows))
    check("prescribed_chart_coefficients", all(
        r["prescribed_finite_gate"] == {
            "D_coefficient": r["direction_coefficients"][0],
            "C_coefficient": -r["direction_coefficients"][1] % 97}
        and r["original_first_coefficient"] == "(D*alpha-C*beta)/(AD-BC)"
        for r in rows))
    check("both_first_rows_fail", all(
        point["row_gates"][0]["lambda_value"] == 0
        and not point["passes_intrinsic_gates"]
        for point in cert["points_and_all_row_gates"]))
    check("all_pivot_records_retained", len(replay["all_pivot_replay"]) == 106)
    check("no_unresolved_branch", cert["summary"]["unresolved_branches"] == 0)
    check("no_recorded_failures", cert["failures"] == replay["failures"] == [])
    report["replay_summary"] = expected_summary
    report["actual_required"] = {
        "audited_occurrences": [1, 1], "complete_projective_points": [2, 2],
        "excluded_points": [2, 2], "original_files_unchanged": [
            sum(checks[name + "_original_unchanged"] for name in paths), len(paths)],
    }
    report["limitations"] = (
        "One indexed exclusion; semantic proof/program audit is recorded in L126. "
        "Fresh replay retains shared Python and residue arithmetic, inherited finite "
        "certificates and arbitrary prescribed charts. No enlarged census."
    )
    path = HERE / "l126-critical-audit.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Checks {sum(checks.values())}/{len(checks)}; "
          f"audited occurrences 1/1; excluded points 2/2; "
          f"rank 19, minor 8!=0; failures {len(report['failures'])}.")
    print(f"Full audit certificate: {path}")
    return not report["failures"]


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
