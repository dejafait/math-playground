"""Exact arithmetic for the conditional small-translation-module test.

Run from the active notebook:
    python3 scripts/finite-support/coefficient_translation_orders.py

This checks field orders only. It does not test any message assignment
or prove that the coefficient-function space is translation invariant.
"""

import json
from pathlib import Path


def main():
    auxiliary_prime = 137
    characteristic = 65537
    dimension_bound = 4
    cases = []
    failures = []
    for name, extension_degree, required_order in (("E", 1, 136), ("F", 28, 34)):
        residue = pow(characteristic, extension_degree, auxiliary_prime)
        powers = [pow(residue, exponent, auxiliary_prime)
                  for exponent in range(1, auxiliary_prime)]
        actual_order = next(exponent for exponent, value in enumerate(powers, 1)
                            if value == 1)
        checks = {
            "coprime_characteristics": characteristic % auxiliary_prime != 0,
            "expected_order": actual_order == required_order,
            "order_exceeds_small_space_dimension": actual_order > dimension_bound,
            "all_earlier_powers_nonidentity": all(value != 1 for value in powers[:actual_order - 1]),
        }
        failures.extend(f"{name}:{key}" for key, passed in checks.items() if not passed)
        cases.append({
            "field": name,
            "extension_degree_over_prime_field": extension_degree,
            "cardinality_modulo_137": residue,
            "required_order": required_order,
            "actual_order": actual_order,
            "small_space_dimension_upper_bound": dimension_bound,
            "minimum_dimension_if_invariant_containing_one_and_nontrivial": actual_order + 1,
            "powers_for_exponents_1_through_136": powers,
            "checks": checks,
        })

    certificate = {
        "scope": "Arithmetic for L138's conditional source specialization; no closure or full-sheet assignment is certified.",
        "auxiliary_prime": auxiliary_prime,
        "coefficient_characteristic": characteristic,
        "cases": cases,
        "failures": failures,
        "closure_memberships_verified": 0,
        "closure_memberships_required_by_start_target": 6,
        "permitted_full_sheet_counterassignments_found": 0,
    }
    output = Path(__file__).with_name("coefficient-translation-orders.json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    for case in cases:
        print(f"{case['field']}: order {case['actual_order']} (required {case['required_order']}); "
              f"nontrivial invariant space containing 1 needs dimension >= "
              f"{case['minimum_dimension_if_invariant_containing_one_and_nontrivial']}, "
              f"available <= {dimension_bound}")
    print(f"Arithmetic failures: {len(failures)}; target memberships: 0/6; "
          "full-sheet counterassignments: 0")
    print(f"Certificate: {output}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
