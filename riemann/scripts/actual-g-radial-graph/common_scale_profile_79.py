#!/usr/bin/env python3
"""Diagnostic only: one common-scale profile, retaining the full determinant."""

import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def bump(x):
    t = 1 / (1 - x * x)
    e = np.exp(1 - t)
    return e, -2 * x * t * t * e


def evaluate(order):
    t, w = leggauss(order)
    # Split at X=0 for the reference absolute value.
    x = np.concatenate(((t - 1) / 2, (t + 1) / 2))
    wx = np.concatenate((w / 2, w / 2))
    y, wy = t, w
    ex, dex = bump(x)
    ey, dey = bump(y)
    X, Y = x[:, None], y[None, :]
    chi = ex[:, None] * ey[None, :]
    chix = dex[:, None] * ey[None, :]
    chiy = ex[:, None] * dey[None, :]
    a, b = 1.0, -1.0
    p, k, n = 1.0, 1.0, 0.0
    P, T = p + a * chix, a * chiy
    N, K = n + b * Y * chix, k + b * (chi + Y * chiy)
    jac = (1 - 1j * P) * (1 - 1j * K) + T * N
    jac0 = (1 - 1j * p) * (1 - 1j * k)
    q = (((p + 1j) * X + a * chi) / (p + 1j)) * jac / jac0
    weights = wx[:, None] * wy[None, :]
    full = float(np.sum(weights * (np.abs(q) - np.abs(X))))
    cost = float(np.sum(weights * (np.abs(q) - np.sign(X) * q.real)))
    boundary = float((a * a * b / 6) * np.sum(wy * ey**3))
    return {
        "order_per_unsplit_axis": order,
        "full_mass_coefficient": full,
        "nonnegative_phase_cost": cost,
        "signed_interface_coefficient": boundary,
        "identity_residual": full - cost - boundary,
        "sampled_minimum_jacobian_modulus": float(np.min(np.abs(jac))),
        "sampled_maximum_abs_chi_chix": float(np.max(np.abs(chi * chix))),
    }


def main():
    records = [evaluate(n) for n in (64, 128, 256)]
    certificate = {
        "status": "NONRIGOROUS_DIAGNOSTIC_NOT_A_CERTIFICATE_OF_SIGN",
        "profile": "eta(t)=exp(1-1/(1-t^2)); chi=eta(X)*eta(Y); V=(chi,-Y*chi)",
        "conditional_slopes": {"p": 1, "k": 1, "n": 0},
        "required_full_mass_coefficient": "< 0",
        "records": records,
        "limitations": [
            "Floating quadrature and sampled J do not verify any sign or nonvanishing.",
            "No actual stationary graph or slope triple is asserted to exist.",
            "Actual-G remainder and all finite endpoint checks need analytic proof.",
        ],
    }
    path = Path(__file__).with_name("common-scale-profile-diagnostic-79.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")
    last = records[-1]
    print(f"DIAGNOSTIC full coefficient={last['full_mass_coefficient']:.12g}; required < 0")
    print(f"phase cost={last['nonnegative_phase_cost']:.12g}; interface={last['signed_interface_coefficient']:.12g}")
    print("FAIL: no rigorous sign, actual-G remainder or endpoint certificate yet")
    print(f"Full diagnostic: {path}")


if __name__ == "__main__":
    main()
