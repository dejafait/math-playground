#!/usr/bin/env python3
"""Bounded diagnostic of a single-grid-factor envelope, not a proof."""
import json
from pathlib import Path

import numpy as np


def main():
    d = 5 / 4
    u2 = 121 / 64
    cosines = np.linspace(-1, 1, 20001)
    sine_squares = 1 - cosines * cosines
    rows = []
    failures = []
    for t in np.linspace(0, 1, 101):
        numerator_at_zero = d * d + t * t + 2 * d * t * cosines
        denominator_at_zero = u2 * u2 + t * t * d * d + 2 * u2 * d * t * cosines
        quadratic_a = (d + t * cosines) ** 2
        quadratic_b = (denominator_at_zero + t * t * numerator_at_zero
                       - 2 * u2 * t * t * sine_squares)
        quadratic_c = t * t * (u2 * cosines + t * d) ** 2
        discriminant = quadratic_b ** 2 - 4 * quadratic_a * quadratic_c
        eigenvalue = 2 * quadratic_a / (
            quadratic_b + np.sqrt(np.maximum(discriminant, 0)))
        gain = 0.5 * np.log(numerator_at_zero / (denominator_at_zero * eigenvalue))
        if not np.all(np.isfinite(gain)):
            failures.append({"t": float(t), "failure": "nonfinite gain"})
        index = int(np.argmax(gain))
        rows.append({"t": float(t), "maximum_sampled_log_gain": float(gain[index]),
                     "cosine": float(cosines[index]),
                     "minimum_raw_discriminant": float(np.min(discriminant))})
    integral = sum((rows[j]["maximum_sampled_log_gain"]
                    + rows[j + 1]["maximum_sampled_log_gain"]) * 0.005
                   for j in range(100))
    output = Path(__file__).with_suffix(".json")
    certificate = {
        "kind": "NONRIGOROUS_DIAGNOSTIC",
        "parameters": {"d": "5/4", "U": "121/64", "t_intervals": 100,
                       "cosine_intervals": 20000, "ordinate_domain": "all real y"},
        "integral_diagnostic": integral,
        "required_amplitude_rate": "1/32",
        "failures": failures,
        "rows": rows,
        "limitations": [
            "No floating-point, cosine-grid or t-quadrature error enclosure.",
            "The unrestricted real ordinate envelope enlarges the allowed pole set.",
            "Each grid factor is optimized separately; a common pole and angle need not attain these values.",
            "This is not a bound on H, a family screen, or a proof of the paid-arc criterion.",
            "The first inline invocation failed before producing a result because NumPy has no trapz attribute; this version uses an explicit trapezoid sum."
        ]
    }
    output.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Single-factor envelope diagnostic; no enclosure or proof.")
    print(f"Integral diagnostic: {integral:.12g}; required amplitude rate: {1/32:.12g}")
    print(f"Failures: {len(failures)}; full diagnostic: {output}")


if __name__ == "__main__":
    main()
