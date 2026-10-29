"""Independent exact audit of L135's printed witnesses and full orbit data.

Run from this notebook: python3 scripts/finite-support/critical_audit_l135.py
Uses a discrete-log/gcd construction, not the producer's subgroup BFS.
The geometry is audited in the canonical lemma; this checks finite data.
"""

import ast
import hashlib
import itertools
import json
import re
from math import gcd, isqrt
from pathlib import Path


def main():
    notebook = Path(__file__).resolve().parents[2]
    source_path = Path(__file__).with_name("span-two-direction-orbits.json")
    generator_path = Path(__file__).with_name("span_two_direction_orbits.py")
    lemma_path = notebook / "lemmas/L135-span-two-evaluation-line-separation.md"
    output_path = Path(__file__).with_name("l135-critical-audit.json")
    source = json.loads(source_path.read_text())
    q = 137
    directions = [16, 64, 70, 102, 112, 118, 121]
    pairs = list(itertools.combinations(directions, 2))
    failures = []

    def check(condition, label):
        if not condition:
            failures.append(label)

    check(all(q % d for d in range(2, isqrt(q) + 1)), "prime modulus")
    check(source["q"] == q and source["T"] == directions, "input parameters")
    # Find a generator by listing every power, independently of source data.
    primitive = next(a for a in range(2, q)
                     if len({pow(a, j, q) for j in range(q - 1)}) == q - 1)
    powers = [pow(primitive, j, q) for j in range(q - 1)]
    logs = {value: j for j, value in enumerate(powers)}
    order_two = next(j for j in range(1, q) if pow(2, j, q) == 1)
    check(order_two == 68, "exact order of 2")
    order_checks = {"2^68": pow(2, 68, q), "2^34": pow(2, 34, q),
                    "2^4": pow(2, 4, q)}
    check(order_checks == {"2^68": 1, "2^34": 136, "2^4": 16},
          "three printed order witnesses")

    printed_rows = []
    for line in lemma_path.read_text().splitlines():
        if re.match(r"\|\s*\(\d", line):
            printed_rows.append([list(ast.literal_eval(cell.strip()))
                                 for cell in line.strip("|").split("|")])
    check([row[0] for row in printed_rows] == [list(pair) for pair in pairs],
          "canonical table has exactly all 21 pairs in order")
    check(len(source["cases"]) == 126, "source has exactly 126 cases")
    check(len(source["required_witnesses"]) == 21, "source has 21 witnesses")

    # Division is checked by solving d*x=n over every residue, not by the
    # producer's modular-inverse implementation.
    def divide(numerator, denominator):
        solutions = [x for x in range(1, q)
                     if (denominator * x - numerator) % q == 0]
        if len(solutions) != 1:
            raise ArithmeticError("nonunique nonzero quotient")
        return solutions[0]

    all_cases = []
    size_table = []
    required_checks = []
    failed_probe_checks = []
    probe_failures = []
    expected_witnesses = []
    for pair_index, (a, b) in enumerate(pairs):
        sizes = {}
        for omitted in [None] + [r for r in directions if r not in (a, b)]:
            remaining = [r for r in directions if r not in (a, b, omitted)]
            kappas = {r: divide(r - a, r - b) for r in remaining}
            anchor = remaining[0]
            gammas = [divide(kappas[r], kappas[anchor]) for r in remaining[1:]]
            step = q - 1
            for gamma in gammas:
                step = gcd(step, logs[gamma])
            subgroup = sorted(powers[j] for j in range(0, q - 1, step))
            # Multiplicative cosets are exactly exponent residue classes.
            cosets = [sorted(powers[j] for j in range(c, q - 1, step))
                      for c in range(step)]
            cosets.sort(key=lambda coset: coset[0])
            check(sorted(itertools.chain.from_iterable(cosets)) == list(range(1, q)),
                  f"coset partition {a},{b}/{omitted}")
            passed = len(subgroup) >= 68 and len(cosets) <= 2
            expected_case = {
                "pair": [a, b], "omitted": omitted, "remaining": remaining,
                "kappas": {str(r): k for r, k in kappas.items()},
                "anchor": anchor, "generators": gammas,
                "subgroup": subgroup, "cosets": cosets,
                "closure_ok": True, "inverse_ok": True,
                "subgroup_size": len(subgroup), "orbit_count": len(cosets),
                "passed": passed,
            }
            case_index = len(all_cases)
            matched = (case_index < len(source["cases"])
                       and source["cases"][case_index] == expected_case)
            check(matched, f"complete saved case {case_index}: {a},{b}/{omitted}")
            all_cases.append({"source_case_index": case_index, "log_step": step,
                              "matches_source": matched, "recomputed": expected_case})
            sizes["none" if omitted is None else str(omitted)] = len(subgroup)
            if not passed:
                probe_failures.append({"pair": [a, b], "omitted": omitted})
                failed_probe_checks.append(all_cases[-1])
            if omitted is None:
                check(pair_index < len(printed_rows), f"printed row {pair_index}")
                if pair_index >= len(printed_rows):
                    continue
                printed_pair, printed_gammas, exponents = printed_rows[pair_index]
                valid_exponents = (len(exponents) == 4
                                   and all(isinstance(e, int) and e >= 0 for e in exponents))
                check(valid_exponents, f"nonnegative exponent vector {a},{b}")
                factors = [pow(gamma, e, q) for gamma, e in zip(gammas, exponents)]
                product = 1
                for factor in factors:
                    product = product * factor % q
                identity_ok = (printed_pair == [a, b] and printed_gammas == gammas
                               and valid_exponents and product == 2 and passed)
                check(identity_ok, f"canonical witness {a},{b}")
                expected_witnesses.append({
                    "pair": [a, b], "remaining": remaining, "anchor": anchor,
                    "generators": gammas, "exponents": exponents,
                    "product": product, "passed": identity_ok,
                })
                required_checks.append({
                    "pair": [a, b], "generators": gammas, "exponents": exponents,
                    "factors": factors, "product": product, "subgroup_size": len(subgroup),
                    "orbit_count": len(cosets), "passed": identity_ok and matched,
                })
        size_table.append({"pair": [a, b], "sizes_by_omission": sizes})

    check(source["required_witnesses"] == expected_witnesses, "all saved witness fields")
    check(source["size_table"] == size_table, "entire saved size table")
    check(probe_failures == [{"pair": [64, 70], "omitted": 102},
                             {"pair": [70, 118], "omitted": 16}],
          "exactly the two recorded failed omission probes")
    expected_probe = {
        "case_count": 126, "required_case_count": 126,
        "minimum_subgroup_size": min(c["recomputed"]["subgroup_size"] for c in all_cases),
        "required_minimum_subgroup_size": 68,
        "maximum_orbit_count": max(c["recomputed"]["orbit_count"] for c in all_cases),
        "required_maximum_orbit_count": 2,
        "failures": probe_failures, "all_passed": False,
    }
    expected_summary = {
        "case_count": 21, "required_case_count": 21,
        "minimum_subgroup_size": min(c["subgroup_size"] for c in required_checks),
        "required_minimum_subgroup_size": 68,
        "maximum_orbit_count": max(c["orbit_count"] for c in required_checks),
        "required_maximum_orbit_count": 2, "witness_element": 2, "witness_order": order_two,
        "order_checks": order_checks, "failures": [], "canonical_table_rows": 21,
        "canonical_table_matches": True, "all_passed": True,
    }
    check(source["arbitrary_omission_probe"] == expected_probe, "complete probe summary")
    check(source["summary"] == expected_summary, "complete required summary")
    check(set(source) == {"q", "T", "summary", "required_witnesses",
                          "arbitrary_omission_probe", "size_table", "cases"},
          "complete certificate top-level scope")
    summary = {
        "all_passed": not failures, "failures": failures,
        "required_pairs_checked": len(required_checks), "required_pairs": 21,
        "saved_cases_checked": len(all_cases), "required_saved_cases": 126,
        "minimum_required_subgroup_size": expected_summary["minimum_subgroup_size"],
        "required_minimum_subgroup_size": 68,
        "maximum_required_orbit_count": expected_summary["maximum_orbit_count"],
        "required_maximum_orbit_count": 2, "order_of_2": order_two,
        "stronger_probe_failures_preserved": probe_failures,
    }
    artifacts = [source_path, generator_path, lemma_path, Path(__file__)]
    certificate = {
        "summary": summary, "q": q, "T": directions,
        "method": "Full multiplicative power table and discrete-log gcd; exhaustive quotient solving",
        "primitive_element": primitive, "primitive_power_table": powers,
        "order_checks": order_checks, "required_checks": required_checks,
        "failed_probe_checks": failed_probe_checks, "all_cases": all_cases,
        "size_table": size_table,
        "input_sha256": {str(path.relative_to(notebook)):
                         hashlib.sha256(path.read_bytes()).hexdigest() for path in artifacts},
    }
    output_path.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"Required pairs: {len(required_checks)}/21; complete saved cases: {len(all_cases)}/126")
    print(f"Subgroup minimum: {summary['minimum_required_subgroup_size']} (required >=68); "
          f"orbit maximum: {summary['maximum_required_orbit_count']} (required <=2); ord(2)={order_two}")
    print("Stronger omission failures retained: (64,70)/102 size 34; (70,118)/16 size 17")
    print(f"Audit failures: {failures}; all_passed={not failures}")
    print(f"Full certificate: {output_path.relative_to(notebook)}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
