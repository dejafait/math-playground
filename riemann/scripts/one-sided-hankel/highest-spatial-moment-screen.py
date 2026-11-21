#!/usr/bin/env python3
"""Diagnostic only: exact finite products, sampled angles, zero displacements."""
import json
from pathlib import Path
import numpy as np


def main():
    dtype = np.clongdouble
    real = np.longdouble
    pi = np.arccos(real(-1))
    R, U, x = real(11) / 8, real(121) / 64, real(-5) / 4
    count = 1024
    rows = []
    for q in [1, 2, 4, 8, 16, 32, 64]:
        n, M = 12 * q + 3, 4 * q + 1
        y = real(27) / (10 * n) * (np.arange(-2*q, 2*q, dtype=real) + real('0.5'))
        a = np.concatenate((np.array([x], dtype=dtype), x + 1j * y))
        k = M - 1
        theta = np.arange(count, dtype=real) * (2 * pi / count)
        observations = []
        for begin in range(0, count, 16):
            th = theta[begin:begin+16]
            u = np.exp(1j * th)[:, None]
            logW = np.broadcast_to(np.log(x / a), (len(th), M)).copy()
            for j in range(1, n):
                t = real(j) / n
                logW += np.log((x-t*u)/(a[None, :]-t*u))
                logW += np.log((U*u-t*a[None, :])/(U*u-t*x))
            moment_log = logW + k * np.log(a[None, :] / R)
            scale = np.max(moment_log.real, axis=1)
            total = np.sum(np.exp(moment_log - scale[:, None]), axis=1) / R
            logabs = scale + np.log(np.abs(total))
            dscale = np.max(2 * logW.real, axis=1)
            diag_log = dscale + np.log(np.sum(
                np.exp(2 * logW.real - dscale[:, None]) / (U - np.abs(a)**2), axis=1))
            for j in range(len(th)):
                observations.append({
                    'theta': float(th[j]), 'log_abs_moment': float(logabs[j]),
                    'log_diagonal': float(diag_log[j]),
                    'max_log_abs_weight': float(np.max(logW[j].real)),
                    'log_absolute_term_sum': float(scale[j] + np.log(np.sum(
                        np.exp(moment_log[j].real-scale[j])) / R)),
                })
        dlogs = np.array([z['log_diagonal'] for z in observations], dtype=real)
        ds = np.max(dlogs)
        logD = ds + np.log(np.mean(np.exp(dlogs - ds)))
        peak = max(observations, key=lambda z: z['log_abs_moment'])
        log_required = np.log(real(n)) - real(n) / 32 + logD / 2
        row = {
            'n': n, 'q': q, 'M': M, 'k': k, 'all_shifts': 0,
            'sample_count': count, 'log_D_sample_mean': float(logD),
            'peak': peak, 'log_required_C_1': float(log_required),
            'log_sampled_ratio': float(peak['log_abs_moment'] - log_required),
            'observations': observations,
        }
        rows.append(row)
        print(f"n={n}: sampled log max={peak['log_abs_moment']:.9g}, "
              f"required(C=1)={float(log_required):.9g}, "
              f"log ratio={row['log_sampled_ratio']:.9g}, theta={peak['theta']:.9g}", flush=True)
    output = Path(__file__).with_suffix('.json')
    result = {'status': 'FLOATING DIAGNOSTIC ONLY', 'failures': [],
              'limitations': ['No interval enclosures or angular supremum certificate.',
                              'D is a sampled mean.',
                              'Cancellation error is not bounded.',
                              'Finite data decide neither uniform constant nor onset.'],
              'rows': rows}
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(f"diagnostic limitations retained; full output: {output}")


if __name__ == '__main__':
    main()
