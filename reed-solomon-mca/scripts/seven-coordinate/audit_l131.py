"""Separate bounded audit of L131's binding, not a new filter/locus search."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
OUT = HERE / "l131-critical-audit.json"


def run():
    report = dict(
        step_id="2026-10-20-mca-382-third59-assembly-critical-audit",
        scope="L131 only: third 59; reuse audited L125/L129/L130 exclusions",
        checks=[], failures=[], input_sha256={}, runs=[],
        complete_case_checks=[], complete_screen_checks=[],
    )

    def check(name, condition):
        report["checks"].append(dict(name=name, passes=bool(condition)))
        if not condition:
            raise ValueError(name)

    def read(name):
        return json.loads((HERE / name).read_bytes())

    def digest(name):
        return sha256((HERE / name).read_bytes()).hexdigest()

    try:
        saved = read("third59-assembly.json")
        names = sorted(set(saved["input_sha256"]) |
                       {"assemble_third59.py", "third59-assembly.json"})
        check("closed original input inventory", len(names) == 29)
        for name in names:
            check("local input path " + name,
                  (HERE / name).resolve().is_relative_to(HERE))
            report["input_sha256"][name] = digest(name)
        check("all 27 recorded input digests",
              all(digest(n) == h for n, h in saved["input_sha256"].items()))
        check("898 nonvacuous successful original checks",
              len(saved["checks"]) == 898 and saved["failures"] == [] and
              all(c["passes"] is True for c in saved["checks"]))
        with TemporaryDirectory(prefix="l131-audit-", dir=HERE) as temp:
            isolated = Path(temp)
            for name in names:
                if name == "third59-assembly.json":
                    continue
                dest = isolated / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(HERE / name, dest)
            completed = subprocess.run(
                [sys.executable, "-B", str(isolated / "assemble_third59.py")],
                capture_output=True, text=True, check=False)
            report["runs"].append(dict(
                program="assemble_third59.py", returncode=completed.returncode,
                stdout=completed.stdout.replace(temp, "<isolated-copy>"),
                stderr=completed.stderr.replace(temp, "<isolated-copy>")))
            check("fresh isolated comparison succeeds", completed.returncode == 0)
            reproduced = (isolated / "third59-assembly.json").read_bytes()
            check("complete certificate byte reproduction",
                  reproduced == (HERE / "third59-assembly.json").read_bytes())

        # Independent domain path: four-subsets, then split/order by S and J.
        # No imported local function or historical universe helper is used.
        h = [a for a in range(1, 97) if a**16 % 97 == 1]
        s = {1, 8, 12, 18, 22, 27, 33}
        rows = []
        for a in range(16):
            for b in range(a + 1, 16):
                for c in range(b + 1, 16):
                    for d in range(c + 1, 16):
                        support = {h[a], h[b], h[c], h[d]}
                        if len(support & s) == 2:
                            rows.append([sorted(support & s), sorted(support - s)])
        rows.sort()
        masks = [sum(1 << h.index(x) for x in i + k) for i, k in rows]
        seed = [0, 412, 59]
        check("independent full universe and seed",
              len(rows) == len(set(masks)) == 756 and
              [rows[i] for i in seed] == saved["seed"] and saved["seed_indices"] == seed)
        eligible = []
        for i, mask in enumerate(masks):
            counts = [(mask & masks[j]).bit_count() for j in seed]
            distinct = i not in seed
            passes = distinct and max(counts) <= 1
            expected = dict(index=i, intersections=counts, distinct=distinct, eligible=passes)
            check(f"independent screen {i}", saved["full_fourth_screen"][i] == expected)
            report["complete_screen_checks"].append(expected)
            if passes:
                eligible.append(i)
        check("complete screen length and ordered eligible indices",
              len(saved["full_fourth_screen"]) == 756 and len(eligible) == 282 and
              saved["eligible_fourth_indices"] == eligible)
        shard = read("new-pair-filter/third-059.json")
        master = read("new-pair-filter.json")
        check("complete coverage and shard lengths",
              len(saved["coverage"]) == len(shard["cases"]) == 282 and
              [c["fourth_index"] for c in shard["cases"]] == eligible)
        columns = [tuple(p) for p in master["column_pairs"]]
        status_counts = Counter()
        for offset, index in enumerate(eligible):
            case = shard["cases"][offset]
            basis = case["kernel_basis"]
            check(f"{index}: canonical residue entries",
                  all(type(x) is int and 0 <= x < 97 for v in basis for x in v))
            factor_passes, omission_passes = [], []
            for test in case["factor_tests"] + case["omission_tests"]:
                c = test["coordinate"]
                is_factor = "row" in test
                allowed = (lambda p: c in p) if is_factor else (lambda p: c not in p)
                violations = [[b, k, v[k]] for b, v in enumerate(basis)
                              for k, p in enumerate(columns) if not allowed(p) and v[k] != 0]
                passed = not violations
                check(f"{index}: full predicate {is_factor}/{test.get('row')}/{c}",
                      test["passes"] == passed and
                      test["failure_witness"] == (violations[0] if violations else None))
                (factor_passes if is_factor else omission_passes).append(passed)
            status = ("rank" if case["rank"] == 21 else
                      "factor" if any(factor_passes) else
                      "omission" if any(omission_passes) else "residual")
            entry = dict(fourth_index=index, support=rows[index], status=status,
                         source_pointer=f"/cases/{offset}")
            check(f"{index}: full coverage entry", saved["coverage"][offset] == entry)
            check(f"{index}: audited shard disposition", case["status"] == status)
            report["complete_case_checks"].append(entry)
            status_counts[status] += 1
        check("required partition", dict(status_counts) ==
              saved["statuses"] == dict(rank=96, factor=175, omission=9, residual=2))
        for binding, index, pos, word, lemma, residue in zip(
                saved["residual_bindings"], [355, 647], [75, 182],
                ["first", "second"], ["L129", "L130"], [54, 85]):
            cert = read(f"third59-{word}-residual-gates.json")
            case = shard["cases"][pos]
            check(f"{index}: entire saved residual binding",
                  binding == dict(
                      fourth_index=index, support=rows[index], lemma=lemma,
                      audit=f"{lemma.lower()}-critical-audit.json", source=cert["source"],
                      shard_case_pointer=f"/cases/{pos}",
                      complete_kernel_basis=case["kernel_basis"],
                      minor_rows=case["minor_rows"], minor_columns=case["pivot_columns"],
                      minor_residue=residue, complete_points=2, passing_points=0)
                  and case["fourth_index"] == index and case["minor_residue"] == residue)
        check("exactly two residual bindings", len(saved["residual_bindings"]) == 2)
        check("all historical residuals retained", len(master["residual_occurrences"]) == 154)
        for name, value in report["input_sha256"].items():
            check("original unchanged " + name, digest(name) == value)
        report["actual_required"] = dict(
            screen=[len(report["complete_screen_checks"]), 756],
            eligible=[len(report["complete_case_checks"]), 282],
            covered=[sum(status_counts.values()), 282], uncovered=[0, 0],
            residual_bindings=[2, 2], original_files_unchanged=[len(names), 29],
            fresh_complete_certificates=[1, 1])
        report["statuses"] = dict(status_counts)
    except Exception as error:
        report["failures"].append(f"{type(error).__name__}: {error}")
    report["audit_program_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    report["summary"] = dict(
        checks_passed=sum(c["passes"] for c in report["checks"]),
        checks_required=len(report["checks"]), failures=len(report["failures"]))
    report["limitations"] = (
        "Audited finite inputs reused; shared Python arithmetic. Actual-row and "
        "extension/chart semantic audit is canonical in L131; no formal verification.")
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print("Summary:", json.dumps(report["summary"], sort_keys=True))
    print("Actual/required:", json.dumps(report.get("actual_required", {}), sort_keys=True))
    print("Failures:", report["failures"])
    print("Certificate:", OUT)
    if report["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    run()
