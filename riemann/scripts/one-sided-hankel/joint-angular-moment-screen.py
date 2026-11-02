"""Diagnostic only: sampled joint moments, no interval/asymptotic certificate."""
import json
from pathlib import Path

import numpy as np

X, R = -1.25, 1.375
U = R * R
NANGLE = 1024
angles = np.arange(NANGLE) * (2 * np.pi / NANGLE)
u = np.exp(1j * angles)
records = []
for n in (51, 99, 195, 387):
    m = n // 3
    for radius in (0.2, 0.3, 0.4, 0.5, 0.54):
        ys = radius * np.cos((2 * np.arange(m) + 1) * np.pi / (2 * m))
        ys[m // 2] = 0
        aa = X + 1j * ys
        weights = np.broadcast_to((X / aa)[:, None], (m, NANGLE)).copy()
        for j in range(1, n):
            t = j / n
            weights *= (X - t * u) / (aa[:, None] - t * u)
            weights *= (U * u - t * aa[:, None]) / (U * u - t * X)
        spatial = (aa[:, None] / R) ** np.arange(m)[None, :] / R
        response = weights.T @ spatial
        energy_by_angle = np.sum(np.abs(response) ** 2, axis=1)
        diagonal_by_angle = np.sum(
            np.abs(weights) ** 2 / (U - np.abs(aa[:, None]) ** 2), axis=0
        )
        energy = float(np.mean(energy_by_angle))
        diagonal = float(np.mean(diagonal_by_angle))
        records.append({
            "n": n, "M": m, "radius": radius,
            "sampled_S_n": energy, "sampled_D_single_n": diagonal,
            "sampled_S_over_D": energy / diagonal,
            "apparent_squared_loss_rate": float(np.log(diagonal / energy) / n),
            "required_squared_loss_rate": 1 / 16,
            "log_scaled_target_ratio": float(n / 16 + np.log(energy / diagonal)),
            "log_S_per_n": float(np.log(energy) / n),
            "log_D_per_n": float(np.log(diagonal) / n),
            "phi_max_S": float(angles[np.argmax(energy_by_angle)]),
            "phi_max_D": float(angles[np.argmax(diagonal_by_angle)]),
            "maximum_weight_modulus": float(np.max(np.abs(weights))),
            "angular_energy": energy_by_angle.tolist(),
            "angular_diagonal": diagonal_by_angle.tolist(),
        })
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps({
    "status": "NONRIGOROUS_SCREEN_ONLY", "angular_samples": NANGLE,
    "required_squared_loss_rate": 1 / 16, "records": records,
    "limitations": [
        "No floating-point enclosure; cancellation may destroy relative accuracy.",
        "No enclosure of angular quadrature error.",
        "Every first-M spatial coefficient is included; no spatial tail claim.",
        "Finite samples prove neither the uniform bound nor a countersequence.",
    ],
}, indent=2) + '\n')
for n in (51, 99, 195, 387):
    row = max((r for r in records if r['n'] == n),
              key=lambda r: r['apparent_squared_loss_rate'])
    print('NONRIGOROUS', {k: row[k] for k in (
        'n', 'radius', 'apparent_squared_loss_rate',
        'required_squared_loss_rate', 'log_scaled_target_ratio')})
print('No certified conclusion; full diagnostic:', output)
