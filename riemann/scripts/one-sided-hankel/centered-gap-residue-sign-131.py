"""Bounded fixed-j phase diagnostic; not a rigorous sign certificate."""
import cmath
import json
import math
from pathlib import Path

K = 200000
J = 64
mesh = 65536
w = complex(625, 225) / 706
U = 121 / 64
phases = []
for j in range(1, J + 1):
    phase = ((j - 1) * math.pi + math.pi / 2 - cmath.phase(w)
             + j * w.imag / (2 * U) + j * w.imag * math.log(K)
             + math.fsum(cmath.phase(1 - j * w / k)
                         for k in range(1, K + 1)))
    phases.append(math.remainder(phase, 2 * math.pi))
mins = [math.inf] * J
locations = [None] * J
for k in range(mesh):
    theta = 2 * math.pi * k / mesh
    high, low = -math.inf, math.inf
    for j in range(1, J + 1):
        value = math.cos(phases[j - 1] - j * theta)
        high, low = max(high, value), min(low, value)
        mix = min(high, -low)
        if mix < mins[j - 1]:
            mins[j - 1], locations[j - 1] = mix, theta
rows = [{'count': count, 'minimum_sampled_mixed_sign_margin': mins[count - 1],
         'phase_at_minimum': locations[count - 1]} for count in range(2, J + 1)]
out = {'kind': 'floating diagnostic only; no exact profile sampling',
       'K': K, 'J': J, 'mesh': mesh, 'phases': phases, 'rows': rows,
       'required_for_uniform_obstruction': 'rigorous mixed-sign margin > 0',
       'failures': ['infinite-product and floating errors not enclosed',
                    'continuous phase not yet enclosed',
                    'asymptotic transfer requires proof']}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out, indent=2) + '\n')
passing = [row for row in rows if row['minimum_sampled_mixed_sign_margin'] > 0]
print('Diagnostic only; required rigorous margin > 0.')
print('First sampled positive margin:', passing[0] if passing else None)
print('Failures:', '; '.join(out['failures']))
print('Full diagnostic:', path)
