#!/usr/bin/env python3
"""Known-method finite plan only; never evaluate new analytic sums.

Cremona (1997), Prop. 2.2.3 and Wuthrich 1608.06423v2 (11),
with audited L049's oriented closing and complete rational tails.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
N = 36


def bezout(a, m):
    if m == 0:
        assert a == 1
        return 1, 0
    if m == 1:
        return 0, -1
    s = pow(a, -1, m)
    return s, (a*s-1)//m


def witness(r, v):
    a, m = r; p, q = v
    sr, tr = bezout(a, m); sv, tv = bezout(p, q)
    rhs, coef = q*sr-m*sv, m*q
    g = gcd(coef, N)
    if rhs % g:
        return None
    if coef:
        mod = N//g
        t0 = (rhs//g)*pow(coef//g, -1, mod) % mod if mod > 1 else 0
        k = (rhs-coef*t0)//(coef*mod)
        choices = [t0+j*mod for j in (k, k+1)]
    else:
        choices = [0]
    def matrix(t):
        return [p*sr-m*(p*t+tv), -p*tr+a*(p*t+tv),
                q*sr-m*(q*t+sv), -q*tr+a*(q*t+sv)]
    t = min(choices, key=lambda t: (abs(matrix(t)[2]), abs(matrix(t)[3]), t))
    A, B, C, D = matrix(t)
    assert A*D-B*C == 1 and C % N == 0
    assert q*(A*a+B*m) == p*(C*a+D*m)
    if C:
        tau = [F(-D, C), F(1, abs(C))]
        image = [F(A, C), F(1, abs(C))]
    else:
        tau, image = [F(0), F(1)], [F(B, D), F(1)]
    # For C=0, determinant one forces A=D=+/-1: exact translation.
    zero = C == 0
    return {'source': list(r), 'target': list(v), 'bezout_source': [sr, tr],
            'bezout_target': [sv, tv], 't': t, 'matrix': [A, B, C, D],
            'inverse': [D, -B, -C, A], 'tau': list(map(str, tau)),
            'image': list(map(str, image)), 'zero_translation': str(F(B, D)) if zero else None}


def key(point):
    x, y = map(F, point)
    shift = (x+F(1, 2)).__floor__()
    return (x-shift, y), shift


def cutoff(y, radius):
    def works(H):
        return F(1, 1 << (6*H*y).__floor__())/(6*y) <= radius
    lo, hi = -1, 1
    while not works(hi):
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if works(mid): hi = mid
        else: lo = mid
    return hi


def build():
    source = HERE/'presentation.json'
    upstream = HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json'
    pres = json.loads(source.read_text()); old = json.loads(upstream.read_text())
    assert pres['inputs'] == {'N': N, 'P': []}
    domain = sorted({tuple(c) for pair in pres['endpoints'] for c in pair},
                    key=lambda c: (c[1], abs(c[0]), c[0]))
    assert domain[0] == (1, 0)
    representatives, assignments = [], []
    for r in domain:
        for i, s in enumerate(representatives):
            transport = witness(s, r)
            if transport is not None:
                break
        else:
            i = len(representatives); representatives.append(r)
            transport = witness(r, r)
        assignments.append({'endpoint': list(r), 'representative_id': i,
                            'transport': transport})
    closures = []
    for s in representatives:
        if s[1] == 0:
            closures.append({'representative': list(s), 'transports': []})
            continue
        r = F(*s); assert gcd(r.denominator, 37) == 1
        vs = [37*r]+[(r+j)/37 for j in range(37)]
        closures.append({'representative': list(s), 'transports': [
            witness(s, (v.numerator, v.denominator)) for v in vs]})
    all_transports = [a['transport'] for a in assignments]+[
        t for closure in closures for t in closure['transports']]
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
        if t['zero_translation'] is not None:
            return []
        i, j = t['primitive_ids']
        return [[i, str(-weight)], [j, str(weight)]]
    assignment_index = {tuple(a['endpoint']): i for i, a in enumerate(assignments)}
    generators = []
    for pair in pres['endpoints']:
        occ, ids = [], []
        for endpoint, sign in zip(pair, (-1, 1)):
            i = assignment_index[tuple(endpoint)]; ids.append(i)
            a = assignments[i]
            # P(endpoint)=P(rep)+P(image)-P(tau).
            occ.extend(occurrence(a['transport'], F(sign)))
            # P(rep)=(sum(P(tau)-P(image)))/h, h=48.
            for t in closures[a['representative_id']]['transports']:
                occ.extend(occurrence(t, -F(sign, old['h'])))
        combined = {}
        for j, w in occ:
            combined[j] = combined.get(j, F(0))+F(w)
        generators.append({'endpoints': pair, 'assignment_ids': ids,
                           'occurrences': occ,
                           'combined': [[j, str(w)] for j, w in sorted(combined.items()) if w],
                           'absolute_occurrence_weight': str(sum((abs(F(w)) for _, w in occ), F(0)))})
    omega_lower = F(old['period']['total'][0], old['scale'])
    W = max(F(row['absolute_occurrence_weight']) for row in generators)
    budget = F(1, 1 << 38)
    radius = budget*omega_lower/(2*W)
    primitives = []
    for x, y in keys:
        H = cutoff(y, radius)
        R = F(1, 1 << (6*H*y).__floor__())/(6*y)
        primitives.append({'x_reduced': str(x), 'y': str(y), 'H': H, 'tail_radius': str(R)})
    for row in generators:
        width = sum((2*abs(F(w))*F(primitives[j]['tail_radius'])/omega_lower
                     for j, w in row['occurrences']), F(0))
        row['normalized_tail_width'] = str(width)
    worst = max(range(len(primitives)), key=lambda i: primitives[i]['H'])
    return {'schema': 'conductor36-cusp-compression-plan-v1',
            'presentation_sha256': sha256(source.read_bytes()).hexdigest(),
            'audited_analytic_sha256': sha256(upstream.read_bytes()).hexdigest(),
            'ell': 37, 'h': old['h'], 'omega_lower': str(omega_lower),
            'tail_budget': str(budget), 'maximum_occurrence_weight': str(W),
            'primitive_radius_budget': str(radius),
            'domain': list(map(list, domain)), 'representatives': list(map(list, representatives)),
            'assignments': assignments, 'closures': closures, 'generators': generators,
            'primitives': primitives, 'summary': {'generators': len(generators),
                'endpoint_occurrences': sum(len(row) for row in pres['endpoints']),
                'distinct_endpoints': len(domain), 'representatives': len(representatives),
                'endpoint_transports': len(assignments),
                'closing_transports': sum(len(c['transports']) for c in closures),
                'zero_translations': sum(t['zero_translation'] is not None for t in all_transports),
                'points': len(keys), 'max_H': primitives[worst]['H'],
                'Fourier_terms': sum(p['H'] for p in primitives), 'worst_primitive_id': worst,
                'max_normalized_tail_width': str(max(F(g['normalized_tail_width']) for g in generators))}}


if __name__ == '__main__':
    data = build()
    destination = HERE/'compressed_plan.json'
    destination.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print('compressed plan', data['summary'], 'required: max_H<=4860; terms<=1000000; width<=2^-38',
          'certificate=', destination)
