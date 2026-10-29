"""Audit all C122a manifests/bins and rerun the reviewed endpoint replay.

Run from the notebook: python3 scripts/finite-support/critical_audit_c122a.py
Original artifacts are read-only; fresh replay artifacts have audit names.
Full expected manifests, exact checks, failures and provenance stay on disk.
This checks finite arithmetic, not the endpoint/orbit proof in C122a/L122.
"""

from collections import Counter, defaultdict
from contextlib import redirect_stdout
from hashlib import sha256
import importlib.util
from io import StringIO
import json
from math import isqrt
from pathlib import Path
import struct
import sys


BASE = Path(__file__).resolve().parent
REPORT = BASE / "c122a-critical-audit.json"
FRESH_REPORT = BASE / "c122a-critical-audit-replay.json"
FRESH_BINS = BASE / "c122a-critical-audit-replay-histograms.u32"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    out = {"checks": [], "failures": [], "complete": False}

    def check(label, actual, required):
        ok = actual == required
        record = {"check": label, "ok": ok}
        if isinstance(actual, (dict, list)):
            record.update({"actual_sha256": sha256(json.dumps(actual, sort_keys=True).encode()).hexdigest(),
                           "required_sha256": sha256(json.dumps(required, sort_keys=True).encode()).hexdigest()})
        else:
            record.update({"actual": actual, "required": required})
        out["checks"].append(record)
        if not ok:
            out["failures"].append({"check": label, "actual": actual, "required": required})

    try:
        files = [BASE / name for name in (
            "l122_full_count.py", "l122_full_count_replay.py",
            "l122-full-count.json", "l122-full-count-replay.json",
            "l122-full-count-histograms.u32", "l122-full-count-replay-histograms.u32")]
        before = {p.name: digest(p) for p in files}
        out["original_sha256"] = before
        prod = json.loads(files[2].read_text())
        replay = json.loads(files[3].read_text())
        q, n = 65537, 1024
        N = n * (n - 1) // 2
        check("prime_trial_division", [d for d in range(2, isqrt(q) + 1) if q % d == 0], [])
        check("uint32_format_bytes", struct.calcsize("<I"), 4)
        h = pow(3, 64, q)
        powers = [pow(h, j, q) for j in range(n)]
        roots = [a for a in range(1, q) if pow(a, n, q) == 1]
        check("h", h, 19139)
        check("h_order_tests", [pow(h, n, q), pow(h, n // 2, q), len(set(powers))], [1, q - 1, n])
        check("powers_equal_all_roots", sorted(powers), roots)
        check("root_count", len(roots), n)
        groups = defaultdict(list)
        for a in range(1, q):
            groups[pow(a, n, q)].append(a)
        parts = sorted(groups.values(), key=lambda part: part[0])
        check("coset_number", len(parts), 64)
        check("coset_sizes", [len(part) for part in parts], [n] * 64)
        check("partition", sorted(a for part in parts for a in part), list(range(1, q)))
        for i, part in enumerate(parts):
            check(f"coset_{i}_multiplicative", part, sorted(part[0] * a % q for a in roots))
        cosets = [{"representative": part[0], "elements": part} for part in parts]
        specs = [("vertical", None), ("horizontal", 0)] + [("nonzero", part[0]) for part in parts]
        source_data, replay_data = files[4].read_bytes(), files[5].read_bytes()
        check("production_binary_bytes", len(source_data), 66 * q * 4)
        check("replay_binary_bytes", len(replay_data), 66 * q * 4)
        # Byte equality is supplemented by the full fresh numerical replay below.
        check("original_binary_equality", source_data == replay_data, True)
        check("canonical_binary_digest", before[files[4].name],
              "4f8161677371fe052b12ead70436b92c0ceb508883a5bd658a593086043aa681")
        expected_prod_rows, expected_replay_rows = [], []
        squares, root_set = {a * a % q for a in roots}, set(roots)
        for i, (kind, u) in enumerate(specs):
            offset = i * q * 4
            data = source_data[offset:offset + q * 4]
            counts = struct.unpack(f"<{q}I", data)
            excluded = None if u is None else -u * u % q
            weight = 1 if i < 2 else n
            first = sum(counts)
            second = sum(r * r for r in counts)
            # Multiplication by zero gives the correct value also at r=0,1,2.
            third_all = sum(r * (r - 1) * (r - 2) for r in counts)
            removed = 0 if excluded is None else counts[excluded] * (counts[excluded] - 1) * (counts[excluded] - 2)
            third = third_all - removed
            maximum = max(r for v, r in enumerate(counts) if v != excluded)
            check(f"row_{i}_mass", first, N)
            check(f"row_{i}_matching_bound", maximum <= n // 2, True)
            if excluded is not None:
                check(f"row_{i}_star", counts[excluded], n - 1 if u in root_set else 0)
            if i == 0:
                check("vertical_antipodal_occupancy", counts[0], 512)
                check("vertical_antipodal_third", counts[0] * (counts[0] - 1) * (counts[0] - 2), 133432320)
            if i == 1:
                wrong = [{"bin": v, "actual": r,
                          "required": 511 if v in squares else 512 if v in root_set else 0}
                         for v, r in enumerate(counts)
                         if r != (511 if v in squares else 512 if v in root_set else 0)]
                check("horizontal_every_bin", wrong, [])
            common = {"kind": kind, "slope": u, "offset_bytes": offset,
                      "bins": q, "sha256": sha256(data).hexdigest(), "weight": weight,
                      "first_unexcluded": first, "second_unexcluded": second,
                      "third_eligible": third}
            expected_prod_rows.append(common | {
                "excluded_intercept": excluded,
                "excluded_occupancy": None if excluded is None else counts[excluded],
                "maximum_eligible_occupancy": maximum,
                "occupancy_distribution": {str(k): v for k, v in sorted(Counter(counts).items())},
                "third_unexcluded": third_all})
            expected_replay_rows.append(common | {"mismatches": 0})
            check(f"row_{i}_production_all_fields", prod["rows"][i], expected_prod_rows[-1])
            check(f"row_{i}_replay_all_fields", replay["rows"][i], expected_replay_rows[-1])
        first = sum(row["weight"] * row["first_unexcluded"] for row in expected_prod_rows)
        second = sum(row["weight"] * row["second_unexcluded"] for row in expected_prod_rows)
        vertical, horizontal = [row["third_eligible"] for row in expected_prod_rows[:2]]
        representative = sum(row["third_eligible"] for row in expected_prod_rows[2:])
        total = vertical + horizontal + n * representative
        check("exact_subtotals", [vertical, horizontal, representative, n * representative, total],
              [163243008, 136234398720, 2111184306, 2161852729344, 2298250371072])
        check("first_moment", first, (q + 1) * N)
        check("second_moment", second, N * (N + q))
        upper = N * (N - 1) * (N - 2)
        check("count_bound", total <= upper, True)
        check("arithmetic_bound", upper < 2 ** 57, True)
        artifact = {"path": files[4].name, "encoding": "little-endian uint32",
                    "bytes": len(source_data), "sha256": before[files[4].name]}
        moments = {"first_moment": {"actual": first, "required": (q + 1) * N},
                   "second_moment": {"actual": second, "required": N * (N + q)}}
        expected_prod = {
            "input": "L122", "q": q, "n": n, "failures": [], "rows": expected_prod_rows,
            "generator": h, "H": powers, "cosets": cosets, "pair_count": N, "orbit_weight": n,
            "vertical_antipodal_ordered": 512 * 511 * 510,
            "vertical_ordered": vertical, "horizontal_ordered": horizontal,
            "representative_ordered": representative, "weighted_nonzero_ordered": n * representative,
            "ordered_count": total, **moments, "all_distinct_pair_ordered_upper": upper,
            "histogram_artifact": artifact, "production_updates": 66 * N,
            "production_bins_scanned": 66 * q,
            "packed_main_arrays_bytes": 8 * N + 4 * q + q + 4 * (n + 64),
            "storage_qualification": "4522245 counts packed main array payloads only; coset lists, report objects, buffers and interpreter overhead are additional; no process-memory measurement claimed",
            "scope": "Full-H L122 count only; no uniform core or RS safety conclusion",
            "script_sha256": before[files[0].name], "complete": True}
        expected_replay = {
            "failures": [], "rows": expected_replay_rows, "compared_bins": 66 * q,
            "ordered_count": total, **moments, "source_report_sha256": before[files[2].name],
            "source_histogram_sha256": before[files[4].name],
            "histogram_artifact": artifact | {"path": files[5].name},
            "subgroup_method": "all nonzero roots of X^1024-1, no generator input",
            "coset_method": "partition by x^1024, no production coset routine",
            "endpoint_method": "all ordered pairs, diagonal subtraction, exact halving",
            "scope": "independent numerical replay of L122; not an independent theorem audit",
            "script_sha256": before[files[1].name], "complete": True}
        out["expected_production_manifest"] = expected_prod
        out["expected_replay_manifest"] = expected_replay
        # Compare complete objects: catches extra/missing keys as well as all values.
        check("complete_production_manifest", prod, expected_prod)
        check("complete_replay_manifest", replay, expected_replay)
        out["arithmetic"] = {"ordered_count": total, "upper": upper, "uint57_limit": 2 ** 57,
                             **moments, "bins": 66 * q, "main_payload_bytes": 8 * N + 5 * q + 4 * (n + 64)}
        # Execute exactly the reviewed replay code, changing output destinations only.
        # BASE remains unchanged, so it still reads the original source artifacts.
        sys.dont_write_bytecode = True
        spec = importlib.util.spec_from_file_location("c122a_reviewed_replay", files[1])
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.REPORT, module.BINS = FRESH_REPORT, FRESH_BINS
        stdout = StringIO()
        with redirect_stdout(stdout):
            code = module.main()
        check("fresh_replay_exit", code, 0)
        out["fresh_replay_stdout"] = json.loads(stdout.getvalue())
        fresh = json.loads(FRESH_REPORT.read_text())
        check("fresh_complete_manifest", fresh,
              expected_replay | {"histogram_artifact": artifact | {"path": FRESH_BINS.name}})
        check("fresh_all_bytes", FRESH_BINS.read_bytes() == source_data, True)
        check("original_files_unchanged", {p.name: digest(p) for p in files}, before)
        out["fresh_artifacts"] = {p.name: digest(p) for p in (FRESH_REPORT, FRESH_BINS)}
    except Exception as exc:
        out["failures"].append({"exception": type(exc).__name__, "message": str(exc)})
    out["script_sha256"] = digest(Path(__file__))
    out["complete"] = not out["failures"]
    REPORT.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"complete": out["complete"], "checks": len(out["checks"]),
                      "arithmetic": out.get("arithmetic"), "failures": out["failures"],
                      "certificate": str(REPORT.relative_to(Path.cwd())),
                      "fresh_replay": str(FRESH_REPORT.relative_to(Path.cwd())),
                      "fresh_histograms": str(FRESH_BINS.relative_to(Path.cwd()))}))
    return 0 if out["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
