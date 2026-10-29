"""Independent ordered-endpoint replay of every actual-field L122 bin.

Does not import the production script or use its pair arrays/generator.
H is recovered by root testing, cosets by multiplicative power signatures.
All ordered pairs including the diagonal are generated in shifted product
coordinates; subtract the diagonal, divide by two and translate intercepts.
"""

from array import array
from collections import defaultdict
from hashlib import sha256
from pathlib import Path
import json
import sys


BASE = Path(__file__).resolve().parent
REPORT = BASE / "l122-full-count-replay.json"
BINS = BASE / "l122-full-count-replay-histograms.u32"


def main():
    result = {"failures": [], "rows": [], "compared_bins": 0}

    def check(label, actual, required):
        if actual != required:
            result["failures"].append({"check": label, "actual": actual, "required": required})

    try:
        p, n = 65537, 1024
        check("prime_trial_division", all(p % d for d in range(2, 257)), True)
        H = [x for x in range(1, p) if pow(x, n, p) == 1]
        check("root_subgroup_size", len(H), n)
        groups = defaultdict(list)
        for x in range(1, p):
            groups[pow(x, n, p)].append(x)
        parts = sorted(groups.values(), key=lambda part: part[0])
        check("power_signature_cosets", len(parts), 64)
        check("power_signature_sizes", all(len(part) == n for part in parts), True)
        main_path = BASE / "l122-full-count.json"
        source = json.loads(main_path.read_text())
        check("source_complete", source["complete"], True)
        check("source_failures", source["failures"], [])
        check("independent_H", H, sorted(source["H"]))
        check("independent_cosets", parts, [part["elements"] for part in source["cosets"]])
        check("source_field", [source["q"], source["n"]], [p, n])
        expected_rows = [("vertical", None), ("horizontal", 0)] + [
            ("nonzero", part[0]) for part in parts]
        check("source_row_order", [(row["kind"], row["slope"]) for row in source["rows"]],
              expected_rows)
        original_bins = BASE / source["histogram_artifact"]["path"]
        source_digest, replay_digest = sha256(), sha256()
        pair_count = n * (n - 1) // 2
        check("source_pair_count", source["pair_count"], pair_count)
        first, second, third = 0, 0, 0
        offset = 0
        with original_bins.open("rb") as original, BINS.open("wb") as output:
            for index, (kind, u) in enumerate(expected_rows):
                counts = array("I", [0]) * p
                if kind == "vertical":
                    for a in H:
                        for b in H:
                            counts[(a + b) % p] += 1
                    for a in H:
                        counts[(2 * a) % p] -= 1
                else:
                    shifted = [(a - u) % p for a in H]
                    for a in shifted:
                        for b in shifted:
                            counts[a * b % p] += 1
                    for a in shifted:
                        counts[a * a % p] -= 1
                check(f"row_{index}_even", all(r % 2 == 0 for r in counts), True)
                recovered = array("I", [0]) * p
                for w, r in enumerate(counts):
                    v = w if u is None else (w - u * u) % p
                    recovered[v] = r // 2
                row = source["rows"][index]
                check(f"row_{index}_offset", row["offset_bytes"], offset)
                data = original.read(4 * p)
                check(f"row_{index}_bytes", len(data), 4 * p)
                source_digest.update(data)
                check(f"row_{index}_source_sha256", sha256(data).hexdigest(), row["sha256"])
                saved = array("I")
                saved.frombytes(data)
                if sys.byteorder != "little":
                    saved.byteswap()
                mismatches = [{"bin": v, "saved": a, "replay": b}
                              for v, (a, b) in enumerate(zip(saved, recovered)) if a != b]
                if mismatches:
                    result["failures"].append({"row": index, "mismatches": mismatches})
                result["compared_bins"] += p
                check(f"row_{index}_mass", sum(recovered), pair_count)
                star = None if u is None else (-u * u) % p
                if star is not None:
                    check(f"row_{index}_star", recovered[star], n - 1 if u in H else 0)
                check(f"row_{index}_matching_bound",
                      all(r <= n // 2 for v, r in enumerate(recovered) if v != star), True)
                weight = 1 if index < 2 else n
                row_first = sum(recovered)
                row_second = sum(r ** 2 for r in recovered)
                row_third = sum(r * (r - 1) * (r - 2)
                                for v, r in enumerate(recovered) if v != star and r >= 3)
                check(f"row_{index}_first", row_first, row["first_unexcluded"])
                check(f"row_{index}_second", row_second, row["second_unexcluded"])
                check(f"row_{index}_third", row_third, row["third_eligible"])
                first += weight * row_first
                second += weight * row_second
                third += weight * row_third
                if sys.byteorder != "little":
                    recovered.byteswap()
                replay_data = recovered.tobytes()
                output.write(replay_data)
                replay_digest.update(replay_data)
                result["rows"].append({"kind": kind, "slope": u, "offset_bytes": offset,
                    "bins": p, "mismatches": len(mismatches),
                    "sha256": sha256(replay_data).hexdigest(), "weight": weight,
                    "first_unexcluded": row_first, "second_unexcluded": row_second,
                    "third_eligible": row_third})
                offset += len(replay_data)
            check("no_trailing_source_bytes", len(original.read()), 0)
        check("source_file_digest", source_digest.hexdigest(), source["histogram_artifact"]["sha256"])
        check("complete_binary_equality", replay_digest.hexdigest(), source_digest.hexdigest())
        check("first_moment", first, (p + 1) * pair_count)
        check("second_moment", second, pair_count * (pair_count + p))
        check("ordered_count", third, source["ordered_count"])
        check("all_bins_compared", result["compared_bins"], 66 * p)
        result.update({"ordered_count": third,
            "first_moment": {"actual": first, "required": (p + 1) * pair_count},
            "second_moment": {"actual": second, "required": pair_count * (pair_count + p)},
            "source_report_sha256": sha256(main_path.read_bytes()).hexdigest(),
            "source_histogram_sha256": source_digest.hexdigest(),
            "histogram_artifact": {"path": BINS.name, "encoding": "little-endian uint32",
                                   "bytes": offset, "sha256": replay_digest.hexdigest()},
            "subgroup_method": "all nonzero roots of X^1024-1, no generator input",
            "coset_method": "partition by x^1024, no production coset routine",
            "endpoint_method": "all ordered pairs, diagonal subtraction, exact halving",
            "scope": "independent numerical replay of L122; not an independent theorem audit"})
    except Exception as exc:
        result["failures"].append({"exception": type(exc).__name__, "message": str(exc)})
    result["script_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    result["complete"] = len(result["rows"]) == 66 and not result["failures"]
    REPORT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result.get(key) for key in ["complete", "ordered_count",
        "compared_bins", "first_moment", "second_moment", "failures"]}
        | {"certificate": str(REPORT.relative_to(Path.cwd())),
           "histograms": str(BINS.relative_to(Path.cwd()))}))
    return 0 if result["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
