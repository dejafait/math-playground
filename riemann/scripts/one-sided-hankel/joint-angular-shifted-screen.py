"""Diagnostic of the same joint target; no certified bounds."""
import json
from pathlib import Path

import numpy as np

X, R = -1.25, 1.375
U = R * R
NANGLE = 1024
angles = np.arange(NANGLE) * (2 * np.pi / NANGLE)
u = np.exp(1j * angles)
records = []
for n in (99, 195, 387):
    m = n // 3 - 1
    for center in (0.05, 0.1, 0.2, 0.3, 0.4):
        for radius in (0.05, 0.1, 0.2, 0.3, 0.4):
            if center + radius > 0.54:
                continue
            ys = center + radius * np.cos((2 * np.arange(m) + 1) * np.pi / (2 * m))
            aa = X + 1j * np.concatenate(([0], ys))
            mass = len(aa)
            weights = np.broadcast_to((X / aa)[:, None], (mass, NANGLE)).copy()
            for j in range(1, n):
                t = j / n
                weights *= (X - t * u) / (aa[:, None] - t * u)
                weights *= (U * u - t * aa[:, None]) / (U * u - t * X)
            spatial = (aa[:, None] / R) ** np.arange(mass)[None, :] / R
            response = weights.T @ spatial
            e_angles = np.sum(np.abs(response) ** 2, axis=1)
            d_angles = np.sum(
                np.abs(weights) ** 2 / (U - np.abs(aa[:, None]) ** 2), axis=0
            )
            energy, diagonal = float(np.mean(e_angles)), float(np.mean(d_angles))
            records.append({
                "n": n, "M": mass, "center": center, "radius": radius,
                "sampled_S_n": energy, "sampled_D_single_n": diagonal,
                "sampled_S_over_D": energy / diagonal,
                "apparent_squared_loss_rate": float(np.log(diagonal / energy) / n),
                "required_squared_loss_rate": 1 / 16,
                "log_scaled_target_ratio": float(n / 16 + np.log(energy / diagonal)),
                "log_S_per_n": float(np.log(energy) / n),
                "log_D_per_n": float(np.log(diagonal) / n),
                "phi_max_S": float(angles[np.argmax(e_angles)]),
                "phi_max_D": float(angles[np.argmax(d_angles)]),
                "maximum_weight_modulus": float(np.max(np.abs(weights))),
                "angular_energy": e_angles.tolist(),
                "angular_diagonal": d_angles.tolist(),
            })
best = []
for n in (99, 195, 387):
    index, row = max(((i, r) for i, r in enumerate(records) if r['n'] == n),
                     key=lambda ir: ir[1]['apparent_squared_loss_rate'])
    summary = {k: row[k] for k in (
        'n', 'center', 'radius', 'apparent_squared_loss_rate',
        'required_squared_loss_rate', 'log_scaled_target_ratio')}
    summary['record_index'] = index
    best.append(summary)
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps({
    "status": "NONRIGOROUS_SCREEN_ONLY", "angular_samples": NANGLE,
    "best_sampled_cases": best, "records": records,
    "limitations": [
        "No floating-point or angular quadrature enclosure.",
        "Cancellation may destroy relative accuracy.",
        "All first-M spatial moments are included; no full-energy upper bound.",
        "Finite samples do not certify any asymptotic or countersequence.",
    ],
}, indent=2) + '\n')
for row in best:
    print('NONRIGOROUS', row)
print('No certified conclusion; full diagnostic:', output)
