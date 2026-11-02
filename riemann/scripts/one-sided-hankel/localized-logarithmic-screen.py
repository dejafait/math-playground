"""Bounded diagnostic for the paid logarithmic criterion; not a certificate.

All first-M moments, original unit residues, the full rotated grid and
the exact squared-residue diagonal are retained. Finite quadrature and
polynomial roots are not enclosed. No optimization/asymptotic claim.
"""
import json
from pathlib import Path

import numpy as np

X, R = -1.25, 1.375
U = R * R
NA, NZ = 512, 4096
theta = 2 * np.pi * np.arange(NA) / NA
u = np.exp(1j * theta)
records = []
failures = []


def root_mean(c):
    indices = np.flatnonzero(c != 0)
    if not len(indices):
        return None
    degree = int(indices[-1])
    roots = np.roots(c[:degree + 1][::-1]) if degree else np.array([])
    return {
        "degree": degree,
        "log_leading_modulus": float(np.log(abs(c[degree]))),
        "root_log_plus_sum": float(np.log(np.maximum(1, np.abs(roots))).sum()),
        "log_mahler": float(np.log(abs(c[degree]))
                            + np.log(np.maximum(1, np.abs(roots))).sum()),
        "root_moduli": np.abs(roots).tolist(),
    }


for n in (51, 99, 195):
    mass = n // 3
    for geometry, radius in (("chebyshev", 0.3), ("chebyshev", 0.54),
                             ("uniform", 0.3), ("uniform", 0.54)):
        if geometry == "chebyshev":
            ys = radius * np.cos((2 * np.arange(mass) + 1) * np.pi / (2 * mass))
        else:
            ys = np.linspace(-radius, radius, mass)
        ys[mass // 2] = 0
        aa = X + 1j * ys
        w = np.broadcast_to((X / aa)[:, None], (mass, NA)).copy()
        for j in range(1, n):
            t = j / n
            w *= (X - t * u) / (aa[:, None] - t * u)
            w *= (U * u - t * aa[:, None]) / (U * u - t * X)
        c = w.T @ ((aa[:, None] / R) ** np.arange(mass)[None, :] / R)
        values = np.fft.fft(c, n=NZ, axis=1)
        logs = np.log(np.abs(values))
        log_mean = logs.mean(axis=1)
        l2 = np.sum(np.abs(c) ** 2, axis=1)
        diag = np.sum(abs(w) ** 2 / (U - abs(aa[:, None]) ** 2), axis=0)
        log_d = float(np.log(np.mean(diag)))
        doubled = np.concatenate([log_mean, log_mean])
        cumulative = np.concatenate([[0.0], np.cumsum(doubled)])
        best = (-np.inf, None, None)
        for count in range(1, NA + 1):
            arc_values = (np.log(count / NA)
                          + 2 * (cumulative[count:count + NA] - cumulative[:NA]) / count)
            start = int(np.argmax(arc_values))
            if arc_values[start] > best[0]:
                best = (float(arc_values[start]), start, count)
        selected = sorted(set([int(np.argmax(log_mean)), int(np.argmax(l2)),
                               int(best[1]), (best[1] + best[2] // 2) % NA]))
        checks = []
        for index in selected:
            rm = root_mean(c[index])
            refined = np.fft.fft(c[index], n=2 * NZ)
            checks.append({
                "angular_index": index, "theta": float(theta[index]),
                "quadrature_log_mean": float(log_mean[index]),
                "refined_quadrature_log_mean": float(np.log(abs(refined)).mean()),
                "root_formula": rm,
            })
        record = {
            "n": n, "M": mass, "geometry": geometry, "radius": radius,
            "ordinates": ys.tolist(), "residues": [1] * mass,
            "sampled_log_D": log_d, "sampled_log_S": float(np.log(np.mean(l2))),
            "sampled_best_paid_mean": best[0],
            "sampled_best_arc_start_index": best[1], "sampled_best_arc_cells": best[2],
            "sampled_best_arc_measure": best[2] / NA,
            "required_minimum_arc_measure": n ** -2,
            "apparent_paid_loss_rate": (log_d - best[0]) / n,
            "apparent_maximum_log_mean_loss_rate": (log_d - 2 * max(log_mean)) / n,
            "required_squared_loss_rate": 1 / 16,
            "sampled_paid_margin_without_C": best[0] - log_d + n / 16,
            "angular_spatial_log_means": log_mean.tolist(),
            "angular_spatial_L2_squared": l2.tolist(),
            "angular_diagonal": diag.tolist(), "selected_root_checks": checks,
        }
        if not (np.isfinite(log_mean).all() and np.isfinite(diag).all()
                and np.isfinite(l2).all() and np.all(diag > 0)):
            failures.append({"n": n, "geometry": geometry, "radius": radius,
                             "failure": "nonfinite logarithm/norm or nonpositive diagonal"})
        if len(np.unique(ys)) != mass or 0.0 not in ys or max(abs(ys)) > 0.54:
            failures.append({"n": n, "geometry": geometry, "radius": radius,
                             "failure": "finite family parameter check"})
        record["maximum_selected_root_quadrature_difference"] = max(
            abs(check["root_formula"]["log_mahler"] - check["quadrature_log_mean"])
            for check in checks)
        records.append(record)
        print("NONRIGOROUS", {k: record[k] for k in (
            "n", "geometry", "radius", "apparent_paid_loss_rate",
            "required_squared_loss_rate", "sampled_paid_margin_without_C")}, flush=True)

output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps({
    "status": "NONRIGOROUS_DIAGNOSTIC_ONLY", "angular_count": NA,
    "spatial_count": NZ, "records": records,
    "failures": failures,
    "limitations": [
        "No roundoff, root-location, spatial-log quadrature or angular-arc enclosure.",
        "Optimizing discrete arcs is not optimizing all connected continuous arcs.",
        "Every tested pole family is admissible; no asymptotic countersequence is certified.",
        "A finite loss above 1/16 does not refute an unknown absolute constant/onset.",
        "The spatial root formula is exact analytically, but its computed roots are floating-point.",
    ],
}, indent=2) + "\n")
print("No certified conclusion; full diagnostic:", output)
print("Finite diagnostic failures:", failures)
