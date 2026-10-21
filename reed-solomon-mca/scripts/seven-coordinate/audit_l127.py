"""Isolated, bounded reproduction for L127's separate critical audit.

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
    "new_pair_second_residual_gates.py",
    "verify_new_pair_second_residual_gates.py",
    "zero_anchor_support_filter.py",
    "residual_kernel_gates.py",
]
CERT = "new-pair-second-residual-gates.json"
REPLAY = "new-pair-second-residual-gates-replay.json"
SHARD = "new-pair-filter/third-058.json"


def run():
    names = PROGRAMS + [SHARD, CERT, REPLAY]
    originals = {name: (HERE / name).read_bytes() for name in names}
    before = {name: sha256(raw).hexdigest() for name, raw in originals.items()}
    checks, failures, runs = [], [], []

    def check(name, condition):
        checks.append({"name": name, "passes": bool(condition)})
        if not condition:
            failures.append(name)

    with tempfile.TemporaryDirectory(prefix="l127-audit-", dir=HERE) as folder:
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
    check("unmodified seven computation inputs",
          all((HERE / n).read_bytes() == raw for n, raw in originals.items()))
    check("saved replay bound to complete producer certificate",
          r["certificate_sha256"] == before[CERT])
    check("frozen shard binding",
          before[SHARD] == "5c22d06699cb5a500ffa8ccbbb5161c5652c7a0364ec4cb5aa412825ef87e3f9")
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
          == -79930926190995594340952590526545920
          and c["rank_minor_residue"] == 9)
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
        ([45, 0], 0, [45, 0, 0, 0]),
        ([0, 54], 0, [54, 0, 0, 0]),
        ([51, 51], 24, [58, 32, 57, 90]),
        ([0, 44], 0, [78, 0, 0, 0]),
        ([0, 29], 0, [0, 47, 0, 0]),
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
        "scope": "L127 only: full-universe occurrence (58,647); no new census or assembly",
        "input_sha256": before,
        "isolated_runs": runs,
        "checks": checks,
        "summary": {"checks_passed": sum(x["passes"] for x in checks),
                    "checks_required": len(checks), "reproduced_certificates": 2,
                    "unchanged_original_computation_files": 7,
                    "passing_planes": 0, "complete_planes": 2,
                    "failures": len(failures)},
        "failures": failures,
        "limitations": "Exact Python/residue arithmetic shared; inherited finite certificates reused. "
                      "Analytic extension and arbitrary-chart audit is recorded in canonical L127.",
    }
    target = HERE / "l127-critical-audit.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"], sort_keys=True))
    print(f"Actual/required checked loci 1/1; passing planes 0/2; failures {len(failures)}; {target}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
