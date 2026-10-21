#!/usr/bin/env python3
"""Complete endpoint/transport plan, prior to expensive finite evaluation."""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent


def bezout(a, b):
    if b == 1:
        return 0, -1
    s = pow(a, -1, b)
    return s, (a*s-1)//b


def transport(r, v):
    a, m = r.numerator, r.denominator
    p, q = v.numerator, v.denominator
    sr, tr = bezout(a, m)
    sv, tv = bezout(p, q)
    rhs, coefficient = q*sr-m*sv, m*q
    common = gcd(coefficient, 36)
    assert rhs % common == 0
    modulus = 36//common
    t0 = (rhs//common)*pow(coefficient//common, -1, modulus) % modulus if modulus > 1 else 0
    # All congruence solutions t=t0+k*modulus; choose minimal |C|.
    k0 = (rhs-coefficient*t0)//(coefficient*modulus)
    choices = []
    for k in (k0, k0+1):
        t = t0+k*modulus
        A = p*sr-m*(p*t+tv)
        B = -p*tr+a*(p*t+tv)
        C = q*sr-m*(q*t+sv)
        D = -q*tr+a*(q*t+sv)
        choices.append((abs(C), abs(D), t, [A, B, C, D]))
    _, _, t, matrix = min(choices)
    A, B, C, D = matrix
    assert A*D-B*C == 1 and C % 36 == 0
    assert C*a+D*m != 0 and F(A*a+B*m, C*a+D*m) == v
    if C:
        tau = [F(-D, C), F(1, abs(C))]
        image = [F(A, C), F(1, abs(C))]
    else:
        tau, image = [F(0), F(1)], [F(B, D), F(1)]
    return {'v': str(v), 'bezout_r': [sr, tr], 'bezout_v': [sv, tv],
            't': t, 'matrix': matrix, 'tau': list(map(str, tau)),
            'image': list(map(str, image))}


def truncation(y):
    # Binary search for the first H giving the same audited full tail bound.
    def works(H):
        return F(1, 2**((6*H*y).__floor__()))/(6*y) <= F(1, 2**38)
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
    presentation = json.loads(source.read_text())
    assert presentation['inputs'] == {'N': 36, 'P': []}
    endpoints = presentation['endpoints']
    cusps = sorted({F(p, q) for pair in endpoints for p, q in pair if q})
    assert all(gcd(37, r.denominator) == 1 for r in cusps)
    rows, points = [], {}
    for r in cusps:
        vs = [37*r]+[(r+j)/37 for j in range(37)]
        transports = [transport(r, v) for v in vs]
        for row in transports:
            for field in ('tau', 'image'):
                x, y = map(F, row[field])
                x -= (x+F(1, 2)).__floor__()
                points[(x, y)] = truncation(y)
        rows.append({'r': str(r), 'transports': transports})
    primitives = [{'x_reduced': str(x), 'y': str(y), 'H': H}
                  for (x, y), H in sorted(points.items())]
    index = {key: i for i, key in enumerate(sorted(points))}
    for cusp in rows:
        for row in cusp['transports']:
            row['primitive_ids'] = []
            for field in ('tau', 'image'):
                x, y = map(F, row[field]); x -= (x+F(1, 2)).__floor__()
                row['primitive_ids'].append(index[(x, y)])
    data = {'schema': 'conductor36-endpoint-plan-v1',
            'presentation_sha256': sha256(source.read_bytes()).hexdigest(),
            'ell': 37, 'endpoints': endpoints, 'cusps': rows,
            'primitives': primitives,
            'T': max(37, max(points.values())),
            'summary': {'generators': len(endpoints), 'finite_cusps': len(cusps),
                        'transports': 38*len(cusps), 'points': len(points),
                        'Fourier_terms': sum(points.values()),
                        'max_abs_C': max(abs(t['matrix'][2]) for row in rows for t in row['transports'])}}
    return data


if __name__ == '__main__':
    data = build()
    destination = HERE/'plan.json'
    destination.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print('complete plan', data['summary'], 'T=', data['T'], 'path=', destination)
