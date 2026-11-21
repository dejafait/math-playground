"""One exact Lagrange-inverse enclosure on the approved frozen box."""
from fractions import Fraction as Q
import json
from pathlib import Path


def pack(q):
    q = Q(q)
    return {"numerator": q.numerator, "denominator": q.denominator}


def main():
    boxes = [(Q(14), Q(29, 2)), (Q(41, 2), Q(43, 2)),
             (Q(49, 2), Q(51, 2))]
    y = [(Q(200) / b**2, Q(200) / a**2) for a, b in boxes]
    gaps = {(j, k): y[j][0] - y[k][1]
            for j in range(3) for k in range(j + 1, 3)}
    failures = []
    if not all(a > 0 and b >= a for a, b in y):
        failures.append("transformed intervals not positive and ordered")
    if not all(g > 0 for g in gaps.values()):
        failures.append("nonpositive separation denominator")
    assert not failures, failures
    rows = []
    bound = Q(0)
    for j in range(3):
        k, ell = [i for i in range(3) if i != j]
        gap_factors = [gaps[tuple(sorted((j, i)))] for i in (k, ell)]
        denominator = y[j][0] * gap_factors[0] * gap_factors[1]
        numerators = [Q(200) * y[k][1] * y[ell][1],
                      Q(200) * (y[k][1] + y[ell][1]), Q(200)]
        entries = [v / denominator for v in numerators]
        row_square = sum((v*v for v in entries), Q(0))
        bound += row_square
        rows.append({"node": j + 1, "other_nodes": [k + 1, ell + 1],
                     "y_lower": pack(y[j][0]),
                     "gap_lower_factors": [pack(g) for g in gap_factors],
                     "denominator_lower": pack(denominator),
                     "absolute_numerator_uppers": [pack(v) for v in numerators],
                     "inverse_entry_absolute_uppers": [pack(v) for v in entries],
                     "inverse_entry_signed_enclosures": [
                         [pack(-v), pack(0)] if (j == 1) != (i == 1)
                         else [pack(0), pack(v)]
                         for i, v in enumerate(entries)],
                     "row_square_upper": pack(row_square)})
        # Signs: denominators +,-,+; numerators +,-,+.
    required_inverse_square = Q(2000000000)
    threshold = 1 / required_inverse_square
    lower = 1 / bound
    passed = lower > threshold
    if not passed:
        failures.append("single enclosure does not exceed required threshold")
    # An additional simple rational presentation is checked, not tuned.
    display_cap = Q(700000000)
    certificate = {
        "step": 2162, "method": "single exact inverse-entry Frobenius enclosure",
        "hypothetical_nodes_only": True, "subdivisions": 0,
        "x_boxes": [[pack(a), pack(b)] for a, b in boxes],
        "y_boxes": [[pack(a), pack(b)] for a, b in y],
        "positive_gap_lowers": {f"{j+1}-{k+1}": pack(g) for (j,k),g in gaps.items()},
        "inverse_rows": rows, "inverse_frobenius_square_upper": pack(bound),
        "eigenvalue_lower": pack(lower), "required_eigenvalue_threshold": pack(threshold),
        "required_inverse_square_strict_upper": pack(required_inverse_square),
        "strict_comparison_difference": pack(lower-threshold),
        "strict_cross_product_reserve": required_inverse_square.numerator * bound.denominator - bound.numerator,
        "display_cap": pack(display_cap), "bound_below_display_cap": bound < display_cap,
        "display_cap_cross_product_reserve": display_cap.numerator * bound.denominator - bound.numerator,
        "passed": passed, "failures": failures,
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"result={'PASS' if passed else 'INCONCLUSIVE'}; inverse square upper={bound}")
    print(f"eigenvalue lower={lower} ({float(lower):.12g}); required > {threshold}")
    print(f"bound < 700000000: {bound < display_cap}; failures={failures}")
    print(f"certificate={output.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
