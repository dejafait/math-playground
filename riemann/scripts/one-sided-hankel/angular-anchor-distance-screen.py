"""Finite floating diagnostic for the approved angular anchor-distance target.

All products and complex coefficients are retained. This is neither a
continuous-circle enclosure nor an asymptotic distance certificate.
"""
import json
from pathlib import Path
import numpy as np

OUT = Path(__file__).with_suffix('.json')


def columns(n, ordinates, count):
    u = np.exp(2j * np.pi * np.arange(count) / count)
    x, U = -1.25, 121 / 64
    t = np.arange(1, n) / n
    answer = np.empty((count, len(ordinates)), complex)
    for k, y in enumerate(ordinates):
        a = x + 1j * y
        factors = ((x - u[:, None] * t) / (a - u[:, None] * t)
                   * (U * u[:, None] - t * a)
                   / (U * u[:, None] - t * x))
        answer[:, k] = (x / a) * np.prod(factors, axis=1)
    return answer


rows, failures = [], []
for q in (1, 2, 4, 8, 16):
    n = 12 * q + 3
    ys = (27 / (10 * n)) * (np.arange(-2 * q, 2 * q) + .5)
    grid = max(2048, 16 * n)
    A = columns(n, ys, grid)
    scale = np.linalg.norm(A, axis=0) / np.sqrt(grid)
    coeff_scaled, _, rank, singular = np.linalg.lstsq(
        A / scale, np.ones(grid), rcond=1e-15)
    coeff = coeff_scaled / scale
    residual = 1 - A @ coeff
    B = columns(n, ys, 2 * grid)
    residual2 = 1 - B @ coeff
    norm1 = float(np.linalg.norm(residual) / np.sqrt(grid))
    norm2 = float(np.linalg.norm(residual2) / np.sqrt(2 * grid))
    disagreement = abs(norm1 - norm2) / max(norm1, norm2)
    if disagreement > 1e-4:
        failures.append(f'n={n}: grid disagreement or roundoff {disagreement:.3g}')
    rows.append(dict(q=q, n=n, displacement='all e_r=0', angles=grid,
                     rank=int(rank), column_count=4*q,
                     sampled_norm=norm1, doubled_grid_norm=norm2,
                     actual_sampled_rate=float(-np.log(norm2)/n),
                     required_rate=.01,
                     excess_over_log_n=float((-np.log(norm2)-n/100)/np.log(n)),
                     singular_values=singular.tolist(),
                     coefficients=[[float(z.real), float(z.imag)] for z in coeff],
                     grid_disagreement=disagreement,
                     max_coefficient=float(np.max(np.abs(coeff)))))
OUT.write_text(json.dumps(dict(status='FLOATING_DIAGNOSTIC_ONLY',
                              failures=failures, rows=rows), indent=2)+'\n')
for r in rows:
    print(f"n={r['n']}: sampled distance <= {r['doubled_grid_norm']:.8g}; "
          f"sampled rate {r['actual_sampled_rate']:.6g}, required .01; "
          f"rank {r['rank']}/{r['column_count']}; "
          f"grid disagreement {r['grid_disagreement']:.3g}")
print('Failures:', failures)
print('Full diagnostic:', OUT)
print('No continuous or asymptotic conclusion is certified.')
