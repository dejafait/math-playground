"""Exact auxiliary projection orbits for the span-two collision test.

Run from the notebook: python3 scripts/finite-support/span_two_direction_orbits.py
This is a finite F_137 computation, not a sampled actual-label rank test.
"""

import ast
import itertools
import json
from pathlib import Path


def main():
    q = 137
    directions = [16, 64, 70, 102, 112, 118, 121]
    failures = []
    cases = []
    size_table = []
    required_witnesses = []
    for a, b in itertools.combinations(directions, 2):
        row = {"pair": [a, b], "sizes_by_omission": {}}
        for omitted in [None] + [t for t in directions if t not in (a, b)]:
            remaining = [t for t in directions if t not in (a, b, omitted)]
            kappas = {
                t: ((t - a) * pow((t - b) % q, -1, q)) % q
                for t in remaining
            }
            anchor = remaining[0]
            generators = [
                (kappas[t] * pow(kappas[anchor], -1, q)) % q
                for t in remaining[1:]
            ]
            subgroup = {1}
            frontier = [1]
            words = {1: [0] * len(generators)}
            while frontier:
                h = frontier.pop(0)
                for index, generator in enumerate(generators):
                    value = h * generator % q
                    if value not in subgroup:
                        subgroup.add(value)
                        frontier.append(value)
                        word = words[h].copy()
                        word[index] += 1
                        words[value] = word
            # Verify the entire generated set is a multiplicative subgroup.
            closure_ok = all(x * y % q in subgroup for x in subgroup for y in subgroup)
            inverse_ok = all(pow(x, -1, q) in subgroup for x in subgroup)
            remaining_nonzero = set(range(1, q))
            cosets = []
            while remaining_nonzero:
                representative = min(remaining_nonzero)
                coset = {representative * h % q for h in subgroup}
                cosets.append(sorted(coset))
                remaining_nonzero -= coset
            passed = closure_ok and inverse_ok and len(subgroup) >= 68 and len(cosets) <= 2
            key = "none" if omitted is None else str(omitted)
            row["sizes_by_omission"][key] = len(subgroup)
            case = {
                "pair": [a, b], "omitted": omitted, "remaining": remaining,
                "kappas": kappas, "anchor": anchor, "generators": generators,
                "subgroup": sorted(subgroup), "cosets": cosets,
                "closure_ok": closure_ok, "inverse_ok": inverse_ok,
                "subgroup_size": len(subgroup), "orbit_count": len(cosets),
                "passed": passed,
            }
            cases.append(case)
            if not passed:
                failures.append({"pair": [a, b], "omitted": omitted})
            if omitted is None:
                word = words.get(2)
                product = 1
                if word is not None:
                    for generator, exponent in zip(generators, word):
                        product = product * pow(generator, exponent, q) % q
                required_witnesses.append({
                    "pair": [a, b], "remaining": remaining,
                    "anchor": anchor, "generators": generators,
                    "exponents": word, "product": product,
                    "passed": word is not None and product == 2 and passed,
                })
        size_table.append(row)
    probe = {
        "case_count": len(cases), "required_case_count": 126,
        "minimum_subgroup_size": min(c["subgroup_size"] for c in cases),
        "required_minimum_subgroup_size": 68,
        "maximum_orbit_count": max(c["orbit_count"] for c in cases),
        "required_maximum_orbit_count": 2,
        "failures": failures,
        "all_passed": not failures and len(cases) == 126,
    }
    required_cases = [case for case in cases if case["omitted"] is None]
    order_checks = {"2^68": pow(2, 68, q), "2^34": pow(2, 34, q),
                    "2^4": pow(2, 4, q)}
    required_failures = [witness["pair"] for witness in required_witnesses
                         if not witness["passed"]]
    # Check the load-bearing table printed in the canonical proof against
    # every computed ratio and modular product, including order and coverage.
    lemma_path = Path(__file__).resolve().parents[2] / "lemmas/L135-span-two-evaluation-line-separation.md"
    printed_rows = []
    for line in lemma_path.read_text().splitlines():
        if line.startswith("| (") and line[3:4].isdigit():
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            printed_rows.append([list(ast.literal_eval(cell)) for cell in cells])
    expected_rows = [[w["pair"], w["generators"], w["exponents"]]
                     for w in required_witnesses]
    table_matches = printed_rows == expected_rows
    summary = {
        "case_count": len(required_cases), "required_case_count": 21,
        "minimum_subgroup_size": min(c["subgroup_size"] for c in required_cases),
        "required_minimum_subgroup_size": 68,
        "maximum_orbit_count": max(c["orbit_count"] for c in required_cases),
        "required_maximum_orbit_count": 2,
        "witness_element": 2, "witness_order": 68,
        "order_checks": order_checks, "failures": required_failures,
        "canonical_table_rows": len(printed_rows),
        "canonical_table_matches": table_matches,
        "all_passed": not required_failures and len(required_cases) == 21
                      and order_checks == {"2^68": 1, "2^34": 136, "2^4": 16}
                      and table_matches,
    }
    path = Path(__file__).with_name("span-two-direction-orbits.json")
    path.write_text(json.dumps({"q": q, "T": directions, "summary": summary,
                                "required_witnesses": required_witnesses,
                                "arbitrary_omission_probe": probe,
                                "size_table": size_table, "cases": cases}, indent=2) + "\n")
    print("Required seven-direction test: " + json.dumps(summary, sort_keys=True))
    print("Stronger arbitrary-omission probe: " + json.dumps(probe, sort_keys=True))
    print(f"Full certificate: {path}")
    if not summary["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
