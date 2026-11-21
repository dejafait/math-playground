#!/usr/bin/env python3
"""Bounded floating screen of the full signed correction; not a proof certificate."""

import json
import math
import sys
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss

X, R, U = -1.25, 1.375, 1.375 ** 2
DEN = 10 ** 10
REG = 1e-16


def family(n, e):
    q = (n - 3) // 12
    assert n == 12 * q + 3 and len(e) == 4 * q
    h = 2.7 / n
    y = h * (np.arange(-2 * q, 2 * q) + 0.5)
    return h, y, np.r_[complex(X), X + 1j * (y + h * e)]


def response(n, e, angles=128, offset=0.0, derivative=False):
    h, _, a = family(n, e)
    m = len(a)
    u = np.exp(2j * np.pi * (np.arange(angles) + offset) / angles)
    tj = np.arange(1, n) / n
    aa, uu, tt = a[None, :, None], u[:, None, None], tj[None, None, :]
    factor = ((X - tt * uu) / (aa - tt * uu)
              * (U * uu - tt * aa) / (U * uu - tt * X))
    w = (X / a)[None, :] * np.exp(np.log(factor).sum(axis=2))
    powers = (a[:, None] / R) ** np.arange(m)[None, :]
    c = w @ powers / R
    if not derivative:
        return c
    da = -1 / a[None, :] - (1 / (aa - tt * uu)
                            + tt / (U * uu - tt * aa)).sum(axis=2)
    dpowers = np.zeros_like(powers)
    dpowers[:, 1:] = (np.arange(1, m)[None, :] / R
                      * (a[:, None] / R) ** np.arange(m - 1)[None, :])
    return c, w, da, powers, dpowers, h


def objective(n, e, angles=96, spatial=256, gradient=False):
    if gradient:
        c, w, da, powers, dpowers, h = response(n, e, angles, derivative=True)
    else:
        c = response(n, e, angles)
    values = np.fft.ifft(c, n=spatial, axis=1) * spatial
    squared = abs(values) ** 2 + REG
    value = float(np.log(squared).mean() / 2)
    if not gradient:
        return value
    beta = np.fft.ifft(np.conj(values) / squared, axis=1)[:, :c.shape[1]]
    grad = np.real((1j * h / R) * w
                   * (da * (beta @ powers.T) + beta @ dpowers.T)).mean(axis=0)
    return value, grad[1:]


def optimize(n, start, iterations=40):
    e = start.copy()
    trace = []
    for iteration in range(iterations):
        value, grad = objective(n, e, gradient=True)
        trace.append({"iteration": iteration, "value": value,
                      "max_abs_gradient": float(max(abs(grad)))})
        direction = -grad / max(1.0, float(max(abs(grad))))
        accepted = False
        for backtrack in range(14):
            candidate = np.clip(e + 0.08 * 0.5 ** backtrack * direction, -0.125, 0.125)
            displacement = float(np.max(abs(candidate - e)))
            if displacement < 1e-12:
                break
            trial = objective(n, candidate)
            if trial < value - 1e-5 * displacement ** 2:
                e = candidate
                accepted = True
                break
        if not accepted:
            break
    numerators = np.rint(e * DEN).astype(np.int64)
    e = numerators / DEN
    return e, {"shift_denominator": DEN, "shift_numerators": numerators.tolist(),
               "trace": trace, "rounded_grid_mean": objective(n, e)}


def root_means(c):
    means, residuals, identities = [], [], []
    for coeff in c:
        degree = len(coeff) - 1
        while degree and coeff[degree] == 0:
            degree -= 1
        coeff = coeff[:degree + 1]
        roots = np.polynomial.polynomial.polyroots(coeff)
        mean = math.log(abs(coeff[-1])) + float(np.log(np.maximum(1, abs(roots))).sum())
        means.append(mean)
        if degree:
            scale = np.polynomial.polynomial.polyval(abs(roots), abs(coeff))
            residuals.append(float(np.max(abs(np.polynomial.polynomial.polyval(roots, coeff)) / scale)))
        if coeff[0] != 0 and all(abs(roots) > 0):
            alternative = math.log(abs(coeff[0])) + float((-np.log(np.minimum(1, abs(roots)))).sum())
            identities.append(abs(mean - alternative))
    return np.asarray(means), max(residuals, default=0.0), max(identities, default=0.0)


def validate_mean(n, e):
    records = []
    for angles, offset in [(128, 0.0), (256, 0.0), (512, 0.0), (512, 0.371)]:
        c = response(n, e, angles, offset)
        means, residual, identity = root_means(c)
        records.append({"angular_samples": angles, "angular_offset": offset,
                        "complete_spatial_root_mean": float(means.mean()),
                        "spatial_means_at_all_angles": means.tolist(),
                        "max_relative_root_residual": residual,
                        "max_two_root_formula_discrepancy": identity})
    _, _, a = family(n, e)
    m = len(a)
    c_at_origin = ((X / a)[:, None] * (a[:, None] / R)
                   ** np.arange(m)[None, :]).sum(axis=0) / R
    origin, residual, identity = root_means(c_at_origin[None, :])
    p_charge = -((n - 1) * math.log(80 / 121)
                 + math.lgamma(n) - (n - 1) * math.log(n))
    return {"angular_refinements": records, "m0_spatial_root_mean": float(origin[0]),
            "m0_root_residual": residual, "m0_root_formula_discrepancy": identity,
            "P_n": p_charge,
            "Z_n_inferred_from_L657_identity_not_independently_root_counted":
            records[-1]["complete_spatial_root_mean"] - float(origin[0]) + p_charge}


def scalar_integrand(n, y, u, zeta, derivative=False):
    a = X + 1j * np.asarray(y)
    tj = np.arange(1, n) / n
    aa, tt = a[:, None], tj[None, :]
    w = X / a * np.exp(np.log((X - tt * u) / (aa - tt * u)
                               * (U * u - tt * aa) / (U * u - tt * X)).sum(axis=1))
    m = n // 3
    powers = (a[:, None] * zeta / R) ** np.arange(m)[None, :]
    poly = powers.sum(axis=1)
    if not derivative:
        return w * poly
    da = -1 / a - (1 / (aa - tt * u) + tt / (U * u - tt * aa)).sum(axis=1)
    dpoly = (np.arange(1, m)[None, :] * zeta / R * powers[:, :-1]).sum(axis=1)
    return 1j * w * (da * poly + dpoly)


def complex_record(value):
    return {"real": float(value.real), "imag": float(value.imag)}


def kernel_check(n, e):
    h, y, _ = family(n, e)
    shifts = h * e
    yn = 2 * ((n - 3) // 12) * h
    corners = [-yn - 0.08j, yn - 0.08j, yn + 0.125j, -yn + 0.125j]
    output = []
    for theta, phi in [(math.pi, 0.43), (1.17, 2.03)]:
        u, zeta = np.exp(1j * theta), np.exp(1j * phi)
        direct = (scalar_integrand(n, y + shifts, u, zeta)
                  - scalar_integrand(n, y, u, zeta)).sum() / R
        row = {"angular_theta": theta, "spatial_phi": phi, "direct": complex_record(direct)}
        for order in [128, 256]:
            nodes, weights = leggauss(order)
            edge_values = []
            for index in range(4):
                first, last = corners[index], corners[(index + 1) % 4]
                z = (first + last) / 2 + (last - first) / 2 * nodes
                delta = (shifts[None, :] / ((z[:, None] - y[None, :] - shifts[None, :])
                                             * (z[:, None] - y[None, :]))).sum(axis=1)
                edge_values.append((weights * scalar_integrand(n, z, u, zeta)
                                    * delta).sum() * (last - first) / (4j * np.pi * R))
            contour = sum(edge_values)
            snodes, sweights = leggauss(24)
            arguments = y[:, None] + shifts[:, None] * (snodes[None, :] + 1) / 2
            deriv = scalar_integrand(n, arguments.reshape(-1), u, zeta, derivative=True).reshape(arguments.shape)
            transport = (deriv * shifts[:, None] * sweights[None, :]).sum() / (2 * R)
            row[str(order)] = {"four_oriented_edges": list(map(complex_record, edge_values)),
                               "signed_contour": complex_record(contour),
                               "signed_transport": complex_record(transport),
                               "contour_relative_error": float(abs(contour - direct) / (1 + abs(direct))),
                               "transport_relative_error": float(abs(transport - direct) / (1 + abs(direct)))}
        output.append(row)
    return output


def main():
    rng = np.random.default_rng(105)
    artifact = {"step_id": "2026-11-03-signed-canonical-correction-test-105",
                "scope": "Floating bounded full-spatial-mean screen; no intervals, global minimum, angular integral certification, or unbounded-n result.",
                "regularization_in_optimization_only": REG,
                "families": [], "failures": [],
                "unverified": ["angular quadrature convergence rate", "all angular numerator roots",
                               "uniform n/100+C log n bound", "asymptotic countersequence"]}
    n = 27
    trial = rng.uniform(-0.1, 0.1, n // 3 - 1)
    direction = rng.uniform(-1, 1, len(trial))
    _, gradient = objective(n, trial, gradient=True)
    dx = 1e-6
    numeric = (objective(n, trial + dx * direction) - objective(n, trial - dx * direction)) / (2 * dx)
    analytic = float(gradient @ direction)
    artifact["gradient_check"] = {"analytic": analytic, "finite_difference": numeric,
                                    "absolute_error": abs(analytic - numeric), "required_below": 1e-6}
    if abs(analytic - numeric) >= 1e-6:
        artifact["failures"].append("directional_gradient_check")
    selected = []
    for n in [51, 99]:
        m = n // 3 - 1
        starts = [("zero", np.zeros(m)), ("dense_random", rng.uniform(-0.125, 0.125, m))]
        for name, start in starts:
            shifts, record = optimize(n, start)
            record.update({"n": n, "start": name, "kind": "optimized_full_cube",
                           "actual_max_shift": float(max(abs(shifts))), "required_max_shift": 0.125})
            record["validation"] = validate_mean(n, shifts)
            record["baseline_validation"] = validate_mean(n, np.zeros(m))
            values = record["validation"]["angular_refinements"]
            baseline = record["baseline_validation"]["angular_refinements"]
            record["refined_loss"] = baseline[-1]["complete_spatial_root_mean"] - values[-1]["complete_spatial_root_mean"]
            record["linear_budget_n_over_100_without_unknown_log_term"] = n / 100
            record["fine_grid_spread"] = abs(values[-1]["complete_spatial_root_mean"] - values[-2]["complete_spatial_root_mean"])
            artifact["families"].append(record)
            selected.append((n, shifts, record))
            print(f"n={n} start={name}: refined loss={record['refined_loss']:.9g}; n/100={n/100:.9g}; shifted-fine-grid spread={record['fine_grid_spread']:.3g}", flush=True)
    n = 195
    m = n // 3 - 1
    for name, shifts in [("alternating_dense", 0.125 * (-1.0) ** np.arange(m)),
                         ("dense_random", rng.choice([-0.125, 0.125], size=m))]:
        validation = validate_mean(n, shifts)
        baseline = validate_mean(n, np.zeros(m))
        loss = baseline["angular_refinements"][-1]["complete_spatial_root_mean"] - validation["angular_refinements"][-1]["complete_spatial_root_mean"]
        artifact["families"].append({"n": n, "kind": name, "shift_denominator": DEN,
                                    "shift_numerators": np.rint(shifts * DEN).astype(np.int64).tolist(),
                                    "actual_max_shift": float(max(abs(shifts))), "required_max_shift": 0.125,
                                    "validation": validation, "baseline_validation": baseline,
                                    "refined_loss": loss, "linear_budget_n_over_100_without_unknown_log_term": n / 100})
        print(f"n={n} pattern={name}: refined loss={loss:.9g}; n/100={n/100:.9g}", flush=True)
    n, shifts, _ = min((item for item in selected if item[0] == 51), key=lambda item: item[2]["rounded_grid_mean"])
    artifact["exact_identity_floating_checks"] = kernel_check(n, shifts)
    for row in artifact["exact_identity_floating_checks"]:
        if row["256"]["contour_relative_error"] > 1e-7:
            artifact["failures"].append("finite_signed_contour_replay")
        if row["256"]["transport_relative_error"] > 1e-9:
            artifact["failures"].append("finite_signed_transport_replay")
    for row in artifact["families"]:
        for side in ["validation", "baseline_validation"]:
            for sample in row[side]["angular_refinements"]:
                if sample["max_relative_root_residual"] > 1e-7:
                    artifact["failures"].append("spatial_root_residual")
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(artifact, indent=2) + "\n")
    print(f"Diagnostic failures: {artifact['failures']}")
    print(f"Certificate: {path}")
    print("Spatial roots are floating; angular means and inferred charges remain uncertified. No theorem follows.")


def extend_once():
    """One larger-size check prompted by the initially observed finite losses."""
    path = Path(__file__).with_suffix(".json")
    artifact = json.loads(path.read_text())
    if "larger_size_followup" in artifact:
        raise SystemExit("The single larger-size follow-up is already saved; no repeated optimization.")
    n = 195
    shifts, record = optimize(n, np.zeros(n // 3 - 1))
    record.update({"n": n, "start": "zero", "kind": "optimized_full_cube",
                   "actual_max_shift": float(max(abs(shifts))), "required_max_shift": 0.125})
    record["validation"] = validate_mean(n, shifts)
    record["baseline_validation"] = validate_mean(n, np.zeros(n // 3 - 1))
    values = record["validation"]["angular_refinements"]
    baseline = record["baseline_validation"]["angular_refinements"]
    record["refined_loss"] = baseline[-1]["complete_spatial_root_mean"] - values[-1]["complete_spatial_root_mean"]
    record["linear_budget_n_over_100_without_unknown_log_term"] = n / 100
    record["fine_grid_spread"] = abs(values[-1]["complete_spatial_root_mean"] - values[-2]["complete_spatial_root_mean"])
    artifact["families"].append(record)
    artifact["larger_size_followup"] = "One n=195 zero-start run; finite n=51,99 losses did not decide the asymptotic rate. No further size escalation."
    summary = []
    residuals, identities, spreads = [], [], []
    for row in artifact["families"]:
        e = np.asarray(row["shift_numerators"]) / row["shift_denominator"]
        _, _, a = family(row["n"], e)
        _, _, a0 = family(row["n"], np.zeros(len(e)))
        row["exact_formula_evaluated_floating_Q_mean_change"] = float((row["n"] - 1) * np.log(abs(a[1:]) / abs(a0[1:])).sum())
        row["m0_change"] = row["validation"]["m0_spatial_root_mean"] - row["baseline_validation"]["m0_spatial_root_mean"]
        row["Z_change_inferred_not_independently_root_counted"] = -row["refined_loss"] - row["m0_change"]
        checks = row["validation"]["angular_refinements"]
        spread = abs(checks[-1]["complete_spatial_root_mean"] - checks[-2]["complete_spatial_root_mean"])
        spreads.append(spread)
        for side in ["validation", "baseline_validation"]:
            for sample in row[side]["angular_refinements"]:
                residuals.append(sample["max_relative_root_residual"])
                identities.append(sample["max_two_root_formula_discrepancy"])
        summary.append({"n": row["n"], "start_or_pattern": row.get("start", row["kind"]),
                        "loss": row["refined_loss"], "n_over_100": row["n"] / 100,
                        "loss_per_n": row["refined_loss"] / row["n"], "fine_grid_spread": spread,
                        "Q_mean_change": row["exact_formula_evaluated_floating_Q_mean_change"],
                        "m0_change": row["m0_change"],
                        "inferred_Z_change": row["Z_change_inferred_not_independently_root_counted"]})
    artifact["summary"] = {"families": summary, "max_relative_root_residual": max(residuals),
                           "root_residual_required_below": 1e-7,
                           "max_two_root_formula_discrepancy": max(identities),
                           "max_shifted_fine_grid_spread": max(spreads),
                           "qualification": "Finite floating comparisons only; the n/100 column omits the unknown C log n and onset. Numerical Z values use the exact identity, not a root census."}
    if max(residuals) > 1e-7:
        artifact["failures"].append("larger_size_spatial_root_residual")
    path.write_text(json.dumps(artifact, indent=2) + "\n")
    print(f"Larger-size follow-up n={n}: refined loss={record['refined_loss']:.9g}; n/100={n/100:.9g}; fine-grid spread={record['fine_grid_spread']:.3g}")
    print(f"Maximum root residual={max(residuals):.6g}; required <1e-7; formula discrepancy={max(identities):.6g}")
    print(f"Diagnostic failures: {artifact['failures']}")
    print(f"Certificate: {path}")


if __name__ == "__main__":
    if sys.argv[1:] == ["--extend-once"]:
        extend_once()
    elif not sys.argv[1:]:
        main()
    else:
        raise SystemExit("Usage: signed-canonical-correction-105.py [--extend-once]")
