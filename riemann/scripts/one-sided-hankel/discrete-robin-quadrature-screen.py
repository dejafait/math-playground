"""Exploratory full-product continuum screen, never a proof certificate."""
import json
from pathlib import Path
import numpy as np

d, U, b = 1.25, 121 / 64, 0.45
lam = 10 * np.pi / 27
t, wt = np.polynomial.legendre.leggauss(96)
t, wt = (t + 1) / 2, wt / 2
angles = np.linspace(0, np.pi, 721)
u = np.exp(1j * angles)


def exponent(s, ys):
    best = (-float('inf'), None)
    for y in ys:
        a = -d + s + 1j * y
        factors = ((-d - t[:, None] * u) / (a - t[:, None] * u)
                   * (U * u - t[:, None] * a) / (U * u + t[:, None] * d))
        vals = wt @ np.log(np.abs(factors)) - 2 * lam * max(s, 0)
        idx = int(np.argmax(vals))
        if vals[idx] > best[0]:
            best = (float(vals[idx]), dict(s=float(s), y=float(y),
                                          angle=float(angles[idx])))
    return dict(sample_maximum=best[0], witness=best[1])


right = [exponent(s, np.linspace(-b, b, 181))
         for s in np.linspace(0.03, 0.12, 19)]
top = [exponent(s, [b, -b]) for s in np.linspace(-0.125, 0.12, 99)]
left = exponent(-0.125, np.linspace(-b, b, 181))
best = min(right, key=lambda row: row['sample_maximum'])
report = dict(kind='uncertified floating design screen', required_upper=-0.01,
              right=right, top=top, left=left, best_right=best,
              failures=['Not a continuous bound or finite-n certificate.'],
              scope='One direct Robin residue kernel, not arbitrary weights.')
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(report, indent=2) + '\n')
print('Exploratory best right exponent:', best)
print('Required: < -0.01; left:', left['sample_maximum'])
print('Top maximum:', max(row['sample_maximum'] for row in top))
print('Not verified; full screen:', out)
