"""Exploratory angular screen; no quadrature value is a certificate."""
import json
from pathlib import Path

import numpy as np

X = -1.25
R = 1.375
U = R * R
NTHETA = 8192
u = np.exp(2j * np.pi * np.arange(NTHETA) / NTHETA)


def weights(n, a):
    result = np.full(NTHETA, X / a, dtype=complex)
    for j in range(1, n):
        t = j / n
        result *= (X - t * u) / (a - t * u)
        result *= (U * u - t * a) / (U * u - t * X)
    return result


records = []
worst = None
for n in (6, 9, 12, 24, 48, 96, 192):
    for y in (0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.54):
        a = X + 1j * y
        w = weights(n, a)
        mean_w = np.mean(w)
        k_xa = np.conjugate(mean_w) / (U - X * np.conjugate(a))
        diagonal = np.mean(np.abs(w) ** 2) / (U - abs(a) ** 2)
        # This family has Z={x,a}, residues one and M=2<=n/3.
        energy = 1 / (U - X * X) + diagonal + 2 * k_xa.real
        record = {
            "n": n,
            "ordinate": y,
            "mean_weight": [float(mean_w.real), float(mean_w.imag)],
            "anchor_gram": [float(k_xa.real), float(k_xa.imag)],
            "diagonal": float(diagonal),
            "two_pole_energy": float(energy),
            "required_squared_rate": float(np.exp(-n / 16)),
        }
        records.append(record)
        if worst is None or k_xa.real < worst["anchor_gram"][0]:
            worst = record

family_records = []
for m in (3, 5, 9, 17, 33):
    n = 3 * m
    ordinates = 0.5 * np.cos((2 * np.arange(1, m + 1) - 1) * np.pi / (2 * m))
    ordinates[m // 2] = 0.0
    poles = X + 1j * ordinates
    ws = np.array([weights(n, a) for a in poles])
    spatial = 1 / (U - poles[:, None] * np.conjugate(poles[None, :]))
    gram = (ws @ np.conjugate(ws.T) / NTHETA) * spatial
    energy = np.sum(gram).real
    family_records.append({
        "n": n, "M": m, "ordinates": ordinates.tolist(),
        "energy": float(energy),
        "anchor_diagonal": 1 / (U - X * X),
        "minimum_gram_real_part": float(gram.real.min()),
        "required_squared_rate": float(np.exp(-n / 16)),
    })

output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps({
    "status": "NONRIGOROUS_SCREEN_ONLY",
    "angular_samples": NTHETA,
    "purpose": "Test entrywise real positivity of the constant-input angular Gram.",
    "records": records,
    "minimum_anchor_real_entry": worst,
    "chebyshev_families": family_records,
    "failure_count": sum(r["anchor_gram"][0] < 0 for r in records),
    "limitations": ["No quadrature or floating point error enclosure.",
                    "No uniform lower bound or full-operator countersequence."],
}, indent=2) + "\n")
print("NONRIGOROUS SCREEN ONLY; records:", len(records))
print("negative anchor Gram real parts:", sum(r["anchor_gram"][0] < 0 for r in records))
print("smallest anchor real part:", worst["anchor_gram"][0],
      "at n, ordinate =", worst["n"], worst["ordinate"])
print("required squared exponential rate: 1/16; no bound certified")
print("Chebyshev family screen (n, energy):", [(r["n"], r["energy"]) for r in family_records])
print("full screen:", output)
