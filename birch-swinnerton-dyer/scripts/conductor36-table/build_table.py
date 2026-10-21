#!/usr/bin/env python3
"""Fixed coupled-table producer. Full finite records; no expected values."""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, lcm
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = 1 << 96
H = 4860


def digest(path):
    h = sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def out(values):
    return [(min(values)*D).__floor__(), -((-max(values)*D).__floor__())]


def mul(a, b):
    v = [x*y for x in a for y in b]
    return [min(v)//D, -((-max(v))//D)]


def scale(a, f):
    # Exact integer numerator/denominator arithmetic, outward at scale D.
    f = F(f)
    v = sorted(x*f.numerator for x in a)
    return [v[0]//f.denominator, -((-v[1])//f.denominator)]


def add(a, b):
    return [a[0]+b[0], a[1]+b[1]]


def phase_key(x):
    return x-(x+F(1, 2)).__floor__()


def matrix_values(values, columns):
    return [sum((v*row[j] for v, row in zip(values, columns)), F(0))
            for j in range(len(columns[0]))]


def build():
    paths = {'geometry': HERE/'coupled_plan.json',
             'tails': HERE/'exponential_plan.json',
             'presentation': HERE/'presentation.json',
             'analytic': HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json',
             'denominator': HERE.parent/'nonunitary-cusp/exact_value_certificate.json'}
    inputs = {name: json.loads(p.read_text()) for name, p in paths.items()}
    geometry, tails, structure, old = [inputs[n] for n in ('geometry', 'tails', 'presentation', 'analytic')]
    assert tails['H'] == H and tails['bits'] == old['bits'] == 96
    assert len(geometry['primitives']) == len(tails['primitives']) == 98
    assert len(old['coefficients']) == H+1
    destination = HERE/'table-data'
    destination.mkdir(exist_ok=True)
    # This new schedule has its own files and never rewrites old evidence.
    pi = old['pi']['interval']
    keys = sorted({phase_key(n*F(p['x_reduced']))
                   for p in geometry['primitives'] for n in range(1, H+1)})
    phase_ids = {x: i for i, x in enumerate(keys)}
    phases = []
    remainder = F(4**81, factorial(81))
    radius = -((-D*remainder).__floor__())
    for x in keys:
        theta = scale(pi, 2*x)
        assert max(map(abs, theta)) <= 4*D
        square = mul(theta, theta)
        term = partial = [D, D]
        trace = []
        for k in range(1, 41):
            term = scale(mul(term, square), F(-1, (2*k-1)*(2*k)))
            partial = add(partial, term)
            trace.append({'k': k, 'term': term, 'partial': partial})
        phases.append({'phase': str(x), 'theta': theta, 'square': square,
                       'degree': 80, 'trace': trace, 'polynomial': partial,
                       'remainder': str(remainder), 'radius': radius,
                       'cosine': [partial[0]-radius, partial[1]+radius]})

    primitives = []
    for i, p in enumerate(geometry['primitives']):
        tail = tails['primitives'][i]
        assert (p['x_reduced'], p['y']) == (tail['x_reduced'], tail['y'])
        attenuation_id = tail['attenuation_id']
        q = tails['attenuation'][attenuation_id]['q']
        assert tails['attenuation'][attenuation_id]['y'] == p['y']
        path = destination/f'point-{i:03d}.jsonl'
        power, partial = [D, D], [0, 0]
        x = F(p['x_reduced'])
        with path.open('w') as stream:
            for n in range(1, H+1):
                power = mul(power, q)
                j = phase_ids[phase_key(n*x)]
                product = mul(power, phases[j]['cosine'])
                contribution = scale(product, F(old['coefficients'][n], n))
                partial = add(partial, contribution)
                stream.write(json.dumps([n, j, power, product, contribution, partial],
                                        separators=(',', ':'))+'\n')
        R = F(tail['tail_bounds'][1])
        r = -((-R*D).__floor__())
        primitives.append({'point_id': i, 'x_reduced': p['x_reduced'], 'y': p['y'],
                           'H': H, 'attenuation_id': attenuation_id,
                           'term_file': path.relative_to(HERE).as_posix(),
                           'term_sha256': digest(path), 'last_power': power,
                           'finite_sum': partial, 'tail_upper': str(R), 'tail_radius': r,
                           'enclosure': [partial[0]-r, partial[1]+r]})
        if (i+1) % 14 == 0:
            print('finite records:', i+1, '/98 points;', (i+1)*H, '/476280 terms', flush=True)

    period = old['period']['total']
    assert period[0] > 0
    rows = []
    for i, g in enumerate(geometry['generators']):
        partial = [0, 0]
        trace = []
        for j, w in g['occurrences']:
            term = scale(primitives[j]['enclosure'], F(w))
            partial = add(partial, term)
            trace.append({'point_id': j, 'weight': w, 'term': term, 'partial': partial})
        quotients = [F(a, b) for a in partial for b in period]
        normalized = out(quotients)
        width = F(normalized[1]-normalized[0], D)
        lower = -((-F(24*normalized[0], D)).__floor__())
        upper = F(24*normalized[1], D).__floor__()
        value = F(lower, 24) if lower == upper else None
        rows.append({'generator_id': i, 'endpoints': g['endpoints'],
                     'occurrence_trace': trace, 'integral': partial,
                     'quotient_endpoints': list(map(str, quotients)),
                     'normalized': normalized, 'width': str(width),
                     'scaled_ceil': lower, 'scaled_floor': upper,
                     'scaled_integer': lower if value is not None else None,
                     'value': str(value) if value is not None else None})
    width_failures = [r['generator_id'] for r in rows if F(r['width']) > F(1, 2**38)]
    isolation_failures = [r['generator_id'] for r in rows if r['value'] is None]
    relations = None
    if not isolation_failures:
        values = [F(r['value']) for r in rows]
        pr = structure['presentation']
        source_images = [sum((a*v for a, v in zip(row, values)), F(0))
                         for row in structure['A']['entries']]
        saturated_images = matrix_values(values, pr['K']['entries'])
        quotient = matrix_values(values, pr['Q']['entries'])
        reconstructed = [sum((a*v for a, v in zip(coord, quotient)), F(0))
                         for coord in pr['generator_coordinates']]
        relations = {'source_images': list(map(str, source_images)),
                     'saturated_images': list(map(str, saturated_images)),
                     'quotient_values': list(map(str, quotient)),
                     'reconstructed': list(map(str, reconstructed)),
                     'denominators': [v.denominator for v in values],
                     'common_denominator': lcm(*(v.denominator for v in values)),
                     'zero_generators': [i for i, v in enumerate(values) if v == 0],
                     'source_failures': [i for i, v in enumerate(source_images) if v],
                     'saturated_failures': [i for i, v in enumerate(saturated_images) if v],
                     'reconstruction_failures': [i for i, (a, b) in enumerate(zip(values, reconstructed)) if a != b]}
    passed = not width_failures and not isolation_failures and relations is not None and all(
        not relations[k] for k in ('source_failures', 'saturated_failures', 'reconstruction_failures'))
    data = {'schema': 'conductor36-coupled-table-v1', 'bits': 96, 'scale': D, 'H': H,
            'input_sha256': {name: digest(path) for name, path in paths.items()},
            'arithmetic_evidence': {key: old[key] for key in
                ('arithmetic', 'pi', 'T', 'point_counts', 'coefficients', 'factorizations', 'period')},
            'clearing_integer': 24, 'infinity_primitive': '0', 'real_part_only': True,
            'phases': phases, 'attenuation': tails['attenuation'], 'primitives': primitives,
            'generators': rows, 'relations': relations,
            'actual': {'points': 98, 'heights': len(tails['attenuation']), 'terms': 98*H,
                       'generators': 72, 'occurrences': sum(len(g['occurrences']) for g in geometry['generators']),
                       'phases': len(phases), 'max_width': str(max(F(r['width']) for r in rows))},
            'required': {'points': 98, 'heights': 16, 'terms': 1000000, 'H': 4860,
                         'generators': 72, 'occurrences': 1316, 'max_width': '1/274877906944'},
            'width_failures': width_failures, 'isolation_failures': isolation_failures,
            'table_complete': passed, 'critical_audit_complete': False}
    path = HERE/'table_certificate.json'
    path.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print('production:', passed, 'actual:', data['actual'], 'required:', data['required'],
          'width failures:', width_failures, 'isolation failures:', isolation_failures,
          'certificate:', path.relative_to(HERE.parent.parent), flush=True)
    return data


if __name__ == '__main__':
    result = build()
    raise SystemExit(0 if result['table_complete'] else 1)
