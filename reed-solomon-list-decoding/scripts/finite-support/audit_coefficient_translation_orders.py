"""Independent integer replay of L138's arithmetic, not a closure test.

Run: python3 scripts/finite-support/audit_coefficient_translation_orders.py
The complete production power arrays are checked by repeated multiplication.
"""

import json
from math import gcd, isqrt
from pathlib import Path


def prime_by_trial_division(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def main():
    here = Path(__file__).resolve().parent
    source = here / "coefficient-translation-orders.json"
    saved = json.loads(source.read_text())
    checks = {}
    failures = []

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)

    check("137_is_prime", prime_by_trial_division(137))
    check("65537_is_prime", prime_by_trial_division(65537))
    check("distinct_characteristics", 65537 % 137 == 51)
    check("label_budget", 7 * 137 + 4 == 1024 - 61 == 963)
    check("source_auxiliary_prime", saved["auxiliary_prime"] == 137)
    check("source_characteristic", saved["coefficient_characteristic"] == 65537)
    check("two_cases_only", len(saved["cases"]) == 2)
    check("source_reports_no_failure", saved["failures"] == [])
    check("no_membership_claim", saved["closure_memberships_verified"] == 0)
    check("no_counterassignment_claim", saved["permitted_full_sheet_counterassignments_found"] == 0)
    cases = []
    for index, (name, extension, required) in enumerate((("E", 1, 136), ("F", 28, 34))):
        residue = 1
        for _ in range(extension):
            residue = residue * 65537 % 137
        value = 1
        powers = []
        for _ in range(136):
            value = value * residue % 137
            powers.append(value)
        actual = powers.index(1) + 1
        recorded = saved["cases"][index]
        check(name + "_field", recorded["field"] == name)
        check(name + "_extension", recorded["extension_degree_over_prime_field"] == extension)
        check(name + "_residue", recorded["cardinality_modulo_137"] == residue)
        check(name + "_all_136_powers", recorded["powers_for_exponents_1_through_136"] == powers)
        check(name + "_order", actual == recorded["actual_order"] == recorded["required_order"] == required)
        check(name + "_dimension", recorded["small_space_dimension_upper_bound"] == 4 < actual)
        check(name + "_threshold", recorded["minimum_dimension_if_invariant_containing_one_and_nontrivial"] == actual + 1)
        check(name + "_source_checks", all(recorded["checks"].values()))
        cases.append({"field": name, "extension_degree": extension,
                      "cardinality_residue": residue, "actual_order": actual,
                      "required_order": required, "available_dimension_upper_bound": 4,
                      "required_dimension_for_nontrivial_action_containing_one": actual + 1,
                      "powers_for_exponents_1_through_136": powers})

    short_expected = {2: 135, 8: 16, 28: 81, 68: 136, 136: 1}
    for exponent, expected in short_expected.items():
        check(f"51_power_{exponent}", cases[0]["powers_for_exponents_1_through_136"][exponent - 1] == expected)
    for exponent, expected in {2: 122, 17: 136, 34: 1}.items():
        check(f"81_power_{exponent}", cases[1]["powers_for_exponents_1_through_136"][exponent - 1] == expected)
    check("order_power_formula", 136 // gcd(136, 28) == 34)
    check("auxiliary_2_power_17", pow(2, 17, 137) == 100)
    check("auxiliary_100_square", 100 * 100 % 137 == 136)

    output = here / "l138-critical-audit-arithmetic.json"
    certificate = {"scope": "Complete integer replay only; operator and directional arguments are audited in prose.",
                   "production_certificate": source.name, "cases": cases,
                   "checks": checks, "failures": failures,
                   "closure_inclusion_established": False,
                   "full_sheet_counterassignment_constructed": False}
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    for case in cases:
        print(f"{case['field']}: order {case['actual_order']} / required {case['required_order']}; "
              f"nontrivial action containing 1 requires dimension >= "
              f"{case['required_dimension_for_nontrivial_action_containing_one']}, available <= 4")
    print(f"Checks: {len(checks)}; failures: {len(failures)} {failures}")
    print(f"Certificate: {output}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
