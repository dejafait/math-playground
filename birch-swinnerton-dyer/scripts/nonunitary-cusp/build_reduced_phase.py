#!/usr/bin/env python3
"""Second fixed schedule: fresh reduced cosine phases and real attenuation.

Original failed certificate is an immutable arithmetic/transport input.
Only real integration is requested; no imaginary enclosure is asserted.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path
from build_certificate import I

HERE = Path(__file__).resolve().parent


def build():
    source = HERE / 'certificate.json'
    data = json.loads(source.read_text())
    assert data['schema'] == 'nonunitary-36-v1'
    c = I(data['bits'])
    pi = data['pi']['interval']
    coefficients = data['coefficients']
    phases, phase_ids, dampings, damping_ids = [], {}, [], {}

    def phase(x):
        x -= (x + F(1, 2)).__floor__()
        if x in phase_ids:
            return phases[phase_ids[x]]['cosine']
        theta = c.scale(pi, 2*x)
        assert max(abs(theta[0]), abs(theta[1])) <= 4*c.D
        square = c.mul(theta, theta)
        term = c.out(1)
        partial = term
        for k in range(1, 41):
            term = c.scale(c.mul(term, square), F(-1, (2*k-1)*(2*k)))
            partial = c.add(partial, term)
        remainder = F(4**81, factorial(81))
        radius = -((-remainder*c.D).__floor__())
        cosine = [partial[0]-radius, partial[1]+radius]
        phase_ids[x] = len(phases)
        phases.append({'phase': str(x), 'theta': theta, 'square': square,
                       'degree': 80, 'polynomial': partial,
                       'remainder': str(remainder), 'radius': radius,
                       'cosine': cosine})
        return cosine

    def damping(y):
        if y in damping_ids:
            return dampings[damping_ids[y]]['q']
        assert 0 < y <= 1
        w = c.scale(pi, -2*y)
        assert -8*c.D <= w[0] <= w[1] < 0
        term = c.out(1)
        partial = term
        for k in range(1, 161):
            term = c.scale(c.mul(term, w), F(1, k))
            partial = c.add(partial, term)
        remainder = F(3**8 * 8**161, factorial(161))
        radius = -((-remainder*c.D).__floor__())
        q = [partial[0]-radius, partial[1]+radius]
        assert 0 < q[0] <= q[1] < c.D
        damping_ids[y] = len(dampings)
        dampings.append({'y': str(y), 'w': w, 'degree': 160,
                         'polynomial': partial, 'remainder': str(remainder),
                         'radius': radius, 'q': q})
        return q

    primitives = []
    for old in data['primitives']:
        x, y, H = F(old['x_reduced']), F(old['y']), old['H']
        q = damping(y)
        power, partial = c.out(1), c.out(0)
        for n in range(1, H+1):
            power = c.mul(power, q)
            cosine = phase(n*x)
            contribution = c.scale(c.mul(power, cosine), F(coefficients[n], n))
            partial = c.add(partial, contribution)
        tail = F(1, 2**((6*H*y).__floor__())) / (6*y)
        radius = -((-tail*c.D).__floor__())
        primitives.append({'x_reduced': str(x), 'y': str(y), 'H': H,
                           'damping_id': damping_ids[y], 'last_power': power,
                           'finite_sum': partial, 'tail_exact': str(tail),
                           'tail_radius': radius,
                           'enclosure': [partial[0]-radius, partial[1]+radius]})
    integral = c.out(0)
    for row in data['transports']:
        i, j = row['primitive_ids']
        integral = c.add(integral, c.sub(primitives[j]['enclosure'], primitives[i]['enclosure']))
    integral = c.scale(integral, F(1, data['h']))
    period = data['period']['total']
    normalized = c.div(integral, period)
    width = F(normalized[1]-normalized[0], c.D)
    data.update(schema='nonunitary-36-reduced-phase-v2',
                input_certificate_sha256=sha256(source.read_bytes()).hexdigest(),
                real_part_only=True, phases=phases, dampings=dampings,
                primitives=primitives,
                result={'integral': integral, 'normalized': normalized,
                        'width': str(width), 'required_width': '1/1048576',
                        'passed': width < F(1, 2**20)})
    return data


if __name__ == '__main__':
    data = build()
    destination = HERE / 'reduced_phase_certificate.json'
    destination.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    result = data['result']
    print('production', 'PASS' if result['passed'] else 'FAIL',
          'T=', data['T'], 'points=', len(data['primitives']),
          'phases=', len(data['phases']), 'dampings=', len(data['dampings']),
          'width=', result['width'], 'required <', result['required_width'],
          'path=', destination)
    raise SystemExit(0 if result['passed'] else 1)
