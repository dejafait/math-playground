#!/usr/bin/env python3
"""Fixed L028 specialization. Exact arithmetic; never modifies input evidence."""
import hashlib
import json
from fractions import Fraction as Q
from math import gcd, lcm
from pathlib import Path

OUT = Path('scripts/calibrated-symbols/certificate.json')
INPUTS = [f'scripts/{topic}/{name}.json'
          for topic in ('relative-t2', 'twist-five')
          for name in ('certificate', 'verification', 'audit')]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def factor(number):
    result = []
    prime = 2
    while prime*prime <= number:
        exponent = 0
        while number % prime == 0:
            number //= prime
            exponent += 1
        if exponent:
            result.append([prime, exponent])
        prime += 1
    if number > 1:
        result.append([number, 1])
    return result


def build():
    data = {path: json.loads(Path(path).read_text()) for path in INPUTS}
    hashes = {path: digest(path) for path in INPUTS}
    base = data[INPUTS[0]]
    for path in INPUTS[1:3]:
        assert data[path]['certificate_sha256'] == hashes[INPUTS[0]]
        assert not data[path]['failures'] and all(data[path]['checks'].values())
    for path in INPUTS[4:6]:
        assert data[path]['certificate_sha256'] == hashes[INPUTS[3]]
    assert data[INPUTS[4]]['finite_arithmetic_verified']
    assert all(not r['failures'] and Q(r['q']) == 4
               for r in data[INPUTS[4]]['reports'])
    assert not data[INPUTS[5]]['failures']
    assert data[INPUTS[5]]['base_certificate_sha256'] == hashes[INPUTS[0]]
    assert Q(data[INPUTS[5]]['q']) == 4
    twist = data[INPUTS[3]]
    isolation = twist['attempts'][twist['selected_attempt']]['isolation']
    assert isolation['isolated'] and isolation['candidates'] == ['4']
    assert not base['failures'] and base['arithmetic']['conductor'] == 389

    n, s = 389, 390
    presentation = base['presentation']
    coordinates = presentation['integral_generator_coordinates']
    dimension = presentation['dimension']
    lifts = base['SL2_lifts']
    phi = [Q(x) for x in base['integration_line']['basis_functional']]
    x = [Q(value) for value in base['integration_line']['integral_generator_values']]
    assert dimension == 65 and len(x) == s
    assert x == [sum(Q(a)*b for a, b in zip(row, phi)) for row in coordinates]

    def canonical(p, q):
        if q == 0:
            assert p
            return [1, 0]
        divisor = gcd(p, q)
        p, q = p//divisor, q//divisor
        return [p, q] if q > 0 else [-p, -q]

    def path(a):
        numerator, denominator = a, 5
        digits = []
        while denominator:
            digit = numerator//denominator
            digits.append(digit)
            numerator, denominator = denominator, numerator-digit*denominator
        p0, q0, p1, q1 = 0, 1, 1, 0
        segments, raw = [], [0]*s
        for digit in digits:
            p2, q2 = digit*p1+p0, digit*q1+q0
            determinant = p2*q1-p1*q2
            assert abs(determinant) == 1
            h = [determinant*p2, p1, determinant*q2, q1]
            aa, bb, cc, dd = h
            index = (dd*pow(cc % n, -1, n)) % n if cc % n else n
            la, lb, lc, ld = lifts[index]
            gamma = [aa*ld-bb*lc, -aa*lb+bb*la,
                     cc*ld-dd*lc, -cc*lb+dd*la]
            assert gamma[2] % n == 0
            segments.append({'start': canonical(p1, q1), 'end': canonical(p2, q2),
                             'lift': h, 'coset': index, 'Gamma0_reduction': gamma})
            raw[index] += 1
            p0, q0, p1, q1 = p1, q1, p2, q2
        assert canonical(p1, q1) == [a, 5]
        quotient = [sum(raw[i]*coordinates[i][j] for i in range(s))
                    for j in range(dimension)]
        value = sum(Q(t)*u for t, u in zip(quotient, phi))
        return {'a': a, 'chi': 1 if a in (1, 4) else -1,
                'start': [1, 0], 'end': [a, 5], 'continued_fraction': digits,
                'segments': segments, 'raw': raw, 'coordinates': quotient,
                'phi_value': str(value)}

    paths = [path(a) for a in range(1, 5)]
    raw = [sum(t['chi']*t['raw'][i] for t in paths) for i in range(s)]
    quotient = [sum(t['chi']*t['coordinates'][j] for t in paths)
                for j in range(dimension)]
    d = sum(Q(a)*b for a, b in zip(quotient, phi))
    assert d == sum(t['chi']*Q(t['phi_value']) for t in paths)
    assert d
    scale = Q(4)/d
    y = [scale*value for value in x]
    residuals = {name: [str(sum(Q(a)*b for a, b in zip(row, y))) for row in rows]
                 for name, rows in [('Manin', base['relations']),
                                    ('saturated', presentation['saturated_relation_basis'])]}
    assert all(Q(z) == 0 for group in residuals.values() for z in group)
    denominator = lcm(*(value.denominator for value in y))
    factors = factor(denominator)
    witnesses = [[prime, exponent, next(i for i, value in enumerate(y)
                  if value.denominator % (prime**exponent) == 0)]
                 for prime, exponent in factors]
    assert sum(Q(a)*b for a, b in zip(raw, y)) == 4
    cert = {'input_sha256': hashes, 'instance': {'model': [0, 1, 1, -2, 0],
            'level': n, 'twist': 5, 'q': '4', 'generator_count': s,
            'relative_dimension': dimension}, 'paths': paths,
            'G5': {'raw': raw, 'coordinates': quotient, 'phi_value': str(d)},
            'scale': str(scale), 'basis_functional': [str(scale*t) for t in phi],
            'integral_generator_values': [str(t) for t in y],
            'relation_residuals': residuals,
            'denominator': {'lcm': denominator, 'prime_factorization': factors,
                            'max_valuation_generator_witnesses': witnesses,
                            'all_scaled_values_integral':
                            all((denominator*t).denominator == 1 for t in y)},
            'failures': []}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2)+'\n')
    print('d', d, 'scale', scale, 'generators', len(y), 'required', s,
          'common denominator', denominator, 'factorization', factors,
          'failures', cert['failures'], 'certificate', OUT)


if __name__ == '__main__':
    build()
