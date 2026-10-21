#!/usr/bin/env python3
"""Fixed L028/L039/L040 calibration; existing evidence is read-only."""
import hashlib
import json
from fractions import Fraction as F
from math import gcd, lcm
from pathlib import Path

ROOT = Path('scripts/conductor-eleven')
OUT = ROOT/'calibrated-symbols/certificate.json'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def build():
    audit = load(ROOT/'critical-audit/manifest.json')
    twist_audit = load(ROOT/'twist-five/critical-audit/audit.json')
    hashes = dict(audit['input_program_hashes'])
    hashes.update({str(ROOT/'twist-five'/name): value
                   for name, value in twist_audit['source_sha256'].items()})
    hashes[str(ROOT/'twist-five/critical-audit/independent-enclosure.json')] = twist_audit['independent_enclosure_sha256']
    assert all(sha(path) == value for path, value in hashes.items())
    for path in (ROOT/'critical-audit/manifest.json', ROOT/'twist-five/critical-audit/audit.json'):
        hashes[str(path)] = sha(path)
    assert not audit['failures'] and all(audit['checks'].values())
    assert not twist_audit['failures'] and twist_audit['q'] == '5'
    assert twist_audit['original_inputs_unchanged'] is True
    base, dual = load(ROOT/'structural-certificate.json'), load(ROOT/'dual-certificate.json')
    isolation = load(ROOT/'twist-five/certificate.json')['attempts'][0]['isolation']
    assert isolation['isolated'] and isolation['candidates'] == ['5']
    assert dual['bindings']['structural_sha256'] == sha(ROOT/'structural-certificate.json')
    assert dual['bindings']['arithmetic_sha256'] == sha(ROOT/'arithmetic-input.json')
    assert dual['arithmetic']['model'] == [0, -1, 1, -10, -20]
    assert base['inputs'] == {'N': 11, 'P': [2]}
    pr = base['presentation']
    n, s, dimension = 11, pr['s'], pr['d']
    assert (s, pr['r'], dimension) == (12, 9, 3)
    coords, lifts = pr['generator_coordinates'], base['cosets']['lifts']
    reps = base['cosets']['representatives']
    phi = [F(x) for x in dual['line']['v']]
    x = [sum(F(a)*b for a, b in zip(row, phi)) for row in coords]
    assert x == [F(a) for a in dual['generator_values']['entries'][0]]

    def canonical(p, q):
        if q == 0:
            assert p
            return [1, 0]
        common = gcd(p, q)
        p, q = p//common, q//common
        return [p, q] if q > 0 else [-p, -q]

    def path(a):
        numerator, denominator, digits = a, 5, []
        while denominator:
            digit = numerator//denominator
            digits.append(digit)
            numerator, denominator = denominator, numerator-digit*denominator
        p0, q0, p1, q1 = 0, 1, 1, 0
        segments, raw = [], [0]*s
        for digit in digits:
            p2, q2 = digit*p1+p0, digit*q1+q0
            det = p2*q1-p1*q2
            assert abs(det) == 1
            h = [det*p2, p1, det*q2, q1]
            aa, bb, cc, dd = h
            rep = [1, dd*pow(cc % n, -1, n) % n] if cc % n else [0, 1]
            index = reps.index(rep)
            la, lb, lc, ld = lifts[index]
            gamma = [aa*ld-bb*lc, -aa*lb+bb*la,
                     cc*ld-dd*lc, -cc*lb+dd*la]
            assert gamma[2] % n == 0
            segments.append({'start': canonical(p1, q1), 'end': canonical(p2, q2),
                             'lift': h, 'coset': index, 'Gamma0_reduction': gamma})
            raw[index] += 1
            p0, q0, p1, q1 = p1, q1, p2, q2
        assert canonical(p1, q1) == [a, 5]
        quotient = [sum(raw[i]*coords[i][j] for i in range(s)) for j in range(dimension)]
        return {'a': a, 'chi': 1 if a in (1, 4) else -1,
                'start': [1, 0], 'end': [a, 5], 'continued_fraction': digits,
                'segments': segments, 'raw': raw, 'coordinates': quotient,
                'phi_value': str(sum(F(t)*u for t, u in zip(quotient, phi)))}

    paths = [path(a) for a in range(1, 5)]
    raw = [sum(t['chi']*t['raw'][i] for t in paths) for i in range(s)]
    quotient = [sum(t['chi']*t['coordinates'][j] for t in paths) for j in range(dimension)]
    d = sum(F(a)*b for a, b in zip(quotient, phi))
    assert d and d == sum(t['chi']*F(t['phi_value']) for t in paths)
    scale = F(5)/d
    y = [scale*value for value in x]
    saturated = list(map(list, zip(*pr['K']['entries'])))
    residuals = {name: [str(sum(F(a)*b for a, b in zip(row, y))) for row in rows]
                 for name, rows in [('Manin', base['A']['entries']), ('saturated', saturated)]}
    assert all(F(z) == 0 for group in residuals.values() for z in group)
    denominator = lcm(*(v.denominator for v in y))
    remaining, prime, factors = denominator, 2, []
    while prime*prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            factors.append([prime, exponent])
        prime += 1
    if remaining > 1:
        factors.append([remaining, 1])
    witnesses = [[p, e, next(i for i, v in enumerate(y) if v.denominator % (p**e) == 0)]
                 for p, e in factors]
    assert sum(F(a)*b for a, b in zip(raw, y)) == 5
    cert = {'input_sha256': hashes, 'instance': {'model': [0, -1, 1, -10, -20],
            'level': n, 'twist': 5, 'q': '5', 'generator_count': s, 'relative_dimension': dimension},
            'paths': paths, 'G5': {'raw': raw, 'coordinates': quotient, 'phi_value': str(d)},
            'scale': str(scale), 'basis_functional': [str(scale*t) for t in phi],
            'integral_generator_values': [str(t) for t in y], 'relation_residuals': residuals,
            'denominator': {'lcm': denominator, 'prime_factorization': factors,
                            'max_valuation_generator_witnesses': witnesses,
                            'all_scaled_values_integral': all((denominator*t).denominator == 1 for t in y)},
            'failures': []}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2)+'\n')
    print('d', d, 'scale', scale, 'paths actual/required', len(paths), '/4',
          'generators actual/required', len(y), '/12', 'common denominator', denominator,
          'factorization', factors, 'failures', cert['failures'], 'certificate', OUT)


if __name__ == '__main__':
    try:
        build()
    except Exception as error:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.with_suffix('.build-failure.json').write_text(json.dumps(
            {'failures': [type(error).__name__+': '+str(error)]}, indent=2)+'\n')
        raise
