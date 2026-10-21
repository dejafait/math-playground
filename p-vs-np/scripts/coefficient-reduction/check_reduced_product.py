"""Exact free-word diagnostics for L024; no quotient simplification."""
import json
from pathlib import Path

from check_correction_update import add, degree, mul, subst, var


ONE = {()}
ZERO = set()


def formulas(a, b, z, w, ba, bb, kba, kaw, kbw, h):
    product = mul(a, b)
    m = add(mul(mul(a, kba), b), mul(ba, mul(b, b)), mul(a, bb))
    return {
        "product_boolean": m,
        "reduced_boolean": add(m, mul(h, z), mul(product, h), h),
        "reduced_commutator": add(mul(a, kbw), mul(kaw, b),
                                  mul(h, w), mul(w, h)),
        "definition_1": add(mul(ba, b), mul(a, kba), mul(h, add(ONE, a))),
        "definition_2": add(mul(a, bb), mul(h, add(ONE, b))),
        "definition_3": add(m, mul(h, product)),
    }


def targets(a, b, z, w):
    product = mul(a, b)
    return {
        "product_boolean": add(mul(product, product), product),
        "reduced_boolean": add(mul(z, z), z),
        "reduced_commutator": add(mul(z, w), mul(w, z)),
        "definition_1": mul(z, add(ONE, a)),
        "definition_2": mul(z, add(ONE, b)),
        "definition_3": mul(add(ONE, z), product),
    }


def main():
    a, b, z, w, ba, bb, kba, kaw, kbw, h, q = map(
        var, "a b z w ba bb kba kaw kbw h q".split()
    )
    f = formulas(a, b, z, w, ba, bb, kba, kaw, kbw, h)
    values = {
        "ba": add(mul(a, a), a), "bb": add(mul(b, b), b),
        "kba": add(mul(b, a), mul(a, b)),
        "kaw": add(mul(a, w), mul(w, a)),
        "kbw": add(mul(b, w), mul(w, b)),
        "h": add(z, mul(a, b)),
    }
    expected = targets(a, b, z, w)
    zero_witnesses = {name: ZERO for name in values}
    for name, polynomial in f.items():
        assert subst(polynomial, values) == expected[name], name
        assert subst(polynomial, zero_witnesses) == ZERO, name

    # Context transport is tested with a completely arbitrary supplied root q.
    for replacement, old in [
        (add(mul(z, q), mul(h, q)), mul(mul(a, b), q)),
        (add(mul(q, z), mul(q, h)), mul(q, mul(a, b))),
    ]:
        assert subst(replacement, values) == old
        assert subst(replacement, {"h": ZERO, "q": ZERO}) == ZERO

    mutations = {
        "omitted local-relation term in definition 1":
            ("definition_1", add(f["definition_1"], mul(h, add(ONE, a)))),
        "reversed relation factor in definition 3":
            ("definition_3", add(f["definition_3"], mul(h, mul(a, b)),
                                 mul(mul(a, b), h))),
        "omitted product commutator in Boolean witness":
            ("reduced_boolean", add(f["reduced_boolean"], mul(mul(a, kba), b))),
        "omitted H z in reduced Boolean witness":
            ("reduced_boolean", add(f["reduced_boolean"], mul(h, z))),
        "omitted w H in reduced commutator":
            ("reduced_commutator", add(f["reduced_commutator"], mul(w, h))),
    }
    for name, (target_name, corrupted) in mutations.items():
        assert subst(corrupted, values) != expected[target_name], name

    x, y, bx, by, c = map(var, "x y bx by c".split())
    original_axioms = {"bx": add(mul(x, x), x),
                       "by": add(mul(y, y), y),
                       "c": add(mul(x, y), mul(y, x))}
    cases = [
        (x, x, x, y, bx, bx, ZERO, c, c, bx),
        (x, add(ONE, x), ZERO, y, bx, bx, ZERO, c, c, bx),
        (x, y, mul(y, x), y, bx, by, c, c, ZERO, c),
    ]
    for operands in cases:
        concrete = formulas(*operands)
        concrete_targets = targets(*operands[:4])
        for name, polynomial in concrete.items():
            assert subst(polynomial, original_axioms) == concrete_targets[name]
            assert subst(polynomial, {"bx": ZERO, "by": ZERO, "c": ZERO}) == ZERO

    boolean_witness = bx
    rows = []
    for k in range(9):
        assert subst(boolean_witness, original_axioms) == original_axioms["bx"]
        assert subst(boolean_witness, {"bx": ZERO}) == ZERO
        assert degree(boolean_witness) == 2 * k + 1
        rows.append({"updates": k, "reduced_value_degree": 1,
                     "local_relation_degree": 1,
                     "boolean_witness_degree": degree(boolean_witness),
                     "all_local_outputs_degree_upper_bound": 2 * k + 3,
                     "boolean_witness_words": [list(t) for t in sorted(boolean_witness)]})
        next_outputs = formulas(x, x, x, x, boolean_witness,
                                boolean_witness, ZERO, ZERO, ZERO, bx)
        for name, polynomial in next_outputs.items():
            assert subst(polynomial, original_axioms) == targets(x, x, x, x)[name]
            assert degree(polynomial) <= 2 * k + 3
        boolean_witness = next_outputs["reduced_boolean"]

    result = {
        "scope": "Universal ordered identities, concrete original-axiom witnesses, and k<=8 expansions; asymptotic proof is L024.",
        "universal_outputs_checked": len(f), "transport_orientations_checked": 2,
        "concrete_gate_cases_checked": len(cases),
        "deliberate_errors_detected": list(mutations), "failed_checks": [],
        "actual_bound": "At most 40 new shared gates for six local outputs; degree <= h+2d. Repeated-square Boolean witness degree 2k+1.",
        "required_bound": "Full original-axiom certificate size AND formal degree T^{O(1)}; the local conditional bound passes, global propagation and input existence are unproved.",
        "repeated_square_cases": rows,
    }
    output = Path(__file__).with_name("reduced-product-results.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: six universal outputs, two transport orientations, three concrete gates, five corruptions, k=0..8.")
    print("Actual: local degree <= h+2d, <=40 new shared gates; repeated-square witness degree 2k+1.")
    print("Required: complete certificate size and degree polynomial in T; global propagation and existence remain open.")
    print("Failed checks: none. Artifact: scripts/coefficient-reduction/reduced-product-results.json")


if __name__ == "__main__":
    main()
