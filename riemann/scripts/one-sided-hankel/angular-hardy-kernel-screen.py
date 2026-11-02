"""Bounded kernel diagnostic. No asymptotic or interval certificate."""

import json
from pathlib import Path

try:
    import mpmath as mp
except ImportError:
    mp = None
import numpy as np

X, R = -1.25, 1.375
U, RADIUS = R * R, 0.54
NANGLE, NKERNEL, NSPATIAL = 128, 64, 512
phis = 2 * np.pi * np.arange(NANGLE) / NANGLE
psis = 2 * np.pi * np.arange(NKERNEL) / NKERNEL
records = []
for n in (51, 99, 195, 387):
    m, s = n // 3, 1 - 1 / n
    ys = RADIUS * np.cos((2 * np.arange(m) + 1) * np.pi / (2 * m))
    ys[m // 2] = 0
    aa = X + 1j * ys
    alpha = aa / R
    spatial = alpha[:, None] ** np.arange(NSPATIAL)[None, :]
    denominators = 1 - s * np.exp(-1j * psis[:, None]) * alpha[None, :]
    per_angle = []
    for ph in phis:
        u = np.exp(1j * ph)
        weights = X / aa
        for j in range(1, n):
            t = j / n
            weights *= (X - t * u) / (aa - t * u)
            weights *= (U * u - t * aa) / (U * u - t * X)
        coeff = (weights / R) @ spatial
        response = (np.sqrt(1-s*s) * weights[None, :] / R / denominators) @ spatial
        energies = np.sum(abs(response) ** 2, axis=1)
        best = int(np.argmax(energies))
        q_energy = float(np.sum(abs(coeff) ** 2))
        per_angle.append({
            "grid_argument": float(ph), "kernel_argument": float(psis[best]),
            "kernel_energy": float(energies[best]), "constant_energy": q_energy,
            "kernel_to_constant_ratio": float(np.sqrt(energies[best] / q_energy)),
            "constant_first_two_energy": float(np.sum(abs(coeff[:2]) ** 2)),
            "peak_spatial_index": int(np.argmax(abs(coeff) ** 2)),
            "maximum_abs_weight": float(np.max(abs(weights))),
        })
    best_index = max(range(NANGLE), key=lambda j: per_angle[j]["kernel_energy"])
    rec = {
        "n": n, "m": m, "radius": RADIUS,
        "sampled_kernel_root_energy": float(np.sqrt(np.mean([a["kernel_energy"] for a in per_angle]))),
        "sampled_constant_root_energy": float(np.sqrt(np.mean([a["constant_energy"] for a in per_angle]))),
        "maximum_angle_index": best_index, "maximum": per_angle[best_index],
        "negative_ray": per_angle[NANGLE // 2], "per_angle": per_angle,
    }
    rec["apparent_kernel_root_rate"] = -np.log(rec["sampled_kernel_root_energy"]) / n
    rec["apparent_constant_root_rate"] = -np.log(rec["sampled_constant_root_energy"]) / n
    records.append(rec)

# Complete finite-pole Gram evaluation at each sampled winner, with 90
# decimal digits. This checks the diagnostic against cancellation/tail
# artifacts there; it is still not an interval or angular certificate.
if mp is not None:
    mp.mp.dps = 90
checks = []
for rec in records if mp is not None else []:
    n, m = rec["n"], rec["m"]
    s = 1 - mp.mpf(1) / n
    x, rr, rad = -mp.mpf(5)/4, mp.mpf(11)/8, mp.mpf(27)/50
    ph = 2*mp.pi*rec["maximum_angle_index"]/NANGLE
    ki = int(round(rec["maximum"]["kernel_argument"]*NKERNEL/(2*np.pi)))
    psi = 2*mp.pi*ki/NKERNEL
    u = mp.exp(1j*ph)
    aa = [x + 1j*rad*mp.cos((2*k+1)*mp.pi/(2*m)) for k in range(m)]
    aa[m//2] = x
    alpha = [a/rr for a in aa]
    cs = []
    for a in aa:
        weight = x/a
        for j in range(1, n):
            t = mp.mpf(j)/n
            weight *= (x-t*u)/(a-t*u)*(rr*rr*u-t*a)/(rr*rr*u-t*x)
        cs.append(weight/rr * mp.sqrt(1-s*s)/(1-s*mp.exp(-1j*psi)*a/rr))
    energy = mp.fsum(cs[i]*mp.conj(cs[j])/(1-alpha[i]*mp.conj(alpha[j]))
                     for i in range(m) for j in range(m))
    approx = rec["maximum"]["kernel_energy"]
    rel = abs(mp.re(energy)-approx)/mp.re(energy)
    checks.append({"n": n, "full_finite_gram_energy": mp.nstr(mp.re(energy), 80),
                   "imaginary_residual": mp.nstr(mp.im(energy), 8),
                   "relative_screen_difference": mp.nstr(rel, 20),
                   "relative_difference_below_1e-8": bool(rel < mp.mpf('1e-8'))})

out = Path(__file__).with_suffix('.json')
failures = (["Optional complete-Gram checks NOT RUN: mpmath is unavailable."]
            if mp is None else [])
failures += [f"n={c['n']}: sampled winner disagrees with high precision by >=1e-8"
            for c in checks if not c["relative_difference_below_1e-8"]]
out.write_text(json.dumps({
    "status": "NONRIGOROUS_DIAGNOSTIC_ONLY", "required_root_rate": 1/32,
    "angular_samples": NANGLE, "kernel_samples": NKERNEL,
    "spatial_modes": NSPATIAL, "high_precision_digits": mp.mp.dps if mp is not None else None,
    "records": records, "winner_checks": checks, "failures": failures,
    "limitations": ["No rounding enclosure, including high precision checks.",
                    "No angular or kernel-optimization enclosure.",
                    "The screen truncates spatial modes; optional Gram checks, when run, do not.",
                    "Finite values do not prove an asymptotic estimate."],
}, indent=2) + '\n')
print('NONRIGOROUS DIAGNOSTIC; required root rate 0.03125')
for rec in records:
    print('n', rec['n'], 'sampled kernel rate', rec['apparent_kernel_root_rate'],
          'constant rate', rec['apparent_constant_root_rate'],
          'maximum grid angle', rec['maximum']['grid_argument'],
          'peak spatial index', rec['maximum']['peak_spatial_index'])
print('Selected full-Gram checks:', len(checks), 'failures:', failures)
print('Full diagnostic:', out)
