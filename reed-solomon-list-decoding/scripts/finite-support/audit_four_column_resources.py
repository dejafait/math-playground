#!/usr/bin/env python3
"""Rebuild every incidence/capacity and check saved witnesses, without simplex."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def rat(v):
    return F(v["numerator"], v["denominator"])


def encode(v):
    return {"numerator": v.numerator, "denominator": v.denominator}


def weak_compositions(n, length):
    if length == 1:
        yield (n,)
    else:
        for i in range(n + 1):
            for tail in weak_compositions(n - i, length - 1):
                yield (i,) + tail


def main():
    source = HERE / "four-column-resource-results.json"
    data = json.loads(source.read_text())
    checks = {}
    def check(label, condition):
        checks[label] = bool(condition)

    check("scope", data["scope"] == {"q": 107, "columns": 9, "block_size": 9,
                                    "resource_size": 5, "max_block_columns": 4,
                                    "extra_embedding_points_used": 0})
    block_profiles = sorted({tuple(v for v in a if v) for a in product(range(10), repeat=4)
                             if sum(a) == 9 and all(a[i] >= a[i+1] for i in range(3))},
                            reverse=True)
    capacities = Counter()
    occupancy_vectors = 0
    for occupancy in weak_compositions(5, 9):
        occupancy_vectors += 1
        profile = tuple(sorted((i for i in occupancy if i), reverse=True))
        capacities[profile] += prod(comb(107, i) for i in occupancy)
    resource_profiles = sorted((b for b in capacities if len(b) <= 4), reverse=True)
    check("block_profile_completeness", block_profiles == [tuple(a) for a in data["block_profiles"]])
    check("resource_profile_completeness", resource_profiles == [tuple(b) for b in data["resource_profiles"]])
    check("all_1287_occupancies", occupancy_vectors == comb(13, 8))
    check("total_five_subsets", sum(capacities.values()) == comb(963, 5))
    check("transversal_five_subset_capacity", capacities[(1, 1, 1, 1, 1)] == comb(9, 5) * 107 ** 5)
    rebuilt_columns = []
    for j, a in enumerate(block_profiles):
        point_columns = [i for i, size in enumerate(a) for _ in range(size)]
        counts = Counter()
        for subset in combinations(range(9), 5):
            occupancy = Counter(point_columns[k] for k in subset)
            profile = tuple(sorted(occupancy.values(), reverse=True))
            counts[profile] += 1
        column = [counts[b] for b in resource_profiles]
        rebuilt_columns.append(column)
        check(f"all_six_coefficients_for_{a}", column == [row[j] for row in data["matrix"]])
        check(f"all_126_subsets_for_{a}", sum(column) == comb(9, 5))
    matrix = [[column[i] for column in rebuilt_columns] for i in range(len(resource_profiles))]
    bounds = [capacities[b] for b in resource_profiles]
    for i, b in enumerate(resource_profiles):
        check(f"capacity_{b}", bounds[i] == data["capacities"][i])
    primal = [rat(v) for v in data["primal"]]
    dual = [rat(v) for v in data["dual"]]
    check("primal_dimension_and_sign", len(primal) == 18 and all(v >= 0 for v in primal))
    check("dual_dimension_and_sign", len(dual) == 6 and all(v >= 0 for v in dual))
    usages, slacks = [], []
    for i, row in enumerate(matrix):
        usage = sum(a * x for a, x in zip(row, primal))
        slack = F(bounds[i]) - usage
        usages.append(usage)
        slacks.append(slack)
        check(f"primal_row_{i}", slack >= 0 and usage == rat(data["row_usage"][i])
              and slack == rat(data["row_slack"][i]))
    dual_columns = []
    for j in range(18):
        value = sum(dual[i] * matrix[i][j] for i in range(6))
        dual_columns.append(value)
        check(f"dual_column_{j}", value >= 1 and value == rat(data["dual_column_values"][j]))
    primal_objective = sum(primal)
    dual_objective = sum(y * c for y, c in zip(dual, bounds))
    check("equal_optimal_objectives", primal_objective == dual_objective == rat(data["objective"])
          == rat(data["dual_objective"]))
    total = F(107 ** 5) + primal_objective
    check("baseline", data["baseline"] == 107 ** 5)
    check("exact_total_and_floor", total == rat(data["total_allowance"])
          and total.numerator // total.denominator == data["integer_total_allowance"])
    check("threshold_and_excess", data["required_threshold"] == 19800269675
          and rat(data["excess_over_required"]) == total - 19800269675
          and data["integer_total_allowance"] > 19800269675)
    check("reported_checks", all(data["checks"].values()) and data["failures"] == [])
    result = {
        "source": str(source.relative_to(HERE.parent.parent)),
        "occupancy_vectors": occupancy_vectors,
        "matrix": matrix,
        "capacities": bounds,
        "row_usage": [encode(v) for v in usages],
        "row_slack": [encode(v) for v in slacks],
        "dual_column_values": [encode(v) for v in dual_columns],
        "added_optimum": encode(primal_objective),
        "total_allowance": encode(total),
        "integer_total_allowance": total.numerator // total.denominator,
        "required_threshold": 19800269675,
        "checks": checks,
        "failures": [k for k, v in checks.items() if not v],
    }
    output = HERE / "four-column-resource-audit-results.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"verified 108 coefficients, 6 capacities, 6 primal rows, 18 dual columns")
    print(f"exact added optimum={primal_objective}; total={total}; integer={result['integer_total_allowance']}; required=19800269675")
    print(f"checks={len(checks)}; failures={result['failures']}; certificate={output.relative_to(HERE.parent.parent)}")
    if result["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
