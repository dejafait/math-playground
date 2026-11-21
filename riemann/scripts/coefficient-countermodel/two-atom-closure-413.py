"""Replay the full screen with integer arithmetic and test the one survivor."""

import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)


def decode(x):
    return F(int(x["numerator"]), int(x["denominator"]))


def encode(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def step(a):
    return [a[n] * a[n] - (a[n - 1] * a[n + 1] if n else 0)
            for n in range(len(a) - 1)]


def main():
    source = Path(__file__).with_name("two-atom-grid-413.json")
    raw = source.read_bytes()
    grid = json.loads(raw)
    failures, negative_cases, replay = [], [], []
    expected_parameters = [(p, j) for p in range(1, 16) for j in range(-8, 9)]
    assert [(c["p"], c["j"]) for c in grid["cases"]] == expected_parameters
    for c in grid["cases"]:
        p, j = c["p"], c["j"]
        b = [(1 + F(2) ** j * F(p, 16) ** n) / math.factorial(2 * n) for n in range(13)]
        assert b == [decode(x) for x in c["initial_entries_0_through_12"]]
        scale = math.lcm(*(x.denominator for x in b))
        initial = [int(x * scale) for x in b]
        determinant_integer = 0
        for permutation in itertools.permutations(range(5)):
            inversions = sum(permutation[i] > permutation[k] for i in range(5) for k in range(i + 1, 5))
            term = math.prod(initial[4 + permutation[i] - i] for i in range(5))
            determinant_integer += -term if inversions % 2 else term
        det = F(determinant_integer, scale ** 5)
        assert det == decode(c["determinant"]) == decode(c["permutation_determinant"])
        replay.append({"p": p, "j": j, "scale": str(scale),
                       "scaled_integer_determinant": str(determinant_integer),
                       "sign": (det > 0) - (det < 0)})
        if det >= 0:
            assert c["screen"] is None
            continue
        layers = [initial]
        recorded_failures = []
        for depth in range(1, 5):
            layers.append(step(layers[-1]))
            recorded = c["screen"]["layers"][depth - 1]
            assert recorded["depth"] == depth and recorded["last_index"] == 12 - depth
            a = [F(x, scale ** (2 ** depth)) for x in layers[-1]]
            assert a == [decode(x) for x in recorded["entries"]]
            recorded_failures.extend({"depth": depth, "index": n, "value": encode(a[n])}
                                     for n in range(9) if a[n] <= 0)
        assert recorded_failures == c["screen"]["nonpositive_target_entries"]
        assert c["screen"]["passes"] == (not recorded_failures)
        selected = p == 7 and j == 4
        if selected:
            assert grid["selected"]["p"] == p and grid["selected"]["j"] == j
            layers.append(step(layers[-1]))
            depth = 5
        else:
            assert (p, j) == (6, 4)
            depth = 4
        previous = layers[depth - 1]
        ratio = F(previous[3] * previous[5], previous[4] ** 2)
        value = F(layers[depth][4], scale ** (2 ** depth))
        lower, upper = (10, 11) if selected else (3, 4)
        if not (all(x > 0 for x in previous[3:6]) and lower < ratio < upper and value < 0):
            failures.append({"p": p, "j": j, "reason": "claimed failure bounds do not hold",
                             "ratio": encode(ratio)})
        negative_cases.append({"p": p, "j": j, "determinant": encode(det),
            "scale": str(scale), "integer_layers": [[str(x) for x in a] for a in layers],
            "failed_depth": depth, "failed_index": 4,
            "previous_three_entries_positive": all(x > 0 for x in previous[3:6]),
            "previous_ratio": encode(ratio), "ratio_lower_bound": lower, "ratio_upper_bound": upper,
            "ratio_lower_margin_integer": str(previous[3]*previous[5] - lower*previous[4]**2),
            "ratio_upper_margin_integer": str(upper*previous[4]**2 - previous[3]*previous[5]),
            "failed_iterate": encode(value)})
    counts = {"grid_points_replayed": len(replay), "positive_determinants": sum(x["sign"] > 0 for x in replay),
              "negative_determinants": len(negative_cases), "zero_determinants": sum(x["sign"] == 0 for x in replay),
              "negative_cases_with_failed_turan_iterate": sum(decode(x["failed_iterate"]) < 0 for x in negative_cases)}
    assert counts == {"grid_points_replayed": 255, "positive_determinants": 253,
                      "negative_determinants": 2, "zero_determinants": 0,
                      "negative_cases_with_failed_turan_iterate": 2}
    report = {"source": str(source), "source_sha256": hashlib.sha256(raw).hexdigest(),
              "arithmetic": "exact integers after common-denominator scaling; all stored rational entries replayed",
              "scale_identity": "integer_layer[d][n] = scale^(2^d) * L^d(b)[n]",
              "scope": "one approved grid and its unique survivor only; no tail or all-order claim",
              "counts": counts, "failures": failures, "determinant_replay": replay,
              "negative_cases": negative_cases,
              "conclusion": "No grid point has both D_(5,4)<0 and strict positivity of all Turan iterates."}
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"counts": counts, "failures": failures,
        "failed_cases": [{"p": x["p"], "j": x["j"], "depth": x["failed_depth"], "index": 4,
                          "ratio_bounds": [x["ratio_lower_bound"], x["ratio_upper_bound"]],
                          "required_for_next_strict_positivity": "ratio < 1"} for x in negative_cases],
        "certificate": str(output)}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
