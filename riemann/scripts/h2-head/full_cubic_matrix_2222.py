"""One frozen weighted four-node inverse enclosure; exact Fraction evidence."""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
import platform


def pack(q):
    q = F(q)
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def display(q):
    with localcontext() as ctx:
        ctx.prec = 18
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def product(values):
    answer = F(1)
    for value in values:
        answer *= value
    return answer


def main():
    boxes = [(F(14), F(29, 2)), (F(41, 2), F(43, 2)),
             (F(49, 2), F(51, 2)), (F(100), F(200))]
    scale, onset, cutoff = 200, 4, 1000
    y = [(F(scale) / hi**2, F(scale) / lo**2) for lo, hi in boxes]
    gaps = {(j, k): y[j][0] - y[k][1]
            for j in range(4) for k in range(j + 1, 4)}
    assert all(0 < lo <= hi for lo, hi in y)
    assert all(gap > 0 for gap in gaps.values())
    rows = []
    B = F(0)
    for j in range(4):
        others = [i for i in range(4) if i != j]
        gap_factors = [gaps[tuple(sorted((j, i)))] for i in others]
        # U=V(y) diag((y/200)^5), not the unweighted W.
        denominator = y[j][0]**5 * product(gap_factors)
        numerators = [F(scale**5) * sum(
            (product(y[i][1] for i in subset)
             for subset in combinations(others, 3 - degree)), F(0))
            for degree in range(4)]
        bounds = [v / denominator for v in numerators]
        row_square = sum((v*v for v in bounds), F(0))
        B += row_square
        # Denominator sign (-1)^j; numerator sign (-1)^(3-degree).
        signs = [(-1)**(j + 3 - degree) for degree in range(4)]
        rows.append({
            "node": j + 1, "other_nodes": [i + 1 for i in others],
            "y_lower_fifth": pack(y[j][0]**5),
            "gap_lower_factors": [pack(v) for v in gap_factors],
            "denominator_lower": pack(denominator),
            "numerator_absolute_uppers": [pack(v) for v in numerators],
            "inverse_entry_absolute_uppers": [pack(v) for v in bounds],
            "inverse_entry_signed_enclosures": [
                [pack(0), pack(v)] if s > 0 else [pack(-v), pack(0)]
                for s, v in zip(signs, bounds)],
            "row_square_upper": pack(row_square)})
    head = 1 / B
    components = [F(scale**(2*i), cutoff**(4*i)) for i in range(4)]
    C = sum(components, F(0))
    first = F(1, cutoff**19)
    integral = F(1, 18 * cutoff**18)
    tail = 18 * C * (first + integral)
    head_step, tail_step = F(1, 200**4), F(1, cutoff**4)
    ratio_step = tail_step / head_step
    checks = {
        "frozen_parameters": (scale, onset, cutoff) == (200, 4, 1000),
        "all_four_intervals_positive": all(0 < lo <= hi for lo, hi in y),
        "all_six_gaps_positive": len(gaps) == 6 and all(v > 0 for v in gaps.values()),
        "all_sixteen_inverse_bounds_positive": all(
            int(v["numerator"]) > 0 for row in rows for v in row["inverse_entry_absolute_uppers"]),
        "head_and_tail_positive": head > 0 and tail > 0,
        "strict_onset_margin": head > tail,
        "all_r_relative_step": ratio_step == F(1, 625) and 0 < ratio_step < 1,
    }
    failures = [name for name, ok in checks.items() if not ok]
    certificate = {
        "target": "H_(3,r)>0 for every integer r>=4",
        "assessment": "drafts/literature/2026-11-21-full-cubic-matrix-test-2221.md",
        "parameters": {"scale": scale, "onset": onset, "cutoff": cutoff,
                       "D": [scale**i for i in range(4)], "subdivisions": 0},
        "arithmetic": {"python": platform.python_version(),
                       "proof": "CPython int/Fraction; Decimal explanatory display only"},
        "inputs": ["L018", "L024", "L025", "L030", "L058", "L467", "C919f", "C919k",
                   "Gautschi1975 Section3/4", "Boyd-Vandenberghe2004 AppendixA", "Platt2017 Theorem5.1"],
        "box_evidence": {"x": [[pack(a), pack(b)] for a, b in boxes],
                         "y": [[pack(a), pack(b)] for a, b in y],
                         "gaps": {f"{j+1}-{k+1}": pack(g) for (j, k), g in gaps.items()}},
        "inverse_rows": rows,
        "comparison": {"B": pack(B), "head_lower_r4": pack(head),
                       "tail_components": [pack(v) for v in components],
                       "tail_vector_factor": pack(C), "first_shell": pack(first),
                       "integral": pack(integral), "tail_upper_r4": pack(tail),
                       "required_head_minus_tail": pack(0), "actual_head_minus_tail": pack(head-tail),
                       "head_over_tail": pack(head/tail),
                       "strict_cross_product": str(head.numerator * tail.denominator - tail.numerator * head.denominator)},
        "all_r": {"k": "arbitrary integer r-4>=0", "head_step": pack(head_step),
                  "tail_step": pack(tail_step), "relative_step": pack(ratio_step),
                  "conclusion": "lambda_min(D H_(3,4+k) D)>=head_step^k*(h4-t4)>0, conditional on analytic proof"},
        "checks": checks, "failures": failures,
        "limits": "Exact specialization, not source-computation replay, all-degree positivity or RH."}
    destination = Path(__file__).with_suffix(".json")
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"result={'PASS' if not failures else 'STOP'}; h4={display(head)}; t4={display(tail)}")
    print(f"actual h4-t4={display(head-tail)}; required>0; h4/t4={display(head/tail)}")
    print(f"all-r relative factor={ratio_step}; failures={failures}")
    print(f"certificate={destination.relative_to(Path.cwd())}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
