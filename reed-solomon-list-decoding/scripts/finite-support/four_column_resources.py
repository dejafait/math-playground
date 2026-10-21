#!/usr/bin/env python3
"""Exact profile resource LP; stdlib only, with a full rational certificate."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
REQUIRED = 19800269675
Q = 107
COLS = 9


def partitions(n, ceiling=None):
    if n == 0:
        yield ()
        return
    ceiling = min(n, ceiling if ceiling is not None else n)
    for first in range(ceiling, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def coefficient(a, b):
    return sum(prod(comb(ai, ui) for ai, ui in zip(a, u))
               for u in product(*(range(ai + 1) for ai in a))
               if sum(u) == 5 and
               tuple(sorted((ui for ui in u if ui), reverse=True)) == b)


def capacity(b):
    multiplicities = {i: b.count(i) for i in set(b)}
    placements = factorial(COLS) // factorial(COLS - len(b))
    placements //= prod(factorial(v) for v in multiplicities.values())
    return placements * prod(comb(Q, bi) for bi in b)


def simplex(matrix, bounds):
    m, n = len(bounds), len(matrix[0])
    tab = [[F(v) for v in row] + [F(int(i == j)) for j in range(m)]
           + [F(bounds[i])] for i, row in enumerate(matrix)]
    tab.append([F(-1)] * n + [F(0)] * (m + 1))
    basis = list(range(n, n + m))
    pivots = []
    while True:
        entering = next((j for j in range(n + m) if tab[m][j] < 0), None)
        if entering is None:
            break
        eligible = [i for i in range(m) if tab[i][entering] > 0]
        if not eligible:
            raise RuntimeError("unbounded LP")
        leaving = min(eligible, key=lambda i: (tab[i][-1] / tab[i][entering], basis[i]))
        pivots.append({"enter": entering, "leave": basis[leaving], "row": leaving})
        pivot = tab[leaving][entering]
        tab[leaving] = [v / pivot for v in tab[leaving]]
        for i in range(m + 1):
            if i != leaving:
                factor = tab[i][entering]
                tab[i] = [v - factor * w for v, w in zip(tab[i], tab[leaving])]
        basis[leaving] = entering
        if len(pivots) > 10000:
            raise RuntimeError("pivot budget exceeded")
    primal = [F(0)] * n
    for i, j in enumerate(basis):
        if j < n:
            primal[j] = tab[i][-1]
    dual = tab[m][n:n + m]
    return primal, dual, basis, pivots


def rat(v):
    v = F(v)
    return {"numerator": v.numerator, "denominator": v.denominator}


def main():
    blocks = [a for a in partitions(9) if len(a) <= 4]
    resources = [b for b in partitions(5) if len(b) <= 4]
    matrix = [[coefficient(a, b) for a in blocks] for b in resources]
    bounds = [capacity(b) for b in resources]
    primal, dual, basis, pivots = simplex(matrix, bounds)
    used = [sum(F(ai) * xi for ai, xi in zip(row, primal)) for row in matrix]
    column_values = [sum(dual[i] * matrix[i][j] for i in range(len(resources)))
                     for j in range(len(blocks))]
    objective = sum(primal)
    dual_objective = sum(y * c for y, c in zip(dual, bounds))
    baseline = Q ** 5
    total = F(baseline) + objective
    checks = {
        "all_primal_nonnegative": all(v >= 0 for v in primal),
        "all_dual_nonnegative": all(v >= 0 for v in dual),
        "all_resource_rows": all(u <= c for u, c in zip(used, bounds)),
        "all_dual_columns": all(v >= 1 for v in column_values),
        "equal_objectives": objective == dual_objective,
        "each_block_has_126_five_subsets": all(sum(row[j] for row in matrix) == comb(9, 5)
                                               for j in range(len(blocks))),
        "all_five_subset_types_accounted": sum(bounds) + comb(9, 5) * Q ** 5 == comb(9 * Q, 5),
        "integer_allowance_above_required": total.numerator // total.denominator > REQUIRED,
    }
    result = {
        "scope": {"q": Q, "columns": COLS, "block_size": 9, "resource_size": 5,
                  "max_block_columns": 4, "extra_embedding_points_used": 0},
        "block_profiles": [list(a) for a in blocks],
        "resource_profiles": [list(b) for b in resources],
        "matrix": matrix,
        "capacities": bounds,
        "primal": [rat(v) for v in primal],
        "dual": [rat(v) for v in dual],
        "row_usage": [rat(v) for v in used],
        "row_slack": [rat(F(c) - u) for c, u in zip(bounds, used)],
        "dual_column_values": [rat(v) for v in column_values],
        "objective": rat(objective),
        "dual_objective": rat(dual_objective),
        "baseline": baseline,
        "total_allowance": rat(total),
        "integer_total_allowance": total.numerator // total.denominator,
        "required_threshold": REQUIRED,
        "excess_over_required": rat(total - REQUIRED),
        "basis": basis,
        "pivots": pivots,
        "checks": checks,
        "failures": [k for k, v in checks.items() if not v],
        "interpretation": "Resource nonexclusion only; primal variables are not an actual packing.",
    }
    output = HERE / "four-column-resource-results.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"profiles: {len(blocks)} blocks, {len(resources)} resources; pivots={len(pivots)}")
    print(f"baseline={baseline}; exact added optimum={objective}; exact total={total}")
    print(f"integer allowance={result['integer_total_allowance']}; required={REQUIRED}")
    print(f"checks={len(checks)}; failures={result['failures']}; certificate={output.relative_to(HERE.parent.parent)}")
    if result["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
