"""Finite exploratory screen; neither quadrature nor tail is certified."""
import json
from pathlib import Path

import numpy as np

X, R = -1.25, 1.375
U = R * R
NANGLE, NSPATIAL = 4096, 256
u = np.exp(2j * np.pi * np.arange(NANGLE) / NANGLE)
records = []
for m in (3, 5, 9, 17, 33, 65):
    n = 3 * m
    ys = 0.5 * np.cos((2 * np.arange(m) + 1) * np.pi / (2 * m))
    ys[m // 2] = 0.0
    aa = X + 1j * ys
    w = np.broadcast_to((X / aa)[:, None], (m, NANGLE)).copy()
    for j in range(1, n):
        t = j / n
        w *= (X - t * u) / (aa[:, None] - t * u)
        w *= (U * u - t * aa[:, None]) / (U * u - t * X)
    spatial = (aa[:, None] / R) ** np.arange(NSPATIAL)[None, :] / R
    response = w.T @ spatial
    modes = np.fft.fft(response, axis=0) / NANGLE
    zero_energy = float(np.sum(abs(modes[0]) ** 2))
    neg_energy = float(np.sum(abs(modes[NANGLE // 2 + 1:]) ** 2))
    full_energy = float(np.sum(abs(modes) ** 2))
    records.append({
        "n": n, "M": m, "radius": 0.5,
        "zero_energy": zero_energy, "negative_energy": neg_energy,
        "projected_energy": zero_energy + neg_energy,
        "full_constant_energy": full_energy,
        "required_squared_scale": float(np.exp(-n / 16)),
        "max_abs_weight": float(abs(w).max()),
    })
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps({
    "status": "NONRIGOROUS_SCREEN_ONLY", "angular_samples": NANGLE,
    "spatial_modes_retained": NSPATIAL, "records": records,
    "limitations": ["No rounding, angular aliasing or spatial-tail enclosure.",
                    "Finite families do not prove a uniform bound or countersequence."]
}, indent=2) + '\n')
print('NONRIGOROUS SCREEN ONLY; (n, projected energy, full energy, required scale):')
for r in records:
    print(r['n'], r['projected_energy'], r['full_constant_energy'], r['required_squared_scale'])
print('Certificate: none. Full exploratory output:', output)
