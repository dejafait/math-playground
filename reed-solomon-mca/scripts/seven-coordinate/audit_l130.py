"""Isolated, bounded reproduction for L130's separate critical audit.

Does not enumerate additional supports or overwrite any input artifact.
The reviewed verifier regenerates every row and pivot record; comparing its
entire output checks the original saved replay, not merely its summary.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
PROGRAMS = [
    "third59_second_residual_gates.py",
    "verify_third59_second_residual_gates.py",
    "zero_anchor_support_filter.py",
    "residual_kernel_gates.py",
]
CERT = "third59-second-residual-gates.json"
REPLAY = "third59-second-residual-gates-replay.json"
SHARD = "new-pair-filter/third-059.json"


def run():
    source_name = "new-pair-second-residual-gates.json"
    prior_audit_name = "l127-critical-audit.json"
    names = PROGRAMS + [SHARD, CERT, REPLAY, source_name, prior_audit_name]
    originals = {name: (HERE / name).read_bytes() for name in names}
    before = {name: sha256(raw).hexdigest() for name, raw in originals.items()}
    checks, failures, runs = [], [], []

    def check(name, condition):
        checks.append({"name": name, "passes": bool(condition)})
        if not condition:
            failures.append(name)

    with tempfile.TemporaryDirectory(prefix="l130-audit-", dir=HERE) as folder:
        isolated = Path(folder)
        for name in names:
            target = isolated / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(HERE / name, target)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        env.pop("PYTHONOPTIMIZE", None)
        for program in PROGRAMS[:2]:
            proc = subprocess.run(
                [sys.executable, "-B", program], cwd=isolated, env=env,
                capture_output=True, text=True, timeout=60,
            )
            runs.append({"program": program, "returncode": proc.returncode,
                         "stdout": proc.stdout, "stderr": proc.stderr})
            check(program + " fresh run", proc.returncode == 0)
        for name in [CERT, REPLAY]:
            check(name + " byte-for-byte reproduction",
                  (isolated / name).read_bytes() == originals[name])

    c, r, shard = [json.loads(originals[name]) for name in [CERT, REPLAY, SHARD]]
    source = json.loads(originals[source_name])
    prior = json.loads(originals[prior_audit_name])
    check("L127 imported certificate bound to prior audit hash",
          before[source_name] == prior["input_sha256"][source_name])
    check("both called helper files bound to prior audit hashes",
          all(before[n] == prior["input_sha256"][n] for n in PROGRAMS[2:]))
    check("prior L127 audit reports full successful scoped checks",
          prior["failures"] == [] and prior["summary"]["checks_passed"]
          == prior["summary"]["checks_required"] == 30
          and all(q["passes"] for q in prior["checks"]))
    check("source identities and correct occurrence binding",
          source["source"]["full_universe_indices"] == [58, 647]
          and c["source"]["full_universe_indices"] == [59, 647]
          and c["source"]["sha256"] == before[source_name]
          and c["source"]["shard_sha256"] == before[SHARD]
          and shard["third_index"] == 59 and shard["residual_indices"] == [355, 647])
    check("complete ordered basis and columns match L127",
          c["kernel_basis"] == source["kernel_basis"]
          and c["column_pairs"] == source["column_pairs"])
    check("complete homogeneous and affine import identity",
          all(c[key] == source[key] for key in ["plucker_quadruples",
              "plucker_coefficients_s2_st_t2", "affine_gcd", "affine_quotients",
              "bezout_coefficients", "complete_projective_parameter_locus"]))
    check("unchanged rows bind original labels and entire blocks",
          all(c["rows"][j] == source["rows"][j]
              and c["blocks"][j] == source["blocks"][j] for j in (0, 1, 3)))
    check("unchanged rows bind all plane and gate fields",
          all(all(point[key] == old[key] for key in ["u", "v", "bivector", "pivot_indices"])
              and all(point["row_gates"][j] == old["row_gates"][j] for j in (0, 1, 3))
              for point, old in zip(c["points_and_all_row_gates"], source["points_and_all_row_gates"])))
    check("third row is changed and independently reconstructed",
          c["rows"][2] == {"I": [1, 12], "K": [70, 85]}
          and source["rows"][2] == {"I": [1, 12], "K": [70, 79]}
          and c["blocks"][2] != source["blocks"][2]
          and r["rebuilt_original_matrix"][12:18] == c["blocks"][2]["matrix"])
    changed = [point["row_gates"][2] for point in c["points_and_all_row_gates"]]
    check("all changed-row g evaluations and projections",
          all(g["g_values_on_S_union_K"] == dict(zip(
              map(str, [1,8,12,18,22,27,33,70,85]), [54,87,2,13,69,60,79,69,68]))
              for g in changed)
          and [(g["Q_u"], g["Q_v"]) for g in changed]
          == [([0,0,0,0], [87,0,0,0]), ([47,63,61,95], [0,0,0,0])])
    check("unmodified nine audit inputs",
          all((HERE / n).read_bytes() == raw for n, raw in originals.items()))
    check("saved replay bound to complete producer certificate",
          r["certificate_sha256"] == before[CERT])
    check("frozen shard binding",
          before[SHARD] == "df53d2429ea83f9c85777da586b1b89be4005f11ad6f8d36ca4edae7025415cb")
    selected = shard["cases"][182]
    check("unique exact residual index",
          selected["fourth_index"] == 647 and selected["status"] == "residual"
          and sum(v["fourth_index"] == 647 for v in shard["cases"]) == 1)
    check("matrix shape and complete original replay",
          len(c["original_matrix"]) == 24
          and all(len(row) == 21 for row in c["original_matrix"])
          and r["rebuilt_original_matrix"] == c["original_matrix"])
    check("original rank minor", c["rank_minor_integer_determinant"]
          == r["rank_minor_integer_determinant"]
          == 3594962637037369699889979396022272
          and c["rank_minor_residue"] == 85)
    check("complete kernel replay",
          r["kernel_residuals"] == c["kernel_residuals"]
          == [[0] * 24 for _ in range(2)])
    quads = c["plucker_quadruples"]
    polys = c["plucker_coefficients_s2_st_t2"]
    expected_mixed = {
        (1, 8, 12, 18): 84, (1, 12, 18, 22): 34,
        (1, 12, 18, 27): 35, (1, 12, 18, 33): 96,
    }
    check("all 35 homogeneous coefficients, including infinity",
          quads == list(map(list, combinations(c["S"], 4)))
          and polys == r["plucker_coefficients_s2_st_t2"]
          and polys == [[0, expected_mixed.get(tuple(q), 0), 0] for q in quads])
    check("complete homogeneous endpoint locus",
          c["complete_projective_parameter_locus"] == [[1, 0], [0, 1]])
    check("affine gcd", c["affine_gcd"] == [0, 1])
    check("all affine divisions",
          c["affine_quotients"] == [[p[1]] if p[1] else [] for p in polys])
    check("full Bezout identity",
          c["bezout_coefficients"] == [[] for _ in range(12)]
          + [[96]] + [[] for _ in range(22)]
          and 96 * polys[12][1] % 97 == 1)

    expected_rows = [
        ([53, 0], 0, [53, 0, 0, 0]),
        ([0, 12], 0, [0, 12, 0, 0]),
        ([10, 0], 0, [10, 0, 0, 0]),
        ([0, 54], 0, [54, 0, 0, 0]),
        ([51, 51], 24, [58, 32, 57, 90]),
        ([0, 44], 0, [78, 0, 0, 0]),
        ([0, 47], 0, [0, 26, 0, 0]),
        ([13, 51], 82, [35, 48, 75, 23]),
    ]
    all_rows = [row for point in c["points_and_all_row_gates"] for row in point["row_gates"]]
    check("all eight full original-row records retained", len(all_rows) == 8)
    for n, (g, expected) in enumerate(zip(all_rows, expected_rows)):
        direction, lam, weights = expected
        check(f"row {n} full gates and prescribed-chart coefficients",
              g["projection_rank"] == 1 and not any(g["projection_minors"])
              and (g["direction_coefficients"], g["lambda_value"], g["error_weights"])
              == (direction, lam, weights)
              and g["passes"] == all(weights)
              and g["prescribed_finite_gate"]
              == {"D_coefficient": direction[0], "C_coefficient": -direction[1] % 97}
              and g["moment_residuals"] == [0] * 8
              and g["h_minus_error_minus_lambda_g_on_H"] == [0] * 16)
    check("complete replay row ordering",
          [(v["point_index"], v["row_number"]) for v in r["all_row_replay"]]
          == [(p, row) for p in range(2) for row in range(1, 5)])
    pivot_keys = [(v["point"], tuple(v["exterior_pivot"]), v["row"],
                   v["projection_component"]) for v in r["all_pivot_replay"]]
    check("all pivot records distinct and fully regenerated",
          len(pivot_keys) == len(set(pivot_keys)) == 88)
    check("seven distinct exterior pivots",
          len({(k[0], k[1]) for k in pivot_keys}) == 7)
    check("exact reported replay counts", r["summary"] == {
        "matrix_entries_compared": 504, "rank": 19, "complete_kernel_vectors": 2,
        "plucker_equations": 35, "complete_points": 2, "row_gates_replayed": 8,
        "nonzero_exterior_pivots": 7, "all_projection_pivot_checks": 88,
        "lambda_zero_rows": 6, "full_weight_rows": 2, "moment_residuals": 64,
        "pointwise_entries": 128,
    })
    check("no reported failure or unresolved component",
          c["failures"] == r["failures"] == []
          and c["summary"]["unresolved_branches"] == 0
          and c["summary"]["intrinsically_passing_points"] == 0)
    result = {
        "scope": "L130 only: full-universe occurrence (59,647); no new census or assembly",
        "input_sha256": before,
        "isolated_runs": runs,
        "checks": checks,
        "summary": {"checks_passed": sum(x["passes"] for x in checks),
                    "checks_required": len(checks), "reproduced_certificates": 2,
                    "unchanged_original_computation_files": len(names),
                    "passing_planes": 0, "complete_planes": 2,
                    "failures": len(failures)},
        "failures": failures,
        "limitations": "Exact Python/residue arithmetic shared; inherited finite certificates reused. "
                      "Analytic extension and arbitrary-chart audit is recorded in canonical L130.",
    }
    target = HERE / "l130-critical-audit.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))
    print(f"Actual/required checked loci 1/1; passing planes 0/2; failures {len(failures)}; {target}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
