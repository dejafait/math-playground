"""Independent intersection-first reconstruction of all load-bearing counts."""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
import json


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first,) + rest


def c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    path = Path(__file__).with_name("four-column-gilbert-results.json")
    original = json.loads(path.read_text())
    profiles = [tuple(row["profile"]) for row in original["profiles"]]
    checks, failures = [], []

    def check(name, passed):
        checks.append({"name": name, "passed": bool(passed)})
        if not passed:
            failures.append(name)

    q, columns, weight = 107, 9, 9
    sizes = Counter()
    occupancy_count = 0
    for occupancy in compositions(weight, columns):
        b = tuple(sorted((v for v in occupancy if v), reverse=True))
        if len(b) > 4:
            continue
        occupancy_count += 1
        count = 1
        for value in occupancy:
            count *= c(q, value)
        sizes[b] += count
    check("independent profile set", set(sizes) == set(profiles))
    residuals = {r: list(compositions(r, columns)) for r in range(5)}
    exact = {}
    for a in profiles:
        padded = a + (0,) * (columns - len(a))
        row = {b: [0] * 5 for b in profiles}
        # Pick the complete intersection first, then points in its complement.
        for short_intersection in product(*(range(size + 1) for size in a)):
            j = sum(short_intersection)
            if j < 5:
                continue
            intersection = short_intersection + (0,) * (columns - len(a))
            intersection_count = 1
            for size, value in zip(a, short_intersection):
                intersection_count *= c(size, value)
            for residual in residuals[weight - j]:
                occupied = tuple(intersection[i] + residual[i] for i in range(columns))
                b = tuple(sorted((v for v in occupied if v), reverse=True))
                if len(b) > 4:
                    continue
                count = intersection_count
                for i in range(columns):
                    count *= c(q - padded[i], residual[i])
                row[b][j - 5] += count
        exact[a] = row
    matrix = []
    table = []
    for index, a in enumerate(profiles):
        old = original["profiles"][index]
        check(f"universe count {a}", old["size"] == sizes[a])
        matrix_row = []
        for column, b in enumerate(profiles):
            saved = old["intersection_counts_by_target_profile"][column]
            check(f"profile ordering {a}/{b}", tuple(saved["target_profile"]) == b)
            check(f"all five conflict intersection counts {a}/{b}",
                  saved["by_intersection_0_to_9"][5:] == exact[a][b])
            check(f"neighborhood contribution {a}/{b}",
                  saved["closed_neighborhood_contribution"] == sum(exact[a][b]))
            matrix_row.append(sum(exact[a][b]))
        matrix.append(matrix_row)
        d = sum(matrix_row)
        self_d = matrix_row[index]
        lower = (sizes[a] + self_d - 1) // self_d
        check(f"union degree {a}", d == old["union_closed_neighborhood"])
        check(f"single profile degree {a}", self_d == old["single_profile_closed_neighborhood"])
        check(f"single profile lower {a}", lower == old["single_profile_lower"])
        check(f"single profile total {a}", original["baseline"] + lower == old["baseline_plus_lower"])
        check(f"single profile decision {a}", old["strictly_exceeds_benchmark"] ==
              (original["baseline"] + lower > original["benchmark"]))
        table.append({"profile": list(a), "size": sizes[a], "union_degree": d,
                      "single_degree": self_d, "single_lower": lower})
    union_size = sum(sizes.values())
    max_d = max(sum(r) for r in matrix)
    union_lower = (union_size + max_d - 1) // max_d
    best = max([union_lower] + [row["single_lower"] for row in table])
    best_profiles = [row["profile"] for row in table if row["single_lower"] == best]
    baseline, benchmark = 107 ** 5, 19800269675
    check("baseline", original["baseline"] == baseline)
    check("benchmark", original["benchmark"] == benchmark)
    check("strict added target", original["required_added_to_exceed"] == benchmark + 1 - baseline)
    check("union certificate", original["union"] == {
        "size": union_size, "maximum_closed_neighborhood": max_d,
        "maximizing_profiles": [list(a) for a, r in zip(profiles, matrix) if sum(r) == max_d],
        "lower": union_lower, "baseline_plus_lower": baseline + union_lower,
        "strictly_exceeds_benchmark": baseline + union_lower > benchmark})
    check("best certificate", original["best_alternative"] == {
        "added_lower": best, "total_lower": baseline + best,
        "strictly_exceeds_benchmark": baseline + best > benchmark,
        "shortfall_to_strict_target": benchmark + 1 - (baseline + best)})
    check("all original checks pass", all(row["passed"] for row in original["checks"]) and
          original["failures"] == [])
    # Fully read every direct small-case row, not merely its failure field.
    small_summary = []
    for case_index, case in enumerate(original["small_cases"]):
        params = case["parameters"]
        ps = [tuple(a) for a in case["profiles"]]
        evidence = case["every_vertex"]
        counters = Counter(tuple(v["profile"]) for v in evidence)
        valid_masks = []
        n = params["columns"] * params["q"]
        # Binary masks give a separate exhaustive universe generator.
        for mask in range(1 << n):
            if mask.bit_count() != params["weight"]:
                continue
            occ = [sum((mask >> (col * params["q"] + value)) & 1
                       for value in range(params["q"])) for col in range(params["columns"])]
            if sum(v > 0 for v in occ) <= params["max_columns"]:
                valid_masks.append((mask, tuple(sorted((v for v in occ if v), reverse=True))))
        check(f"small case {case_index} every vertex present",
              sorted((v["mask"], tuple(v["profile"])) for v in evidence) == valid_masks)
        all_histograms_pass = True
        maximum = 0
        for v in evidence:
            expected = {b: [0] * (params["weight"] + 1) for b in ps}
            for mask, b in valid_masks:
                intersection = (mask & v["mask"]).bit_count()
                expected[b][intersection] += 1
            all_histograms_pass &= v["histograms"] == [expected[b] for b in ps]
            d = sum(sum(hist[params["conflict"]:]) for hist in v["histograms"])
            maximum = max(maximum, d)
            all_histograms_pass &= all(sum(hist) == counters[b] for b, hist in zip(ps, v["histograms"]))
        check(f"small case {case_index} complete histograms", all_histograms_pass)
        check(f"small case {case_index} bound and coverage",
              case["vertex_count"] == len(valid_masks) and
              case["ordered_pairs_checked"] == len(valid_masks) ** 2 and
              maximum == case["maximum_closed_neighborhood"] and
              case["gilbert_lower"] == (len(valid_masks) + maximum - 1) // maximum and
              case["failures"] == [])
        small_summary.append({"parameters": params, "vertices": len(valid_masks),
                              "ordered_pairs": len(valid_masks) ** 2,
                              "all_histograms_pass": bool(all_histograms_pass)})
    audit = {"independent_method": "complete-intersection-first, complement occupancies",
             "labeled_occupancies": occupancy_count, "profile_table": table,
             "full_neighborhood_matrix": matrix,
             "conflict_histograms": [{"profile": list(a), "by_target_profile": [exact[a][b] for b in profiles]}
                                      for a in profiles],
             "comparison": {"baseline": baseline, "benchmark": benchmark,
                            "required_added": benchmark + 1 - baseline,
                            "union_size": union_size, "union_maximum_degree": max_d,
                            "union_lower": union_lower, "best_added": best,
                            "best_profiles": best_profiles, "best_total": baseline + best,
                            "shortfall": benchmark + 1 - (baseline + best)},
             "small_cases": small_summary, "checks": checks, "failures": failures}
    out = path.with_name("four-column-gilbert-audit-results.json")
    out.write_text(json.dumps(audit, indent=2) + "\n")
    print(f"Independent labeled occupancies: {occupancy_count}; reconstructed conflict histograms: {18*18*5}")
    print(f"Checks: {len(checks)}; failures: {failures}")
    print(f"Best profiles: {best_profiles}; total={baseline + best}; required={benchmark + 1}")
    print(f"Full audit: {out}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
