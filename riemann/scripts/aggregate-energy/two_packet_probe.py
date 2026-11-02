#!/usr/bin/env python3
"""Diagnostic only: finite sampling of the approved two-packet family.

Run from riemann with python3 scripts/aggregate-energy/two_packet_probe.py.
Floating-point results do not certify a sign or a universal inequality.
"""
import json
from pathlib import Path

import numpy as np


def main():
    depths = np.unique(np.r_[0.0, np.geomspace(1e-5, 0.1, 36),
                             np.linspace(0.1, 2.0, 153)])
    spacings = np.unique(np.r_[np.geomspace(1e-5, 0.1, 30),
                               np.linspace(0.1, 4.0, 781), 1., 2., 3., 4.])
    u, v = depths[:, None], depths[None, :]
    h_u = np.sinc(2j * u).real ** 2 - 1
    h_v = np.sinc(2j * v).real ** 2 - 1
    runs = []
    # Swapping the packets covers (m,n)=(2,1); m=n=2 scales m=n=1.
    for m, n in ((1, 1), (1, 2)):
        best = None
        negative_count = 0
        near_zero_count = 0
        for a in spacings:
            cross = (np.sinc(a + 1j * (u - v)) ** 2
                     + np.sinc(a + 1j * (u + v)) ** 2).real
            defect = 2 * m*m * h_u + 2 * n*n * h_v + 4*m*n * cross
            scale = 1 + 2*m*m*np.abs(h_u) + 2*n*n*np.abs(h_v) + 4*m*n*np.abs(cross)
            negative_count += int(np.sum(defect < -1e-11 * scale))
            near_zero_count += int(np.sum(np.abs(defect) <= 1e-11 * scale))
            # Normalize away the exact depth-zero/integer-spacing equalities.
            denominator = u*u + v*v + float(np.sinc(a))**2
            mask = denominator > 1e-9
            normalized = np.where(mask, defect / np.maximum(denominator, 1e-300), np.inf)
            index = np.unravel_index(int(np.argmin(normalized)), normalized.shape)
            value = float(normalized[index])
            if best is None or value < best['normalized_defect']:
                best = {'a': float(a), 'u': float(u[index[0], 0]),
                        'v': float(v[0, index[1]]), 'm': m, 'n': n,
                        'defect': float(defect[index]), 'M': 4*m*m+4*n*n,
                        'normalized_defect': value}
        runs.append({'m': m, 'n': n, 'evaluated_points': len(depths)**2*len(spacings),
                     'negative_count_with_tolerance': negative_count,
                     'near_zero_count_with_tolerance': near_zero_count,
                     'minimum_normalized_sample': best})
    certificate = {
        'kind': 'floating-point diagnostic, not a rigorous certificate',
        'required': 'E-M >= 0 at every allowed parameter, or one rigorous E-M < 0 witness',
        'depth_grid': depths.tolist(), 'spacing_grid': spacings.tolist(),
        'negative_detection_relative_tolerance': 1e-11,
        'runs': runs, 'unresolved': ['unsampled parameters', 'floating-point rounding',
                                    'universal two-packet sign', 'general finite multiset claim']}
    path = Path(__file__).with_name('two-packet-probe.json')
    path.write_text(json.dumps(certificate, indent=2) + '\n')
    for run in runs:
        print(json.dumps(run))
    print('Required: a proof over the full family or a rigorous strict negative witness.')
    print('Diagnostic only; certificate:', path)


if __name__ == '__main__':
    main()
