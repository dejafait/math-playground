"""Fresh, isolated L129 producer/replay audit; never rewrites source evidence."""
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
INPUTS = [
    "third59_first_residual_gates.py",
    "verify_third59_first_residual_gates.py",
    "zero_anchor_support_filter.py",
    "residual_kernel_gates.py",
    "new-pair-first-residual-gates.json",
    "l126-critical-audit.json",
    "new-pair-filter/third-059.json",
]
OUTPUTS = [
    "third59-first-residual-gates.json",
    "third59-first-residual-gates-replay.json",
]


def run():
    paths = INPUTS + OUTPUTS
    before = {name: (HERE / name).read_bytes() for name in paths}
    report = {
        "step_id": "2026-10-20-mca-374-third59-first-residual-critical-audit",
        "target": [59, 355],
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

    with TemporaryDirectory(prefix="l129-audit-") as directory:
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
          == -183559014313634527018950183616512)
    check("nonzero_minor_residue",
          cert["rank_minor_integer_determinant"] % 97 == cert["rank_minor_residue"] == 54)
    check("all_homogeneous_coefficients",
          cert["plucker_coefficients_s2_st_t2"]
          == [[0, x, 0] for x in [2, 44, 54, 1]] + [[0, 0, 0]] * 31)
    check("affine_and_infinity_complete",
          cert["affine_gcd"] == [0, 1]
          and cert["complete_projective_parameter_locus"] == [[1, 0], [0, 1]])
    expected = [
        (0, [85, 0], [85, 0, 0, 0]),
        (30, [19, 12], [9, 94, 10, 9]),
        (0, [18, 0], [18, 0, 0, 0]),
        (29, [61, 90], [88, 28, 9, 53]),
        (0, [81, 0], [0, 81, 0, 0]),
        (0, [0, 75], [75, 0, 0, 0]),
        (0, [0, 84], [0, 84, 0, 0]),
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
    source = json.loads(before["new-pair-first-residual-gates.json"])
    old_audit = json.loads(before["l126-critical-audit.json"])
    check("import_bound_to_separate_L126_audit",
          old_audit["failures"] == [] and all(old_audit["checks"].values())
          and old_audit["input_sha256"]["new-pair-first-residual-gates.json"]
          == sha256(before["new-pair-first-residual-gates.json"]).hexdigest()
          == cert["source"]["sha256"])
    check("same_audited_helper_bytes", all(
        old_audit["input_sha256"][name] == sha256(before[name]).hexdigest()
        for name in ("zero_anchor_support_filter.py", "residual_kernel_gates.py")))
    check("literal_complete_kernel_and_order_import",
          cert["kernel_basis"] == source["kernel_basis"]
          and cert["column_pairs"] == source["column_pairs"])
    check("unchanged_original_rows_and_gate_inputs", all(
        cert["rows"][j] == source["rows"][j]
        and cert["blocks"][j] == source["blocks"][j]
        and all(p["row_gates"][j] == old["row_gates"][j]
                for p, old in zip(cert["points_and_all_row_gates"],
                                  source["points_and_all_row_gates"]))
        for j in (0, 1, 3)))
    check("changed_third_support", cert["rows"][2] == {
        "I": [1, 12], "K": [70, 85]})
    expected_g = dict(zip(map(str, [1, 8, 12, 18, 22, 27, 33, 70, 85]),
                         [54, 87, 2, 13, 69, 60, 79, 69, 68]))
    check("changed_third_evaluations", all(
        p["row_gates"][2]["g_values_on_S_union_K"] == expected_g
        for p in cert["points_and_all_row_gates"]))
    check("changed_third_projections", [
        (p["row_gates"][2]["Q_u"], p["row_gates"][2]["Q_v"])
        for p in cert["points_and_all_row_gates"]] == [
            ([0, 0, 0, 0], [79, 78, 96, 32]),
            ([84, 28, 37, 18], [0, 0, 0, 0])])
    shard_bytes = before["new-pair-filter/third-059.json"]
    shard = json.loads(shard_bytes)
    check("exact_shard_hash", sha256(shard_bytes).hexdigest()
          == cert["source"]["shard_sha256"]
          == "df53d2429ea83f9c85777da586b1b89be4005f11ad6f8d36ca4edae7025415cb")
    check("unique_shard_position_75", [n for n, c in enumerate(shard["cases"])
          if c["fourth_index"] == 355] == [75]
          and shard["cases"][75]["kernel_basis"] == cert["kernel_basis"])
    check("historical_residual_indices_preserved", shard["residual_indices"] == [355, 647])
    report["replay_summary"] = expected_summary
    report["actual_required"] = {
        "audited_occurrences": [1, 1], "complete_projective_points": [2, 2],
        "excluded_points": [2, 2], "original_files_unchanged": [
            sum(checks[name + "_original_unchanged"] for name in paths), len(paths)],
    }
    report["limitations"] = (
        "One indexed exclusion; semantic proof/program audit is recorded in L129. "
        "Fresh replay retains shared Python and residue arithmetic, inherited finite "
        "certificates and arbitrary prescribed charts. No enlarged census."
    )
    path = HERE / "l129-critical-audit.json"
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Checks {sum(checks.values())}/{len(checks)}; "
          f"audited occurrences 1/1; excluded points 2/2; "
          f"rank 19, minor 54!=0; failures {len(report['failures'])}.")
    print(f"Full audit certificate: {path}")
    return not report["failures"]


if __name__ == "__main__":
    sys.exit(0 if run() else 1)
