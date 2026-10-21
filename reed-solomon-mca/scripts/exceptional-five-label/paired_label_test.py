"""Exact necessary edge tests for one specified exceptional labeling.

This does not construct a pencil, enumerate arbitrary labelings, or bound N_ext.
Run from the active notebook: python3 scripts/exceptional-five-label/paired_label_test.py
"""

import itertools
import json
from pathlib import Path


def product(values):
    result = 1
    for value in values:
        result = result * value % 97
    return result


def evaluate(roots, value):
    return product(value - root for root in roots)


def evaluate_by_coefficients(roots, value):
    """Independent coefficient expansion followed by Horner evaluation."""
    coefficients = [1]
    for root in roots:
        new = [0] * (len(coefficients) + 1)
        for index, coefficient in enumerate(coefficients):
            new[index] = (new[index] - root * coefficient) % 97
            new[index + 1] = (new[index + 1] + coefficient) % 97
        coefficients = new
    result = 0
    for coefficient in reversed(coefficients):
        result = (result * value + coefficient) % 97
    return result


def main():
    h = sorted({pow(8, index, 97) for index in range(16)})
    x, y, p = 22, 79, 50
    pairs = [[1, 96], [8, 89], [64, 33], [27, 70]]
    v = [y, *pairs[0], *pairs[1]]
    vp = [p, *pairs[2], *pairs[3]]
    e = sorted(set(h) - {x} - set(v) - set(vp))
    assert len(h) == 16 and pow(8, 8, 97) == 96
    assert len({x, *v, *vp, *e}) == 16
    assert len(v) == len(vp) == len(e) == 5
    assert set(v).isdisjoint(vp)
    assert all((a + b) % 97 == 0 for a, b in pairs)
    # Opposite pairs satisfy R*(0,1,0)=0; different products give rank two.
    row_products = [a * b % 97 for a, b in pairs]
    assert len(set(row_products)) > 1
    tests = []
    for u, w in itertools.combinations(e, 2):
        matrix = []
        candidates = []
        for z in v:
            row = []
            qroots = [a for a in v if a != z]
            for zp in vp:
                proots = [b for b in vp if b != zp]
                assert all(evaluate(proots, a) and evaluate(qroots, a)
                           for a in [u, w, x])
                assert all(evaluate(roots, a) == evaluate_by_coefficients(roots, a)
                           for roots in [proots, qroots] for a in [u, w, x])
                delta = (evaluate(proots, u) * evaluate(qroots, w)
                         - evaluate(proots, w) * evaluate(qroots, u)) % 97
                row.append(delta)
                if delta == 0:
                    candidates.append([z, zp])
            matrix.append(row)
        tests.append({"edge": [u, w],
                      "P_values_at_edge": [[evaluate([b for b in vp if b != zp], a)
                                             for a in [u, w]] for zp in vp],
                      "Q_values_at_edge": [[evaluate([b for b in v if b != z], a)
                                             for a in [u, w]] for z in v],
                      "delta_matrix": matrix,
                      "matrix_entry_product": product(itertools.chain.from_iterable(matrix)),
                      "candidate_tag_pairs": candidates,
                      "candidate_count": len(candidates)})
    failures = [item["edge"] for item in tests if not item["candidate_tag_pairs"]]
    result = {
        "scope": "One specified labeling only; necessary tests, no actual pencil or global bound.",
        "modulus": 97, "H": h, "x": x, "y": y, "p": p,
        "involution_pairs": pairs, "involution": "z -> -z",
        "R_rank": 2, "R_row_products": row_products,
        "V_row_tags": v, "Vprime_column_tags": vp, "E": e,
        "delta_convention": "P_zprime(u)*Q_z(w)-P_zprime(w)*Q_z(u)",
        "tests": tests, "required_candidates_per_edge": 1,
        "coefficient_horner_crosscheck": "All root products at both edge labels and x agree.",
        "actual_minimum_candidates": min(item["candidate_count"] for item in tests),
        "failed_edges": failures,
        "labeling_excluded_by_necessary_test": bool(failures),
    }
    destination = Path(__file__).with_name("paired-label-test-result.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Specified labeling passes involution rank test: rank {result['R_rank']} (required 2).")
    print(f"Per-edge candidate counts: {[item['candidate_count'] for item in tests]}")
    print(f"Actual minimum {result['actual_minimum_candidates']}; required >=1.")
    print(f"Failed edges: {failures}; labeling excluded: {bool(failures)}.")
    print(f"Full certificate: {destination}")


if __name__ == "__main__":
    main()
