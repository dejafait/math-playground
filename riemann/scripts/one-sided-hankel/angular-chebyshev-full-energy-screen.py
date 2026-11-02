"""Diagnostic only: no quadrature, floating-point, or tail certificate."""
import json
from pathlib import Path

import numpy as np

X, R = -1.25, 1.375
U = R * R
NANGLE, NSPATIAL = 2048, 256
u = np.exp(2j * np.pi * np.arange(NANGLE) / NANGLE)
records = []
for n in (51, 99, 195, 387):
    m = n // 3
    radii = ((0.1, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5)
             if n < 387 else (0.24, 0.27, 0.28, 0.29, 0.30, 0.31, 0.32, 0.34))
    for radius in radii:
        ys = radius * np.cos((2*np.arange(m)+1)*np.pi/(2*m))
        ys[m // 2] = 0.0
        aa = X + 1j*ys
        w = np.broadcast_to((X/aa)[:, None], (m, NANGLE)).copy()
        for j in range(1, n):
            t = j/n
            w *= (X-t*u)/(aa[:, None]-t*u)
            w *= (U*u-t*aa[:, None])/(U*u-t*X)
        spatial = (aa[:, None]/R)**np.arange(NSPATIAL)[None, :]/R
        response = w.T @ spatial
        point_energy = np.sum(abs(response)**2 *
                              (np.arange(NSPATIAL)+1)[None, :], axis=1)
        energy = float(np.mean(point_energy))
        record = {
            "n": n, "m": m, "radius": radius,
            "truncated_sampled_hs_energy": energy,
            "root_energy": float(np.sqrt(energy)),
            "apparent_root_rate": float(-np.log(energy)/(2*n)),
            "required_root_rate": 1/32,
            "sampled_constant_input_energy": float(np.mean(np.sum(abs(response)**2, axis=1))),
            "theta_max_energy_index": int(np.argmax(point_energy)),
            "maximum_point_energy": float(np.max(point_energy)),
            "negative_real_grid_point_energy": float(point_energy[NANGLE//2]),
            "maximum_abs_weight": float(np.max(abs(w))),
            "minimum_point_energy": float(np.min(point_energy)),
        }
        records.append(record)
endpoint_records = []
t_mid = (np.arange(8192)+0.5)/8192
for radius in (0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5):
    a = X + 1j*radius
    gains = []
    for angular_u in (1, -1, 1j):
        gain = np.log(abs((a-t_mid*angular_u)/(X-t_mid*angular_u)
                          *(U*angular_u-t_mid*X)/(U*angular_u-t_mid*a)))
        gains.append({"angular_u": str(angular_u),
                      "sampled_endpoint_log_gain": float(np.mean(gain))})
    endpoint_records.append({"radius": radius, "gains": gains})
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps({
    "status": "NONRIGOROUS_SCREEN_ONLY",
    "angular_samples": NANGLE, "spatial_modes": NSPATIAL,
    "records": records,
    "endpoint_diagnostics": endpoint_records,
    "endpoint_midpoint_samples": 8192,
    "negative_ray_phase_derivative_diagnostic":
        float(np.mean(1/(-X-t_mid)+t_mid/(U+X*t_mid))),
    "limitations": ["No rounding enclosure.", "No angular quadrature enclosure.",
                    "No spatial tail enclosure; truncation is not an upper bound.",
                    "Finite values do not certify an asymptotic rate."],
}, indent=2)+'\n')
print('NONRIGOROUS SCREEN ONLY; required root rate > 0.03125')
for n in (51, 99, 195, 387):
    selected = [r for r in records if r['n'] == n]
    best = max(selected, key=lambda r: r['apparent_root_rate'])
    print('n', n, 'best sampled radius', best['radius'],
          'apparent root rate', best['apparent_root_rate'])
print('No certificate; full diagnostics:', output)
