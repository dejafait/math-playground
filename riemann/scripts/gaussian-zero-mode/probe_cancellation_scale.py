"""Bounded floating-point discovery for the approved regulated sign test.

The printed values are candidate locations, never sign certificates.
Independent outward arithmetic is required for any accepted example.
NumPy is used only here, not by the certificate.
"""

import json
import math
import numpy as np


def probe(epsilon, seed, samples=20000):
    rng = np.random.default_rng(seed)
    tenths = rng.integers(500000, 10000000, size=samples)
    last = math.ceil(math.sqrt(40 / (math.pi * epsilon)))
    indices = np.arange(1, last + 1)
    logs = np.log(indices)
    coefficients = indices**(-0.5) * np.exp(-math.pi * epsilon * indices**2)
    best_sign = best_bound = None
    negative_samples = 0
    for offset in range(0, samples, 256):
        ticks = tenths[offset:offset + 256]
        xi = ticks / 10
        terms = coefficients * np.exp(-1j * xi[:, None] * logs)
        series = terms.sum(axis=1)
        first = (terms * (-1j * logs)).sum(axis=1)
        second = (terms * (-logs**2)).sum(axis=1)
        s = 0.25 + 0.5j * xi
        # Discovery approximations only; the certificate reuses gamma_data.
        lg = ((s - 0.5) * np.log(s) - s + 0.5 * math.log(2 * math.pi)
              + 1 / (12 * s) - 1 / (360 * s**3))
        psi = np.log(s) - 1 / (2 * s) - 1 / (12 * s**2) + 1 / (120 * s**4)
        psi1 = 1 / s + 1 / (2 * s**2) + 1 / (6 * s**3) - 1 / (30 * s**5)
        omega = (psi.real - math.log(math.pi)) / 2
        omega_prime = -psi1.imag / 4
        polynomial = xi**2 + 0.25
        curvature = 2 / polynomial - 4 * xi**2 / polynomial**2 - psi1.real / 4
        phase = lg.imag - xi * math.log(math.pi) / 2
        rotation = np.exp(1j * phase)
        c, d, e = rotation * series, rotation * first, rotation * second
        velocity = first + 1j * omega * series
        sign = (np.abs(velocity)**2 - d.imag**2 - c.real * e.real
                + omega_prime * c.real * c.imag - curvature * c.real**2)
        # A sufficient upper bound retains the two leading squares and
        # controls the second derivative and gamma corrections in magnitude.
        upper = (np.abs(velocity)**2 - d.imag**2 + np.abs(series) * np.abs(second)
                 + (np.abs(omega_prime) / 2 + np.abs(curvature)) * np.abs(series)**2)
        negative_samples += int((sign < 0).sum())
        for values, label in ((sign, "sign"), (upper, "bound")):
            index = int(values.argmin())
            entry = {
                "xi_tenths": int(ticks[index]), "value": float(values[index]),
                "normalized_laguerre_probe": float(sign[index]),
                "cancellation_upper_probe": float(upper[index]),
                "omega_probe": float(omega[index]),
                "series_abs_probe": float(abs(series[index])),
                "derivative_abs_probe": float(abs(first[index])),
                "second_derivative_abs_probe": float(abs(second[index])),
                "velocity_abs_probe": float(abs(velocity[index])),
                "rotated_derivative_imag_probe": float(d.imag[index]),
            }
            if label == "sign" and (best_sign is None or entry["value"] < best_sign["value"]):
                best_sign = entry
            if label == "bound" and (best_bound is None or entry["value"] < best_bound["value"]):
                best_bound = entry
    return {
        "epsilon_probe": epsilon, "seed": seed, "samples": samples,
        "xi_range": "[50000,1000000), rational tenths", "last_series_index": last,
        "negative_samples_probe": negative_samples,
        "best_sign_probe": best_sign, "best_bound_probe": best_bound,
    }


if __name__ == "__main__":
    print(json.dumps({
        "scope": "Floating-point discovery only; no epsilon-to-zero conclusion",
        "cases": [probe(epsilon, seed) for epsilon, seed in
                  ((1e-4, 10401), (1e-5, 10402), (1e-6, 10403))],
    }, indent=2))
