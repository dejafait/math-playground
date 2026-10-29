"""Reproduce L122 on its actual field; save every bin, print only a summary.

Run from the notebook: python3 scripts/finite-support/l122_full_count.py
Only Python standard-library, exact-integer arithmetic is used.
The binary histogram certificate is row-major little-endian uint32.
"""

from array import array
from collections import Counter
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import sys


BASE = Path(__file__).resolve().parent
REPORT = BASE / "l122-full-count.json"
BINS = BASE / "l122-full-count-histograms.u32"
Q, N_H = 65537, 1024


def f3(r):
    return r * (r - 1) * (r - 2) if r >= 3 else 0


def little_bytes(values):
    copy = array("I", values)
    if sys.byteorder != "little":
        copy.byteswap()
    return copy.tobytes()


def main():
    result = {"input": "L122", "q": Q, "n": N_H, "failures": [], "rows": []}

    def check(label, actual, required):
        if actual != required:
            result["failures"].append({"check": label, "actual": actual,
                                       "required": required})

    try:
        check("uint32_itemsize", array("I").itemsize, 4)
        h = pow(3, 64, Q)
        H = array("I", (pow(h, j, Q) for j in range(N_H)))
        check("generator_full_power", pow(h, N_H, Q), 1)
        check("generator_half_power", pow(h, N_H // 2, Q), Q - 1)
        check("subgroup_distinct", len(set(H)), N_H)
        marks = bytearray(Q)
        representatives = array("I")
        cosets = []
        for u in range(1, Q):
            if marks[u]:
                continue
            part = sorted(u * a % Q for a in H)
            check(f"coset_{u}_distinct", len(set(part)), N_H)
            check(f"coset_{u}_overlap", sum(marks[x] for x in part), 0)
            for x in part:
                marks[x] = 1
            representatives.append(u)
            cosets.append({"representative": u, "elements": part})
        check("coset_count", len(cosets), 64)
        check("coset_partition", sum(marks), Q - 1)
        check("first_representative", representatives[0], 1)
        sums, products = array("I"), array("I")
        for i, a in enumerate(H):
            for j in range(i + 1, N_H):
                b = H[j]
                sums.append((a + b) % Q)
                products.append(a * b % Q)
        pair_count = comb(N_H, 2)
        check("pair_count", len(sums), pair_count)
        check("product_count", len(products), pair_count)
        result.update({"generator": h, "H": list(H), "cosets": cosets,
                       "pair_count": pair_count, "orbit_weight": N_H})
        stream_hash = sha256()
        offset = 0
        with BINS.open("wb") as output:
            for kind, slope in [("vertical", None), ("horizontal", 0)] + [
                    ("nonzero", int(u)) for u in representatives]:
                counts = array("I", [0]) * Q
                if kind == "vertical":
                    for s in sums:
                        counts[s] += 1
                elif kind == "horizontal":
                    for t in products:
                        counts[t] += 1
                else:
                    for s, t in zip(sums, products):
                        counts[(t - slope * s) % Q] += 1
                label = f"{kind}_{slope}"
                excluded = None if slope is None else (-slope * slope) % Q
                check(label + "_mass", sum(counts), pair_count)
                if excluded is not None:
                    check(label + "_star", counts[excluded],
                          N_H - 1 if slope in H else 0)
                eligible_max = max(r for v, r in enumerate(counts) if v != excluded)
                check(label + "_matching_bound", eligible_max <= N_H // 2, True)
                third = sum(f3(r) for v, r in enumerate(counts) if v != excluded)
                first = sum(counts)
                second = sum(r * r for r in counts)
                if kind == "vertical":
                    check("antipodal_occupancy", counts[0], 512)
                    check("antipodal_third", f3(counts[0]), 133432320)
                    result["vertical_antipodal_ordered"] = f3(counts[0])
                if kind == "horizontal":
                    squares = {a * a % Q for a in H}
                    h_set = set(H)
                    check("horizontal_all_bins", all(
                        r == (511 if v in squares else 512 if v in h_set else 0)
                        for v, r in enumerate(counts)), True)
                    check("horizontal_third", third, 136234398720)
                data = little_bytes(counts)
                output.write(data)
                stream_hash.update(data)
                result["rows"].append({
                    "kind": kind, "slope": slope, "offset_bytes": offset,
                    "bins": Q, "sha256": sha256(data).hexdigest(),
                    "weight": N_H if kind == "nonzero" else 1,
                    "excluded_intercept": excluded,
                    "excluded_occupancy": None if excluded is None else counts[excluded],
                    "maximum_eligible_occupancy": eligible_max,
                    "occupancy_distribution": dict(sorted(Counter(counts).items())),
                    "first_unexcluded": first, "second_unexcluded": second,
                    "third_unexcluded": sum(f3(r) for r in counts),
                    "third_eligible": third,
                })
                offset += len(data)
        rows = result["rows"]
        vertical = rows[0]["third_eligible"]
        horizontal = rows[1]["third_eligible"]
        representative = sum(row["third_eligible"] for row in rows[2:])
        total = vertical + horizontal + N_H * representative
        actual_first = sum(row["weight"] * row["first_unexcluded"] for row in rows)
        actual_second = sum(row["weight"] * row["second_unexcluded"] for row in rows)
        check("first_moment", actual_first, (Q + 1) * pair_count)
        check("second_moment", actual_second, pair_count ** 2 + Q * pair_count)
        check("all_distinct_pair_upper", total <= f3(pair_count), True)
        check("uint64_accumulator_bound", f3(pair_count) < 2 ** 57, True)
        check("rows_count", len(rows), 66)
        check("histogram_file_size", BINS.stat().st_size, 66 * Q * 4)
        result.update({
            "vertical_ordered": vertical, "horizontal_ordered": horizontal,
            "representative_ordered": representative,
            "weighted_nonzero_ordered": N_H * representative, "ordered_count": total,
            "first_moment": {"actual": actual_first, "required": (Q + 1) * pair_count},
            "second_moment": {"actual": actual_second,
                              "required": pair_count ** 2 + Q * pair_count},
            "all_distinct_pair_ordered_upper": f3(pair_count),
            "histogram_artifact": {"path": BINS.name, "encoding": "little-endian uint32",
                                   "bytes": offset, "sha256": stream_hash.hexdigest()},
            "production_updates": 66 * pair_count, "production_bins_scanned": 66 * Q,
            "packed_main_arrays_bytes": sums.itemsize * len(sums) + products.itemsize * len(products)
                + counts.itemsize * len(counts) + len(marks)
                + H.itemsize * len(H) + representatives.itemsize * len(representatives),
            "storage_qualification": "4522245 counts packed main array payloads only; "
                "coset lists, report objects, buffers and interpreter overhead are additional; "
                "no process-memory measurement claimed",
            "scope": "Full-H L122 count only; no uniform core or RS safety conclusion",
        })
    except Exception as exc:
        result["failures"].append({"exception": type(exc).__name__, "message": str(exc)})
    result["script_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    result["complete"] = len(result["rows"]) == 66 and not result["failures"]
    REPORT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result.get(key) for key in [
        "complete", "ordered_count", "vertical_ordered", "horizontal_ordered",
        "weighted_nonzero_ordered", "first_moment", "second_moment", "failures"]}
        | {"certificate": str(REPORT.relative_to(Path.cwd())),
           "histograms": str(BINS.relative_to(Path.cwd()))}))
    return 0 if result["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
