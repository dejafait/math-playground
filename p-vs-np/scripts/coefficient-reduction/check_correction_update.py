"""Exact free-word checks for L023; no Boolean or commutative reduction."""
import json
from pathlib import Path


def var(name):
    return {(name,)}


def add(*polys):
    result = set()
    for poly in polys:
        result.symmetric_difference_update(poly)
    return result


def mul(left, right):
    result = set()
    for a in left:
        for b in right:
            word = a + b
            if word in result:
                result.remove(word)
            else:
                result.add(word)
    return result


def subst(poly, mapping):
    result = set()
    for word in poly:
        term = {()}
        for letter in word:
            term = mul(term, mapping.get(letter, var(letter)))
        result = add(result, term)
    return result


def degree(poly):
    return max(map(len, poly), default=-1)


def main():
    p, q, r, s, u, e, g, h, x, b, t, a = map(
        var, "p q r s u e g h x b t a".split()
    )
    update = add(mul(e, s), mul(r, g), mul(e, g), h)
    values = {"e": add(p, r), "g": add(q, s), "h": add(mul(r, s), u)}
    target = add(mul(p, q), u)
    assert subst(update, values) == target
    assert subst(update, {"e": set(), "g": set(), "h": set()}) == set()
    assert subst(add(update, mul(e, g)), values) != target
    reversed_factor = add(update, mul(r, g), mul(g, r))
    assert subst(reversed_factor, values) != target

    # Abstract a is the original axiom value, independent of e and t.
    transport = [
        (add(mul(r, t), mul(e, a)), mul(p, a)),
        (add(mul(r, t), mul(e, t)), mul(p, a)),
        (add(mul(t, r), mul(a, e)), mul(a, p)),
        (add(mul(t, r), mul(t, e)), mul(a, p)),
    ]
    for replacement, old_value in transport:
        assert subst(replacement, {"t": a, "e": add(p, r)}) == old_value
        assert subst(replacement, {"t": set(), "e": set()}) == set()

    boolean = add(mul(x, x), x)
    correction = b
    rows = []
    for k in range(1, 5):
        expected = {tuple("x" for _ in range(2**k)), ("x",)}
        assert subst(correction, {"b": boolean}) == expected
        assert subst(correction, {"b": set()}) == set()
        assert degree(correction) == 2 ** (k - 1)
        rows.append({
            "k": k,
            "reduced_coefficient_degree": 1,
            "correction_degree": degree(correction),
            "required_exact_lift_degree_lower_bound": 2 ** (k - 1),
            "expanded_words": ["".join(w) for w in sorted(correction)],
        })
        if k < 4:
            correction = add(mul(correction, x), mul(x, correction),
                             mul(correction, correction), b)

    data = {
        "scope": "Exact noncommutative identities and k<=4 word expansions; asymptotic proof is L023.",
        "universal_update": "passed",
        "zero_placeholder_identity": "passed",
        "transport_variants_checked": len(transport),
        "deliberate_errors_detected": ["omitted E G", "reversed r G"],
        "failed_checks": [],
        "actual_bound": "O(k) shared gates; correction degree exactly 2^(k-1)",
        "required_bound": "Both size and correction degree polynomial in supplied input length; degree fails.",
        "repeated_square_cases": rows,
    }
    output = Path(__file__).with_name("correction-results.json")
    output.write_text(json.dumps(data, indent=2) + "\n")
    print("PASS: ordered update, zero identity, four transport variants, two corruptions, k=1..4.")
    print("Actual: O(k) shared gates, exact correction degree 2^(k-1); required: polynomial size AND degree.")
    print("Failed checks: none. Artifact: scripts/coefficient-reduction/correction-results.json")


if __name__ == "__main__":
    main()
