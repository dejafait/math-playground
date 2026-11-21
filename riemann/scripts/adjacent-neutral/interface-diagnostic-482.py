#!/usr/bin/env python3
"""Floating-point locator for the fixed neutral adjacent-cell question.

This is not an enclosure, an upper bound, or a smooth-witness certificate.
All eigenvalues and approximate moment residuals are saved in the JSON.
The diagnostic uses polynomial form tests and removes two quadrature
moment directions. Exact neutrality and smoothing require separate proof.
"""
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss, legvander


ELL = np.log(3.0) / 2
D = np.log(2.0)
A = D / np.sqrt(2.0)
GAMMA = 0.577215664901532860606512090082402431


def basis(x, degree):
    return legvander(2 * x / ELL - 1, degree) * np.sqrt(
        (2 * np.arange(degree + 1) + 1) / ELL
    )


def run(degree, order):
    z, w = leggauss(order)
    x, w = (z + 1) * ELL / 2, w * ELL / 2
    b = basis(x, degree)
    wb = w[:, None] * b
    v = -GAMMA - np.log(2 * np.pi) - np.log(x * (ELL - x)) / 2
    harmonic = np.r_[0.0, np.cumsum(1 / np.arange(1, degree + 1))]
    energy = b.T @ (w[:, None] * v[:, None] * b) + np.diag(harmonic)
    # k(u)-1/u has the continuous value 1/2 at zero.
    dist = np.abs(x[:, None] - x[None, :])
    np.fill_diagonal(dist, 1.0)
    regular = 2 * np.exp(-dist / 2) / (-np.expm1(-2 * dist)) - 1 / dist
    np.fill_diagonal(regular, 0.5)
    energy -= (wb.T @ regular @ wb) / 2
    # Remove the slowest response exactly at the formula level. The
    # polynomial projection below is only floating-point neutral.
    summed = x[:, None] + x[None, :]
    hankel = np.exp(-2.5 * summed) / (-np.expm1(-2 * summed))
    cross_cont = wb.T @ hankel @ wb
    lo, hi = D - ELL, ELL
    s, ws = lo + (z + 1) * (hi - lo) / 2, w * (hi - lo) / ELL
    cross_prime = A * basis(s, degree).T @ (
        ws[:, None] * basis(D - s, degree)
    )
    moments = np.vstack((np.exp(x / 2) @ wb, np.exp(-x / 2) @ wb))
    q, _ = np.linalg.qr(moments.T, mode="complete")
    neutral = q[:, 2:]
    en = neutral.T @ energy @ neutral
    cn = neutral.T @ cross_cont @ neutral
    pn = neutral.T @ cross_prime @ neutral
    ev, u = np.linalg.eigh(en)
    invroot = (u * (1 / np.sqrt(ev))) @ u.T
    rel = invroot @ (cn + pn) @ invroot
    vals, vecs = np.linalg.eigh((rel + rel.T) / 2)
    minus_values = np.linalg.eigvalsh(en - 2 * (cn + pn))
    plus_values = np.linalg.eigvalsh(en + 2 * (cn + pn))
    index = int(np.argmax(np.abs(vals)))
    witness = neutral @ invroot @ vecs[:, index]
    energy_value = float(witness @ energy @ witness)
    continuous_value = float(witness @ cross_cont @ witness)
    prime_value = float(witness @ cross_prime @ witness)
    return {
        "degree": degree,
        "quadrature_order": order,
        "energy_eigenvalues": ev.tolist(),
        "relative_eigenvalues": vals.tolist(),
        "minus_form_eigenvalues": minus_values.tolist(),
        "plus_form_eigenvalues": plus_values.tolist(),
        "minimum_half_test_L2_margin": float(min(minus_values[0], plus_values[0])),
        "largest_absolute_ratio": float(abs(vals[index])),
        "signed_ratio": float(vals[index]),
        "required_upper_bound": 0.5,
        "witness_legendre_coefficients": witness.tolist(),
        "witness_energy": energy_value,
        "witness_continuous_pairing": continuous_value,
        "witness_prime_pairing": prime_value,
        "quadrature_moment_residuals": (moments @ witness).tolist(),
        "certified": False,
        "limitations": [
            "Floating-point quadrature has no rigorous error enclosure.",
            "Finite subspaces cannot certify a uniform upper bound.",
            "Moment projection is numerical; polynomial test is not compactly smooth.",
        ],
    }


def main():
    results = [run(n, m) for n, m in
               ((8, 192), (16, 256), (32, 384), (64, 512), (64, 1024), (128, 1024))]
    output = Path(__file__).with_suffix(".json")
    record = {
        "task": "fixed adjacent neutral beta_1 diagnostic",
        "ell": float(ELL),
        "prime_delay": float(D),
        "required_strict_upper_threshold": 0.5,
        "certified": False,
        "runs": results,
    }
    output.write_text(json.dumps(record, indent=2) + "\n")
    for result in results:
        print(f"degree={result['degree']} order={result['quadrature_order']} "
              f"diagnostic ratio={result['largest_absolute_ratio']:.12g} "
              f"half-test L2 margin={result['minimum_half_test_L2_margin']:.12g} "
              f"required uniform bound<0.5 and margin>0; certified=False")
    print("Failures: no enclosure, exact moment certificate, smooth transfer, or all-space bound.")
    print(f"Full diagnostic: {output}")


if __name__ == "__main__":
    main()
