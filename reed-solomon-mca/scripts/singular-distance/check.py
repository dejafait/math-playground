"""Auxiliary support-event checks for L012 over F_97, not all input pairs."""

import importlib.util
import sys
from math import comb
from pathlib import Path

sys.dont_write_bytecode = True
SOURCE = Path(__file__).resolve().parents[1] / "persistent-root" / "check.py"
SPEC = importlib.util.spec_from_file_location("support_check", SOURCE)
SUPPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUPPORT)
BASE = SUPPORT.BASE
P, H = BASE.P, BASE.H


def check_case(name, a, b, full_constraints, reduced_constraints,
               expected_bad, expected_close, expected_weight=None,
               nonzero_locator=False):
    determinant, _, locators = BASE.locator(a, b)
    assert determinant == (0,), name
    if nonzero_locator:
        assert any(polynomial != (0,) for polynomial in locators.values()), name

    # Both events are tested by interpolation on their own allowed supports.
    # Neither membership computation uses the Hankel determinant or a decoder.
    full_bad, full_weights = SUPPORT.event(a, b, full_constraints)
    reduced_bad, reduced_weights = SUPPORT.event(a, b, reduced_constraints)
    assert full_bad == reduced_bad == expected_bad, (name, full_bad, reduced_bad)
    assert full_weights == reduced_weights, (name, full_weights, reduced_weights)
    assert set(full_weights) == expected_close, (name, full_weights)
    assert all(weight <= 3 for weight in full_weights.values()), name
    assert full_bad <= set(full_weights) and len(full_bad) <= 5, name
    if expected_weight is not None:
        parameter, weight = expected_weight
        assert full_weights[parameter] == weight, name
    print(
        f"PASS: {name}: D(T)=0; bad(4)=bad(3)={sorted(full_bad)}; "
        f"close count={len(full_weights)}; weights={sorted(set(full_weights.values()))}."
    )


def main():
    full_constraints = SUPPORT.constraints(H, 4)
    reduced_constraints = [row for row in full_constraints if len(row[2]) >= 13]
    assert len(full_constraints) == sum(comb(16, i) for i in range(5)) == 2517
    assert len(reduced_constraints) == sum(comb(16, i) for i in range(4)) == 697
    zero = (0,) * 16
    all_parameters = set(range(P))
    code_a = tuple(BASE.evaluate((3, 1, 4, 1, 5, 9, 2, 6), x) for x in H)
    code_b = tuple(BASE.evaluate((2, 7, 1, 8, 2, 8, 1), x) for x in H)

    check_case("both inputs in the code", code_a, code_b,
               full_constraints, reduced_constraints, set(), all_parameters,
               expected_weight=(0, 0))
    fixed_a = (1, 1, 1) + (0,) * 13
    fixed_b = (1, 2, 3) + (0,) * 13
    roots = {-pow(i, -1, P) % P for i in range(1, 4)}
    check_case("fixed three-coordinate family", fixed_a, fixed_b,
               full_constraints, reduced_constraints, roots, all_parameters,
               expected_weight=(0, 3))
    check_case("zero direction with a sparse input", fixed_a, zero,
               full_constraints, reduced_constraints, set(), all_parameters,
               expected_weight=(0, 3))

    y, z = H[:2]
    derivative = BASE.word_with_syndrome(tuple(
        j * pow(z, j - 1, P) % P for j in range(1, 9)
    ))
    for weight in (0, 1, 2):
        a = tuple(int(x in (y, z)[:weight]) for x in H)
        check_case(f"confluent pencil, weight {weight} at zero", a, derivative,
                   full_constraints, reduced_constraints, {0}, {0},
                   expected_weight=(0, weight))

    shift = 41
    shifted_a = tuple(
        (int(x == y) - shift * value + code) % P
        for x, value, code in zip(H, derivative, code_a)
    )
    shifted_b = tuple((value + code) % P for value, code in zip(derivative, code_b))
    check_case("translated and shifted confluent pencil", shifted_a, shifted_b,
               full_constraints, reduced_constraints, {shift}, {shift},
               expected_weight=(shift, 1))

    # A singular leading Hankel block need not make the whole 4-by-5 matrix
    # rank deficient or supply a sparse representative. Perturb only s_8.
    # This tests that the proof uses singularity only after agreement is witnessed.
    moments = BASE.syndrome(fixed_a)
    perturbed = moments[:-1] + ((moments[-1] + 1) % P,)
    dense_a = BASE.word_with_syndrome(perturbed)
    check_case("singular determinant with nonzero locators and no close values",
               dense_a, fixed_a, full_constraints, reduced_constraints,
               set(), set(), nonzero_locator=True)

    assert 5 * 2**128 <= 15 * 2**128 <= 97**20 < 16 * 2**128
    print("PASS: count five meets the allowance fifteen; the global count sixteen leaves safety undecided.")
    print("Checked 2517 original and 697 reduced supports per pair over F_97.")
    print("These examples do not enumerate all pairs or F_(97^20); the upper bound uses L007 and a proof.")


if __name__ == "__main__":
    main()
