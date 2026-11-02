"""Outer-half input diagnostic only; no rounding/quadrature/tail enclosure."""

import json
from pathlib import Path

import numpy as np

X, R = -1.25, 1.375
U = R * R
NANGLE, NSPATIAL = 1024, 192
angles = 2 * np.pi * np.arange(NANGLE) / NANGLE
us = np.exp(1j * angles)
records = []
for n in (51, 99, 195):
    m, k = n // 3, (n + 1) // 2
    for radius in (0.3, 0.4, 0.5, 0.54):
        ys = radius * np.cos((2 * np.arange(m) + 1) * np.pi / (2 * m))
        ys[m // 2] = 0.0
        aa = X + 1j * ys
        weights = np.broadcast_to((X / aa)[:, None], (m, NANGLE)).copy()
        for j in range(1, k):
            t = j / n
            weights *= (X - t * us) / (aa[:, None] - t * us)
            weights *= (U * us - t * aa[:, None]) / (U * us - t * X)
        outer = np.ones(NANGLE, dtype=complex)
        for j in range(k, n):
            t = j / n
            outer *= R * (X - t * us) / (U - t * np.conjugate(us) * X)
        weights *= outer
        spatial = (aa[:, None] / R) ** np.arange(NSPATIAL)[None, :] / R
        response = weights.T @ spatial
        energies = np.sum(abs(response) ** 2, axis=1)
        energy = float(np.mean(energies))
        records.append({
            "n": n, "m": m, "radius": radius,
            "sampled_truncated_response_energy": energy,
            "root_energy": float(np.sqrt(energy)),
            "apparent_root_rate": float(-np.log(energy) / (2 * n)),
            "required_root_rate": 1 / 32,
            "maximum_point_energy": float(np.max(energies)),
            "maximum_point_angle": float(angles[int(np.argmax(energies))]),
            "maximum_abs_weight": float(np.max(abs(weights))),
        })

# Endpoint exponents for a possible Chebyshev contour argument.
nsamples = 4096
ts = (np.arange(nsamples) + 0.5) / nsamples
low, outer_ts = ts[:nsamples // 2], ts[nsamples // 2:]
endpoint_records = []
for radius in (0.3, 0.4, 0.5, 0.54):
    vals = []
    for u in us:
        bx = R * (X - outer_ts * u) / (U - outer_ts * np.conjugate(u) * X)
        outer_rate = -float(np.sum(np.log(abs(bx))) / nsamples)
        a = X + 1j * radius
        ratio = (a - low * u) / (X - low * u) * (U * u - low * X) / (U * u - low * a)
        gain = float(np.sum(np.log(abs(ratio))) / nsamples)
        vals.append(outer_rate + gain)
    endpoint_records.append({
        "radius": radius, "minimum_sampled_endpoint_rate": min(vals),
        "minimizing_sampled_angle": float(angles[int(np.argmin(vals))]),
        "positive_ray_endpoint_rate": vals[0],
    })

out = Path(__file__).with_suffix('.json')
pair_records = []
half_plane_records = []
radius, width = 0.54, 0.065
vertical = np.sqrt(radius * radius + width * width)
ellipse_angle = np.linspace(0, 2 * np.pi, 513)
vs = X + width * np.cos(ellipse_angle) + 1j * vertical * np.sin(ellipse_angle)
for t in np.linspace(0, 0.5, 11):
    u = us[:, None]
    v = vs[None, :]
    low_ratio = (X - t * u) / (v - t * u) * (U - t * np.conjugate(u) * v) / (U - t * np.conjugate(u) * X)
    outer_t = t + 0.5
    out_factor = R * (X - outer_t * u) / (U - outer_t * np.conjugate(u) * X)
    pair_records.append({"t": float(t), "sampled_maximum_pair_modulus": float(np.max(abs(low_ratio * out_factor)))})
    cs = np.linspace(-1, 1, 1025)
    h = -X - width
    qa = h * t*t / U + t * cs
    qb = R * (1 - t*t / U)
    qc = h + t * cs
    sigma = 2*qc / (qb + np.sqrt(qb*qb + 4*qa*qc))
    bx = np.sqrt(U*(X*X + t*t - 2*X*t*cs)/(U*U + X*X*t*t - 2*U*X*t*cs))
    bo = np.sqrt(U*(X*X + outer_t*outer_t - 2*X*outer_t*cs)/(U*U + X*X*outer_t*outer_t - 2*U*X*outer_t*cs))
    half_plane_records.append({"t": float(t), "sampled_maximum_half_plane_pair": float(np.max(bx*bo/sigma))})
out.write_text(json.dumps({
    "status": "NONRIGOROUS_DIAGNOSTIC_ONLY",
    "angular_samples": NANGLE, "spatial_modes": NSPATIAL,
    "records": records, "endpoint_records": endpoint_records,
    "ellipse_pair_records": pair_records,
    "half_plane_records": half_plane_records,
    "ellipse_radius": radius, "ellipse_width": width,
    "required_root_rate": 1 / 32,
    "limitations": ["No rounding enclosure.", "No angular quadrature enclosure.",
                    "No spatial tail enclosure; truncation is not an upper bound.",
                    "Finite values and sampled rates do not prove an asymptotic claim."],
}, indent=2) + '\n')
print('NONRIGOROUS DIAGNOSTIC; required rate 0.03125')
for n in (51, 99, 195):
    best = max((v for v in records if v['n'] == n), key=lambda v: v['apparent_root_rate'])
    print('n', n, 'best sampled radius', best['radius'], 'apparent rate', best['apparent_root_rate'])
for v in endpoint_records:
    print('radius', v['radius'], 'sampled minimum endpoint rate', v['minimum_sampled_endpoint_rate'])
print('Largest sampled ellipse pair:', max(v['sampled_maximum_pair_modulus'] for v in pair_records))
print('Largest sampled half-plane pair:', max(v['sampled_maximum_half_plane_pair'] for v in half_plane_records))
print('Full uncertified diagnostic:', out)
