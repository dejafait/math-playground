#!/usr/bin/env python3
"""Check the canonical L043 tables, exact witnesses, and integer rounding."""
from fractions import Fraction as F
from itertools import combinations_with_replacement, product
from math import comb, factorial, prod
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def main():
    original = json.loads((HERE / "four-column-resource-results.json").read_text())
    audit = json.loads((HERE / "four-column-resource-audit-results.json").read_text())
    text = (ROOT / "lemmas/L043-four-column-resource-optimum.md").read_text()
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
    def rational(v):
        return F(v["numerator"], v["denominator"])

    # Every positive partition has a unique nondecreasing zero-padded tuple.
    blocks = sorted({tuple(v for v in reversed(a) if v)
                     for a in combinations_with_replacement(range(10), 4)
                     if sum(a) == 9}, reverse=True)
    resources = sorted({tuple(v for v in reversed(b) if v)
                        for b in combinations_with_replacement(range(6), 4)
                        if sum(b) == 5}, reverse=True)
    check("all_block_profiles", blocks == [tuple(a) for a in original["block_profiles"]] and len(blocks) == 18)
    check("all_resource_profiles", resources == [tuple(b) for b in original["resource_profiles"]] and len(resources) == 6)
    matrix = []
    capacities = []
    for b in resources:
        capacities.append(factorial(9) // factorial(9-len(b))
                          // prod(factorial(b.count(i)) for i in set(b))
                          * prod(comb(107, i) for i in b))
        matrix.append([sum(prod(comb(ai, ui) for ai, ui in zip(a, u))
                           for u in product(*(range(ai+1) for ai in a))
                           if sum(u) == 5 and tuple(sorted((v for v in u if v), reverse=True)) == b)
                       for a in blocks])
    check("both_complete_matrices", matrix == original["matrix"] == audit["matrix"])
    check("both_complete_capacities", capacities == original["capacities"] == audit["capacities"])
    check("all_block_subsets", all(sum(row[j] for row in matrix) == 126 for j in range(18)))
    check("all_ground_subsets", sum(capacities) + comb(9, 5)*107**5 == comb(963, 5))

    # These witnesses are copied from the mathematical statement, not optimized.
    x = [F(0)]*18
    for a, value in [((5,2,1,1), F(956777094)), ((4,2,2,1), F(367059422016,95)),
                     ((3,2,2,2), F(1284582693324,95))]:
        x[blocks.index(a)] = value
    y = [F(v,57) for v in (17,0,2,0,1,0)]
    check("stated_primal", x == [rational(v) for v in original["primal"]] and all(v >= 0 for v in x))
    check("stated_dual", y == [rational(v) for v in original["dual"]] and all(v >= 0 for v in y))
    usage = [sum(a*v for a,v in zip(row,x)) for row in matrix]
    slack = [F(c)-u for c,u in zip(capacities,usage)]
    dual_columns = [sum(y[i]*matrix[i][j] for i in range(6)) for j in range(18)]
    for key, values in [("row_usage",usage),("row_slack",slack),("dual_column_values",dual_columns)]:
        check("both_"+key, all(values == [rational(v) for v in artifact[key]] for artifact in (original,audit)))
    check("all_primal_constraints", all(v >= 0 for v in slack))
    check("all_dual_constraints", all(v >= 1 for v in dual_columns))
    objective = sum(x)
    check("exact_optimum", objective == sum(c*v for c,v in zip(capacities,y)) == F(348507187854,19)
          == rational(original["objective"]) == rational(original["dual_objective"]) == rational(audit["added_optimum"]))

    table_rows = [[v.strip() for v in line.strip().strip('|').split('|')]
                  for line in text.splitlines() if line.startswith('|')]
    for j,a in enumerate(blocks):
        label = ''.join(map(str,a))
        rows = [r for r in table_rows if len(r) == 8 and r[0] == label]
        expected = [matrix[i][j] for i in range(6)] + [int(57*dual_columns[j])]
        check("canonical_block_"+label, len(rows) == 1 and list(map(int,rows[0][1:])) == expected)
    for i,b in enumerate(resources):
        label = ''.join(map(str,b))
        rows = [r for r in table_rows if len(r) == 3 and r[0] == label]
        check("canonical_resource_"+label, len(rows) == 1 and int(rows[0][1]) == capacities[i] and F(rows[0][2]) == slack[i])

    integer_x = [v.numerator//v.denominator for v in x]
    integer_slack = [c-sum(a*v for a,v in zip(row,integer_x)) for c,row in zip(capacities,matrix)]
    total = F(107**5)+objective
    integer_total = 107**5+sum(integer_x)
    check("integer_feasibility", all(v >= 0 for v in integer_x+integer_slack))
    check("exact_total", total == F(614992016687,19) == rational(original["total_allowance"]) == rational(audit["total_allowance"]))
    check("baseline", original["baseline"] == 107**5 == 14025517307)
    check("total_floor", total.numerator//total.denominator == 32368000878 == original["integer_total_allowance"] == audit["integer_total_allowance"])
    check("rounding_and_threshold", integer_total == 32368000877 and integer_total >= 32368000878-2
          and integer_total > 19800269675 == original["required_threshold"] == audit["required_threshold"])
    check("excess", rational(original["excess_over_required"]) == total-19800269675)
    check("old_checks_and_failures", all(all(d["checks"].values()) and not d["failures"] for d in (original,audit)))
    result = {"scope": "L043 critical audit only; feasible counts do not construct blocks",
              "block_profiles": blocks, "resource_profiles": resources,
              "matrix": matrix, "capacities": capacities,
              "primal": list(map(str,x)), "dual": list(map(str,y)),
              "row_usage": list(map(str,usage)), "row_slack": list(map(str,slack)),
              "dual_columns": list(map(str,dual_columns)), "added_optimum": str(objective),
              "integer_primal": integer_x, "integer_slack": integer_slack,
              "integer_total": integer_total, "required_strict_benchmark": 19800269675,
              "checks": checks, "failures": [k for k,v in checks.items() if not v]}
    path = HERE / "four-column-resource-critical-audit-results.json"
    path.write_text(json.dumps(result, indent=2)+"\n")
    print(f"canonical tables: 108 coefficients, 18 dual numerators, 6 capacities/slacks")
    print(f"added optimum={objective}; integer witness total={integer_total}; required >19800269675")
    print(f"checks={len(checks)}; failures={result['failures']}; certificate={path.relative_to(ROOT)}")
    if result["failures"]:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
