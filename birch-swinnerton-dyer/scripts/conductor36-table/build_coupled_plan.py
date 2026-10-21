#!/usr/bin/env python3
"""Approved T_5 coupled specialization: exact plan only, no analytic sums."""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path

from build_compressed_plan import witness, key, cutoff

HERE = Path(__file__).resolve().parent


def eliminate(matrix):
    a = [list(map(F, row)) for row in matrix]
    nr, nc = len(a), len(a[0])
    e = [[F(i == j) for j in range(nr)] for i in range(nr)]
    pivots = []
    for col in range(nc):
        row = len(pivots)
        candidate = next((j for j in range(row, nr) if a[j][col]), None)
        if candidate is None:
            continue
        a[row], a[candidate] = a[candidate], a[row]
        e[row], e[candidate] = e[candidate], e[row]
        divisor = a[row][col]
        a[row] = [x/divisor for x in a[row]]
        e[row] = [x/divisor for x in e[row]]
        for j in range(nr):
            if j == row:
                continue
            scalar = a[j][col]
            a[j] = [x-scalar*y for x, y in zip(a[j], a[row])]
            e[j] = [x-scalar*y for x, y in zip(e[j], e[row])]
        pivots.append(col)
    return a, e, pivots


def encoded(a):
    return [list(map(str, row)) for row in a]


def build():
    source = HERE/'presentation.json'
    analytic = HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json'
    saved = HERE/'compressed_plan.json'
    pres = json.loads(source.read_text())
    old = json.loads(analytic.read_text())
    previous = json.loads(saved.read_text())
    assert pres['inputs'] == {'N': 36, 'P': []}
    domain = sorted({tuple(e) for pair in pres['endpoints'] for e in pair},
                    key=lambda e: (e[1], abs(e[0]), e[0]))
    reps = list(map(tuple, previous['representatives']))
    assert reps[0] == (1, 0) and len(reps) == 12
    def assign(v):
        matches = [(i, witness(s, v)) for i, s in enumerate(reps)]
        matches = [(i, t) for i, t in matches if t is not None]
        assert len(matches) == 1
        i, t = matches[0]
        return {'endpoint': list(v), 'representative_id': i, 'transport': t}
    assignments = [assign(v) for v in domain]
    # Independent exhaustive target point count at the eligible good prime.
    ell = 5
    points = [[x, y] for x in range(ell) for y in range(ell)
              if (y*y-x*x*x-1) % ell == 0]
    count = 1+len(points); trace = ell+1-count
    assert gcd(ell, 36) == 1 and trace == old['coefficients'][ell]
    closures, adjacency = [], [[0]*12 for _ in reps]
    for i, s in enumerate(reps):
        if s[1] == 0:
            images = [(1, 0)]*6
        else:
            r = F(*s)
            images = [(v.numerator, v.denominator)
                      for v in [5*r]+[(r+j)/5 for j in range(5)]]
        rows = [assign(v) for v in images]
        closures.append({'representative': list(s), 'images': rows})
        for row in rows:
            adjacency[i][row['representative_id']] += 1
    matrix = [[trace*int(i == j)-adjacency[i][j] for j in range(12)] for i in range(12)]
    normalized = matrix+[[int(j == 0) for j in range(12)]]
    reduced, transform, pivots = eliminate(normalized)
    _, inverse_transform, epivots = eliminate(transform)
    assert epivots == list(range(13))
    data = {'schema': 'conductor36-coupled-T5-plan-v1',
            'presentation_sha256': sha256(source.read_bytes()).hexdigest(),
            'audited_analytic_sha256': sha256(analytic.read_bytes()).hexdigest(),
            'saved_compression_sha256': sha256(saved.read_bytes()).hexdigest(),
            'ell': ell, 'point_count': count, 'affine_points': points, 'a_ell': trace,
            'domain': list(map(list, domain)), 'representatives': list(map(list, reps)),
            'assignments': assignments, 'closures': closures, 'adjacency': adjacency,
            'matrix': matrix, 'normalized_matrix': normalized,
            'elimination': {'rank': len(pivots), 'pivots': pivots, 'rref': encoded(reduced),
                            'transform': encoded(transform), 'inverse_transform': encoded(inverse_transform)}}
    if pivots != list(range(12)):
        free = next(j for j in range(12) if j not in pivots)
        kernel = [F(j == free) for j in range(12)]
        for k, p in enumerate(pivots): kernel[p] = -reduced[k][free]
        data['stop'] = {'reason': 'normalized rank deficient', 'kernel': list(map(str, kernel))}
        return data
    # Formal RHS basis: one variable for every nontranslation correction.
    labels = [(i, k) for i, c in enumerate(closures) for k, a in enumerate(c['images'])
              if a['transport']['zero_translation'] is None]
    rhs = [[F(label[0] == i) for label in labels] for i in range(12)]+[[F(0)]*len(labels)]
    transformed_rhs = [[sum((transform[i][k]*rhs[k][j] for k in range(13)), F(0))
                        for j in range(len(labels))] for i in range(13)]
    data['rhs_labels'] = [list(label) for label in labels]
    data['elimination']['transformed_rhs'] = encoded(transformed_rhs)
    if any(transformed_rhs[12]):
        data['stop'] = {'reason': 'formal consistency failed', 'row': 12,
                        'rhs': list(map(str, transformed_rhs[12]))}
        return data
    weights = [row[:12] for row in transform[:12]]
    data['solution_equation_weights'] = encoded(weights)
    all_transports = [a['transport'] for a in assignments]+[
        a['transport'] for c in closures for a in c['images']]
    point_keys = set()
    for t in all_transports:
        t['reduction_shifts'] = [key(t[f])[1] for f in ('tau', 'image')]
        if t['zero_translation'] is None:
            point_keys.update(key(t[f])[0] for f in ('tau', 'image'))
    keys = sorted(point_keys); index = {k: i for i, k in enumerate(keys)}
    for t in all_transports:
        t['primitive_ids'] = [] if t['zero_translation'] is not None else [
            index[key(t[f])[0]] for f in ('tau', 'image')]
    def occurrence(t, weight):
        if t['zero_translation'] is not None or weight == 0: return []
        i, j = t['primitive_ids']
        return [[i, str(-weight)], [j, str(weight)]]
    def representative_occurrences(i, sign):
        return [term for k, c in enumerate(closures) for a in c['images']
                for term in occurrence(a['transport'], sign*weights[i][k])]
    data['representative_occurrences'] = [representative_occurrences(i, F(1)) for i in range(12)]
    assignment_index = {tuple(a['endpoint']): i for i, a in enumerate(assignments)}
    generators = []
    for pair in pres['endpoints']:
        ids, occ = [], []
        for endpoint, sign in zip(pair, (-1, 1)):
            i = assignment_index[tuple(endpoint)]; ids.append(i)
            a = assignments[i]
            occ.extend(occurrence(a['transport'], F(sign)))
            occ.extend(representative_occurrences(a['representative_id'], F(sign)))
        combined = {}
        for j, w in occ: combined[j] = combined.get(j, F(0))+F(w)
        generators.append({'endpoints': pair, 'assignment_ids': ids, 'occurrences': occ,
                           'combined': [[j, str(w)] for j, w in sorted(combined.items()) if w],
                           'absolute_occurrence_weight': str(sum((abs(F(w)) for _, w in occ), F(0)))})
    omega = F(old['period']['total'][0], old['scale'])
    W = max(F(g['absolute_occurrence_weight']) for g in generators)
    budget = F(1, 1 << 38); rho = budget*omega/(2*W)
    primitives = []
    for x, y in keys:
        H = cutoff(y, rho); R = F(1, 1 << (6*H*y).__floor__())/(6*y)
        primitives.append({'x_reduced': str(x), 'y': str(y), 'H': H, 'tail_radius': str(R)})
    for g in generators:
        g['normalized_tail_width'] = str(sum((2*abs(F(w))*F(primitives[j]['tail_radius'])/omega
                                              for j, w in g['occurrences']), F(0)))
    data.update({'omega_lower': str(omega), 'tail_budget': str(budget),
                 'maximum_occurrence_weight': str(W), 'primitive_radius_budget': str(rho),
                 'generators': generators, 'primitives': primitives,
                 'summary': {'generators': len(generators), 'endpoint_occurrences': 144,
                    'distinct_endpoints': len(domain), 'representatives': len(reps),
                    'endpoint_transports': len(assignments), 'closing_transports': 72,
                    'zero_translations': sum(t['zero_translation'] is not None for t in all_transports),
                    'points': len(keys), 'normalized_rank': len(pivots),
                    'max_H': max(p['H'] for p in primitives),
                    'Fourier_terms': sum(p['H'] for p in primitives),
                    'max_normalized_tail_width': str(max(F(g['normalized_tail_width']) for g in generators))}})
    return data


if __name__ == '__main__':
    data = build(); destination = HERE/'coupled_plan.json'
    destination.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print('coupled plan:', data.get('summary', data.get('stop')),
          'required: rank=12, consistency, max_H<=4860; terms<=1000000; width<=2^-38;',
          'certificate=', destination)
