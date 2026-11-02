#!/usr/bin/env python3
"""Replay every stored interval and phase row, without floating point."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def polynomial_value(coefficients, x):
    result = F(0)
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def atan8(z):
    if not 0 <= z <= F(1, 2):
        raise ValueError("reduced atan argument outside [0,1/2]")
    return sum((z ** (2 * k + 1) * F((-1) ** k, 2 * k + 1)
                for k in range(8)), F(0))


def reduced_atan(z):
    if z <= F(1, 2):
        return atan8(z)
    if z <= 1:
        return atan8(F(1, 2)) + atan8((2 * z - 1) / (2 + z))
    return atan8(F(1, 2)) + atan8(F(1, 3)) + atan8((z - 1) / (z + 1))


def main():
    directory = Path(__file__).resolve().parent
    source = directory / "phase-census-endpoint-certificate.json"
    data = json.loads(source.read_text())
    failures, factor_rows, phase_rows = [], [], []

    def check(condition, location):
        if not condition:
            failures.append(location)

    d, U, Y = F(5, 4), F(121, 64), F(27, 100)
    rate, global_min, cells_total, coefficients_total = F(0), None, 0, 0
    check(len(data["factor_checks"]) == 128, "/factor_checks length")
    for index, row in enumerate(data["factor_checks"]):
        t, L = F(row["t"]), F(row["squared_factor_bound"])
        check(t == F(index + 1, 128), f"factor/{index}/t")
        check(1 < L < 2, f"factor/{index}/L")
        p = list(map(F, row["determinant_power_coefficients"]))
        check(len(p) == 5, f"factor/{index}/degree")
        for c in map(F, [-2, -1, 0, 1, 2]):
            N0, D0 = d * d + t * t + 2 * d * t * c, U * U + d * d * t * t + 2 * U * d * t * c
            exact = (L * D0 - t * t * N0) * (L - 1) * D0 * N0 - t * t * (1 - c * c) * (L * D0 - U * N0) ** 2
            check(polynomial_value(p, c) == exact, f"factor/{index}/polynomial/{c}")
        previous = F(-1)
        row_min = None
        for cell_index, cell in enumerate(row["cells"]):
            left, right = F(cell["left"]), F(cell["right"])
            check(left == previous and left < right <= 1, f"factor/{index}/cell/{cell_index}/cover")
            previous = right
            local = [sum((p[j] * comb(j, k) * left ** (j - k) * (right - left) ** k
                          for j in range(k, 5)), F(0)) for k in range(5)]
            bernstein = [sum((local[j] * F(comb(k, j), comb(4, j))
                              for j in range(k + 1)), F(0)) for k in range(5)]
            check(list(map(F, cell["bernstein_coefficients"])) == bernstein,
                  f"factor/{index}/cell/{cell_index}/coefficients")
            minimum = min(bernstein)
            check(minimum > 0 and F(cell["minimum"]) == minimum,
                  f"factor/{index}/cell/{cell_index}/positivity")
            row_min = minimum if row_min is None else min(row_min, minimum)
            cells_total += 1
            coefficients_total += 5
        check(previous == 1 and row_min == F(row["minimum_bernstein_coefficient"]),
              f"factor/{index}/full cover and minimum")
        global_min = row_min if global_min is None else min(global_min, row_min)
        e = L - 1
        half_log = (e - e * e / 2 + e ** 3 / 3) / 2
        check(half_log == F(row["half_log_upper"]), f"factor/{index}/half log")
        rate += half_log / 128
        factor_rows.append({"t": str(t), "cells_replayed": len(row["cells"]),
                            "minimum_recomputed": str(row_min)})

    phase = F(0)
    check(len(data["phase_riemann_rows"]) == 128, "/phase_riemann_rows length")
    for index, row in enumerate(data["phase_riemann_rows"]):
        t = F(index, 128)
        args = [Y / (d - t), t * Y / (U - d * t)]
        raw = list(map(reduced_atan, args))
        rounded = [F((value * 10 ** 12).__floor__(), 10 ** 12) for value in raw]
        check(F(row["t"]) == t and list(map(F, row["atan_arguments"])) == args,
              f"phase/{index}/arguments")
        check(list(map(F, row["raw_lower_bounds"])) == raw, f"phase/{index}/raw lower")
        check(list(map(F, row["rounded_lower_bounds"])) == rounded, f"phase/{index}/rounding")
        check(all(0 <= lo <= exact for lo, exact in zip(rounded, raw)), f"phase/{index}/outward direction")
        phase += sum(rounded, F(0)) / 128
        phase_rows.append({"t": str(t), "rounded_sum": str(sum(rounded, F(0)))})

    comparisons = data["comparisons"]
    check(rate == F(comparisons["factor_rate_actual"]) < F(91, 5000), "factor rate")
    check(128 * rate == F(comparisons["factor_additive_actual"]) < 3, "factor additive")
    check(phase == F(comparisons["phase_integral_lower"]) > F(11, 21), "phase integral")
    onset = comparisons["valid_onset_for_n"]
    check(onset * (phase - F(11, 21)) > 4, "phase onset")
    check(Y * Y * F(8, 45) == F(81, 6250), "endpoint log rate")
    check(F(1, 32) - F(91, 5000) - F(81, 6250) == F(9, 100000), "cost growth rate")
    check(not data["failures"], "source certificate failures")
    summary = {"factor_rows": len(factor_rows), "cells_replayed": cells_total,
               "bernstein_coefficients_replayed": coefficients_total,
               "minimum_bernstein_coefficient": str(global_min),
               "factor_rate": str(rate), "required_rate_strict_upper": "91/5000",
               "rate_margin": str(F(91, 5000) - rate),
               "phase_rows_replayed": len(phase_rows), "phase_integral_lower": str(phase),
               "required_phase_strict_lower": "11/21", "onset": onset,
               "cost_growth_rate": "9/100000"}
    output = {"kind": "COMPLETE_EXACT_REPLAY", "source_certificate": source.name,
              "summary": summary, "factor_rows": factor_rows, "phase_rows": phase_rows,
              "failures": failures,
              "limitations": "Arithmetic replay, not an independent audit of the analytic contour proof or of H."}
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(f"Replayed every factor: {len(factor_rows)}, cell: {cells_total}, Bernstein coefficient: {coefficients_total}, phase row: {len(phase_rows)}")
    print(f"Rate actual {float(rate):.12g}, required < .0182; endpoint cost growth {F(9, 100000)} > required 0")
    print(f"Failures: {len(failures)}; full replay: {path}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
