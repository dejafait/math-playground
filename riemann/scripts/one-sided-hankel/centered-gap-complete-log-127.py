#!/usr/bin/env python3
"""Finite centered-gap/Picard and full-log screen. NOT a proof certificate."""

import importlib.util
import json
import math
import sys
from decimal import Decimal, localcontext
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OUT = HERE / "centered-gap-complete-log-127.json"
X, D, R, U, A = -1.25, 1.25, 1.375, 1.375 ** 2, 2.7
OMEGA = A * (math.log((D + 1) / D) - 1 / D
             + U / D ** 2 * math.log((U + D) / U))
CENTER = OMEGA / (2 * math.pi)
WIDTH = min(0.04, 0.8 * (CENTER - 0.125), 0.8 * (0.375 - CENTER))
DEGREE = 14


def cutoff(v, inside, outside):
    """Smooth even cutoff: one on |v|<=inside, zero on |v|>=outside."""
    r = np.abs(np.asarray(v))
    out = np.zeros_like(r)
    out[r <= inside] = 1.0
    mask = (r > inside) & (r < outside)
    s = (outside - r[mask]) / (outside - inside)
    aa, bb = np.exp(-1 / s), np.exp(-1 / (1 - s))
    out[mask] = aa / (aa + bb)
    return out


def solve_profile(size):
    t = np.fft.fftfreq(size)
    phi = cutoff(t, 3 / 8, 7 / 16)
    chi = cutoff(t - CENTER, WIDTH / 2, WIDTH) + cutoff(t + CENTER, WIDTH / 2, WIDTH)
    target = np.zeros(size, dtype=complex)
    nz = chi != 0
    # Q(t)=P(-t)=-exp(-pi*i*t)*chi(t)/(2*pi*i*t).
    target[nz] = -np.exp(-1j * math.pi * t[nz]) * chi[nz] / (2j * math.pi * t[nz])
    alpha = (np.fft.fft(target) / size).real
    traces = []
    for iteration in range(50):
        nonlinear = np.zeros(size, dtype=complex)
        for k in range(2, DEGREE + 1):
            nonlinear += ((2j * math.pi * t) ** (k - 1) / math.factorial(k)
                          * (np.fft.ifft(alpha ** k) * size))
        updated_complex = np.fft.fft(target - phi * nonlinear) / size
        updated = updated_complex.real
        change = float(np.max(abs(updated - alpha)))
        traces.append({"iteration": iteration, "sup_change": change,
                       "l1_change": float(np.sum(abs(updated - alpha))),
                       "max_imaginary_coefficient": float(np.max(abs(updated_complex.imag)))})
        alpha = updated
        if change < 2e-15:
            break
    indices = np.rint(np.fft.fftfreq(size) * size).astype(int)
    order = np.argsort(indices)
    indices, alpha = indices[order], alpha[order]
    # Check the finite signed correction away from FFT nodes, not just the equation grid.
    frequencies = np.linspace(OMEGA - math.pi * WIDTH, OMEGA + math.pi * WIDTH, 61)
    residual = []
    for v in frequencies:
        correction = np.sum(np.exp(1j * v * (indices + 0.5)) * np.expm1(1j * v * alpha))
        residual.append(complex(1 + correction))
    record = {
        "grid_size": size, "indices": indices.tolist(), "shifts": alpha.tolist(),
        "iteration_trace": traces, "max_abs_shift": float(np.max(abs(alpha))),
        "l1_shift_sum_finite": float(np.sum(abs(alpha))),
        "outer_quarter_l1": float(np.sum(abs(alpha[abs(indices) >= size // 4]))),
        "gap_frequencies": frequencies.tolist(),
        "finite_gap_residuals": [{"real": v.real, "imag": v.imag} for v in residual],
        "max_finite_gap_residual": float(max(abs(v) for v in residual)),
        "qualified": "Finite Fourier approximation, no infinite gap or contraction certificate.",
    }
    return dict(zip(indices.tolist(), alpha.tolist())), record


def coefficients(n, profile, theta):
    q = (n - 3) // 12
    indices = np.arange(-2 * q, 2 * q)
    shifts = np.array([profile[int(k)] for k in indices])
    nodes = np.r_[complex(X), X + 1j * A / n * (indices + 0.5 + shifts)]
    degree = n // 3
    powers = (nodes[:, None] / R) ** np.arange(degree)[None, :]
    tj = np.arange(1, n) / n
    all_c = []
    conditions = []
    for start in range(0, len(theta), 8):
        u = np.exp(1j * theta[start:start + 8])
        aa, uu, tt = nodes[None, :, None], u[:, None, None], tj[None, None, :]
        factor = ((X - tt * uu) / (aa - tt * uu)
                  * (U * uu - tt * aa) / (U * uu - tt * X))
        w = (X / nodes)[None, :] * np.exp(np.log(factor).sum(axis=2))
        c = w @ powers / R
        all_c.extend(c)
        conditions.extend(np.sum(abs(w), axis=1) / np.maximum(abs(np.sum(w, axis=1)), 1e-300))
    return np.asarray(all_c), nodes, np.asarray(conditions)


def evaluate(n, profile, angular, spatial, offset):
    theta = 2 * math.pi * (np.arange(angular) + offset) / angular
    c, nodes, condition = coefficients(n, profile, theta)
    values = np.fft.ifft(c, n=spatial, axis=1) * spatial
    magnitudes = abs(values)
    means = np.log(magnitudes).mean(axis=1)
    # This fixed diagnostic arc is not claimed to be L698's existential arc.
    wrapped = (theta + math.pi) % (2 * math.pi) - math.pi
    mask = abs(wrapped) <= 0.10
    return {
        "angular_samples": angular, "spatial_samples": spatial, "angular_offset": offset,
        "theta": theta.tolist(), "spatial_log_means": means.tolist(),
        "approximate_A": float(means.mean()), "approximate_A_over_n": float(means.mean() / n),
        "test_arc_radians": 0.10, "test_arc_sample_count": int(mask.sum()),
        "test_arc_weighted_log_contribution": float(np.sum(means[mask]) / angular),
        "complement_weighted_log_contribution": float(np.sum(means[~mask]) / angular),
        "minimum_sampled_modulus": float(np.min(magnitudes)),
        "max_scalar_cancellation_condition": float(max(condition)),
        "finite_values": bool(np.all(np.isfinite(means))),
        "full_moment_count": len(nodes),
        "no_log_regularizer": True,
        "zeros_warning": "Sampled nonzero values and grid agreement do not certify a singular logarithmic integral.",
    }, c


def main():
    records = []
    profiles = []
    for size in (4096, 8192):
        profile, record = solve_profile(size)
        profiles.append(profile)
        records.append(record)
        print(f"Picard grid {size}: cap {record['max_abs_shift']:.6g} <= 0.125; "
              f"finite gap residual {record['max_finite_gap_residual']:.3g} (diagnostic target 1e-8)", flush=True)
    common = range(-512, 512)
    discrepancy = max(abs(profiles[0][k] - profiles[1][k]) for k in common)
    data = {
        "step_id": "2026-11-03-centered-gap-complete-log-127",
        "status": "NUMERICAL EXPLORATION, NOT A RIGOROUS CERTIFICATE",
        "constants": {"omega_star": OMEGA, "center_cycles": CENTER, "cutoff_width_cycles": WIDTH,
                      "nominal_gap_radius_radians": math.pi * WIDTH, "nonlinear_series_degree": DEGREE},
        "profiles": records, "central_1024_shift_grid_discrepancy": discrepancy,
        "same_fixed_largest_grid_profile_all_n": True,
        "families": [], "diagnostic_failures": [],
        "unresolved": ["Nominal cutoff width not certified against Lev/L694 contraction constant.",
                       "Finite Fourier approximation has no certified infinite centered gap or tail.",
                       "No rigorous growing-n logarithmic quadrature or sign bound.",
                       "No asymptotic counterprofile, full-mean theorem, H/support or Xi implication."],
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    old_spec = importlib.util.spec_from_file_location("screen105", HERE / "signed-canonical-correction-105.py")
    old = importlib.util.module_from_spec(old_spec)
    old_spec.loader.exec_module(old)
    for n in (51, 99, 195, 387, 771):
        family = {"n": n, "q": (n - 3) // 12, "grids": []}
        for angular, spatial, offset in ((256, 512, 0.0), (512, 1024, 0.371)):
            result, coeff = evaluate(n, profiles[1], angular, spatial, offset)
            if n <= 99 and angular == 256:
                means, residual, identity = old.root_means(coeff)
                result["complete_spatial_root_check"] = {
                    "all_spatial_means": means.tolist(), "angular_mean": float(means.mean()),
                    "root_vs_spatial_grid_mean_difference": float(abs(means.mean() - result["approximate_A"])),
                    "max_relative_root_residual": residual,
                    "max_two_root_formula_discrepancy": identity,
                }
            family["grids"].append(result)
            print(f"n={n}, grid={angular}x{spatial}: A~{result['approximate_A']:.9g}, "
                  f"A/n~{result['approximate_A_over_n']:.6g}, arc~{result['test_arc_weighted_log_contribution']:.6g}, "
                  f"complement~{result['complement_weighted_log_contribution']:.6g}", flush=True)
        family["quadrature_refinement_difference"] = abs(family["grids"][0]["approximate_A"] - family["grids"][1]["approximate_A"])
        # The smaller Fourier grid changes the same retained finite shifts only.
        check, _ = evaluate(n, profiles[0], 256, 512, 0.0)
        family["profile_refinement_mean_difference"] = abs(check["approximate_A"] - family["grids"][0]["approximate_A"])
        for grid in family["grids"]:
            if not grid["finite_values"]:
                data["diagnostic_failures"].append(f"nonfinite sampled logs at n={n}")
        data["families"].append(family)
        OUT.write_text(json.dumps(data, indent=2) + "\n")
    for rec in records:
        if rec["max_abs_shift"] > 0.125:
            data["diagnostic_failures"].append(f"cap exceeded on grid {rec['grid_size']}")
        if rec["max_finite_gap_residual"] > 1e-8:
            data["diagnostic_failures"].append(f"finite gap residual >1e-8 on grid {rec['grid_size']}")
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Central-profile discrepancy: {discrepancy:.3g}; failures: {data['diagnostic_failures']}")
    print(f"Full diagnostic artifact: {OUT}")


def decimal_check(n, profile, theta, phi):
    """Independent 60-digit finite products/sums at selected points only."""
    with localcontext() as ctx:
        ctx.prec = 60
        zero, one = Decimal(0), Decimal(1)

        def add(a, b):
            return a[0] + b[0], a[1] + b[1]

        def sub(a, b):
            return a[0] - b[0], a[1] - b[1]

        def mul(a, b):
            return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]

        def div(a, b):
            denom = b[0] * b[0] + b[1] * b[1]
            return ((a[0] * b[0] + a[1] * b[1]) / denom,
                    (a[1] * b[0] - a[0] * b[1]) / denom)

        def scalar(s, a):
            return s * a[0], s * a[1]

        def phase(angle):
            angle = Decimal(str(angle))
            # Direct Taylor terms; at the used |angle|<=2*pi, 140 terms
            # put the truncation far below the working precision.
            cc, ss, tc, ts = one, angle, one, angle
            for k in range(1, 140):
                tc *= -angle * angle / Decimal((2 * k - 1) * (2 * k))
                ts *= -angle * angle / Decimal((2 * k) * (2 * k + 1))
                cc += tc
                ss += ts
            return cc, ss

        xx, rr, uu = Decimal(-5) / 4, Decimal(11) / 8, Decimal(121) / 64
        h = Decimal(27) / (10 * n)
        u, z = phase(theta), phase(phi)
        q = (n - 3) // 12
        nodes = [(xx, zero)] + [(xx, h * (Decimal(m) + Decimal('0.5') + Decimal(str(profile[m]))))
                               for m in range(-2 * q, 2 * q)]
        total = (zero, zero)
        for a in nodes:
            w = (one, zero)
            for j in range(n):
                t = Decimal(j) / n
                first = div(sub((xx, zero), scalar(t, u)), sub(a, scalar(t, u)))
                second = div(sub(scalar(uu, u), scalar(t, a)),
                             sub(scalar(uu, u), (t * xx, zero)))
                w = mul(w, mul(first, second))
            az = scalar(one / rr, mul(a, z))
            term, poly = (one, zero), (zero, zero)
            for k in range(n // 3):
                poly = add(poly, term)
                term = mul(term, az)
            total = add(total, mul(w, poly))
        value = scalar(one / rr, total)
        return {"real": str(value[0]), "imag": str(value[1])}


def verify():
    data = json.loads(OUT.read_text())
    rec = data["profiles"][-1]
    profile = dict(zip(rec["indices"], rec["shifts"]))
    verification = {"scope": "Floating and selected 60-digit checks only, not rigorous integral enclosures.",
                    "mpmath_unavailable": True, "point_checks": [], "failures": []}
    family = data["families"][-1]
    result, _ = evaluate(771, profile, 1024, 2048, 0.173)
    family["grids"].append(result)
    verification["last_mean_refinement_difference"] = abs(result["approximate_A"] - family["grids"][-2]["approximate_A"])
    # Fix the cancellation-sensitive angle from the original refined grid.
    grid = family["grids"][1]
    cc, _, conditions = coefficients(771, profile, np.array(grid["theta"]))
    scalar_logs = np.log(abs(cc[:, 0]))
    verification["scalar_lower_bound_probe"] = {
        "n": 771, "angular_samples": len(scalar_logs), "theta": grid["theta"],
        "all_scalar_log_magnitudes": scalar_logs.tolist(),
        "approximate_scalar_log_mean": float(scalar_logs.mean()),
        "approximate_scalar_log_mean_over_n": float(scalar_logs.mean() / 771),
        "all_finite": bool(np.isfinite(scalar_logs).all()),
        "qualification": "Diagnostic for L666's existing pointwise Jensen lower bound only; no asymptotic scalar or full-mean estimate.",
    }
    worst = int(np.argmax(conditions))
    points = [(0.0, 0.37), (grid["theta"][worst], math.pi), (math.pi / 2, 0.37)]
    for theta, phi in points:
        c, _, _ = coefficients(771, profile, np.array([theta]))
        value = np.polynomial.polynomial.polyval(np.exp(1j * phi), c[0])
        independent = decimal_check(771, profile, theta, phi)
        precise = complex(float(independent["real"]), float(independent["imag"]))
        absolute = abs(value - precise)
        relative = absolute / max(abs(precise), 1e-300)
        check = {"n": 771, "theta": theta, "phi": phi,
                 "float_value": {"real": float(value.real), "imag": float(value.imag)},
                 "decimal_60_digit_value": independent, "absolute_discrepancy": absolute,
                 "relative_discrepancy": relative, "required_relative_discrepancy": 1e-6}
        verification["point_checks"].append(check)
        if relative > 1e-6:
            verification["failures"].append(f"point relative discrepancy >1e-6 at theta={theta}")
        print(f"60-digit n=771 check theta={theta:.6g}: relative discrepancy {relative:.3g}, required <=1e-6", flush=True)
        data["verification"] = verification
        OUT.write_text(json.dumps(data, indent=2) + "\n")
    all_checks = []
    for family in data["families"]:
        for grid in family["grids"]:
            v = np.array(grid["spatial_log_means"])
            grid["positive_weighted_log_contribution"] = float(np.maximum(v, 0).mean())
            grid["negative_weighted_log_contribution"] = float(np.minimum(v, 0).mean())
            grid["minimum_spatial_log_mean"] = float(min(v))
            grid["maximum_spatial_log_mean"] = float(max(v))
            all_checks.append({"n": family["n"], "angular_samples": len(v),
                               "all_finite": bool(np.isfinite(v).all()),
                               "arc_complement_sum_error": abs(grid["approximate_A"]
                                   - grid["test_arc_weighted_log_contribution"]
                                   - grid["complement_weighted_log_contribution"]),
                               "positive_negative_sum_error": abs(grid["approximate_A"]
                                   - grid["positive_weighted_log_contribution"]
                                   - grid["negative_weighted_log_contribution"])})
            root = grid.get("complete_spatial_root_check")
            if root and (root["max_relative_root_residual"] > 1e-7
                         or root["max_two_root_formula_discrepancy"] > 1e-7):
                verification["failures"].append(f"root check exceeds 1e-7 at n={family['n']}")
        last = family["grids"][-1]
        print(f"n={family['n']}: A/n~{last['approximate_A_over_n']:.8g}; positive~{last['positive_weighted_log_contribution']:.6g}; "
              f"negative~{last['negative_weighted_log_contribution']:.6g}", flush=True)
    verification["all_sampled_mean_checks"] = all_checks
    for check in all_checks:
        if not check["all_finite"] or max(check["arc_complement_sum_error"], check["positive_negative_sum_error"]) > 1e-12:
            verification["failures"].append(f"mean accounting check at n={check['n']}")
    data["verification"] = verification
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Last angular/spatial refinement difference: {verification['last_mean_refinement_difference']:.6g}; "
          f"diagnostic failures: {data['diagnostic_failures']}; verification failures: {verification['failures']}")
    print(f"Full diagnostic artifact: {OUT}")


def scalar_probe():
    data = json.loads(OUT.read_text())
    rec = data["profiles"][-1]
    profile = dict(zip(rec["indices"], rec["shifts"]))
    grid = data["families"][-1]["grids"][1]
    c, _, _ = coefficients(771, profile, np.array(grid["theta"]))
    logs = np.log(abs(c[:, 0]))
    data["verification"]["scalar_lower_bound_probe"] = {
        "n": 771, "angular_samples": len(logs), "theta": grid["theta"],
        "all_scalar_log_magnitudes": logs.tolist(),
        "approximate_scalar_log_mean": float(logs.mean()),
        "approximate_scalar_log_mean_over_n": float(logs.mean() / 771),
        "all_finite": bool(np.isfinite(logs).all()),
        "qualification": "Diagnostic for L666's existing pointwise Jensen lower bound only; no asymptotic scalar or full-mean estimate.",
    }
    OUT.write_text(json.dumps(data, indent=2) + "\n")
    print(f"Scalar probe at n=771: mean~{logs.mean():.9g}, mean/n~{logs.mean()/771:.9g}; "
          f"full mean on same angular grid~{grid['approximate_A']:.9g}; finite={bool(np.isfinite(logs).all())}")
    print(f"Full diagnostic artifact: {OUT}")


if __name__ == "__main__":
    if "--scalar-probe" in sys.argv:
        scalar_probe()
    elif "--verify" in sys.argv:
        verify()
    else:
        main()
