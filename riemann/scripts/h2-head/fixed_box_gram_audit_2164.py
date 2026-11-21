"""Audit the frozen C919e certificate in q=1/x^2 coordinates.

No import from, or overwrite of, the original calculation.  Exact rational
identities check the arithmetic; the canonical proof justifies full-box use.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import re


def pack(value):
    if isinstance(value, Q):
        return {"numerator": value.numerator, "denominator": value.denominator}
    if isinstance(value, list):
        return [pack(v) for v in value]
    if isinstance(value, dict):
        return {k: pack(v) for k, v in value.items()}
    return value


def main():
    root = Path(__file__).resolve().parents[2]
    saved_path = root / "scripts/h2-head/fixed_box_gram_2162.json"
    proof_path = root / "lemmas/C919e-fixed-box-three-node-gram-margin.md"
    saved_bytes = saved_path.read_bytes()
    saved = json.loads(saved_bytes)
    proof = proof_path.read_text()
    failures = []
    checked = []

    def check(name, condition):
        checked.append({"check": name, "passed": bool(condition)})
        if not condition:
            failures.append(name)

    def equal(name, expected, actual):
        check(name, pack(expected) == actual)

    boxes = [[Q(14), Q(29, 2)], [Q(41, 2), Q(43, 2)],
             [Q(49, 2), Q(51, 2)]]
    q = [[1 / (hi * hi), 1 / (lo * lo)] for lo, hi in boxes]
    y = [[200 * lo, 200 * hi] for lo, hi in q]
    # Scaling in the original coordinates: W=diag(1,200,40000)*V(q)*diag(q).
    scales = [Q(1), Q(200), Q(40000)]
    gaps = {(i, j): q[i][0] - q[j][1]
            for i, j in [(0, 1), (0, 2), (1, 2)]}
    check("all q intervals positive and internally ordered",
          all(0 < lo <= hi for lo, hi in q))
    check("all three entire-box separations positive", all(g > 0 for g in gaps.values()))
    equal("x endpoints", boxes, saved["x_boxes"])
    equal("transformed y endpoints", y, saved["y_boxes"])
    equal("three y separation values",
          {f"{i+1}-{j+1}": 200*g for (i,j), g in gaps.items()},
          saved["positive_gap_lowers"])

    rows = []
    manuscript_fractions = [v for interval in y for v in interval]
    manuscript_fractions += [200*g for g in gaps.values()]
    for j in range(3):
        others = [i for i in range(3) if i != j]
        k, ell = others
        gap_q = [gaps[tuple(sorted((j, i)))] for i in others]
        d_q = q[j][0] * gap_q[0] * gap_q[1]
        # Coefficients of (u-q_k)(u-q_ell), then the right row scaling D^-1.
        numerator_q = [q[k][1]*q[ell][1], q[k][1]+q[ell][1], Q(1)]
        upper = [numerator_q[c] / (d_q*scales[c]) for c in range(3)]
        denominator_sign = 1 if j in (0, 2) else -1
        signs = [denominator_sign, -denominator_sign, denominator_sign]
        signed = [[Q(0), v] if s == 1 else [-v, Q(0)]
                  for s, v in zip(signs, upper)]
        square = sum((v*v for v in upper), Q(0))
        # Convert the independently computed q operands to the saved y convention.
        row = {
            "node": j+1, "other_nodes": [i+1 for i in others],
            "y_lower": 200*q[j][0],
            "gap_lower_factors": [200*g for g in gap_q],
            "denominator_lower": 200**3*d_q,
            "absolute_numerator_uppers": [200**3*numerator_q[c]/scales[c]
                                          for c in range(3)],
            "inverse_entry_absolute_uppers": upper,
            "inverse_entry_signed_enclosures": signed,
            "row_square_upper": square,
        }
        equal(f"row {j+1}: all fields, three magnitudes and signed enclosures",
              row, saved["inverse_rows"][j])
        check(f"row {j+1}: positive denominator", d_q > 0)
        rows.append(row)
        manuscript_fractions += [row["denominator_lower"], *upper, square]

    equal("complete inverse-row list including node count", rows, saved["inverse_rows"])
    equal("saved method label", "single exact inverse-entry Frobenius enclosure", saved["method"])

    bound = sum((row["row_square_upper"] for row in rows), Q(0))
    lower = 1 / bound
    threshold = Q(1, 2000000000)
    cap = Q(700000000)
    reserve = 2000000000*bound.denominator - bound.numerator
    cap_reserve = 700000000*bound.denominator - bound.numerator
    expected_scalars = {
        "inverse_frobenius_square_upper": bound,
        "eigenvalue_lower": lower,
        "required_eigenvalue_threshold": threshold,
        "required_inverse_square_strict_upper": 1/threshold,
        "strict_comparison_difference": lower-threshold,
        "strict_cross_product_reserve": reserve,
        "display_cap": cap,
        "bound_below_display_cap": bound < cap,
        "display_cap_cross_product_reserve": cap_reserve,
        "passed": lower > threshold,
        "failures": [],
    }
    for name, expected in expected_scalars.items():
        equal(name, expected, saved[name])
    check("strict reciprocal chain", 0 < bound < cap < 1/threshold)
    check("positive exact cross products", reserve > 0 and cap_reserve > 0)
    check("certificate scope flags", saved["hypothetical_nodes_only"] is True
          and saved["subdivisions"] == 0 and saved["step"] == 2162)
    check("saved certificate contains exactly the audited fields",
          set(saved) == {"step", "method", "hypothetical_nodes_only", "subdivisions",
                         "x_boxes", "y_boxes", "positive_gap_lowers", "inverse_rows"}
          | set(expected_scalars))

    manuscript_fractions += [bound]
    for i, value in enumerate(manuscript_fractions):
        pattern = rf"(?<![0-9]){value.numerator}\s*/\s*{value.denominator}(?![0-9])"
        check(f"canonical displayed fraction {i+1}", re.search(pattern, proof) is not None)
    for name, value in [("cap", cap_reserve), ("required", reserve)]:
        check(f"canonical {name} cross product", str(value) in proof)

    output = Path(__file__).with_suffix(".json")
    report = {
        "step": 2164, "method": "independent q=1/x^2 exact operand audit",
        "saved_certificate": str(saved_path.relative_to(root)),
        "saved_certificate_sha256": hashlib.sha256(saved_bytes).hexdigest(),
        "q_intervals": q, "q_gap_lowers": {f"{i+1}-{j+1}": g for (i,j),g in gaps.items()},
        "row_scalings": scales, "reconstructed_y_rows": rows,
        "checked_scalar_values": expected_scalars,
        "checks": checked, "failures": failures,
        "passed": not failures,
        "scope": "hypothetical closed box; no actual placement, sampling or new bound",
    }
    output.write_text(json.dumps(pack(report), indent=2) + "\n")
    print(f"result={'PASS' if not failures else 'FAIL'}; checks={len(checked)}; failures={failures}")
    print(f"actual inverse square upper={bound}; required < 2000000000; stronger < 700000000")
    print(f"actual eigenvalue lower={lower}; required > {threshold}")
    print(f"certificate={output.relative_to(root)}; original preserved")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
