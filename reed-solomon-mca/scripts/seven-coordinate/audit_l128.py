"""Bounded audit of L128's assembly; reuse the separately audited exclusions.

Rebuild the complete domain and every predicate without producer imports.
Replay only the assembly in isolation. No other shard or locus is computed.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
OUT = HERE / "l128-critical-audit.json"
SHARD = "new-pair-filter/third-058.json"


def run():
    evidence = {"checks": [], "failures": []}

    def check(name, condition):
        evidence["checks"].append({"name": name, "passes": bool(condition)})
        if not condition:
            raise ValueError(name)

    def digest(path):
        return sha256(path.read_bytes()).hexdigest()

    def read(name):
        return json.loads((HERE / name).read_bytes())

    try:
        saved = read("third58-assembly.json")
        original_hashes = dict(saved["input_sha256"])
        for name in ("assemble_third58.py", "third58-assembly.json"):
            original_hashes[name] = digest(HERE / name)
        evidence["input_sha256"] = original_hashes
        check("all 23 saved input hashes", len(saved["input_sha256"]) == 23
              and all(digest(HERE / n) == v for n, v in saved["input_sha256"].items()))
        check("entire saved comparison passed", len(saved["checks"]) == 893
              and all(c["passes"] is True for c in saved["checks"])
              and len({c["name"] for c in saved["checks"]}) == 893
              and saved["failures"] == [])

        # Exact input copies; subprocess writes only its temporary output.
        with tempfile.TemporaryDirectory(prefix="l128-audit-", dir=HERE) as tmp:
            root = Path(tmp)
            for name in original_hashes:
                destination = root / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE / name, destination)
            proc = subprocess.run(
                [sys.executable, "-B", str(root / "assemble_third58.py")],
                cwd=root, text=True, capture_output=True, check=False)
            evidence["isolated_run"] = {
                "returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
            check("isolated complete assembly succeeds", proc.returncode == 0)
            check("complete certificate reproduces byte for byte",
                  (root / "third58-assembly.json").read_bytes()
                  == (HERE / "third58-assembly.json").read_bytes())

        master, replay, audit = [read(n) for n in (
            "new-pair-filter.json", "new-pair-filter-replay.json", "l125-critical-audit.json")]
        shard = read(SHARD)
        common = {
            "new-pair-filter.json", "new-pair-filter-replay.json",
            "new_pair_filter.py", "verify_new_pair_filter.py",
            "zero_anchor_support_filter.py", "verify_fixed_three_row_extensions.py",
            "new-pair-filter.log", "new-pair-filter-replay.log", SHARD}
        scoped = {n: v for n, v in audit["audited_input_hashes"].items()
                  if "/" not in n or n == SHARD}
        check("explicit nine-file L125 scope", set(scoped) == common
              and all(original_hashes[n] == v for n, v in scoped.items()))
        check("L125 audit program and log bound",
              audit["audit_code_sha256"] == original_hashes["audit_l125_partition.py"]
              and audit["complete_replay_log_sha256"]
              == original_hashes["l125-critical-audit-replay.log"])
        check("audited L125 full replay retained",
              audit["original_artifacts_byte_unchanged"] is True
              and audit["full_saved_replay_identical"] is True
              and audit["summary"] == master["summary"] == replay["summary"]
              and audit["failures"] == master["failures"] == replay["failures"] == []
              and replay["source_sha256"] == original_hashes["new-pair-filter.json"])
        manifests = [[r for r in x["thirds"] if r["third_index"] == 58]
                     for x in (master, replay)]
        check("unique full shard manifest in master and replay",
              len(manifests[0]) == 1 and manifests[0] == manifests[1]
              and manifests[0][0]["certificate"] == SHARD
              and manifests[0][0]["sha256"] == original_hashes[SHARD])

        h = [x for x in range(1, 97) if x**16 % 97 == 1]
        s = [1, 8, 12, 18, 22, 27, 33]
        j = [x for x in h if x not in s]
        # Enumerate four-subsets first, unlike the producer's pair product.
        universe = sorted([[list(x for x in a if x in s), list(x for x in a if x in j)]
                           for a in combinations(h, 4) if sum(x in s for x in a) == 2])
        supports = [set(i + k) for i, k in universe]
        seed_indices = [0, 412, 58]
        seed = [[[1, 8], [47, 50]], [[12, 18], [64, 75]], [[1, 12], [70, 79]]]
        check("complete exact independent universe",
              len(h) == 16 and len(universe) == 756 and len({tuple(sorted(a)) for a in supports}) == 756
              and master["modulus"] == 97 and master["H"] == h
              and master["S"] == s and master["J"] == j and master["universe"] == universe)
        check("exact seed and full-universe third",
              [universe[n] for n in seed_indices] == seed == saved["seed"]
              and saved["seed_indices"] == seed_indices
              and saved["third_index"] == shard["third_index"] == 58
              and master["first_indices"] == [0, 412] and master["first_two"] == seed[:2]
              and master["third_indices"].count(58) == 1
              and master["third_screen"][58]
              == {"index": 58, "intersections": [1, 1], "distinct": True, "eligible": True})
        screen = []
        for n, a in enumerate(supports):
            sizes = [sum(x in supports[b] for x in a) for b in seed_indices]
            screen.append({"index": n, "intersections": sizes,
                           "distinct": n not in seed_indices,
                           "eligible": n not in seed_indices and max(sizes) <= 1})
        eligible = [r["index"] for r in screen if r["eligible"]]
        check("all 756 screens and all 282 ordered cases",
              screen == saved["full_fourth_screen"] == shard["fourth_screen"]
              and len(eligible) == 282 == manifests[0][0]["cases"]
              and eligible == saved["eligible_fourth_indices"]
              == [r["fourth_index"] for r in shard["cases"]] and shard["failures"] == [])

        pairs = list(combinations(s, 2))
        check("exterior coordinate order", master["column_pairs"] == [list(p) for p in pairs])
        coverage, predicate_records = [], []
        for offset, case in enumerate(shard["cases"]):
            n, rank, basis = case["fourth_index"], case["rank"], case["kernel_basis"]
            check(f"{n}: audited rank and complete basis shape",
                  0 <= rank <= 21 and len(basis) == 21-rank
                  and all(len(v) == 21 and all(type(x) is int and 0 <= x < 97 for x in v)
                          for v in basis) and case["minor_residue"] % 97 != 0)
            factors, omissions = [], []
            # Full antisymmetric matrices give an independent predicate path.
            matrices = []
            for vector in basis:
                matrix = [[0]*7 for _ in s]
                for value, (a, b) in zip(vector, pairs):
                    ai, bi = s.index(a), s.index(b)
                    matrix[ai][bi], matrix[bi][ai] = value, -value % 97
                matrices.append(matrix)
            if rank < 21:
                for row, (overlap, _) in enumerate(seed + [universe[n]]):
                    for coordinate in overlap:
                        ci = s.index(coordinate)
                        passes = all(m[a][b] == 0 for m in matrices
                                     for a in range(7) for b in range(7) if a != ci and b != ci)
                        witnesses = [[bi, col, vector[col]]
                                     for bi, vector in enumerate(basis) for col, pair in enumerate(pairs)
                                     if coordinate not in pair and vector[col] != 0]
                        factors.append({"row": row, "coordinate": coordinate, "passes": passes,
                                        "failure_witness": witnesses[0] if witnesses else None})
                for coordinate in s:
                    passes = all(value == 0 for m in matrices for value in m[s.index(coordinate)])
                    witnesses = [[bi, col, vector[col]]
                                 for bi, vector in enumerate(basis) for col, pair in enumerate(pairs)
                                 if coordinate in pair and vector[col] != 0]
                    omissions.append({"coordinate": coordinate, "passes": passes,
                                      "failure_witness": witnesses[0] if witnesses else None})
            status = ("rank" if rank == 21 else "factor" if any(x["passes"] for x in factors)
                      else "omission" if any(x["passes"] for x in omissions) else "residual")
            check(f"{n}: every predicate, failure witness and status",
                  factors == case["factor_tests"] and omissions == case["omission_tests"]
                  and status == case["status"])
            coverage.append({"fourth_index": n, "support": universe[n], "status": status,
                             "source_pointer": f"/cases/{offset}"})
            predicate_records.append({"fourth_index": n, "factor_tests": factors,
                                      "omission_tests": omissions})
        expected_statuses = {"rank": 96, "factor": 175, "omission": 9, "residual": 2}
        check("complete coverage and fixed required partition",
              coverage == saved["coverage"]
              and dict(Counter(x["status"] for x in coverage)) == expected_statuses
              == saved["statuses"] == manifests[0][0]["statuses"])
        check("both residuals and all 154 historical records retained",
              [x["fourth_index"] for x in coverage if x["status"] == "residual"]
              == shard["residual_indices"] == [355, 647]
              and len(master["residual_occurrences"]) == 154
              and [x for x in master["residual_occurrences"] if x[0] == 58] == [[58, 355], [58, 647]])

        bindings = []
        for n, word, audit_name, pointer, count in (
            (355, "first", "l126-critical-audit.json", "/first_residual", 29),
            (647, "second", "l127-critical-audit.json", "/cases/182", 30)):
            exact_audit = read(audit_name)
            flags = exact_audit["checks"]
            flags = list(flags.values()) if isinstance(flags, dict) else [x["passes"] for x in flags]
            runs = exact_audit.get("runs", exact_audit.get("isolated_runs"))
            check(f"{n}: entire prior audit manifest and verdict",
                  len(flags) == count and all(x is True for x in flags)
                  and exact_audit["failures"] == [] and len(runs) == 2
                  and all(x["returncode"] == 0 for x in runs)
                  and all(original_hashes[name] == value
                          for name, value in exact_audit["input_sha256"].items()))
            cert_name = f"new-pair-{word}-residual-gates.json"
            cert, exact_replay = read(cert_name), read(f"new-pair-{word}-residual-gates-replay.json")
            case = next(x for x in shard["cases"] if x["fourth_index"] == n)
            source = cert["source"]
            expected_path = "l125-critical-audit.json" if n == 355 else SHARD
            rows = seed + [universe[n]]
            check(f"{n}: exact rows, full basis and literal source pointers",
                  case["rank"] == 19 and cert["kernel_basis"] == case["kernel_basis"]
                  and cert["rows"] == [{"I": i, "K": k} for i, k in rows]
                  and cert["H"] == h and cert["S"] == s and cert["J"] == j
                  and source == {"path": expected_path, "sha256": original_hashes[expected_path],
                                 "pointer": pointer, "full_universe_indices": [58, n],
                                 "shard_path": SHARD, "shard_sha256": original_hashes[SHARD]})
            if n == 355:
                check("first residual audit record equals actual shard record",
                      audit["first_residual"] == {
                          "third_index": 58, "fourth_index": n, "supports": rows,
                          "rank": 19, "kernel_basis": case["kernel_basis"]})
            else:
                check("second residual exact case pointer", shard["cases"][182] == case)
            check(f"{n}: imported exhaustive exclusion and complete replay binding",
                  cert["summary"]["complete_projective_points"] == 2
                  and cert["summary"]["intrinsically_passing_points"] == 0
                  and cert["summary"]["unresolved_branches"] == 0
                  and exact_replay["certificate_sha256"] == original_hashes[cert_name]
                  and cert["failures"] == exact_replay["failures"] == [])
            bindings.append({"fourth_index": n, "support": universe[n], "audit": audit_name,
                             "source": source, "complete_points": 2, "passing_points": 0})
        check("every complete residual binding", bindings == saved["residual_bindings"])
        summary = {"actual_screen": 756, "required_screen": 756, "actual_eligible": 282,
                   "required_eligible": 282, "covered": 282, "uncovered": 0,
                   "residuals_bound": 2, "residuals_required": 2}
        check("entire assembly summary", saved["summary"] == summary)
        check("all 25 original artifacts unchanged",
              all(digest(HERE / name) == value for name, value in original_hashes.items()))
        evidence.update(summary=summary, statuses=expected_statuses,
                        full_fourth_screen=screen, eligible_fourth_indices=eligible,
                        coverage=coverage, complete_predicates=predicate_records,
                        residual_bindings=bindings, original_artifacts_byte_unchanged=True,
                        qualification="Assembly audit only; imported audits are not rerun. "
                        "No new matrix/locus calculation, census or global bound.")
    except Exception as error:
        evidence["failures"].append(f"{type(error).__name__}: {error}")
    OUT.write_text(json.dumps(evidence, indent=2) + "\n")
    print("Summary:", json.dumps(evidence.get("summary", {}), sort_keys=True))
    print(f"Audit checks passed/required: {sum(c['passes'] for c in evidence['checks'])}/"
          f"{len(evidence['checks'])}; failures: {len(evidence['failures'])}; certificate: {OUT}")
    if evidence["failures"]:
        print("Failures:", evidence["failures"])
        raise SystemExit(1)


if __name__ == "__main__":
    run()
